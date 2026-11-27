# TÀI LIỆU KIẾN THỨC #2: QUY TRÌNH TDT VNROAD CAD 2024, AUTOLISP & TRÌNH BÀY BẢN VẼ TCVN

> **Mục đích:** Tài liệu huấn luyện chuyên sâu về chuỗi lệnh TDT Solution 2022 trên AutoCAD 2024, lệnh kiểm tra `TKDAUTO_KIEMTRA.lsp`, vạch sơn `VACHSON41.lsp`, quy tắc chống lỗi `DAODAP` và quy cách trình bày bản vẽ chuẩn TCVN tiếng Việt có dấu Unicode.

---

# Quy Trình Phối Hợp Phần Mềm TDT + AutoCAD 2024 + Antigravity MCP

*(Tri thức vận hành thực tế đã kiểm chứng trên máy tính của người dùng — lưu vĩnh viễn trong plugin `vn-infra-consulting` để mọi phiên làm việc sau luôn ghi nhớ).*

---

## 1. Kiến Trúc TDT & Công Cụ Bổ Trợ Đã Cài Trên Máy
- **Bản cài gốc TDT:** `C:\Program Files (x86)\TDT Solution 2022` (không sửa file gốc của hãng).
- **Thư mục khởi động (Startup):** `<TDT_ROOT>\STARTUP\` (`acad.rx`, `acad.lsp`, `acaddoc.lsp`) tự động nạp:
  - 7 MenuGroups TDT: `KSVN`, `VNROAD`, `SANNEN`, `KVN`, `DCCT`, `TDT3D`, `RM`.
  - Hơn 20 module ARX/DBX: `TDTObjects.dbx`, `AlignmentDb.dbx`, `AlignmentUI.arx`, `HorizontalProfileDesign.arx`, `NhapSoLieuTuyen.arx`, `ProjectDH.arx`, `SNVN.arx`, `RoadMarkingUI.arx`, `RoadSignsUI.arx`...
  - Bộ lệnh **Vạch sơn QCVN 41:2024** (`VACHSON41.lsp`): `VSDONVI`, `VS73`–`VS78`, `VS41`–`VS44`, `VS61`, `VS62`, `VS92`, `VSCATALOG`, `VSHELP`.
  - Bộ lệnh **Kiểm tra tự động TKĐ AUTO** (`TKDAUTO_KIEMTRA.lsp`): `KTTHAMSO`, `KTDOC`, `KTBTH`, `KTBUOC`, `KLSON`, `KTALL`, `KTHELP`.
- **Thư viện tham khảo sẵn có:**
  - Bộ vạch sơn & biển báo QCVN 41:2024: `<SIGNAGE_ROOT>\`
  - Bản vẽ mẫu TDT hoàn chỉnh: `<TDT_ROOT>\CHAY_THU_20261111\TUYEN_THU_HOAN_TAT.dwg`

---

## 2. Nguyên Tắc Vàng Khi Điều Khiển AutoCAD + TDT Qua MCP (`vn-infra-consulting_autocad`)
1. **Chỉ mở MỘT phiên AutoCAD 2024 duy nhất** ở quyền người dùng thường (không *Run as Administrator*) để tránh xung đột COM.
2. **Bảo vệ bản gốc:** Tuyệt đối không vẽ/ghi đè trực tiếp lên file trong `<TDT_ROOT>\`; luôn sao chép bản vẽ sang thư mục dự án làm việc rồi mới thao tác.
3. **Quản lý đối tượng tùy biến TDT (`TdtDbMeasurePointObj`, `TdtDbAlignment`):**
   - Không dùng DXF code `10` cho `TdtDbMeasurePointObj`; muốn lấy tọa độ nhanh trong AutoLISP dùng `(vla-GetBoundingBox obj 'p1 'p2)`.
   - Khi số lượng điểm đo lớn (`> 5.000` đối tượng), tránh quét tuần tự từng đối tượng qua COM Python; dùng AutoLISP `(ssget "X" ...)` để lấy mẫu/thống kê trong `< 0,5 giây`.
4. **Hành vi hộp thoại Modal GUI của TDT & Bộ 5 công cụ điều khiển hộp thoại Win32:**
   - Các lệnh TDT (`TT`, `CN`, `TD`, `DD`, `TN`, `TKTN`, `BTH`) mở hộp thoại Windows Modal làm tạm khóa luồng COM đồng bộ.
   - Sử dụng bộ 5 công cụ Win32 tích hợp sẵn trong `vn-infra-consulting_autocad`:
     - `cad_send_command_async`: Gửi lệnh TDT bất đồng bộ, không treo phiên khi hộp thoại mở lên.
     - `cad_list_windows`: Tìm `HWND` cửa sổ AutoCAD & hộp thoại TDT đang hiển thị.
     - `cad_dialog_inspect`: Đọc toàn bộ `Button`, `Edit`, `ComboBox`, `Static` trong hộp thoại TDT.
     - `cad_dialog_set_text`: Điền tham số (`R`, tên tuyến, bước cọc...) vào ô `Edit`.
     - `cad_dialog_click`: Bấm nút `OK` / `Đồng ý` / `Chọn` / `Hủy` bằng `BM_CLICK`.
   - *(Lưu ý môi trường: Nếu `cad_list_windows` trả về `0` cửa sổ do tiến trình MCP chạy ở Window Station tách biệt desktop tương tác, chuyển về chế độ phối hợp: MCP mở lệnh → người dùng bấm OK trên hộp thoại TDT → MCP chạy `KTALL` & kiểm toán tự động).*
5. **Chữ tiếng Việt có dấu trên AutoCAD:** Luôn tạo TextStyle TrueType `Arial` (`VN_ARIAL`) và mã hóa tiếng Việt sang `\U+XXXX` khi sinh file `.lsp` để không bao giờ lỗi font.

---

## 3. Chuỗi Lệnh Thiết Kế Đường Chuẩn Bằng TDT + Kiểm Tra `KTALL`

| Giai đoạn | Lệnh TDT / Công cụ | Mô tả & Điểm kiểm soát theo TCVN / QCVN |
| :--- | :--- | :--- |
| **0. Chuẩn bị đầu vào** | Antigravity MCP (`cad_draw_polyline`) | Xác định hành lang điểm đo `TdtDbMeasurePointObj`, vẽ Polyline tim tuyến mới (`TIM_TUYEN_MOI`) và Zoom vào tuyến. |
| **1. Tạo tuyến & Cong nằm** | `DLBD` → `TT` → `CN` / `HCT` → `XYTC` / `XTDC` | Khai báo dữ liệu bình đồ, tạo `TdtDbAlignment`; bố trí cong nằm $R \ge R_{\min}$ (**Bảng 11 TCVN 4054:2005** hoặc **Bảng 6 TCVN 10380:2014**). |
| **2. Trắc dọc & Đường đỏ** | `TD` `(1000/200)` → `DD` → `CD` → `CNDD` → `DIENTKTD` | Vẽ trắc dọc tự nhiên (tỷ lệ thông dụng `1000/200`, đường đỏ liền tới cọc cuối, thước cao độ vừa phạm vi tuyến); thiết kế đường đỏ $i \le i_{\max}$, nối **cong đứng `CD`** khi $|\Delta i| > 1\%$ ($V_{tk} \ge 60$ km/h). |
| **3. Trắc ngang & Khuôn đường** | `TN` `(100/100 hoặc 1000/1000)` → `TKTN` → `TKAD` → `DIENTKTN` | Xuất trắc ngang tự nhiên (`100/100` hoặc `1000/1000` `1 đv = 1 m` — **xóa sạch đồ họa TN cũ trước khi đổi tỷ lệ!**), áp khuôn KCAD (`TCCS 38:2022` / `QĐ 3230`), lề, rãnh biên, taluy, điền thiết kế `DIENTKTN`. |
| **4. Đào đắp & Tổng hợp KL** | `DAODAP` → `BTH` → `CNB` | **Quy tắc thực chiến `DAODAP`:** trên CAD 2024 chạy 3 pass dòng 1 (`Y` tăng dần, điền tay `X/Y/Cao chữ`, **không dùng dấu phẩy trong tên**, **không bấm Enter trong lưới**); pass 1 xóa nhãn cũ, pass 2–3 bật `Không xóa diện tích cũ`. Xuất `BTH` đặt tách hẳn sang phải lưới `TN` và kiểm $V = \frac{A_1+A_2}{2}\times L$. |
| **5. Vạch sơn & Biển báo** | `VS73`..`VS92`, `VSCATALOG`, menu `RM` | Bố trí báo hiệu & vạch kẻ đường đúng **QCVN 41:2024/BGTVT** (lưu trên layer `VS_*`, `BIEN BAO`). |
| **6. Dàn trang in A3** | `INTD`, `INTN` (chuẩn A3 `TCVN 7285/5571`) | **Bình đồ + Trắc dọc chung khung A3** (thước cao độ vừa phạm vi tuyến, đường đỏ liền tới cọc cuối); **Trắc ngang chia khung A3** gọn gàng, không đè nét; khung tên góc dưới phải 6 chức danh ký. |
| **7. Tự kiểm thử tự động** | **`KTTHAMSO` → `KTALL`** + Python `audit_boq_excel.py` | Chạy `KTALL` (`KTBUOC`, `KTDOC`, `KTBTH`, `KLSON`), đọc `<ten_ban_ve>_KIEMTRA.txt` xuất cạnh file `.dwg`, đối chiếu chéo 3 chiều với Thuyết minh & Dự toán Excel. |

---

## 4. Bộ Layer TDT Chuẩn Để Đọc & Thẩm Tra Tự Động
- **Tuyến & Trắc dọc:** `TUYEN`, `plinetdtn`, `PlineThangCong`, `tracdocthietke`, `CONGDUNG`, `entkhieult`, `entdauco`, `Texttencoc`, `kcle_*`, `enttdtunhien`.
- **Trắc ngang & Khuôn đường:** `enttntunhien`, `DienTKTN`, `linedongtn`, `plinetntn`, `MSSTracNgang`, `TS_CONG_TN`, `Mat duong 1 Trai/Phai`, `Le GC`, `Le KGC`, `BTNC12.5`, `CPDD1`, `CPDD2`, `Atphan2`, `Base`, `Ranh Trai/Phai`, `Taluy Trai/Phai`, `Taluy_FACE`.
- **Khối lượng & ATGT:** `diendientich`, `BangTongHop`, `VS_*`, `BIEN BAO`, `TEN BIEN BAO`, `THONGKE BIENBAO`.

---

## 5. Cẩm Nang Thực Chiến TDT VNRoad CAD 2024: TN `1000/1000`, Thông Số Cong & QA Hình Thức (`v2.4`)

*(Đúc kết trực tiếp từ quá trình chạy Native TDT 2024 + QA độc lập 12.554 thực thể trên `DA-CAMTAN-03` ngày 27/11/2026).*

### 5.1. Quy tắc chống crash & sai số khi chạy chuỗi lệnh TDT Native 2024
1. **Tránh crash `TT` từ `.ntd`:** Lệnh `TT` đọc tệp `.ntd` trên AutoCAD 2024 có thể gây `FATAL ERROR` (`Unhandled 9dbfa5f0h`). Thay bằng luồng ổn định 100%: `TDCAD` (nhập điểm đo) → `DLBD` (xây dựng mô hình `OBJECTDIAHINH`) → `TT` (tạo tuyến từ Polyline) → `CN` (cong nằm) → `DCT` (điền cọc) → `HCT`.
2. **Bẫy lệch `10×` cao độ tự nhiên khi đổi tỷ lệ `TN` (`100/100` → `1000/1000`):**
   - Nếu chạy lại lệnh `TN` tỷ lệ `1000/1000` **khi đồ họa `TN 100/100` cũ vẫn còn trên bản vẽ**, TDT đọc `ΔY` cũ (`10 đv/m`) như đơn vị mét khiến cao độ tự nhiên đội gấp `10×` trên MSS (ví dụ `15,75 m` thành `31,52 m`, làm khối lượng đào nền đội hàng trăm nghìn `m³`).
   - **Bắt buộc:** Kiểm tra số liệu gốc trong `SLT`, **xóa sạch toàn bộ thực thể đồ họa `TN` và bảng `ACAD_TABLE` cũ** trước khi chạy `TN 1000/1000` → chọn toàn bộ cọc (`DS cọc >>` → `Chọn toàn bộ`) → vẽ lại từ gốc `SLT` → áp `TKTN → TKAD → DIENTKTN → DAODAP → BTH`.
3. **Khóa hệ biến & bấm hộp thoại Win32 chính xác:**
   - Luôn đặt `(setvar "DYNMODE" 0) (setvar "OSMODE" 0)` trước khi nhập tọa độ điểm chèn `TD`/`TN`/`BTH`, và khôi phục `(setvar "DYNMODE" 1)` khi hoàn tất.
   - Khi nhiều nút trùng chuỗi con (VD `"Vẽ"` vs `"Vẽ nhóm theo chiều dọc"`, `"Áp khuôn"` vs checkbox `"áp khuôn..."`), luôn dùng `control_hwnd` chính xác lấy từ `cad_dialog_inspect`.
   - Trong `TKAD`, sau khi sửa lớp vật liệu của `khuon 1`, phải bấm sang dòng khác (`Khuôn 2`) trước khi đổi tab/áp khuôn để TDT ghi nhận thay đổi.
4. **Bộ tham số chuẩn đã kiểm chứng cho Trắc ngang `1000/1000` (`1 đv = 1 m`):**
   - File `.dntn` (giữ nguyên mã hóa TCVN3): `Cao chữ = 0.4`, `Cao hàng = 2.2`, `Trai = 1` (thước tỷ lệ trái), `MSSTN = 1` (bắt buộc cho `KTALL`), `RongThuoc = 0.25`, `DonviThuoc = 1.0`, `TyleDauCo = 0.25`, `DaiRau = 0.5`, `CaochuDaubang = 0.4`, `CaochuThuocTyle = 0.4`, `CaochuDauco = 0.4`, `KHCDB = 0.6`.
   - Hộp thoại `TN`: `Tỷ lệ X = 1000`, `Tỷ lệ Y = 1000`, `KCách đầu cờ = 5.5`, `Số hàng = 3`, `Số cột = 3`, `Cách hàng = 12`, `Cách cột = 10`, `KCách nhóm = 20`, `Lấy sang trái/phải = 12.00`.
   - `DAODAP` 3 pass (vì CAD 2024 chỉ tính dòng 1 mỗi lần & mở `.cfg` không tự điền ô `X/Y/Cao chữ` nên phải điền tay qua `cad_dialog_set_text`): `Cao chữ = 0.4`, `Left X = 3.5`, `Right X = 1.5`, `Y = 1.2 / 1.9 / 2.6`, `Điền giá trị 0 = ON`; pass đầu tắt và pass 2–3 bật `Không xóa diện tích cũ, điền thêm mã mới`.
   - Bảng `BTH` (`117+` dòng, cao `~468 đv` tại `Cao hàng = 4`): luôn đặt tách hẳn sang bên phải lưới `TN` (`X_BTH > X_max(TN) + 70`) để đáy bảng không đâm xuống góc trái lưới `TN`.

### 5.2. An toàn điều khiển AutoLISP/MCP & Kiểm chứng hình ảnh
1. **Chống chạy đúp `cad_send_command` (Idempotency Guard):** Khi gửi LISP xử lý nặng (`>15–20 giây`), COM timeout/retry có thể khiến hàm chạy 2 lần (`2×` dịch chuyển). **Quy tắc:** tách riêng lệnh sửa và lệnh thống kê/dump; bọc mọi hàm biến đổi tọa độ trong cờ chống lặp `(if (not *qa-step-done*) (progn (setq *qa-step-done* T) ...))` và hậu kiểm bằng `vla-GetBoundingBox`.
2. **Dùng `_.PNGOUT` (`FILEDIA=0`) + `ZOOM _W` theo bbox thực:** `cad_screenshot` có thể dính cửa sổ ứng dụng khác che lên desktop; `_.PNGOUT` xuất thẳng viewport AutoCAD sắc nét. Với bản vẽ có `OBJECTDIAHINH` tại `(0,0)`, **cấm dùng `ZOOM _E`** (thu cả bản vẽ về 1 chấm) — luôn `ZOOM _W` theo bbox thực của từng khối.

### 5.3. Checklist hậu xử lý tự động 5 lỗi trình bày cố hữu của TDT (0 chồng lấn)
1. **Thông số cong TN (`TS_CONG_TN`):**
   - TDT hay vẽ lệch lên hàng trên (`+14,07 m`), lệch màu hàng đầu (Đỏ `1` vs Xanh lá `3`), cung `ARC` (`R=1.45`) đâm xuyên chữ và chân chữ `p` của `ip1` đè `w1`.
   - **Cảnh báo OCS Mirror:** Với đường cong rẽ phải, TDT tạo `ARC` bằng phép lật OCS (`210 = (0 0 -1)`) khiến `assoc 10` có `X` âm. **Tuyệt đối không sửa DXF code `10`** — luôn dùng `vla-Move` trong WCS theo độ lệch `vla-GetBoundingBox`.
   - Căn tâm cung ngang đầu cờ (`Y = Y_dauco + 1.25`), đặt 4 dòng bước `0,58 m` ôm gọn trong lòng cung theo phương trình tròn $\sqrt{R^2 - \Delta y^2}$ (hở cung `>= 0,25 m`), đồng bộ màu xanh lá (`3`).
2. **Thông số cong TD (`enttdtunhien` — hàng `Sơ họa tuyến`):**
   - Luôn cắt ký tự xuống dòng `\n` thừa ở chuỗi `Isc=.. W=..`.
   - Khoang trống thực của `PlineThangCong` cao `7,50 m`; căn giữa 3 dòng chữ (cao `1,2`, bước `1,80 m`) vào chính giữa khoang `7,50 m` để hở `>= 1,2 m` cả hai phía tới `PlineThangCong` và viền bảng.
3. **Nhãn diện tích `DAODAP` (`diendientich`) trên cọc đắp cao:**
   - Do TDT đặt theo cao độ tự nhiên, các cọc nền đắp cao (`H_đắp > 0,8 m`) bị chữ đè lên mặt đường, mũi tên dốc `2%/4%` và đầu cờ `entdauco`. Giải đặt 2D tách đối xứng 2 cụm Trái/Phải né vùng cờ `[-3.7, +3.7]`, đặt trên đỉnh mặt cắt/taluy (khe hở `>= 0,25 m`).
4. **Chữ bảng dọc `DienTKTN` / `enttntunhien` & `kcle` TD tại ô hẹp:**
   - Lề rộng `0,25 m` với chữ dọc `H = 0,40` luôn đè nhau. Vì text bảng TN dùng `align = 4,0` (Middle tại `P11`), chỉ cần giảm `vla-put-Height` cục bộ về `0,21` (và `0,22–0,23` cho điểm mia dày, kết hợp giãn X `min_gap >= 0,03 m`) là chữ tự co đúng tâm ô. Tương tự trên TD cho khoảng cách lẻ `< 1,0 m` (`H = 0,48–0,72`) và tách 2 tầng `Texttencoc` `±0,50 m`.
5. **Va chạm ngang giữa 2 cột TN khi có cọc vế địa hình dài đột biến:**
   - Quét khe hở `true_L[i] - true_R[i-1]` từng hàng; nếu âm, cô lập đúng nhóm thực thể của cọc đó theo bbox + ranh giới handle để dịch cân giữa hai cọc kề.
6. **Khóa an toàn sau hậu xử lý hình thức:** Luôn sao lưu bản vẽ `*_truocQA.dwg` trước khi sửa, chạy lại **`KTALL`** xác nhận giữ nguyên `7/7 [OK]` & `0,00 m³` biến động khối lượng `KTBTH`, rồi mới lưu đè `.dwg`.

---

# Quy Cách Trình Bày Bản Vẽ Xây Dựng & Đường Giao Thông Tại Việt Nam

*(Tài liệu chuẩn tích hợp trong plugin `vn-infra-consulting` — áp dụng cho cả công tác lập bản vẽ AutoCAD qua MCP và thẩm tra hình thức/quy cách hồ sơ bản vẽ).*

---

## 1. Hệ Thống TCVN Trình Bày Bản Vẽ Kỹ Thuật & Xây Dựng

| Hạng mục | Tiêu chuẩn Việt Nam | Quy định cốt lõi |
| :--- | :--- | :--- |
| **Khổ giấy & Khung bản vẽ** | **TCVN 7285:2003** *(ISO 5457:1999)* | • Khổ giấy đã xén (mm): **A0** (`841×1189`), **A1** (`594×841`), **A2** (`420×594`), **A3** (`297×420`), **A4** (`210×297`).<br>• **Lề bản vẽ:** Lề trái đóng gáy **`20 mm`**; 3 lề còn lại (trên, dưới, phải) **`10 mm`**.<br>• Khung bản vẽ kẻ bằng **nét liền đậm** (`0,5 – 0,7 mm`). |
| **Khung tên bản vẽ** | **TCVN 5571:2012** | • Đặt ở **góc dưới cùng bên phải** tờ bản vẽ.<br>• Chiều dài chuẩn **`140 mm`** hoặc **`190 mm`** (khớp khổ gấp A4 để khung tên lộ ra ngoài khi gấp hồ sơ).<br>• Bắt buộc đủ ô: Chủ đầu tư, Tư vấn thiết kế, Tên dự án/công trình, Tên bản vẽ, Bảng chữ ký (*Người vẽ – Thiết kế – Chủ trì – Kiểm tra – Chủ nhiệm – Đại diện TVTK*), Ký hiệu/Mã bản vẽ, Tờ số, Tỷ lệ, Bước thiết kế (TKCS / TKKT / TKBVTC), Ngày tháng lập. |
| **Tỷ lệ bản vẽ** | **TCVN 7286:2003** *(ISO 5455:1979)* | • Tỷ lệ chính bắt buộc ghi trong khung tên; chi tiết có tỷ lệ riêng ghi ngay dưới tên hình.<br>• Tỷ lệ chuẩn ngành đường xem Mục 2 dưới đây. |
| **Đường nét & Nét in** | **TCVN 8-24:2002** *(nhóm TCVN 8)* | • Trên khổ A3 chọn nét cơ bản $b = 0,5\text{ mm}$:<br>&nbsp;&nbsp;- **Nét liền đậm (`0,5 – 0,7 mm`):** Khung bản vẽ, khung tên, đường bao chính, mép mặt đường thiết kế, đường đỏ trắc dọc.<br>&nbsp;&nbsp;- **Nét liền mảnh (`~0,25 mm`):** Đường kích thước, đường gióng, lưới trắc dọc/trắc ngang, đường tự nhiên, các lớp KCAD.<br>&nbsp;&nbsp;- **Nét đứt (`~0,25 mm`):** Đường khuất, công trình ngầm, ranh GPMB.<br>&nbsp;&nbsp;- **Nét chấm gạch mảnh (`~0,25 mm`):** Tim tuyến, trục đối xứng. |
| **Chữ viết & Font chữ** | **TCVN 4608:2012** & **TCVN 7284** *(ISO 3098)* | • Khổ chữ chuẩn trên giấy: `2,5 ; 3,5 ; 5 ; 7 ; 10 ; 14 ; 20 mm`; tối thiểu không nhỏ hơn `2,0 mm` (số bảng biểu dày đặc `1,75 – 2,0 mm`).<br>• Trên 1 tờ bản vẽ **không nên dùng quá 4 cỡ chữ**.<br>• **Bắt buộc dùng tiếng Việt có dấu chuẩn Unicode** (khuyên dùng TrueType **`Arial`** / `Times New Roman`; khi viết AutoLISP chuyển ký tự có dấu sang mã `\U+XXXX` để hiển thị chuẩn trên mọi máy AutoCAD). |

---

## 2. Tỷ Lệ & Cỡ Chữ Khuyến Nghị Cho Hồ Sơ Bản Vẽ Đường (Đặc Biệt Khổ A3 Đóng Tập)

### 2.1. Tỷ lệ theo loại bản vẽ
| Loại bản vẽ đường giao thông | Tỷ lệ chuẩn phổ biến (A3 / A1) | Nguyên tắc kỹ thuật |
| :--- | :---: | :--- |
| **Bình đồ tổng thể vị trí tuyến** | `1:5.000` – `1:10.000` | Thể hiện hướng tuyến, kết nối khu vực, mũi tên chỉ Bắc, lưới tọa độ VN-2000 |
| **Bình đồ chi tiết tuyến** | `1:500` (đô thị/ngắn) • `1:1.000` / `1:2.000` | Chiều tăng lý trình đọc từ **trái sang phải**; đầy đủ cọc Km/H, đường cong, cống, rãnh, GPMB, biển báo |
| **Trắc dọc thiết kế** | Ngang `1:1.000` – Đứng `1:100`<br>*(hoặc Ngang `1:2.000` – Đứng `1:200`)* | **Tỷ lệ đứng luôn phóng lớn gấp `10×` tỷ lệ ngang** để dễ đọc độ dốc và đường cong đứng |
| **Trắc ngang chi tiết & Điển hình** | `1:100` hoặc `1:200` | Tỷ lệ ngang = tỷ lệ đứng để giữ đúng hình dáng taluy, rãnh biên |
| **Chi tiết KCAD, Cống, Rãnh, Tường chắn** | `1:10`, `1:20`, `1:50` | Đầy đủ kích thước chiều dày từng lớp (cm/mm), vật liệu, cao độ đáy/đỉnh |

### 2.2. Quy đổi chiều cao chữ khi vẽ trên Model AutoCAD (đơn vị mét)
- Với khổ in A3:
  - **Tiêu đề chính bản vẽ / tên hạng mục:** `3,5 – 5,0 mm` trên giấy.
  - **Ghi chú kích thước, lý trình, cao độ, thông số kỹ thuật:** `2,0 – 2,5 mm` trên giấy.
  - **Số liệu trong bảng trắc dọc / bảng thống kê:** `1,75 – 2,0 mm` trên giấy.
- **Công thức quy đổi nhanh vào ModelSpace:** `Chiều cao chữ Model = Chiều cao in trên giấy (mm) × Mẫu số tỷ lệ / 1000` *(ví dụ in tỷ lệ `1:1000`, chữ `2,5 mm` trên giấy → chiều cao chữ trong Model đơn vị mét là `2,5 m`)*.

---

## 3. Trình Tự Sắp Xếp Chuẩn Của Một Tập Hồ Sơ Bản Vẽ Đường Giao Thông

1. **Bìa tập bản vẽ** & **Danh mục bản vẽ** (kèm ký hiệu bản vẽ, số tờ, bước thiết kế).
2. **Ghi chú chung & Bảng ký hiệu quy ước** (hệ tọa độ VN-2000, hệ cao độ Quốc gia Hòn Dấu, đơn vị đo: cao độ & lý trình tính bằng `m`, kết cấu chi tiết bằng `cm`/`mm`).
3. **Bình đồ tổng thể vị trí dự án** & **Bình đồ chi tiết tuyến** (kèm Bảng tọa độ đỉnh & yếu tố đường cong nằm, mũi tên chỉ Bắc).
4. **Trắc dọc thiết kế tuyến** (khớp từng đoạn lý trình với bình đồ, đầy đủ bảng 5–8 dòng bên dưới & ký hiệu công trình ngang).
5. **Mặt cắt ngang điển hình** & **Chi tiết kết cấu áo đường** (kèm bảng thông số mô đun đàn hồi / chiều dày từng lớp).
6. **Trắc ngang chi tiết từng cọc** (kèm bảng tính diện tích đào/đắp từng cọc).
7. **Công trình thoát nước & Công trình trên tuyến** (rãnh dọc, cống tròn/hộp, cầu, tường chắn, xử lý đất yếu).
8. **Nút giao** (bình đồ vuốt nối, thiết kế đứng quy hoạch cao độ nút giao).
9. **Tổ chức giao thông & An toàn giao thông** (bố trí biển báo, vạch sơn, hộ lan, cột Km/cọc H theo `QCVN 41:2024/BGTVT` + Bảng thống kê ATGT).
