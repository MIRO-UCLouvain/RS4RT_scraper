from __future__ import annotations

import json
import re
from pathlib import Path

IN_PATH = Path("../data/catalog.json")
OUT_PATH = Path("data/rsd_entries.json")

UNKNOWN_LICENSES = {"NOASSERTION", "NONE", ""}


def slugify(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", name or "").strip("-").lower()


def clean(text: str) -> str:
    text = re.sub(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)", "", text or "")
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"^[#>\s]*", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def description(readme: str, fallback: str) -> str:
    for block in clean(readme).split("\n\n"):
        block = re.sub(r"\s+", " ", block).strip()
        if len(block) >= 60 and not block.startswith("$"):
            return block[:9990]
    return fallback or ""


def short_statement(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    return text[:300]


def find_doi(text: str) -> str | None:
    for match in re.finditer(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", text or ""):
        doi = match.group(0).rstrip(".),;")
        if "zenodo" in doi.lower():
            return doi
    match = re.search(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", text or "")
    return match.group(0).rstrip(".),;") if match else None


def transform(repo: dict) -> dict | None:
    name = (repo.get("full_name") or "").split("/")[-1]
    if not name:
        return None

    readme = repo.get("readme_excerpt") or ""
    license_id = repo.get("license") or ""
    paths = repo.get("repo_paths_sample") or []

    return {
        "software": {
            "slug": slugify(name),
            "brand_name": name,
            "short_statement": short_statement(repo.get("description")),
            "description": description(readme, repo.get("description")),
            "description_type": "markdown",
            "get_started_url": repo.get("url"),
            "concept_doi": find_doi(readme),
            "closed_source": False,
            "is_published": False,
        },
        "repository_url": {
            "url": repo.get("url"),
            "code_platform": repo.get("platform"),
        },
        "license": None if license_id.upper() in UNKNOWN_LICENSES else license_id,
        "keywords": repo.get("topics") or [],
        "language": repo.get("language"),
        "has_citation_file": any(p.lower() == "citation.cff" for p in paths),
    }


def main() -> None:
    repos = json.loads(IN_PATH.read_text(encoding="utf-8"))

    entries = []
    seen = set()
    for repo in repos:
        entry = transform(repo)
        if entry is None:
            continue
        slug = entry["software"]["slug"]
        n = 2
        while slug in seen:
            slug = f"{entry['software']['slug']}-{n}"
            n += 1
        entry["software"]["slug"] = slug
        seen.add(slug)
        entries.append(entry)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"{len(repos)} in, {len(entries)} out -> {OUT_PATH}")


main()