# TÀI LIỆU KIẾN THỨC #2: QUY TRÌNH TDT VNROAD CAD 2024, AUTOLISP & TRÌNH BÀY BẢN VẼ TCVN

> **Mục đích:** Tài liệu huấn luyện chuyên sâu về chuỗi lệnh TDT Solution 2022 trên AutoCAD 2024, lệnh kiểm tra `TKDAUTO_KIEMTRA.lsp`, vạch sơn `VACHSON41.lsp`, quy tắc chống lỗi `DAODAP` và quy cách trình bày bản vẽ chuẩn TCVN tiếng Việt có dấu Unicode.

---

# Quy Trình Phối Hợp Phần Mềm TDT + AutoCAD 2024 + Antigravity MCP

*(Tri thức vận hành thực tế đã kiểm chứng trên máy tính của người dùng — lưu vĩnh viễn trong plugin `vn-infra-consulting` để mọi phiên làm việc sau luôn ghi nhớ).*

---

## 1. Kiến Trúc TDT & Công Cụ Bổ Trợ Đã Cài Trên Máy
- **Bản cài gốc TDT:** `C:\Program Files (x86)\TDT Solution 2022` (không sửa file gốc của hãng).
- **Thư mục khởi động (Startup):** `D:\TDT_CAD2024_DIDONG\STARTUP\` (`acad.rx`, `acad.lsp`, `acaddoc.lsp`) tự động nạp:
  - 7 MenuGroups TDT: `KSVN`, `VNROAD`, `SANNEN`, `KVN`, `DCCT`, `TDT3D`, `RM`.
  - Hơn 20 module ARX/DBX: `TDTObjects.dbx`, `AlignmentDb.dbx`, `AlignmentUI.arx`, `HorizontalProfileDesign.arx`, `NhapSoLieuTuyen.arx`, `ProjectDH.arx`, `SNVN.arx`, `RoadMarkingUI.arx`, `RoadSignsUI.arx`...
  - Bộ lệnh **Vạch sơn QCVN 41:2024** (`VACHSON41.lsp`): `VSDONVI`, `VS73`–`VS78`, `VS41`–`VS44`, `VS61`, `VS62`, `VS92`, `VSCATALOG`, `VSHELP`.
  - Bộ lệnh **Kiểm tra tự động TKĐ AUTO** (`TKDAUTO_KIEMTRA.lsp`): `KTTHAMSO`, `KTDOC`, `KTBTH`, `KTBUOC`, `KLSON`, `KTALL`, `KTHELP`.
- **Thư viện tham khảo sẵn có:**
  - Bộ vạch sơn & biển báo QCVN 41:2024: `D:\CATALO_VSBB_QCVN_41_2024\`
  - Bản vẽ mẫu TDT hoàn chỉnh: `D:\TDT_CAD2024_DIDONG\CHAY_THU_20261111\TUYEN_THU_HOAN_TAT.dwg`

---

## 2. Nguyên Tắc Vàng Khi Điều Khiển AutoCAD + TDT Qua MCP (`vn-infra-consulting_autocad`)
1. **Chỉ mở MỘT phiên AutoCAD 2024 duy nhất** ở quyền người dùng thường (không *Run as Administrator*) để tránh xung đột COM.
2. **Bảo vệ bản gốc:** Tuyệt đối không vẽ/ghi đè trực tiếp lên file trong `D:\TDT_CAD2024_DIDONG\`; luôn sao chép bản vẽ sang thư mục dự án làm việc rồi mới thao tác.
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
| **3. Trắc ngang & Khuôn đường** | `TN` `(100/100)` → `TKTN` → `TKAD` → `DIENTKTN` | Xuất trắc ngang tự nhiên (`100/100`), áp khuôn kết cấu áo đường (`TCCS 38:2022` / `QĐ 3230`), lề, rãnh biên, taluy. |
| **4. Đào đắp & Tổng hợp KL** | `DAODAP` → `BTH` → `CNB` | **Quy tắc thực chiến `DAODAP`:** chạy từng lượt dòng 1, đổi cao độ Y, **không dùng dấu phẩy trong tên**, **không bấm Enter trong lưới**; chữ diện tích `DAODAP` thẳng hàng phía trên mặt thiết kế, không đè nét. Xuất bảng `BTH` và kiểm tra $V = \frac{A_1+A_2}{2}\times L$. |
| **5. Vạch sơn & Biển báo** | `VS73`..`VS92`, `VSCATALOG`, menu `RM` | Bố trí báo hiệu & vạch kẻ đường đúng **QCVN 41:2024/BGTVT** (lưu trên layer `VS_*`, `BIEN BAO`). |
| **6. Dàn trang in A3** | `INTD`, `INTN` (chuẩn A3 `TCVN 7285/5571`) | **Bình đồ + Trắc dọc chung khung A3** (thước cao độ vừa phạm vi tuyến, đường đỏ liền tới cọc cuối); **Trắc ngang chia khung A3** gọn gàng, không đè nét; khung tên góc dưới phải 6 chức danh ký. |
| **7. Tự kiểm thử tự động** | **`KTTHAMSO` → `KTALL`** + Python `audit_boq_excel.py` | Chạy `KTALL` (`KTBUOC`, `KTDOC`, `KTBTH`, `KLSON`), đọc `<ten_ban_ve>_KIEMTRA.txt` xuất cạnh file `.dwg`, đối chiếu chéo 3 chiều với Thuyết minh & Dự toán Excel. |

---

## 4. Bộ Layer TDT Chuẩn Để Đọc & Thẩm Tra Tự Động
- **Tuyến & Trắc dọc:** `TUYEN`, `plinetdtn`, `tracdocthietke`, `entkhieult`, `entdauco`, `Texttencoc`.
- **Trắc ngang & Khuôn đường:** `enttntunhien`, `linedongtn`, `plinetntn`, `MSSTracNgang`, `Mat duong 1 Trai/Phai`, `Le GC Trai/Phai`, `Le KGC Trai/Phai`, `Ranh Trai/Phai`, `Taluy Trai/Phai`, `Taluy_FACE`.
- **Khối lượng & ATGT:** `diendientich`, `BangTongHop`, `VS_*`, `BIEN BAO`, `TEN BIEN BAO`, `THONGKE BIENBAO`.

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
