from __future__ import annotations

import csv
import hashlib
import json
import logging
import re
import shutil
import time
from pathlib import Path
from typing import Any

import requests
import yaml

from src.classifier import classify_repo
from src.providers import (
    get_github_repository,
    get_gitlab_project,
    github_get_file,
    github_get_readme,
    github_list_repository_paths,
    gitlab_get_file,
    gitlab_list_repository_paths,
    parse_repo_url,
    polite_sleep,
    search_github_repositories,
    search_gitlab_projects,
)
from src.render_readme import write_readme
from src.render_site import write_site
from src.scoring import passes_prefilter, score_text

LOGGER = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

CACHE_PATH = Path("data/repo_cache.json")
REVIEW_ROOT = Path("to_review")
REVIEW_PARTS = ["part_A", "part_B", "part_C", "part_D"]

README_CANDIDATES = ["README.md", "README.rst", "README.txt", "Readme.md", "readme.md"]
EXTRA_FILES = [
    "requirements.txt",
    "pyproject.toml",
    "environment.yml",
    "environment.yaml",
    "setup.py",
    "docs/index.md",
    "docs/README.md",
]

CODE_EXTENSIONS = {
    ".py", ".ipynb", ".m", ".jl", ".r", ".cpp", ".cc", ".c", ".h", ".hpp",
    ".java", ".kt", ".scala", ".go", ".rs", ".js", ".ts", ".tsx", ".jsx",
    ".php", ".rb", ".swift", ".cs", ".lua", ".sh", ".zsh", ".ps1"
}

CODE_FILENAMES = {
    "setup.py", "pyproject.toml", "requirements.txt", "environment.yml", "environment.yaml",
    "pom.xml", "build.gradle", "gradlew", "makefile", "cmakelists.txt",
    "package.json", "dockerfile", "snakefile"
}


def load_yaml(path: str) -> dict[str, Any]:
    file_path = Path(path)
    if not file_path.exists():
        return {}
    with open(file_path, "r", encoding="utf-8") as handle:
        return yaml.safe_load(handle) or {}


def safe_write_json(path: str | Path, payload: Any) -> None:
    file_path = Path(path)
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(json.dumps(payload, indent=2, ensure_ascii=False), encoding="utf-8")


def load_repo_cache() -> dict[str, dict[str, Any]]:
    if not CACHE_PATH.exists():
        return {}
    try:
        return json.loads(CACHE_PATH.read_text(encoding="utf-8"))
    except Exception:
        return {}


def save_repo_cache(cache: dict[str, dict[str, Any]]) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8")


def normalize_repo_name(full_name: str) -> str:
    text = full_name or ""
    text = text.replace("/", " ")
    text = text.replace("-", " ")
    text = text.replace("_", " ")
    return text


def count_words(text: str) -> int:
    return len(re.findall(r"\b\w+\b", text or ""))


def repo_has_code(paths: list[str]) -> bool:
    for path in paths:
        lower = path.lower()
        name = lower.split("/")[-1]
        if name in CODE_FILENAMES:
            return True
        if any(lower.endswith(ext) for ext in CODE_EXTENSIONS):
            return True
    return False


def coalesce(preferred: Any, fallback: Any) -> Any:
    if preferred is None:
        return fallback
    if isinstance(preferred, str) and not preferred.strip():
        return fallback
    if isinstance(preferred, list) and len(preferred) == 0:
        return fallback
    return preferred


def build_blob(
    full_name: str,
    description: str,
    topics: list[str],
    readme: str,
    extra: str,
) -> str:
    parts = [
        full_name or "",
        normalize_repo_name(full_name),
        description or "",
        " ".join(topics or []),
        readme or "",
        extra or "",
    ]
    return " ".join(parts)


def collect_github_text_and_paths(owner: str, repo: str, branch: str | None) -> tuple[str, str, list[str]]:
    paths = github_list_repository_paths(owner, repo, branch=branch)
    path_set = {p.lower() for p in paths}

    readme = github_get_readme(owner, repo)

    extra_chunks: list[str] = []
    for candidate in EXTRA_FILES:
        if candidate.lower() not in path_set:
            continue
        text = github_get_file(owner, repo, candidate)
        if text:
            extra_chunks.append(text[:4000])

    return readme[:12000], "\n\n".join(extra_chunks)[:12000], paths


