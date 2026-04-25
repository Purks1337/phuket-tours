#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from pathlib import Path


FRONTMATTER_DELIM_RE = re.compile(r"(?m)^---[ \t]*$")
FIELD_RE = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*):(?P<rest>.*)$")


def find_frontmatter_body_span(text: str) -> tuple[int, int] | None:
    matches = list(FRONTMATTER_DELIM_RE.finditer(text))
    if len(matches) < 2:
        return None
    if matches[0].start() != 0:
        return None

    first = matches[0]
    second = matches[1]

    body_start = first.end()
    if body_start < len(text) and text[body_start : body_start + 1] == "\n":
        body_start += 1

    body_end = second.start()
    if body_end > 0 and text[body_end - 1 : body_end] == "\n":
        body_end -= 1

    return body_start, body_end


def _parse_scalar(value: str) -> tuple[str, str, str]:
    v = value.strip()
    if len(v) >= 2 and ((v[0] == v[-1] == '"') or (v[0] == v[-1] == "'")):
        return v[0], v[1:-1], v[-1]
    return "", v, ""


def fix_child_age_value(frontmatter_body: str) -> tuple[str, int]:
    changed = 0
    out_lines: list[str] = []

    for line in frontmatter_body.splitlines():
        m = FIELD_RE.match(line)
        if not m:
            out_lines.append(line)
            continue

        key = m.group("key")
        rest = m.group("rest")
        if key != "childAge":
            out_lines.append(line)
            continue

        quote_l, raw, quote_r = _parse_scalar(rest)

        if raw == "от 4 до 10 лет":
            raw = "4-10 лет"
            changed += 1

        spacer = " " if rest.startswith(" ") else ""
        out_lines.append(f"{key}:{spacer}{quote_l}{raw}{quote_r}")

    return "\n".join(out_lines), changed


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def process_file(path: Path, *, write: bool) -> tuple[bool, int]:
    original = path.read_text(encoding="utf-8")
    span = find_frontmatter_body_span(original)
    if not span:
        return False, 0
    body_start, body_end = span
    body = original[body_start:body_end]

    updated_body, n = fix_child_age_value(body)
    if n <= 0:
        return False, 0

    updated = original[:body_start] + updated_body + original[body_end:]
    if write:
        path.write_text(updated, encoding="utf-8")
    return True, n


def main() -> int:
    parser = argparse.ArgumentParser(
        description='Replace frontmatter childAge "от 4 до 10 лет" -> "4-10 лет" in excursions markdown',
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
        changed, n = process_file(path, write=args.write)
        if not changed:
            continue
        total_replacements += n
        changed_files.append((path, n))

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

