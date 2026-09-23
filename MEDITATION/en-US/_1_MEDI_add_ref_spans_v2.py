#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Wrap supported HTML reference texts with idref spans."""
from pathlib import Path
import re

VALID_CODES = {
    "A1","A2","A3","A4","A5","A6",
    "B1","B2","B3","B4","B5","B6","B7","B8",
    "C1.1","C1.2","C1.3","C1.4","C1.5",
    "C2.1","C2.2","C2.3","C2.4","C2.5","C2.6",
    "D1.1","D1.2","D1.3","D1.4","D1.5","D1",
    "D2.1","D2.2","D2.3","D2.4","D2.5","D2",
    "D3.1","D3.2","D3.3","D3.4","D3.5","D3.6","D3.7","D3.8",
    "E1.1","E1.2","E1.3","E1.4",
    "E2.1","E2.2","E2.3","E2.4","E2.5","E2.6",
    "E3.1","E3.2","E3.3","E3.4","E3.5",
    "F1.1","F1.2","F1.3","F1.4","F1.5","F1.6","F1.7",
    "G1.1","G1.2","G1.3","G1.4","G1.5","G1.6","G1.7","G1.8",
    "G2.1","G2.2","G2.3","G2.4","G2.5","G2.6","G2.7","G2.8","G2.9","G2.10","G2.11","G2.12",
}
GROUPS = {"C", "D", "E", "F"}
FIRST_CODE = {g: f"{g}1" for g in GROUPS}

# Longest first + strict boundaries prevents G2.1 matching inside G2.10.
CODES_SORTED = sorted(VALID_CODES, key=len, reverse=True)
CODE_RE = re.compile(r"(?<![\w.])(?:" + "|".join(re.escape(x) for x in CODES_SORTED) + r")(?![\w.])")

# The group code itself is deliberately case-sensitive.  With re.I, the
# initial "c" in Vietnamese words such as "có" was incorrectly treated as C.
# Only the phrase prefix is case-insensitive, so both "nhóm C" and "Nhóm C"
# are supported while ordinary prose remains untouched.
GROUP_MULTI_RE = re.compile(
    r"(\b(?i:nhóm)(?:\s+(?i:bài))?\s+)([CDEF](?:\s*/\s*[CDEF])+)(?![\w./])"
)
GROUP_SINGLE_RE = re.compile(
    r"(\b(?i:nhóm)(?:\s+(?i:bài))?\s+)([CDEF])(?![\w./])"
)

# Preserve every existing span exactly, matching the behavior of your working script.
SPAN_RE = re.compile(r"<span\b[^>]*>.*?</span\s*>", re.I | re.S)
SKIP_BLOCK_RE = re.compile(r"<(script|style|textarea)\b[^>]*>.*?</\1\s*>", re.I | re.S)
TAG_SPLIT_RE = re.compile(r"(<[^>]+>)", re.S)
OPEN = "\uE000"
CLOSE = "\uE001"


def mask(text, pattern):
    stored = []
    def repl(m):
        stored.append(m.group(0))
        return f"{OPEN}{len(stored)-1}{CLOSE}"
    return pattern.sub(repl, text), stored


def unmask(text, stored):
    if not stored:
        return text
    pattern = re.compile(re.escape(OPEN) + r"(\d+)" + re.escape(CLOSE))
    return pattern.sub(lambda m: stored[int(m.group(1))], text)


def wrap(code):
    return f'<span id="idref" data-id="{code}">{code}</span>'


def process_text(text):
    original = text
    text, spans = mask(text, SPAN_RE)
    text, skipped = mask(text, SKIP_BLOCK_RE)
    tokens = TAG_SPLIT_RE.split(text)
    for i in range(0, len(tokens), 2):
        seg = tokens[i]
        # Process ordinary reference codes first. Group replacement comes
        # afterwards so generated group spans are not processed again.
        seg = CODE_RE.sub(lambda m: wrap(m.group(0)), seg)

        def replace_multi(m):
            prefix = m.group(1)
            letters = re.findall(r"[CDEF]", m.group(2))
            parts = [
                f'<span id="idref" data-id="{FIRST_CODE[x.upper()]}">{x}</span>'
                for x in letters
            ]
            return prefix + "/".join(parts)

        seg = GROUP_MULTI_RE.sub(replace_multi, seg)
        seg = GROUP_SINGLE_RE.sub(
            lambda m: m.group(1) + f'<span id="idref" data-id="{m.group(2).upper()}1">{m.group(2)}</span>',
            seg,
        )
        tokens[i] = seg
    text = unmask("".join(tokens), skipped)
    text = unmask(text, spans)
    added = text.count('<span id="idref" data-id="') - original.count('<span id="idref" data-id="')
    return text, added


def main():
    files = sorted(Path.cwd().glob("*.html"))
    if not files:
        print("No .html files found in the current folder.")
        return
    changed = added = 0
    for path in files:
        # pathlib.Path.read_text() does not accept ``newline`` until Python 3.13.
        # Open the file directly so existing line endings are preserved on older
        # Python versions too.
        with path.open("r", encoding="utf-8", newline="") as source:
            original = source.read()
        updated, n = process_text(original)
        if updated != original:
            backup = path.with_name(path.name + ".bak")
            if not backup.exists():
                with backup.open("w", encoding="utf-8", newline="") as destination:
                    destination.write(original)
            # Match the newline-preserving read above while remaining compatible
            # with Python versions before 3.13.
            with path.open("w", encoding="utf-8", newline="") as destination:
                destination.write(updated)
            changed += 1; added += n
            print(f"[UPDATED]   {path.name}: {n} reference(s) added")
        else:
            print(f"[UNCHANGED] {path.name}")
    print(f"\nFiles changed: {changed}")
    print(f"References added: {added}")

if __name__ == "__main__":
    main()
