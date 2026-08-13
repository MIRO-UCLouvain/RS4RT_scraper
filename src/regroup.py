from __future__ import annotations

import json
import re
import shutil
from pathlib import Path

import yaml

REVIEW_ROOT = Path("to_review")
CATALOG_PATH = Path("data/catalog.json")
NEW_PATH = Path("data/new_elements.json")
IMAGE_DIR = Path("data/images")

IMAGE_EXT = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}


def load_catalog() -> list[dict]:
    if not CATALOG_PATH.exists():
        return []
    try:
        return json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    except Exception:
        return []


def slugify(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", (text or "").split("/")[-1]).strip("-").lower()


def pick_image(entry_dir: Path, yaml_name: str) -> Path | None:
    images = [
        p for p in entry_dir.iterdir()
        if p.is_file() and p.suffix.lower() in IMAGE_EXT
    ]
    if not images:
        return None
    if len(images) == 1:
        return images[0]

    added = [p for p in images if p.stem != yaml_name]
    if added:
        added.sort(key=lambda p: p.stat().st_mtime, reverse=True)
        return added[0]

    return images[0]


def main() -> None:
    if not REVIEW_ROOT.exists():
        raise SystemExit("no to_review/ directory")

    catalog = load_catalog()
    known = {row.get("url") for row in catalog if row.get("url")}

    IMAGE_DIR.mkdir(parents=True, exist_ok=True)

    new_entries = []
    empty = unreadable = duplicate = images_kept = 0

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

            slug = slugify(data.get("name") or entry_dir.name)

            image = pick_image(entry_dir, files[0].stem)
            if image:
                target = IMAGE_DIR / (slug + image.suffix.lower())
                shutil.copy2(image, target)
                data["image_file"] = str(target).replace("\\", "/")
                print(f"image  {entry_dir.name} <- {image.name}")
                images_kept += 1
            else:
                data.pop("image_file", None)

            new_entries.append(data)
            known.add(data.get("url"))

    NEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    NEW_PATH.write_text(json.dumps(new_entries, indent=2, ensure_ascii=False), encoding="utf-8")

    catalog.extend(new_entries)
    CATALOG_PATH.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")

    for part in REVIEW_ROOT.glob("part_*"):
        shutil.rmtree(part, ignore_errors=True)

    print(f"\n{len(new_entries)} new -> {NEW_PATH}")
    print(f"{images_kept} images -> {IMAGE_DIR}")
    print(f"catalog now {len(catalog)} entries")
    print(f"{empty} empty, {unreadable} unreadable, {duplicate} already known")


main()