---
name: content-video
description: |
  Viết script video ngắn theo framework QUEST (Question-Unexpected-Explain-Solution-Transform)
  cho TikTok, Instagram Reels, YouTube Shorts. Output có timing markers và visual cues.
  Kích hoạt khi user yêu cầu: "QUEST", "script tiktok", "script reels", "script shorts",
  "video ngắn", "viết kịch bản video", "script 60 giây", "hook video", "tiktok script",
  "reels script", "youtube shorts", "kịch bản tiktok", "kịch bản video ngắn",
  "viết script cho video", "hook tiktok", "15 giây", "30 giây", "60 giây".
  Cú pháp: --keyword "X" --category slug [--duration 15|30|60] [--platform tiktok|reels|shorts] [--cta "hành động"] [--lang vi|en]
argument-hint: --keyword "X" --category slug [--duration 15|30|60] [--platform tiktok|reels|shorts] [--cta "hành động"] [--lang vi|en]
allowed-tools: [Read, Write, WebSearch]
---

# Content Video — Viết Script Video Ngắn theo QUEST

Tạo kịch bản video ngắn tối ưu cho TikTok / Instagram Reels / YouTube Shorts với timing markers, VO (voiceover), visual cues và caption overlay.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: chủ đề/từ khóa
- `--category slug` — **BẮT BUỘC** (VD: digital-marketing, suc-khoe, social-media)
- `--duration 15|30|60` — TÙY CHỌN: độ dài video (giây). Mặc định: 60
- `--platform tiktok|reels|shorts` — TÙY CHỌN: nền tảng (ảnh hưởng CTA và tone). Mặc định: tiktok
- `--cta "hành động"` — TÙY CHỌN: hành động muốn khán giả làm (follow, comment, inbox, link bio)
- `--lang vi|en` — TÙY CHỌN: ngôn ngữ (mặc định: vi)

Nếu thiếu `--keyword` hoặc `--category`: hỏi user ngay.

## Framework QUEST

**QUEST** = Question → Unexpected → Explain → Solution → Transform

Thiết kế cho video ngắn có thuật toán ưu tiên: 3 giây đầu quyết định xem tiếp, retention cao = reach rộng.

**Phân bổ thời gian theo duration:**

| Phase | 15s | 30s | 60s |
|-------|-----|-----|-----|
| Q — Hook | 0-2s | 0-3s | 0-3s |
| U — Engage | 2-5s | 3-8s | 3-8s |
| E — Explain | 5-10s | 8-18s | 8-30s |
| S — Solution | 10-13s | 18-26s | 30-50s |
| T — Transform | 13-15s | 26-30s | 50-60s |

---

## Quy trình thực hiện

### Bước 1 — Thu thập thông tin

**Đọc profile:** `D:\Nunu-Claude\seo_content\profiles\default.json` → `brand_name`, `brand_tone`, `target_audience`, `author_name`.

**[Tùy chọn] Nếu cần nghiên cứu trend:** WebSearch "#{keyword} tiktok viral 2026" → xem format video phổ biến nhất.

**Tạo slug:** ASCII, gạch ngang, không dấu. VD: "cách tăng follow TikTok" → `tang-follow-tiktok`

