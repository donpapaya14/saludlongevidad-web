"""
Plans topics avoiding duplicates and rotating categories.
Reads existing articles in src/content/blog/ to avoid repetition.
"""

import random
import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"

CATEGORIES = ["habits", "nutrition", "exercise", "sleep", "aging-science"]

ARTICLE_FORMULAS = {
    "habits": [
        "Blue Zone habit with data from Dan Buettner study and real longevity figures",
        "Morning routine for longevity with 5 steps backed by studies from real universities",
        "Daily habit that adds X years to life according to epidemiological study with name and figures",
        "One social habit that extends lifespan more than exercise according to Harvard data",
        "Breathing technique that activates the vagus nerve with specific pattern and proven benefits",
    ],
    "nutrition": [
        "Food or dietary pattern associated with longevity with data from real studies",
        "Blue Zone diet: what the longest-lived people eat with specific data",
        "Supplement with real longevity evidence: meta-analysis, dose and precautions",
        "One food Harvard researchers link to longer lifespan: specific compound and mechanism",
        "Anti-inflammatory diet guide: specific foods, mechanisms and study citations",
        "Gut microbiome and longevity: specific bacteria, food sources and health impact",
    ],
    "exercise": [
        "Exercise type that most extends lifespan according to epidemiological studies with years gained",
        "Minimum exercise minutes for real longevity benefit according to WHO and recent studies",
        "Exercise after 50: evidence-based guide with geriatrics recommendations",
        "Zone 2 cardio for longevity: specific protocol, mechanism and research backing",
        "Strength training and longevity: how many sets/week according to current research",
    ],
    "sleep": [
        "Impact of sleep on longevity with data from real cohort studies and figures",
        "Technique to improve sleep quality backed by neuroscience studies with researcher name",
        "Optimal sleep hours by age according to National Sleep Foundation and mortality studies",
        "Circadian rhythm optimization for longevity: specific timing changes and evidence",
        "Sleep deprivation and aging: specific biological mechanisms with study citations",
    ],
    "aging-science": [
        "Recent aging science discovery with study name, journal and specific finding",
        "Aging biomarker: what it measures, why it matters and how to improve it with real data",
        "Anti-aging technology in development: current state, evidence and realistic timeline",
        "Telomere science explained: what affects them and specific interventions with evidence",
        "Senescent cells and aging: what the science says and current research state",
        "Biological age vs chronological age: how to measure it and what affects it most",
    ],
}


def get_existing_titles() -> set[str]:
    titles = set()
    if not BLOG_DIR.exists():
        return titles
    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', content, re.MULTILINE)
        if match:
            titles.add(match.group(1).lower().strip())
    return titles


def get_category_counts() -> dict[str, int]:
    counts = {cat: 0 for cat in CATEGORIES}
    if not BLOG_DIR.exists():
        return counts
    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^category:\s*["\']?([^"\'\n]+)["\']?\s*$', content, re.MULTILINE)
        if match and match.group(1).strip() in counts:
            counts[match.group(1).strip()] += 1
    return counts


def pick_category() -> str:
    counts = get_category_counts()
    min_count = min(counts.values())
    least_covered = [cat for cat, count in counts.items() if count == min_count]
    return random.choice(least_covered)


def pick_formula(category: str) -> str:
    formulas = ARTICLE_FORMULAS.get(category, list(ARTICLE_FORMULAS.values())[0])
    return random.choice(formulas)


def plan_topic() -> dict:
    category = pick_category()
    formula = pick_formula(category)
    existing = get_existing_titles()
    return {
        "category": category,
        "formula": formula,
        "existing_titles": list(existing)[:20],
        "existing_count": len(existing),
    }
