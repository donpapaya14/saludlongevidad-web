"""
Planifica temas evitando duplicados y rotando categorías.
Lee artículos existentes en src/content/blog/ para evitar repetir.
"""

import os
import random
import re
from pathlib import Path

BLOG_DIR = Path(__file__).parent.parent / "src" / "content" / "blog"

CATEGORIES = ["habitos", "nutricion", "ejercicio", "sueno", "ciencia"]

ARTICLE_FORMULAS = {
    "habitos": [
        "Habito de las zonas azules con datos del estudio de Dan Buettner y cifras de longevidad",
        "Rutina matutina para longevidad con 5 pasos respaldados por estudios de universidades reales",
        "Habito diario que anade X anos de vida segun estudio epidemiologico con nombre y cifras",
    ],
    "nutricion": [
        "Alimento o patron alimentario asociado a longevidad con datos de estudios reales",
        "Dieta de las zonas azules: que comen las personas mas longevas con datos concretos",
        "Suplemento con evidencia real para longevidad: metaanalisis, dosis y precauciones",
    ],
    "ejercicio": [
        "Tipo de ejercicio que mas alarga la vida segun estudios epidemiologicos con cifras de anos ganados",
        "Minutos minimos de ejercicio para beneficio real en longevidad segun OMS y estudios recientes",
        "Ejercicio despues de los 50: guia con recomendaciones de geriatria basadas en evidencia",
    ],
    "sueno": [
        "Impacto del sueno en la longevidad con datos de estudios de cohorte reales y cifras",
        "Tecnica para mejorar calidad de sueno respaldada por estudios de neurociencia con nombre investigador",
        "Horas optimas de sueno por edad segun National Sleep Foundation y estudios de mortalidad",
    ],
    "ciencia": [
        "Descubrimiento reciente en ciencia del envejecimiento con nombre del estudio, revista y hallazgo concreto",
        "Biomarcador de envejecimiento: que mide, por que importa y como mejorarlo con datos reales",
        "Tecnologia anti-envejecimiento en desarrollo: estado actual, evidencia y timeline realista",
    ],
}


def get_existing_titles() -> set[str]:
    """Lee títulos de artículos existentes del frontmatter."""
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
    """Cuenta artículos por categoría."""
    counts = {cat: 0 for cat in CATEGORIES}
    if not BLOG_DIR.exists():
        return counts

    for md_file in BLOG_DIR.glob("*.md"):
        content = md_file.read_text(encoding="utf-8")
        match = re.search(r'^category:\s*["\']?(\w+)["\']?\s*$', content, re.MULTILINE)
        if match and match.group(1) in counts:
            counts[match.group(1)] += 1
    return counts


def pick_category() -> str:
    """Elige categoría con menos artículos (rotación equilibrada)."""
    counts = get_category_counts()
    min_count = min(counts.values())
    least_covered = [cat for cat, count in counts.items() if count == min_count]
    return random.choice(least_covered)


def pick_formula(category: str) -> str:
    """Elige fórmula aleatoria para la categoría."""
    formulas = ARTICLE_FORMULAS.get(category, list(ARTICLE_FORMULAS.values())[0])
    return random.choice(formulas)


def plan_topic() -> dict:
    """Devuelve categoría y fórmula para el próximo artículo."""
    category = pick_category()
    formula = pick_formula(category)
    existing = get_existing_titles()

    return {
        "category": category,
        "formula": formula,
        "existing_titles": list(existing)[:20],  # Para contexto al AI
        "existing_count": len(existing),
    }
