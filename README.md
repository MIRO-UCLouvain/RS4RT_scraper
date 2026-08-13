<p align="center">
  <img src="assets/logo.png" alt="RS4RT" height="90">
</p>

<h1 align="center">RS4RT Catalog</h1>

<p align="center">
  <em>Resource Sharing for RadioTherapy &mdash; an open catalog of software for radiotherapy research</em>
</p>

<p align="center">
  <a href="https://miro-uclouvain.github.io/RS4RT_scraper/">Browse the catalog</a> &middot;
  <a href="https://research-software-directory.org/communities/rs4rt/software">RS4RT on the Research Software Directory</a>
</p>

---

## About

RS4RT is an independent initiative created after the 2024 ESTRO physics workshop
*Open-Source software and resource sharing in radiotherapy*. Its aim is to make open-source
radiotherapy software easier to find, cite and reuse.

This repository holds the tooling behind the catalog: a scraper that discovers candidate
repositories on GitHub and GitLab, a review workflow for curating them by hand, and a
publisher that pushes approved entries to the
[RS4RT community](https://research-software-directory.org/communities/rs4rt/software) on the Research Software Directory.

Maintained with the MIRO laboratory, UCLouvain.

## How it works

1. **Discover** &mdash; the scraper queries GitHub and GitLab for radiotherapy and particle
   therapy software, scoring each candidate against a curated taxonomy of domain terms.
2. **Review** &mdash; surviving candidates are written to `to_review/` as one folder per
   repository, split across four parts. Reviewers edit the metadata and mark entries as
   approved directly in the pull request.
3. **Publish** &mdash; approved entries are grouped, formatted and posted to the Research
   Software Directory under the RS4RT community.

Discovery runs on a schedule; review and publication are triggered by hand.

## Contributing

Know a tool that belongs here? Open an issue using the catalog submission template,
or add it to `config/manual_seed_repos.yml` and open a pull request.

---

## Catalog

**0** repositories &middot; sources:  &middot; last updated 13 August 2026

| Repository | Platform | Stars | Type | Categories | Summary |
|---|---|---:|---|---|---|

---

<sub>This file is generated automatically. Edit `src/render_readme.py` rather than `README.md`.</sub>
