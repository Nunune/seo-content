---
name: seo-progress
description: |
  Giám sát tiến độ toàn bộ content pipeline: đọc content-index, scan output/,
  phân loại từng bài theo giai đoạn (research/viết/audit/export/review), hiển thị
  dashboard tổng quan và flag bài cần xử lý ưu tiên.
  Trigger: "tiến độ content", "progress", "giám sát content", "dashboard content",
  "bài nào chưa xong", "tổng quan bài viết", "báo cáo tiến độ", "bài nào cần làm",
  "content status", "xem tiến độ", "pipeline status", "theo dõi bài", "review tiến độ",
  "kiểm tra tiến độ", "bài nào đang làm", "update tiến độ".
argument-hint: [--category slug] [--stage 0|1|2|3|4|5] [--flag-low 75] [--save]
allowed-tools: [Read, Glob, Write]
---

# SEO Progress — Giám Sát Tiến Độ Content Pipeline

Quét toàn bộ `output/` và `content-index.md`, phân loại từng bài theo giai đoạn sản xuất,
hiển thị dashboard tổng quan, flag bài cần xử lý ưu tiên.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--category slug` — tùy chọn: chỉ xem 1 category (VD: `digital-marketing`)
- `--stage N` — tùy chọn: chỉ lọc bài ở giai đoạn N (0-5)
- `--flag-low N` — điểm audit cần flag là "cần improve" (mặc định: **75**)
- `--save` — tùy chọn: lưu report ra file `output/_shared/progress-{YYYYMMDD}.md`

---

## Các Giai Đoạn Sản Xuất

| Stage | Tên | Điều kiện |
|-------|-----|-----------|
| 0 | Chưa bắt đầu | Không có file nào trong slug folder |
| 1 | Research xong | `research.md` tồn tại |
| 2 | Draft xong | `draft.md` tồn tại |
| 3 | Audit xong | `audit.json` tồn tại |
| 4 | Export xong | `export-{slug}.docx` tồn tại |
| 5 | QA xong | `review.md` tồn tại |

*Giai đoạn được tính theo file cao nhất tồn tại — bài có cả 5 files = Stage 5.*

---

## Bước 1 — Thu Thập Dữ Liệu

### 1A. Đọc Content Index

Đọc `D:\Nunu-Claude\seo_content\content-index.md`.

Trích xuất từ bảng index:
- `slug` (từ cột slug hoặc cột đầu)
- `category`
- `keyword`
- `score` (điểm audit nếu có — thường ở cột "Điểm")

Nếu không có `content-index.md` → vẫn tiếp tục bằng cách scan thư mục (Bước 1B).

### 1B. Scan Thư Mục Output

Dùng Glob tool để tìm tất cả `draft.md` trong output:
```
D:\Nunu-Claude\seo_content\output\**\draft.md
```

Từ mỗi path, trích xuất:
- `category` = component thứ 2 của path (sau `output/`)
- `slug` = component thứ 3

Kết hợp với data từ content-index (nếu có). Nếu slug có trong index → dùng keyword và score từ index. Nếu slug chỉ có trong folder mà không có trong index → đánh dấu "chưa index".

### 1C. Lọc theo --category (nếu có)

Nếu `--category` được chỉ định → chỉ giữ lại các bài có `category == {--category}`.

---

## Bước 2 — Phân Loại Từng Bài

Với mỗi `{slug}` đã thu thập, kiểm tra file tồn tại:

```
article_dir = D:\Nunu-Claude\seo_content\output\{category}\{slug}\
```

Dùng Read tool thử đọc 1 dòng đầu của từng file:
- `research.md` → exists/missing
- `draft.md` → exists/missing
- `audit.json` → exists/missing (nếu exists → đọc `total_score` và `target`)
- `export-{slug}.docx` → exists/missing (dùng Glob: `output/{category}/{slug}/export-*.docx`)
- `review.md` → exists/missing

**Xác định stage:**
- Stage 5: có `review.md`
- Stage 4: có `export-*.docx` (không có review.md)
- Stage 3: có `audit.json` (không có export)
- Stage 2: có `draft.md` (không có audit)
- Stage 1: có `research.md` (không có draft)
- Stage 0: không có file nào

**Xác định trạng thái đặc biệt:**
- `NEEDS_IMPROVE`: Stage 3+ VÀ `total_score < --flag-low`
- `NOT_INDEXED`: slug không có trong content-index.md
- `STALE`: draft.md tồn tại nhưng không có audit.json sau >7 ngày (kiểm tra bằng timestamp nếu có thể — nếu không thể thì bỏ qua)

---

## Bước 3 — Tổng Hợp và Hiển Thị Dashboard

### Header

```
=== SEO PROGRESS DASHBOARD ===
Date     : {YYYY-MM-DD HH:MM}
Scope    : {All categories / category: {name}}
Articles : {total} bài

