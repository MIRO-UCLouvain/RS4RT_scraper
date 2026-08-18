from __future__ import annotations

import re
from dataclasses import dataclass
from typing import Any

# When True, a term also matches its simple plural ("beam" matches "beams").
# This keeps recall close to the old substring behaviour, where "proton" used
# to match inside "protons".
MATCH_PLURALS = True

_PATTERN_CACHE: dict[str, re.Pattern[str]] = {}
_NEVER_MATCHES = re.compile(r"(?!x)x")


@dataclass
class HeuristicResult:
    strong_particle_hits: int
    particle_hits: int
    support_hits: int
    ai_hits: int
    negative_hits: int
    generic_radiotherapy_hits: int
    title_strong_particle_hits: int
    title_ai_hits: int
    total_score: int
    has_strong_particle_anchor: bool
    passes: bool
    reasons: list[str]


def normalize(text: str) -> str:
    text = (text or "").lower()
    text = re.sub(r"[-_/]+", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def compile_term(term: str) -> re.Pattern[str]:
    """Compile a taxonomy term into a whole-word pattern.

    The pattern is built against *normalized* text, so separators inside a
    multi-word term have already been flattened to single spaces. The word
    boundaries stop acronyms from matching inside longer alphanumeric runs:

        "DVH", "(dvh)", "dvh.", ".DVH", "dvh-related"  -> match
        "leodvh52", "sumdvh", "DVH2"                   -> no match
    """
    normalized = normalize(term)

    cached = _PATTERN_CACHE.get(normalized)
    if cached is not None:
        return cached

    if not normalized:
        pattern = _NEVER_MATCHES
    else:
        body = re.escape(normalized)
        suffix = ""
        if MATCH_PLURALS and normalized[-1].isalpha() and not normalized.endswith("s"):
            suffix = "s?"
        pattern = re.compile(rf"\b{body}{suffix}\b")

    _PATTERN_CACHE[normalized] = pattern
    return pattern


def term_matches(term: str, text: str) -> bool:
    """True if `term` appears in `text` as a standalone token."""
    return compile_term(term).search(normalize(text)) is not None


def _count_hits_normalized(blob: str, terms: list[str]) -> int:
    return sum(1 for term in terms if compile_term(term).search(blob))


def count_hits(text: str, terms: list[str]) -> int:
    return _count_hits_normalized(normalize(text), terms)


def score_text(
    blob: str,
    taxonomy: dict[str, Any],
    min_total: int = 4,
    title_blob: str = "",
) -> HeuristicResult:
    strong_terms = taxonomy.get("strong_particle_therapy_terms", [])
    particle_terms = taxonomy.get("particle_therapy_terms", [])
    support_terms = taxonomy.get("support_terms", [])
    ai_terms = taxonomy.get("ai_terms", [])
    negative_terms = taxonomy.get("negative_terms", [])
    generic_radiotherapy_terms = taxonomy.get("generic_radiotherapy_terms", [])

    normalized_blob = normalize(blob)
    normalized_title = normalize(title_blob)

    strong_particle_hits = _count_hits_normalized(normalized_blob, strong_terms)
    particle_hits = _count_hits_normalized(normalized_blob, particle_terms)
    support_hits = _count_hits_normalized(normalized_blob, support_terms)
    ai_hits = _count_hits_normalized(normalized_blob, ai_terms)
    negative_hits = _count_hits_normalized(normalized_blob, negative_terms)
    generic_radiotherapy_hits = _count_hits_normalized(normalized_blob, generic_radiotherapy_terms)

    title_strong_particle_hits = (
        _count_hits_normalized(normalized_title, strong_terms) if normalized_title else 0
    )
    title_ai_hits = (
        _count_hits_normalized(normalized_title, ai_terms) if normalized_title else 0
    )

    has_strong_particle_anchor = (strong_particle_hits > 0) or (title_strong_particle_hits > 0)

    total_score = 0
    total_score += strong_particle_hits * 5
    total_score += particle_hits * 2
    total_score += support_hits * 1
    # total_score += ai_hits * 3
    total_score += title_strong_particle_hits * 4
    # total_score += title_ai_hits * 2
    total_score -= negative_hits * 4

    #if generic_radiotherapy_hits > 0 and not has_strong_particle_anchor:
    #    total_score -= 5

    reasons: list[str] = []
    if strong_particle_hits:
        reasons.append(f"Matched {strong_particle_hits} strong particle-therapy term(s) in metadata/content.")
    if title_strong_particle_hits:
        reasons.append(f"Matched {title_strong_particle_hits} strong particle-therapy term(s) in repository name.")
    if particle_hits:
        reasons.append(f"Matched {particle_hits} particle-therapy term(s).")
    if support_hits:
        reasons.append(f"Matched {support_hits} support term(s).")
    if title_ai_hits:
        reasons.append(f"Matched {title_ai_hits} AI/ML term(s) in repository name.")
    # if negative_hits:
    #     reasons.append(f"Matched {negative_hits} negative term(s).")

    passes = (
        negative_hits == 0 and
        strong_particle_hits >= 1 and
        #and ((ai_hits + title_ai_hits) >= 1)
        total_score >= min_total
    )

    return HeuristicResult(
        strong_particle_hits=strong_particle_hits,
        particle_hits=particle_hits,
        support_hits=support_hits,
        ai_hits=ai_hits,
        negative_hits=negative_hits,
        generic_radiotherapy_hits=generic_radiotherapy_hits,
        title_strong_particle_hits=title_strong_particle_hits,
        title_ai_hits=title_ai_hits,
        total_score=total_score,
        has_strong_particle_anchor=has_strong_particle_anchor,
        passes=passes,
        reasons=reasons,
    )


def passes_prefilter(result: HeuristicResult) -> bool:
    return result.passes