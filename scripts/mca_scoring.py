#!/usr/bin/env python3
"""Tính điểm đánh giá đa tiêu chí (MCA) và xếp hạng phương án quy hoạch / hướng tuyến."""

import argparse
import json
import sys
from pathlib import Path


def main() -> None:
    parser = argparse.ArgumentParser(description="Tính điểm MCA cho các phương án quy hoạch / hướng tuyến.")
    parser.add_argument("input_json", help="Đường dẫn file JSON chứa tiêu chí, trọng số và điểm các phương án")
    args = parser.parse_args()

    path = Path(args.input_json).expanduser().resolve()
    if not path.exists():
        print(f"[LỖI] Không tìm thấy file: {path}", file=sys.stderr)
        sys.exit(1)

    data = json.loads(path.read_text(encoding="utf-8"))
    criteria = data.get("criteria", [])
    alternatives = data.get("alternatives", [])

    if not criteria or not alternatives:
        print("[LỖI] File JSON cần có `criteria` và `alternatives`.", file=sys.stderr)
        sys.exit(1)

    total_weight = sum(float(c["weight"]) for c in criteria)
    if abs(total_weight - 100.0) > 1e-6:
        print(f"[LỖI] Tổng trọng số phải bằng 100%, hiện tại là {total_weight:.2f}%.", file=sys.stderr)
        sys.exit(1)

    results = []
    for alt in alternatives:
        scores = alt.get("scores", {})
        weighted_sum = 0.0
        breakdown = {}
        for c in criteria:
            cid = c["id"]
            if cid not in scores:
                print(f"[LỖI] Phương án `{alt['name']}` thiếu điểm cho tiêu chí `{cid}`.", file=sys.stderr)
                sys.exit(1)
            raw = float(scores[cid])
            contrib = raw * float(c["weight"]) / 100.0
            weighted_sum += contrib
            breakdown[cid] = (raw, contrib)
        results.append({"name": alt["name"], "total": weighted_sum, "breakdown": breakdown})

    results.sort(key=lambda x: x["total"], reverse=True)

    print(f"# Kết Quả Đánh Giá Đa Tiêu Chí (MCA): {data.get('title', path.stem)}\n")
    header = "| Tiêu chí | Trọng số (%) | " + " | ".join(r["name"] for r in results) + " |"
    sep = "| :--- | :---: | " + " | ".join(":---:" for _ in results) + " |"
    print(header)
    print(sep)

    for c in criteria:
        cid = c["id"]
        cols = [f"{r['breakdown'][cid][0]:.2f} ({r['breakdown'][cid][1]:.2f})" for r in results]
        print(f"| {c['name']} | {float(c['weight']):.1f}% | " + " | ".join(cols) + " |")

    totals_row = [f"**{r['total']:.2f}**" for r in results]
    print(f"| **TỔNG ĐIỂM CÓ TRỌNG SỐ** | **100.0%** | " + " | ".join(totals_row) + " |\n")

    print("## Xếp Hạng Phương Án")
    for idx, r in enumerate(results, start=1):
        delta = "" if idx == 1 else f" (kém hạng 1: {results[0]['total'] - r['total']:.2f} điểm)"
        print(f"{idx}. **{r['name']}** — **{r['total']:.2f}** điểm{delta}")


if __name__ == "__main__":
    main()
