#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


# Match times like 05.40, 7.05 won't match (requires 2-digit hour).
# Only allow valid hours 00-23 and minutes 00-59.
TIME_DOT_RE = re.compile(r"\b(?P<h>[01]\d|2[0-3])\.(?P<m>[0-5]\d)\b")


def fix_text(text: str) -> tuple[str, int]:
    return TIME_DOT_RE.subn(r"\g<h>:\g<m>", text)


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Replace time format HH.MM -> HH:MM in markdown files under src/content/excursions."
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

