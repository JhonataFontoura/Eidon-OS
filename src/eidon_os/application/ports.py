from __future__ import annotations

from typing import Protocol
from uuid import UUID

from eidon_os.domain.memory import Memory


class MemoryRepository(Protocol):
    """Application-facing contract for memory persistence."""

    def save(self, memory: Memory) -> None: ...

    def get_by_id(self, memory_id: UUID) -> Memory | None: ...

    def list_all(self) -> list[Memory]: ...
