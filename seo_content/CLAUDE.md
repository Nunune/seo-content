# SEO Content Workspace

Bộ công cụ viết và tối ưu nội dung SEO theo chuẩn Google 2025-2026 (E-E-A-T, People-first, GEO/AI Search).

## Slash commands

```
/seo-pipeline  --keyword "từ khóa" --category slug [--target 85] [--max-iter 3] [--competitor URLs] [--author "Tên"] [--lang vi|en]
/seo-research  --keyword "từ khóa" --category slug-linh-vuc [--competitor URL1 URL2...] [--lang vi|en]
/seo-write     --keyword "từ khóa" --category slug-linh-vuc [--research output/{cat}/{slug}/research.md] [--author "Tên, Chức danh"]
/seo-audit     --file output/{category}/{slug}/draft.md | --url https://example.com [--keyword "từ khóa"]
/seo-improve   --draft output/{category}/{slug}/draft.md --keyword "từ khóa" [--target 85] [--max-iter 3]
/seo-image     --draft output/{category}/{slug}/draft.md [--type diagram|chart|stock|screenshot|all]
/seo-webp      --slug {slug} --category {slug-linh-vuc} | --input path/ [--quality 85] [--keep-original]
/seo-export    --draft output/{category}/{slug}/draft.md [--font Arial|Times]
/seo-pagespeed --url https://example.com [--strategy mobile|desktop|both]
```

## Sub-agents (pipeline điều phối)

Agents tự động chuỗi nhiều skill với 1 lệnh duy nhất — không cần gọi từng skill riêng lẻ:

| Agent | Cú pháp | Skills được gọi |
|-------|---------|-----------------|
| **seo-writer** | `--keyword "X" --category slug [--competitor URLs] [--author "Tên, Chức danh"]` | seo-research → seo-write |
| **seo-auditor** | `--draft path --keyword "X" [--target 85] [--max-iter 3]` | seo-audit (baseline) → seo-improve |

### Pipeline 2-agent hoàn chỉnh (từ từ khóa đến .docx)

```
# Bước 1 — Viết bài
"viết bài SEO cho từ khóa 'content marketing là gì', category digital-marketing"
→ seo-writer chạy → research.md + draft.md

# Bước 2 — Audit và xuất
"audit và cải thiện bài content-marketing-la-gi --target 85"
→ seo-auditor chạy → draft cải thiện + audit.json + export-*.docx + README.md
```

> **Phân biệt:** `/seo-audit` (skill) = chỉ chấm điểm. `seo-auditor` (agent) = audit + improve loop + ảnh + export.

## Quy trình chuẩn

> **Nhanh hơn:** Dùng `/seo-pipeline --keyword "X" --category slug` để chạy toàn bộ trong 1 lệnh.

```
/seo-research → /seo-write → /seo-audit → /seo-improve
                                                  ↓ (tự động, không cần thêm lệnh)
                                           loop fix đến score ≥ 85
                                                  ↓
                                           tạo ảnh (generate_images.py)
                                                  ↓
                                           xuất export-{slug}.docx (ảnh nhúng)
                                                  ↓
                                           tạo README.md (score + TODO + tips)
                                                  ↓
                                           → /seo-pagespeed (sau khi đăng lên live)
```

**Quy tắc cốt lõi:** Mỗi từ khóa chạy đến khi `audit score ≥ 85` thì mới xuất file.
`/seo-improve` xử lý toàn bộ: fix loop → ảnh → docx → README. Không cần gọi `/seo-image` hay `/seo-export` riêng trừ khi muốn re-run độc lập.

### Chi tiết từng bước

1. **Research**: phân tích SERP, đối thủ, content gap → `output/{category}/{slug}/research.md`
2. **Write**: viết bài hoàn chỉnh E-E-A-T + GEO → `output/{category}/{slug}/draft.md`
3. **Audit**: chấm điểm 8 giai đoạn (0-100) → `output/{category}/{slug}/audit.md` + `audit.json`
4. **Improve** _(all-in-one)_:
   - Vòng lặp fix đến `score ≥ target` (mặc định 85), tối đa 3 vòng
   - Tạo ảnh tự động (matplotlib diagram/chart; placeholder cho screenshot/stock)
   - Xuất `export-{slug}.docx` với ảnh đã nhúng
   - Tạo `README.md` — điểm audit + TODO còn lại + tips tối ưu
5. **WebP** _(tuỳ chọn)_: convert ảnh PNG → WebP trước khi upload CMS
6. **PageSpeed** _(sau khi đăng)_: kiểm tra Core Web Vitals → `output/_shared/pagespeed/{slug}.md`

