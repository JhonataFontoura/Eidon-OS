from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from eidon_os.infrastructure.sqlite_activity_repository import SQLiteActivityRepository
from eidon_os.infrastructure.sqlite_goal_repository import SQLiteGoalRepository
from eidon_os.infrastructure.sqlite_knowledge_repository import SQLiteKnowledgeRepository
from eidon_os.intelligence.tools import EidonToolRegistry


class EidonAIToolTests(unittest.TestCase):
    def test_ai_tools_can_write_and_read_eidon(self) -> None:
        with TemporaryDirectory() as directory:
            db = Path(directory) / "eidon.db"
            tools = EidonToolRegistry(
                SQLiteKnowledgeRepository(db),
                SQLiteActivityRepository(db),
                SQLiteGoalRepository(db),
            )
            created = tools.execute(
                "create_activity",
                {"title": "Estudo de IA", "category": "Estudos", "duration_minutes": 60},
            )
            dashboard = tools.execute("get_dashboard", {})
            self.assertIn("created", created)
            self.assertEqual(1, dashboard["activities"])
            self.assertEqual(60, dashboard["total_minutes"])

    def test_delete_requires_visual_authorization(self) -> None:
        with TemporaryDirectory() as directory:
            db = Path(directory) / "eidon.db"
            activities = SQLiteActivityRepository(db)
            tools = EidonToolRegistry(
                SQLiteKnowledgeRepository(db), activities, SQLiteGoalRepository(db)
            )
            created = tools.execute(
                "create_activity",
                {"title": "Temporária", "category": "Teste", "duration_minutes": 1},
            )["created"]
            denied = tools.execute(
                "delete_record",
                {"record_type": "activity", "record_id": created["id"]},
                allow_destructive=False,
            )
            self.assertFalse(denied["deleted"])
            self.assertEqual(1, len(activities.list_all()))
            allowed = tools.execute(
                "delete_record",
                {"record_type": "activity", "record_id": created["id"]},
                allow_destructive=True,
            )
            self.assertTrue(allowed["deleted"])
            self.assertEqual([], activities.list_all())


if __name__ == "__main__":
    unittest.main()
