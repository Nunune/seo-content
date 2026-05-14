---
name: content-story
description: |
  Viết content kể chuyện theo framework STAR (case study) hoặc HERO'S JOURNEY (StoryBrand 7 bước).
  Kích hoạt khi user yêu cầu: "kể chuyện", "case study", "câu chuyện thương hiệu",
  "STAR", "HERO", "hero's journey", "storybrand", "brand story", "câu chuyện khách hàng",
  "chuyện thành công", "success story", "situation task action result",
  "câu chuyện thương hiệu", "viết brand story", "storytelling".
  Cú pháp: --keyword "X" --category slug [--format STAR|HERO] [--subject "nhân vật/thương hiệu"] [--outcome "kết quả"] [--timeframe "thời gian"] [--lang vi|en]
argument-hint: --keyword "X" --category slug [--format STAR|HERO] [--subject "nhân vật/thương hiệu"] [--outcome "kết quả"] [--timeframe "thời gian"] [--lang vi|en]
allowed-tools: [Read, Write, WebSearch]
---

# Content Story — Viết Content Kể Chuyện theo STAR / HERO'S JOURNEY

Tạo content storytelling tạo kết nối cảm xúc, xây dựng trust và thúc đẩy quyết định.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: chủ đề/từ khóa
- `--category slug` — **BẮT BUỘC** (VD: digital-marketing, suc-khoe, bat-dong-san)
- `--format STAR|HERO` — TÙY CHỌN: framework
- `--subject "nhân vật/thương hiệu"` — TÙY CHỌN: ai là nhân vật chính
- `--outcome "kết quả cụ thể"` — TÙY CHỌN: kết quả đạt được
- `--timeframe "thời gian"` — TÙY CHỌN: thời gian chuyển đổi (VD: "3 tháng", "6 tuần")
- `--lang vi|en` — TÙY CHỌN: ngôn ngữ (mặc định: vi)

Nếu thiếu `--keyword` hoặc `--category`: hỏi user ngay.

## Detect Format (nếu không có `--format`)

- "STAR", "case study", "câu chuyện khách hàng", "success story", "situation task action result", "chuyện thành công" → **STAR**
- "HERO", "hero's journey", "storybrand", "brand story", "câu chuyện thương hiệu", "viết brand story", "storytelling thương hiệu" → **HERO**

Nếu vẫn không rõ, hỏi:
```
Bạn muốn viết theo framework nào?
1. STAR — Case study khách hàng (Situation → Task → Action → Result)
2. HERO'S JOURNEY — Brand story theo StoryBrand 7 bước (khách hàng là hero)
```

## Quy trình thực hiện

### Bước 1 — Thu thập thông tin

**Đọc profile:** `D:\Nunu-Claude\seo_content\profiles\default.json` → `brand_name`, `brand_tone`, `target_audience`, `author_name`, `author_title`.

**Tạo slug:** ASCII, gạch ngang, không dấu. VD: "câu chuyện khách hàng giảm 10kg" → `cau-chuyen-khach-hang-giam-10kg`

