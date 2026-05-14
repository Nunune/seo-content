---
name: content-intro
description: |
  Viết phần mở bài theo framework APP (Agree - Promise - Preview).
  3 đoạn 80-120 từ kéo người đọc vào bài trong 10 giây đầu, keyword tự nhiên trong 100 từ đầu.
  Kích hoạt khi user yêu cầu: "APP intro", "viết mở bài", "intro hấp dẫn",
  "hook bài blog", "mở đầu bài viết", "intro video", "viết phần mở", "mở bài SEO".
  Cú pháp: --keyword "X" [--draft path/to/draft.md] [--tone "giọng văn"] [--variants 3] [--lang vi|en]
argument-hint: --keyword "X" [--draft path/to/draft.md] [--tone "giọng văn"] [--variants 3] [--lang vi|en]
allowed-tools: [Read, Write]
---

# Content Intro — Viết Mở Bài theo Framework APP

Viết phần intro ngắn gọn, đủ sức kéo người đọc tiếp tục đọc toàn bài.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: từ khóa/chủ đề bài viết
- `--draft path` — TÙY CHỌN: đường dẫn draft đã có → đọc để hiểu context, đề xuất thay phần intro hiện tại
- `--tone "giọng văn"` — TÙY CHỌN: ví dụ "thân thiện", "chuyên nghiệp", "trực tiếp" (mặc định: theo brand_tone trong profile)
- `--variants N` — TÙY CHỌN: số phiên bản intro cần tạo (mặc định: 3)
- `--lang vi|en` — TÙY CHỌN: ngôn ngữ (mặc định: vi)

Nếu không có `--keyword`, hỏi user ngay.

## Framework APP

### A — Agree (Đồng ý, 2-3 câu)
Mở đầu bằng điều người đọc **đang cảm thấy hoặc đang gặp phải** — họ phải gật đầu "đúng rồi".

Quy tắc:
- Dùng "bạn", tone đồng cảm, không phán xét
- Nêu sự thật hiển nhiên hoặc nỗi đau phổ biến
- KHÔNG giới thiệu sản phẩm/giải pháp ở đây

### P — Promise (Hứa hẹn, 2-3 câu)
Vẽ ra **tương lai tươi sáng** nếu họ tiếp tục đọc — nhưng chưa nói cụ thể là gì.

Quy tắc:
- Dùng cấu trúc "Nhưng có tin tốt...", "Và đây là điều tôi muốn bạn biết..."
- Hứa kết quả cụ thể đo được
- Tạo curiosity gap — họ muốn biết "làm thế nào?"

### P — Preview (Xem trước, 2-3 câu)
Tóm tắt CHÍNH XÁC những gì họ sẽ học/nhận được trong bài.

Quy tắc:
- Dùng dạng bullet nhanh hoặc liệt kê "Bạn sẽ học..."
- KHÔNG spoil toàn bộ, chỉ đủ để họ muốn đọc tiếp
- Kết bằng câu kéo vào bài: "Hãy bắt đầu." / "Cùng tìm hiểu." / "Đây là cách."

**Yêu cầu kỹ thuật:**
- Tổng: 80-120 từ
- Keyword xuất hiện tự nhiên trong 100 từ đầu
- Câu ≤20 từ, đoạn 2-3 câu mỗi phần

## Quy trình thực hiện

### Bước 1 — Thu thập context

**Nếu có `--draft`**: Đọc file draft → lấy chủ đề, tone, cấu trúc bài để viết intro phù hợp.

**Đọc profile**: Đọc `D:\Nunu-Claude\seo_content\profiles\default.json` → lấy `brand_tone`, `target_audience`.

**Nếu `--tone` được chỉ định**: ưu tiên `--tone` thay vì `brand_tone`.

### Bước 2 — Viết N variants

Tạo N phiên bản intro (theo `--variants`, mặc định 3). Mỗi variant khác nhau ở:
- **Variant 1**: Agree mạnh về nỗi đau (emotional hook)
- **Variant 2**: Agree mạnh về thực tế/số liệu (factual hook)
- **Variant 3**: Agree mạnh về tình huống quen thuộc (story hook)

Output format:
```
## Intro Variant 1 — Emotional Hook
---
[A — Agree: 2-3 câu đồng cảm với nỗi đau]

[P — Promise: 2-3 câu hứa hẹn kết quả]

[P — Preview: 2-3 câu liệt kê sẽ học được gì. Kết: "Hãy bắt đầu."]
---
📊 Từ: ~[số từ] | Keyword: xuất hiện ở câu [số]

## Intro Variant 2 — Factual Hook
---
[...]
---

## Intro Variant 3 — Story Hook
---
[...]
---

**Gợi ý chọn:**
- Variant 1: phù hợp nếu bài viết về [use case]
- Variant 2: phù hợp nếu bài viết về [use case]
- Variant 3: phù hợp nếu bài viết về [use case]
```

### Bước 3 — Đề xuất thay intro (nếu có `--draft`)

Nếu draft đã có intro → show intro hiện tại → so sánh với variant tốt nhất → gợi ý thay thế.

```
## Intro hiện tại trong draft:
> [trích dẫn intro cũ]
⚠️ Điểm yếu: [không có Agree rõ ràng / Promise mơ hồ / Preview thiếu]

## Đề xuất thay bằng Variant [N]:
[intro mới]
✅ Cải thiện: [giải thích tại sao tốt hơn]
```

### Bước 4 — Thông báo hoàn thành

```
✅ Content Intro — Hoàn thành
Keyword  : {keyword}
Variants : {N} phiên bản (APP framework)
Tone     : {tone}

Bước tiếp theo:
→ Copy variant phù hợp vào đầu draft
→ /content-headline --keyword "{keyword}"  (nếu chưa có tiêu đề tốt)
→ /seo-audit --file {draft_path}  (nếu muốn kiểm tra toàn bài)
```