def collect_gitlab_text_and_paths(project_id: int, default_branch: str | None) -> tuple[str, str, list[str]]:
    if not default_branch:
        return "", "", []

    readme = ""
    extra_chunks: list[str] = []

    for candidate in README_CANDIDATES:
        readme = gitlab_get_file(project_id, candidate, default_branch)
        if readme:
            break

    for candidate in EXTRA_FILES:
        if candidate in README_CANDIDATES and readme:
            continue
        text = gitlab_get_file(project_id, candidate, default_branch)
        if text:
            extra_chunks.append(text[:4000])

    paths = gitlab_list_repository_paths(project_id, default_branch)
    return readme[:12000], "\n\n".join(extra_chunks)[:12000], paths


def build_github_record(item: dict[str, Any], taxonomy: dict[str, Any], min_heuristic_score: int) -> dict[str, Any]:
    full_name = item["full_name"]
    owner, repo = full_name.split("/", 1)

    readme, extra, paths = collect_github_text_and_paths(owner, repo, item.get("default_branch"))
    blob = build_blob(full_name, item.get("description") or "", item.get("topics") or [], readme, extra)
    title_blob = normalize_repo_name(full_name)
    heuristic = score_text(blob, taxonomy, min_total=min_heuristic_score, title_blob=title_blob)

    return {
        "platform": "github",
        "full_name": full_name,
        "url": item["html_url"],
        "description": item.get("description") or "",
        "stars": item.get("stargazers_count", 0),
        "language": item.get("language"),
        "updated_at": item.get("updated_at"),
        "license": (item.get("license") or {}).get("spdx_id"),
        "topics": item.get("topics") or [],
        "readme_excerpt": readme,
        "extra_excerpt": extra,
        "readme_word_count": count_words(readme),
        "has_code": repo_has_code(paths),
        "repo_paths_sample": paths[:200],
        "is_fork": item.get("fork", False),
        "is_manual": False,
        "manual_source": None,
        "heuristic_strong_particle_hits": heuristic.strong_particle_hits,
        "heuristic_particle_hits": heuristic.particle_hits,
        "heuristic_support_hits": heuristic.support_hits,
        "heuristic_ai_hits": heuristic.ai_hits,
        "heuristic_negative_hits": heuristic.negative_hits,
        "heuristic_generic_radiotherapy_hits": heuristic.generic_radiotherapy_hits,
        "heuristic_title_strong_particle_hits": heuristic.title_strong_particle_hits,
        "heuristic_title_ai_hits": heuristic.title_ai_hits,
        "heuristic_total_score": heuristic.total_score,
        "heuristic_has_strong_particle_anchor": heuristic.has_strong_particle_anchor,
        "heuristic_passes": heuristic.passes,
        "heuristic_reasons": heuristic.reasons,
    }


def build_gitlab_record(item: dict[str, Any], taxonomy: dict[str, Any], min_heuristic_score: int) -> dict[str, Any]:
    project_id = item["id"]
    default_branch = item.get("default_branch")
    repo_name = item.get("path_with_namespace") or item.get("name_with_namespace") or str(project_id)

    readme, extra, paths = collect_gitlab_text_and_paths(project_id, default_branch)
    blob = build_blob(repo_name, item.get("description") or "", item.get("topics") or [], readme, extra)
    title_blob = normalize_repo_name(repo_name)
    heuristic = score_text(blob, taxonomy, min_total=min_heuristic_score, title_blob=title_blob)

    return {
        "platform": "gitlab",
        "full_name": repo_name,
        "url": item["web_url"],
        "description": item.get("description") or "",
        "stars": item.get("star_count", 0),
        "language": None,
        "updated_at": item.get("last_activity_at"),
        "license": None,
        "topics": item.get("topics") or [],
        "readme_excerpt": readme,
        "extra_excerpt": extra,
        "readme_word_count": count_words(readme),
        "has_code": repo_has_code(paths),
        "repo_paths_sample": paths[:200],
        "is_fork": bool(item.get("forked_from_project")),
        "is_manual": False,
        "manual_source": None,
        "heuristic_strong_particle_hits": heuristic.strong_particle_hits,
        "heuristic_particle_hits": heuristic.particle_hits,
        "heuristic_support_hits": heuristic.support_hits,
        "heuristic_ai_hits": heuristic.ai_hits,
        "heuristic_negative_hits": heuristic.negative_hits,
        "heuristic_generic_radiotherapy_hits": heuristic.generic_radiotherapy_hits,
        "heuristic_title_strong_particle_hits": heuristic.title_strong_particle_hits,
        "heuristic_title_ai_hits": heuristic.title_ai_hits,
        "heuristic_total_score": heuristic.total_score,
        "heuristic_has_strong_particle_anchor": heuristic.has_strong_particle_anchor,
        "heuristic_passes": heuristic.passes,
        "heuristic_reasons": heuristic.reasons,
    }


