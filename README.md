# 🧠 VN-INFRA AI Shared Brain (`v2.4 · 2026`)

> **Bộ não dùng chung tối giản trên GitHub** cho **Claude**, **ChatGPT**, **Gemini** và **Antigravity**.  
> Chỉnh sửa trực tiếp từng file Markdown trên GitHub — **một nguồn sự thật duy nhất (`BRAIN.md`)**, không cần build phức tạp.

---

## 1. Cấu Trúc Kho Tối Giản

```text
vn-infra-ai-brain/
├── BRAIN.md                ← Nguồn quy tắc cốt lõi duy nhất (sửa 1 chỗ, mọi AI đều cập nhật)
├── CLAUDE.md               ← Điểm nạp tự động cho Claude / Claude Code / Claude Projects
├── GEMINI.md               ← Điểm nạp tự động cho Antigravity / Gemini CLI
├── AGENTS.md               ← Điểm nạp chuẩn mở cho ChatGPT Codex / Multi-Agent
├── prompts/
│   ├── AI1_THUC_THI.md     ← System Prompt AI 1 (Thực thi — tối ưu < 5.000 ký tự)
│   └── AI2_QA_AUDITOR.md   ← System Prompt AI 2 (QA Auditor độc lập 5 lớp)
├── knowledge/
│   ├── 01_phap_ly_tieu_chuan_thiet_ke_duong.md
│   ├── 02_tdt_autocad_ban_ve_tcvn.md
│   ├── 03_tham_tra_du_toan_quy_hoach.md
│   ├── 04_quy_trinh_van_hanh_bo_nao.md
│   └── 05_nhat_ky_duc_ket_kinh_nghiem.md
├── scripts/
│   ├── audit_boq_excel.py  ← Kiểm toán tự động công thức & bẫy Excel BOQ/Dự toán
│   ├── init_project_brain.py
│   ├── mca_scoring.py
│   └── snapshot_project.py
├── resources/
│   └── GEMINI_template.md  ← Mẫu được script khởi tạo dự án sử dụng
├── tests/
│   └── test_project_data_safety.py
└── projects/
    ├── README.md           ← Bảng theo dõi các dự án (chỉ lưu Markdown phi mật)
    └── _TEMPLATE/          ← Mẫu bộ não dự án & nhật ký quyết định chuẩn 2026
```

---

## 2. Raw URL Trực Tiếp (Dùng Chung Cho Mọi AI)

> *Sau khi đẩy lên GitHub, các link dưới đây luôn trả về phiên bản mới nhất trên nhánh `main`:*

- **Bộ não lõi (`BRAIN.md`):** `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/BRAIN.md`
- **Prompt AI 1 (Thực thi):** `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/prompts/AI1_THUC_THI.md`
- **Prompt AI 2 (QA Auditor):** `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/prompts/AI2_QA_AUDITOR.md`
- **KB #1 Pháp lý & Thiết kế đường:** `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/knowledge/01_phap_ly_tieu_chuan_thiet_ke_duong.md`
- **KB #2 TDT AutoCAD & Bản vẽ TCVN:** `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/knowledge/02_tdt_autocad_ban_ve_tcvn.md`
- **KB #3 Thẩm tra, Dự toán & Quy hoạch:** `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/knowledge/03_tham_tra_du_toan_quy_hoach.md`
- **KB #4 Quy trình vận hành & Bộ não dự án:** `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/knowledge/04_quy_trinh_van_hanh_bo_nao.md`
- **KB #5 Nhật ký đúc kết thực chiến:** `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/knowledge/05_nhat_ky_duc_ket_kinh_nghiem.md`

---

## 3. Hướng Dẫn Kết Nối 4 Nền Tảng AI (1 Phút Thiết Lập)

