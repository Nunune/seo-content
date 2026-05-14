---
name: content-ai
description: |
  Viết bài blog tối ưu cho AI Search (Google AI Overviews, ChatGPT Search, Perplexity)
  theo framework FAQ-FIRST: H1 là câu hỏi, TL;DR box, mỗi H2 là câu hỏi tự nhiên, direct answer 40-80 từ.
  Output draft.md tương thích với seo-audit → seo-improve pipeline.
  Kích hoạt khi user yêu cầu: "FAQ-FIRST", "tối ưu AI search", "AI Overviews", "GEO",
  "generative engine optimization", "bài cho ChatGPT", "bài cho Perplexity",
  "tối ưu AI Overview", "featured snippet", "direct answer", "bài hỏi đáp SEO",
  "bài câu hỏi", "FAQ content", "answer engine optimization", "AEO",
  "bài chuẩn AI search 2026", "AI SEO".
  Cú pháp: --keyword "X" --category slug [--questions "Q1|Q2|Q3"] [--author "Tên, Chức danh"] [--lang vi|en]
argument-hint: --keyword "X" --category slug [--questions "Q1|Q2|Q3"] [--author "Tên, Chức danh"] [--lang vi|en]
allowed-tools: [WebSearch, WebFetch, Read, Write]
---

# Content AI — Viết Bài Tối Ưu AI Search theo FAQ-FIRST

Tạo bài blog được tối ưu để xuất hiện trong Google AI Overviews, ChatGPT Search và Perplexity — không chỉ Google Search truyền thống.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: câu hỏi hoặc chủ đề
- `--category slug` — **BẮT BUỘC** (VD: digital-marketing, suc-khoe, bat-dong-san)
- `--questions "Q1|Q2|Q3"` — TÙY CHỌN: override danh sách câu hỏi H2 (ngăn cách bởi |)
- `--author "Tên, Chức danh"` — TÙY CHỌN: override tác giả trong profile
- `--lang vi|en` — TÙY CHỌN: ngôn ngữ (mặc định: vi)

Nếu thiếu `--keyword` hoặc `--category`: hỏi user ngay.

## Quy trình thực hiện

### Bước 1 — Thu thập thông tin

**Đọc profile:** `D:\Nunu-Claude\seo_content\profiles\default.json` → `brand_name`, `brand_tone`, `target_audience`, `author_name`, `author_title`, `brand_website`.

**Tạo slug:** ASCII, gạch ngang, không dấu. VD: "khám phụ khoa ở đâu tốt" → `kham-phu-khoa-o-dau-tot`

