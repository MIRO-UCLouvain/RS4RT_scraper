from __future__ import annotations

import base64
import hashlib
import json
import os
import re
from pathlib import Path

import requests

TOKEN = "9d9776ab-e9c1-4543-ae54-c04baf60c7db.aaef14b6-d7a4-4d45-a04a-961c8e6fcfe2"
BASE = "http://localhost/api/v2"
IN_PATH = Path("data/rsd_entries.json")
COMMUNITY = "2a9e0427-6b8f-40b6-9702-bd635205d012"

IN_PATH = Path(os.getenv("RSD_INPUT", "data/new_elements.json"))
LOG_PATH = Path("data/published.json")
PUBLISH = os.getenv("RSD_PUBLISH", "false").lower() in {"1", "true", "yes"}
 
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
 
 
def post(table: str, payload: dict, tolerate: tuple[str, ...] = ()) -> bool:
    r = requests.post(f"{BASE}/{table}", json=payload, headers=HEADERS)
    if r.status_code < 400:
        return True
    if any(code in r.text for code in tolerate):
        print(f"    {table}: tolerated {r.status_code}")
        return False
    raise RuntimeError(f"{table}: {r.status_code} {r.text[:300]}")
 
 
def get(path: str) -> list:
    r = requests.get(f"{BASE}/{path}", headers=AUTH)
    r.raise_for_status()
    return r.json()
 
 
def slugify(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9]+", "-", (text or "").split("/")[-1]).strip("-").lower()
 
 
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
    if get(f"image?id=eq.{digest}&select=id"):
        return digest
    post("image", {"id": digest, "data": base64.b64encode(raw).decode(), "mime_type": mime})
    return digest
 
 
def local_image(entry: dict) -> Path | None:
    name = entry.get("image_file")
    if not name:
        return None
    for root in (Path("approved"), Path("to_review")):
        for match in root.glob(f"**/{name}"):
            return match
    return None
 
 
def add_logo(sid: str, entry: dict) -> None:
    path = local_image(entry)
    if path and path.exists():
        try:
            mime = MIME.get(path.suffix.lstrip(".").lower(), "image/png")
            image_id = upload_image(path.read_bytes(), mime)
            r = requests.patch(f"{BASE}/software?id=eq.{sid}", headers=HEADERS,
                               json={"image_id": image_id})
            if r.status_code < 400:
                print(f"    logo from {path}")
                return
        except Exception as exc:
            print(f"    local image failed: {exc}")
 
    readme = entry.get("readme_excerpt") or ""
    repo_url = entry.get("url") or ""
 
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
 
        r = requests.patch(f"{BASE}/software?id=eq.{sid}", headers=HEADERS,
                           json={"image_id": image_id})
        if r.status_code < 400:
            print(f"    logo from {url}")
            return
 
    print("    no logo")
 
 
def build_software(entry: dict) -> dict:
    name = entry.get("name") or entry.get("full_name") or ""
    description = entry.get("long_description") or entry.get("description") or ""
 
    software = {
        "slug": slugify(name),
        "brand_name": name.split("/")[-1],
        "short_statement": (entry.get("description") or "")[:300],
        "description": description[:9990],
        "description_type": "markdown",
        "get_started_url": entry.get("url"),
        "closed_source": False,
        "is_published": PUBLISH,
    }
    if entry.get("concept_doi"):
        software["concept_doi"] = entry["concept_doi"]
 
    return {k: v for k, v in software.items() if v not in (None, "")}
 
 
def push(entry: dict) -> str:
    software = build_software(entry)
    slug = software["slug"]
 
    post("software", software)
    found = get(f"software?slug=eq.{slug}&select=id")
    if not found:
        raise RuntimeError(f"created but not readable: {slug}")
    sid = found[0]["id"]
 
    url = entry.get("url")
    if url:
        post("repository_url", {
            "url": url,
            "code_platform": entry.get("platform") or "other",
        }, tolerate=("23505",))
 
        q = requests.utils.quote(url, safe="")
        rows = get(f"repository_url?url=eq.{q}&select=id")
        if rows:
            post("repository_url_for_software", {
                "repository_url": rows[0]["id"],
                "software": sid,
                "position": 0,
            }, tolerate=("23505",))
 
    if entry.get("license"):
        post("license_for_software", {
            "software": sid,
            "license": entry["license"],
            "name": entry["license"],
            "open_source": True,
        }, tolerate=("23505",))
 
    for value in entry.get("keywords") or []:
        try:
            post("keyword_for_software", {"software": sid, "keyword": keyword_id(value)},
                 tolerate=("23505",))
        except Exception as exc:
            print(f"    keyword {value!r} failed: {exc}")
 
    post("software_for_community", {
        "software": sid,
        "community": COMMUNITY,
        "status": "approved",
    }, tolerate=("23505",))
 
    add_logo(sid, entry)
 
    return sid
 
 
def main() -> None:
    if not TOKEN:
        raise SystemExit("RSD_TOKEN is not set")
    if not IN_PATH.exists():
        raise SystemExit(f"{IN_PATH} not found")
 
    entries = json.loads(IN_PATH.read_text(encoding="utf-8"))
    if not entries:
        print(f"{IN_PATH} is empty, nothing to publish")
        return
 
    print(f"{len(entries)} entries from {IN_PATH}")
    print(f"target {BASE}, community {COMMUNITY}, is_published={PUBLISH}\n")
 
    existing = {row["slug"] for row in get("software?select=slug")}
 
    published: list[dict] = []
    created = skipped = failed = 0
 
    for entry in entries:
        name = entry.get("name") or entry.get("full_name") or "<unnamed>"
        slug = slugify(name)
 
        if not slug:
            print(f"FAIL {name}: no usable slug")
            failed += 1
            continue
 
        if slug in existing:
            print(f"skip {slug}")
            skipped += 1
            continue
 
        try:
            sid = push(entry)
        except Exception as exc:
            print(f"FAIL {slug}: {exc}")
            failed += 1
            continue
 
        print(f"ok   {slug} {sid}")
        published.append({"slug": slug, "name": name, "url": entry.get("url"), "rsd_id": sid})
        existing.add(slug)
        created += 1
 
    if published:
        log = []
        if LOG_PATH.exists():
            try:
                log = json.loads(LOG_PATH.read_text(encoding="utf-8"))
            except Exception:
                log = []
        log.extend(published)
        LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
        LOG_PATH.write_text(json.dumps(log, indent=2, ensure_ascii=False), encoding="utf-8")
        print(f"\nrecorded {len(published)} in {LOG_PATH}")
 
    print(f"{created} created, {skipped} skipped, {failed} failed")
 
 
main()
 
