# SEO Content Workspace

Bộ công cụ viết và tối ưu nội dung SEO theo chuẩn Google 2025-2026 (E-E-A-T, People-first, GEO/AI Search).

## Slash commands

```
/seo-research --keyword "từ khóa" [--competitor URL1 URL2...] [--lang vi|en]
/seo-write    --keyword "từ khóa" [--research research_{slug}.md] [--author "Tên, Chức danh"]
/seo-audit    --file draft_{slug}.md | --url https://example.com [--keyword "từ khóa"]
/seo-pagespeed --url https://example.com [--strategy mobile|desktop|both]
```

## Quy trình chuẩn

```
/seo-research → /seo-write → /seo-audit → /seo-pagespeed
```

1. **Research**: phân tích SERP, đối thủ, content gap → `research_{slug}.md`
2. **Write**: viết bài hoàn chỉnh E-E-A-T + GEO → `draft_{slug}.md`
3. **Audit**: chấm điểm 7 giai đoạn (0-100) → `audit_{slug}.md` + `audit_{slug}.json`
4. **PageSpeed**: kiểm tra Core Web Vitals thực tế → `pagespeed_{slug}.md` + `pagespeed_{slug}.json`

## Cấu trúc

```
seo_content/
  .claude/
    skills/
      seo-research/SKILL.md    # Nghiên cứu từ khóa & SERP
      seo-write/SKILL.md       # Viết bài chuẩn SEO
      seo-audit/SKILL.md       # Chấm điểm content
      seo-pagespeed/
        SKILL.md               # Kiểm tra Core Web Vitals
        thresholds.json        # Ngưỡng GOOD/NEEDS IMPROVEMENT/POOR
  profiles/
    default.json               # Thông tin tác giả & thương hiệu (điền 1 lần)
  checklist.md                 # Checklist 8 giai đoạn đầy đủ (tài liệu tham chiếu)
  research_{slug}.md           # Output: research brief
  draft_{slug}.md              # Output: bài viết hoàn chỉnh
  audit_{slug}.md              # Output: báo cáo audit dạng đọc
  audit_{slug}.json            # Output: điểm số cấu trúc JSON
  pagespeed_{slug}.md          # Output: báo cáo Core Web Vitals
  pagespeed_{slug}.json        # Output: điểm PageSpeed JSON
```

## Cấu hình lần đầu

Điền thông tin vào `profiles/default.json`:

```json
{
  "author_name": "Tên tác giả",
  "author_title": "Chức danh",
  "author_bio": "Mô tả ngắn",
  "brand_name": "Tên thương hiệu",
  "brand_website": "https://example.com",
  "brand_tone": "thân thiện, chuyên nghiệp, dễ hiểu",
  "target_audience": "Đối tượng mục tiêu",
  "industry": "Lĩnh vực"
}
```

## Thang điểm audit

| Điểm | Ý nghĩa |
|------|---------|
| 90-100 | Xuất sắc — sẵn sàng đăng |
| 75-89 | Tốt — cần chỉnh nhỏ |
| 60-74 | Trung bình — cần cải thiện |
| 40-59 | Yếu — cần viết lại một số phần |
| 0-39 | Kém — nên viết lại toàn bộ |

## Ví dụ

```bash
# Nghiên cứu từ khóa
/seo-research --keyword "học lái xe ô tô"

# Viết bài dùng research có sẵn
/seo-write --keyword "học lái xe ô tô" --research research_hoc-lai-xe-o-to.md

# Audit bài trước khi đăng
/seo-audit --file draft_hoc-lai-xe-o-to.md

# Kiểm tra tốc độ trang đã đăng
/seo-pagespeed --url https://example.com/hoc-lai-xe-o-to
```