**Tạo thư mục:** `D:\Nunu-Claude\seo_content\output\{category}\{slug}\`

---

### Bước 2 — Viết script theo QUEST

Áp dụng thời gian phù hợp với `--duration`. Nếu không có `--duration`, mặc định 60 giây.

---

## Q — Question/Hook (0-3s) ← QUAN TRỌNG NHẤT

**Mục tiêu:** Làm người dùng dừng scroll trong 3 giây đầu.

**6 kỹ thuật Hook hiệu quả:**

1. **Câu hỏi gây shock:** "Bạn có biết 90% người Việt đang làm sai điều này?"
2. **Tuyên bố ngược đời:** "Tôi đã xóa Instagram và doanh thu tăng 3 lần."
3. **Số liệu gây chú ý:** "Chỉ 7% creator biết cách này — và họ kiếm gấp đôi."
4. **Tình huống quen thuộc:** "Bạn đã làm đúng rồi nhưng vẫn không ra kết quả?"
5. **Hứa hẹn cụ thể:** "Tôi sẽ cho bạn xem cách tôi tăng 10k follow trong 2 tuần."
6. **Gọi thẳng đối tượng:** "[Đối tượng cụ thể], video này dành cho bạn."

**Quy tắc Hook:**
- Nói thẳng vào camera (eye contact)
- Tốc độ nói: nhanh nhưng rõ ràng
- KHÔNG có intro thương hiệu — người dùng sẽ scroll ngay
- Caption hook phải xuất hiện trong 1 giây đầu

---

## U — Unexpected/Engage (3-8s)

**Mục tiêu:** Mở "loop" khiến khán giả muốn xem đến cuối.

Kỹ thuật:
- **Pattern interrupt:** Thay đổi góc quay, âm nhạc, hoặc visual bất ngờ
- **Thông tin bất ngờ:** Fact ít người biết, nghiên cứu mới, góc nhìn ngược
- **Teaser kết quả:** "Và đây là điều đã thay đổi mọi thứ..." (nhưng chưa nói là gì)
- **Conflict setup:** Thiết lập vấn đề vs. giải pháp bất ngờ

**Nguyên tắc:** Khán giả phải nghĩ "Ồ thật không? Phải xem tiếp mới biết."

---

## E — Explain/Understand (8-30s)

**Mục tiêu:** Giải thích vấn đề/bối cảnh đủ để khán giả hiểu TẠI SAO giải pháp quan trọng.

Kỹ thuật:
- Dùng visual support: text overlay, B-roll, graphic
- Số liệu/thống kê tăng credibility
- Kể câu chuyện ngắn: "Tôi từng...", "Khách hàng của tôi..."
- Tempo nhanh — mỗi 2-3 giây phải có thông tin mới

**Quy tắc Explain:**
- Không giải thích dài — chỉ đủ để setup Solution
- Mỗi câu = 1 ý rõ ràng
- Visual phải match với VO (voice over)

---

## S — Solution (30-50s)

**Mục tiêu:** Trình bày giải pháp CỤ THỂ, có thể áp dụng ngay.

Cấu trúc Solution:
- **1-3 điểm giải pháp** (không nhiều hơn — video ngắn)
- Mỗi điểm: Tên → Giải thích ngắn → Ví dụ cụ thể
- Dùng số: "Bước 1", "Bước 2", "Bước 3" → dễ theo dõi
- Text overlay liệt kê các điểm song song với VO

**Quy tắc Solution:**
- Phải đủ cụ thể để áp dụng ngay — không chỉ "lý thuyết"
- Nếu sản phẩm/dịch vụ liên quan: giới thiệu tự nhiên ở đây, không cứng
- Demo > Tell: show màn hình, thực hiện thật, kết quả thật

---

## T — Transform/CTA (50-60s)

**Mục tiêu:** Kết nối kết quả → CTA rõ ràng, 1 hành động duy nhất.

Kỹ thuật Transform:
- **Kết quả:** "Tôi đã [kết quả cụ thể] sau khi áp dụng điều này."
- **Identity shift:** "Bạn không còn là người [trạng thái cũ] nữa — bạn là người [trạng thái mới]."
- **Future pacing:** "Tưởng tượng [thời gian] sau khi bạn làm điều này mỗi ngày..."

CTA theo platform:
- **TikTok:** "Follow để không bỏ lỡ video tiếp theo" / "Comment [từ khóa] để nhận [resource]"
- **Reels:** "Save video này để dùng lại" / "Tag bạn bè cần xem điều này"
- **Shorts:** "Subscribe để xem thêm" / "Like nếu video này hữu ích"

**Nếu có `--cta`:** Dùng CTA được chỉ định. Nếu không: chọn CTA phù hợp nhất với platform.

---

### Bước 3 — Output Script với Timing Markers

Viết script theo format chuẩn với đầy đủ markers:

```
<!-- Video Script
Framework: QUEST
Keyword: {keyword}
Platform: {platform}
Duration: {duration}s
Created: {date}
-->

# Script: {tiêu đề video — cũng là caption/title đăng lên}

**📊 Thông tin kỹ thuật:**
- Platform: {TikTok | Reels | Shorts}
- Thời lượng: {duration} giây
- CTA: {cta}
- Hook type: {loại hook đã chọn}

---

## SCRIPT ĐẦY ĐỦ

---

[0-3s | Q — HOOK]
VO: "{câu hook — ngắn, mạnh, bắt đầu bằng hook phrase}"
[VISUAL: mô tả cảnh quay — góc camera, hành động, biểu cảm]
[CAPTION: text overlay xuất hiện ngay giây 1 — chữ lớn, màu nổi bật]

