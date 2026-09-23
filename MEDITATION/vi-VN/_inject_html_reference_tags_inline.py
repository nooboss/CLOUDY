#!/usr/bin/env python3
"""
Inject inline reference tags into all .html files in the current folder.

Example:
    A3
becomes:
    <span id="idref" data-id="A3">A3</span>

Example:
    G2.2
becomes:
    <span id="idref" data-id="G2.2">G2.2</span>

The script:
- processes only .html files directly in the current folder
- matches only the reference codes listed below
- preserves the existing HTML text/formatting as much as possible
- does not modify HTML tags/attributes
- does not modify <script>, <style>, <textarea>, <code>, or <pre> content
- skips references already inside <div id="idref">...</div>
- is safe to run repeatedly without creating nested duplicate idref tags

By default, files are modified in place.
Use --backup to create a .bak copy before modifying each file.
Use --dry-run to preview how many replacements would be made without changing files.
"""

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


# All allowed reference codes from the user's project.
REFERENCE_CODES = [
    "A1", "A2", "A3", "A4", "A5", "A6",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",

    "C1.1", "C1.2", "C1.3", "C1.4", "C1.5",
    "C2.1", "C2.2", "C2.3", "C2.4", "C2.5", "C2.6",

    "D1.1", "D1.2", "D1.3", "D1.4", "D1.5", "D1",
    "D2.1", "D2.2", "D2.3", "D2.4", "D2.5", "D2",
    "D3.1", "D3.2", "D3.3", "D3.4", "D3.5", "D3.6", "D3.7", "D3.8",

    "E1.1", "E1.2", "E1.3", "E1.4",
    "E2.1", "E2.2", "E2.3", "E2.4", "E2.5", "E2.6",
    "E3.1", "E3.2", "E3.3", "E3.4", "E3.5",

    "F1.1", "F1.2", "F1.3", "F1.4", "F1.5", "F1.6", "F1.7",

    "G1.1", "G1.2", "G1.3", "G1.4", "G1.5", "G1.6", "G1.7", "G1.8",
    "G2.1", "G2.2", "G2.3", "G2.4", "G2.5", "G2.6", "G2.7", "G2.8",
    "G2.9", "G2.10", "G2.11", "G2.12",
]

# Longest first prevents G2.1 from being partially matched inside G2.10.
REFERENCE_CODES.sort(key=len, reverse=True)

REFERENCE_PATTERN = re.compile(
    r"(?<![A-Za-z0-9_.])("
    + "|".join(re.escape(code) for code in REFERENCE_CODES)
    + r")(?![A-Za-z0-9_.])"
)

# Existing idref blocks are protected so the script is idempotent.
IDREF_BLOCK_PATTERN = re.compile(
    r'(<(?:div|span)\b[^>]*\bid\s*=\s*(["\'])idref\2[^>]*>.*?</(?:div|span)>)',
    re.IGNORECASE | re.DOTALL,
)

# HTML elements whose text should not be treated as tutorial references.
SKIP_CONTENT_TAGS = {"script", "style", "textarea", "code", "pre"}

# Used only to identify opening/closing tags while preserving them byte-for-byte.
TAG_PATTERN = re.compile(r"<!--.*?-->|<![^>]*>|<[^>]+>", re.DOTALL)


