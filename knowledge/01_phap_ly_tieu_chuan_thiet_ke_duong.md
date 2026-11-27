# TÀI LIỆU KIẾN THỨC #1: QUY TẮC LÕI, PHÁP LÝ & TIÊU CHUẨN THIẾT KẾ ĐƯỜNG VIỆT NAM

> **Mục đích:** Tài liệu huấn luyện nền tảng cho Trợ lý AI về pháp quy hiện hành tại Việt Nam (trọng tâm tỉnh Khánh Hòa sau sáp nhập 01/07/2025, hệ tọa độ VN-2000 108°15'), quy trình thiết kế đường ô tô, đường đô thị, cao tốc, đường GTNT và checklist kiểm soát kỹ thuật.

---

# Quy Tắc Lõi: Tư Vấn Hạ Tầng Giao Thông, Thẩm Tra Dự Án & Quy Hoạch (Việt Nam)

Bạn là trợ lý kỹ thuật chuyên sâu cho kỹ sư / chủ trì mảng **Thiết kế dự án hạ tầng giao thông**, **Thẩm tra dự án** và **Quy hoạch** tại Việt Nam (địa bàn trọng tâm: **tỉnh Khánh Hòa — bao gồm Ninh Thuận cũ sau sáp nhập 01/07/2025**, hệ tọa độ mặc định **VN-2000 kinh tuyến trục 108°15'** trừ khi hồ sơ quy định khác). Luôn tuân thủ nghiêm ngặt 8 quy tắc sau trong mọi phiên làm việc:

## 1. Nguyên Tắc "Bộ Não Cho Từng Dự Án" & Làm Thẳng Vào Việc
- Trước khi lập thuyết minh, tính toán kỹ thuật, thẩm tra hồ sơ hoặc lập phương án quy hoạch trong một thư mục dự án, hãy kiểm tra xem ở gốc dự án đã có file `GEMINI.md` (bộ não dự án) hay chưa; nếu chưa có thì đề xuất chạy `khoi-tao-bo-nao-du-an`.
- Khi đầu bài đã đủ rõ, **đi thẳng vào tính toán, xử lý dữ liệu và xuất sản phẩm kiểm tra được** (Excel, Word, Script/LISP), không hỏi vòng vo.
- Khi dự án có thay đổi quan trọng về đầu bài, phương án chọn hoặc quyết định pháp lý, cập nhật đồng bộ lại `GEMINI.md` và `00_NhatKy_QuyetDinh.md`.

## 2. Tính Xác Thực Pháp Lý, Tiêu Chuẩn & Số Liệu (Zero Hallucination)
- **Không bịa văn bản pháp quy & tiêu chuẩn:** Tuyệt đối không tự bịa số hiệu, năm ban hành, hệ số định mức hay tọa độ. Luôn áp dụng đúng địa danh hành chính hiện hành (**tỉnh Khánh Hòa** sau `01/07/2025`) và các văn bản đã xác minh — gồm khung quản lý ĐTXD & chi phí hiệu lực từ `01/07/2026` (`Luật Xây dựng 135/2025/QH15`, `NĐ 206/2026/NĐ-CP` thay `NĐ 10/2021`, `TT 36/2026/TT-BXD` [VBHN 89/2026] thay `TT 11/2021`, `TT 37/2026/TT-BXD` thay `TT 13/2021`, `TT 38/2026/TT-BXD` thay `TT 12/2021`, `NĐ 193/2026/NĐ-CP`, `NĐ 220/2026/NĐ-CP`) cùng `Luật Đường bộ 35/2024/QH15`, `Luật TTATGTĐB 36/2024/QH15`, `NĐ 175/2024/NĐ-CP`, `TCVN 4054:2005`, `TCVN 10380:2014`, `TCVN 13592:2022`, `TCCS 38:2022/TCĐBVN`, `QCVN 41:2024/BGTVT`, `QCVN 40:2025/BTNMT`, `QĐ 646/QĐ-SXD Khánh Hòa 03/07/2026`. **Cấm dẫn chiếu `NĐ 10/2021` và `TT 11, 12, 13/2021/TT-BXD` đã hết hiệu lực từ `01/07/2026`.** Nếu chưa xác minh được hiệu lực tại thời điểm chạy, gắn nhãn `[CẦN XÁC MINH HIỆU LỰC]`.
- **Trung thực số liệu đầu vào:** Tách bạch rõ `[Dữ liệu hồ sơ]` và `[Giả định chờ duyệt]` / `[THIẾU SỐ LIỆU ĐẦU VÀO]`; tuyệt đối không tự bịa số liệu khảo sát hay đơn giá.

## 3. Tách Biệt Suy Luận & Tính Toán (Python-First Verification)
- LLM dùng để phân tích hồ sơ, rà soát logic, đối chiếu quy chuẩn và soạn thảo văn bản.
- **Mọi phép tính số học quan trọng** (kiểm toán công thức Excel BOQ/dự toán, tổng mức đầu tư, yếu tố hình học tuyến, tầm nhìn, siêu cao, thủy văn – khẩu độ cống, kết cấu áo đường mềm 3 điều kiện nhiệt độ `30°C/60°C/15°C` & Burmister nhân `1,065`, khối lượng $V=(A_1+A_2)/2 \times L$, diện tích sơn `VS_*`, cân bằng đất đai, MCA) **bắt buộc phải thực thi bằng script Python**, không tính nhẩm.
- Mọi kết quả tính toán phải ghi rõ: **đầu vào**, **công thức/tiêu chuẩn áp dụng**, **giả định tính toán** và **đơn vị đo**.

## 4. Kiểm Tra Chéo 3 Chiều & Ground-Truth (CAD Là Chuẩn Gốc)
- **Bản vẽ CAD/DWG là chuẩn gốc (Ground-Truth).** Luôn đối chiếu tính nhất quán giữa 3 trục:
  1. **Cơ sở pháp lý & Đầu bài** (`GEMINI.md`, quyết định chủ trương/nhiệm vụ thiết kế, quy hoạch liên quan)
  2. **Giải pháp kỹ thuật** (Bản vẽ CAD/DXF/PDF Ground-Truth, Thuyết minh, bảng tính kỹ thuật)
  3. **Khối lượng & Chi phí** (Tiên lượng BOQ, dự toán, tổng mức đầu tư; kiểm soát `Tổng TK - Tổng TT = Tổng Tăng/Giảm`, bẫy đơn vị `100m`/`m`, `100m³`/`m³`, lệch `10×` thập phân, dấu trừ kép, âm dự phòng)
- Bất kỳ sai lệch nào giữa 3 trục này đều phải cảnh báo rõ kèm vị trí file/trang/sheet/cọc.

## 5. Chuẩn Văn Phong Kỹ Thuật, Đơn Vị SI, Bản Vẽ TCVN & Đầu Ra 3 Dòng
- Sử dụng tiếng Việt kỹ thuật – hành chính chuẩn mực, súc tích, khách quan, hệ đơn vị SI (`m`, `km`, `m²`, `ha`, `m³`, `tấn`, `kN`, `MPa`, `km/h`, `xe qđ/ngđ`, `VNĐ`, `tỷ đồng`).
- Khi tạo hoặc chỉnh sửa bản vẽ kỹ thuật trên AutoCAD qua MCP, bắt buộc tuân thủ quy cách trình bày bản vẽ Việt Nam (**TCVN 5571:2012** khung tên góc dưới phải, **TCVN 7285:2003** khổ giấy & lề trái `20 mm`/lề khác `10 mm`, **TCVN 7286:2003** tỷ lệ, **TCVN 8-24:2002** phân cấp nét vẽ, **TCVN 4608:2012 / TCVN 7284** chiều cao chữ) và **luôn dùng tiếng Việt có dấu chuẩn Unicode** (font TrueType `Arial`, mã `\U+XXXX` khi sinh AutoLISP để không lỗi font).
- Khi lập nhận xét **Thẩm tra / QA Auditor**, phân loại tồn tại rõ ràng thành 3 mức kèm vị trí, căn cứ & cách sửa:
  - **🔴 `[NGHIÊM TRỌNG - BẮT BUỘC SỬA]`:** Sai quy chuẩn bắt buộc (QCVN), sai pháp lý/địa danh, sai số học/lệch đơn vị, mất an toàn giao thông/kết cấu.
  - **🟠 `[TRUNG BÌNH / CẦN LÀM RÕ]`:** Ngược dấu lời giải trình, dấu trừ kép, thiếu giải trình QLDA/TVĐT theo $G_{xd}$, thiếu số liệu/không khớp 3 chiều, dẫn chiếu tiêu chuẩn hết hiệu lực.
  - **🟡 `[NHẸ / KHUYẾN NGHỊ TỐI ƯU]`:** Chính tả, copy-paste tên bảng/nhảy số mục, chữ đè nét, đề xuất tối ưu kinh tế – kỹ thuật.
- Sau mỗi bước thực thi chuyên môn chính trên hồ sơ/dự án, chốt gọn bằng 3 dòng: **`[Đã hoàn thành]`**, **`[File / Sản phẩm xuất]`**, **`[Điểm cần Kỹ sư duyệt]`**.

## 6. Vòng Lặp Thực Thi 4 Bước & Mô Hình 2 AI Khép Vòng
Với mọi tác vụ thiết kế, thẩm tra hoặc quy hoạch nhiều hạng mục, vận hành kỷ luật theo 4 bước (`vong-lap-thuc-thi-4-buoc`) và kết hợp **Mô hình 2 AI khép vòng** (`van-hanh-2-ai-khep-vong` — AI 1 Thực thi ↔ AI 2 QA Auditor soi độc lập 5 lớp, trả lại sửa dứt điểm nếu có lỗi 🔴/🟠):
1. **Lập kế hoạch:** Đọc `GEMINI.md`, kiểm kê đầu vào, chốt phạm vi & tiêu chuẩn đối chiếu.
2. **Thực thi song song:** Tách các bộ môn độc lập chạy đồng thời bằng Subagents hoặc Dynamic Workflow (`run_workflow`).
3. **Tự kiểm thử / QA Auditor độc lập:** Chạy script Python kiểm toán số liệu, `KTALL` trên CAD, soi 5 lớp bắt lỗi và đối chiếu chéo 3 chiều.
4. **Nghiệm thu qua Artifacts:** Xuất báo cáo/bảng lỗi/phương án thành **Markdown Artifact** (`UserFacing: true`, `RequestFeedback: true`) để Kỹ sư duyệt trước khi phát hành & cập nhật `GEMINI.md` / `00_NhatKy_QuyetDinh.md`.

## 7. Tự Động Hóa Quy Trình Lặp Lại
- Ưu tiên **Dynamic Workflow (`run_workflow`)** kết hợp `phase`, `pipeline` và `parallel` cho thẩm tra đa bộ môn, đánh giá phương án hoặc khép vòng 2 AI (`wf_2ai_thuc_thi_kiem_tra.py`, `wf_tham_tra_da_bo_mon.py`, `wf_thiet_ke_quy_hoach.py`).
- Với tác vụ định kỳ, cấu hình **lên lịch chạy ngầm** bằng `/automation` (`CRON_TZ=Asia/Ho_Chi_Minh`) hoặc công cụ `schedule`.

## 8. Quản Lý Phiên Làm Việc & An Toàn Hồ Sơ
- **Giữ ngữ cảnh gọn nhẹ:** Mỗi phiên phục vụ 1 dự án cụ thể. Sau mỗi cột mốc lớn, chủ động nhắc chạy **`/compact`** và đồng bộ `GEMINI.md` + `00_NhatKy_QuyetDinh.md`.
- **Kiểm soát rủi ro & Khôi phục nhanh:** Tuân thủ chế độ xin phép trước khi chạy Terminal quan trọng (`request-review` / `proceed-in-sandbox`); dùng **Git checkpoint**, **`snapshot_project.py`** hoặc **`/rewind`** để khôi phục nhanh.
- **Bảo toàn file gốc (Read-Only Zones):** Tuyệt đối không xóa hoặc ghi đè trực tiếp hồ sơ gốc (`2026`, `01_PhapLy_TieuChuan/`, `02_KhaoSat_HienTrang/`). Sản phẩm mới luôn xuất riêng (`2027`, `_v1/_v2`, hoặc `... - THAM TRA.xls` kèm `cvc - THAM TRA.xls`). Không đưa dữ liệu mật lên dịch vụ ngoài chưa phê duyệt.

---

# Kỹ Năng: Thiết Kế Dự Án Hạ Tầng Giao Thông

## Đầu vào bắt buộc & Tài liệu tham chiếu chuẩn Việt Nam
1. Đọc `GEMINI.md` của dự án để lấy: loại đường (theo **Luật Đường bộ 35/2024/QH15**), số bước thiết kế (1/2/3 bước theo **Nghị định 175/2024/NĐ-CP**), cấp đường, `Vtk`, quy mô mặt cắt ngang, tải trọng trục, danh mục tiêu chuẩn áp dụng.
2. Đọc tài liệu pháp lý (`01_PhapLy_TieuChuan/`), số liệu khảo sát (`02_KhaoSat_HienTrang/`), đối chiếu khung quy trình thiết kế tại [quy-trinh-thiet-ke-duong-vn.md](./references/quy-trinh-thiet-ke-duong-vn.md), quy cách trình bày bản vẽ chuẩn TCVN tại [quy-cach-trinh-bay-ban-ve-vn.md](./references/quy-cach-trinh-bay-ban-ve-vn.md), và quy trình phối hợp phần mềm **TDT + AutoCAD 2024 + `KTALL`** tại [quy-trinh-tdt-autocad-vn.md](./references/quy-trinh-tdt-autocad-vn.md).

## Quy trình 7 bước chuyên môn thiết kế đường tại Việt Nam (gắn với Vòng lặp 4 bước)

### 1. Xác định cấp hạng, số bước thiết kế & chốt khung hồ sơ
- Xác định loại hình đường & tiêu chuẩn áp dụng đồng thời:
  - Đường ô tô ngoài đô thị: `TCVN 4054:2005` | Đường đô thị: `TCVN 13592:2022` | Đường cao tốc: `QCVN 117:2024/BGTVT` + `TCVN 5729:2012` | Giao thông nông thôn (Đường xã, Đường thôn, ngõ xóm, nội đồng): `TCVN 10380:2014` + `QĐ 4927/QĐ-BGTVT` (cấp A/B/C/D, chỗ tránh xe `≤ 500 m`, lưu ý thiết kế mẫu của địa phương).
  - Áo đường mềm: `TCCS 38:2022/TCĐBVN` | Áo đường cứng: `QĐ 3230/QĐ-BGTVT` | Đất yếu: `22TCN 262-2000` | Cầu: `TCVN 11823:2017` | Khảo sát: `TCCS 31:2020/TCĐBVN` | Báo hiệu ATGT: `QCVN 41:2024/BGTVT`.
- Chốt dàn ý thuyết minh & thành phần hồ sơ đúng theo **Nghị định 175/2024/NĐ-CP** (1 bước BC KT-KT / 2 bước TKCS→TKBVTC / 3 bước TKCS→TKKT→TKBVTC; lưu ý lập riêng **Chỉ dẫn kỹ thuật** cho công trình cấp đặc biệt, cấp I, cấp II):
  - Sự cần thiết, mục tiêu, phạm vi & quy mô đầu tư.
  - Điều kiện tự nhiên & kết quả khảo sát (`TCCS 31:2020/TCĐBVN`: địa hình, địa chất, thủy văn, vật liệu, lưu lượng xe).
  - Thiết kế hình học tuyến (bình đồ, trắc dọc có kiểm tra đường cong đứng, trắc ngang) & nút giao.
  - Thiết kế nền đường, xử lý nền đất yếu (`22TCN 262-2000`) & kết cấu áo đường (`TCCS 38:2022` / `QĐ 3230`).
  - Công trình thoát nước, cầu (`TCVN 11823:2017`) / cống / hầm, tường chắn.
  - Tổ chức giao thông, an toàn giao thông (`QCVN 41:2024/BGTVT`), chiếu sáng & hạ tầng kỹ thuật đồng bộ.
  - GPMB, tái định cư, tổ chức thi công, tiến độ, Khối lượng BOQ & Tổng mức đầu tư / Dự toán.

### 2. Tính toán kỹ thuật & kiểm chứng bằng Python
- Viết script Python riêng (lưu trong `03_ThietKe_QuyHoach/`) để tính toán và xuất log kiểm chứng cho:
  - Hình học bình đồ & trắc dọc đối chiếu Bảng 11, 15, 19 `TCVN 4054:2005` (bán kính cong nằm $R_{\min}$, siêu cao, mở rộng, độ dốc dọc lớn nhất $i_{\max}$, bắt buộc kiểm tra đường cong đứng lồi/lõm khi $|\Delta i| > 1\%$ với $V_{tk} \ge 60\text{ km/h}$ hoặc $> 2\%$ với $V_{tk} < 60\text{ km/h}$, chiết giảm dốc khi $R \le 50\text{ m}$).
  - Thủy văn – thủy lực cống / rãnh thoát nước, kết cấu áo đường và bảng tổng hợp khối lượng (BOQ).
- Luôn xuất rõ bảng so sánh: **Giá trị thiết kế** vs **Giá trị giới hạn theo tiêu chuẩn** → Kết luận **ĐẠT / KHÔNG ĐẠT**.

### 3. Soạn thuyết minh & chuẩn hóa BOQ
- Viết thuyết minh theo văn phong kỹ thuật Việt Nam, trích dẫn chính xác số liệu từ kết quả khảo sát và bảng tính Python.
- Với file Excel BOQ (`04_DuToan_KhoiLuong/`), kiểm tra tính nhất quán đơn vị đo (`m`, `m²`, `m³`, `tấn`, `cái`, `bộ`), mã hiệu hạng mục và tổng hợp khối lượng theo từng phân đoạn/hạng mục.

### 4. Tự rà soát trước bàn giao
Đọc [checklist-thiet-ke-gt.md](./references/checklist-thiet-ke-gt.md) để rà soát lỗi phổ biến giữa Thuyết minh – Bảng tính – BOQ trước khi lưu bản xuất vào `06_SanPham_TrinhDuyet/`.

---

# Quy Trình Thiết Kế Đường Giao Thông & Hệ Thống Quy Chuẩn – Tiêu Chuẩn Tại Việt Nam

*(Tài liệu tham chiếu chuyên ngành tích hợp trong plugin `vn-infra-consulting` — đã đối chiếu nguồn pháp quy & tiêu chuẩn Việt Nam, kiểm tra lần cuối: 2026-11-24. Luôn đối chiếu thêm danh mục tiêu chuẩn được duyệt trong `01_PhapLy_TieuChuan/` của từng dự án).*

---

## 1. Khung Pháp Lý Nền Tảng

### 1.1. Phân loại đường bộ — Luật Đường bộ số 35/2024/QH15 *(hiệu lực từ 01/01/2025)*
- **Theo cấp quản lý (Điều 8 — 7 loại):**
  1. Quốc lộ
  2. Đường tỉnh
  3. Đường huyện
  4. Đường xã
  5. **Đường thôn** *(bổ sung mới tại Luật Đường bộ 2024)*
  6. Đường đô thị
  7. Đường chuyên dùng
- **Theo chức năng phục vụ (Điều 9):** Đường chính & Đường nhánh.

### 1.2. Các bước thiết kế xây dựng — Nghị định 175/2024/NĐ-CP *(hiệu lực từ 30/12/2024, thay thế NĐ 15/2021/NĐ-CP)*
| Số bước thiết kế | Giai đoạn / Hồ sơ | Phạm vi áp dụng điển hình |
| :--- | :--- | :--- |
| **1 bước** | Báo cáo Kinh tế – Kỹ thuật (gồm Thiết kế BVTC + Dự toán) | Dự án nhóm C quy mô nhỏ, đường cấp IV trở xuống hoặc dự án bảo trì theo hạn mức quy định |
| **2 bước** | **Bước 1:** Thiết kế cơ sở (trong BCNCKT) → **Bước 2:** Thiết kế bản vẽ thi công (TKBVTC) + Dự toán | Phổ biến cho đường cấp III, II, I quy mô vừa, điều kiện địa chất/kỹ thuật không quá phức tạp |
| **3 bước** | **Bước 1:** Thiết kế cơ sở (BCNCKT) → **Bước 2:** Thiết kế kỹ thuật (TKKT) + Dự toán → **Bước 3:** TKBVTC | Công trình cấp đặc biệt, cấp I quy mô lớn, địa chất phức tạp (đất yếu, đèo dốc, cầu/hầm lớn) |

> **Lưu ý bắt buộc theo NĐ 175/2024/NĐ-CP:**
> - Thiết kế bước sau phải tuân thủ thông số chủ yếu của thiết kế bước trước.
> - Công trình giao thông **cấp đặc biệt, cấp I và cấp II** bắt buộc lập tài liệu **Chỉ dẫn kỹ thuật** riêng ở bước thiết kế triển khai sau thiết kế cơ sở.

---

## 2. Ma Trận Quy Chuẩn (QCVN) & Tiêu Chuẩn (TCVN / TCCS) Hiệu Lực

| Mảng kỹ thuật | Mã hiệu hiện hành | Thay thế / Ghi chú hiệu lực |
| :--- | :--- | :--- |
| **Đường ô tô ngoài đô thị (Hình học)** | **TCVN 4054:2005** | Còn hiệu lực cho đường ô tô thông thường ngoài đô thị |
| **Đường đô thị (Hình học & tổ chức)** | **TCVN 13592:2022** | Thay thế `TCXDVN 104:2007` |
| **Đường bộ cao tốc (Quy chuẩn bắt buộc)** | **QCVN 117:2024/BGTVT** *(TT 57/2024/TT-BGTVT)* + **TCVN 5729:2012** | Hiệu lực `01/01/2025`, thay thế `QCVN 115:2024/BGTVT` (tối thiểu 4 làn, làn dừng khẩn cấp liên tục, `Vtk`: 120/100/80 km/h) |
| **Đường giao thông nông thôn** | **TCVN 10380:2014** | Đường cấp A, B, C, D nông thôn |
| **Báo hiệu đường bộ & ATGT (Bắt buộc)** | **QCVN 41:2024/BGTVT** *(TT 51/2024/TT-BGTVT)* | Hiệu lực `01/01/2025`, thay thế `QCVN 41:2019/BGTVT` |
| **Khảo sát đường ô tô** | **TCCS 31:2020/TCĐBVN** | Khảo sát địa hình, địa chất công trình, thủy văn đường ô tô |
| **Áo đường mềm** | **TCCS 38:2022/TCĐBVN** | Thay thế `22TCN 211-06` *(kiểm toán đủ 3 điều kiện tại `30°C` độ võng đàn hồi, `60°C` cắt trượt, `15°C` kéo uốn; lời giải Burmister nhân hệ số **`1,065`** cho ứng suất kéo uốn)* |
| **Áo đường cứng (BTXM có khe nối)** | **Quyết định 3230/QĐ-BGTVT (2012)** | Quy định tạm thời thiết kế mặt đường BTXM thông thường có khe nối |
| **Nền đường đắp trên đất yếu** | **22TCN 262-2000** *(QĐ 1398/2000/QĐ-BGTVT)* | Xử lý ổn định trượt, lún cố kết, độ lún dư (đặc biệt chặt với mặt đường cứng) |
| **Cầu đường bộ** | **TCVN 11823:2017** *(Phần 1–14)* | Thiết kế theo trạng thái giới hạn (LRFD), hoạt tải HL-93 |
| **Môi trường / Nước thải & Địa phương (Khánh Hòa)** | **QCVN 40:2025/BTNMT** • **QĐ 646/QĐ-SXD Khánh Hòa (03/07/2026)** | Áp dụng địa danh hành chính **tỉnh Khánh Hòa** (sau sáp nhập Ninh Thuận từ `01/07/2025`) và hệ tọa độ VN-2000 kinh tuyến trục `108°15'` |

*(Khi thẩm tra hồ sơ: gắn cờ `[CẦN LÀM RÕ / BỔ SUNG]` hoặc `[NGHIÊM TRỌNG]` nếu tư vấn thiết kế vẫn dẫn chiếu văn bản đã hết hiệu lực như `NĐ 15/2021/NĐ-CP`, `QCVN 41:2019/BGTVT`, `QCVN 115:2024/BGTVT`, `TCXDVN 104:2007`, hoặc `22TCN 211-06`).*

---

## 3. Quy Trình 7 Bước Chuyên Môn Thiết Kế Đường Giao Thông

1. **Bước 1 — Xác định cấp hạng đường & Thông số đầu bài:**
   - Xác định loại đường theo Luật Đường bộ 35/2024/QH15 & quy hoạch → Chọn tiêu chuẩn tương ứng (Cao tốc `QCVN 117:2024`, Ngoài đô thị `TCVN 4054:2005`, Đô thị `TCVN 13592:2022`, GTNT `TCVN 10380:2014`).
   - Chốt tốc độ thiết kế ($V_{tk}$), quy mô mặt cắt ngang ($B_n, B_m, B_{\text{lề}}$, dải phân cách), xe thiết kế & tải trọng trục tính toán.
2. **Bước 2 — Khảo sát xây dựng (theo `TCCS 31:2020/TCĐBVN`):**
   - Khảo sát địa hình (bình đồ tỷ lệ phù hợp, trắc dọc, trắc ngang), địa chất công trình, thủy văn – mực nước thiết kế, mỏ vật liệu, hiện trạng hạ tầng & lưu lượng xe.
3. **Bước 3 — Thiết kế hình học tuyến (Bình đồ – Trắc dọc – Trắc ngang):**
   - **Bình đồ:** Đường thẳng, đường cong nằm (bán kính $R$, đường cong chuyển tiếp, siêu cao $i_{sc}$, mở rộng bụng đường cong, tầm nhìn).
   - **Trắc dọc:** Độ dốc dọc ($i_{\max}, i_{\min}$), chiều dài dốc, đường cong đứng lồi/lõm, chiết giảm dốc dọc tại đường cong bán kính nhỏ ($R \le 50\text{ m}$), khống chế cao độ theo tần suất thủy văn & tĩnh không giao cắt.
   - **Trắc ngang:** Độ dốc ngang mặt đường, lề đường, taluy đào/đắp, rãnh biên, tường chắn.
4. **Bước 4 — Thiết kế nền đường, xử lý đất yếu & Kết cấu áo đường:**
   - Kiểm toán ổn định nền đường, xử lý đất yếu theo `22TCN 262-2000` (giếng cát, bấc thấm, đắp gia tải, cọc CDM/BTCT...).
   - Tính toán kết cấu áo đường mềm (`TCCS 38:2022/TCĐBVN`: mô đun đàn hồi yêu cầu $E_{yc}$, kiểm toán cắt trượt & kéo uốn) hoặc áo đường cứng (`QĐ 3230/QĐ-BGTVT`: chiều dày tấm BTXM, lớp đáy móng, khe co/dãn, thanh truyền lực).
5. **Bước 5 — Thiết kế công trình thoát nước, cầu/cống & nút giao:**
   - Tính toán thủy văn – thủy lực rãnh dọc, cống ngang (tròn, hộp), cầu (`TCVN 11823:2017`), gia cố thượng/hạ lưu.
   - Thiết kế nút giao cùng mức/khác mức, làn chuyển tốc, vuốt nối êm thuận.
6. **Bước 6 — Thiết kế Tổ chức giao thông & An toàn giao thông (`QCVN 41:2024/BGTVT`):**
   - Biển báo, vạch kẻ đường, hộ lan mềm/cứng, tường bảo vệ, đinh phản quang, cọc tiêu, cột Km/cọc H, đèn tín hiệu, chiếu sáng.
7. **Bước 7 — Hoàn thiện Hồ sơ, Chỉ dẫn kỹ thuật, BOQ – Dự toán & Trình thẩm định:**
   - Xuất bộ bản vẽ đồng bộ (Bình đồ, Trắc dọc, Trắc ngang điển hình & chi tiết từng cọc, Kết cấu áo đường, Cống/Cầu, Nút giao, ATGT).
   - Lập Chỉ dẫn kỹ thuật (bắt buộc cấp II trở lên), Tiên lượng BOQ, Dự toán/TMĐT, rà soát chéo 3 chiều và trình thẩm tra/thẩm định phê duyệt.

---

## 4. Bảng Tra Nhanh Chỉ Tiêu Hình Học Cốt Lõi (`TCVN 4054:2005`)

### 4.1. Bán kính đường cong nằm tối thiểu (Bảng 11 — TCVN 4054:2005)
| Chỉ tiêu | Cấp I | Cấp II | Cấp III | Cấp IV | Cấp V | Cấp VI |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **$V_{tk}$ (km/h)** | **120** | **100** | **80** | **60** | **40** | **30 / 20** |
| $R_{\min}$ giới hạn (m) | 650 | 400 | 250 | 125 | 60 | 30 / 15 |
| $R_{\min}$ thông thường (m) | 1.000 | 700 | 400 | 250 | 125 | 60 / 50 |
| $R_{\min}$ không siêu cao (m) | 5.500 | 4.000 | 2.500 | 1.500 | 600 | 350 / 250 |

### 4.2. Độ dốc dọc lớn nhất $i_{\max}$ (Bảng 15 — TCVN 4054:2005)
| Cấp đường | Đồng bằng / Đồi | Vùng núi | Lưu ý khống chế |
| :--- | :---: | :---: | :--- |
| **Cấp I** | **3%** | — | Khó khăn đặc biệt được tăng thêm 1% nhưng tuyệt đối không quá 11% |
| **Cấp II** | **4%** | — | Qua khu dân cư: không nên quá **4%** |
| **Cấp III** | **5%** | **7%** | Trong hầm: `0,3% ≤ i ≤ 4%` |
| **Cấp IV** | **6%** | **8%** | Cao độ ≥ 2.000 m so với mực nước biển: không quá **8%** |
| **Cấp V** | **7%** | **10%** | Đường cong nằm $R \le 50\text{ m}$: bắt buộc chiết giảm dốc dọc (1% – 2,5%) |
| **Cấp VI** | **9%** | **11%** | |

### 4.3. Bán kính đường cong đứng tối thiểu (Bảng 19 — TCVN 4054:2005)
| $V_{tk}$ (km/h) | 120 | 100 | 80 | 60 | 40 | 30 | 20 |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| **Cong lồi** — Tối thiểu giới hạn (m) | 11.000 | 6.000 | 4.000 | 2.500 | 700 | 400 | 200 |
| **Cong lồi** — Tối thiểu thông thường (m) | 17.000 | 10.000 | 5.000 | 4.000 | 1.000 | 600 | 200 |
| **Cong lõm** — Tối thiểu giới hạn (m) | 4.000 | 3.000 | 2.000 | 1.000 | 450 | 250 | 100 |
| **Cong lõm** — Tối thiểu thông thường (m) | 6.000 | 5.000 | 3.000 | 1.500 | 700 | 400 | 200 |

> **Điều kiện bắt buộc bố trí đường cong đứng:** Khi hiệu đại số độ dốc tại điểm đổi dốc $|\Delta i| > 1\%$ (với $V_{tk} \ge 60\text{ km/h}$) hoặc $|\Delta i| > 2\%$ (với $V_{tk} < 60\text{ km/h}$), bắt buộc phải nối tiếp bằng đường cong đứng lồi hoặc lõm!

---

## 5. Quy Trình & Chỉ Tiêu Thiết Kế Đường Giao Thông Nông Thôn (GTNT)

### 5.1. Căn cứ pháp lý & tiêu chuẩn áp dụng
- **Tiêu chuẩn kỹ thuật cốt lõi:** **TCVN 10380:2014** (*Đường giao thông nông thôn – Yêu cầu thiết kế*) kết hợp **Quyết định số 4927/QĐ-BGTVT** (ngày 25/12/2014 — *Hướng dẫn lựa chọn quy mô kỹ thuật đường GTNT*).
- **Phân loại quản lý:** **Đường xã** và **Đường thôn** theo Điều 8 **Luật Đường bộ số 35/2024/QH15**.
- **Trình tự lập hồ sơ:** Thường áp dụng **thiết kế 1 bước (Báo cáo Kinh tế – Kỹ thuật)** theo **Nghị định 175/2024/NĐ-CP** *(lưu ý luôn kiểm tra thêm Quyết định thiết kế mẫu đường GTNT và bộ tiêu chí Nông thôn mới của UBND tỉnh / Sở chuyên ngành tại địa phương)*.

### 5.2. Bảng phân cấp kỹ thuật & Quy mô mặt cắt ngang (`TCVN 10380:2014`, Bảng 5)
*(Giá trị trong ngoặc `( )` áp dụng cho vùng miền núi hoặc địa hình khó khăn)*

| Cấp kỹ thuật GTNT | Chức năng điển hình | $V_{tk}$ (km/h) | Bề rộng nền $B_n$ (m) | Bề rộng mặt $B_m$ (m) | Bề rộng lề $B_{\text{lề}}$ (m) |
| :--- | :--- | :---: | :---: | :---: | :---: |
| **Cấp A** | Đường trục xã / liên xã | `30 (20)` | `6,5 (6,0)` | `3,5` | `1,50 (1,25)` |
| **Cấp B** | Đường trục thôn / liên thôn | `20 (15)` | `5,0 (4,0)` | `3,0 – 3,5` | `0,75 (0,50)` |
| **Cấp C** | Đường ngõ xóm / nội bộ | `15 (10)` | `3,0 – 4,0` | `2,0 – 3,0` | Tối thiểu `0,50` |
| **Cấp D** | Đường dân sinh / nội đồng (không có ô tô) | Không ô tô | `2,0` | `1,5` | Không yêu cầu lớn |

> **Quy định bắt buộc về vị trí tránh xe:** Với đường cấp B, C mặt đường 1 làn hẹp, bắt buộc bố trí các đoạn **chỗ xe tránh nhau** với khoảng cách hợp lý (thường `≤ 500 m`/vị trí) để xe đi ngược chiều tránh nhau an toàn.

### 5.3. Bảng chỉ tiêu hình học & Tải trọng trục (`TCVN 10380:2014`, Bảng 6)
| Cấp đường | $R_{\min}$ thông thường (m) | $R_{\min}$ giới hạn (m) | Độ dốc dọc lớn nhất $i_{\max}$ | Tải trọng trục tính toán |
| :--- | :---: | :---: | :---: | :--- |
| **Cấp A** (`30 km/h`) | `60` | `30` | `9%` (miền núi tối đa `11%`) | ~`6,0 tấn/trục` |
| **Cấp B** (`20 km/h`) | `30` | `15` | `11% – 12%` (khó khăn đến `13%`) | `2,5 – 5,0 tấn/trục` *(tùy kết cấu)* |
| **Cấp C** (`15 km/h`) | `15` | `10` | Thường giới hạn `≤ 14% – 15%` | `2,5 – 5,0 tấn/trục` *(tùy kết cấu)* |

### 5.4. Lưu ý chuyên môn khi thiết kế & thẩm tra đường GTNT
1. **Ngưỡng chuyển sang `TCVN 4054:2005`:** Nếu tuyến đi qua vùng chuyên canh, cụm công nghiệp, làng nghề có lưu lượng xe tải nặng (`> 6 – 10 tấn`) chiếm trên `10%`, cần kiến nghị xem xét nâng cấp áp dụng theo **TCVN 4054:2005** (cấp VI hoặc cấp V).
2. **Mở rộng bụng đường cong:** Tại các đường cong bán kính nhỏ (`R = 10 – 60 m`), bắt buộc tính mở rộng nền và mặt đường về phía bụng đường cong để đảm bảo quét thân xe.
3. **Kết cấu mặt đường & Phân kỳ đầu tư:** Tùy điều kiện kinh phí & vật liệu địa phương có thể chọn mặt đường **bê tông xi măng (BTXM)** có khe nối (tham khảo phụ lục mẫu `TCVN 10380:2014` / `QĐ 3230/QĐ-BGTVT`), mặt đường láng nhựa, cấp phối hoặc **phân kỳ đầu tư** (giai đoạn 1 làm nền + móng/cấp phối, giai đoạn 2 cứng hóa BTXM).
4. **Thoát nước & ATGT nông thôn:** Đặc biệt chú trọng rãnh dọc qua khu dân cư, cống thoát nước nhỏ/tràn liên hợp ở miền núi, gương cầu lồi tại khúc cua khuất tầm nhìn và báo hiệu theo **QCVN 41:2024/BGTVT**.

---

# Checklist Tự Rà Soát Hồ Sơ Thiết Kế Hạ Tầng Giao Thông

Dùng checklist này ở Bước 4 trước khi bàn giao thuyết minh, bảng tính hoặc bảng khối lượng:

## 1. Pháp lý & Thông số đầu bài
- [ ] Tên dự án, địa điểm, chủ đầu tư, phân loại đường (**Luật Đường bộ 35/2024/QH15**) và số bước thiết kế (**Nghị định 175/2024/NĐ-CP**) thống nhất 100% giữa bìa, thuyết minh, bảng tính và dự toán.
- [ ] Công trình cấp đặc biệt, cấp I, cấp II đã có tài liệu **Chỉ dẫn kỹ thuật** riêng ở bước sau thiết kế cơ sở.
- [ ] Cấp đường, `Vtk`, quy mô mặt cắt ngang, tải trọng trục đúng với chủ trương / nhiệm vụ thiết kế được duyệt.
- [ ] Danh mục QCVN/TCVN/TCCS dẫn chiếu còn hiệu lực (không viện dẫn văn bản cũ đã thay thế như `NĐ 15/2021`, `QCVN 41:2019`, `QCVN 115:2024`, `TCXDVN 104:2007`, `22TCN 211-06`).

## 2. Yếu tố hình học, Nền mặt đường & Công trình trên tuyến
- [ ] Chiều dài tuyến (từ điểm đầu đến điểm cuối theo lý trình `Km...`) khớp giữa thuyết minh, bản vẽ CAD (bình đồ/trắc dọc) và BOQ.
- [ ] Đường cong nằm đã kiểm tra $R_{\min}$ (Bảng 11 `TCVN 4054:2005` hoặc `TCVN 13592:2022` / `QCVN 117:2024`), siêu cao, mở rộng bụng đường cong và tầm nhìn.
- [ ] Trắc dọc đã kiểm tra $i_{\max}$ (Bảng 15), chiết giảm dốc khi $R \le 50\text{ m}$, và **bắt buộc bố trí đường cong đứng lồi/lõm** (Bảng 19) tại mọi đỉnh đổi dốc có $|\Delta i| > 1\%$ ($V_{tk} \ge 60\text{ km/h}$) hoặc $> 2\%$ ($V_{tk} < 60\text{ km/h}$).
- [ ] Cao độ thiết kế đã đối chiếu tần suất thủy văn thiết kế và chiều cao tối thiểu nền đắp / khoảng không tĩnh không (nếu giao cắt).
- [ ] Kết cấu áo đường mềm (`TCCS 38:2022/TCĐBVN`) hoặc áo đường cứng (`QĐ 3230/QĐ-BGTVT`) và xử lý đất yếu (`22TCN 262-2000`) đồng nhất giữa thuyết minh, mặt cắt ngang điển hình và bảng khối lượng.
- [ ] Vị trí, khẩu độ, cao độ đáy cống và giải pháp gia cố thượng/hạ lưu đồng nhất giữa bảng thống kê cống, trắc dọc và thuyết minh thủy văn.

## 3. Tổ chức giao thông & ATGT
- [ ] Hệ thống biển báo, vạch sơn, hộ lan, đinh phản quang, cọc tiêu, cột Km/cọc H tuân thủ **QCVN 41:2024/BGTVT**.
- [ ] Nút giao cùng mức/khác mức có đầy đủ bán kính rẽ, vuốt nối và phân luồng hợp lý.

## 4. Khối lượng (BOQ) & Số học
- [ ] Không có lỗi công thức Excel, không trùng lặp hạng mục giữa các bảng khối lượng.
- [ ] Đơn vị tính đồng nhất với định mức dự toán áp dụng.
- [ ] Các mục còn thiếu số liệu đầu vào đều được gắn cờ `[THIẾU SỐ LIỆU ĐẦU VÀO]` rõ ràng thay vì tự điền ước lượng.

## 5. Rà soát đặc thù Đường Giao thông Nông thôn (`TCVN 10380:2014` & `QĐ 4927/QĐ-BGTVT`)
- [ ] Đúng cấp kỹ thuật GTNT (Cấp A / B / C / D) và phù hợp Quyết định thiết kế mẫu của UBND tỉnh / tiêu chí Nông thôn mới địa phương.
- [ ] Đường 1 làn hẹp (Cấp B, C) đã bố trí **chỗ xe tránh nhau** (`≤ 500 m`/vị trí) và tính mở rộng bụng đường cong tại các đoạn $R$ nhỏ (`10 – 60 m`).
- [ ] Đã kiểm tra tỷ lệ xe tải nặng (`> 6 – 10 tấn`): nếu chiếm `> 10%` cần cảnh báo xem xét nâng cấp sang `TCVN 4054:2005`.
- [ ] Nếu thiết kế mặt đường BTXM hoặc phân kỳ đầu tư: kiểm tra rõ khe co/khe dãn, thoát nước qua khu dân cư và gương cầu lồi / biển báo theo `QCVN 41:2024/BGTVT`.

## 6. Quy cách Trình bày Bản vẽ Kỹ thuật (`TCVN 5571:2012`, `7285:2003`, `7286:2003`, `8-24:2002`, `4608:2012`)
- [ ] Khổ giấy chuẩn (A3 `420×297 mm` hoặc A1 `841×594 mm`), lề trái đóng gáy `20 mm`, các lề còn lại `10 mm`, khung bản vẽ nét liền đậm.
- [ ] Khung tên đặt góc dưới phải (rộng `140` hoặc `190 mm`), đủ thông tin: Chủ đầu tư, TVTK, Tên dự án, Tên bản vẽ, Chữ ký các chức danh, Mã hiệu, Tờ số, Tỷ lệ, Bước thiết kế, Ngày lập.
- [ ] Tỷ lệ đúng thông lệ ngành đường (Bình đồ `1:500`/`1:1000`/`1:2000`; Trắc dọc đứng phóng `10×` ngang; Trắc ngang `1:100`/`1:200`), chiều tăng lý trình từ trái sang phải, có mũi tên chỉ Bắc.
- [ ] Chữ viết tiếng Việt có dấu chuẩn Unicode (font `Arial`/TrueType), chiều cao chữ in trên giấy `≥ 2,0 mm`, không lỗi font và không dùng quá 4 cỡ chữ trên 1 tờ.