**Tạo thư mục:** `D:\Nunu-Claude\seo_content\output\{category}\{slug}\`

---

## FRAMEWORK 1: STAR

**Đặc điểm:** Case study cấu trúc rõ ràng, có số liệu trước/sau, quote thực tế. Dùng cho testimonial, case study trang, email nurturing.
**Phân bổ:** S (20%) → T (20%) → A (40%) → R (20%)
**Độ dài mặc định:** 600-1000 từ

### S — Situation (Bối cảnh)

Mô tả đầy đủ bối cảnh ban đầu của nhân vật:
- Tên/tuổi/nghề/địa điểm cụ thể (nếu là khách hàng thật: xin phép trước)
- Background đủ để người đọc đồng cảm
- Tình trạng trước khi gặp vấn đề (cuộc sống bình thường)
- Điểm mà vấn đề bắt đầu xuất hiện

**Nguyên tắc:** Người đọc phải tự nhận ra "đây cũng có thể là tôi".

### T — Task (Nhiệm vụ/Thách thức)

Xác định rõ vấn đề CỤ THỂ + mục tiêu đo được:
- Vấn đề cụ thể là gì? (không nói chung chung)
- Mục tiêu muốn đạt: con số, timeline
- Các ràng buộc/khó khăn: thời gian, ngân sách, điều kiện
- Đã thử các cách khác chưa? Kết quả ra sao?

**Nguyên tắc:** Task càng cụ thể → Result càng đáng tin.

### A — Action (Hành động)

Từng bước giải quyết vấn đề — đây là phần dài nhất:
- Bước 1: [Hành động đầu tiên + lý do chọn cách này]
- Bước 2: [Hành động tiếp theo]
- Bước 3: [...]
- Vai trò cụ thể của sản phẩm/dịch vụ/phương pháp trong từng bước
- Khó khăn gặp phải trong quá trình và cách vượt qua
- Điều bất ngờ/unexpected đã xảy ra

**Nguyên tắc:** Action phải đủ chi tiết để người đọc hiểu QUÁ TRÌNH, không chỉ kết quả.

### R — Result (Kết quả)

Kết quả đo được + tác động cảm xúc:
- Số liệu CỤ THỂ trước/sau: "từ X → Y trong Z thời gian"
- Kết quả phụ không ngờ tới (bonus result)
- Quote trực tiếp từ nhân vật (cảm xúc, suy nghĩ)
- Tác động đến cuộc sống/công việc dài hạn

**Cấu trúc bài STAR:**

```
<!-- Story Content
Framework: STAR
Keyword: {keyword}
Subject: {subject}
Outcome: {outcome}
Created: {date}
-->

# [Tiêu đề: Tên/Đối tượng] Đã [Kết quả Cụ thể] Trong [Thời gian] — Câu Chuyện Thật

[Intro 50-80 từ: hook — kết quả nổi bật nhất, ai đạt được, bằng cách nào]

## Bối cảnh: [Tên] Trước Khi Thay Đổi

[S — Situation: 150-200 từ, tình trạng ban đầu, chi tiết về nhân vật]

## Thách thức: Điều Gì Đang Cản Trở?

[T — Task: 150-200 từ, vấn đề cụ thể, mục tiêu, những gì đã thử]

## Hành Trình: Từng Bước Thay Đổi

[A — Action: 250-350 từ, các bước cụ thể, vai trò của giải pháp]

<!-- [ẢNH] Hình minh họa quá trình/before-after. File: star-action-{slug}.jpg -->

## Kết Quả: Con Số Nói Lên Tất Cả

[R — Result: 150-200 từ]

**Trước:** [mô tả tình trạng cũ với số liệu]
**Sau [thời gian]:** [mô tả tình trạng mới với số liệu]

> "[Quote trực tiếp từ nhân vật — cảm xúc thật, ngôn ngữ tự nhiên]"
> — [Tên], [Vị trí/Nghề nghiệp]

### Kết Quả Bất Ngờ Thêm

[Những điều không ngờ tới đã xảy ra]

## Bài Học Rút Ra

[2-3 insight người đọc có thể áp dụng]

**Bước tiếp theo:** [CTA phù hợp — tham khảo, liên hệ, thử nghiệm]

<!-- TODO — Cần làm trước khi đăng
- [ ] Xin phép nhân vật sử dụng câu chuyện và ảnh
- [ ] Thêm ảnh before/after thực tế
- [ ] Verify lại tất cả số liệu
-->

