#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script xử lý tất cả file .html trong folder hiện tại.

Yêu cầu:
- Tìm mọi thẻ dạng: <span id="idref" data-id="XXX">YYY</span>
- Thêm tiền tố "M." vào giá trị data-id và vào phần text bên trong thẻ.

Ví dụ:
  <span id="idref" data-id="A1">A1</span>)
    -> <span id="idref" data-id="M.A1">M.A1</span>)

  <span id="idref" data-id="C2.1">C2</span>)
    -> <span id="idref" data-id="M.C2.1">M.C2</span>)

Lưu ý:
- Script tự động bỏ qua các thẻ đã có tiền tố "M." (để chạy lại nhiều lần
  không bị nhân đôi tiền tố).
- Mặc định script sẽ tạo file backup (đuôi .bak) trước khi ghi đè.
  Dùng --no-backup nếu không muốn tạo backup.
- Dùng --dry-run để xem trước số lượng thay đổi mà KHÔNG ghi vào file.

Cách chạy:
  python xu_ly_idref_M.py                # chạy thật, có backup
  python xu_ly_idref_M.py --dry-run       # chỉ xem trước, không sửa file
  python xu_ly_idref_M.py --no-backup     # chạy thật, không tạo file .bak
"""

import re
import sys
from pathlib import Path

PREFIX = "M."

# Regex bắt toàn bộ thẻ <span ... id="idref" ...>TEXT</span>
# - Không phụ thuộc thứ tự thuộc tính (id có thể đứng trước hoặc sau data-id)
# - re.DOTALL để phòng trường hợp text xuống dòng
SPAN_PATTERN = re.compile(
    r'<span\b(?P<attrs>[^>]*\bid=["\']idref["\'][^>]*)>(?P<text>.*?)</span>',
    re.DOTALL | re.IGNORECASE,
)

# Regex bắt data-id="..." bên trong phần thuộc tính của thẻ span ở trên
DATAID_PATTERN = re.compile(
    r'(data-id=["\'])(?P<value>[^"\']*)(["\'])',
    re.IGNORECASE,
)


def add_prefix(value: str) -> str:
    """Thêm tiền tố 'M.' vào value nếu chưa có sẵn."""
    value = value.strip()
    if value.startswith(PREFIX):
        return value
    return PREFIX + value


def process_span(match: re.Match) -> str:
    attrs = match.group("attrs")
    text = match.group("text")

    def repl_dataid(m: re.Match) -> str:
        new_val = add_prefix(m.group("value"))
        return f'{m.group(1)}{new_val}{m.group(3)}'

    new_attrs = DATAID_PATTERN.sub(repl_dataid, attrs)
    new_text = add_prefix(text)

    return f'<span{new_attrs}>{new_text}</span>'


def process_file(path: Path, dry_run: bool, make_backup: bool) -> int:
    content = path.read_text(encoding="utf-8")
    new_content, count = SPAN_PATTERN.subn(process_span, content)

    if count == 0 or new_content == content:
        return 0

    if not dry_run:
        if make_backup:
            backup_path = path.with_suffix(path.suffix + ".bak")
            backup_path.write_text(content, encoding="utf-8")
        path.write_text(new_content, encoding="utf-8")

    return count


def main():
    dry_run = "--dry-run" in sys.argv
    make_backup = "--no-backup" not in sys.argv

    folder = Path(".")
    html_files = sorted(folder.glob("*.html"))

    if not html_files:
        print("Không tìm thấy file .html nào trong folder hiện tại.")
        return

    total_files_changed = 0
    total_tags_changed = 0

    for f in html_files:
        count = process_file(f, dry_run=dry_run, make_backup=make_backup)
        if count:
            total_files_changed += 1
            total_tags_changed += count
            print(f"[OK] {f.name}: đã sửa {count} tag")
        else:
            print(f"[--] {f.name}: không có tag cần sửa")

    print("\n=== TỔNG KẾT ===")
    print(f"Số file có thay đổi : {total_files_changed}/{len(html_files)}")
    print(f"Tổng số tag đã sửa  : {total_tags_changed}")
    if dry_run:
        print("(Chế độ --dry-run: CHƯA ghi thay đổi vào file)")
    elif make_backup and total_files_changed:
        print("(Đã tạo file backup .bak cho các file bị thay đổi)")


if __name__ == "__main__":
    main()