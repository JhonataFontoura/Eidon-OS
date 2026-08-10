from __future__ import annotations

from eidon_os.application.goal_ports import GoalRepository
from eidon_os.domain.goal import Goal


class GoalService:
    def __init__(self, repository: GoalRepository) -> None:
        self._repository = repository

    def create(self, *, area: str, indicator: str, target: float, unit: str, period: str = "monthly") -> Goal:
        goal = Goal.create(area=area, indicator=indicator, target=target, unit=unit, period=period)
        self._repository.save(goal)
        return goal

    def list_active(self) -> list[Goal]:
        return self._repository.list_active()