**Tạo thư mục:** `D:\Nunu-Claude\seo_content\output\{category}\{slug}\`

**Nghiên cứu PAA (People Also Ask):**

Nếu không có `--questions`:
1. WebSearch `{keyword}` → ghi nhận People Also Ask questions (top 5-8)
2. WebSearch `{keyword} site:vn OR .vn` → ghi nhận câu hỏi phổ biến trong thị trường Việt Nam
3. Tổng hợp 8-12 câu hỏi quan trọng nhất → dùng làm H2 headers

Nếu có `--questions`: Parse danh sách câu hỏi → dùng trực tiếp làm H2 headers.

**[Tùy chọn] Nghiên cứu đối thủ:**
WebFetch 1-2 bài top ranking → xem họ trả lời câu nào, bỏ câu nào → thêm câu họ bỏ qua.

---

## Framework FAQ-FIRST

### 7 Quy tắc bắt buộc

1. **H1 = Câu hỏi tổng quát nhất** về chủ đề (không phải statement)
2. **TL;DR box ngay sau H1** — 5 bullet trả lời trực tiếp toàn bài
3. **Mỗi H2 = Câu hỏi tự nhiên** dạng PAA — KHÔNG dùng "Giới thiệu", "Kết luận", "Phần 1"
4. **Câu đầu mỗi section = Direct Answer 40-80 từ** — tự đứng được KHÔNG cần context bài
5. **Câu SPO rõ ràng** (Subject-Predicate-Object) — không đại từ mơ hồ ("nó", "điều này")
6. **Ít nhất 8 H2** câu hỏi, mỗi section 150-300 từ
7. **FAQ Schema JSON-LD** cuối bài để Google parse dễ hơn

### Direct Answer — Tiêu chuẩn quan trọng nhất

Direct Answer phải:
- **Tự đứng được**: đọc 1 câu này mà không cần đọc bài vẫn hiểu câu trả lời
- **40-80 từ**: đủ dài để informative, đủ ngắn để AI trích dẫn
- **Subject rõ ràng**: không bắt đầu bằng "Nó", "Đây", "Điều này" → dùng tên cụ thể
- **Factual**: ưu tiên definition → số liệu → mechanism → consequence

**Ví dụ tốt vs xấu:**

❌ Tệ: "Đây là một vấn đề rất phổ biến mà nhiều người gặp phải, đặc biệt trong thời đại ngày nay khi..."

✅ Tốt: "[Keyword] là [định nghĩa súc tích]. [Nguyên nhân chính]. [Cách nhận biết hoặc giải quyết]. [Con số/thống kê nếu có]."

### TL;DR Box

Đặt ngay sau H1, trước phần thân bài:
- 5 bullet points, mỗi bullet = 1 câu ngắn trả lời 1 khía cạnh quan trọng
- Đọc TL;DR là hiểu 80% bài
- Format: `> **TL;DR — [Chủ đề]**`

### Bảng so sánh

Thêm bảng so sánh khi chủ đề có nhiều options/lựa chọn:
- So sánh ít nhất 3 options
- Columns: tên option | ưu điểm | nhược điểm | phù hợp cho ai
- Dễ trích xuất bởi AI

---

## Cấu trúc bài FAQ-FIRST

```
<!-- SEO Meta
Title: {keyword} — Giải Đáp Toàn Diện {Năm}
Meta Description: Tìm hiểu {keyword}: {câu trả lời trực tiếp 150 ký tự}...
Slug: {slug}
Keyword chính: {keyword}
Keyword phụ: [3-5 từ khóa phụ từ PAA research]
Schema: FAQPage + Article
-->

# {Keyword}? — Giải Đáp Toàn Diện {Năm}

> **TL;DR — {Chủ đề ngắn gọn}**
> - **[Điểm 1]:** [Trả lời trực tiếp — 1 câu]
> - **[Điểm 2]:** [Trả lời trực tiếp — 1 câu]
> - **[Điểm 3]:** [Trả lời trực tiếp — 1 câu]
> - **[Điểm 4]:** [Trả lời trực tiếp — 1 câu]
> - **[Điểm 5]:** [Trả lời trực tiếp — 1 câu]

[Intro 80-120 từ: tại sao câu hỏi này quan trọng, bài này trả lời những gì, ai nên đọc]

> **Cập nhật:** {Tháng/Năm} — Thông tin được kiểm tra và cập nhật mới nhất.

---

## [Câu hỏi H2 — quan trọng nhất, người dùng tìm nhiều nhất]?

[Direct Answer: 40-80 từ. Subject rõ ràng. Tự đứng được. Không cần đọc phần trước.]

[Body: 100-220 từ bổ sung chi tiết, ví dụ, số liệu]

- [Bullet point 1 — detail cụ thể]
- [Bullet point 2]
- [Bullet point 3]

<!-- [ẢNH] Infographic hoặc diagram minh họa. File: {slug}-h2-1.png
Alt text: "[mô tả ảnh bằng tiếng Việt đầy đủ]" -->

<!-- [NGUỒN] Tìm nghiên cứu/thống kê về {chủ đề} từ nguồn uy tín -->

---

## [Câu hỏi H2 thứ 2]?

[Direct Answer: 40-80 từ]

[Body: 100-220 từ]

[Nếu có nhiều options → thêm bảng so sánh:]

| Lựa chọn | Ưu điểm | Nhược điểm | Phù hợp cho |
|----------|---------|-----------|------------|
| [Option 1] | [+] | [-] | [Ai] |
| [Option 2] | [+] | [-] | [Ai] |
| [Option 3] | [+] | [-] | [Ai] |

