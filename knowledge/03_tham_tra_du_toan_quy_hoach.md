# TÀI LIỆU KIẾN THỨC #3: THẨM TRA DỰ ÁN – DỰ TOÁN, QUY HOẠCH & NHẬT KÝ ĐÚC KẾT 2 AI

> **Mục đích:** Tài liệu huấn luyện chuyên sâu về thẩm tra hồ sơ thiết kế – dự toán (mẫu đơn vị thẩm tra / Mẫu số 11, MATY / Dự toán Bắc Nam), kiểm toán bẫy Excel 5 lớp QA Auditor, quy hoạch giao thông (cân bằng đất đai, ma trận MCA) và bài học thực chiến tích lũy.

---

# Kỹ Năng: Thẩm Tra Dự Án & Kiểm Toán Khối Lượng – Dự Toán

## Quy trình thẩm tra 5 bước chuẩn

### Bước 1: Kiểm đếm danh mục hồ sơ & Rà soát pháp lý
1. Đọc `GEMINI.md` và quét toàn bộ file trong `05_ThamTra_RaSoat/` (cùng `01_PhapLy_TieuChuan/`, `04_DuToan_KhoiLuong/` nếu có).
2. Lập bảng kiểm đếm thành phần hồ sơ (Pháp lý, Khảo sát, Thuyết minh, Bảng tính, Bản vẽ, Dự toán) và ghi rõ tài liệu còn thiếu hoặc chưa đủ tính pháp lý.
3. Kiểm tra sự phù hợp giữa hồ sơ trình thẩm tra với chủ trương đầu tư, nhiệm vụ thiết kế, quy hoạch liên quan và năng lực/chứng chỉ (nếu có trong hồ sơ).

### Bước 2: Rà soát hệ thống Quy chuẩn – Tiêu chuẩn áp dụng
- Trích xuất toàn bộ danh mục Luật/Nghị định/QCVN/TCVN/TCCS mà tư vấn thiết kế viện dẫn.
- Đối chiếu trực tiếp với bảng hiệu lực tại `../thiet-ke-ha-tang-giao-thong/references/quy-trinh-thiet-ke-duong-vn.md` (và dùng `search_web` khi gặp văn bản mới/chuyên ngành đặc thù).
- Bắt ngay các tồn tại phổ biến: hồ sơ vẫn dẫn chiếu văn bản đã hết hiệu lực (`NĐ 10/2021/NĐ-CP`, `TT 11/2021`, `TT 12/2021`, `TT 13/2021/TT-BXD` đã bị thay bởi `NĐ 206/2026` & `TT 36–38/2026/TT-BXD` từ `01/07/2026`; `NĐ 15/2021/NĐ-CP`, `QCVN 41:2019/BGTVT`, `QCVN 115:2024/BGTVT`, `TCXDVN 104:2007`, `22TCN 211-06`), thiếu **Chỉ dẫn kỹ thuật** cho công trình cấp II trở lên, thiếu đường cong đứng khi $|\Delta i| > 1\%$ ($V_{tk} \ge 60\text{ km/h}$), hoặc áp dụng sai cấp công trình / sai loại đường.

### Bước 3: Thẩm tra giải pháp kỹ thuật theo bộ môn
*(Với bộ hồ sơ lớn nhiều tập, đề xuất chia song song bằng Subagents: (1) Pháp lý & Quy chuẩn, (2) Kỹ thuật Đường – Cầu – Thoát nước – ATGT, (3) Khối lượng & Dự toán).*
- Kiểm tra tính hợp lý của thông số thiết kế hình học, địa chất – xử lý nền đất yếu, kết cấu áo đường, thủy văn – khẩu độ công trình thoát nước, giải pháp kết cấu cầu/tường chắn, nút giao và ATGT.
- Kiểm tra quy cách trình bày bản vẽ theo `../thiet-ke-ha-tang-giao-thong/references/quy-cach-trinh-bay-ban-ve-vn.md` (**TCVN 5571:2012** khung tên & đủ chữ ký chức danh, **TCVN 7285:2003** khổ giấy/lề, **TCVN 7286:2003** tỷ lệ khớp giữa hình và khung tên, **TCVN 4608:2012** cỡ chữ rõ đọc không lỗi font tiếng Việt).
- Với bản vẽ thiết kế bằng phần mềm **TDT** trên AutoCAD 2024, áp dụng thêm quy trình tại `../thiet-ke-ha-tang-giao-thong/references/quy-trinh-tdt-autocad-vn.md`: chạy kiểm tra tự động **`KTTHAMSO` → `KTALL`** (`KTBUOC`, `KTDOC`, `KTBTH`, `KLSON`) và đọc báo cáo `<ten_ban_ve>_KIEMTRA.txt` để đối chiếu chéo với Thuyết minh & Dự toán.
- Kiểm tra xem các bảng tính quan trọng có đầy đủ và nhất quán với thông số trong thuyết minh không.

