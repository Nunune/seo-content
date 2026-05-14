---
name: content-seo
description: |
  Viết bài blog SEO dài theo cấu trúc LISTICLE, HOW-TO, SKYSCRAPER hoặc PILLAR-CLUSTER.
  Output draft.md tương thích với seo-audit → seo-improve pipeline.
  Kích hoạt khi user yêu cầu: "listicle", "top X", "X cách", "X lý do",
  "hướng dẫn", "cách làm", "how-to", "từng bước", "bài hướng dẫn",
  "skyscraper", "bài SEO dài", "vượt đối thủ", "bài blog chuẩn SEO",
  "pillar", "content hub", "bài blog dài", "content authority".
  Cú pháp: --keyword "X" --category slug [--format LISTICLE|HOW-TO|SKYSCRAPER|PILLAR] [--competitor URL1 URL2] [--length 1500|3000|5000] [--author "Tên, Chức danh"] [--lang vi|en]
argument-hint: --keyword "X" --category slug [--format LISTICLE|HOW-TO|SKYSCRAPER|PILLAR] [--competitor URL1 URL2] [--length 1500|3000|5000] [--author "Tên, Chức danh"] [--lang vi|en]
allowed-tools: [WebSearch, WebFetch, Read, Write]
---

# Content SEO — Viết Blog SEO theo LISTICLE / HOW-TO / SKYSCRAPER / PILLAR

Tạo bài blog SEO dài theo cấu trúc phù hợp với mục tiêu từ khóa và đối thủ.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**
- `--category slug` — **BẮT BUỘC** (VD: digital-marketing, suc-khoe, social-media)
- `--format LISTICLE|HOW-TO|SKYSCRAPER|PILLAR` — TÙY CHỌN
- `--competitor URL1 URL2` — TÙY CHỌN: tối đa 3 URL đối thủ (dùng cho SKYSCRAPER)
- `--length 1500|3000|5000` — TÙY CHỌN: độ dài mục tiêu (mặc định theo format)
- `--author "Tên, Chức danh"` — TÙY CHỌN: override tác giả trong profile
- `--lang vi|en` — TÙY CHỌN: ngôn ngữ (mặc định: vi)

Nếu thiếu `--keyword` hoặc `--category`: hỏi user ngay.

## Detect Format (nếu không có `--format`)

- "top X", "X cách", "X lý do", "X bước", "danh sách", "listicle" → **LISTICLE**
- "hướng dẫn", "cách làm", "how-to", "từng bước", "tutorial", "step-by-step" → **HOW-TO**
- "vượt đối thủ", "skyscraper", "bài SEO dài", "top Google", "content authority" → **SKYSCRAPER**
- "pillar", "content hub", "topical authority", "nội dung tổng quan", "bài trụ" → **PILLAR**

Nếu vẫn không rõ, hỏi:
```
Bạn muốn viết theo cấu trúc nào?
1. LISTICLE — Bài "top X", danh sách có số thứ tự (CTR cao)
2. HOW-TO — Hướng dẫn từng bước (Featured Snippet, Schema HowTo)
3. SKYSCRAPER — Bài dài vượt top 10 đối thủ (phân tích competitor trước)
4. PILLAR — Bài trụ 3000-5000 từ + outline cluster articles
```

## Quy trình thực hiện

### Bước 1 — Thu thập thông tin

**Đọc profile:** `D:\Nunu-Claude\seo_content\profiles\default.json` → `brand_name`, `brand_tone`, `target_audience`, `author_name`, `author_title`.

**Tạo slug:** ASCII, gạch ngang, không dấu. VD: "7 cách tăng follow TikTok" → `tang-follow-tiktok`

**Tạo thư mục:** `D:\Nunu-Claude\seo_content\output\{category}\{slug}\`

**[Nếu SKYSCRAPER]:** WebSearch "{keyword} site:vn OR inurl:vn" → lấy top 5-10 URL → WebFetch 3 bài đối thủ → phân tích độ dài, H2, gaps.

**[Nếu HOW-TO/LISTICLE]:** WebSearch "{keyword}" → check People Also Ask → lấy 3-5 câu hỏi liên quan cho phần FAQ.

### Bước 2 — Viết theo framework

---

## FRAMEWORK 1: LISTICLE

**Đặc điểm:** H1 có con số rõ (ưu tiên số lẻ 7/9/11/15), mỗi item là H2, có checklist tổng kết.
**Độ dài mặc định:** 1500-2500 từ

**Cấu trúc bài:**

```
<!-- SEO Meta
Title: [Số] [Chủ đề] [Năm] ([Đối tượng/Điều kiện])
Meta Description: Khám phá [Số] [chủ đề] hiệu quả nhất [năm]...
Slug: {slug}
Keyword chính: {keyword}
Keyword phụ: [danh sách 3-5 từ khóa phụ]
Schema: Article
-->

