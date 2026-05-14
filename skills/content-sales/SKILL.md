---
name: content-sales
description: |
  Viết content bán hàng/chuyển đổi theo framework AIDA, PAS, BAB hoặc PASTOR.
  Kích hoạt khi user yêu cầu: "bài bán hàng", "caption quảng cáo", "landing page",
  "AIDA", "PAS", "BAB", "PASTOR", "sales page", "bài đánh pain point",
  "khoét nỗi đau", "bài chuyển đổi", "viết content bán", "content chuyển đổi",
  "email marketing", "email bán hàng", "copy quảng cáo", "ad copy".
  Cú pháp: --keyword "X" --category slug [--format AIDA|PAS|BAB|PASTOR] [--product "tên SP"] [--audience "đối tượng"] [--tone "giọng văn"] [--length short|medium|long] [--lang vi|en]
argument-hint: --keyword "X" --category slug [--format AIDA|PAS|BAB|PASTOR] [--product "tên SP"] [--audience "đối tượng"] [--tone "giọng văn"] [--length short|medium|long] [--lang vi|en]
allowed-tools: [Read, Write, WebSearch]
---

# Content Sales — Viết Content Bán Hàng theo AIDA / PAS / BAB / PASTOR

Tạo content chuyển đổi theo framework phù hợp với mục tiêu và loại sản phẩm/dịch vụ.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: từ khóa/chủ đề
- `--category slug` — **BẮT BUỘC**: danh mục (VD: digital-marketing, suc-khoe, bat-dong-san)
- `--format AIDA|PAS|BAB|PASTOR` — TÙY CHỌN: framework muốn dùng
- `--product "tên SP"` — TÙY CHỌN: tên sản phẩm/dịch vụ cụ thể
- `--audience "đối tượng"` — TÙY CHỌN: đối tượng mục tiêu cụ thể
- `--tone "giọng văn"` — TÙY CHỌN: ví dụ "thân thiện", "khẩn cấp", "chuyên nghiệp"
- `--length short|medium|long` — TÙY CHỌN: độ dài (short ~200 từ, medium ~500 từ, long ~1000 từ)
- `--lang vi|en` — TÙY CHỌN: ngôn ngữ (mặc định: vi)

Nếu thiếu `--keyword` hoặc `--category`: hỏi user ngay.

## Detect Format (nếu không có `--format`)

Phân tích trigger keywords trong message của user:
- "landing page", "AIDA", "caption quảng cáo", "ad copy", "email marketing", "thu hút" → **AIDA**
- "pain point", "khoét nỗi đau", "y tế", "bất động sản", "bảo hiểm", "PAS", "cảnh báo" → **PAS**
- "transformation", "before after", "BAB", "email nurturing", "trước sau", "chuyển đổi" → **BAB**
- "sales page", "khóa học", "PASTOR", "bán hàng dài", "offer", "testimonial" → **PASTOR**

Nếu vẫn không rõ, hỏi:
```
Bạn muốn viết theo framework nào?
1. AIDA — Caption quảng cáo, landing page, email marketing
2. PAS — Khoét pain point (y tế, BĐS, bảo hiểm, tư vấn)
3. BAB — Transformation story, email nurturing
4. PASTOR — Sales page dài, bán khóa học/dịch vụ cao cấp
```

## Quy trình thực hiện

### Bước 1 — Thu thập thông tin

Đọc `D:\Nunu-Claude\seo_content\profiles\default.json` → lấy: `brand_name`, `brand_tone`, `target_audience`, `brand_website`.

Tạo slug từ keyword: ASCII, gạch ngang, không dấu.
- Ví dụ: "dịch vụ khám phụ khoa" → `dich-vu-kham-phu-khoa`

