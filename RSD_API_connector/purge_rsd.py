from __future__ import annotations

import os

import requests

TOKEN = os.getenv("RSD_TOKEN", "")
BASE = os.getenv("RSD_BASE", "https://research-software-directory.org/api/v2")

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}
AUTH = {"Authorization": f"Bearer {TOKEN}"}

CHILD_TABLES = [
    "keyword_for_software",
    "license_for_software",
    "software_for_community",
    "software_for_organisation",
    "software_for_project",
    "contributor",
    "testimonial",
    "reference_paper_for_software",
    "mention_for_software",
    "package_manager",
    "swhid_for_software",
    "badge",
    "invite_maintainer_for_software",
]


def get(path: str) -> list:
    r = requests.get(f"{BASE}/{path}", headers=AUTH, timeout=60)
    r.raise_for_status()
    return r.json()


def delete(path: str) -> int:
    return requests.delete(f"{BASE}/{path}", headers=AUTH, timeout=60).status_code


def owned_ids() -> list[str]:
    return [row["software"] for row in get("maintainer_for_software?select=software")]


def purge(sid: str) -> bool:
    rows = get(f"software?id=eq.{sid}&select=slug")
    slug = rows[0]["slug"] if rows else "<hidden>"

    for table in CHILD_TABLES:
        code = delete(f"{table}?software=eq.{sid}")
        if code >= 400 and code != 404:
            print(f"    {table}: {code}")

    links = get(f"repository_url_for_software?software=eq.{sid}&select=repository_url")
    delete(f"repository_url_for_software?software=eq.{sid}")
    for link in links:
        delete(f"repository_url?id=eq.{link['repository_url']}")

    delete(f"maintainer_for_software?software=eq.{sid}")

    code = delete(f"software?id=eq.{sid}")
    ok = code < 400
    print(f"{'ok  ' if ok else 'FAIL'} {slug} {sid} -> {code}")
    return ok


def main() -> None:
    if not TOKEN:
        raise SystemExit("RSD_TOKEN is not set")

    ids = owned_ids()
    if not ids:
        print("nothing owned, nothing to delete")
        return

    print(f"deleting {len(ids)} entries from {BASE}\n")
    removed = sum(1 for sid in ids if purge(sid))

    left = owned_ids()
    print(f"\n{removed}/{len(ids)} removed, {len(left)} still owned")


main()