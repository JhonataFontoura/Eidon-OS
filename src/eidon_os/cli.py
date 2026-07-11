from __future__ import annotations

import argparse

from eidon_os.application.use_cases import CreateMemory, ListMemories
from eidon_os.infrastructure.sqlite_repository import SQLiteMemoryRepository


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Eidon OS local memory manager")
    subparsers = parser.add_subparsers(dest="command", required=True)

    create_parser = subparsers.add_parser("add", help="Catalog a new memory")
    create_parser.add_argument("--title", required=True)
    create_parser.add_argument("--content", required=True)
    create_parser.add_argument("--category", required=True)
    create_parser.add_argument("--source")

    subparsers.add_parser("list", help="List cataloged memories")
    return parser


def main() -> None:
    args = build_parser().parse_args()
    repository = SQLiteMemoryRepository()

    if args.command == "add":
        memory = CreateMemory(repository).execute(
            title=args.title,
            content=args.content,
            category=args.category,
            source=args.source,
        )
        print(f"Memory cataloged: {memory.id} — {memory.title}")
        return

    memories = ListMemories(repository).execute()
    if not memories:
        print("No memories cataloged.")
        return

    for memory in memories:
        print(f"[{memory.category}] {memory.title} ({memory.id})")


if __name__ == "__main__":
    main()
