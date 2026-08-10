from __future__ import annotations

from typing import Protocol

from eidon_os.domain.goal import Goal


class GoalRepository(Protocol):
    def save(self, goal: Goal) -> None: ...
    def list_active(self) -> list[Goal]: ...
