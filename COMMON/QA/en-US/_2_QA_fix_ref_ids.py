#!/usr/bin/env python3
"""
Chỉnh sửa các thẻ <span id="idref" data-id="...">...</span> trong tất cả
các file .html của thư mục hiện tại, thêm tiền tố "G." nếu chưa có.

Cách chạy:
    python fix_ref_ids.py

Mặc định sẽ xử lý mọi file *.html trong thư mục hiện tại (không đệ quy
vào thư mục con). Có thể đổi PREFIX hoặc thư mục quét bên dưới nếu cần.
"""

import re
import sys
from pathlib import Path

# Tiền tố sẽ được thêm vào, đổi tại đây nếu cần dùng cho file khác (VD "F.")
PREFIX = "Q."

# Danh sách các mã chú thích hợp lệ
VALID_CODES = {
    "A1", "A2", "A3",
    "B1", "B2", "B3", "B4", "B5", "B6", "B7", "B8",
    "C1", "C2", "C3", "C4",
    "D1", "D2", "D3", "D4", "D5",
    "E1", "E2", "E3", "E4",
    "F1", "F2", "F3", "F4", "F5", "F6",
    "G1", "G2", "G3", "G4",
    "H1", "H2", "H3", "H4", "H5",
    "I1", "I2", "I3", "I4", "I5", "I6",
    "J1", "J2", "J3", "J4",
}

# Khớp: <span id="idref" data-id="XXX">YYY</span>
SPAN_RE = re.compile(
    r'<span id="idref" data-id="([^"]+)">([^<]*)</span>'
)


def base_code_valid(data_id: str) -> bool:
    """Kiểm tra data-id có khớp chính xác một mã hợp lệ trong danh sách không."""
    return data_id in VALID_CODES


def process_span(match: re.Match, counter: list) -> str:
    data_id = match.group(1)
    text = match.group(2)

    # Case 4: đã có tiền tố -> giữ nguyên
    if data_id.startswith(PREFIX):
        return match.group(0)

    # Chỉ xử lý nếu mã gốc nằm trong danh sách hợp lệ
    if not base_code_valid(data_id):
        return match.group(0)

    new_data_id = f"{PREFIX}{data_id}"
    new_text = f"{PREFIX}{text}" if text else text

    counter[0] += 1
    return f'<span id="idref" data-id="{new_data_id}">{new_text}</span>'


def process_file(path: Path) -> int:
    original = path.read_text(encoding="utf-8")
    counter = [0]
    updated = SPAN_RE.sub(lambda m: process_span(m, counter), original)
    if counter[0]:
        path.write_text(updated, encoding="utf-8")
    return counter[0]


def main():
    folder = Path(".")
    html_files = sorted(folder.glob("*.html"))

    if not html_files:
        print("Không tìm thấy file .html nào trong thư mục hiện tại.")
        return

    total_files_changed = 0
    total_spans_changed = 0

    for path in html_files:
        try:
            changed = process_file(path)
        except Exception as e:
            print(f"[LỖI] {path.name}: {e}", file=sys.stderr)
            continue

        if changed:
            total_files_changed += 1
            total_spans_changed += changed
            print(f"{path.name}: đã sửa {changed} thẻ span")

    print(
        f"\nHoàn tất. {total_files_changed}/{len(html_files)} file được sửa, "
        f"tổng cộng {total_spans_changed} thẻ span."
    )


if __name__ == "__main__":
    main()
