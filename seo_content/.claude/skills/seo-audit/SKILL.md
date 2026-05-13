---
name: seo-audit
description: |
  Kiểm tra và chấm điểm chất lượng content SEO theo checklist 8 giai đoạn chuẩn Google 2025-2026.
  Kích hoạt khi user yêu cầu "audit bài viết", "kiểm tra SEO", "seo audit",
  "chấm điểm content", "review bài SEO", "kiểm tra chất lượng bài", "seo check",
  "đánh giá bài viết", "audit content", "check SEO score", "kiểm tra bài trước khi đăng".
argument-hint: --file output/{category}/{slug}/draft.md | --url https://example.com/bai-viet [--keyword "từ khóa"]
allowed-tools: [WebFetch, Read, Write]
---

# SEO Audit — Kiểm tra & chấm điểm content

Đọc bài viết (từ file hoặc URL), chấm điểm theo checklist 8 giai đoạn,
phát hiện lỗi cụ thể, và tạo báo cáo cải thiện chi tiết với ví dụ sửa.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--file path` — đường dẫn file Markdown cần audit (ưu tiên nếu có cả hai)
- `--url https://...` — URL bài viết đã xuất bản để audit
- `--keyword "X"` — từ khóa chính (nếu không có, tự đoán từ nội dung)

Nếu không có `--file` và `--url`, hỏi user trước khi tiếp tục.

## Quy trình thực hiện

### Bước 1 — Đọc nội dung cần audit

**Nếu có `--file`:** Dùng Read tool đọc file.

**Nếu có `--url`:** Dùng WebFetch để fetch nội dung trang.
Trích xuất: text nội dung, title tag, headings, meta description (nếu có trong HTML head).
Bỏ qua navigation, footer, sidebar — chỉ lấy main content.

### Bước 2 — Xác định từ khóa

Nếu có `--keyword`, dùng làm từ khóa chính để đánh giá.
Nếu không có, tự xác định từ khóa chính từ: H1, mật độ từ xuất hiện nhiều nhất, context tổng thể.
Ghi rõ từ khóa đã xác định vào đầu báo cáo.

### Bước 3 — Đọc checklist tham chiếu

Đọc `D:\Nunu-Claude\seo_content\checklist.md` để có đầy đủ tiêu chí đánh giá.

### Bước 4 — Chấm điểm từng giai đoạn

Đánh giá từng hạng mục. Mỗi hạng mục cho 1 trong 3 trạng thái:
- ✅ **Đạt** — tiêu chí được thực hiện tốt
- ⚠️ **Cần cải thiện** — có nhưng chưa tốt, cần chỉnh sửa
- ❌ **Thiếu** — không có, cần bổ sung

**Giai đoạn 2 — Cấu trúc (15 điểm):**
- Title tag: có trong bài / chứa keyword / 50-60 ký tự / kích thích CTR
- Meta description: có / 140-160 ký tự / có CTA / chứa keyword
- URL slug: có / ngắn / không dấu / chứa keyword
- H1: duy nhất 1 / chứa keyword / 50-60 ký tự
- H2/H3: phân cấp logic / chứa keyword phụ / đọc lướt nắm được nội dung

**Giai đoạn 3 — E-E-A-T & Nội dung (30 điểm):**
- People-first: giải quyết vấn đề cụ thể / đọc xong không cần tìm thêm
- Experience: có ví dụ thực tế / số liệu / trải nghiệm first-hand
- Expertise: thuật ngữ đúng / nguồn uy tín được trích dẫn
- Authoritativeness: bio tác giả / ngày cập nhật
- Mở bài: hook rõ / BLUF / keyword trong 100 từ đầu
- Thân bài: đoạn ngắn / bullet/bảng / FAQ block / mật độ keyword ~1-2%
- Kết bài: tóm tắt / CTA rõ ràng

**Giai đoạn 4 — Media (10 điểm):**
- Alt text ảnh được gợi ý / mô tả đúng / chứa keyword khi phù hợp
- Tên file ảnh mô tả (nếu thấy trong content)
- Đề xuất thêm visual phù hợp chưa

**Giai đoạn 5 — Linking (10 điểm):**

Trước khi chấm Phase 5, đọc `D:\Nunu-Claude\seo_content\content-index.md` để biết danh sách bài đã tồn tại.

- Internal links đã nhúng vào body: số lượng 3-5 / anchor text tự nhiên / link đến pillar content
- **Phantom link check**: với mỗi slug trong `<!-- Internal Links gợi ý -->`, kiểm tra có trong content-index.md không
  - ✅ Slug có trong index → link hợp lệ
  - ⚠️ Slug KHÔNG có trong index → "phantom link" → ghi vào `warnings`, trừ 1pt/link (tối đa -2pt)
- External links: có nguồn uy tín / 1-3 link / anchor text không spam

**Giai đoạn 6 — Technical (10 điểm):**
- Schema markup được gợi ý đúng loại (Article, FAQ, HowTo, Author)
- Structured data đầy đủ các field quan trọng

