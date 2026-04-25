#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


TARGETS = ("ОБЗОР", "ОСНОВНЫЕ МОМЕНТЫ", "МАРШРУТ")

# Replace lines that are exactly one of the target headings, with or without leading #'s.
HEADING_RE = re.compile(
    r"(?m)^[ \t]*(?:#{1,6}[ \t]*)?(?P<t>ОБЗОР|ОСНОВНЫЕ МОМЕНТЫ|МАРШРУТ)[ \t]*$"
)


def fix_text(text: str) -> tuple[str, int]:
    return HEADING_RE.subn(lambda m: f"### {m.group('t')}", text)


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Normalize section headings "ОБЗОР", "ОСНОВНЫЕ МОМЕНТЫ", "МАРШРУТ" to "### ..."',
    )
    parser.add_argument(
        "--root",
        default="src/content/excursions",
        help="Root directory to scan (default: src/content/excursions)",
    )
    parser.add_argument(
        "--write",
        action="store_true",
        help="Write changes to files (default: dry-run)",
    )
    args = parser.parse_args()

    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"Root does not exist: {root}")
    if not root.is_dir():
        raise SystemExit(f"Root is not a directory: {root}")

    files = iter_markdown_files(root)
    changed_files: list[tuple[Path, int]] = []
    total_replacements = 0

    for path in files:
        original = path.read_text(encoding="utf-8")
        updated, n = fix_text(original)
        if n <= 0:
            continue
        total_replacements += n
        changed_files.append((path, n))
        if args.write:
            path.write_text(updated, encoding="utf-8")

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"[{mode}] scanned: {len(files)} file(s)")
    print(f"[{mode}] changed: {len(changed_files)} file(s)")
    print(f"[{mode}] replacements: {total_replacements}")
    if changed_files:
        print("\nFiles:")
        for p, n in changed_files:
            print(f"- {p} ({n})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

