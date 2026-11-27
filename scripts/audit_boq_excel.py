#!/usr/bin/env python3
"""Kiểm toán nhanh file Excel Tiên lượng khối lượng (BOQ) & Dự toán cho công tác thẩm tra."""

import argparse
import sys
from collections import Counter
from pathlib import Path

EXCEL_ERRORS = {"#REF!", "#DIV/0!", "#VALUE!", "#NAME?", "#N/A", "#NUM!", "#NULL!"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Kiểm toán tự động công thức, lỗi và bất thường trong file Excel dự toán/BOQ.")
    parser.add_argument("excel_file", help="Đường dẫn tới file .xlsx cần kiểm toán")
    parser.add_argument("--max-items", type=int, default=30, help="Số mục tối đa hiển thị cho mỗi loại cảnh báo")
    args = parser.parse_args()

    try:
        import openpyxl
    except ImportError:
        print(
            "[THIẾU THƯ VIỆN] Chưa cài `openpyxl`. Hãy cài bằng lệnh: pip install openpyxl",
            file=sys.stderr,
        )
        sys.exit(2)

    path = Path(args.excel_file).expanduser().resolve()
    if not path.exists():
        print(f"[LỖI] Không tìm thấy file: {path}", file=sys.stderr)
        sys.exit(1)

    wb_formulas = openpyxl.load_workbook(path, data_only=False)
    wb_values = openpyxl.load_workbook(path, data_only=True)

    print(f"# Báo Cáo Kiểm Toán Tự Động Excel: `{path.name}`")
    print(f"- **Số lượng sheet:** {len(wb_formulas.sheetnames)}")
    print(f"- **Danh sách sheet:** {', '.join(f'`{s}`' for s in wb_formulas.sheetnames)}\n")

    total_errors = 0
    total_hardcoded_in_formula_col = 0

    for sheet_name in wb_formulas.sheetnames:
        ws_f = wb_formulas[sheet_name]
        ws_v = wb_values[sheet_name]

        formula_count = 0
        number_count = 0
        error_cells = []
        col_formula_counts = Counter()
        col_number_cells = {}
        row_signatures = Counter()
        duplicate_rows = []

        for r in range(1, ws_f.max_row + 1):
            row_texts = []
            for c in range(1, ws_f.max_column + 1):
                val_f = ws_f.cell(r, c).value
                val_v = ws_v.cell(r, c).value
                coord = ws_f.cell(r, c).coordinate

                if isinstance(val_v, str) and val_v.strip().upper() in EXCEL_ERRORS:
                    error_cells.append((coord, val_v.strip(), repr(val_f)))
                elif isinstance(val_f, str) and val_f.strip().upper() in EXCEL_ERRORS:
                    error_cells.append((coord, val_f.strip(), repr(val_f)))

                if isinstance(val_f, str) and val_f.startswith("="):
                    formula_count += 1
                    col_formula_counts[c] += 1
                elif isinstance(val_f, (int, float)) and not isinstance(val_f, bool):
                    number_count += 1
                    col_number_cells.setdefault(c, []).append((coord, val_f))

                if isinstance(val_v, str) and len(val_v.strip()) >= 8:
                    row_texts.append(val_v.strip())

            if row_texts:
                sig = " | ".join(row_texts[:3])
                row_signatures[sig] += 1
                if row_signatures[sig] == 2:
                    duplicate_rows.append((r, sig))

        # Phát hiện ô nhập số cứng nằm trong cột chủ yếu dùng công thức (>= 5 công thức và >75% là công thức)
        suspicious_hardcoded = []
        for col_idx, f_cnt in col_formula_counts.items():
            nums = col_number_cells.get(col_idx, [])
            if f_cnt >= 5 and nums and (f_cnt / (f_cnt + len(nums))) >= 0.75:
                for coord, num_val in nums:
                    suspicious_hardcoded.append((coord, num_val))

        total_errors += len(error_cells)
        total_hardcoded_in_formula_col += len(suspicious_hardcoded)

        print(f"## Sheet: `{sheet_name}` ({ws_f.max_row} dòng x {ws_f.max_column} cột)")
        print(f"- Ô công thức: **{formula_count}** | Ô số nhập trực tiếp: **{number_count}**")
        print(f"- Lỗi công thức Excel: **{len(error_cells)}** | Ô nghi ngờ gõ cứng đè công thức: **{len(suspicious_hardcoded)}** | Dòng nội dung lặp lại: **{len(duplicate_rows)}**")

        if error_cells:
            print("\n### [NGHIÊM TRỌNG] Lỗi công thức phát hiện")
            for coord, err, raw in error_cells[: args.max_items]:
                print(f"- `{coord}`: `{err}` (biểu thức: `{raw}`)")

        if suspicious_hardcoded:
            print("\n### [CẦN LÀM RÕ] Ô nhập số cứng trong cột chủ yếu là công thức")
            for coord, num_val in suspicious_hardcoded[: args.max_items]:
                print(f"- `{coord}` = `{num_val}`")

        if duplicate_rows:
            print("\n### [CẦN LÀM RÕ] Nội dung hạng mục xuất hiện trùng lặp")
            for r_idx, sig in duplicate_rows[: args.max_items]:
                print(f"- Dòng `{r_idx}`: {sig}")

        print()

    print("---")
    print(
        f"**TỔNG KẾT:** Tổng lỗi công thức = **{total_errors}** | "
        f"Tổng ô nghi ngờ gõ cứng đè công thức = **{total_hardcoded_in_formula_col}**"
    )


if __name__ == "__main__":
    main()