<!-- Author: {author_name}, {author_title}
Ngày tạo: {date}
-->
```

---

## FRAMEWORK 2: HERO'S JOURNEY (StoryBrand 7 Bước)

**Đặc điểm:** Khách hàng là Hero (không phải thương hiệu). Thương hiệu là Guide (người dẫn đường). Dùng cho about page, brand story, landing page dài, email sequence.
**Phân bổ:** Hero+Problem (30%) → Guide+Plan (20%) → CTA+Failure+Success (50%)
**Độ dài mặc định:** 800-1500 từ

### Bước 1 — Hero (Nhân vật chính = Khách hàng)

**Nguyên tắc vàng: KHÁCH HÀNG là hero, không phải thương hiệu.**

Mô tả hero:
- Họ là ai (đặc điểm, cuộc sống, mong muốn)
- Điều họ khao khát nhất là gì? (external goal)
- Cuộc sống bình thường của họ trước khi có vấn đề

### Bước 2 — Problem (3 tầng vấn đề)

Ba tầng vấn đề cần xác định:
- **External Problem** (bề mặt): Vấn đề hữu hình, có thể thấy được — "doanh số thấp", "da nổi mụn", "lương không tăng"
- **Internal Problem** (cảm xúc): Cảm giác bên trong — "tôi cảm thấy thất bại", "tôi lo lắng mỗi sáng thức dậy", "tôi xấu hổ khi nhìn gương"
- **Philosophical Problem** (niềm tin): Câu hỏi về lẽ phải — "một người chăm chỉ xứng đáng được thành công hơn thế này", "cuộc sống không nên khổ sở như vậy"
- **Villain** (kẻ thù trừu tượng): Không phải người — là thứ gây ra vấn đề (hệ thống lạc hậu, thông tin sai lệch, thói quen xấu, thị trường bất công)

**Nguyên tắc:** Internal problem tạo kết nối sâu nhất. Villain giúp khách hàng không cảm thấy bị đổ lỗi.

### Bước 3 — Guide (Thương hiệu = Người dẫn đường)

Thương hiệu xuất hiện với 2 phẩm chất:
- **Empathy** ("Chúng tôi hiểu bạn"): "Chúng tôi biết cảm giác đó... Chúng tôi đã gặp hàng nghìn người như bạn..."
- **Authority** (Chứng minh năng lực): Số liệu, giải thưởng, năm kinh nghiệm, số khách hàng đã giúp, case study ngắn

**Nguyên tắc:** Guide KHÔNG nói về mình nhiều — chỉ đủ để khách tin tưởng rằng guide có thể giúp.

### Bước 4 — Plan (Kế hoạch 3 bước)

Đơn giản hóa hành trình thành 3 bước rõ ràng:
- **Bước 1:** [Hành động đầu tiên] — giảm lo lắng khi bắt đầu
- **Bước 2:** [Hành động tiếp theo]
- **Bước 3:** [Hành động cuối → dẫn đến kết quả]

**Nguyên tắc:** 3 bước (không nhiều hơn) — nhiều bước hơn tạo ra sự do dự.

### Bước 5 — CTA (Kêu gọi hành động kép)

Hai loại CTA:
- **Direct CTA**: Hành động rõ ràng, ngay lập tức — "Đặt lịch tư vấn miễn phí", "Mua ngay", "Đăng ký hôm nay"
- **Transitional CTA**: Hành động ít rủi ro hơn — "Tải ebook miễn phí", "Xem video hướng dẫn", "Đọc case study"

### Bước 6 — Avoid Failure (Hậu quả nếu không hành động)

Mô tả ngắn gọn điều xảy ra nếu hero KHÔNG có guide:
- Hậu quả thực tế + cảm xúc
- **Không bi kịch hóa** quá mức — chỉ đủ để tạo urgency
- Kết bằng cơ hội: "Nhưng điều đó không cần phải xảy ra..."

### Bước 7 — Success (Tương lai tươi sáng)

Vẽ ra viễn cảnh khi hero thành công nhờ guide:
- Cuộc sống thay đổi thế nào? (cụ thể, có thể hình dung)
- Cảm xúc họ sẽ có
- Điều gì trở nên khác biệt mỗi ngày
- Identity mới: "Bạn trở thành người..."

**Cấu trúc bài HERO'S JOURNEY:**

```
<!-- Story Content
Framework: HERO'S JOURNEY (StoryBrand)
Keyword: {keyword}
Brand: {brand_name}
Created: {date}
-->

