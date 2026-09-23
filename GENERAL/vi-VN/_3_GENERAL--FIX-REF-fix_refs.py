#!/usr/bin/env python3
"""
Chỉnh sửa các thẻ <span id="idref" data-id="G.XX">G.XX</span> có kèm số
tham chiếu phía sau (ví dụ .3 hoặc .16) thành dạng chuẩn.

Case 1 (đuôi là .SỐ.):
    <span id="idref" data-id="G.E7">G.E7</span>.3.
 -> <span id="idref" data-id="G.E7.3">G.E7</span>.

Case 2 (đuôi là .SỐ, không có dấu chấm theo sau):
    <span id="idref" data-id="G.D5">G.D5</span>.16
 -> <span id="idref" data-id="G.D5.16">G.D5.16</span>

Chạy: python3 fix_refs.py
(mặc định xử lý tất cả file .html trong thư mục hiện tại, ghi đè tại chỗ)
"""

import re
import glob
import os

# ---------------------------------------------------------------------
# Danh sách tất cả các mã tham chiếu có thể gặp. Sửa/thêm/bớt tại đây.
REF_CODES = [
    "G.A1", "G.A2", "G.A3", "G.A4",
    "G.B1", "G.B2", "G.B3", "G.B4", "G.B5", "G.B6", "G.B7",
    "G.C1", "G.C2", "G.C3", "G.C4", "G.C5", "G.C6", "G.C7",
    "G.D1", "G.D2", "G.D3", "G.D4", "G.D5",
    "G.E1", "G.E2", "G.E3", "G.E4", "G.E5", "G.E6", "G.E7",
    "G.F1", "G.F2", "G.F3", "G.F4", "G.F5",
    "G.G1", "G.G2",
    "G.H1", "G.H2", "G.H3",
]

# Thư mục chứa các file .html cần xử lý. "." = thư mục hiện tại.
TARGET_DIR = "."

# Có tạo backup (.bak) trước khi ghi đè hay không
MAKE_BACKUP = False
# ---------------------------------------------------------------------


def build_pattern(ref_codes):
    # Sắp theo độ dài giảm dần để tránh khớp nhầm mã ngắn hơn nằm trong mã dài hơn
    sorted_codes = sorted(ref_codes, key=len, reverse=True)
    alternation = "|".join(re.escape(code) for code in sorted_codes)
    # (ref) ... phải khớp đúng ref đó lần thứ hai (dùng backreference)
    pattern = (
        r'<span id="idref" data-id="(' + alternation + r')">\1</span>'
        r'\.(\d+)(\.)?'
    )
    return re.compile(pattern)


def replace_match(m):
    ref = m.group(1)
    num = m.group(2)
    trailing_dot = m.group(3)

    if trailing_dot:
        # Case 1: có dấu chấm theo sau số -> giữ lại 1 dấu chấm sau span
        return f'<span id="idref" data-id="{ref}.{num}">{ref}</span>.'
    else:
        # Case 2: không có dấu chấm theo sau số -> gộp số vào cả data-id và text
        return f'<span id="idref" data-id="{ref}.{num}">{ref}.{num}</span>'


def process_file(path, pattern):
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    new_content, count = pattern.subn(replace_match, content)

    if count > 0:
        if MAKE_BACKUP:
            with open(path + ".bak", "w", encoding="utf-8") as f:
                f.write(content)
        with open(path, "w", encoding="utf-8") as f:
            f.write(new_content)

    return count


def main():
    pattern = build_pattern(REF_CODES)
    html_files = glob.glob(os.path.join(TARGET_DIR, "*.html"))

    if not html_files:
        print("Không tìm thấy file .html nào trong thư mục.")
        return

    total = 0
    for path in sorted(html_files):
        count = process_file(path, pattern)
        total += count
        if count > 0:
            print(f"{path}: đã sửa {count} chỗ")
        else:
            print(f"{path}: không có thay đổi")

    print(f"\nTổng cộng: {total} chỗ đã được sửa trong {len(html_files)} file.")


if __name__ == "__main__":
    main()
