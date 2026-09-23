"""Normalize the Hán–Việt label in every HTML file in this folder.

Usage:
    python fix_han_viet_html.py
"""

from pathlib import Path


OLD = "(Hán–Việt:".encode("utf-8")
NEW = "(Hán–Việt,".encode("utf-8")


def main() -> None:
    folder = Path.cwd()
    html_files = sorted(
        path for path in folder.iterdir() if path.is_file() and path.suffix.lower() == ".html"
    )

    changed_files = 0
    replacements = 0

    for path in html_files:
        content = path.read_bytes()
        count = content.count(OLD)
        if not count:
            continue

        path.write_bytes(content.replace(OLD, NEW))
        changed_files += 1
        replacements += count
        print(f"Updated {path.name}: {count} replacement(s)")

    print(
        f"Done. Updated {changed_files} of {len(html_files)} HTML file(s); "
        f"made {replacements} replacement(s)."
    )


if __name__ == "__main__":
    main()