def apply_overrides(entries: list[dict[str, Any]], overrides: dict[str, Any]) -> list[dict[str, Any]]:
    excluded = set(overrides.get("exclude", []))
    included = set(overrides.get("include", []))
    notes = overrides.get("notes", {})
    tags = overrides.get("tags", {})

    result: list[dict[str, Any]] = []

    for entry in entries:
        if entry["url"] in excluded:
            continue
        if entry["url"] in included:
            entry["forced_include"] = True
        if entry["url"] in notes:
            entry["manual_note"] = notes[entry["url"]]
        if entry["url"] in tags:
            entry["manual_tags"] = tags[entry["url"]]
        result.append(entry)

    return result


def load_manual_seed_repos() -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []

    yaml_cfg = load_yaml("config/manual_seed_repos.yml")
    for repo in yaml_cfg.get("repos", []):
        url = (repo.get("url") or "").strip()
        if not url:
            continue

        rows.append({
            "url": url,
            "always_include": bool(repo.get("always_include", False)),
            "platform": repo.get("platform", "manual"),
            "full_name": repo.get("full_name", ""),
            "description": repo.get("description", ""),
            "language": repo.get("language"),
            "topics": repo.get("topics", []) or [],
            "note": repo.get("note", ""),
            "tags": repo.get("tags", []) or [],
            "stars": int(repo.get("stars", 0) or 0),
            "updated_at": repo.get("updated_at"),
            "license": repo.get("license"),
            "readme_excerpt": repo.get("readme_excerpt", ""),
            "has_code": bool(repo.get("has_code", True)),
        })

    csv_path = Path("data/manual_seed_repos.csv")
    if csv_path.exists():
        with open(csv_path, "r", encoding="utf-8-sig", newline="") as handle:
            reader = csv.DictReader(handle)
            for row in reader:
                url = (row.get("url") or "").strip()
                if not url:
                    continue

                tags = [x.strip() for x in (row.get("tags") or "").split(";") if x.strip()]
                topics = [x.strip() for x in (row.get("topics") or "").split(";") if x.strip()]
                always_include = str(row.get("always_include", "")).strip().lower() in {"1", "true", "yes", "y"}
                has_code = str(row.get("has_code", "true")).strip().lower() in {"1", "true", "yes", "y"}

                rows.append({
                    "url": url,
                    "always_include": always_include,
                    "platform": (row.get("platform") or "manual").strip(),
                    "full_name": (row.get("full_name") or "").strip(),
                    "description": (row.get("description") or "").strip(),
                    "language": (row.get("language") or "").strip() or None,
                    "topics": topics,
                    "note": (row.get("note") or "").strip(),
                    "tags": tags,
                    "stars": int((row.get("stars") or "0").strip() or 0),
                    "updated_at": (row.get("updated_at") or "").strip() or None,
                    "license": (row.get("license") or "").strip() or None,
                    "readme_excerpt": (row.get("readme_excerpt") or "").strip(),
                    "has_code": has_code,
                })

    deduped: dict[str, dict[str, Any]] = {}
    for row in rows:
        deduped[row["url"]] = row
    return list(deduped.values())


def merge_seed_overrides(live_record: dict[str, Any], seed: dict[str, Any]) -> dict[str, Any]:
    record = dict(live_record)

    record["platform"] = coalesce(record.get("platform"), seed.get("platform", "manual"))
    record["full_name"] = coalesce(record.get("full_name"), seed.get("full_name"))
    record["description"] = coalesce(record.get("description"), seed.get("description", ""))
    record["language"] = coalesce(record.get("language"), seed.get("language"))
    record["topics"] = coalesce(record.get("topics"), seed.get("topics", []) or [])
    record["stars"] = coalesce(record.get("stars"), int(seed.get("stars", 0) or 0))
    record["updated_at"] = coalesce(record.get("updated_at"), seed.get("updated_at"))
    record["license"] = coalesce(record.get("license"), seed.get("license"))
    record["readme_excerpt"] = coalesce(record.get("readme_excerpt"), seed.get("readme_excerpt", ""))
    record["has_code"] = record.get("has_code", bool(seed.get("has_code", True)))

    if seed.get("always_include"):
        record["forced_include"] = True
    if seed.get("note"):
        record["manual_note"] = seed["note"]
    if seed.get("tags"):
        record["manual_tags"] = seed.get("tags", []) or []

    record["is_manual"] = True
    record["manual_source"] = "live+yaml"
    return record


