---
name: content-headline
description: |
  Đánh giá và viết headline/tiêu đề theo framework 4U (Useful - Urgent - Unique - Ultra-specific).
  Chấm điểm 1-4 cho từng yếu tố, tổng ≥12/16 mới đạt chuẩn. Xuất alternatives tốt hơn.
  Kích hoạt khi user yêu cầu: "4U", "viết tiêu đề", "headline", "tối ưu title",
  "meta title", "đánh giá tiêu đề", "viết hook", "kiểm tra headline", "cải thiện headline",
  "title hấp dẫn", "tối ưu meta", "tiêu đề SEO".
  Cú pháp: --keyword "X" [--headline "tiêu đề cần đánh giá"] [--count 5] [--type blog|ad|email|social] [--lang vi|en]
argument-hint: --keyword "X" [--headline "tiêu đề cần đánh giá"] [--count 5] [--type blog|ad|email|social] [--lang vi|en]
allowed-tools: [Read, Write]
---

# Content Headline — Viết & Đánh Giá Tiêu Đề theo 4U

Đánh giá headline hiện tại và/hoặc tạo alternatives đạt chuẩn 4U.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: chủ đề/từ khóa bài viết
- `--headline "tiêu đề"` — TÙY CHỌN: headline cần đánh giá. Nếu không có → chỉ tạo mới
- `--count N` — TÙY CHỌN: số alternatives cần tạo (mặc định: 5)
- `--type blog|ad|email|social` — TÙY CHỌN: loại content, ảnh hưởng tone và độ dài (mặc định: blog)
- `--lang vi|en` — TÙY CHỌN: ngôn ngữ (mặc định: vi)

Nếu không có `--keyword`, hỏi user ngay trước khi tiếp tục.

## Framework 4U — Thang điểm chi tiết

Mỗi yếu tố chấm từ **1 đến 4**. Headline đạt chuẩn: **tổng ≥12/16 VÀ không yếu tố nào < 3**.

### U1 — Useful (Hữu ích)
Headline hứa hẹn lợi ích CỤ THỂ cho người đọc không?
- **4**: Lợi ích rõ ràng, cụ thể, đo được — người đọc biết mình được gì
- **3**: Có lợi ích nhưng còn chung chung
- **2**: Lợi ích mơ hồ, phải suy đoán
- **1**: Không có lợi ích rõ ràng

### U2 — Urgent (Cấp thiết)
Tạo cảm giác phải đọc NGAY bây giờ không?
- **4**: Urgency mạnh — deadline, xu hướng đang nóng, "hôm nay", "trước khi...", "năm 2026"
- **3**: Có urgency nhẹ (từ thời gian, sự kiện)
- **2**: Ít cảm giác urgency
- **1**: Không có urgency

### U3 — Unique (Độc đáo)
Khác biệt với 100 bài tương tự trên Google không?
- **4**: Góc nhìn mới, đối tượng cụ thể, điểm khác biệt rõ ràng, chưa ai nói
- **3**: Có điểm khác nhưng chưa đủ nổi
- **2**: Khá giống các bài phổ biến
- **1**: Giống y chang headline phổ biến nhất

### U4 — Ultra-specific (Cực kỳ cụ thể)
Có con số, thời gian, đối tượng, kết quả cụ thể không?
- **4**: Rất cụ thể — có ≥2 yếu tố (số, thời gian, đối tượng, kết quả)
- **3**: Khá cụ thể — có 1 yếu tố cụ thể
- **2**: Chung chung
- **1**: Rất mơ hồ, không có gì cụ thể

**Ngưỡng đánh giá:**
- ≥12/16 và không yếu tố nào < 3 → **ĐẠT ✓** — sẵn sàng dùng
- 9-11 hoặc có yếu tố dưới 3 → **CẦN CẢI THIỆN ⚠️**
- <9 → **VIẾT LẠI ✗**

## Quy trình thực hiện

### Bước 1 — Đánh giá headline gốc (chỉ khi có `--headline`)

Chấm điểm từng yếu tố với lý do cụ thể, không phán xét chung chung.

Output:
```
## Đánh giá: "{headline gốc}"

| Yếu tố | Điểm | Lý do |
|--------|------|-------|
| Useful | X/4 | [lý do cụ thể] |
| Urgent | X/4 | [lý do cụ thể] |
| Unique | X/4 | [lý do cụ thể] |
| Ultra-specific | X/4 | [lý do cụ thể] |
| **Tổng** | **X/16** | **ĐẠT ✓ / CẦN CẢI THIỆN ⚠️ / VIẾT LẠI ✗** |

**Điểm yếu cần cải thiện:** [yếu tố thấp nhất] — [gợi ý cụ thể]
```

### Bước 2 — Tạo alternatives

Tạo N alternatives (theo `--count`, mặc định 5), tất cả đều ≥12/16.

**Nguyên tắc tạo alternatives:**
- Đa dạng góc tiếp cận: số liệu / thời gian / đối tượng / kết quả / bí mật / cảnh báo
- Ưu tiên **con số lẻ** (7, 9, 11, 15) — CTR cao hơn số chẵn
- Thêm **năm (2026)** nếu `--type blog` — tăng tính cập nhật
- **Đối tượng cụ thể**: không phải "phụ nữ" mà "mẹ sau sinh 0-6 tháng"
- Tránh trùng lặp cấu trúc giữa các alternatives

**Templates hữu ích theo từng type:**

*Blog:*
- "[Số] [Phương pháp] để [Kết quả] cho [Đối tượng] ([Năm])"
- "Cách [Hành động] [Kết quả cụ thể] trong [Thời gian] (Đã test trên [Con số])"
- "[Đối tượng]: [Số] Điều [Chủ đề] Bạn Chưa Biết ([Năm])"

*Ad:*
- "[Kết quả cụ thể] trong [Thời gian] — [Giảm rào cản]"
- "Tại sao [Đối tượng] chọn [Sản phẩm]? [Con số] người đã [Kết quả]"

*Email:*
- "[Tên], [Số] điều về [Chủ đề] bạn cần biết trước [Deadline]"

*Social:*
- "[Con số gây sốc] — [Hậu quả nếu không biết điều này]"

Output:
```
## {N} Headline Alternatives (tất cả ≥12/16)

1. "{headline 1}" → **14/16** (U:4 Ur:3 Un:4 S:3)
   Mạnh nhất ở: [điểm mạnh]. Phù hợp: [use case]

2. "{headline 2}" → **13/16** (U:4 Ur:3 Un:3 S:3)
   Mạnh nhất ở: [điểm mạnh]. Phù hợp: [use case]

[...tiếp tục]

---
**Nên chọn:**
- #[N] nếu bạn muốn [mục đích A]
- #[N] nếu bạn muốn [mục đích B]
```

### Bước 3 — Thông báo hoàn thành

```
✅ Content Headline — Hoàn thành
Keyword     : {keyword}
Type        : {type}
Đánh giá    : {headline gốc nếu có → điểm/16}
Alternatives: {N} headlines (tất cả ≥12/16)

Bước tiếp theo:
→ /content-intro --keyword "{keyword}"  (viết mở bài phù hợp)
→ /content-sales --keyword "{keyword}" --category {category}  (viết bài bán hàng)
```
