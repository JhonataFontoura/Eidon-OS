from __future__ import annotations

from uuid import UUID

from eidon_os.application.knowledge_ports import KnowledgeRepository
from eidon_os.domain.knowledge import Company, FileRecord, KnowledgeItem, Person, Project, Relationship


class KnowledgeCatalog:
    def __init__(self, repository: KnowledgeRepository) -> None:
        self._repository = repository

    def create_project(self, **data: object) -> Project:
        project = Project.create(**data)
        self._repository.save_project(project)
        return project

    def create_file(self, **data: object) -> FileRecord:
        file_record = FileRecord.create(**data)
        self._repository.save_file(file_record)
        return file_record

    def create_person(self, **data: object) -> Person:
        person = Person.create(**data)
        self._repository.save_person(person)
        return person

    def create_company(self, **data: object) -> Company:
        company = Company.create(**data)
        self._repository.save_company(company)
        return company

    def create_knowledge(self, **data: object) -> KnowledgeItem:
        item = KnowledgeItem.create(**data)
        self._repository.save_knowledge(item)
        return item

    def create_relationship(self, *, source_type: str, source_id: str, target_type: str, target_id: str, relation_type: str, notes: str | None = None) -> Relationship:
        relationship = Relationship.create(
            source_type=source_type,
            source_id=UUID(source_id),
            target_type=target_type,
            target_id=UUID(target_id),
            relation_type=relation_type,
            notes=notes,
        )
        self._repository.save_relationship(relationship)
        return relationship