### 3.1. Claude (Claude Projects & Claude Code)
- **Cách 1 — Claude Projects (Web/Desktop, khuyên dùng):**
  1. Tạo 2 Project: `HTGT - AI 1 Thực thi` và `HTGT - AI 2 QA Auditor`.
  2. Dán nội dung `prompts/AI1_THUC_THI.md` (hoặc `AI2_QA_AUDITOR.md`) vào **Project Instructions**.
  3. Tại mục **Project Knowledge**, bấm **Add from GitHub** → chọn repo `quoclepr/vn-infra-ai-brain` → chọn `BRAIN.md`, thư mục `knowledge/` và `projects/`. Khi cập nhật trên GitHub, chỉ cần bấm **Sync** 1 lần.
- **Cách 2 — Claude Code (Local):** Clone repo về máy; Claude Code tự động nạp `CLAUDE.md` → `BRAIN.md`.

### 3.2. ChatGPT (Custom GPT, ChatGPT Projects & Codex)
- **Cách 1 — ChatGPT Web (đọc trực tiếp qua Raw URL):**
  - Mở chat mới và dán câu lệnh khởi động ở Mục 4 (ChatGPT bật Web/Browse sẽ đọc thẳng các Raw URL mới nhất).
- **Cách 2 — Custom GPT (2 GPT: AI 1 & AI 2):**
  1. Dán nội dung `prompts/AI1_THUC_THI.md` (hoặc `AI2_QA_AUDITOR.md`) vào ô **Instructions** (vừa khít giới hạn 8.000 ký tự).
  2. Bật **Code Interpreter & Data Analysis** và **Web Search**.
  3. Tải lên 5 file trong `knowledge/` + `scripts/audit_boq_excel.py` (hoặc gắn GitHub Connector trong ChatGPT Plus/Team/Enterprise).
- **Cách 3 — Codex / OpenAI Agents:** Kết nối trực tiếp repo GitHub này; Codex tự đọc `AGENTS.md` → `BRAIN.md`.

### 3.3. Google Gemini (Gems & Gemini CLI)
- **Cách 1 — Gemini Gems (Web, tạo 2 Gem AI 1 & AI 2):**
  1. Dán nội dung `prompts/AI1_THUC_THI.md` (hoặc `AI2_QA_AUDITOR.md`) vào ô **Instructions**, kèm thêm 1 dòng tham chiếu link repo `https://github.com/quoclepr/vn-infra-ai-brain`.
  2. Tại mục **Knowledge**, tải lên `BRAIN.md` và các file trong `knowledge/` (hoặc kết nối trực tiếp kho GitHub qua tính năng Import code/GitHub trong Gemini).
- **Cách 2 — Gemini CLI:** Clone repo về máy; Gemini CLI tự đọc `GEMINI.md` → `BRAIN.md`.

### 3.4. Antigravity (Trung Tâm Đồng Bộ Chính Trên Máy)
1. Mở thư mục `vn-infra-ai-brain` làm workspace (hoặc tham chiếu trực tiếp từ máy). Antigravity tự nạp `GEMINI.md` + `AGENTS.md` + plugin `vn-infra-consulting`.
2. **Đầu phiên:** chạy `git pull` để nhận mọi cập nhật mới từ GitHub.
3. **Sau khi rút ra bài học mới hoặc chốt mốc dự án:** cập nhật `knowledge/05_nhat_ky_duc_ket_kinh_nghiem.md` hoặc `projects/<MA_DU_AN>/` rồi `git add . && git commit -m "Cap nhat bo nao" && git push`.

---

## 4. Câu Lệnh Khởi Động Nhanh Cho Chat Thường (Copy–Paste 1 Dòng)

Dùng khi mở một cuộc chat mới trên **ChatGPT / Claude / Gemini** mà chưa tạo Project/Gem:

> **Vai AI 1 (Thực thi):**  
> *"Hãy đọc toàn bộ quy tắc tại `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/BRAIN.md` và `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/prompts/AI1_THUC_THI.md`. Từ bây giờ bạn đóng vai AI 1 – Trợ lý Kỹ thuật Thực thi, tuân thủ 100% khung pháp lý 01/07/2026, TCVN/QCVN, Python-First và định dạng đầu ra 3 dòng + Auto-QA. Xác nhận ngắn gọn 3 dòng để bắt đầu."*