---

## [Câu hỏi H2 thứ 3]?

[Direct Answer + Body]

---

[Tiếp tục 5-9 H2 câu hỏi nữa, tổng ≥8 H2]

---

## Câu Hỏi Thường Gặp Khác

**[Câu hỏi ngắn 1]?**
[Trả lời 40-60 từ — tự đứng được]

**[Câu hỏi ngắn 2]?**
[Trả lời 40-60 từ]

**[Câu hỏi ngắn 3]?**
[Trả lời 40-60 từ]

**[Câu hỏi ngắn 4]?**
[Trả lời 40-60 từ]

**[Câu hỏi ngắn 5]?**
[Trả lời 40-60 từ]

---

## Tóm Tắt

[Kết luận 80-100 từ: tóm lại các điểm chính + CTA]

**Đọc thêm:**
- [Internal link 1: bài liên quan]
- [Internal link 2: bài liên quan]

---

<!-- Schema Markup
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "[Câu hỏi H2 1]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Direct Answer 1 — copy từ section tương ứng]"
      }
    },
    {
      "@type": "Question",
      "name": "[Câu hỏi H2 2]?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "[Direct Answer 2]"
      }
    }
  ]
}
-->

<!-- TODO — Cần làm trước khi đăng
- [ ] Verify tất cả số liệu và thêm nguồn trích dẫn
- [ ] Thêm ảnh minh họa cho các section chính
- [ ] Thêm internal links đến bài liên quan
- [ ] Implement Schema JSON-LD trong CMS
- [ ] Kiểm tra Direct Answer: mỗi câu có tự đứng được không?
-->

<!-- Author: {author_name}, {author_title}
Ngày tạo: {date} | Cập nhật: {date}
-->
```

---

### Bước 2 — Áp dụng AI Search Standards

**GEO (Generative Engine Optimization) — Checklist:**

- [ ] Câu đầu mỗi H2 = Direct Answer (Subject + Predicate rõ ràng)
- [ ] Không dùng đại từ mơ hồ ở đầu câu
- [ ] Mỗi Direct Answer 40-80 từ — đủ ngắn để AI trích dẫn
- [ ] TL;DR box ở đầu bài
- [ ] Bảng so sánh cho chủ đề có nhiều options
- [ ] FAQ Schema JSON-LD cuối bài
- [ ] Bullet lists (3-7 items) sau mỗi Direct Answer
- [ ] Câu SPO: "[Tên cụ thể] là/có/làm..." không phải "Nó là..."

**E-E-A-T:**
- Author block với tên và chức danh chuyên môn
- Ngày cập nhật rõ ràng
- Nguồn trích dẫn cho mọi số liệu
- Gợi ý ảnh cho credibility

**UX Writing:**
- Câu ≤20 từ, đoạn 3-4 câu
- Dùng "bạn", active voice
- Bold keyword chính lần đầu xuất hiện trong mỗi section

### Bước 3 — Lưu file

Lưu tại: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\draft.md`

(Output `draft.md` — tương thích với `/seo-audit` → `/seo-improve` pipeline)

### Bước 4 — Thông báo hoàn thành

```
✅ Content AI — Hoàn thành
Framework : FAQ-FIRST (AI Search Optimized)
Keyword   : {keyword}
File      : seo_content/output/{category}/{slug}/draft.md
H2 sections: {N} câu hỏi
Độ dài    : ~{N} từ

AI Search checklist:
→ TL;DR box: ✅
→ Direct Answer mỗi H2: ✅
→ FAQ Schema JSON-LD: ✅
→ Bảng so sánh: {✅ có | — không áp dụng}

Bước tiếp theo (pipeline tương thích):
→ /seo-audit --file seo_content/output/{category}/{slug}/draft.md --keyword "{keyword}"
→ /seo-improve --draft seo_content/output/{category}/{slug}/draft.md --keyword "{keyword}"
```