def build_manual_metadata_record(
    seed: dict[str, Any],
    taxonomy: dict[str, Any],
    min_heuristic_score: int,
) -> dict[str, Any] | None:
    if not seed.get("url"):
        return None

    full_name = seed.get("full_name") or seed["url"]
    description = seed.get("description") or ""
    topics = seed.get("topics") or []
    readme_excerpt = seed.get("readme_excerpt") or ""
    extra_excerpt = ""

    blob = build_blob(full_name, description, topics, readme_excerpt, extra_excerpt)
    title_blob = normalize_repo_name(full_name)
    heuristic = score_text(blob, taxonomy, min_total=min_heuristic_score, title_blob=title_blob)

    return {
        "platform": seed.get("platform", "manual"),
        "full_name": full_name,
        "url": seed["url"],
        "description": description,
        "stars": int(seed.get("stars", 0) or 0),
        "language": seed.get("language"),
        "updated_at": seed.get("updated_at"),
        "license": seed.get("license"),
        "topics": topics,
        "readme_excerpt": readme_excerpt,
        "extra_excerpt": extra_excerpt,
        "readme_word_count": count_words(readme_excerpt),
        "has_code": bool(seed.get("has_code", True)),
        "repo_paths_sample": [],
        "is_fork": False,
        "is_manual": True,
        "manual_source": "yaml-only",
        "forced_include": bool(seed.get("always_include", False)),
        "manual_note": seed.get("note", ""),
        "manual_tags": seed.get("tags", []) or [],
        "heuristic_strong_particle_hits": heuristic.strong_particle_hits,
        "heuristic_particle_hits": heuristic.particle_hits,
        "heuristic_support_hits": heuristic.support_hits,
        "heuristic_ai_hits": heuristic.ai_hits,
        "heuristic_negative_hits": heuristic.negative_hits,
        "heuristic_generic_radiotherapy_hits": heuristic.generic_radiotherapy_hits,
        "heuristic_title_strong_particle_hits": heuristic.title_strong_particle_hits,
        "heuristic_title_ai_hits": heuristic.title_ai_hits,
        "heuristic_total_score": heuristic.total_score,
        "heuristic_has_strong_particle_anchor": heuristic.has_strong_particle_anchor,
        "heuristic_passes": heuristic.passes,
        "heuristic_reasons": heuristic.reasons,
    }


def build_live_manual_seed_record(
    seed: dict[str, Any],
    taxonomy: dict[str, Any],
    min_heuristic_score: int,
) -> dict[str, Any] | None:
    parsed = parse_repo_url(seed.get("url", ""))
    if not parsed:
        return None

    platform, repo_path = parsed

    try:
        if platform == "github":
            owner, repo = repo_path.split("/", 1)
            item = get_github_repository(owner, repo)
            live_record = build_github_record(item, taxonomy, min_heuristic_score)
            return merge_seed_overrides(live_record, seed)

        if platform == "gitlab":
            item = get_gitlab_project(repo_path)
            live_record = build_gitlab_record(item, taxonomy, min_heuristic_score)
            return merge_seed_overrides(live_record, seed)
    except Exception as exc:
        LOGGER.warning("Live fetch failed for manual seed %s: %s", seed.get("url"), exc)

    return None


def build_manual_seed_record(
    seed: dict[str, Any],
    taxonomy: dict[str, Any],
    min_heuristic_score: int,
) -> dict[str, Any] | None:
    live_record = build_live_manual_seed_record(seed, taxonomy, min_heuristic_score)
    if live_record is not None:
        return live_record

    if seed.get("full_name") and seed.get("description"):
        return build_manual_metadata_record(seed, taxonomy, min_heuristic_score)

    LOGGER.warning(
        "Skipping manual seed without sufficient metadata after live fetch failed: %s "
        "(need at least full_name and description for YAML fallback)",
        seed.get("url", "<missing-url>"),
    )
    return None


def load_json(path: str | Path) -> Any:
    file_path = Path(path)
    if not file_path.exists():
        return []
    try:
        return json.loads(file_path.read_text(encoding="utf-8"))
    except Exception:
        return []


