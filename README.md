# Nunu-Claude — Personal AI Workspace

Không gian làm việc cá nhân với Claude Code, gồm 2 bộ công cụ chính:

1. **Google Ads Rank Checker** — tự động kiểm tra thứ hạng quảng cáo Google Ads mobile
2. **SEO Content Workspace** — bộ 4 skill viết và tối ưu nội dung SEO chuẩn Google 2025-2026

---

## Bộ 1: Google Ads Rank Checker (`/check-rank`)

Tự động kiểm tra thứ hạng quảng cáo Google Ads trả phí trên giao diện mobile,
phát hiện đối thủ mới, ghi kết quả vào Google Sheets với màu sắc cạnh tranh.

### Cú pháp
```bash
/check-rank --sheet <URL_GOOGLE_SHEET> [--headed] [--no-vpn]
```

### Setup
```bash
pip install -r requirements.txt
python -m playwright install chromium
windscribe login
```

---

## Bộ 2: SEO Content Workspace (`seo_content/`)

Bộ 4 skill độc lập hỗ trợ toàn bộ quy trình tạo content SEO.

### Các skill

| Skill | Mô tả | Kết nối |
|-------|-------|---------|
| `/seo-research` | Nghiên cứu từ khóa, phân tích SERP & đối thủ | WebSearch |
| `/seo-write` | Viết bài chuẩn E-E-A-T + GEO/AIO | WebSearch |
| `/seo-audit` | Chấm điểm 7 giai đoạn (0-100) | — |
| `/seo-pagespeed` | Kiểm tra Core Web Vitals thực tế | **Google PageSpeed Insights API** |

### Quy trình chuẩn
```
/seo-research → /seo-write → /seo-audit → /seo-pagespeed
```

### Cú pháp
```bash
/seo-research  --keyword "từ khóa" [--competitor URL1 URL2]
/seo-write     --keyword "từ khóa" [--research research_slug.md]
/seo-audit     --file draft_slug.md | --url https://example.com
/seo-pagespeed --url https://example.com --apikey YOUR_KEY
```

### Cấu hình
Điền thông tin tác giả / thương hiệu tại `seo_content/profiles/default.json` (chỉ cần 1 lần).

Để dùng `/seo-pagespeed`, lấy API key miễn phí tại
[Google Cloud Console](https://console.cloud.google.com/apis/credentials) → Enable **PageSpeed Insights API**.

---

## Cấu trúc thư mục

```
.claude/skills/          # Skills dùng khi mở D:\Nunu-Claude
  check-rank/
  seo-research/
  seo-write/
  seo-audit/
  seo-pagespeed/
    SKILL.md
    thresholds.json      # Ngưỡng Core Web Vitals

check_rank/              # Source code Google Ads checker (Python + Playwright)
data/                    # Keywords, competitors, run history
credentials/             # Service account (không commit key thật)

seo_content/             # Workspace SEO độc lập
  .claude/skills/        # Skills dùng khi mở seo_content/
  profiles/default.json  # Cấu hình tác giả & thương hiệu
  checklist.md           # Checklist 8 giai đoạn tham chiếu
  CLAUDE.md              # Tài liệu workspace
  research_*.md          # Output: research brief
  draft_*.md             # Output: bài viết hoàn chỉnh
  audit_*.md / *.json    # Output: báo cáo + điểm số
  pagespeed_*.md / *.json # Output: Core Web Vitals report
```

---

## Yêu cầu

- Python 3.10+
- [Claude Code](https://claude.ai/code)
- Windscribe VPN (cho check-rank)
- Google Service Account (cho check-rank → Google Sheets)
- Google PageSpeed Insights API key (cho seo-pagespeed)