---

[3-8s | U — ENGAGE]
VO: "{thông tin bất ngờ hoặc teaser — tạo open loop}"
[VISUAL: cut nhanh, B-roll, hoặc graphic minh họa]
[CAPTION: {key phrase ngắn — 3-5 từ}]
[MUSIC: {gợi ý âm nhạc — trending sound hoặc mô tả vibe}]

---

[8-{X}s | E — EXPLAIN]
VO: "{giải thích vấn đề/bối cảnh}"
[VISUAL: {screen recording / B-roll / talking head}]
[TEXT OVERLAY: "{key stat hoặc fact}"]

[Tiếp tục nếu cần nhiều dòng E...]

---

[{X}-{Y}s | S — SOLUTION]
VO: "Đây là cách tôi làm:"
[VISUAL: {demo thực tế hoặc step-by-step}]

**[Điểm 1]:**
VO: "{bước 1 — cụ thể}"
[CAPTION: "1️⃣ {tên điểm 1}"]

**[Điểm 2]:**
VO: "{bước 2}"
[CAPTION: "2️⃣ {tên điểm 2}"]

**[Điểm 3 — nếu có]:**
VO: "{bước 3}"
[CAPTION: "3️⃣ {tên điểm 3}"]

---

[{Y}-{duration}s | T — TRANSFORM + CTA]
VO: "{kết quả thật / identity shift}"
[VISUAL: {kết quả, screenshot, before-after}]
[CAPTION: "{số liệu kết quả cụ thể}"]

VO: "{CTA — 1 hành động rõ ràng}"
[CAPTION: "👆 {CTA text — ngắn gọn}"]

---

## NOTES CHO EDITOR / CREATOR

**Hashtags gợi ý:**
#{keyword-slug} #{brand} #{topic1} #{topic2} #{platform}

**Caption đăng bài (150-200 ký tự):**
"{hook phrase} {value proposition} {CTA ngắn} {2-3 hashtags quan trọng}"

**Thumbnail/Cover frame:**
- Giây: [{giây tốt nhất làm thumbnail}]
- Text trên thumbnail: "{câu ngắn gọn, gây chú ý}"

**A/B Test gợi ý:**
- Hook A: [{hook đã viết}]
- Hook B: [{alternative hook — khác kiểu}]

<!-- TODO — Cần làm trước khi quay
- [ ] Chuẩn bị B-roll cho phần Explain
- [ ] Chọn trending sound phù hợp trên {platform}
- [ ] Chuẩn bị props/setup cho phần demo
- [ ] Kiểm tra lighting và âm thanh
-->

<!-- Author: {author_name}
Ngày tạo: {date}
-->
```

---

### Bước 4 — Áp dụng Platform-specific Standards

**TikTok:**
- Hook bằng câu hỏi hoặc statement — không chào hỏi
- Trending sound > original sound (nếu không có brief cụ thể)
- Text overlay lớn, contrasting color (trắng trên tối, hoặc ngược lại)
- Caption tối đa 2.200 ký tự — nhưng chỉ 150 ký tự hiển thị trước "more"

**Instagram Reels:**
- Quality hình ảnh cao hơn TikTok
- Save-worthy content — tip, checklist, tutorial
- CTA: "Save" hoạt động tốt hơn "like"
- Caption đầy đủ hơn, có thể dài hơn

**YouTube Shorts:**
- Title quan trọng cho SEO — keyword ở đầu
- Thumbnail quan trọng (dù autoplay)
- CTA: "Subscribe" phù hợp hơn
- Ít trend sound hơn, nội dung giữ lâu hơn

---

### Bước 5 — Lưu file

Lưu tại: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\script-{slug}.md`

### Bước 6 — Thông báo hoàn thành

```
✅ Content Video — Hoàn thành
Framework : QUEST
Keyword   : {keyword}
Platform  : {platform}
Duration  : {duration}s
File      : seo_content/output/{category}/{slug}/script-{slug}.md

Script đã bao gồm:
→ Timing markers (0s → {duration}s)
→ VO (voiceover text)
→ Visual cues và caption overlay
→ Hashtags và caption đăng bài
→ A/B test hook alternatives

Gợi ý bước tiếp:
→ /content-headline --keyword "{keyword}" --type social  (tối ưu caption hook)
→ /content-sales --keyword "{keyword}" --category {category}  (landing page cho traffic từ video)
```
