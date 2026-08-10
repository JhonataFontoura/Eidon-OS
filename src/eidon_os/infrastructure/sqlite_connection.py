from __future__ import annotations

import sqlite3
from contextlib import contextmanager
from pathlib import Path
from collections.abc import Iterator


@contextmanager
def sqlite_connection(
    database_path: str | Path,
    *,
    foreign_keys: bool = False,
) -> Iterator[sqlite3.Connection]:
    """Open a SQLite connection and always release the file handle.

    ``sqlite3.Connection`` as a context manager commits or rolls back a
    transaction, but does not guarantee that the connection itself is closed.
    On Windows this can keep temporary database files locked after a test.
    """
    connection = sqlite3.connect(database_path)
    connection.row_factory = sqlite3.Row
    if foreign_keys:
        connection.execute("PRAGMA foreign_keys = ON")

    try:
        yield connection
        connection.commit()
    except Exception:
        connection.rollback()
        raise
    finally:
        connection.close()