# [Số] [Chủ đề] [Năm] ([Qualifier nếu có])

[Intro 100-150 từ theo APP framework: Agree → Promise → Preview]

## 1. [Item 1 — ấn tượng nhất, dễ áp dụng nhất]

[Mô tả 1-2 câu]

[Giải thích chi tiết 3-5 câu]

[Ví dụ thực tế]

💡 **Pro tip:** [Mẹo nâng cao]

<!-- [ẢNH] Infographic hoặc screenshot minh họa Item 1. File: [tên-file].png -->

## 2. [Item 2]
[...]

## [N]. [Item cuối — bất ngờ nhất, ít người biết]
[...]

## Tóm tắt nhanh

✅ [Item 1 — 1 câu]
✅ [Item 2 — 1 câu]
[...]

**Bước tiếp theo:** [CTA phù hợp]

## Câu hỏi thường gặp

**[Câu hỏi 1 từ PAA]?**
[Trả lời 40-60 từ, tự đứng được]

**[Câu hỏi 2]?**
[Trả lời]

<!-- TODO — Cần làm trước khi đăng
- [ ] Thêm ảnh thực tế cho từng item
- [ ] Internal link đến [bài liên quan]
- [ ] Update số liệu nếu cũ
-->

<!-- Author: {author_name}, {author_title}
Ngày tạo: {date} | Cập nhật: {date}
-->
```

---

## FRAMEWORK 2: HOW-TO

**Đặc điểm:** H1 bắt đầu "Cách..." hoặc "Hướng dẫn...", có metadata box, Bước 1/2/3, Schema HowTo.
**Độ dài mặc định:** 1500-2000 từ

**Cấu trúc bài:**

```
<!-- SEO Meta
Title: Cách [Làm gì] [Kết quả] (Hướng dẫn [Năm])
Meta Description: Hướng dẫn từng bước cách [làm gì]...
Slug: {slug}
Keyword chính: {keyword}
Schema: HowTo
-->

# Cách [Làm gì] [Kết quả] (Hướng dẫn từ A-Z [Năm])

[Intro 100-150 từ: kết quả đạt được, mất bao lâu, ai phù hợp]

> **⏱ Thời gian:** [X phút/giờ]
> **📊 Độ khó:** [Dễ / Trung bình / Khó]
> **🎯 Kết quả:** [Mô tả cụ thể kết quả]

## Bạn sẽ cần

- [Tool/vật liệu 1]
- [Tool/vật liệu 2]
- [Kỹ năng/kiến thức cần có]

## Bước 1: [Action Verb + Tên Bước]

**Mục đích:** [Tại sao cần bước này]

[Hướng dẫn chi tiết — 3-5 câu]

[Ví dụ cụ thể]

<!-- [ẢNH] Screenshot hoặc hình minh họa Bước 1. File: buoc-1-[slug].png -->

⚠️ **Lưu ý:** [Sai lầm phổ biến ở bước này và cách tránh]

## Bước 2: [...]
[...]

## Bước [N]: [Bước cuối]
[...]

## Sai lầm thường gặp

1. **[Sai lầm 1]** — [Hậu quả] → [Cách khắc phục]
2. **[Sai lầm 2]** — [...] → [...]

## Kết quả mong đợi

[Mô tả kết quả cuối cùng + hình ảnh]

## Tiếp theo nên làm gì?

[Gợi ý nâng cao hoặc bước tiếp theo trong hành trình]

## Câu hỏi thường gặp
[3-5 câu hỏi PAA]

<!-- TODO + Author block -->
```

---

## FRAMEWORK 3: SKYSCRAPER

**Đặc điểm:** Phân tích đối thủ trước → viết dài hơn 20%, đầy đủ hơn, mới hơn.
**Độ dài mặc định:** 3000-5000 từ

**Bước phân tích đối thủ (trước khi viết):**

1. WebSearch "{keyword}" → lấy top 10 kết quả
2. WebFetch 3 bài đối thủ mạnh nhất → ghi nhận:
   - Độ dài (số từ ước tính)
   - Các H2 chính
   - Nội dung họ thiếu (missing sections)
   - Năm xuất bản (data cũ?)
3. Xây outline bài "cao hơn": bao phủ tất cả H2 của đối thủ + ít nhất 5 phần họ thiếu

**Các phần thường bị đối thủ bỏ qua (ưu tiên thêm vào):**
- Case study thực tế (với số liệu)
- Bảng so sánh tools/phương pháp
- "Sai lầm thường gặp" section
- Template/Checklist tải được
- Video hướng dẫn (embed hoặc gợi ý tạo)
- FAQ từ People Also Ask thực tế
- Dữ liệu/nghiên cứu mới nhất 2025-2026

**Cấu trúc bài:**

```
<!-- SEO Meta
Title: [Keyword]: Hướng Dẫn Toàn Diện [Năm] (Cập nhật mới nhất)
Meta Description: Hướng dẫn đầy đủ nhất về [keyword]...
Schema: Article
-->

