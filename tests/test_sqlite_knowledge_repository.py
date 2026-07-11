from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from eidon_os.application.knowledge_use_cases import KnowledgeCatalog
from eidon_os.infrastructure.sqlite_knowledge_repository import SQLiteKnowledgeRepository


class SQLiteKnowledgeRepositoryTest(unittest.TestCase):
    def test_persists_all_knowledge_core_entities(self) -> None:
        with TemporaryDirectory() as temporary_directory:
            database_path = Path(temporary_directory) / "eidon.db"
            repository = SQLiteKnowledgeRepository(database_path)
            catalog = KnowledgeCatalog(repository)

            project = catalog.create_project(name="Eidon OS", description="Personal knowledge platform")
            file_record = catalog.create_file(name="README.md", path="README.md", category="documentation")
            catalog.create_person(name="Jhony Nunes", role="Creator")
            catalog.create_company(name="OpenAI", website="https://openai.com")
            catalog.create_knowledge(title="PKMS", content="Personal Knowledge Management System", kind="concept")
            catalog.create_relationship(
                source_type="project",
                source_id=str(project.id),
                target_type="file",
                target_id=str(file_record.id),
                relation_type="contains",
            )

            self.assertEqual(1, len(repository.list_projects()))
            self.assertEqual(1, len(repository.list_files()))
            self.assertEqual(1, len(repository.list_people()))
            self.assertEqual(1, len(repository.list_companies()))
            self.assertEqual(1, len(repository.list_knowledge()))
            self.assertEqual(1, len(repository.list_relationships()))


if __name__ == "__main__":
    unittest.main()
