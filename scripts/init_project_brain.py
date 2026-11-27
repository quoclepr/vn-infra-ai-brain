#!/usr/bin/env python3
"""Khởi tạo cấu trúc thư mục chuẩn và bộ não dự án (GEMINI.md) trên Antigravity."""

import argparse
import subprocess
from datetime import datetime
from pathlib import Path

GITIGNORE_TEMPLATE = """# Thu muc sao luu & file tam
_Backups/
__pycache__/
*.pyc
~$*
*.tmp
*.bak
.DS_Store
Thumbs.db
"""

STANDARD_DIRS = [
    ".agents/rules",
    "01_PhapLy_TieuChuan",
    "02_KhaoSat_HienTrang",
    "03_ThietKe_QuyHoach",
    "04_DuToan_KhoiLuong",
    "05_ThamTra_RaSoat",
    "06_SanPham_TrinhDuyet",
]

TYPE_LABELS = {
    "thiet-ke": "Thiết kế dự án hạ tầng giao thông",
    "tham-tra": "Thẩm tra dự án",
    "quy-hoach": "Quy hoạch giao thông / đô thị",
}


def load_template() -> str:
    template_path = Path(__file__).resolve().parent.parent / "resources" / "GEMINI_template.md"
    return template_path.read_text(encoding="utf-8")


def build_decision_log(project_code: str, project_name: str, created_date: str) -> str:
    return (
        f"# Nhật Ký Quyết Định & Thay Đổi Đầu Bài — {project_name} (`{project_code}`)\n\n"
        "| Ngày | Hạng mục | Nội dung quyết định / thay đổi | Căn cứ (Họp / Văn bản) | Trạng thái cập nhật `GEMINI.md` |\n"
        "| :--- | :--- | :--- | :--- | :--- |\n"
        f"| {created_date} | Khởi tạo | Thiết lập cấu trúc thư mục chuẩn & bộ não dự án `GEMINI.md` | Khởi tạo hệ thống | Đã cập nhật |\n"
    )


def main() -> None:
    parser = argparse.ArgumentParser(description="Khởi tạo bộ não cho từng dự án hạ tầng/thẩm tra/quy hoạch.")
    parser.add_argument("--target", required=True, help="Đường dẫn thư mục gốc của dự án")
    parser.add_argument("--code", required=True, help="Mã dự án ngắn gọn (vd: DA-GT01)")
    parser.add_argument("--name", required=True, help="Tên đầy đủ của dự án")
    parser.add_argument(
        "--type",
        required=True,
        choices=list(TYPE_LABELS.keys()),
        help="Loại dự án: thiet-ke | tham-tra | quy-hoach",
    )
    parser.add_argument("--stage", default="[CHƯA CẬP NHẬT]", help="Giai đoạn đầu tư / quy hoạch")
    parser.add_argument("--git", action="store_true", help="Khởi tạo Git repository và .gitignore để dễ khôi phục")
    parser.add_argument("--force", action="store_true", help="Ghi đè GEMINI.md nếu đã tồn tại")
    args = parser.parse_args()

    root = Path(args.target).expanduser().resolve()
    root.mkdir(parents=True, exist_ok=True)

    created_dirs = []
    for rel in STANDARD_DIRS:
        d = root / rel
        if not d.exists():
            d.mkdir(parents=True, exist_ok=True)
            created_dirs.append(rel)

    created_date = datetime.now().strftime("%Y-%m-%d")
    gemini_path = root / "GEMINI.md"
    log_path = root / "00_NhatKy_QuyetDinh.md"

    if not gemini_path.exists() or args.force:
        content = load_template()
        content = (
            content.replace("{{PROJECT_NAME}}", args.name)
            .replace("{{PROJECT_CODE}}", args.code)
            .replace("{{PROJECT_TYPE}}", TYPE_LABELS[args.type])
            .replace("{{PROJECT_STAGE}}", args.stage)
            .replace("{{CREATED_DATE}}", created_date)
        )
        gemini_path.write_text(content, encoding="utf-8")
        gemini_status = "CREATED" if not args.force else "WRITTEN (force)"
    else:
        gemini_status = "SKIPPED (already exists)"

    if not log_path.exists() or args.force:
        log_path.write_text(build_decision_log(args.code, args.name, created_date), encoding="utf-8")
        log_status = "CREATED"
    else:
        log_status = "SKIPPED (already exists)"

    git_status = "NOT REQUESTED"
    if args.git:
        gitignore_path = root / ".gitignore"
        if not gitignore_path.exists():
            gitignore_path.write_text(GITIGNORE_TEMPLATE, encoding="utf-8")
        if not (root / ".git").exists():
            try:
                res = subprocess.run(["git", "init"], cwd=root, capture_output=True, text=True)
                git_status = "INITIALIZED" if res.returncode == 0 else f"FAILED ({res.stderr.strip()})"
            except FileNotFoundError:
                git_status = "SKIPPED (git chưa cài trên PATH — dùng snapshot_project.py thay thế)"
        else:
            git_status = "ALREADY EXISTS"

    print(f"Project Root : {root}")
    print(f"GEMINI.md    : {gemini_status} ({gemini_path.stat().st_size} bytes)")
    print(f"Decision Log : {log_status}")
    print(f"Git Repo     : {git_status}")
    print(f"New Folders  : {len(created_dirs)} ({', '.join(created_dirs) if created_dirs else 'none'})")


if __name__ == "__main__":
    main()