### Bước 4: Kiểm toán tự động Excel BOQ / Dự toán & Đối chiếu chéo 3 chiều (QA Auditor 5 lớp)
1. Chạy script kiểm toán tự động [audit_boq_excel.py](./scripts/audit_boq_excel.py) trên toàn bộ file `.xlsx`/`.xls` khối lượng / dự toán:
   ```bash
   python "<path_to_this_skill>/scripts/audit_boq_excel.py" "<duong_dan_file_excel.xlsx>"
   ```
2. Kiểm tra đủ **5 lớp bẫy thực chiến** (theo chuẩn **QA Auditor**):
   - **Bản vẽ CAD/DWG là Ground-Truth** đối chiếu 3 chiều với Thuyết minh & Dự toán.
   - **Bẫy số học & Excel:** Cộng ngang/dọc `Tổng TK - Tổng TT = Tổng Tăng/Giảm`; lệch đơn vị định mức (`100m` vs `m`, `100m³` vs `m³`); lệch `10` lần dấu thập phân công suất; ô hard-code làm âm dự phòng; công thức đường $V = \frac{A_1+A_2}{2}\times L$ và diện tích sơn `VS_*`.
   - **Logic lời văn:** Ngược dấu giải trình tăng/giảm, lỗi dấu trừ kép (`"giảm -1.500.000"`), quên giải trình biến động QLDA/TVĐT theo $G_{xd}$.
   - **Pháp quy & Địa danh:** Địa danh **tỉnh Khánh Hòa** (sau `01/07/2025`), `QCVN 41:2024`, `QCVN 40:2025`, `QĐ 646/QĐ-SXD Khánh Hòa (03/07/2026)`, không để trống `.../QĐ-...`.
   - **Trình bày:** Copy-paste nhầm tên bảng/nhảy số mục, chữ đè nét trắc ngang, sai định dạng số.
3. **Quy cách xuất file Dự toán / Thẩm tra chuẩn đơn vị:**
   - Lập dự toán mới theo cấu trúc mẫu **`MATY`** hoặc kiểu **Dự toán Bắc Nam**; hồ sơ BCKTKT xuất gộp 1 file PDF.
   - Thẩm tra theo mẫu **đơn vị thẩm tra / Mẫu số 11**: giữ nguyên cấu trúc file thiết kế, sửa trực tiếp và **tô đỏ** ô thay đổi, xuất thành **`... - THAM TRA.xls`** (kèm **`cvc - THAM TRA.xls`**); thân báo cáo gọn, các lỗi nhỏ đưa vào bảng phụ lục.

### Bước 5: Xuất Báo Cáo Thẩm Tra & Bảng Tổng Hợp Tồn Tại / Giải Trình
Đọc khung mẫu tại [mau-bao-cao-tham-tra.md](./references/mau-bao-cao-tham-tra.md) để xuất đồng bộ:
1. **Báo cáo kết quả thẩm tra** gọn gàng, lỗi nhỏ đưa vào phụ lục, chốt rõ kết luận **`[ĐẠT – ĐƯỢC PHÉP PHÁT HÀNH]`** hoặc **`[TRẢ LẠI AI 1 SỬA CÁC LỖI 🔴 & 🟠]`**.
2. **Bảng tổng hợp tồn tại phân 3 cấp** (`🔴 Nghiêm trọng`, `🟠 Trung bình`, `🟡 Nhẹ`), ghi rõ vị trí Trang/Sheet/Cọc, căn cứ và cách sửa đề xuất.
3. Nếu người dùng chuyển sang giai đoạn tiếp thu ý kiến, sinh **Bảng theo dõi giải trình – tiếp thu** 5 cột.

