#!/usr/bin/env python3
"""
Update reference suffixes in all .html files in the current folder.

Example:
    <span id="idref" data-id="M.E7">M.E7</span>.3.
becomes:
    <span id="idref" data-id="M.E7.3">M.E7.3</span>.

And:
    <span id="idref" data-id="M.D5">M.D5</span>.16
becomes:
    <span id="idref" data-id="M.D5.16">M.D5.16</span>

Notes:
- The script edits .html files in-place.
- Only spans with id="idref" are changed.
- A backup file is NOT created automatically.
"""

from pathlib import Path
import re


# ============================================================
# CONFIGURATION
# ============================================================

# Put all reference bases that are allowed to receive a numeric suffix here.
# You can freely add/remove references later.
BASE_REFERENCES = [
    "M.A1", "M.A2", "M.A3", "M.A4", "M.A5", "M.A6",
    "M.B1", "M.B2", "M.B3", "M.B4", "M.B5", "M.B6", "M.B7", "M.B8",
    "M.C1.1", "M.C1.2", "M.C1.3", "M.C1.4", "M.C1.5",
    "M.C2.1", "M.C2.2", "M.C2.3", "M.C2.4", "M.C2.5", "M.C2.6",
    "M.D1.1", "M.D1.2", "M.D1.3", "M.D1.4", "M.D1.5", "M.D1",
    "M.D2.1", "M.D2.2", "M.D2.3", "M.D2.4", "M.D2.5", "M.D2",
    "M.D3.1", "M.D3.2", "M.D3.3", "M.D3.4", "M.D3.5", "M.D3.6",
    "M.D3.7", "M.D3.8",
    "M.E1.1", "M.E1.2", "M.E1.3", "M.E1.4",
    "M.E2.1", "M.E2.2", "M.E2.3", "M.E2.4", "M.E2.5", "M.E2.6",
    "M.E3.1", "M.E3.2", "M.E3.3", "M.E3.4", "M.E3.5",
    "M.F1.1", "M.F1.2", "M.F1.3", "M.F1.4", "M.F1.5", "M.F1.6", "M.F1.7",
    "M.G1.1", "M.G1.2", "M.G1.3", "M.G1.4", "M.G1.5", "M.G1.6",
    "M.G1.7", "M.G1.8",
    "M.G2.10", "M.G2.11", "M.G2.12",
    "M.G2.1", "M.G2.2", "M.G2.3", "M.G2.4", "M.G2.5", "M.G2.6",
    "M.G2.7", "M.G2.8", "M.G2.9",

    # These two appear in the examples from your request.
    # Remove them if they should NOT be processed.
    "M.E7",
    "M.D5",
]

# Only spans with this id are processed.
TARGET_SPAN_ID = "idref"

# If True, a suffix is accepted only when it is immediately after </span>.
# Example: </span>.16  -> yes
# Example: </span> .16 -> no
REQUIRE_IMMEDIATE_SUFFIX = True


# ============================================================
# REGEX SETUP
# ============================================================

if not BASE_REFERENCES:
    raise ValueError("BASE_REFERENCES must contain at least one reference.")

# Escape and sort by length so a longer reference such as M.G2.12
# is considered before M.G2.1.
BASE_PATTERN = "|".join(
    re.escape(ref)
    for ref in sorted(set(BASE_REFERENCES), key=len, reverse=True)
)

# Match the complete target span:
#   <span ... id="idref" ... data-id="M.E7">M.E7</span>.3.
#
# Attribute order is allowed to vary.
# The data-id value and visible text must match the configured reference.
SPAN_PATTERN = re.compile(
    rf"""
    (?P<span>
        <span
            (?=[^>]*\bid\s*=\s*["']{re.escape(TARGET_SPAN_ID)}["'])
            (?=[^>]*\bdata-id\s*=\s*["'](?P<ref>{BASE_PATTERN})["'])
            [^>]*>
            \s*(?P<text>(?P=ref))\s*
        </span>
    )
    (?P<suffix>\.\d+)
    (?P<trailing_punct>[.,;:!?])?
    """,
    re.IGNORECASE | re.DOTALL | re.VERBOSE,
)


def replace_reference(match: re.Match) -> str:
    ref = match.group("ref")
    suffix = match.group("suffix")
    trailing_punct = match.group("trailing_punct") or ""

    full_ref = f"{ref}{suffix}"

    span = match.group("span")

    # Replace the data-id value only.
    span = re.sub(
        rf'(\bdata-id\s*=\s*["\']){re.escape(ref)}(["\'])',
        rf'\g<1>{full_ref}\g<2>',
        span,
        count=1,
        flags=re.IGNORECASE,
    )

    # Replace the visible text only.
    span = re.sub(
        rf'(\A.*?>)\s*{re.escape(ref)}(\s*</span>\Z)',
        rf'\g<1>{full_ref}\g<2>',
        span,
        count=1,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Keep the final punctuation outside the span.
    return f"{span}{trailing_punct}"


def process_html_file(path: Path) -> int:
    # Read/write with newline="" so existing CRLF/LF line endings are preserved.
    # Also preserve a UTF-8 BOM when the original file has one.
    raw = path.read_bytes()
    has_bom = raw.startswith(b"\\xef\\xbb\\xbf")

    text = raw.decode("utf-8-sig" if has_bom else "utf-8")
    new_text, count = SPAN_PATTERN.subn(replace_reference, text)

    if count:
        encoding = "utf-8-sig" if has_bom else "utf-8"
        path.write_bytes(new_text.encode(encoding))

    return count


def main() -> None:
    current_folder = Path.cwd()
    html_files = sorted(
        p for p in current_folder.iterdir()
        if p.is_file() and p.suffix.lower() == ".html"
    )

    if not html_files:
        print("No .html files found in the current folder.")
        return

    total_changes = 0
    changed_files = 0

    for path in html_files:
        try:
            count = process_html_file(path)
        except UnicodeDecodeError as exc:
            print(f"[ERROR] {path.name}: cannot decode as UTF-8 ({exc})")
            continue
        except OSError as exc:
            print(f"[ERROR] {path.name}: {exc}")
            continue

        if count:
            changed_files += 1
            total_changes += count
            print(f"[CHANGED] {path.name}: {count} reference(s)")
        else:
            print(f"[OK]      {path.name}: no changes")

    print()
    print(f"Files scanned : {len(html_files)}")
    print(f"Files changed : {changed_files}")
    print(f"References    : {total_changes}")


if __name__ == "__main__":
    main()