Giai đoạn:
  Stage 0 — Chưa bắt đầu : {n} bài
  Stage 1 — Research xong : {n} bài
  Stage 2 — Draft xong    : {n} bài
  Stage 3 — Audit xong    : {n} bài
  Stage 4 — Export xong   : {n} bài  ← Sẵn sàng đăng
  Stage 5 — QA xong       : {n} bài  ← Đã review

Cần chú ý:
  ⚠️  Cần improve (score < {flag_low}): {n} bài
  ❓  Chưa index trong content-index.md: {n} bài
```

### Bảng Chi Tiết Theo Category

Nhóm bài theo `category`, sắp xếp trong mỗi category: Stage cao → thấp, score cao → thấp.

```
─── {CATEGORY} ({n} bài) ──────────────────────────────────────
  {slug}
    Stage: {n} ({tên stage}) | Score: {score}/100 | {flags}
  ...
```

**Flags hiển thị:**
- `⚠️ NEEDS IMPROVE` — score < flag_low
- `✅ READY` — Stage 4+ và score ≥ flag_low
- `❓ NOT INDEXED` — chưa có trong content-index.md
- `📋 QA DONE` — Stage 5

### Priority Queue

Liệt kê tối đa 5 bài cần xử lý ngay (theo thứ tự ưu tiên):

```
=== VIỆC CẦN LÀM (TOP 5) ===

1. [{category}/{slug}]
   → {lý do cụ thể: "Stage 2 — chưa audit", "Score 68/100 — cần improve", v.v.}
   → Lệnh: /seo-{action} --{args}

2. ...
```

**Logic ưu tiên:**
1. Bài Stage 3 với `score < flag_low` → cần `/seo-improve`
2. Bài Stage 2 (có draft, chưa audit) → cần `/seo-audit`
3. Bài Stage 1 (có research, chưa draft) → cần `/seo-write`
4. Bài Stage 4 (export xong, chưa QA) → cần `/seo-review`
5. Bài Stage 3, score đạt nhưng chưa export → cần `/seo-export`

**Gợi ý lệnh cụ thể cho mỗi bài:**
```
/seo-improve --draft output/{category}/{slug}/draft.md --keyword "{keyword}" --target 85
/seo-audit   --file output/{category}/{slug}/draft.md --keyword "{keyword}"
/seo-write   --keyword "{keyword}" --category {category} --research output/{category}/{slug}/research.md
/seo-review  --keyword "{keyword}" --category {category} --slug {slug}
/seo-export  --draft output/{category}/{slug}/draft.md
```

---

## Bước 4 — Lưu File (nếu --save)

Nếu `--save` được chỉ định → lưu report đầy đủ ra:
```
D:\Nunu-Claude\seo_content\output\_shared\progress-{YYYYMMDD}.md
```

Format file lưu:

```markdown
# Content Progress Report

**Date:** {YYYY-MM-DD}
**Scope:** {All / category: {name}}

## Tổng quan

| Stage | Tên | Số bài |
|-------|-----|--------|
| 0 | Chưa bắt đầu | {n} |
| 1 | Research xong | {n} |
| 2 | Draft xong | {n} |
| 3 | Audit xong | {n} |
| 4 | Export xong | {n} |
| 5 | QA xong | {n} |
| **Tổng** | | **{total}** |

**Cần improve (score < {flag_low}):** {n} bài
**Sẵn sàng đăng (Stage 4+ và score ≥ {flag_low}):** {n} bài

---

## Chi tiết

| Category | Slug | Stage | Score | Flags |
|----------|------|-------|-------|-------|
| {cat} | {slug} | {n} — {tên} | {score}/100 | {flags} |
| ... | | | | |

---

## Việc cần làm

{danh sách priority queue với lệnh cụ thể}
```

---

## Xử Lý Edge Cases

- **Slug trong index nhưng không có thư mục:** Hiển thị Stage 0 (chưa bắt đầu).
- **Slug có thư mục nhưng không có file nào:** Stage 0.
- **audit.json tồn tại nhưng không đọc được score:** Stage 3, score = "N/A".
- **Nhiều export file (re-export nhiều lần):** Lấy file mới nhất — dùng Glob `export-*.docx`.
- **content-index.md không tồn tại:** Chạy hoàn toàn dựa vào Glob scan, không có keyword info.