def inject_references(text: str) -> tuple[str, int]:
    """
    Replace reference tokens only in visible HTML text.

    HTML tags are never altered. Content inside script/style/textarea/code/pre
    is skipped. Existing idref elements are protected from reprocessing.
    """
    total_replacements = 0
    output: list[str] = []

    # Protect existing idref blocks with placeholders.
    protected: list[str] = []

    def protect(match: re.Match[str]) -> str:
        index = len(protected)
        protected.append(match.group(1))
        return f"\x00IDREF_{index}\x00"

    protected_text = IDREF_BLOCK_PATTERN.sub(protect, text)

    pos = 0
    skip_depth = 0

    for match in TAG_PATTERN.finditer(protected_text):
        # Process text before this HTML tag.
        text_segment = protected_text[pos:match.start()]

        if skip_depth == 0:
            def replace_reference(m: re.Match[str]) -> str:
                nonlocal total_replacements
                code = m.group(1)
                total_replacements += 1
                return f'<span id="idref" data-id="{code}">{code}</span>'

            text_segment = REFERENCE_PATTERN.sub(replace_reference, text_segment)

        output.append(text_segment)

        tag = match.group(0)
        output.append(tag)

        # Update skip depth based on opening/closing tags.
        tag_match = re.match(
            r"<\s*(/?)\s*([A-Za-z][A-Za-z0-9:-]*)\b", tag
        )
        if tag_match:
            is_closing = bool(tag_match.group(1))
            tag_name = tag_match.group(2).lower()

            if tag_name in SKIP_CONTENT_TAGS:
                if is_closing:
                    skip_depth = max(0, skip_depth - 1)
                elif not re.search(r"/\s*>$", tag):
                    skip_depth += 1

        pos = match.end()

    # Process trailing text after the last HTML tag.
    tail = protected_text[pos:]
    if skip_depth == 0:
        def replace_reference(m: re.Match[str]) -> str:
            nonlocal total_replacements
            code = m.group(1)
            total_replacements += 1
            return f'<span id="idref" data-id="{code}">{code}</span>'

        tail = REFERENCE_PATTERN.sub(replace_reference, tail)

    output.append(tail)

    result = "".join(output)

    # Restore existing idref blocks.
    for index, original in enumerate(protected):
        result = result.replace(f"\x00IDREF_{index}\x00", original)

    return result, total_replacements


def read_text_preserving_encoding(path: Path) -> tuple[str, str]:
    """Read UTF-8 first, then fall back to common encodings."""
    raw = path.read_bytes()

    if raw.startswith(b"\xef\xbb\xbf"):
        return raw[3:].decode("utf-8"), "utf-8-sig"

    for encoding in ("utf-8", "utf-8-sig", "cp1258"):
        try:
            return raw.decode(encoding), encoding
        except UnicodeDecodeError:
            pass

    raise UnicodeDecodeError(
        "unknown", raw, 0, 1,
        f"Could not decode {path.name} as UTF-8 or CP1258."
    )


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Inject <div id=\"idref\" ...> tags into HTML references."
    )
    parser.add_argument(
        "--backup",
        action="store_true",
        help="Create filename.html.bak before changing each file.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not modify files; only report what would change.",
    )
    args = parser.parse_args()

    folder = Path.cwd()
    html_files = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() == ".html"
    )

    if not html_files:
        print(f"No .html files found in: {folder}")
        return

    print(f"Folder: {folder}")
    print(f"HTML files found: {len(html_files)}")
    print()

    changed_files = 0
    total_replacements = 0

    for path in html_files:
        try:
            original, encoding = read_text_preserving_encoding(path)
            updated, count = inject_references(original)

            if count > 0 and updated != original:
                changed_files += 1
                total_replacements += count

                if args.dry_run:
                    print(f"[DRY RUN] {path.name}: {count} replacement(s)")
                else:
                    if args.backup:
                        shutil.copy2(path, path.with_suffix(path.suffix + ".bak"))

                    # Preserve the original encoding style where possible.
                    path.write_text(updated, encoding=encoding, newline="")
                    print(f"[UPDATED]  {path.name}: {count} replacement(s)")
            else:
                print(f"[UNCHANGED] {path.name}: 0 replacement(s)")

        except Exception as exc:
            print(f"[ERROR]    {path.name}: {exc}")

    print()
    if args.dry_run:
        print(f"Would update {changed_files} file(s).")
        print(f"Would make {total_replacements} replacement(s).")
    else:
        print(f"Updated {changed_files} file(s).")
        print(f"Total replacements: {total_replacements}")


if __name__ == "__main__":
    main()
