from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from eidon_os.domain.activity import Activity


@dataclass(frozen=True, slots=True)
class GeneralRow:
    date: datetime
    area: str
    activity: str
    category: str
    minutes: int
    origin: str
    status: str
    description: str | None


def normalize_area(category: str) -> str:
    normalized = category.strip().casefold()
    if "academia" in normalized or "código" in normalized or "codigo" in normalized:
        return "Academia de Código"
    if "estudo" in normalized or "curso" in normalized or "faculdade" in normalized:
        return "Estudos"
    if "projeto" in normalized or "desenvolvimento" in normalized:
        return "Projetos"
    if "carreira" in normalized or "entrevista" in normalized or "processo seletivo" in normalized:
        return "Carreira"
    return category.strip() or "Outros"


def build_general_rows(activities: list[Activity]) -> list[GeneralRow]:
    return [
        GeneralRow(
            date=item.occurred_at,
            area=normalize_area(item.category),
            activity=item.title,
            category=item.category,
            minutes=item.duration_minutes,
            origin=item.source_type or "Eidon OS",
            status="Concluído",
            description=item.description,
        )
        for item in activities
    ]


def filter_by_area(rows: list[GeneralRow], area: str) -> list[GeneralRow]:
    return [row for row in rows if row.area == area]