---

# Khung Mẫu Báo Cáo Kết Quả Thẩm Tra & Bảng Tổng Hợp Tồn Tại

## Phần I. Thông Tin Chung Dự Án
- Tên dự án, địa điểm, chủ đầu tư, đơn vị tư vấn lập hồ sơ, giai đoạn thẩm tra.
- Danh mục hồ sơ tiếp nhận (ghi rõ đầy đủ / còn thiếu).

## Phần II. Kết Quả Rà Soát Pháp Lý & Tiêu Chuẩn Áp Dụng
- Đánh giá sự phù hợp quy hoạch, chủ trương đầu tư, nhiệm vụ thiết kế.
- Bảng đối chiếu danh mục QCVN/TCVN tư vấn áp dụng (Đúng / Hết hiệu lực / Thiếu).

## Phần III. Nhận Xét Thẩm Tra Theo Bộ Môn Kỹ Thuật
1. Khảo sát địa hình, địa chất, thủy văn.
2. Tuyến (bình đồ, trắc dọc, trắc ngang) & Nút giao.
3. Nền đường, xử lý nền đất yếu & Kết cấu áo đường.
4. Công trình thoát nước, cầu, cống, tường chắn.
5. An toàn giao thông, tổ chức giao thông, hạ tầng kỹ thuật đồng bộ.
6. Khối lượng (BOQ) & Dự toán / Tổng mức đầu tư (kèm tóm tắt kết quả chạy script `audit_boq_excel.py`).

## Phần IV. Bảng Tổng Hợp Tồn Tại Phân Cấp
| STT | Mức độ | Bộ môn / Hạng mục | Vị trí (File / Trang / Sheet) | Nội dung tồn tại | Căn cứ pháp lý / QCVN-TCVN | Đề xuất chỉnh sửa |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | **[NGHIÊM TRỌNG - BẮT BUỘC SỬA]** | | | | | |
| 2 | **[CẦN LÀM RÕ / BỔ SUNG]** | | | | | |
| 3 | **[KHUYẾN NGHỊ TỐI ƯU]** | | | | | |

## Phần V. Kết Luận & Kiến Nghị
- Nêu rõ điều kiện đủ hay chưa đủ để trình phê duyệt sau khi hoàn thiện các tồn tại mức **NGHIÊM TRỌNG** và **CẦN LÀM RÕ**.

---

## Phụ Lục: Mẫu Bảng Theo Dõi Tiếp Thu – Giải Trình Ý Kiến
| STT | Nội dung ý kiến thẩm tra / thẩm định | Căn cứ kỹ thuật / pháp lý | Phương án tiếp thu / giải trình của Tư vấn | Mục / Bản vẽ / Sheet đã chỉnh sửa | Trạng thái |
| :--- | :--- | :--- | :--- | :--- | :--- |
| 1 | | | | | Đã sửa / Bảo lưu |

---

# Kỹ Năng: Quy Hoạch Giao Thông & Đô Thị

## Quy trình thực hiện (gắn với Vòng lặp 4 bước)

### 1. Tổng hợp dữ liệu hiện trạng & Kiểm tra chỉ tiêu đầu bài
1. Đọc `GEMINI.md` để nắm rõ cấp độ quy hoạch, tỷ lệ bản đồ, diện tích phạm vi nghiên cứu, mốc thời gian quy hoạch và nhiệm vụ quy hoạch.
2. Đọc dữ liệu hiện trạng trong `02_KhaoSat_HienTrang/` (Excel/CSV/GIS/Shapefile/GeoJSON/thuyết minh cũ).
3. Kiểm kê khoảng trống dữ liệu hiện trạng và gắn cờ `[THIẾU SỐ LIỆU ĐẦU VÀO]` cho các chỉ tiêu chưa có căn cứ.

