#!/usr/bin/env python3
"""Inject top/bottom navigator placeholders into every .html file in this folder.

Rules:
1. Insert <div id="navigators-top"></div> immediately below the title block
   containing an element with id="title-text". If that element is wrapped in a
   <center>...</center> block, insertion is made after the closing </center>,
   matching the structure shown in the example.
2. Insert <div id="navigators-bottom"></div> immediately above the first
   <div><h4>Chú giải:</h4>...</div> heading group.

The script is idempotent: existing navigator divs are not duplicated.
It processes only .html files in the current directory (not subdirectories).
Original files are modified in place.
"""

from __future__ import annotations

import re
from pathlib import Path

TOP_TAG = '<div id="navigators-top"></div>'
BOTTOM_TAG = '<div id="navigators-bottom"></div>'

# Match a complete element whose id is title-text. This is intentionally
# attribute-order/whitespace tolerant and preserves the original HTML text.
TITLE_ELEMENT_RE = re.compile(
    r'<(?P<tag>[A-Za-z][\w:-]*)\b'
    r'(?=[^>]*\bid\s*=\s*["\']title-text["\'])'
    r'[^>]*>.*?</(?P=tag)\s*>',
    re.IGNORECASE | re.DOTALL,
)

# The example places the top navigator after a <center> block containing the
# title. Match that block first, with a fallback to the title element itself.
CENTER_TITLE_BLOCK_RE = re.compile(
    r'<center\b[^>]*>'
    r'(?:(?!</center\s*>).)*?'
    r'<(?P<tag>[A-Za-z][\w:-]*)\b'
    r'(?=[^>]*\bid\s*=\s*["\']title-text["\'])'
    r'[^>]*>.*?</(?P=tag)\s*>'
    r'(?:(?!</center\s*>).)*?'
    r'</center\s*>',
    re.IGNORECASE | re.DOTALL,
)

# Match the opening div + heading exactly enough to avoid accidentally
# injecting above an unrelated heading with similar text.
GLOSSARY_GROUP_RE = re.compile(
    r'<div\b[^>]*>\s*<h4\b[^>]*>\s*Chú\s+giải\s*:\s*</h4>',
    re.IGNORECASE | re.DOTALL,
)


def has_navigator_near(text: str, position: int, tag: str) -> bool:
    """Return True if the navigator already exists immediately around position."""
    before = text[max(0, position - 120):position]
    after = text[position:position + 120]
    marker = tag
    return marker in before or marker in after


def inject_top(text: str) -> tuple[str, bool]:
    # Prefer the structure shown in the user's example.
    m = CENTER_TITLE_BLOCK_RE.search(text)
    if m:
        insert_at = m.end()
        if has_navigator_near(text, insert_at, TOP_TAG):
            return text, False
        # Keep the existing file's newline convention when possible.
        newline = "\r\n" if "\r\n" in text else "\n"
        return text[:insert_at] + newline + TOP_TAG + text[insert_at:], True

    # Fallback: title-text element not wrapped in a center block.
    m = TITLE_ELEMENT_RE.search(text)
    if m:
        insert_at = m.end()
        if has_navigator_near(text, insert_at, TOP_TAG):
            return text, False
        newline = "\r\n" if "\r\n" in text else "\n"
        return text[:insert_at] + newline + TOP_TAG + text[insert_at:], True

    return text, False


def inject_bottom(text: str) -> tuple[str, bool]:
    m = GLOSSARY_GROUP_RE.search(text)
    if not m:
        return text, False

    insert_at = m.start()
    if has_navigator_near(text, insert_at, BOTTOM_TAG):
        return text, False

    newline = "\r\n" if "\r\n" in text else "\n"
    return text[:insert_at] + BOTTOM_TAG + newline + text[insert_at:], True


def process_file(path: Path) -> tuple[bool, list[str]]:
    # utf-8-sig preserves/removes BOM cleanly when present; it is written back
    # as UTF-8 with BOM only if the original started with one.
    raw = path.read_bytes()
    has_bom = raw.startswith(b"\xef\xbb\xbf")
    encoding = "utf-8-sig" if has_bom else "utf-8"

    try:
        text = raw.decode(encoding)
    except UnicodeDecodeError as exc:
        return False, [f"SKIPPED (UTF-8 decode error: {exc})"]

    original = text
    notes: list[str] = []

    text, changed_top = inject_top(text)
    if changed_top:
        notes.append("inserted navigators-top")
    elif TOP_TAG in text:
        notes.append("navigators-top already present")
    else:
        notes.append("title-text not found")

    text, changed_bottom = inject_bottom(text)
    if changed_bottom:
        notes.append("inserted navigators-bottom")
    elif BOTTOM_TAG in text:
        notes.append("navigators-bottom already present")
    else:
        notes.append("Chú giải heading group not found")

    if text != original:
        path.write_bytes(text.encode(encoding))
        return True, notes

    return False, notes


def main() -> None:
    folder = Path.cwd()
    html_files = sorted(
        p for p in folder.iterdir()
        if p.is_file() and p.suffix.lower() == ".html"
    )

    if not html_files:
        print(f"No .html files found in: {folder}")
        return

    changed_count = 0
    print(f"Processing {len(html_files)} HTML file(s) in: {folder}\n")

    for path in html_files:
        changed, notes = process_file(path)
        status = "MODIFIED" if changed else "UNCHANGED"
        print(f"[{status}] {path.name}")
        for note in notes:
            print(f"    - {note}")
        if changed:
            changed_count += 1

    print(f"\nDone. Modified {changed_count} of {len(html_files)} file(s).")


if __name__ == "__main__":
    main()
