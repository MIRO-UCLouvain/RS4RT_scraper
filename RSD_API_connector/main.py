from __future__ import annotations

import base64
import hashlib
import json
import os
import re
from pathlib import Path

import requests

TOKEN = os.getenv("RSD_TOKEN", "")
BASE = "http://localhost/api/v2"
IN_PATH = Path("data/rsd_entries.json")
COMMUNITY = "5ed2176a-967b-4d84-8945-6093cf79655e"
# community id of RS4RT

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}
AUTH = {"Authorization": f"Bearer {TOKEN}"}

SKIP_HOSTS = ("shields.io", "badge", "codecov", "travis-ci", "appveyor", "readthedocs.org/projects")
PREFER = ("logo", "banner", "title", "icon")
MIME = {
    "png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg",
    "gif": "image/gif", "svg": "image/svg+xml", "webp": "image/webp",
}

MD_IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)")
HTML_IMAGE = re.compile(r'<img[^>]+src=["\']([^"\']+)')
RST_IMAGE = re.compile(r"image::\s*(\S+)")


def post(table: str, payload: dict) -> None:
    r = requests.post(f"{BASE}/{table}", json=payload, headers=HEADERS)
    print(f"    POST {table} -> {r.status_code} {r.text[:200]}")
    if r.status_code >= 400:
        raise RuntimeError(f"{table}: {r.status_code} {r.text}")


def get(path: str) -> list:
    r = requests.get(f"{BASE}/{path}", headers=AUTH)
    r.raise_for_status()
    return r.json()


def keyword_id(value: str) -> str:
    q = requests.utils.quote(value)
    found = get(f"keyword?value=eq.{q}&select=id")
    if found:
        return found[0]["id"]
    post("keyword", {"value": value})
    return get(f"keyword?value=eq.{q}&select=id")[0]["id"]


def candidate_images(readme: str) -> list[str]:
    urls: list[str] = []
    for pattern in (MD_IMAGE, HTML_IMAGE, RST_IMAGE):
        urls.extend(pattern.findall(readme or ""))

    clean: list[str] = []
    for url in urls:
        low = url.lower()
        if any(host in low for host in SKIP_HOSTS):
            continue
        if not any(low.split("?")[0].endswith(f".{ext}") for ext in MIME):
            continue
        if url not in clean:
            clean.append(url)

    clean.sort(key=lambda u: 0 if any(p in u.lower() for p in PREFER) else 1)
    return clean


def absolute(url: str, repo_url: str) -> str:
    if url.startswith("http"):
        return url
    raw = (repo_url or "").replace("github.com", "raw.githubusercontent.com").rstrip("/")
    return f"{raw}/HEAD/{url.lstrip('./')}"


def fetch_image(url: str) -> tuple[bytes, str] | None:
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
    except Exception:
        return None

    if len(r.content) > 5_000_000 or len(r.content) < 500:
        return None

    ext = url.split("?")[0].rsplit(".", 1)[-1].lower()
    return r.content, MIME.get(ext, "image/png")


def upload_image(raw: bytes, mime: str) -> str:
    digest = hashlib.sha1(raw).hexdigest()

    found = get(f"image?id=eq.{digest}&select=id")
    if found:
        return digest

    post("image", {"id": digest, "data": base64.b64encode(raw).decode(), "mime_type": mime})
    return digest


def add_logo(sid: str, entry: dict) -> None:
    readme = entry.get("readme_excerpt") or ""
    repo_url = (entry.get("repository_url") or {}).get("url") or ""

    for candidate in candidate_images(readme)[:5]:
        url = absolute(candidate, repo_url)
        result = fetch_image(url)
        if not result:
            continue

        raw, mime = result
        try:
            image_id = upload_image(raw, mime)
        except Exception as exc:
            print(f"    image upload failed: {exc}")
            continue

        r = requests.patch(f"{BASE}/software?id=eq.{sid}", headers=HEADERS, json={"image_id": image_id})
        print(f"    PATCH image_id -> {r.status_code} ({url})")
        if r.status_code < 400:
            return

    print("    no logo found")


def push(entry: dict) -> str:
    slug = entry["software"]["slug"]
    software = {k: v for k, v in entry["software"].items() if v is not None}

    post("software", software)
    found = get(f"software?slug=eq.{slug}&select=id")
    if not found:
        raise RuntimeError(f"created but not readable: {slug}")
    sid = found[0]["id"]
    print(f"    software id {sid}")

    repo = entry.get("repository_url") or {}
    if repo.get("url"):
        post("repository_url", {
            "url": repo["url"],
            "code_platform": repo.get("code_platform") or "other",
        })
        q = requests.utils.quote(repo["url"], safe="")
        rid = get(f"repository_url?url=eq.{q}&select=id")[0]["id"]
        post("repository_url_for_software", {
            "repository_url": rid,
            "software": sid,
            "position": 0,
        })

    if entry.get("license"):
        post("license_for_software", {
            "software": sid,
            "license": entry["license"],
            "name": entry["license"],
            "open_source": True,
        })

    for value in entry.get("keywords") or []:
        post("keyword_for_software", {"software": sid, "keyword": keyword_id(value)})

    post("software_for_community", {
        "software": sid,
        "community": COMMUNITY,
        "status": "approved",
    })

    add_logo(sid, entry)

    return sid


def main() -> None:
    if not TOKEN:
        raise SystemExit("set RSD_TOKEN")

    entries = json.loads(IN_PATH.read_text(encoding="utf-8"))
    entries = entries[:]
    existing = {row["slug"] for row in get("software?select=slug")}

    created, skipped, failed = 0, 0, 0
    for entry in entries:
        slug = entry["software"]["slug"]
        if slug in existing:
            print(f"skip {slug}")
            skipped += 1
            continue
        try:
            sid = push(entry)
            print(f"ok   {slug} {sid}")
            created += 1
        except Exception as exc:
            print(f"FAIL {slug}: {exc}")
            failed += 1

    print(f"{created} created, {skipped} skipped, {failed} failed")


main()