def derive_gitlab_queries_from_main_queries(main_queries: list[str], taxonomy: dict[str, Any]) -> list[str]:
    strong_terms = taxonomy.get("strong_particle_therapy_terms", [])
    derived: list[str] = []

    for query in main_queries:
        lowered = query.lower()
        for term in strong_terms:
            if term.lower() in lowered:
                derived.append(term)

    seen = set()
    result = []
    for q in derived:
        if q not in seen:
            seen.add(q)
            result.append(q)
    return result


def discover_github_repositories(
    queries: list[str],
    taxonomy: dict[str, Any],
    settings: dict[str, Any],
    cache: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    scraper_cfg = settings.get("scraper", {})
    github_max_results = int(scraper_cfg.get("github_max_results", 1000))
    sleep_seconds = float(scraper_cfg.get("polite_sleep_seconds", 0.35))
    min_heuristic_score = int(scraper_cfg.get("min_heuristic_score", 4))

    seen: dict[str, dict[str, Any]] = {}
    hits = 0
    fetched = 0

    for query in queries:
        LOGGER.info("GitHub query: %s", query)
        try:
            github_items = search_github_repositories(query, max_results=github_max_results)
            LOGGER.info("GitHub returned %d items for query %r", len(github_items), query)

            for item in github_items:
                url = item.get("html_url")
                if not url:
                    continue

                if url in cache:
                    hits += 1
                    seen.setdefault(url, cache[url])
                    continue

                record = build_github_record(item, taxonomy, min_heuristic_score)
                cache[url] = record
                fetched += 1

                current = seen.get(url)
                if current is None or record["heuristic_total_score"] > current["heuristic_total_score"]:
                    seen[url] = record

            save_repo_cache(cache)
            time.sleep(max(1.5, sleep_seconds))
        except Exception as exc:
            LOGGER.warning("GitHub query failed for %r: %s", query, exc)

    LOGGER.info("GitHub: %d from cache, %d newly fetched", hits, fetched)
    return list(seen.values())


def discover_gitlab_repositories(
    queries: list[str],
    taxonomy: dict[str, Any],
    settings: dict[str, Any],
    cache: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    scraper_cfg = settings.get("scraper", {})
    gitlab_max_results = int(scraper_cfg.get("gitlab_max_results", 1000))
    sleep_seconds = float(scraper_cfg.get("polite_sleep_seconds", 0.35))
    min_heuristic_score = int(scraper_cfg.get("min_heuristic_score", 4))

    seen: dict[str, dict[str, Any]] = {}
    hits = 0
    fetched = 0

    for query in queries:
        LOGGER.info("GitLab query: %s", query)
        try:
            gitlab_items = search_gitlab_projects(query, gitlab_max_results)
            LOGGER.info("GitLab returned %d items for query %r", len(gitlab_items), query)

            for item in gitlab_items:
                url = item.get("web_url")
                if not url:
                    continue

                if url in cache:
                    hits += 1
                    seen.setdefault(url, cache[url])
                    continue

                record = build_gitlab_record(item, taxonomy, min_heuristic_score)
                cache[url] = record
                fetched += 1

                current = seen.get(url)
                if current is None or record["heuristic_total_score"] > current["heuristic_total_score"]:
                    seen[url] = record

            save_repo_cache(cache)
            time.sleep(max(1.0, sleep_seconds))
        except Exception as exc:
            LOGGER.warning("GitLab query failed for %r: %s", query, exc)

    LOGGER.info("GitLab: %d from cache, %d newly fetched", hits, fetched)
    return list(seen.values())


def readme_hash(text: str) -> str:
    normalized = re.sub(r"\s+", " ", (text or "").lower()).strip()
    if len(normalized) < 200:
        return ""
    return hashlib.sha256(normalized.encode("utf-8")).hexdigest()


def merge_and_sort_candidates(*candidate_groups: list[dict[str, Any]]) -> list[dict[str, Any]]:
    seen: dict[str, dict[str, Any]] = {}

    for group in candidate_groups:
        for row in group:
            current = seen.get(row["url"])
            if current is None or row["heuristic_total_score"] > current["heuristic_total_score"]:
                seen[row["url"]] = row

    by_popularity = sorted(
        seen.values(),
        key=lambda row: (row.get("stars", 0), row["heuristic_total_score"]),
        reverse=True,
    )

    kept: list[dict[str, Any]] = []
    seen_hashes: set[str] = set()
    dropped_duplicates = 0

    for row in by_popularity:
        digest = readme_hash(row.get("readme_excerpt", ""))

        if digest and digest in seen_hashes and not row.get("forced_include", False):
            dropped_duplicates += 1
            LOGGER.info("Duplicate README, dropping %s", row.get("full_name"))
            continue

        if digest:
            seen_hashes.add(digest)
        kept.append(row)

    if dropped_duplicates:
        LOGGER.info("Dropped %d repositories with duplicate READMEs", dropped_duplicates)

    return sorted(
        kept,
        key=lambda row: (
            row["heuristic_total_score"],
            row["heuristic_strong_particle_hits"] + row["heuristic_title_strong_particle_hits"],
            row["heuristic_ai_hits"] + row["heuristic_title_ai_hits"],
            row.get("stars", 0),
        ),
        reverse=True,
    )


def passes_quality_filters(repo: dict[str, Any], settings: dict[str, Any]) -> bool:
    scraper_cfg = settings.get("scraper", {})
    require_code = bool(scraper_cfg.get("require_code", True))
    min_readme_words = int(scraper_cfg.get("min_readme_words", 100))
    bypass = bool(scraper_cfg.get("force_include_bypasses_quality_filters", True))

    if repo.get("forced_include", False) and bypass:
        return True
    if require_code and not repo.get("has_code", False):
        return False
    if repo.get("readme_word_count", 0) < min_readme_words:
        return False
    return True


SKIP_IMAGE_HOSTS = ("shields.io", "badge", "codecov", "travis-ci", "appveyor")
PREFER_IMAGE = ("logo", "banner", "title", "icon")
IMAGE_MIME = {
    "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
    "gif": "image/gif", "svg": "image/svg+xml", "webp": "image/webp",
}

MD_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
HTML_IMAGE = re.compile(r'<img[^>]+src=["\']([^"\']+)')
RST_IMAGE = re.compile(r"image::\s*(\S+)")


def slugify_name(full_name: str) -> str:
    name = (full_name or "").split("/")[-1]
    return re.sub(r"[^A-Za-z0-9]+", "-", name).strip("-").lower()


def candidate_images(readme: str) -> list[str]:
    urls: list[str] = []
    for pattern in (MD_IMAGE, HTML_IMAGE, RST_IMAGE):
        urls.extend(pattern.findall(readme or ""))

    clean: list[str] = []
    for url in urls:
        low = url.lower()
        if any(host in low for host in SKIP_IMAGE_HOSTS):
            continue
        if not any(low.split("?")[0].endswith("." + ext) for ext in IMAGE_MIME):
            continue
        if url not in clean:
            clean.append(url)

    clean.sort(key=lambda u: 0 if any(p in u.lower() for p in PREFER_IMAGE) else 1)
    return clean


def absolute_image_url(url: str, repo_url: str) -> str:
    if url.startswith("http"):
        return url
    raw = (repo_url or "").replace("github.com", "raw.githubusercontent.com").rstrip("/")
    return raw + "/HEAD/" + url.lstrip("./")


def download_image(readme: str, repo_url: str, target_dir: Path, stem: str) -> str | None:
    for candidate in candidate_images(readme)[:4]:
        url = absolute_image_url(candidate, repo_url)
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
        except Exception:
            continue

        if len(response.content) > 5_000_000 or len(response.content) < 500:
            continue

        ext = url.split("?")[0].rsplit(".", 1)[-1].lower()
        if ext not in IMAGE_MIME:
            continue

        path = target_dir / (stem + "." + ext)
        path.write_bytes(response.content)
        return url

    return None


def build_review_entry(repo: dict[str, Any], image_source: str | None) -> dict[str, Any]:
    return {
        "review": {
            "approved": False,
            "reviewer": "",
            "note": "",
        },
        "name": repo.get("full_name"),
        "url": repo.get("url"),
        "platform": repo.get("platform"),
        "description": repo.get("description") or "",
        "license": repo.get("license"),
        "language": repo.get("language"),
        "keywords": repo.get("topics") or [],
        "stars": repo.get("stars", 0),
        "updated_at": repo.get("updated_at"),
        "image_source": image_source,
        "heuristic_total_score": repo.get("heuristic_total_score"),
        "heuristic_reasons": repo.get("heuristic_reasons") or [],
        "readme_excerpt": repo.get("readme_excerpt") or "",
    }


def write_review_tree(included: list[dict[str, Any]], fetch_images: bool = True) -> None:
    if REVIEW_ROOT.exists():
        shutil.rmtree(REVIEW_ROOT)

    for part in REVIEW_PARTS:
        (REVIEW_ROOT / part).mkdir(parents=True, exist_ok=True)

    written = 0
    with_image = 0

    LOGGER.info("Writing review tree for %d entries", len(included))

    for index, repo in enumerate(included):
        stem = slugify_name(repo.get("full_name", "")) or f"entry-{index}"
        part = REVIEW_PARTS[index % len(REVIEW_PARTS)]

        entry_dir = REVIEW_ROOT / part / stem
        entry_dir.mkdir(parents=True, exist_ok=True)

        image_source = None
        if fetch_images:
            image_source = download_image(
                repo.get("readme_excerpt") or "",
                repo.get("url") or "",
                entry_dir,
                stem,
            )
            if image_source:
                with_image += 1

        entry = build_review_entry(repo, image_source)
        (entry_dir / (stem + ".yml")).write_text(
            yaml.safe_dump(entry, sort_keys=False, allow_unicode=True, width=100),
            encoding="utf-8",
        )
        written += 1

    LOGGER.info("Review tree: %d entries across %d parts, %d with images",
                written, len(REVIEW_PARTS), with_image)


def run() -> int:
    queries_cfg = load_yaml("config/queries.yml")
    gitlab_queries_cfg = load_yaml("config/gitlab_queries.yml")
    taxonomy = load_yaml("config/taxonomy.yml")
    overrides = load_yaml("config/manual_overrides.yml")
    settings = load_yaml("config/settings.yml")

    github_queries = queries_cfg.get("queries", [])
    if not github_queries:
        raise ValueError("config/queries.yml contains no queries.")

    gitlab_queries = gitlab_queries_cfg.get("queries", [])
    if not gitlab_queries:
        gitlab_queries = derive_gitlab_queries_from_main_queries(github_queries, taxonomy)

    scraper_cfg = settings.get("scraper", {})
    llm_cfg = settings.get("llm", {})

    min_heuristic_score = int(scraper_cfg.get("min_heuristic_score", 4))
    classify_sleep_seconds = float(scraper_cfg.get("classify_sleep_seconds", 1.25))
    max_llm_repos = int(llm_cfg.get("max_repos_per_run", 25))
    llm_enabled = bool(llm_cfg.get("enabled", False))
    use_gitlab = bool(scraper_cfg.get("use_gitlab", True))
    cache_classifications = bool(llm_cfg.get("cache_classifications", True))
    llm_cfg["cache_classifications"] = cache_classifications

    cache = load_repo_cache()
    LOGGER.info("Repo cache loaded: %d known URLs", len(cache))

    github_candidates = discover_github_repositories(github_queries, taxonomy, settings, cache)
    gitlab_candidates = discover_gitlab_repositories(gitlab_queries, taxonomy, settings, cache) if use_gitlab else []

    save_repo_cache(cache)
    LOGGER.info("Repo cache saved: %d known URLs", len(cache))

    manual_seed_rows = load_manual_seed_repos()
    manual_seed_candidates: list[dict[str, Any]] = []
    for seed in manual_seed_rows:
        record = build_manual_seed_record(seed, taxonomy, min_heuristic_score)
        if record:
            manual_seed_candidates.append(record)

    LOGGER.info("GitHub candidate count: %d", len(github_candidates))
    LOGGER.info("GitLab candidate count: %d", len(gitlab_candidates))
    LOGGER.info("Manual seed candidate count: %d", len(manual_seed_candidates))

    all_candidates = merge_and_sort_candidates(
        github_candidates,
        gitlab_candidates,
        manual_seed_candidates,
    )
    all_candidates = apply_overrides(all_candidates, overrides)

    safe_write_json("data/all_candidates.json", all_candidates)

    prefiltered: list[dict[str, Any]] = []
    dropped_forks = 0
    dropped_quality = 0
    dropped_prefilter = 0

    for repo in all_candidates:
        if repo.get("is_fork") and not repo.get("forced_include", False):
            dropped_forks += 1
            continue

        blob = build_blob(
            repo.get("full_name", ""),
            repo.get("description", ""),
            repo.get("topics", []),
            repo.get("readme_excerpt", ""),
            repo.get("extra_excerpt", ""),
        )
        title_blob = normalize_repo_name(repo.get("full_name", ""))

        heuristic = score_text(blob, taxonomy, min_total=min_heuristic_score, title_blob=title_blob)

        repo["heuristic_strong_particle_hits"] = heuristic.strong_particle_hits
        repo["heuristic_particle_hits"] = heuristic.particle_hits
        repo["heuristic_support_hits"] = heuristic.support_hits
        repo["heuristic_ai_hits"] = heuristic.ai_hits
        repo["heuristic_negative_hits"] = heuristic.negative_hits
        repo["heuristic_generic_radiotherapy_hits"] = heuristic.generic_radiotherapy_hits
        repo["heuristic_title_strong_particle_hits"] = heuristic.title_strong_particle_hits
        repo["heuristic_title_ai_hits"] = heuristic.title_ai_hits
        repo["heuristic_total_score"] = heuristic.total_score
        repo["heuristic_has_strong_particle_anchor"] = heuristic.has_strong_particle_anchor
        repo["heuristic_passes"] = heuristic.passes
        repo["heuristic_reasons"] = heuristic.reasons

        if not passes_quality_filters(repo, settings):
            dropped_quality += 1
            continue

        if passes_prefilter(heuristic) or repo.get("forced_include", False):
            prefiltered.append(repo)
        else:
            dropped_prefilter += 1

    prefiltered = sorted(
        prefiltered,
        key=lambda row: (
            row["heuristic_total_score"],
            row["heuristic_strong_particle_hits"] + row["heuristic_title_strong_particle_hits"],
            row["heuristic_ai_hits"] + row["heuristic_title_ai_hits"],
            row.get("stars", 0),
        ),
        reverse=True,
    )

    included: list[dict[str, Any]] = []

    for repo in prefiltered:
        if llm_enabled:
            classification = classify_repo(
                repo=repo,
                llm_cfg=llm_cfg,
                cache_path="data/classification_cache.json",
            )

            if not classification.include and not repo.get("forced_include", False):
                time.sleep(classify_sleep_seconds)
                continue

            repo["classification"] = {
                "include": classification.include,
                "confidence": classification.confidence,
                "summary": classification.summary,
                "particle_therapy_relevance": classification.particle_therapy_relevance,
                "ml_relevance": classification.ml_relevance,
                "categories": classification.categories,
                "reasons": classification.reasons,
                "warnings": classification.warnings,
                "likely_tool_type": classification.likely_tool_type,
            }

            included.append(repo)
            time.sleep(classify_sleep_seconds)
        else:
            repo["classification"] = {
                "include": True,
                "confidence": 0,
                "summary": repo.get("description") or "Included by heuristic/manual filtering.",
                "particle_therapy_relevance": None,
                "ml_relevance": None,
                "categories": repo.get("manual_tags", []) or [],
                "reasons": [],
                "warnings": [],
                "likely_tool_type": "unclear",
            }
            included.append(repo)

    included = sorted(
        included,
        key=lambda row: (
            row["heuristic_total_score"],
            row["classification"].get("confidence", 0),
            row.get("stars", 0),
        ),
        reverse=True,
    )

    hf_model_tools = load_json("data/hf_model_tools.json")
    if hf_model_tools:
        included.extend(hf_model_tools)
        deduped: dict[str, dict[str, Any]] = {}
        for row in included:
            current = deduped.get(row["url"])
            if current is None or row.get("stars", 0) > current.get("stars", 0):
                deduped[row["url"]] = row
        included = sorted(
            deduped.values(),
            key=lambda row: (
                row.get("heuristic_total_score", 0),
                row.get("classification", {}).get("confidence", 0),
                row.get("stars", 0),
            ),
            reverse=True,
        )

    safe_write_json("data/catalog.json", included)
    write_readme(included)
    write_site(included)

    write_review_tree(included, fetch_images=bool(scraper_cfg.get("fetch_review_images", True)))

    LOGGER.info("GitHub queries used: %d", len(github_queries))
    LOGGER.info("GitLab queries used: %d", len(gitlab_queries))
    LOGGER.info("All candidates: %d", len(all_candidates))
    LOGGER.info("Dropped forks: %d", dropped_forks)
    LOGGER.info("Dropped by quality filters: %d", dropped_quality)
    LOGGER.info("Dropped by heuristic prefilter: %d", dropped_prefilter)
    LOGGER.info("Prefiltered candidates: %d", len(prefiltered))
    LOGGER.info("Included repositories: %d", len(included))

    return 0