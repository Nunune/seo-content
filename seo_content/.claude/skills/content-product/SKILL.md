---
name: content-product
description: |
  Viết content giới thiệu sản phẩm/dịch vụ theo framework FAB (Feature-Advantage-Benefit)
  hoặc INVERTED PYRAMID (Lead → Body → Tail, chuẩn báo chí/PR).
  Kích hoạt khi user yêu cầu: "FAB", "feature advantage benefit", "giới thiệu sản phẩm",
  "mô tả sản phẩm", "product description", "tính năng lợi ích", "viết product page",
  "inverted pyramid", "bài PR", "thông cáo báo chí", "press release", "tin tức sản phẩm",
  "ra mắt sản phẩm", "khai trương", "bài báo chí", "bài PR sản phẩm".
  Cú pháp: --keyword "X" --category slug [--format FAB|PYRAMID] [--product "tên SP"] [--features "feat1 | feat2 | feat3"] [--event "sự kiện"] [--lang vi|en]
argument-hint: --keyword "X" --category slug [--format FAB|PYRAMID] [--product "tên SP"] [--features "feat1 | feat2 | feat3"] [--event "sự kiện"] [--lang vi|en]
allowed-tools: [Read, Write, WebSearch]
---

# Content Product — Viết Giới Thiệu Sản Phẩm theo FAB / INVERTED PYRAMID

Tạo content sản phẩm tập trung vào lợi ích thực tế (FAB) hoặc chuẩn báo chí/PR (INVERTED PYRAMID).

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: chủ đề/từ khóa
- `--category slug` — **BẮT BUỘC** (VD: gia-dung, suc-khoe, digital-marketing)
- `--format FAB|PYRAMID` — TÙY CHỌN: framework
- `--product "tên SP"` — TÙY CHỌN: tên sản phẩm/dịch vụ cụ thể
- `--features "feat1 | feat2 | feat3"` — TÙY CHỌN: danh sách tính năng (ngăn cách bởi |)
- `--event "sự kiện"` — TÙY CHỌN: sự kiện ra mắt/khai trương (dùng cho PYRAMID)
- `--lang vi|en` — TÙY CHỌN: ngôn ngữ (mặc định: vi)

Nếu thiếu `--keyword` hoặc `--category`: hỏi user ngay.

## Detect Format (nếu không có `--format`)

- "FAB", "feature advantage benefit", "giới thiệu sản phẩm", "mô tả sản phẩm", "product description", "tính năng lợi ích", "product page", "trang sản phẩm" → **FAB**
- "inverted pyramid", "bài PR", "thông cáo báo chí", "press release", "tin tức sản phẩm", "ra mắt", "khai trương", "bài báo chí" → **PYRAMID**

Nếu vẫn không rõ, hỏi:
```
Bạn muốn viết theo framework nào?
1. FAB — Mô tả sản phẩm: Feature → Advantage → Benefit (tập trung lợi ích cảm xúc)
2. INVERTED PYRAMID — Bài PR/báo chí: Lead quan trọng nhất → Body → Tail
```

## Quy trình thực hiện

### Bước 1 — Thu thập thông tin

**Đọc profile:** `D:\Nunu-Claude\seo_content\profiles\default.json` → `brand_name`, `brand_tone`, `target_audience`, `author_name`, `author_title`.

**Tạo slug:** ASCII, gạch ngang, không dấu. VD: "máy lọc không khí Xiaomi" → `may-loc-khong-khi-xiaomi`

**Tạo thư mục:** `D:\Nunu-Claude\seo_content\output\{category}\{slug}\`

**Nếu có `--features`:** Parse danh sách features (ngăn cách bởi `|`) → dùng làm danh sách FAB items.

**Nếu không có `--features`:** Dựa vào keyword và brand → tự suy luận 3-5 tính năng tiêu biểu của loại sản phẩm này.

---

## FRAMEWORK 1: FAB

**Đặc điểm:** Mỗi tính năng được trình bày theo 3 lớp: Feature (kỹ thuật) → Advantage (so sánh thị trường) → Benefit (cảm xúc/cuộc sống). Áp dụng "So what?" test để đào sâu đến lợi ích thật.
**Độ dài mặc định:** 500-1000 từ tùy số lượng tính năng

### F — Feature (Tính năng)

Mô tả kỹ thuật khách quan, chính xác:
- Thông số cụ thể, có thể đo được
- Ngôn ngữ trung lập, không marketing
- VD: "Pin 5000mAh", "Lọc HEPA 3 lớp", "Công nghệ AI nhận diện da"

### A — Advantage (Ưu điểm)

So sánh với chuẩn thị trường hoặc giải pháp cũ:
- "Tốt hơn X% so với trung bình thị trường"
- "Nhanh hơn X lần so với phương pháp truyền thống"
- "Duy nhất trên thị trường có..."
- Dùng so sánh CỤ THỂ, không nói chung chung "tốt hơn"

### B — Benefit (Lợi ích)

**Đây là phần quan trọng nhất** — chạm đến cảm xúc và cuộc sống thật.

Dùng "So what?" test liên tục cho đến khi chạm cảm xúc thật:
- Feature: "Pin 5000mAh"
- So what? → Advantage: "Dùng được 2 ngày không cần sạc"
- So what? → Benefit 1: "Không lo hết pin giữa chừng khi đang làm việc quan trọng"
- So what? → Benefit 2: "Tự tin đi cả ngày dài không cần mang theo sạc"

Benefit phải đặt trong ngữ cảnh cuộc sống:
- Thời điểm họ cần điều này nhất là khi nào?
- Cảm giác gì khi có/không có tính năng này?
- Tác động đến người thân/đồng nghiệp thế nào?

**Cấu trúc bài FAB:**

```
<!-- Product Content
Framework: FAB
Keyword: {keyword}
Product: {product}
Created: {date}
-->

