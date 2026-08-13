from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

SITE_URL = "https://miro-uclouvain.github.io/RS4RT_scraper/"
COMMUNITY_URL = "https://research-software-directory.org/communities/rs4rt/software"
LOGO_PATH = "assets/logo.png"


def header(entries: list[dict]) -> list[str]:
    generated = datetime.now(timezone.utc).strftime("%d %B %Y")
    platforms = sorted({item.get("platform", "unknown") for item in entries})

    return [
        f'<p align="center">',
        f'  <img src="{LOGO_PATH}" alt="RS4RT" height="90">',
        f'</p>',
        "",
        '<h1 align="center">RS4RT Catalog</h1>',
        "",
        '<p align="center">',
        "  <em>Resource Sharing for RadioTherapy &mdash; an open catalog of software for radiotherapy research</em>",
        "</p>",
        "",
        f'<p align="center">',
        f'  <a href="{SITE_URL}">Browse the catalog</a> &middot;',
        f'  <a href="{COMMUNITY_URL}">RS4RT on the Research Software Directory</a>',
        f'</p>',
        "",
        "---",
        "",
        "## About",
        "",
        "RS4RT is an independent initiative created after the 2024 ESTRO physics workshop",
        "*Open-Source software and resource sharing in radiotherapy*. Its aim is to make open-source",
        "radiotherapy software easier to find, cite and reuse.",
        "",
        "This repository holds the tooling behind the catalog: a scraper that discovers candidate",
        "repositories on GitHub and GitLab, a review workflow for curating them by hand, and a",
        "publisher that pushes approved entries to the",
        f"[RS4RT community]({COMMUNITY_URL}) on the Research Software Directory.",
        "",
        "Maintained with the MIRO laboratory, UCLouvain.",
        "",
        "## How it works",
        "",
        "1. **Discover** &mdash; the scraper queries GitHub and GitLab for radiotherapy and particle",
        "   therapy software, scoring each candidate against a curated taxonomy of domain terms.",
        "2. **Review** &mdash; surviving candidates are written to `to_review/` as one folder per",
        "   repository, split across four parts. Reviewers edit the metadata and mark entries as",
        "   approved directly in the pull request.",
        "3. **Publish** &mdash; approved entries are grouped, formatted and posted to the Research",
        "   Software Directory under the RS4RT community.",
        "",
        "Discovery runs on a schedule; review and publication are triggered by hand.",
        "",
        "## Contributing",
        "",
        "Know a tool that belongs here? Open an issue using the catalog submission template,",
        "or add it to `config/manual_seed_repos.yml` and open a pull request.",
        "",
        "---",
        "",
        "## Catalog",
        "",
        f"**{len(entries)}** repositories &middot; sources: {', '.join(platforms)} &middot; last updated {generated}",
        "",
    ]


def table(entries: list[dict]) -> list[str]:
    lines = [
        "| Repository | Platform | Stars | Type | Categories | Summary |",
        "|---|---|---:|---|---|---|",
    ]

    for item in entries:
        cls = item.get("classification") or {}
        categories = ", ".join((cls.get("categories") or [])[:4])
        summary = (cls.get("summary") or item.get("description") or "").replace("|", " ")
        summary = " ".join(summary.split())[:180]

        lines.append(
            f"| [{item.get('full_name', '')}]({item.get('url', '')}) "
            f"| {item.get('platform', '')} "
            f"| {item.get('stars', 0)} "
            f"| {cls.get('likely_tool_type', '')} "
            f"| {categories} "
            f"| {summary} |"
        )

    return lines


def footer() -> list[str]:
    return [
        "",
        "---",
        "",
        "<sub>This file is generated automatically. Edit `src/render_readme.py` rather than `README.md`.</sub>",
        "",
    ]


def write_readme(entries: list[dict]) -> None:
    lines = header(entries) + table(entries) + footer()
    Path("README.md").write_text("\n".join(lines), encoding="utf-8")