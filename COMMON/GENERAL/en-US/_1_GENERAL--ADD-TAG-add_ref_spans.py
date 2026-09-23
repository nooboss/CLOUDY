#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
add_ref_spans.py

Xử lý tất cả file .html trong thư mục hiện hành, tự động bọc các "chú thích
tham chiếu" (A1..H3) bằng tag <span id="idref" data-id="...">...</span>.

Quy tắc:
  Case 1: Nếu mã đã nằm trong tag <span>...</span> rồi -> giữ nguyên.
  Case 2: Mã đứng riêng, ví dụ "A3" -> <span id="idref" data-id="A3">A3</span>
  Case 3: "nhóm C" / "nhóm bài C" (chỉ 1 chữ cái, không có số) ->
          nhóm <span id="idref" data-id="C1">C</span>
          (dùng mã đầu tiên của nhóm, vì chỉ có 1 nhóm)
  Case 4: "nhóm D/E/F" (nhiều chữ cái nối bằng "/") -> mỗi chữ cái được
          bọc riêng bằng span với mã đầu tiên của nhóm đó:
          nhóm <span ...data-id="D1">D</span>/<span ...data-id="E1">E</span>/<span ...data-id="F1">F</span>

Chỉ áp dụng cho các mã hợp lệ được liệt kê bên dưới (VALID_GROUPS).
Mã không hợp lệ (vd A5, G3...) sẽ KHÔNG bị bọc.

Cách dùng:
    python add_ref_spans.py
Sẽ sửa trực tiếp (in-place) tất cả *.html trong thư mục hiện hành.
"""

import glob
import re

# Danh sách nhóm hợp lệ và số lượng mã tối đa trong mỗi nhóm
VALID_GROUPS = {
    "A": 4,  # A1-A4
    "B": 7,  # B1-B7
    "C": 7,  # C1-C7
    "D": 5,  # D1-D5
    "E": 7,  # E1-E7
    "F": 5,  # F1-F5
    "G": 2,  # G1-G2
    "H": 3,  # H1-H3
}

VALID_CODES = {f"{letter}{i}" for letter, n in VALID_GROUPS.items() for i in range(1, n + 1)}
FIRST_CODE = {letter: f"{letter}1" for letter in VALID_GROUPS}

# ---- Regex patterns -------------------------------------------------

# Case 2: mã đứng riêng, vd "A3", "C7"
# (?<!\.) để tránh bắt nhầm ký hiệu chương kiểu "G.C3" (vd trong tiêu đề bài)
CASE2_RE = re.compile(r"(?<!\.)\b([A-H][1-9])\b")

# Case 4: "nhóm D/E/F" hoặc "nhóm bài D/E/F" (>=2 chữ cái nối bằng "/")
CASE4_RE = re.compile(r"(nhóm(?:\s+bài)?\s+)([A-H](?:/[A-H])+)\b")

# Case 3: "nhóm C" hoặc "nhóm bài C" (1 chữ cái, không theo sau bởi "/")
CASE3_RE = re.compile(r"(nhóm(?:\s+bài)?\s+)([A-H])\b(?!/)")

# Đã có span bao quanh rồi -> giữ nguyên, không đụng vào bên trong
SPAN_RE = re.compile(r"<span\b[^>]*>.*?</span>", re.DOTALL)

# Tách text ngoài tag khỏi các tag HTML để không sửa nhầm bên trong thuộc tính
TAG_SPLIT_RE = re.compile(r"(<[^>]+>)")

PLACEHOLDER_OPEN = "\uE000"
PLACEHOLDER_CLOSE = "\uE001"


def mask_spans(text):
    """Thay các <span>...</span> đã có sẵn bằng placeholder để không đụng vào."""
    stored = []

    def _store(m):
        stored.append(m.group(0))
        return f"{PLACEHOLDER_OPEN}{len(stored) - 1}{PLACEHOLDER_CLOSE}"

    return SPAN_RE.sub(_store, text), stored


def unmask_spans(text, stored):
    def _restore(m):
        return stored[int(m.group(1))]

    return re.sub(f"{PLACEHOLDER_OPEN}(\\d+){PLACEHOLDER_CLOSE}", _restore, text)


def case2_repl(m):
    code = m.group(1)
    if code not in VALID_CODES:
        return m.group(0)  # mã không hợp lệ -> giữ nguyên
    return f'<span id="idref" data-id="{code}">{code}</span>'


def case4_repl(m):
    prefix, letters_str = m.groups()
    letters = letters_str.split("/")
    if not all(l in VALID_GROUPS for l in letters):
        return m.group(0)
    parts = [f'<span id="idref" data-id="{FIRST_CODE[l]}">{l}</span>' for l in letters]
    return prefix + "/".join(parts)


def case3_repl(m):
    prefix, letter = m.groups()
    if letter not in VALID_GROUPS:
        return m.group(0)
    return f'{prefix}<span id="idref" data-id="{FIRST_CODE[letter]}">{letter}</span>'


def process_text(text):
    text, stored_spans = mask_spans(text)

    tokens = TAG_SPLIT_RE.split(text)
    # tokens[0], tokens[2], tokens[4], ... là text ngoài tag
    for i in range(0, len(tokens), 2):
        seg = tokens[i]
        seg = CASE2_RE.sub(case2_repl, seg)   # mã đứng riêng trước
        seg = CASE4_RE.sub(case4_repl, seg)   # nhóm X/Y/Z
        seg = CASE3_RE.sub(case3_repl, seg)   # nhóm X
        tokens[i] = seg

    text = "".join(tokens)
    text = unmask_spans(text, stored_spans)
    return text


def main():
    files = sorted(glob.glob("*.html"))
    if not files:
        print("Không tìm thấy file .html nào trong thư mục hiện hành.")
        return

    for path in files:
        # newline="" giữ nguyên kiểu xuống dòng gốc (CRLF/LF) của file
        with open(path, "r", encoding="utf-8", newline="") as f:
            original = f.read()

        updated = process_text(original)

        if updated != original:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.write(updated)
            print(f"[Đã sửa]   {path}")
        else:
            print(f"[Không đổi] {path}")


if __name__ == "__main__":
    main()