Tạo thư mục output: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\`

### Bước 2 — Viết content theo framework đã chọn

---

## FRAMEWORK 1: AIDA

**Phân bổ:** A (10-15%) → I (25-30%) → D (35-40%) → A (10-15%)

**A — Attention (Thu hút)**
- Hook 1-2 câu phải dừng người đọc trong 3 giây
- Kỹ thuật: số liệu gây sốc | câu hỏi tu từ | tuyên bố ngược đời | tình huống quen thuộc
- Ví dụ tốt: "90% người Việt không biết dấu hiệu này..." / "Mỗi 2 phút, có 1 người..."

**I — Interest (Tạo hứng thú)**
- Nói về VẤN ĐỀ của họ, CHƯA đề cập sản phẩm
- Cung cấp insight mới, câu chuyện có thật, số liệu từ nghiên cứu
- Nguyên tắc: khiến họ muốn đọc tiếp để tìm giải pháp

**D — Desire (Khao khát)**
- Chuyển từ "vấn đề" sang "giải pháp = sản phẩm"
- Mô tả kết quả CỤ THỂ họ sẽ nhận được (số liệu, timeline)
- Kỹ thuật Before-After-Bridge
- Social proof: review, case study, con số người đã dùng

**A — Action (Hành động)**
- 1 CTA duy nhất, rõ ràng, động từ mạnh
- Urgency: "chỉ còn X suất hôm nay", "ưu đãi đến [date]"
- Giảm rào cản: "miễn phí tư vấn", "không cần đặt cọc", "hoàn tiền 100%"

**Template AIDA:**
```
[HOOK — 1-2 câu gây chú ý]

[Mô tả vấn đề người đọc đang gặp — 2-3 đoạn]
[Insight/câu chuyện thật/số liệu]

[Giới thiệu giải pháp]
[Lợi ích 1 + bằng chứng]
[Lợi ích 2 + bằng chứng]
[Lợi ích 3 + bằng chứng]
[Social proof: số lượng + testimonial]

[CTA cụ thể] + [Urgency] + [Giảm rào cản]
```

---

## FRAMEWORK 2: PAS

**Phân bổ:** P (20%) → A (40-50%) → S (30-40%)

**P — Problem (Vấn đề)**
- Nêu CHÍNH XÁC vấn đề, dùng ngôn ngữ của khách hàng
- Khiến họ gật đầu "đúng rồi, đó là tôi"
- Câu mở thường là câu hỏi: "Bạn có đang...?"

**A — Agitate (Khoét sâu)** ← PHẦN QUAN TRỌNG NHẤT
- Hậu quả ngắn hạn → trung hạn → dài hạn
- Tác động: sức khỏe | tài chính | mối quan hệ | sự nghiệp | tinh thần
- Kể câu chuyện thực tế về người đã chịu hậu quả vì không giải quyết
- Câu chốt: "Đừng để điều này xảy ra với bạn"
- Chú ý: khoét đủ sâu để tạo urgency, KHÔNG cường điệu gây phản cảm

**S — Solution (Giải pháp)**
- Giải pháp xuất hiện như "vị cứu tinh" sau phần Agitate
- Giải thích cơ chế: tại sao nó giải quyết được vấn đề
- Bằng chứng: số liệu, case study, chứng nhận
- CTA cuối bài

**Template PAS:**
```
[Câu hỏi xác định vấn đề: "Bạn có đang...?"]
[Mô tả vấn đề chi tiết]

[Hậu quả 1: ngắn hạn — cảm giác tức thì]
[Hậu quả 2: trung hạn — ảnh hưởng cuộc sống]
[Hậu quả 3: dài hạn — thiệt hại lớn]
[Câu chuyện thực tế về người chịu hậu quả]
[Câu chốt: "Đừng để điều này xảy ra với bạn"]

[Giới thiệu giải pháp]
[Cơ chế hoạt động — tại sao nó hiệu quả]
[Bằng chứng/Social proof]
[CTA]
```

---

## FRAMEWORK 3: BAB

**Phân bổ:** B-Before (30%) → A-After (40%) → B-Bridge (30%)

**B — Before (Trạng thái hiện tại)**
- Mô tả CHI TIẾT tình trạng khách hàng đang gặp
- Dùng giác quan: họ THẤY gì, NGHE gì, CẢM gì
- Khiến họ tự nhận ra "đây chính xác là tôi"
- Liệt kê 3-5 vấn đề/bất tiện cụ thể

**A — After (Viễn cảnh mơ ước)**
- Vẽ ra tương lai SAU KHI đã giải quyết vấn đề
- Càng cụ thể càng tốt: con số, timeline, hình ảnh, cảm xúc
- Future pacing: "Hãy tưởng tượng [thời gian] sau..."
- Dùng "bạn sẽ...", "bạn sẽ cảm thấy...", "mỗi sáng bạn thức dậy..."

**B — Bridge (Cây cầu)**
- Giới thiệu sản phẩm/dịch vụ là "chiếc cầu" từ Before → After
- Giải thích cơ chế: tại sao nó hoạt động
- Bằng chứng: số người đã đi qua "cây cầu" này thành công
- CTA rõ ràng

**Template BAB:**
```
[Before]
Bạn có đang...? [Mô tả tình trạng hiện tại với giác quan]
[Vấn đề 1] / [Vấn đề 2] / [Vấn đề 3]

