from datetime import datetime, timezone
from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from eidon_os.application.activity_use_cases import ActivityService
from eidon_os.infrastructure.sqlite_activity_repository import SQLiteActivityRepository


class ActivityTests(unittest.TestCase):
    def test_register_and_list_activity(self) -> None:
        with TemporaryDirectory() as directory:
            repository = SQLiteActivityRepository(Path(directory) / "eidon.db")
            service = ActivityService(repository)
            occurred_at = datetime(2026, 8, 3, 12, 0, tzinfo=timezone.utc)

            created = service.register(
                title="Study SQL",
                category="studies",
                duration_minutes=45,
                occurred_at=occurred_at,
            )

            activities = service.list_all()
            self.assertEqual(1, len(activities))
            self.assertEqual(created.id, activities[0].id)
            self.assertEqual(45, activities[0].duration_minutes)

    def test_negative_duration_is_rejected(self) -> None:
        with TemporaryDirectory() as directory:
            repository = SQLiteActivityRepository(Path(directory) / "eidon.db")
            service = ActivityService(repository)
            with self.assertRaises(ValueError):
                service.register(title="Invalid", category="test", duration_minutes=-1)


if __name__ == "__main__":
    unittest.main()
