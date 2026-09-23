#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_ref_spans.py

Process every *.html file in the current folder and wrap supported
reference annotations with:

    <span id="idref" data-id="CODE">TEXT</span>

Rules
-----
Case 1:
    If a reference is already inside an existing <span>...</span>,
    leave that span unchanged.

    Example:
        <span id="idref" data-id="B1">B1</span>
    stays exactly as it is.

Case 2:
    A standalone reference code is wrapped.

        A3
    ->
        <span id="idref" data-id="A3">A3</span>

Case 3:
    A single group reference is wrapped using the first code in
    that group.

        nhóm C
    ->
        nhóm <span id="idref" data-id="C1">C</span>

    The same applies to "nhóm bài C".

Case 4:
    Multiple group references separated by "/" are wrapped
    individually.

        nhóm D/E/F
    ->
        nhóm <span id="idref" data-id="D1">D</span>/
        <span id="idref" data-id="E1">E</span>/
        <span id="idref" data-id="F1">F</span>

    The same applies to "nhóm bài D/E/F".

Important
---------
Only the codes listed in VALID_CODES are processed.

Supported codes:
    A1, A2, A3
    B1 ... B8
    C1 ... C4
    D1 ... D5
    E1 ... E4
    F1 ... F6
    G1 ... G4
    H1 ... H5
    I1 ... I6
    J1 ... J4

The script modifies HTML files in-place.

Usage:
    python add_ref_spans.py
"""

import glob
import re


# ---------------------------------------------------------------------------
# Valid reference codes
# ---------------------------------------------------------------------------

VALID_GROUPS = {
    "A": 3,  # A1-A3
    "B": 8,  # B1-B8
    "C": 4,  # C1-C4
    "D": 5,  # D1-D5
    "E": 4,  # E1-E4
    "F": 6,  # F1-F6
    "G": 4,  # G1-G4
    "H": 5,  # H1-H5
    "I": 6,  # I1-I6
    "J": 4,  # J1-J4
}

VALID_CODES = {
    f"{letter}{number}"
    for letter, max_number in VALID_GROUPS.items()
    for number in range(1, max_number + 1)
}

FIRST_CODE = {
    letter: f"{letter}1"
    for letter in VALID_GROUPS
}


# ---------------------------------------------------------------------------
# Regex patterns
# ---------------------------------------------------------------------------

# Existing spans are masked first so their content is never modified.
SPAN_RE = re.compile(
    r"<span\b[^>]*>.*?</span>",
    re.IGNORECASE | re.DOTALL,
)

# Split HTML into tags and non-tag text.
# Only non-tag text is processed, so attributes such as data-id="A3"
# are never changed.
TAG_SPLIT_RE = re.compile(r"(<[^>]+>)", re.DOTALL)

# Process references in ONE regex pass.
#
# Why Unicode-aware \w?
# Python's \w recognizes Unicode letters, so Vietnamese characters such
# as "ỏ", "á", "ê", etc. count as word characters. This is important for
# avoiding the old bug where:
#
#     "Nhóm bài hỏi"
#
# was incorrectly changed because the "H" was treated as a group reference.
#
# Group references:
#     nhóm C
#     nhóm bài C
#     nhóm D/E/F
#     nhóm bài D/E/F
#
# A group list is accepted only when it ends cleanly. The "(?!/)" check
# prevents partial matches such as "nhóm D/E/Foo" from becoming "D/E"
# and leaving "Foo" behind.
GROUP_RE = r"""
    (?P<group>
        (?<![\w.-])
        (?P<prefix>nhóm(?:\s+bài)?\s+)
        (?P<letters>[A-J](?:/[A-J])*)
        (?![\w.-])
        (?!/)
    )
"""

# Standalone reference code:
#     A3, B8, J4
#
# The boundary uses Unicode-aware \w plus "." and "-". This means a code
# must not be part of a larger identifier such as:
#     M.D2.1
#     X-D2
#     A3_test
#
# At the same time, normal punctuation such as "," and ":" is allowed, so
# a standalone reference like "A3." can still be recognized.
CODE_RE = r"""
    (?P<code>
        (?<![\w.-])
        [A-J][1-9]
        (?![\w.-])
    )
"""

REFERENCE_RE = re.compile(
    rf"{GROUP_RE}|{CODE_RE}",
    re.IGNORECASE | re.VERBOSE,
)

PLACEHOLDER_OPEN = "\uE000"
PLACEHOLDER_CLOSE = "\uE001"


# ---------------------------------------------------------------------------
# Existing-span protection
# ---------------------------------------------------------------------------

def mask_spans(text):
    """
    Replace existing <span>...</span> blocks with placeholders.

    This guarantees that references already wrapped in a span are not
    processed again.
    """
    stored = []

    def _store(match):
        stored.append(match.group(0))
        return f"{PLACEHOLDER_OPEN}{len(stored) - 1}{PLACEHOLDER_CLOSE}"

    return SPAN_RE.sub(_store, text), stored


def unmask_spans(text, stored):
    """Restore the original <span>...</span> blocks."""

    def _restore(match):
        return stored[int(match.group(1))]

    return re.sub(
        f"{re.escape(PLACEHOLDER_OPEN)}(\\d+){re.escape(PLACEHOLDER_CLOSE)}",
        _restore,
        text,
    )


# ---------------------------------------------------------------------------
# Replacement functions
# ---------------------------------------------------------------------------

def reference_repl(match):
    group = match.group("group")
    code = match.group("code")

    # Case 3 / Case 4: group reference(s).
    if group is not None:
        prefix = match.group("prefix")
        letters = match.group("letters").upper().split("/")

        if not all(letter in VALID_GROUPS for letter in letters):
            return match.group(0)

        parts = [
            f'<span id="idref" data-id="{FIRST_CODE[letter]}">{letter}</span>'
            for letter in letters
        ]

        return prefix + "/".join(parts)

    # Case 2: standalone reference code.
    code = code.upper()

    if code not in VALID_CODES:
        return match.group(0)

    return f'<span id="idref" data-id="{code}">{code}</span>'


# ---------------------------------------------------------------------------
# HTML processing
# ---------------------------------------------------------------------------

def process_text(text):
    """
    Process only text outside HTML tags and outside existing spans.

    Existing <span>...</span> blocks are masked first.
    All new references are then handled in one regex pass, which avoids
    re-processing HTML that the script itself just inserted.
    """

    text, stored_spans = mask_spans(text)

    tokens = TAG_SPLIT_RE.split(text)

    # tokens[0], tokens[2], tokens[4], ... are text nodes.
    # tokens[1], tokens[3], tokens[5], ... are HTML tags.
    for index in range(0, len(tokens), 2):
        tokens[index] = REFERENCE_RE.sub(reference_repl, tokens[index])

    text = "".join(tokens)
    return unmask_spans(text, stored_spans)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    files = sorted(glob.glob("*.html"))

    if not files:
        print("Không tìm thấy file .html nào trong thư mục hiện hành.")
        return

    changed = 0

    for path in files:
        # newline="" preserves the original newline style (LF / CRLF).
        with open(path, "r", encoding="utf-8", newline="") as file:
            original = file.read()

        updated = process_text(original)

        if updated != original:
            with open(path, "w", encoding="utf-8", newline="") as file:
                file.write(updated)

            changed += 1
            print(f"[Đã sửa]    {path}")
        else:
            print(f"[Không đổi] {path}")

    print()
    print(f"Đã xử lý: {len(files)} file .html")
    print(f"Đã thay đổi: {changed} file")


if __name__ == "__main__":
    main()