[After]
Hãy tưởng tượng [thời gian] sau...
[Viễn cảnh chi tiết — con số, hình ảnh, cảm xúc]
[Cuộc sống thay đổi thế nào — cụ thể từng khía cạnh]

[Bridge]
[Giải pháp] chính là cây cầu đưa bạn từ A đến B.
[Cơ chế hoạt động]
[Con số người đã thành công]
[CTA]
```

---

## FRAMEWORK 4: PASTOR

**Phân bổ:** P-A-S (40%) → T (20%) → O (25%) → R (15%)

**P — Problem**: Nêu vấn đề (như PAS-P)
**A — Amplify**: Khuếch đại hậu quả (như PAS-A)
**S — Story & Solution**: Kể câu chuyện cá nhân hoặc khách hàng ĐÃ vượt qua vấn đề → giới thiệu giải pháp

**T — Testimonial**:
- 2-3 testimonials thật từ khách hàng đã dùng
- Format: "[Quote]" — [Tên, Vị trí, Địa điểm]
- Thêm số liệu tổng: "[X] người đã tin tưởng / đạt [kết quả Y]"

**O — Offer (Đề nghị chi tiết)**:
- Tên sản phẩm/gói dịch vụ
- Liệt kê ĐẦY ĐỦ những gì bao gồm (dùng ✓)
- Bonus/tặng kèm (nếu có)
- Bảo đảm/guarantee (hoàn tiền, cam kết kết quả)
- Giá gốc → giá ưu đãi (nếu có)

**R — Response (Hành động)**:
- CTA chính: "Đăng ký ngay" / "Đặt lịch hôm nay" / "Mua ngay"
- Urgency: giới hạn thời gian hoặc số lượng
- Nhắc lại guarantee để giảm lo ngại

**Template PASTOR:**
```
[Problem: Bạn có đang...?]

[Amplify: Hậu quả 1→2→3]

[Story: Tôi đã từng như bạn... / Khách hàng A đã từng...]
[Solution: Cho đến khi tôi tìm ra...]

[Testimonial 1: "[Quote]" — Tên, vị trí]
[Testimonial 2: "[Quote]" — Tên, vị trí]
[Số liệu tổng: X người đã...]

[Offer]
Hôm nay tôi giới thiệu [Tên sản phẩm]:
✓ [Thành phần 1] — Trị giá [X]
✓ [Thành phần 2] — Trị giá [Y]
✓ [Bonus 1]
Tổng giá trị: [Z] | Giá hôm nay: [Giá ưu đãi]
Bảo đảm: [Cam kết]

[Response]
👉 [CTA chính]
⏰ [Urgency]
🛡️ [Nhắc lại guarantee]
```

---

### Bước 3 — Áp dụng UX Writing Standards

- Câu ≤20 từ, đoạn 2-4 câu
- Dùng "bạn", active voice
- Bold ý quan trọng: tên sản phẩm, con số, CTA
- Emoji tiết chế (chỉ dùng ở CTA và đầu mục nếu phù hợp với tone)

### Bước 4 — Lưu file

Lưu tại: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\sales-{slug}.md`

Thêm metadata block đầu file:
```
<!-- Sales Content
Framework: {AIDA|PAS|BAB|PASTOR}
Keyword: {keyword}
Product: {product}
Audience: {audience}
Length: ~{N} từ
Created: {date}
-->
```

### Bước 5 — Thông báo hoàn thành

```
✅ Content Sales — Hoàn thành
Framework : {AIDA|PAS|BAB|PASTOR}
Keyword   : {keyword}
Product   : {product}
File      : seo_content/output/{category}/{slug}/sales-{slug}.md
Độ dài    : ~{N} từ

Gợi ý bước tiếp:
→ /content-headline --keyword "{keyword}" --type ad  (tối ưu tiêu đề)
→ /seo-audit --file path  (nếu dùng làm landing page dài)
```
