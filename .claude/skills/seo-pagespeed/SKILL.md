---
name: seo-pagespeed
description: |
  Kiểm tra Core Web Vitals và điểm PageSpeed của URL bằng Google PageSpeed Insights API.
  Kích hoạt khi user yêu cầu "kiểm tra tốc độ", "check pagespeed", "core web vitals",
  "kiểm tra LCP CLS INP", "tốc độ tải trang", "pagespeed score", "lighthouse score",
  "check performance", "tối ưu tốc độ", "web vitals", "kiểm tra website".
argument-hint: --url https://example.com [--apikey YOUR_KEY] [--strategy mobile|desktop|both] [--keyword "từ khóa"]
allowed-tools: [WebFetch, Read, Write]
---

# SEO PageSpeed — Kiểm tra Core Web Vitals qua API

Gọi Google PageSpeed Insights API để lấy điểm Lighthouse và số liệu Core Web Vitals
thực tế từ dữ liệu người dùng thật (CrUX). Lưu báo cáo Markdown và JSON.

**Yêu cầu API key** (miễn phí, 25.000 req/ngày):
1. Vào https://console.cloud.google.com/apis/credentials → "Create credentials" → "API key"
2. Enable "PageSpeed Insights API" tại https://console.cloud.google.com/apis/library
3. Lưu key vào `D:\Nunu-Claude\seo_content\profiles\default.json` trường `pagespeed_api_key`
   hoặc truyền qua `--apikey YOUR_KEY`

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--url https://...` — **BẮT BUỘC**: URL cần kiểm tra
- `--apikey KEY` — Google PageSpeed API key (ưu tiên hơn profile)
- `--strategy mobile|desktop|both` — thiết bị kiểm tra (mặc định: both)
- `--keyword "X"` — từ khóa SEO của trang (dùng để đặt tên file)

Nếu không có `--url`, hỏi user trước khi tiếp tục.

**Xác định API key:**
1. Nếu có `--apikey KEY`: dùng key đó
2. Nếu không: đọc `D:\Nunu-Claude\seo_content\profiles\default.json`, lấy `pagespeed_api_key`
3. Nếu không có key: thông báo và hướng dẫn tạo key (xem phần đầu)

## Quy trình thực hiện

### Bước 1 — Gọi PageSpeed Insights API

Gọi API cho từng strategy được yêu cầu bằng WebFetch:

**Mobile:**
```
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={URL}&strategy=mobile&key={API_KEY}
```

**Desktop:**
```
https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={URL}&strategy=desktop&key={API_KEY}
```

Nếu `--strategy both` (mặc định): gọi cả 2 URL. Nếu chỉ `mobile` hoặc `desktop`: gọi 1 URL.

### Bước 2 — Trích xuất dữ liệu từ JSON response

Từ mỗi response, trích xuất:

**Điểm Lighthouse (0-100):**
- `lighthouseResult.categories.performance.score × 100`
- `lighthouseResult.categories.accessibility.score × 100`
- `lighthouseResult.categories.best-practices.score × 100`
- `lighthouseResult.categories.seo.score × 100`

**Core Web Vitals — Dữ liệu thực tế (CrUX field data):**
- `loadingExperience.metrics.LARGEST_CONTENTFUL_PAINT_MS.percentile` → LCP (ms)
- `loadingExperience.metrics.LARGEST_CONTENTFUL_PAINT_MS.category` → FAST/AVERAGE/SLOW
- `loadingExperience.metrics.CUMULATIVE_LAYOUT_SHIFT_SCORE.percentile` → CLS (×100)
- `loadingExperience.metrics.CUMULATIVE_LAYOUT_SHIFT_SCORE.category`
- `loadingExperience.metrics.INTERACTION_TO_NEXT_PAINT.percentile` → INP (ms)
- `loadingExperience.metrics.INTERACTION_TO_NEXT_PAINT.category`
- `loadingExperience.overall_category` → kết luận tổng: FAST / AVERAGE / SLOW

Nếu `loadingExperience.metrics` thiếu (URL ít traffic, chưa có CrUX data):
- Ghi rõ "Chưa đủ dữ liệu thực tế từ người dùng" và dùng dữ liệu Lighthouse lab thay thế.

**Core Web Vitals — Dữ liệu lab (Lighthouse):**
- `lighthouseResult.audits.largest-contentful-paint.displayValue` → LCP lab
- `lighthouseResult.audits.cumulative-layout-shift.displayValue` → CLS lab
- `lighthouseResult.audits.total-blocking-time.displayValue` → TBT (thay cho INP trong lab)
- `lighthouseResult.audits.first-contentful-paint.displayValue` → FCP
- `lighthouseResult.audits.speed-index.displayValue` → Speed Index

**Opportunities (gợi ý tối ưu):**
- Lấy các audit có `score < 0.9` và `details.type == "opportunity"`
- Trích: `title`, `displayValue`, `description`
- Lấy tối đa 5 opportunity quan trọng nhất (sắp xếp theo `numericValue` giảm dần)

### Bước 3 — Đọc ngưỡng đánh giá

Đọc `D:\Nunu-Claude\seo_content\.claude\skills\seo-pagespeed\thresholds.json`
để lấy ngưỡng GOOD/NEEDS IMPROVEMENT/POOR cho từng chỉ số.

