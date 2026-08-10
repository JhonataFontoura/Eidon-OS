from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class Goal:
    id: UUID
    area: str
    indicator: str
    target: float
    unit: str
    period: str = "monthly"
    active: bool = True
    created_at: datetime = field(default_factory=utc_now)

    @classmethod
    def create(cls, *, area: str, indicator: str, target: float, unit: str, period: str = "monthly") -> "Goal":
        if target <= 0:
            raise ValueError("target must be greater than zero")
        area = area.strip()
        indicator = indicator.strip()
        unit = unit.strip()
        period = period.strip()
        if not all((area, indicator, unit, period)):
            raise ValueError("goal fields cannot be empty")
        return cls(uuid4(), area, indicator, target, unit, period)