**Giai đoạn 7A — GEO cơ bản (7 điểm):**
- Cấu trúc Q&A rõ ràng (câu hỏi → trả lời ngay)
- BLUF có trong từng section
- Mỗi đoạn tự đứng được không cần ngữ cảnh
- Có số liệu / thống kê cụ thể
- Định nghĩa thuật ngữ rõ ràng
- Có bảng so sánh hoặc danh sách dễ trích xuất

**Giai đoạn 7B — AIO chuyên sâu (8 điểm):**
- Direct Answer: câu trả lời 40-60 từ ngay sau heading, không cần ngữ cảnh trước
- Semantic Triple: câu Subject–Predicate–Object rõ, không đại từ mơ hồ
- Question-based Headings: heading dạng câu hỏi khớp PAA
- Definition Block: mỗi thuật ngữ chính có block định nghĩa 1-2 câu
- Statistics: ≥3-5 số liệu có nguồn + năm, đặt ngay sau luận điểm
- Comparison Tables: so sánh dùng bảng, có cột "Phù hợp cho ai"
- TL;DR Box: tóm tắt 3-5 ý sau H1
- Freshness Signals: có "Cập nhật: [ngày]" + schema dateModified
- Original Research: ≥1 thông tin gốc (khảo sát, case study, quan điểm độc quyền)
- Disambiguation: phân biệt với khái niệm dễ nhầm
- Conversational Tone: câu tự nhiên, trả lời được "làm thế nào / tại sao / khi nào"

**Giai đoạn 1 — Research (10 điểm, đánh giá gián tiếp qua nội dung):**
- Keyword phụ và LSI được sử dụng tự nhiên
- Nội dung bao phủ đủ sub-topic quan trọng
- Không bỏ sót câu hỏi người dùng thường tìm kiếm

### Bước 5 — Tính điểm tổng

Công thức: Tính theo trọng số từng giai đoạn (xem checklist.md phần thang điểm).
Điểm tổng: 0-100 (giai đoạn 8 không tính vào tổng, đánh giá riêng).

### Bước 6 — Tạo danh sách lỗi ưu tiên

Phân loại:
- **Ưu tiên cao (❌)**: lỗi ảnh hưởng nhiều đến ranking, cần sửa ngay
- **Ưu tiên trung (⚠️)**: cần cải thiện nhưng không critical
- **Gợi ý thêm**: nâng cấp từ tốt lên xuất sắc

Với MỖI lỗi ❌ và ⚠️: đưa ví dụ cụ thể:
> "Hiện tại: X → Gợi ý sửa: Y"

### Bước 7 — Xác định thư mục và lưu 2 file

Tạo slug: từ keyword hoặc H1 (ASCII, gạch ngang, không dấu).

**Xác định thư mục bài viết:**
- Nếu `--file` được cung cấp: lấy thư mục cha của file draft.
  - VD: `output/digital-marketing/ung-dung-ai-vao-seo/draft.md` → thư mục = `output/digital-marketing/ung-dung-ai-vao-seo/`
- Nếu `--url`: lưu vào `output/_shared/audits/` (không có category)

Lưu báo cáo Markdown: `{thu_muc_bai_viet}\audit.md`
Lưu điểm JSON: `{thu_muc_bai_viet}\audit.json`

## Định dạng file audit.md

