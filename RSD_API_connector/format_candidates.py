from __future__ import annotations

import json
import re
from pathlib import Path

IN_PATH = Path("data/new_elements.json")
OUT_PATH = Path("data/rsd_entries.json")

UNKNOWN_LICENSES = {"NOASSERTION", "NONE", "", "UNKNOWN"}
MAX_DESCRIPTION = 9800
BADGE_HOSTS = ("shields.io", "badge", "codecov", "travis-ci", "appveyor", "zenodo.org/badge")


def slugify(name: str) -> str:
    return re.sub(r"[^a-zA-Z0-9]+", "-", (name or "").split("/")[-1]).strip("-").lower()


def drop_badge_lines(text: str) -> str:
    kept = []
    for line in text.split("\n"):
        stripped = line.strip()
        if stripped and all(
            any(host in part.lower() for host in BADGE_HOSTS)
            for part in re.findall(r"\((https?://[^)\s]+)", stripped)
        ) and re.findall(r"\((https?://[^)\s]+)", stripped):
            continue
        kept.append(line)
    return "\n".join(kept)


def clean_markdown(text: str) -> str:
    text = text or ""
    text = drop_badge_lines(text)
    text = re.sub(r"\[!\[[^\]]*\]\([^)]*\)\]\([^)]*\)", "", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", "", text)
    text = re.sub(r"<img[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"</?(div|p|small|center|br|span|table|tr|td|th|tbody|thead)[^>]*>", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^\s*[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"[ \t]+$", "", text, flags=re.MULTILINE)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def strip_leading_title(text: str, name: str) -> str:
    lines = text.split("\n")
    while lines:
        first = lines[0].strip()
        if not first:
            lines.pop(0)
            continue
        bare = re.sub(r"[^a-z0-9]+", "", first.lstrip("#").strip().lower())
        target = re.sub(r"[^a-z0-9]+", "", (name or "").lower())
        if bare and target and bare == target:
            lines.pop(0)
            continue
        break
    return "\n".join(lines).strip()


def truncate_markdown(text: str, limit: int = MAX_DESCRIPTION) -> str:
    if len(text) <= limit:
        return text
    cut = text[:limit]
    boundary = cut.rfind("\n\n")
    if boundary > limit // 2:
        cut = cut[:boundary]
    return cut.rstrip() + "\n\n_(truncated)_"


def long_description(readme: str, name: str, fallback: str) -> str:
    body = strip_leading_title(clean_markdown(readme), name)
    if len(body) < 80:
        return (fallback or "").strip()
    return truncate_markdown(body)


def short_statement(text: str, readme: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    if text:
        return text[:300]

    body = clean_markdown(readme)
    for block in body.split("\n\n"):
        block = re.sub(r"\s+", " ", block).strip()
        if block.startswith("#") or len(block) < 40:
            continue
        return block[:300]
    return ""


def find_doi(text: str) -> str | None:
    def tidy(value: str) -> str:
        return re.sub(r"\.(svg|png|json|pdf)$", "", value.rstrip(".),;"))

    for match in re.finditer(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", text or ""):
        doi = tidy(match.group(0))
        if "zenodo" in doi.lower():
            return doi

    match = re.search(r"10\.\d{4,9}/[-._;()/:A-Za-z0-9]+", text or "")
    return tidy(match.group(0)) if match else None


def transform(entry: dict) -> dict | None:
    name = entry.get("name") or entry.get("full_name") or ""
    if not name:
        return None

    readme = entry.get("readme_excerpt") or ""
    short_name = name.split("/")[-1]
    license_id = (entry.get("license") or "").strip()
    review = entry.get("review") or {}

    return {
        "slug": slugify(name),
        "name": name,
        "url": entry.get("url"),
        "platform": entry.get("platform") or "other",
        "description": short_statement(entry.get("description"), readme),
        "long_description": long_description(readme, short_name, entry.get("description")),
        "license": None if license_id.upper() in UNKNOWN_LICENSES else license_id,
        "keywords": entry.get("keywords") or [],
        "language": entry.get("language"),
        "concept_doi": entry.get("concept_doi") or find_doi(readme),
        "image_file": entry.get("image_file"),
        "readme_excerpt": readme,
        "reviewer": review.get("reviewer", ""),
        "review_note": review.get("note", ""),
    }


def main() -> None:
    if not IN_PATH.exists():
        raise SystemExit(f"{IN_PATH} not found")

    source = json.loads(IN_PATH.read_text(encoding="utf-8"))

    entries = []
    seen: set[str] = set()

    for item in source:
        entry = transform(item)
        if entry is None or not entry["slug"]:
            continue

        slug = entry["slug"]
        suffix = 2
        while slug in seen:
            slug = f"{entry['slug']}-{suffix}"
            suffix += 1
        entry["slug"] = slug
        seen.add(slug)

        entries.append(entry)

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(entries, indent=2, ensure_ascii=False), encoding="utf-8")

    no_license = sum(1 for e in entries if not e["license"])
    no_doi = sum(1 for e in entries if not e["concept_doi"])
    print(f"{len(source)} in, {len(entries)} out -> {OUT_PATH}")
    print(f"{no_license} without licence, {no_doi} without DOI")


main()