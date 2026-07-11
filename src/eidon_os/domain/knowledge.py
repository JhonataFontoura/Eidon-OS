from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from uuid import UUID, uuid4


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def require_text(value: str, field_name: str) -> str:
    normalized = value.strip()
    if not normalized:
        raise ValueError(f"{field_name} cannot be empty")
    return normalized


@dataclass(slots=True)
class Project:
    id: UUID
    name: str
    description: str
    status: str = "active"
    github_url: str | None = None
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    @classmethod
    def create(cls, *, name: str, description: str, status: str = "active", github_url: str | None = None) -> "Project":
        return cls(uuid4(), require_text(name, "name"), require_text(description, "description"), require_text(status, "status"), github_url)


@dataclass(slots=True)
class FileRecord:
    id: UUID
    name: str
    path: str
    media_type: str | None = None
    category: str | None = None
    sha256: str | None = None
    size_bytes: int | None = None
    summary: str | None = None
    source: str | None = None
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    @classmethod
    def create(cls, *, name: str, path: str, media_type: str | None = None, category: str | None = None, sha256: str | None = None, size_bytes: int | None = None, summary: str | None = None, source: str | None = None) -> "FileRecord":
        if size_bytes is not None and size_bytes < 0:
            raise ValueError("size_bytes cannot be negative")
        return cls(uuid4(), require_text(name, "name"), str(Path(require_text(path, "path"))), media_type, category, sha256, size_bytes, summary, source)


@dataclass(slots=True)
class Person:
    id: UUID
    name: str
    role: str | None = None
    organization: str | None = None
    contact: str | None = None
    notes: str | None = None
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    @classmethod
    def create(cls, *, name: str, role: str | None = None, organization: str | None = None, contact: str | None = None, notes: str | None = None) -> "Person":
        return cls(uuid4(), require_text(name, "name"), role, organization, contact, notes)


@dataclass(slots=True)
class Company:
    id: UUID
    name: str
    website: str | None = None
    technologies: str | None = None
    notes: str | None = None
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    @classmethod
    def create(cls, *, name: str, website: str | None = None, technologies: str | None = None, notes: str | None = None) -> "Company":
        return cls(uuid4(), require_text(name, "name"), website, technologies, notes)


@dataclass(slots=True)
class KnowledgeItem:
    id: UUID
    title: str
    content: str
    kind: str
    source: str | None = None
    tags: str | None = None
    created_at: datetime = field(default_factory=utc_now)
    updated_at: datetime = field(default_factory=utc_now)

    @classmethod
    def create(cls, *, title: str, content: str, kind: str, source: str | None = None, tags: str | None = None) -> "KnowledgeItem":
        return cls(uuid4(), require_text(title, "title"), require_text(content, "content"), require_text(kind, "kind"), source, tags)


@dataclass(slots=True)
class Relationship:
    id: UUID
    source_type: str
    source_id: UUID
    target_type: str
    target_id: UUID
    relation_type: str
    notes: str | None = None
    created_at: datetime = field(default_factory=utc_now)

    @classmethod
    def create(cls, *, source_type: str, source_id: UUID, target_type: str, target_id: UUID, relation_type: str, notes: str | None = None) -> "Relationship":
        return cls(uuid4(), require_text(source_type, "source_type"), source_id, require_text(target_type, "target_type"), target_id, require_text(relation_type, "relation_type"), notes)