# [Keyword]: Hướng Dẫn Toàn Diện [Năm]

[Intro 150-200 từ: tại sao bài này tốt hơn, đọc xong biết được gì]

**Mục lục:** [Table of Contents với anchor links]

## [H2: Khái niệm / Định nghĩa cơ bản]
[Đầy đủ hơn đối thủ, có definition rõ ràng]

## [H2: Phần chính 1]
### [H3: Khía cạnh 1.1]
### [H3: Khía cạnh 1.2]

## [H2: Phần chính 2]
[...]

## Case Study Thực Tế ← đối thủ thường thiếu
[Case study cụ thể với số liệu]

## Sai Lầm Thường Gặp ← đối thủ thường thiếu
[...]

## Công Cụ & Tài Nguyên ← đối thủ thường thiếu
[Bảng so sánh tools]

## Câu Hỏi Thường Gặp
[8-10 câu hỏi từ PAA thực tế]

## Kết Luận
[Tóm tắt + CTA]

<!-- TODO + Author block -->
```

---

## FRAMEWORK 4: PILLAR-CLUSTER

**Đặc điểm:** Bài trụ tổng quan + outline cluster articles để liên kết nội bộ.
**Độ dài mặc định:** 3000-5000 từ

**Cấu trúc bài:**

```
<!-- SEO Meta
Title: [Chủ đề Lớn]: Hướng Dẫn Toàn Diện [Năm]
Schema: Article
-->

# [Chủ đề Lớn]: Hướng Dẫn Toàn Diện [Năm]

[Intro 200-300 từ: tại sao chủ đề quan trọng, bài này bao quát gì]

**Mục lục:** [Liên kết đến mỗi phần]

## Phần 1: [Khía cạnh lớn 1]

[Tóm tắt 300-400 từ về khía cạnh này]

**Những gì bạn cần biết về [khía cạnh 1]:**
- [Điểm 1]
- [Điểm 2]
- [Điểm 3]

👉 **Đọc chi tiết:** [Cluster Article 1: Tiêu đề đầy đủ]

## Phần 2: [Khía cạnh lớn 2]
[...]
👉 **Đọc chi tiết:** [Cluster Article 2]

[Tiếp tục 6-10 phần]

## FAQ Tổng Hợp
[5-8 câu hỏi]

## Kết Luận
[Tổng kết + liên kết tất cả cluster]

<!-- TODO + Author block -->

---

## Outline Cluster Articles (viết riêng)

### Cluster 1: [Tiêu đề]
- Slug đề xuất: {slug-cluster-1}
- Target keyword: [keyword dài]
- Tóm tắt nội dung: [2-3 câu]
- Internal link về Pillar: "[Anchor text]" → {pillar-slug}

[8-12 clusters với cùng format]
```

---

### Bước 3 — Áp dụng Quality Standards

**E-E-A-T:**
- `<!-- Author: {author_name}, {author_title} -->` ở cuối bài
- Trích dẫn nguồn uy tín: `<!-- [NGUỒN] tìm nghiên cứu về X -->`
- Gợi ý ảnh: `<!-- [ẢNH] mô tả ảnh -->`

**AI Search:**
- Đầu mỗi H2: 1 đoạn 40-80 từ trả lời trực tiếp (câu SPO, tự đứng được)
- FAQ block ≥5 câu cuối bài

**UX Writing:**
- Câu ≤20 từ, đoạn 3-4 câu
- Bold ý quan trọng, dùng "bạn"

### Bước 4 — Lưu file

Lưu tại: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\draft.md`

### Bước 5 — Thông báo hoàn thành

```
✅ Content SEO — Hoàn thành
Framework : {LISTICLE|HOW-TO|SKYSCRAPER|PILLAR}
Keyword   : {keyword}
File      : seo_content/output/{category}/{slug}/draft.md
Độ dài    : ~{N} từ

Bước tiếp theo (pipeline tương thích):
→ /seo-audit --file seo_content/output/{category}/{slug}/draft.md --keyword "{keyword}"
→ /seo-improve --draft seo_content/output/{category}/{slug}/draft.md --keyword "{keyword}"
```