### 2. Tính toán chỉ tiêu quy hoạch & Cân bằng đất đai bằng Python
Viết script Python để tính chính xác và đối chiếu với quy chuẩn quy hoạch xây dựng hiện hành (xác minh hiệu lực QCVN trước khi dẫn chiếu):
- Bảng cân bằng sử dụng đất (diện tích `ha`, tỷ lệ `%`, chỉ tiêu `m²/người`) đảm bảo tổng diện tích khớp tuyệt đối `100.00%`.
- Chỉ tiêu mạng lưới giao thông: tỷ lệ đất giao thông trên đất xây dựng đô thị (`%`), mật độ đường chính (`km/km²`), diện tích bãi đỗ xe (`m²/người`), phân cấp mặt cắt ngang và chỉ giới đường đỏ.
- Phân tích lưu lượng – năng lực thông hành (nếu có dữ liệu đếm xe/dự báo).

### 3. So sánh phương án bằng Ma trận Đánh giá Đa tiêu chí (MCA)
Khi cần so sánh các phương án hướng tuyến, phương án tổ chức mạng lưới hoặc phương án phân khu:
1. Chốt bộ tiêu chí & trọng số (tổng trọng số = 100%), ví dụ:
   - Hiệu quả kết nối & phục vụ giao thông
   - Khối lượng GPMB & tác động xã hội
   - Tổng mức đầu tư & hiệu quả kinh tế
   - Điều kiện kỹ thuật – địa hình – địa chất
   - Tác động môi trường & khả năng phân kỳ đầu tư
2. Chuẩn bị file JSON đầu vào và chạy script [mca_scoring.py](./scripts/mca_scoring.py) để tính điểm trọng số, xếp hạng phương án và kiểm tra độ nhạy:
   ```bash
   python "<path_to_this_skill>/scripts/mca_scoring.py" "<duong_dan_input_mca.json>"
   ```

### 4. Xuất hồ sơ trình duyệt & Dàn ý bảo vệ Hội đồng
- Xuất báo cáo phân tích hiện trạng, báo cáo so sánh phương án (kèm bảng số liệu & kết quả MCA) vào `06_SanPham_TrinhDuyet/`.
- Kèm theo dàn ý slide tóm tắt (10–15 slide) tập trung vào: Hiện trạng & Điểm nghẽn → Mục tiêu & Chỉ tiêu → So sánh Phương án → Phương án Chọn & Kế hoạch phân kỳ đầu tư.

---

# Nhật Ký Đúc Kết Kinh Nghiệm Thực Chiến — Mô Hình 2 AI (`VN-INFRA-CONSULTING`)

*Sau mỗi lần chạy thử thực tế trên một hồ sơ/dự án, ghi lại các tình huống phát sinh vào bảng dưới đây và cập nhật quy tắc mới vào `rules/AGENTS.md` hoặc các skill tương ứng để không bao giờ lặp lại lỗi cũ.*

| Ngày | Công trình chạy thử | Tình huống / Lỗi thực tế phát sinh | Quy tắc mới bổ sung (AI 1 / AI 2) | Phiên bản |
| :--- | :--- | :--- | :--- | :---: |
| 25/11/2026 | Khởi tạo từ bộ nhớ Claude & ChatGPT | Đóng gói quy trình TDT, QCVN 41:2024 và bộ quy tắc thẩm tra của đơn vị | Tách thành 2 AI (Thực thi & Kiểm tra độc lập 5 lớp), lưu thành plugin `vn-infra-consulting` `v1.1.0` kèm Dynamic Workflow khép vòng | `v1.0 → v1.1` |
| 24/11/2026 | `DA-TEST-GT01` & `DA-TDT-02` (Antigravity) | Thiếu `git` trên PATH; tách phiên COM tạo thêm tiến trình `acad.exe`; lệnh `TT` mở modal dialog làm treo COM đồng bộ | Bổ sung fallback `snapshot_project.py`, cache `_CACHED_ACAD` và 5 công cụ Win32 điều khiển hộp thoại bất đồng bộ trong MCP `vn-infra-consulting_autocad` | `v1.1` |
