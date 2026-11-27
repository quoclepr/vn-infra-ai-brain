#!/usr/bin/env python3
"""Tạo bản sao lưu nén (.zip) an toàn cho thư mục dự án trước các thao tác lớn."""

import argparse
import os
import re
import stat
import zipfile
from datetime import datetime
from fnmatch import fnmatchcase
from pathlib import Path

EXCLUDE_DIRS = {
    "_backups", "backups", ".git", "__pycache__", "node_modules", ".venv", "venv",
    ".ssh", ".aws", ".azure", "gcloud",
}
# Keep aligned with SECRET_GITIGNORE in init_project_brain.py.
SECRET_PATTERNS = (
    ".env", ".env.*", "*.pem", "*.key", "*.p12", "*.pfx",
    "id_rsa*", "id_dsa*", "id_ecdsa*", "id_ed25519*",
    ".git-credentials", ".netrc", "_netrc", ".npmrc", ".pypirc",
    "*secret*", "*token*", "*credential*",
)


def is_link(path: Path) -> bool:
    info = path.lstat()
    # Windows junctions and other reparse points can also redirect file access.
    return stat.S_ISLNK(info.st_mode) or bool(
        getattr(info, "st_file_attributes", 0)
        & getattr(stat, "FILE_ATTRIBUTE_REPARSE_POINT", 0)
    )


def should_exclude(path: Path) -> bool:
    name = path.name.casefold()
    return (
        name in EXCLUDE_DIRS
        or any(fnmatchcase(name, pattern) for pattern in SECRET_PATTERNS)
        or is_link(path)
    )


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
    if backup_dir.exists() and is_link(backup_dir):
        raise SystemExit("[LỖI] _Backups phải là thư mục thật, không phải liên kết.")
    backup_dir.mkdir(parents=True, exist_ok=True)

    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    label = sanitize_label(args.label)
    zip_path = backup_dir / f"{ts}_{root.name}_{label}.zip"

    file_count = 0
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED) as zf:
        for directory, dirs, files in os.walk(root, topdown=True, followlinks=False):
            parent = Path(directory)
            # Prune before descent; do not inspect contents of excluded directories.
            dirs[:] = [name for name in dirs if not should_exclude(parent / name)]
            for name in files:
                path = parent / name
                if not should_exclude(path) and path.is_file():
                    zf.write(path, arcname=str(path.relative_to(root)))
                    file_count += 1

    size_kb = zip_path.stat().st_size / 1024.0
    print(f"Snapshot OK : {zip_path}")
    print(f"Files saved : {file_count} ({size_kb:.1f} KB)")


if __name__ == "__main__":
    main()
