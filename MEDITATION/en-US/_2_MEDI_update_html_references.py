#!/usr/bin/env python3
"""
Update reference spans in all .html files in the current folder.

Examples:
    <span id="idref" data-id="B1">B1</span>
        -> <span id="idref" data-id="M.B1">M.B1</span>

    <span id="idref" data-id="D3.5">D3.5</span>
        -> <span id="idref" data-id="M.D3.5">M.D3.5</span>

    <span id="idref" data-id="C1">C</span>
        -> <span id="idref" data-id="M.C1">M.C</span>

Already-prefixed references such as M.B1 are left unchanged.
"""

from pathlib import Path
import re

# All supported bare reference IDs.
REFERENCE_IDS = [
    # A
    "A1", "A2", "A3", "A4", "A5", "A6",

    # B
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",

    # C
    "C1",
    "C1.1", "C1.2", "C1.3", "C1.4", "C1.5",
    "C2.1", "C2.2", "C2.3", "C2.4", "C2.5", "C2.6",

    # D
    "D1",
    "D1.1", "D1.2", "D1.3", "D1.4", "D1.5",
    "D2",
    "D2.1", "D2.2", "D2.3", "D2.4", "D2.5",
    "D3.1", "D3.2", "D3.3", "D3.4", "D3.5", "D3.6", "D3.7", "D3.8",

    # E
    "E1.1", "E1.2", "E1.3", "E1.4",
    "E2.1", "E2.2", "E2.3", "E2.4", "E2.5", "E2.6",
    "E3.1", "E3.2", "E3.3", "E3.4", "E3.5",

    # F
    "F1.1", "F1.2", "F1.3", "F1.4", "F1.5", "F1.6", "F1.7",

    # G
    "G1.1", "G1.2", "G1.3", "G1.4", "G1.5", "G1.6", "G1.7", "G1.8",
    "G2.1", "G2.2", "G2.3", "G2.4", "G2.5", "G2.6",
    "G2.7", "G2.8", "G2.9", "G2.10", "G2.11", "G2.12",
]

# Escape and sort longest-first so, for example, G2.10 is never confused
# with a shorter prefix such as G2.1.
REF_PATTERN = "|".join(
    re.escape(ref) for ref in sorted(REFERENCE_IDS, key=len, reverse=True)
)

# Match a span whose id is exactly "idref" and whose data-id is one of the
# supported bare reference IDs. Attribute order may vary.
SPAN_PATTERN = re.compile(
    rf"""
    <span
        (?=[^>]*\bid\s*=\s*(['"])idref\1)
        (?=[^>]*\bdata-id\s*=\s*(['"])({REF_PATTERN})\2)
        (?P<attrs>[^>]*)
    >
    (?P<text>[^<]*)
    </span>
    """,
    re.IGNORECASE | re.VERBOSE | re.DOTALL,
)


def replacement(match: re.Match) -> str:
    original_ref = match.group(3)

    new_data_id = f"M.{original_ref}"

    opening_tag = match.group(0)[: match.group(0).find(">") + 1]
    text = match.group("text")

    # Replace only the data-id value inside the opening span tag.
    updated_opening_tag = re.sub(
        rf'(\bdata-id\s*=\s*)(["\']){re.escape(original_ref)}\2',
        rf'\1\2{new_data_id}\2',
        opening_tag,
        count=1,
        flags=re.IGNORECASE,
    )

    # The visible text may be a shortened, leading portion of the data-id:
    # B1 -> B, C1.1 -> C1, and C1 -> C. Prefix that actual visible reference
    # instead of assuming it is identical to the data-id.
    display_ref = text.strip()
    if display_ref and original_ref.startswith(display_ref):
        leading_whitespace = text[: len(text) - len(text.lstrip())]
        trailing_whitespace = text[len(text.rstrip()):]
        updated_text = f"{leading_whitespace}M.{display_ref}{trailing_whitespace}"
    else:
        # Preserve unexpected whitespace/text rather than altering content
        # blindly.
        updated_text = text

    closing = "</span>"
    return updated_opening_tag + updated_text + closing


def process_file(path: Path) -> int:
    try:
        original = path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"[SKIP] {path.name}: not valid UTF-8")
        return 0

    updated, count = SPAN_PATTERN.subn(replacement, original)

    if count:
        path.write_text(updated, encoding="utf-8")
        print(f"[OK]   {path.name}: {count} reference(s) updated")
    else:
        print(f"[--]   {path.name}: no matching references")

    return count


def main() -> None:
    current_folder = Path.cwd()
    html_files = sorted(current_folder.glob("*.html"))

    if not html_files:
        print("No .html files found in the current folder.")
        return

    total_files_changed = 0
    total_replacements = 0

    for html_file in html_files:
        count_before = total_replacements
        total_replacements += process_file(html_file)
        if total_replacements > count_before:
            total_files_changed += 1

    print()
    print(f"Done. {total_replacements} reference(s) updated in "
          f"{total_files_changed} file(s).")


if __name__ == "__main__":
    main()
