from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from eidon_os.application.goal_use_cases import GoalService
from eidon_os.infrastructure.sqlite_goal_repository import SQLiteGoalRepository


class GoalTests(unittest.TestCase):
    def test_create_and_list_goal(self) -> None:
        with TemporaryDirectory() as directory:
            service = GoalService(SQLiteGoalRepository(Path(directory) / "eidon.db"))
            created = service.create(area="Estudos", indicator="Horas", target=20, unit="horas")
            goals = service.list_active()
            self.assertEqual(1, len(goals))
            self.assertEqual(created.id, goals[0].id)

    def test_invalid_target_is_rejected(self) -> None:
        with TemporaryDirectory() as directory:
            service = GoalService(SQLiteGoalRepository(Path(directory) / "eidon.db"))
            with self.assertRaises(ValueError):
                service.create(area="Estudos", indicator="Horas", target=0, unit="horas")


if __name__ == "__main__": unittest.main()
