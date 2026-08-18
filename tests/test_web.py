from pathlib import Path
from tempfile import TemporaryDirectory
import unittest

from eidon_os.web.app import create_app


class EidonWebTests(unittest.TestCase):
    def test_web_app_exposes_initial_routes(self) -> None:
        with TemporaryDirectory() as directory:
            app = create_app(Path(directory) / "eidon.db")
            paths = {route.path for route in app.routes}

        self.assertIn("/", paths)
        self.assertIn("/health", paths)
        self.assertIn("/api/dashboard", paths)
        self.assertIn("/api/activities", paths)
        self.assertIn("/api/goals", paths)

    def test_web_app_uses_v050_metadata(self) -> None:
        with TemporaryDirectory() as directory:
            app = create_app(Path(directory) / "eidon.db")

        self.assertEqual("Eidon OS Web", app.title)
        self.assertEqual("0.5.0", app.version)


if __name__ == "__main__":
    unittest.main()
