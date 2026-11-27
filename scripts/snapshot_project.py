#!/usr/bin/env python3
"""Tạo bản sao lưu nén (.zip) an toàn cho thư mục dự án trước các thao tác lớn."""

import argparse
import re
import zipfile
from datetime import datetime
from pathlib import Path

EXCLUDE_DIRS = {"_Backups", ".git", "__pycache__", "node_modules", ".venv", "venv"}


def sanitize_label(label: str) -> str:
    cleaned = re.sub(r"[^a-zA-Z0-9_-]+", "_", label.strip())
    return cleaned.strip("_") or "snapshot"


def main() -> None:
    parser = argparse.ArgumentParser(description="Tạo bản sao lưu nén an toàn vào <project>/_Backups/.")
    parser.add_argument("--project", required=True, help="Đường dẫn thư mục gốc dự án")
    parser.add_argument("--label", default="pre_batch", help="Nhãn ngắn gọn mô tả thời điểm sao lưu")
    args = parser.parse_args()

    root = Path(args.project).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit(f"[LỖI] Thư mục dự án không tồn tại: {root}")

    backup_dir = root / "_Backups"
    backup_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    label = sanitize_label(args.label)
    zip_path = backup_dir / f"{ts}_{root.name}_{label}.zip"

    file_count = 0
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for path in root.rglob("*"):
            rel_parts = path.relative_to(root).parts
            if any(part in EXCLUDE_DIRS for part in rel_parts):
                continue
            if path.is_file():
                zf.write(path, arcname=str(path.relative_to(root)))
                file_count += 1

    size_kb = zip_path.stat().st_size / 1024.0
    print(f"Snapshot OK : {zip_path}")
    print(f"Files saved : {file_count} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
