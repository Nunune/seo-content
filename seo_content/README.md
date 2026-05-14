# SEO Content Pipeline — Claude Code

Bộ công cụ tự động viết và tối ưu nội dung SEO chuẩn Google 2025-2026 chạy trên **Claude Code**.
Từ 1 từ khóa → nghiên cứu → viết bài → audit → cải thiện → tạo ảnh → xuất `.docx` → upload Google Drive.

---

## Tính năng

- **Pipeline đầy đủ** — research → write → audit → improve → image → export `.docx` → Drive upload
- **Chuẩn E-E-A-T + GEO** — tối ưu AI Overview, People Also Ask, schema JSON-LD
- **Batch từ Google Sheet** — đọc danh sách từ khóa, chạy tự động, ghi kết quả ngược lại Sheet
- **20 bài viết mẫu** — 5 category, điểm audit từ 85–92/100
- **Tạo ảnh tự động** — matplotlib chart/diagram + download screenshot từ web
- **Export `.docx`** — ảnh nhúng thật, heading styles, bảng, sẵn sàng upload CMS

---

## Yêu cầu

- [Claude Code](https://claude.ai/code) (CLI hoặc Desktop)
- Python 3.10+

```bash
pip install python-docx Pillow matplotlib gspread google-auth google-api-python-client google-auth-oauthlib
```

---

## Cấu hình lần đầu

**1. Copy file cấu hình:**
```bash
cp profiles/default.example.json profiles/default.json
```

**2. Điền thông tin vào `profiles/default.json`:**

| Field | Mô tả |
|-------|-------|
| `author_name` | Tên tác giả bài viết |
| `brand_name` | Tên thương hiệu / website |
| `brand_website` | URL website (dùng cho internal links) |
| `brand_tone` | Giọng văn (VD: thân thiện, chuyên nghiệp) |
| `pagespeed_api_key` | Google PageSpeed Insights API key |
| `drive_folder_id` | Google Drive folder ID để upload `.docx` |

**3. (Tuỳ chọn) Google Drive upload:**
- Tạo OAuth2 credentials tại Google Cloud Console → lưu vào `../credentials/oauth_client.json`
- Lần đầu chạy upload → browser tự mở để xác thực

> `profiles/default.json` và `credentials/` đã được `.gitignore` — không bao giờ commit key thật.

---

## Sử dụng nhanh

Mở Claude Code trong thư mục `seo_content/`, sau đó:

```
# Viết 1 bài từ đầu đến cuối
/seo-research --keyword "học lái xe ô tô" --category giao-thong
/seo-write    --keyword "học lái xe ô tô" --category giao-thong --research output/giao-thong/hoc-lai-xe-o-to/research.md
/seo-improve  --draft output/giao-thong/hoc-lai-xe-o-to/draft.md --keyword "học lái xe ô tô" --target 85
# → Tự động: fix loop → ảnh → export .docx → README.md

# Batch từ Google Sheet
/seo-batch --sheet "https://docs.google.com/spreadsheets/d/ID/edit" --limit 5
```

Xem đầy đủ lệnh tại [CLAUDE.md](CLAUDE.md).

---

## Skills có sẵn

### SEO Pipeline

| Skill | Chức năng |
|-------|-----------|
| `/seo-research` | Phân tích SERP, đối thủ, content gap → `research.md` |
| `/seo-write` | Viết bài chuẩn SEO E-E-A-T + GEO → `draft.md` |
| `/seo-audit` | Chấm điểm 8 phase (0–100) → `audit.md` + `audit.json` |
| `/seo-improve` | Auto-fix loop → ảnh → `.docx` → `README.md` |
| `/seo-image` | Tạo diagram/chart (matplotlib) + tải screenshot |
| `/seo-export` | Xuất `.docx` với ảnh nhúng, loại comment kỹ thuật |
| `/seo-webp` | Convert PNG/JPG → WebP trước khi upload CMS |
| `/seo-pagespeed` | Kiểm tra Core Web Vitals qua PageSpeed Insights API |

### Content Writing

| Skill | Framework | Output |
|-------|-----------|--------|
| `/content-seo` | LISTICLE, HOW-TO, SKYSCRAPER, PILLAR | `draft.md` |
| `/content-ai` | FAQ-FIRST (AI Overviews) | `draft.md` |
| `/content-sales` | AIDA, PAS, BAB, PASTOR | `sales-{slug}.md` |
| `/content-story` | STAR, HERO'S JOURNEY | `story-{slug}.md` |
| `/content-product` | FAB, INVERTED PYRAMID | `product-{slug}.md` |
| `/content-video` | QUEST (TikTok/Reels/Shorts) | `script-{slug}.md` |
| `/content-headline` | 4U scoring | đánh giá + alternatives |
| `/content-intro` | APP (3 variants) | mở bài thay thế |

### Agents (điều phối tự động)

| Agent | Chức năng |
|-------|-----------|
| `seo-writer` | research → write (2 bước trong 1) |
| `seo-auditor` | audit → improve loop → ảnh → export |
| `seo-batch` | Đọc Google Sheet → pipeline tự động → cập nhật Sheet |
| `seo-review` | QA report card A–F cho 1 bài |
| `seo-progress` | Dashboard tiến độ toàn bộ bài viết |

---

## Bài viết mẫu (20 bài, 5 category)

| Category | Số bài | Điểm trung bình |
|----------|--------|-----------------|
| social-media | 11 | 89/100 |
| suc-khoe | 4 | 89/100 |
| bat-dong-san | 2 | 80/100 |
| digital-marketing | 2 | 85/100 |
| gia-dung | 1 | 88/100 |

Xem danh sách đầy đủ tại [content-index.md](content-index.md).

---

## Cấu trúc thư mục

```
seo_content/
├── .claude/
│   ├── agents/          # 5 agents điều phối pipeline
│   └── skills/          # 20 skills SEO + content
├── profiles/
│   ├── default.example.json   # Template cấu hình (commit được)
│   └── default.json           # Cấu hình thật (gitignore)
├── checklist.md         # Checklist 8 phase audit đầy đủ
├── content-index.md     # Index bài viết + internal link map
├── CLAUDE.md            # Hướng dẫn đầy đủ cho Claude Code
├── _scripts/            # Utilities: batch, Drive upload, export
└── output/
    └── {category}/
        └── {slug}/
            ├── draft.md               # Bài viết Markdown
            ├── research.md            # Research brief
            ├── audit.md + audit.json  # Báo cáo điểm
            ├── export-{slug}.docx     # File Word sẵn sàng CMS
            ├── images/                # Ảnh diagram/chart
            └── _scripts/              # preprocess + convert scripts
```

---

## Thang điểm audit

| Điểm | Ý nghĩa |
|------|---------|
| 90–100 | Xuất sắc — sẵn sàng đăng |
| 75–89 | Tốt — chỉnh nhỏ trước khi đăng |
| 60–74 | Trung bình — cần cải thiện |
| < 60 | Yếu — nên viết lại |
