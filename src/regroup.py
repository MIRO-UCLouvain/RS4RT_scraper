from __future__ import annotations

import json
import shutil
from pathlib import Path

import yaml

REVIEW_ROOT = Path("to_review")
CATALOG_PATH = Path("data/catalog.json")
NEW_PATH = Path("data/new_elements.json")

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def load_catalog() -> list[dict]:
    if not CATALOG_PATH.exists():
        return []
    try:
        return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []


def main() -> None:
    if not REVIEW_ROOT.exists():
        raise SystemExit("no to_review/ directory")

    catalog = load_catalog()
    known = {row.get("url") for row in catalog if row.get("url")}

    new_entries = []
    empty = 0
    unreadable = 0
    duplicate = 0

    for part in sorted(REVIEW_ROOT.glob("part_*")):
        for entry_dir in sorted(part.iterdir()):
            if not entry_dir.is_dir():
                continue

            files = list(entry_dir.glob("*.yml")) + list(entry_dir.glob("*.yaml"))
            if not files:
                print(f"empty  {part.name}/{entry_dir.name}")
                empty += 1
                continue

            try:
                data = yaml.safe_load(files[0].read_text(encoding="utf-8"))
            except Exception as exc:
                print(f"bad    {part.name}/{entry_dir.name}: {exc}")
                unreadable += 1
                continue

            if not data:
                print(f"empty  {part.name}/{entry_dir.name}")
                empty += 1
                continue

            if data.get("url") in known:
                print(f"dup    {entry_dir.name}")
                duplicate += 1
                continue

            images = [p.name for p in entry_dir.iterdir() if p.suffix.lower() in IMAGE_EXT]
            if images:
                data["image_file"] = images[0]

            new_entries.append(data)
            known.add(data.get("url"))

    NEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    NEW_PATH.write_text(json.dumps(new_entries, indent=2, ensure_ascii=False), encoding="utf-8")

    catalog.extend(new_entries)
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")

    for part in REVIEW_ROOT.glob("part_*"):
        shutil.rmtree(part, ignore_errors=True)

    print(f"\n{len(new_entries)} new -> {NEW_PATH}")
    print(f"catalog now {len(catalog)} entries")
    print(f"{empty} empty, {unreadable} unreadable, {duplicate} already known")


main()