# [Tên Sản Phẩm]: [Lợi Ích Chính] Bạn Chưa Tìm Được Ở Đâu Khác

[Intro 60-80 từ: mô tả vấn đề người dùng đang gặp → sản phẩm là giải pháp → kết quả đạt được]

## [Tính năng 1 — ấn tượng nhất]

**Feature:** [Mô tả kỹ thuật cụ thể]

**Advantage:** [So với thị trường: tốt hơn thế nào, bao nhiêu phần trăm]

**Benefit:** [Điều này nghĩa là bạn có thể... / Bạn sẽ không bao giờ phải lo lắng về...]

<!-- [ẢNH] Hình minh họa tính năng 1. File: fab-feature-1-{slug}.jpg -->

---

## [Tính năng 2]

**Feature:** [...]
**Advantage:** [...]
**Benefit:** [...]

---

## [Tính năng 3]

**Feature:** [...]
**Advantage:** [...]
**Benefit:** [...]

---

[Tiếp tục đến tính năng cuối]

---

## Bạn không chỉ mua [tên sản phẩm]

Bạn mua [giá trị cảm xúc tổng hợp — 2-3 câu kết nối tất cả benefits].

[Mô tả cuộc sống của họ sau khi có sản phẩm — 3-4 câu]

**[CTA chính]** | [Giảm rào cản: bảo hành, đổi trả, tư vấn miễn phí]

## Thông số kỹ thuật đầy đủ

| Thông số | Chi tiết |
|----------|---------|
| [Thông số 1] | [Giá trị] |
| [Thông số 2] | [Giá trị] |
| [Thông số 3] | [Giá trị] |

## Câu hỏi thường gặp

**[Câu hỏi 1 về sản phẩm]?**
[Trả lời 40-60 từ]

**[Câu hỏi 2]?**
[Trả lời]

<!-- TODO — Cần làm trước khi đăng
- [ ] Verify thông số kỹ thuật với manufacturer specs
- [ ] Thêm ảnh thực tế sản phẩm
- [ ] Thêm testimonials từ khách hàng đã dùng
-->

<!-- Author: {author_name}, {author_title}
Ngày tạo: {date}
-->
```

---

## FRAMEWORK 2: INVERTED PYRAMID

**Đặc điểm:** Chuẩn báo chí — thông tin quan trọng nhất ở đầu, chi tiết bổ sung theo thứ tự giảm dần. Người đọc hiểu toàn bộ câu chuyện chỉ sau đoạn đầu tiên. Dùng cho press release, tin tức sản phẩm, bài PR, thông báo khai trương.
**Độ dài mặc định:** 400-800 từ

### Lead (Đỉnh kim tự tháp — 50-100 từ)

**Đây là phần quan trọng nhất.** Sau khi đọc Lead, người đọc biết TOÀN BỘ câu chuyện.

Trả lời đầy đủ 5W + 1H trong 1-2 câu đầu tiên:
- **Who**: Ai? (thương hiệu, nhân vật, tổ chức)
- **What**: Gì? (sự kiện, sản phẩm, thành tích)
- **When**: Khi nào? (ngày/tháng/năm cụ thể)
- **Where**: Ở đâu? (địa điểm, kênh, thị trường)
- **Why**: Tại sao quan trọng? (tác động, ý nghĩa)
- **How**: Bằng cách nào? (phương thức, cơ chế)

**Kỹ thuật Lead hiệu quả:**
- Lead tóm tắt: "Công ty X vừa ra mắt Y tại Z ngày A, giúp người dùng B bằng cách C."
- Lead câu hỏi (dùng khi câu chuyện phức tạp): "Điều gì xảy ra khi [vấn đề]? [Thương hiệu] vừa tìm ra câu trả lời."
- Lead narrative (dùng khi có yếu tố con người): "Khi [nhân vật] gặp [vấn đề], ít ai ngờ giải pháp lại đến từ..."

### Body (Phần thân — chi tiết bổ sung theo thứ tự quan trọng giảm dần)

Thứ tự ưu tiên thông tin trong Body:
1. **Quote từ người phát ngôn/CEO/chuyên gia** — tạo credibility ngay
2. **Chi tiết sản phẩm/sự kiện** — specs, tính năng, thời gian, địa điểm
3. **Dữ liệu và con số** — nghiên cứu, thống kê hỗ trợ
4. **Quote từ khách hàng/đối tác** — social proof
5. **Thông tin bổ sung** — pricing, availability, điều kiện

Mỗi đoạn = 1 ý rõ ràng, câu đầu = câu quan trọng nhất của đoạn đó.

### Tail (Đuôi — thông tin nền, có thể bỏ qua)

- Background về công ty/tổ chức (boilerplate)
- Lịch sử, context dài hạn
- Thông tin liên hệ, website
- Thông tin hỗ trợ, chú thích

**Cấu trúc bài INVERTED PYRAMID:**

```
<!-- Product Content
Framework: INVERTED PYRAMID
Keyword: {keyword}
Product: {product}
Event: {event}
Created: {date}
-->

