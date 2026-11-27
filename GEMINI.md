# GEMINI.md — Điểm Nạp Bộ Não Dùng Chung (Antigravity / Gemini CLI)

> File này là điểm nạp tự động cho **Antigravity** và **Gemini CLI**. Toàn bộ quy tắc nguồn được quản lý tập trung tại **[BRAIN.md](BRAIN.md)** để tránh trùng lặp khi chỉnh sửa trên GitHub.

## Chỉ dẫn nạp bắt buộc
1. **Đọc toàn bộ [BRAIN.md](BRAIN.md)** trước khi bắt đầu mọi tác vụ chuyên môn.
2. **Xác định vai trò phiên làm việc:**
   - Mặc định **AI 1 (Thực thi):** tuân thủ [prompts/AI1_THUC_THI.md](prompts/AI1_THUC_THI.md).
   - Khi chạy phản biện / kiểm tra độc lập (**AI 2 – QA Auditor**): tuân thủ [prompts/AI2_QA_AUDITOR.md](prompts/AI2_QA_AUDITOR.md).
3. **Tra cứu chuyên sâu:** đọc các file Markdown tương ứng trong `knowledge/` (`01_` → `05_`) và chạy script Python trong `scripts/` để kiểm chứng số học.
4. **Đồng bộ đa AI qua Git:**
   - Đầu phiên: `git pull` để nhận cập nhật mới nhất từ Claude / ChatGPT / Gemini.
   - Cuối mốc lớn: cập nhật `knowledge/05_nhat_ky_duc_ket_kinh_nghiem.md` hoặc `projects/<ma-du-an>/` rồi `git add / commit / push`.
5. **An toàn Public Repo:** Tuyệt đối không commit file hồ sơ dự án mật, bản vẽ CAD, Excel dự toán thật hoặc thông tin cá nhân.
