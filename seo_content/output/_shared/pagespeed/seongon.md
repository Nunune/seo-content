# Báo cáo PageSpeed: seongon.com

**Ngày kiểm tra:** 2026-05-09
**URL:** https://seongon.com
**Keyword:** seongon
**Nguồn dữ liệu:** Google PageSpeed Insights API v5

---

## Tổng quan Lighthouse Scores

| Chỉ số | Mobile | Desktop |
|--------|--------|---------|
| Performance | 28/100 ❌ | 52/100 ⚠️ |
| Accessibility | 71/100 ⚠️ | 80/100 ⚠️ |
| Best Practices | 100/100 ✅ | 81/100 ⚠️ |
| SEO | 92/100 ✅ | 100/100 ✅ |

> **Nhận xét nhanh:** SEO và Best Practices tốt, nhưng Performance mobile đang ở mức kém (28/100) — cần cải thiện gấp.

---

## Core Web Vitals — Dữ liệu thực tế (CrUX)

> Dữ liệu từ người dùng thật trong 28 ngày qua. Đây là chỉ số Google dùng để ranking.

### Mobile

| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP (Largest Contentful Paint) | 1,988 ms | < 2,500 ms | ✅ FAST |
| INP (Interaction to Next Paint) | 221 ms | < 200 ms | ⚠️ AVERAGE |
| CLS (Cumulative Layout Shift) | 0.00 | < 0.1 | ✅ FAST |
| **Kết luận tổng** | | | ⚠️ **AVERAGE** |

### Desktop

| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP (Largest Contentful Paint) | 1,163 ms | < 2,500 ms | ✅ FAST |
| INP (Interaction to Next Paint) | 77 ms | < 200 ms | ✅ FAST |
| CLS (Cumulative Layout Shift) | 0.00 | < 0.1 | ✅ FAST |
| **Kết luận tổng** | | | ✅ **FAST** |

---

## Core Web Vitals — Dữ liệu Lab (Lighthouse)

> Dữ liệu từ môi trường kiểm soát. Dùng để debug — thường khắt khe hơn CrUX thực tế.

### Mobile

| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP (Largest Contentful Paint) | 23.7 s | < 2.5 s | ❌ POOR |
| TBT (Total Blocking Time) | 740 ms | < 200 ms | ❌ POOR |
| CLS (Cumulative Layout Shift) | 0.395 | < 0.1 | ❌ POOR |
| FCP (First Contentful Paint) | 2.3 s | < 1.8 s | ⚠️ |
| Speed Index | 8.1 s | < 3.4 s | ❌ POOR |

### Desktop

| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP (Largest Contentful Paint) | 1.5 s | < 2.5 s | ✅ |
| TBT (Total Blocking Time) | 570 ms | < 200 ms | ⚠️ |
| CLS (Cumulative Layout Shift) | 0.264 | < 0.1 | ❌ |
| FCP (First Contentful Paint) | 0.5 s | < 1.8 s | ✅ |
| Speed Index | 2.5 s | < 3.4 s | ✅ |

---

## Cơ hội tối ưu (Top Opportunities)

### 1. Reduce unused JavaScript
- **Tiết kiệm ước tính:** ~761 KiB (~1,350 ms)
- **Mô tả:** Loại bỏ JavaScript không được dùng để giảm byte cần truyền tải và thời gian parse/compile.

> *Đây là vấn đề duy nhất được phát hiện ở mức opportunity — nhưng có tác động rất lớn đến mobile performance.*

---

## Nhận xét & Khuyến nghị

### Ưu tiên cao — cần xử lý ngay

1. **Performance mobile (28/100) quá thấp** — chủ yếu do LCP lab 23.7s và TBT 740ms. Nguyên nhân chính: JavaScript chưa sử dụng (~761 KiB). Cần audit và loại bỏ JS không cần thiết, dùng lazy loading.

2. **CLS lab mobile = 0.395** — layout bị dịch chuyển trong quá trình load. Cần kiểm tra ảnh không có thuộc tính width/height, font chữ tải chậm, hoặc content inject sau khi render.

3. **INP mobile = 221ms (AVERAGE)** — phản hồi tương tác còn chậm. Cần giảm long tasks trên main thread.

### Ưu tiên trung — cải thiện thêm

4. **Accessibility mobile (71/100)** — kiểm tra contrast màu chữ/nền, thêm label cho form, alt text cho ảnh.

5. **TBT desktop (570ms)** — còn cao, cần tối ưu JavaScript execution time trên desktop.

### Điểm sáng

- ✅ CrUX desktop: FAST — người dùng desktop có trải nghiệm tốt
- ✅ SEO score: 92 mobile / 100 desktop — cấu trúc SEO kỹ thuật tốt
- ✅ LCP CrUX mobile: 1,988ms (FAST) — dù lab chậm, người dùng thực tế nhận được LCP trong ngưỡng tốt

---

## Liên kết hữu ích

- Xem chi tiết: https://pagespeed.web.dev/report?url=https%3A%2F%2Fseongon.com
- Web Vitals docs: https://web.dev/vitals/
- Hướng dẫn giảm unused JS: https://web.dev/unused-javascript/