# [Tiêu đề báo chí: Ai + Làm gì + Kết quả/Tác động]

**[Ngày, Địa điểm]** — [LEAD: 50-100 từ, trả lời đầy đủ 5W+1H. Đây là toàn bộ câu chuyện trong 1-2 câu.]

<!-- [ẢNH] Ảnh sản phẩm hoặc sự kiện chính. File: pyramid-hero-{slug}.jpg -->

## Chi tiết sự kiện / sản phẩm

> "[Quote từ CEO/người phát ngôn — phản hồi về sản phẩm/sự kiện, vision, tầm quan trọng]"
> — [Tên], [Chức danh], [Tên Công ty]

[Paragraph 1: Chi tiết quan trọng nhất về sản phẩm/sự kiện — 2-3 câu]

[Paragraph 2: Tính năng nổi bật, điểm khác biệt — 2-3 câu]

[Paragraph 3: Dữ liệu/nghiên cứu hỗ trợ — con số cụ thể]

## Phản hồi từ thị trường / khách hàng

> "[Quote từ khách hàng hoặc đối tác — phản ứng thực tế]"
> — [Tên], [Vị trí]

[Thông tin về tình trạng nhận hàng, giá, kênh phân phối]

## Thông tin chi tiết

| | |
|--|--|
| **Ngày ra mắt** | [Ngày cụ thể] |
| **Giá** | [Giá/Liên hệ báo giá] |
| **Có mặt tại** | [Kênh bán hàng] |
| **Bảo hành** | [Chính sách] |

## Về [Tên Công ty]

[Boilerplate 50-80 từ: năm thành lập, lĩnh vực, thành tích chính, số liệu key]

**Liên hệ truyền thông:**
- Email: [email PR]
- Điện thoại: [số điện thoại]
- Website: [URL]

<!-- TODO — Cần làm trước khi đăng
- [ ] Confirm quotes với người phát ngôn
- [ ] Verify tất cả ngày tháng và con số
- [ ] Thêm ảnh sản phẩm/sự kiện độ phân giải cao
- [ ] Gửi embargo date nếu cần
-->

<!-- Author: {author_name}, {author_title}
Ngày tạo: {date}
-->
```

---

### Bước 2 — Áp dụng Quality Standards

**UX Writing (FAB):**
- Câu ≤20 từ, đoạn 3-4 câu
- Bold tên tính năng, con số, CTA
- Dùng "bạn", active voice
- Kết hợp cảm xúc + lý trí: logic justify, emotion mua

**Báo chí (INVERTED PYRAMID):**
- Khách quan, không marketing language trong Lead và Body
- Chỉ dùng quote để express opinion
- Số liệu phải có nguồn
- Tránh superlative không có chứng minh ("tốt nhất", "số 1")

### Bước 3 — Lưu file

Lưu tại: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\product-{slug}.md`

### Bước 4 — Thông báo hoàn thành

```
✅ Content Product — Hoàn thành
Framework : {FAB|INVERTED PYRAMID}
Keyword   : {keyword}
Product   : {product}
File      : seo_content/output/{category}/{slug}/product-{slug}.md
Độ dài    : ~{N} từ

Gợi ý bước tiếp:
→ /content-headline --keyword "{keyword}"  (tối ưu tiêu đề)
→ /content-sales --keyword "{keyword}" --category {category}  (thêm bản copy bán hàng)
```
