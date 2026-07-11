from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from eidon_os.application.use_cases import CreateMemory, ListMemories
from eidon_os.infrastructure.sqlite_repository import SQLiteMemoryRepository


class SQLiteMemoryRepositoryTest(unittest.TestCase):
    def test_persists_and_lists_memory(self) -> None:
        with TemporaryDirectory() as temp_directory:
            database_path = Path(temp_directory) / "eidon-test.db"
            repository = SQLiteMemoryRepository(database_path)

            created = CreateMemory(repository).execute(
                title="Decisão arquitetural",
                content="Usar SQLite na primeira versão.",
                category="projetos",
                source="Eidon OS",
            )

            memories = ListMemories(repository).execute()

            self.assertEqual(1, len(memories))
            self.assertEqual(created.id, memories[0].id)
            self.assertEqual("Decisão arquitetural", memories[0].title)


if __name__ == "__main__":
    unittest.main()
