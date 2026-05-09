---
name: seo-research
description: |
  Nghiên cứu từ khóa SEO, phân tích SERP và đối thủ cạnh tranh theo chuẩn Google 2025-2026.
  Kích hoạt khi user hỏi về "nghiên cứu từ khóa", "phân tích đối thủ", "seo research",
  "tìm keyword", "phân tích SERP", "content gap", "research bài viết", "tìm ý tưởng content",
  "keyword research", "phân tích từ khóa", "lên brief SEO", "outline bài viết".
argument-hint: --keyword "từ khóa" [--competitor URL1 URL2...] [--lang vi|en]
allowed-tools: [WebSearch, WebFetch, Read, Write]
---

# SEO Research — Nghiên cứu từ khóa & phân tích đối thủ

Thực hiện nghiên cứu SEO toàn diện cho một từ khóa: phân tích SERP, tìm intent, crawl đối thủ,
phát hiện content gap, và tạo research brief đầy đủ sẵn sàng chuyển sang bước viết bài.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: từ khóa chính cần nghiên cứu
- `--competitor URL1 URL2...` — URL bài viết đối thủ muốn phân tích (tối đa 5)
- `--lang vi|en` — ngôn ngữ output (mặc định: vi)

Nếu không có `--keyword`, hỏi user từ khóa trước khi tiếp tục.

## Quy trình thực hiện

### Bước 1 — Phân tích SERP (WebSearch)

Thực hiện 3 lượt tìm kiếm:

1. Tìm kiếm chính:
   - Query: `{keyword}` — lấy top 10 kết quả
   - Ghi nhận: loại trang (blog, ecommerce, news, forum), định dạng (hướng dẫn, danh sách, so sánh)

2. Tìm "People Also Ask":
   - Query: `{keyword} câu hỏi thường gặp` hoặc `{keyword} FAQ`
   - Ghi nhận tối thiểu 5 câu hỏi PAA

3. Tìm từ khóa liên quan:
   - Query: `{keyword} là gì` hoặc `{keyword} như thế nào`
   - Ghi nhận: related searches, LSI keywords, long-tail variants

### Bước 2 — Phân loại Search Intent

Dựa trên SERP, phân loại:
- **Informational**: người dùng muốn học/hiểu
- **Navigational**: người dùng tìm trang cụ thể
- **Commercial**: người dùng so sánh trước mua
- **Transactional**: người dùng muốn mua/đăng ký ngay

### Bước 3 — Crawl bài đối thủ (WebFetch)

Nếu user cung cấp `--competitor URL`:
- WebFetch từng URL, trích xuất:
  - Tiêu đề H1 và cấu trúc H2/H3
  - Độ dài bài (ước tính số từ)
  - Các điểm mạnh (thông tin độc đáo, dữ liệu, ví dụ)
  - Các điểm yếu (thông tin thiếu, lỗi thời, thiếu depth)

Nếu không có `--competitor`:
- Lấy 3 URL từ kết quả tìm kiếm bước 1, WebFetch để phân tích nhanh

### Bước 4 — Xây dựng Keyword Map

Dựa trên nghiên cứu, lập:
- **Primary keyword**: từ khóa chính (đã cho)
- **Secondary keywords** (3-5): biến thể, từ đồng nghĩa có volume
- **LSI keywords** (5-10): entity và khái niệm liên quan
- **Long-tail keywords** (3-5): từ khóa đuôi dài từ PAA

### Bước 5 — Phát hiện Content Gap (Information Gain)

Sau khi đọc các bài đối thủ, liệt kê:
- Thông tin nào ĐỐI THỦ THIẾU mà bài mới có thể bổ sung
- Góc nhìn mới nào chưa được khai thác
- Dữ liệu, ví dụ, case study nào có thể làm độc đáo hơn

### Bước 6 — Tạo Outline đề xuất

Xây dựng cấu trúc bài viết:
- H1: tiêu đề (chứa keyword chính)
- H2/H3: phân cấp logic, mỗi H2 trả lời một sub-topic rõ ràng
- Đảm bảo headings đọc lướt vẫn nắm được toàn bộ nội dung

### Bước 7 — Đọc file profile (nếu cần)

Đọc `D:\Nunu-Claude\seo_content\profiles\default.json` để biết brand_name và industry.
Dùng thông tin này để customize outline phù hợp với thương hiệu.

### Bước 8 — Tạo Research Brief và lưu file

Tạo slug từ keyword (chuyển sang ASCII, thay dấu cách bằng `-`, bỏ dấu tiếng Việt).
Ví dụ: "học lái xe ô tô" → `hoc-lai-xe-o-to`

Lưu file tại: `D:\Nunu-Claude\seo_content\output\research_{slug}.md`

## Định dạng file output

```markdown
# Research Brief: {Keyword}

**Ngày tạo:** {YYYY-MM-DD}
**Từ khóa chính:** {keyword}
**Search Intent:** {loại intent}
**Ngôn ngữ target:** {vi/en}

---

## 1. Keyword Map

### Primary Keyword
- {keyword chính}

### Secondary Keywords
- {kw phụ 1} 
- {kw phụ 2}
- ...

### LSI Keywords & Entities
- {entity 1}
- {entity 2}
- ...

### Long-tail Keywords (từ PAA)
- {long-tail 1}
- {long-tail 2}
- ...

---

## 2. Phân tích SERP

**Định dạng được Google ưu tiên:** {loại nội dung phổ biến nhất trong top 10}
**Độ dài trung bình bài top:** {ước tính}

### Top 5 kết quả
| # | Tiêu đề | Domain | Loại trang |
|---|---------|--------|-----------|
| 1 | ... | ... | ... |
...

### People Also Ask
1. {câu hỏi 1}
2. {câu hỏi 2}
...

---

## 3. Phân tích đối thủ

### {Đối thủ 1 — domain}
- **Điểm mạnh:** ...
- **Điểm yếu / thiếu:** ...
- **Cấu trúc H2:** ...

### {Đối thủ 2 — domain}
...

---

## 4. Content Gap — Information Gain

Những điểm bài mới CẦN có mà đối thủ CHƯA làm tốt:
- {điểm 1}
- {điểm 2}
- ...

---

## 5. Outline đề xuất

**H1:** {Tiêu đề đề xuất — chứa keyword, 50-60 ký tự}

**H2: {Section 1}**
  - H3: {Sub-point 1}
  - H3: {Sub-point 2}

**H2: {Section 2}**
  - H3: {Sub-point 1}
  ...

**H2: FAQ — Câu hỏi thường gặp**
  - H3: {Câu hỏi từ PAA 1}
  - H3: {Câu hỏi từ PAA 2}
  ...

**H2: Kết luận**

---

## 6. Gợi ý tiêu đề (3 lựa chọn)

1. {Tiêu đề A — dạng How-to, có số}
2. {Tiêu đề B — dạng hỏi đáp, có năm 2025/2026}
3. {Tiêu đề C — dạng lợi ích rõ ràng}

## 7. Meta Description gợi ý

> {140-160 ký tự, chứa keyword, có CTA}

## 8. URL Slug gợi ý

`{slug-khong-dau-bang-tieng-anh}`
```

## Thông báo hoàn thành

Sau khi lưu file, báo cáo ngắn gọn:
- Đường dẫn file đã lưu
- Search intent được xác định
- Số đối thủ đã phân tích
- Top 3 content gap quan trọng nhất
- Gợi ý: "Dùng `/seo-write --keyword "{keyword}" --research seo_content/output/research_{slug}.md` để viết bài"