## Cấu trúc

```
seo_content/
  .claude/
    skills/
      seo-research/SKILL.md    # Nghiên cứu từ khóa & SERP       ← INPUT
      seo-write/SKILL.md       # Viết bài chuẩn SEO               ← INPUT
      seo-audit/SKILL.md       # Chấm điểm content                ← INPUT
      seo-improve/SKILL.md     # Auto-fix loop đến điểm mục tiêu   ← INPUT
      seo-image/SKILL.md       # Tìm & tạo ảnh cho bài             ← INPUT
      seo-webp/SKILL.md        # Convert PNG/JPG sang WebP          ← INPUT
      seo-export/SKILL.md      # Xuất .docx sẵn sàng upload CMS    ← INPUT
      seo-pagespeed/
        SKILL.md               # Kiểm tra Core Web Vitals          ← INPUT
        thresholds.json        # Ngưỡng GOOD/NEEDS IMPROVEMENT/POOR ← INPUT
  profiles/
    default.json               # Thông tin tác giả & thương hiệu   ← INPUT
  checklist.md                 # Checklist 8 giai đoạn đầy đủ      ← INPUT
  output/                      # ← TẤT CẢ KẾT QUẢ TỪ SKILL
    {category}/                # VD: digital-marketing, gia-dung, bat-dong-san, social-media
      {slug}/                  # VD: ung-dung-ai-vao-seo, su-dung-may-lanh-tiet-kiem-dien
        README.md              # ⭐ Tóm tắt: điểm audit + TODO + tips tối ưu  ← ĐỌC ĐÂY TRƯỚC
        draft.md               # Bài viết hoàn chỉnh (Markdown)
        research.md            # Research brief (nếu có)
        audit.md               # Báo cáo audit chi tiết dạng đọc
        audit.json             # Điểm số cấu trúc JSON (dùng bởi seo-improve)
        export-{slug}.docx     # File Word sẵn sàng upload CMS (ảnh đã nhúng)
        images.md              # Manifest ảnh + hướng dẫn tạo thủ công
        images/                # Ảnh đã tạo (PNG, WebP)
          *.png / *.webp       # Files ảnh thực (matplotlib / screenshot)
        _scripts/              # Scripts tái sử dụng
          generate_images.py   # Tạo ảnh diagram/chart bằng matplotlib
          preprocess.py        # Chuyển <!-- [ẢNH] --> → ![alt](path)
          convert.py           # Markdown → .docx (python-docx)
    _shared/                   # Dùng chung, không gắn bài cụ thể
      pagespeed/               # Báo cáo Core Web Vitals theo URL
        {slug}.md
        {slug}.json
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
# ── FULL CHAIN (từ từ khóa đến file xuất) ──────────────────────────────
/seo-research --keyword "học lái xe ô tô" --category giao-thong
/seo-write    --keyword "học lái xe ô tô" --category giao-thong \
              --research output/giao-thong/hoc-lai-xe-o-to/research.md
/seo-improve  --draft output/giao-thong/hoc-lai-xe-o-to/draft.md \
              --keyword "học lái xe ô tô"
# → Tự động: fix loop → score ≥ 85 → ảnh → docx → README.md

# ── CHỈ VIẾT (đã có research) ──────────────────────────────────────────
/seo-write --keyword "cách trồng rau tại nhà" --category nong-nghiep

# ── CHỈ AUDIT (kiểm tra bài hiện tại) ─────────────────────────────────
/seo-audit --file output/giao-thong/hoc-lai-xe-o-to/draft.md

# ── IMPROVE VỚI TARGET CAO HƠN ────────────────────────────────────────
/seo-improve --draft output/giao-thong/hoc-lai-xe-o-to/draft.md \
             --keyword "học lái xe ô tô" --target 90 --max-iter 5

# ── SAU KHI ĐĂNG BÀI ─────────────────────────────────────────────────
/seo-pagespeed --url https://example.com/hoc-lai-xe-o-to --strategy both
```

## Cấu trúc output mẫu sau khi chạy full chain

```
output/giao-thong/hoc-lai-xe-o-to/
  README.md                        ← đọc đây để biết trạng thái bài
  draft.md                         ← bài viết Markdown
  research.md                      ← research brief
  audit.md + audit.json            ← báo cáo điểm chi tiết
  export-hoc-lai-xe-o-to.docx      ← file Word với ảnh nhúng
  images/
    so-do-quy-trinh-hoc-lai-xe.png
    bang-so-sanh-truong-lx.png
  _scripts/
    generate_images.py
    preprocess.py
    convert.py
```
*API Key mình không Up*