```markdown
# Báo cáo SEO Audit: {Tiêu đề bài / Keyword}

**Ngày audit:** {YYYY-MM-DD}
**Keyword chính:** {keyword}
**Nguồn:** {file path hoặc URL}

---

## Tổng điểm: {X}/100 — {Xuất sắc / Tốt / Trung bình / Yếu / Kém}

| Giai đoạn | Điểm tối đa | Điểm đạt | Trạng thái |
|-----------|------------|---------|-----------|
| GĐ1 — Nghiên cứu | 10 | X | ✅/⚠️/❌ |
| GĐ2 — Cấu trúc | 15 | X | ✅/⚠️/❌ |
| GĐ3 — E-E-A-T / Nội dung | 30 | X | ✅/⚠️/❌ |
| GĐ4 — Media | 10 | X | ✅/⚠️/❌ |
| GĐ5 — Linking | 10 | X | ✅/⚠️/❌ |
| GĐ6 — Technical | 10 | X | ✅/⚠️/❌ |
| GĐ7A — GEO cơ bản | 7 | X | ✅/⚠️/❌ |
| GĐ7B — AIO chuyên sâu | 8 | X | ✅/⚠️/❌ |

---

## Lỗi cần sửa ngay (❌ Ưu tiên cao)

### 1. {Tên lỗi}
- **Vấn đề:** {mô tả cụ thể}
- **Hiện tại:** "{đoạn text hiện tại}"
- **Gợi ý sửa:** "{đoạn text đề xuất}"

### 2. {Tên lỗi}
...

---

## Cần cải thiện (⚠️ Ưu tiên trung)

### 1. {Tên mục cần cải thiện}
- **Hiện tại:** {tình trạng}
- **Cần làm:** {hành động cụ thể}

---

## Chi tiết từng giai đoạn

### Giai đoạn 2 — Cấu trúc

- ✅/⚠️/❌ **Title tag:** {nhận xét cụ thể}
- ✅/⚠️/❌ **Meta description:** {nhận xét}
- ✅/⚠️/❌ **URL slug:** {nhận xét}
- ✅/⚠️/❌ **H1:** {nhận xét}
- ✅/⚠️/❌ **H2/H3:** {nhận xét}

### Giai đoạn 3 — E-E-A-T & Nội dung

- ✅/⚠️/❌ **People-first:** {nhận xét}
- ✅/⚠️/❌ **Experience / số liệu:** {nhận xét}
- ✅/⚠️/❌ **Expertise / nguồn trích dẫn:** {nhận xét}
- ✅/⚠️/❌ **Mở bài (BLUF + keyword):** {nhận xét}
- ✅/⚠️/❌ **Thân bài (đoạn ngắn, bullet, FAQ):** {nhận xét}
- ✅/⚠️/❌ **Kết bài (tóm tắt + CTA):** {nhận xét}

### Giai đoạn 7A — GEO cơ bản

- ✅/⚠️/❌ **Cấu trúc Q&A:** {nhận xét}
- ✅/⚠️/❌ **BLUF per section:** {nhận xét}
- ✅/⚠️/❌ **Đoạn tự đứng được:** {nhận xét}
- ✅/⚠️/❌ **Số liệu / thống kê:** {nhận xét}
- ✅/⚠️/❌ **Định nghĩa thuật ngữ:** {nhận xét}
- ✅/⚠️/❌ **Bảng so sánh / danh sách:** {nhận xét}

### Giai đoạn 7B — AIO chuyên sâu

- ✅/⚠️/❌ **Direct Answer Format:** {câu trả lời 40-60 từ ngay sau heading}
- ✅/⚠️/❌ **Semantic Triple / Entity Clarity:** {không đại từ mơ hồ, SPO rõ}
- ✅/⚠️/❌ **Question-based Headings:** {heading dạng câu hỏi, khớp PAA}
- ✅/⚠️/❌ **Definition Block:** {thuật ngữ chính có block định nghĩa}
- ✅/⚠️/❌ **Statistics có nguồn + năm:** {số liệu đặt đúng chỗ}
- ✅/⚠️/❌ **Comparison Table:** {dùng bảng khi so sánh, có cột "Phù hợp cho ai"}
- ✅/⚠️/❌ **TL;DR Box:** {tóm tắt 3-5 ý sau H1}
- ✅/⚠️/❌ **Freshness Signals:** {"Cập nhật: ngày" + dateModified schema}
- ✅/⚠️/❌ **Original Research:** {≥1 thông tin gốc độc quyền}
- ✅/⚠️/❌ **Disambiguation:** {phân biệt khái niệm dễ nhầm}
- ✅/⚠️/❌ **Conversational Tone:** {tự nhiên, trả lời được "tại sao / khi nào"}

[... các giai đoạn khác ...]

---

## Gợi ý nâng cấp (từ Tốt lên Xuất sắc)

- {gợi ý 1}
- {gợi ý 2}

---

## Schema Markup gợi ý

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  ...
}
```

[Thêm FAQPage schema nếu bài có FAQ block]
```

## Định dạng file audit.json

```json
{
  "keyword": "{keyword}",
  "source": "{file path hoặc URL}",
  "audited_at": "{ISO 8601 datetime}",
  "total_score": 0,
  "grade": "pass|warn|fail",
  "phases": {
    "phase1_research": { "score": 0, "max": 10, "status": "pass|warn|fail" },
    "phase2_structure": { "score": 0, "max": 15, "status": "pass|warn|fail" },
    "phase3_eeeat": { "score": 0, "max": 30, "status": "pass|warn|fail" },
    "phase4_media": { "score": 0, "max": 10, "status": "pass|warn|fail" },
    "phase5_linking": { "score": 0, "max": 10, "status": "pass|warn|fail" },
    "phase6_technical": { "score": 0, "max": 10, "status": "pass|warn|fail" },
    "phase7a_geo": { "score": 0, "max": 7, "status": "pass|warn|fail" },
    "phase7b_aio": { "score": 0, "max": 8, "status": "pass|warn|fail" }
  },
  "critical_issues": [],
  "warnings": [],
  "suggestions": []
}
```

(Điền "pass" nếu score >= 75% max, "warn" nếu 50-74%, "fail" nếu < 50%)

## Thông báo hoàn thành

Sau khi lưu cả 2 file, tóm tắt ngắn gọn:
- Tổng điểm và xếp loại
- Top 3 lỗi quan trọng nhất cần sửa ngay
- Đường dẫn 2 file đã lưu: `output/{category}/{slug}/audit.md` và `audit.json`
- Nếu điểm < 75: "Sau khi sửa, chạy lại `/seo-audit --file output/{category}/{slug}/draft.md` để kiểm tra lại"
- Nếu điểm >= 75: "Bài đã đủ chất lượng để đăng. Xem TODO trong file draft trước."
