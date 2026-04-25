#!/usr/bin/env python3
from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


# Add/adjust proper nouns here. Keys are matched case-insensitively.
PROPER_NOUNS: dict[str, str] = {
    "пхукет": "Пхукет",
    "пхукете": "Пхукете",
    "пхукету": "Пхукету",
    "таиланд": "Таиланд",
    "андаман": "Андаман",
    "андаманского": "Андаманского",
    "андоманского моря": "Андаманского моря",
    "пханг нга": "Пханг Нга",
    "пхи пхи": "Пхи-Пхи",
    "пхи-пхи": "Пхи-Пхи",
    "майя бэй": "Майя Бэй",
    "джеймс бонд": "Джеймс Бонд",
    "джеймса бонда": "Джеймса Бонда",
    "краби": "Краби",
    "бамбу": "Бамбу",
    "кай": "Кай",
    "майтон": "Майтон",
    "рача": "Рача",
    "корал": "Корал",
    "панак": "Панак",
    "паньи": "Паньи",
    "ко паньи": "Ко Паньи",
    "ко-тапу": "Ко-Тапу",
    "нака яй": "Нака Яй",
    "ранг яй": "Ранг Яй",
    "эраван": "Эраван",
    "као лак": "Као Лак",
    "као сок": "Као Сок",
    "чео лан": "Чео Лан",
    "самет нангше": "Самет Нангше",
    "boat lagoon": "Boat Lagoon",
    "wi-fi": "Wi‑Fi",
    "wifi": "Wi‑Fi",
    "atv": "ATV",
    "spa": "SPA",
    "jet ski": "Jet Ski",
    "x show": "X Show",
    "carnival magic": "Carnival Magic",
    "fantasea": "FantaSea",
    "andamanda": "Andamanda",
    "siam niramit": "Siam Niramit",
    "simon cabaret": "Simon Cabaret",
}


FRONTMATTER_DELIM_RE = re.compile(r"(?m)^---[ \t]*$")


@dataclass(frozen=True)
class FrontmatterSpan:
    start: int  # inclusive index of first delimiter line start
    end: int  # exclusive index of end delimiter line end
    body: str  # content between delimiters (no delimiter lines)
    body_start: int  # inclusive start index of body in original text
    body_end: int  # exclusive end index of body in original text


def find_frontmatter(text: str) -> FrontmatterSpan | None:
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

    body = text[body_start:body_end]
    end = second.end()
    if end < len(text) and text[end : end + 1] == "\n":
        end += 1

    return FrontmatterSpan(
        start=first.start(),
        end=end,
        body=body,
        body_start=body_start,
        body_end=body_end,
    )


def _sentence_case_keep_rest(s: str) -> str:
    for i, ch in enumerate(s):
        if ch.isalpha():
            return s[:i] + ch.upper() + s[i + 1 :]
    return s


def _apply_proper_nouns(s: str) -> str:
    # Longer keys first to avoid partial matches overriding phrases.
    for k in sorted(PROPER_NOUNS.keys(), key=len, reverse=True):
        v = PROPER_NOUNS[k]
        # "Word-ish" boundaries that work better with hyphens than \b.
        pat = re.compile(rf"(?<![\w-]){re.escape(k)}(?![\w-])", flags=re.IGNORECASE)
        s = pat.sub(v, s)
    return s


def format_ru_title(s: str) -> str:
    s = " ".join(s.strip().split())
    s = s.lower()
    s = _apply_proper_nouns(s)
    s = _sentence_case_keep_rest(s)
    return s


def _parse_scalar(value: str) -> tuple[str, str, str]:
    v = value.strip()
    if len(v) >= 2 and ((v[0] == v[-1] == '"') or (v[0] == v[-1] == "'")):
        return v[0], v[1:-1], v[-1]
    return "", v, ""


FIELD_RE = re.compile(r"^(?P<key>[A-Za-z_][A-Za-z0-9_]*):(?P<rest>.*)$")


def format_frontmatter_fields(frontmatter_body: str, keys: set[str]) -> tuple[str, int]:
    changed = 0
    out_lines: list[str] = []

    for line in frontmatter_body.splitlines():
        m = FIELD_RE.match(line)
        if not m:
            out_lines.append(line)
            continue
        key = m.group("key")
        rest = m.group("rest")
        if key not in keys:
            out_lines.append(line)
            continue

        quote_l, raw, quote_r = _parse_scalar(rest)
        formatted = format_ru_title(raw)
        if formatted != raw:
            changed += 1

        spacer = " " if rest.startswith(" ") else ""
        new_value = f"{quote_l}{formatted}{quote_r}"
        out_lines.append(f"{key}:{spacer}{new_value}")

    return "\n".join(out_lines), changed


def iter_markdown_files(root: Path) -> list[Path]:
    return sorted([p for p in root.rglob("*.md") if p.is_file()])


def process_file(path: Path, *, write: bool) -> tuple[bool, int]:
    original = path.read_text(encoding="utf-8")
    fm = find_frontmatter(original)
    if not fm:
        return False, 0

    updated_body, n = format_frontmatter_fields(fm.body, {"title", "subtitle"})
    if n <= 0:
        return False, 0

    updated = original[: fm.body_start] + updated_body + original[fm.body_end :]
    if write:
        path.write_text(updated, encoding="utf-8")
    return True, n


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            'Format frontmatter fields "title" and "subtitle" in excursions markdown: '
            "sentence case + proper nouns dictionary"
        ),
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
    total_field_updates = 0

    for path in files:
        changed, n = process_file(path, write=args.write)
        if not changed:
            continue
        total_field_updates += n
        changed_files.append((path, n))

    mode = "WRITE" if args.write else "DRY-RUN"
    print(f"[{mode}] scanned: {len(files)} file(s)")
    print(f"[{mode}] changed: {len(changed_files)} file(s)")
    print(f"[{mode}] title/subtitle updates: {total_field_updates}")
    if changed_files:
        print("\nFiles:")
        for p, n in changed_files:
            print(f"- {p} ({n})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