> **Vai AI 2 (QA Auditor phản biện độc lập):**  
> *"Hãy đọc toàn bộ quy tắc tại `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/BRAIN.md` và `https://raw.githubusercontent.com/quoclepr/vn-infra-ai-brain/main/prompts/AI2_QA_AUDITOR.md`. Từ bây giờ bạn đóng vai AI 2 – QA Auditor kiểm tra độc lập 5 lớp không nể nang. Xác nhận ngắn gọn 2 dòng để tôi gửi sản phẩm cần soi lỗi."*

---

## 5. Quy Tắc Bảo Mật Bắt Buộc (Public Repo)
- Kho này đặt **Public** để mọi AI đọc Raw URL không gặp tường xác thực.
- File `.gitignore` giúp Git bỏ qua các tệp chưa được theo dõi theo mẫu tên: `*.dwg`, `*.dxf`, `*.ntd`, `*.pdf`, `*.docx`, `*.xlsx`, `*.xls`, `*.zip`, `.env`, `*secret*`, `*token*`. Tệp đã được Git theo dõi vẫn có thể được commit; `.gitignore` không quét nội dung để phát hiện khóa bị dán vào mã nguồn hay Markdown.
- **Chỉ lưu:** quy tắc, tiêu chuẩn, prompt, script tổng quát và ghi chú dự án đã ẩn danh/phi mật.
- **Không bao giờ đưa lên kho này:** tên chủ đầu tư/nhà thầu nhạy cảm, đơn giá thầu mật, file bản vẽ/dự toán thật, thông tin cá nhân hoặc API key.

## 6. Khởi tạo và sao lưu dự án cục bộ

```powershell
python scripts/init_project_brain.py --target "./DU_AN_TEST" --code "DA-TEST" --name "Dự án thử" --type tham-tra --git
python scripts/snapshot_project.py --project "./DU_AN_TEST" --label "truoc_khi_sua"
```

- Khi có `--git`, script khởi tạo bổ sung quy tắc loại trừ `.env*`, khóa PEM/KEY/P12/PFX, khóa SSH, tệp đăng nhập Git/npm/Python và tên chứa `secret`, `token`, `credential`. Quy tắc riêng trong `.gitignore` có sẵn được giữ lại; khối bảo vệ được đặt cuối tệp và chạy lại không làm lặp khối đó. Script từ chối ghi qua `.gitignore` là liên kết tệp.
- Script ZIP tự áp dụng bộ lọc tên bí mật kể cả khi dự án không dùng Git. Nó loại thư mục thông tin đăng nhập phổ biến, cache, bản sao lưu cũ và liên kết tệp/thư mục (gồm junction/reparse point trên Windows); `_Backups` phải là thư mục thật. Bộ lọc tên không phân biệt hoa thường.
- Bản sao lưu vẫn giữ tài liệu CAD/Office thông thường phục vụ khôi phục dự án. ZIP không được mã hóa; không chia sẻ ZIP chứa hồ sơ riêng tư lên kho công khai.
- Đây là bộ lọc tên, không phải công cụ quét bí mật trong nội dung hay bộ đọc toàn bộ quy tắc `.gitignore`. Tệp có tên bình thường vẫn có thể chứa thông tin nhạy cảm. Khi bổ sung mẫu tên bí mật, cập nhật cả hai script và kiểm thử hồi quy.
- Chạy trên cây thư mục ổn định, không có tiến trình khác thay đổi liên kết trong lúc sao lưu. Trên Windows, các kiểm thử tạo liên kết tệp cần quyền tạo symbolic link hoặc Developer Mode.
- Trong tài liệu công khai, `<USER_HOME>`, `<LOCAL_WORKSPACE>`, `<TDT_ROOT>` và `<SIGNAGE_ROOT>` là ký hiệu thay cho đường dẫn máy riêng; thay bằng thư mục thực tế khi chạy ví dụ.

Kiểm thử bằng dữ liệu giả, chỉ dùng thư viện chuẩn Python:

```powershell
python -m unittest discover -s tests -v
```