# [Tên Thương Hiệu/Dịch vụ]: Câu Chuyện Của [Đối Tượng Khách Hàng]

[Intro 80-100 từ: kết nối ngay với hero — mô tả họ, điều họ muốn, vấn đề họ đang gặp]

## [Hero] Bạn đang ở đâu trong hành trình này?

[Bước 1 — Hero: 100-150 từ, mô tả khách hàng mục tiêu như người thật]

## Vấn đề không chỉ là những gì bạn thấy

[Bước 2 — Problem: 150-200 từ]

**Vấn đề bạn thấy:** [External — cụ thể]

**Vấn đề bạn cảm thấy:** [Internal — cảm xúc]

**Điều bạn tin:** [Philosophical — niềm tin]

Và kẻ thù thật sự không phải là bạn — đó là [Villain].

## Chúng tôi hiểu — và chúng tôi có thể giúp

[Bước 3 — Guide: 100-150 từ]

[Empathy: 2-3 câu đồng cảm]

[Authority: 2-3 câu credentials/số liệu]

<!-- [ẢNH] Ảnh team hoặc logo thương hiệu. File: guide-{slug}.jpg -->

## 3 Bước Để Thay Đổi

[Bước 4 — Plan]

**Bước 1:** [Action + giải thích ngắn]
**Bước 2:** [Action + giải thích ngắn]
**Bước 3:** [Action + kết quả]

## Bắt đầu hành trình của bạn hôm nay

[Bước 5 — CTA]

👉 **[Direct CTA — hành động chính]**

Chưa sẵn sàng? → **[Transitional CTA — bước nhỏ hơn]**

## Điều gì xảy ra nếu không có gì thay đổi?

[Bước 6 — Avoid Failure: 80-120 từ, không bi kịch hóa]

Nhưng điều đó không cần phải xảy ra.

## Cuộc sống của bạn có thể trông như thế này

[Bước 7 — Success: 150-200 từ, viễn cảnh cụ thể, có thể hình dung]

Hãy tưởng tượng [thời gian] sau — [mô tả cụ thể cuộc sống mới].

**Bạn sẽ:** [kết quả 1]
**Bạn sẽ cảm thấy:** [cảm xúc]
**Bạn sẽ trở thành:** [identity mới]

[Repeat Direct CTA]

<!-- TODO — Cần làm trước khi đăng
- [ ] Thêm testimonials thật từ khách hàng
- [ ] Thêm số liệu cụ thể vào Authority section
- [ ] Review tone: thương hiệu không nên nói về mình quá nhiều
-->

<!-- Author: {author_name}, {author_title}
Ngày tạo: {date}
-->
```

---

### Bước 2 — Áp dụng Quality Standards

**UX Writing:**
- Câu ≤20 từ, đoạn 3-4 câu
- Dùng "bạn", active voice
- Bold tên nhân vật, số liệu, quote

**Storytelling Rules:**
- Conflict rõ ràng: không có conflict → không có story
- Specific beats generic: "giảm 8kg trong 10 tuần" > "giảm cân thành công"
- Emotion trước, logic sau
- Quote dùng ngôn ngữ tự nhiên, không "đánh bóng"

### Bước 3 — Lưu file

Lưu tại: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\story-{slug}.md`

### Bước 4 — Thông báo hoàn thành

```
✅ Content Story — Hoàn thành
Framework : {STAR|HERO'S JOURNEY}
Keyword   : {keyword}
Subject   : {subject}
File      : seo_content/output/{category}/{slug}/story-{slug}.md
Độ dài    : ~{N} từ

Gợi ý bước tiếp:
→ /content-headline --keyword "{keyword}"  (tối ưu tiêu đề)
→ /content-intro --keyword "{keyword}"  (viết mở bài hấp dẫn hơn)
```
