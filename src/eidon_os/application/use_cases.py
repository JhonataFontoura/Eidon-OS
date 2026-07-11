from __future__ import annotations

from eidon_os.application.ports import MemoryRepository
from eidon_os.domain.memory import Memory


class CreateMemory:
    def __init__(self, repository: MemoryRepository) -> None:
        self._repository = repository

    def execute(
        self,
        *,
        title: str,
        content: str,
        category: str,
        source: str | None = None,
    ) -> Memory:
        memory = Memory.create(
            title=title,
            content=content,
            category=category,
            source=source,
        )
        self._repository.save(memory)
        return memory


class ListMemories:
    def __init__(self, repository: MemoryRepository) -> None:
        self._repository = repository

    def execute(self) -> list[Memory]:
        return self._repository.list_all()