### Bước 4 — Đánh giá và xếp loại

Dùng ngưỡng từ thresholds.json, gán trạng thái cho từng metric:
- ✅ **Tốt** — đạt ngưỡng GOOD
- ⚠️ **Cần cải thiện** — NEEDS IMPROVEMENT
- ❌ **Kém** — POOR

Điểm tổng PageSpeed:
- 90-100: Xuất sắc
- 75-89: Tốt
- 50-74: Cần cải thiện
- 0-49: Kém

### Bước 5 — Tạo slug và lưu file

Tạo slug:
- Nếu có `--keyword`: dùng keyword → ASCII, gạch ngang
- Nếu không có: lấy hostname của URL (VD: `example-com`)

Lưu 2 file vào thư mục shared (không gắn với bài viết cụ thể):
- `D:\Nunu-Claude\seo_content\output\_shared\pagespeed\{slug}.md`
- `D:\Nunu-Claude\seo_content\output\_shared\pagespeed\{slug}.json`

Tạo thư mục nếu chưa có.

## Định dạng file pagespeed_{slug}.md

```markdown
# Báo cáo PageSpeed: {URL}

**Ngày kiểm tra:** {YYYY-MM-DD HH:MM}
**URL:** {url}
**Keyword:** {keyword hoặc N/A}
**Nguồn dữ liệu:** Google PageSpeed Insights API v5

---

## Tổng quan

| Chỉ số | Mobile | Desktop |
|--------|--------|---------|
| Performance | {score}/100 | {score}/100 |
| Accessibility | {score}/100 | {score}/100 |
| Best Practices | {score}/100 | {score}/100 |
| SEO | {score}/100 | {score}/100 |

---

## Core Web Vitals — Dữ liệu thực tế (CrUX)

> Dữ liệu từ người dùng thật trong 28 ngày qua. Đây là chỉ số Google dùng để ranking.

| Metric | Giá trị | Ngưỡng Tốt | Trạng thái |
|--------|---------|-----------|-----------|
| LCP (Largest Contentful Paint) | {Xms} | < 2500ms | ✅/⚠️/❌ |
| INP (Interaction to Next Paint) | {Xms} | < 200ms | ✅/⚠️/❌ |
| CLS (Cumulative Layout Shift) | {X.XXX} | < 0.1 | ✅/⚠️/❌ |
| **Kết luận tổng** | | | {FAST/AVERAGE/SLOW} |

---

## Core Web Vitals — Dữ liệu Lab (Lighthouse)

> Dữ liệu từ môi trường kiểm soát, dùng để debug.

**Mobile:**
| Metric | Giá trị | Trạng thái |
|--------|---------|-----------|
| LCP | {Xs} | ✅/⚠️/❌ |
| TBT (Total Blocking Time) | {Xms} | ✅/⚠️/❌ |
| CLS | {X.XXX} | ✅/⚠️/❌ |
| FCP | {Xs} | ✅/⚠️/❌ |
| Speed Index | {Xs} | ✅/⚠️/❌ |

**Desktop:** *(nếu --strategy both)*
[bảng tương tự]

---

## Cơ hội tối ưu (Top 5)

### 1. {Tên opportunity}
- **Tiết kiệm ước tính:** {displayValue}
- **Mô tả:** {description ngắn}

### 2. {Tên opportunity}
...

---

## Nhận xét & Khuyến nghị

{Tóm tắt 3-5 điểm hành động ưu tiên dựa trên kết quả, sắp xếp theo mức độ ảnh hưởng}

---

## Liên kết hữu ích

- Xem chi tiết: https://pagespeed.web.dev/report?url={url_encoded}
- Web Vitals docs: https://web.dev/vitals/
```

## Định dạng file pagespeed_{slug}.json

```json
{
  "url": "{url}",
  "keyword": "{keyword hoặc null}",
  "checked_at": "{ISO 8601}",
  "mobile": {
    "performance": 0,
    "accessibility": 0,
    "best_practices": 0,
    "seo": 0,
    "lcp_ms": 0,
    "inp_ms": 0,
    "cls": 0.0,
    "fcp_ms": 0,
    "tbt_ms": 0,
    "crux_overall": "FAST|AVERAGE|SLOW|NO_DATA"
  },
  "desktop": {
    "performance": 0,
    "accessibility": 0,
    "best_practices": 0,
    "seo": 0,
    "lcp_ms": 0,
    "inp_ms": 0,
    "cls": 0.0,
    "fcp_ms": 0,
    "tbt_ms": 0,
    "crux_overall": "FAST|AVERAGE|SLOW|NO_DATA"
  },
  "top_opportunities": [
    { "title": "...", "savings": "..." }
  ],
  "grade": "excellent|good|needs_improvement|poor"
}
```

## Thông báo hoàn thành

Sau khi lưu, báo cáo:
- Điểm Performance mobile / desktop
- Trạng thái CrUX tổng (FAST / AVERAGE / SLOW)
- Top 2 vấn đề cần sửa ngay
- Đường dẫn 2 file đã lưu
- Gợi ý: "Dùng `/seo-audit --url {url}` để kiểm tra chất lượng nội dung"
