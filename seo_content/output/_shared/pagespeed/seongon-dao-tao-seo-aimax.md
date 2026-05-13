# Báo cáo PageSpeed: https://seongon.com/dao-tao/seo-aimax

**Ngày kiểm tra:** 2026-05-10
**URL:** https://seongon.com/dao-tao/seo-aimax
**Keyword:** N/A
**Nguồn dữ liệu:** Google PageSpeed Insights API v5

---

## Tổng quan

| Chỉ số | Mobile | Desktop |
|--------|--------|---------|
| Performance | 33/100 ❌ | 41/100 ❌ |

> *Lighthouse chỉ trả về điểm Performance cho URL này — các category còn lại (Accessibility, Best Practices, SEO) không có trong response.*

---

## Core Web Vitals — Dữ liệu thực tế (CrUX)

> Dữ liệu từ người dùng thật trong 28 ngày qua. Đây là chỉ số Google dùng để ranking.

### Mobile
| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP | 1,985 ms | < 2,500 ms | ✅ Tốt |
| INP | 223 ms | < 200 ms | ⚠️ Cần cải thiện |
| CLS | 0.000 | < 0.1 | ✅ Tốt |
| FCP | 1,564 ms | < 1,800 ms | ✅ Tốt |
| TTFB | 785 ms | < 800 ms | ✅ Tốt |
| **Kết luận tổng** | | | ⚠️ **AVERAGE** |

### Desktop
| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP | 966 ms | < 2,500 ms | ✅ Tốt |
| INP | 95 ms | < 200 ms | ✅ Tốt |
| CLS | 0.000 | < 0.1 | ✅ Tốt |
| FCP | 747 ms | < 1,800 ms | ✅ Tốt |
| **Kết luận tổng** | | | ✅ **FAST** |

---

## Core Web Vitals — Dữ liệu Lab (Lighthouse)

> Dữ liệu từ môi trường kiểm soát, dùng để debug. Thường khắc nghiệt hơn dữ liệu thực tế.

### Mobile
| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP | 23.1 s | < 2.5 s | ❌ Kém |
| TBT | 1,070 ms | < 200 ms | ❌ Kém |
| CLS | 0 | < 0.1 | ✅ Tốt |
| FCP | 5.7 s | < 1.8 s | ❌ Kém |
| Speed Index | 17.4 s | < 3.4 s | ❌ Kém |

### Desktop
| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP | 1.7 s | < 2.5 s | ✅ Tốt |
| TBT | 1,950 ms | < 200 ms | ❌ Kém |
| CLS | 0.263 | < 0.1 | ❌ Kém |
| FCP | 0.6 s | < 1.8 s | ✅ Tốt |
| Speed Index | 3.9 s | < 3.4 s | ⚠️ Cần cải thiện |

---

## Cơ hội tối ưu (Top 3)

### 1. Reduce unused JavaScript
- **Tiết kiệm ước tính:** ~3,964 KiB (mobile) / ~3,837 KiB (desktop)
- **Mô tả:** Đây là vấn đề nghiêm trọng nhất. Gần 4MB JavaScript được tải nhưng không dùng, làm tăng TBT và block main thread. Cần audit các plugin/script đang enqueue — đặc biệt là các script của page builder hoặc plugin WordPress không dùng trên trang này.

### 2. Reduce unused CSS
- **Tiết kiệm ước tính:** ~95 KiB (mobile) / ~45 KiB (desktop)
- **Mô tả:** CSS không dùng làm chậm render. Dùng PurgeCSS hoặc cấu hình plugin caching để chỉ load CSS cần thiết cho từng trang.

### 3. Minify JavaScript
- **Tiết kiệm ước tính:** ~13 KiB
- **Mô tả:** Một số file JS chưa được minify. Bật minification trong plugin caching (WP Rocket, LiteSpeed Cache, W3 Total Cache).

---

## Nhận xét & Khuyến nghị

**Điểm tích cực:**
- CrUX desktop **FAST** — người dùng thực tế trên desktop có trải nghiệm tốt
- CrUX mobile LCP/FCP/CLS đều FAST — tốc độ tải thực tế trên mobile ổn
- TTFB 785ms — server response time chấp nhận được

**Vấn đề cần xử lý ngay (theo thứ tự ưu tiên):**

1. **Unused JavaScript ~4MB** — Nguyên nhân chính khiến TBT cao (1,070ms mobile / 1,950ms desktop) và điểm Lighthouse thấp. Kiểm tra xem plugin/theme nào đang enqueue script toàn site — dequeue trên trang không cần thiết.

2. **Mobile lab LCP 23.1s** — Chênh lệch lớn so với CrUX (1,985ms). Nguyên nhân: JS blocking render. Giải quyết vấn đề JS sẽ kéo lab LCP xuống đáng kể.

3. **Desktop CLS lab 0.263** — Layout shift trong môi trường lab khá cao (dù CrUX = 0). Nguyên nhân thường là font loading hoặc lazy-load images thiếu `width/height`. Thêm `font-display: swap` và khai báo kích thước ảnh.

4. **INP mobile 223ms (AVERAGE)** — Gần ngưỡng tốt. Giảm JS execution time sẽ cải thiện metric này.

---

## Tóm tắt

| | Mobile | Desktop |
|-|--------|---------|
| Lighthouse Performance | 33 ❌ | 41 ❌ |
| CrUX Overall | AVERAGE ⚠️ | FAST ✅ |
| Vấn đề chính | 4MB unused JS | 4MB unused JS + CLS lab |

**Kết luận:** Trang có điểm Lighthouse thấp chủ yếu do **JavaScript quá nhiều và không tối ưu**. Dữ liệu thực tế (CrUX) tốt hơn đáng kể so với lab — desktop đã FAST, mobile AVERAGE. Ưu tiên số 1: audit và giảm JS bundle size.

---

## Liên kết hữu ích

- Xem chi tiết: https://pagespeed.web.dev/report?url=https%3A%2F%2Fseongon.com%2Fdao-tao%2Fseo-aimax
- Web Vitals docs: https://web.dev/vitals/
