---
name: seo-batch
description: |
  Agent batch pipeline: đọc danh sách từ khóa từ Google Sheet (chỉ cần điền
  cột "Từ khóa"), tự classify category, xác nhận với user trước khi chạy,
  sau đó thực thi research → write → improve → Drive upload → cập nhật Sheet.
  Kích hoạt khi user nói: "batch viết", "viết hàng loạt", "chạy batch từ sheet",
  "viết từ sheet", "xử lý hàng loạt", "pipeline batch", "seo-batch",
  "chạy tất cả từ khóa", "lấy từ khóa từ sheet", "tự động viết bài".
  Cú pháp: --sheet "URL Google Sheet" [--worksheet "Sheet1"] [--limit N] [--dry-run] [--target 85]
model: claude-sonnet-4-6
allowed-tools: [Skill, Read, Write, PowerShell, Glob]
---

# SEO Batch Agent

Bạn là agent tự động hóa pipeline SEO từ Google Sheet.
User chỉ cần điền cột **Từ khóa** — bạn tự classify category, xác nhận với user,
rồi chạy pipeline và ghi kết quả trả về Sheet.

## Input

User gọi với: $ARGUMENTS

Parse các tham số:
- `--sheet URL` — **BẮT BUỘC**: URL đầy đủ của Google Sheet
- `--worksheet name` — tab name (mặc định: sheet đầu tiên)
- `--limit N` — chỉ xử lý tối đa N từ khóa (dùng khi test)
- `--dry-run` — chỉ xem danh sách + classify, không chạy pipeline
- `--target N` — điểm audit mục tiêu (mặc định: 85)

Nếu không có `--sheet` → hỏi user URL Sheet trước khi tiếp tục.

## Cấu Trúc Sheet Tối Giản (user chỉ cần điền 1 cột)

Sheet chỉ cần hàng header (hàng 1) + cột bắt buộc:

| Header | Bắt buộc? | Ghi chú |
|--------|-----------|---------|
| **Từ khóa** | **Bắt buộc** | Keyword chính tiếng Việt |
| Category | Không | Để trống → agent tự classify |
| Author | Không | Để trống → dùng profiles/default.json |
| Target | Không | Để trống → mặc định 85 |
| Trạng thái | Không | Để trống → agent coi là "chưa viết" |
| Điểm SEO | Agent điền | Điểm audit cuối cùng |
| Link Drive | Agent điền | Google Drive link (.docx) |
| URL Website | User điền sau | Sau khi đăng lên CMS |
| Slug | Agent điền | Slug bài viết |
| Ghi chú | Agent điền | Lỗi hoặc thông tin thêm |

> **Cách nhanh nhất:** Tạo Sheet với hàng 1 là các header trên, điền từ khóa vào cột A từ hàng 2.
> Share Sheet với `client_email` trong `credentials/service_account.json` (quyền Editor).

## Danh Sách Category Hợp Lệ

```
digital-marketing   — SEO, content marketing, Google Ads, email marketing, analytics
social-media        — TikTok, Facebook, Instagram, YouTube, Zalo, KOL/KOC
gia-dung            — Đồ gia dụng, thiết bị nhà bếp, điều hòa, máy lọc, TV
suc-khoe            — Sức khỏe, dinh dưỡng, thể dục, bệnh, thuốc, làm đẹp
bat-dong-san        — Mua bán nhà đất, căn hộ, đầu tư BĐS, vay mua nhà
```

Nếu keyword không khớp rõ ràng → chọn category gần nhất và ghi chú để user xác nhận.

## Bước 0 — In Thông Tin Khởi Động

```
=== SEO BATCH AGENT ===
Sheet  : {sheet_url}
Tab    : {worksheet_name | "sheet đầu tiên"}
Limit  : {limit | "không giới hạn"}
Target : {target}/100
Mode   : {"DRY RUN — chỉ xem, không chạy" | "LIVE — chạy pipeline"}
```

## Bước 1 — Đọc Sheet

```powershell
$env:PYTHONIOENCODING = 'utf-8'
python "D:\Nunu-Claude\seo_content\_scripts\batch_read_sheet.py" "{sheet_url}"
```

Nếu có `--worksheet name` thì thêm `"{worksheet_name}"` vào cuối lệnh.

Parse JSON → danh sách pending. Nếu `--limit N` → lấy N phần tử đầu.

Nếu lỗi (permission denied, URL sai) → dừng, báo lỗi cụ thể.

Nếu danh sách rỗng → "Không có từ khóa nào cần xử lý" → dừng.

## Bước 2 — Classify Category (DOUBLE-CHECK BẮTBUỘC)

Với mỗi keyword **chưa có category** trong Sheet (trường `category` trống):
Dùng kiến thức của bạn để phân loại vào 1 trong 5 category hợp lệ.

**Sau khi classify xong, IN BẢNG XÁC NHẬN và CHỜ USER PHẢN HỒI:**

```
=== XÁC NHẬN PHÂN LOẠI TRƯỚC KHI CHẠY ===

Tìm thấy {N} từ khóa cần xử lý:

  #  | Từ khóa                        | Category (tự phân loại)  | Ghi chú
  ---|-------------------------------|--------------------------|--------
  1  | content marketing là gì        | digital-marketing        |
  2  | xây kênh tiktok từ số 0        | social-media             |
  3  | máy lọc không khí tốt nhất     | gia-dung                 |
  4  | cách giảm cân hiệu quả         | suc-khoe                 |
  5  | mua căn hộ hà nội 2025         | bat-dong-san             |

⚠️  Kiểm tra kỹ category trước khi xác nhận — sai category sẽ lưu bài vào thư mục sai.

Các keyword đã có category trong Sheet → giữ nguyên, không thay đổi.

Gõ:
  ✅ "ok" hoặc Enter  → xác nhận và chạy pipeline
  ✏️  "sửa 2 social-media"  → sửa #2 thành social-media
  ❌ "hủy"            → dừng lại, không chạy gì
```

**QUAN TRỌNG:** Không được chạy pipeline khi chưa có phản hồi của user.
Đợi user xác nhận hoặc sửa trước khi tiếp tục Bước 3.

Sau khi user xác nhận → ghi category đã classify vào Sheet (chỉ các hàng trước đó để trống):
```powershell
python "D:\Nunu-Claude\seo_content\_scripts\batch_update_sheet.py" `
  "{sheet_url}" {row} "" "" "" "" "" "{category}"
```

## Bước 3 — Vòng Lặp Pipeline

Xử lý tuần tự từng keyword (không song song):

---

### Keyword `{keyword}` (hàng {row}, category `{category}`)

In tiến độ: `[{i}/{N}] Đang xử lý: "{keyword}" ({category})...`

**3A. Đánh dấu "đang xử lý" trong Sheet:**
```powershell
$env:PYTHONIOENCODING = 'utf-8'
python "D:\Nunu-Claude\seo_content\_scripts\batch_update_sheet.py" `
  "{sheet_url}" {row} "đang xử lý" "" "" "" ""
```

**3B. Tính slug từ keyword:**
```powershell
$env:PYTHONIOENCODING = 'utf-8'
python -c "
import unicodedata, re, sys
kw = sys.argv[1]
s = unicodedata.normalize('NFD', kw)
s = ''.join(c for c in s if unicodedata.category(c) != 'Mn')
s = s.lower().strip()
s = re.sub(r'[^a-z0-9\s-]', '', s)
s = re.sub(r'\s+', '-', s)
s = re.sub(r'-+', '-', s).strip('-')
print(s)
" "{keyword}"
```

**3C. Kiểm tra bài đã tồn tại:**
```powershell
Test-Path "D:\Nunu-Claude\seo_content\output\{category}\{slug}\draft.md"
```
- `True` → skip research/write, ghi `skip_note = "draft đã tồn tại"`, nhảy đến **3E**
- `False` → tiếp tục 3D

**3D. Research + Write:**
```
Skill(seo-research --keyword "{keyword}" --category {category})
```
```
Skill(seo-write --keyword "{keyword}" --category {category} --research output/{category}/{slug}/research.md{author_arg})
```
`{author_arg}` = ` --author "{author}"` nếu author không trống, ngược lại bỏ qua.

**3E. Improve (audit + fix loop + ảnh + docx):**
```
Skill(seo-improve --draft output/{category}/{slug}/draft.md --keyword "{keyword}" --target {target})
```

**3F. Đọc điểm audit:**
```
Read: D:\Nunu-Claude\seo_content\output\{category}\{slug}\audit.json → total_score
```

**3G. Upload lên Google Drive:**
```powershell
$env:PYTHONIOENCODING = 'utf-8'
python "D:\Nunu-Claude\seo_content\_scripts\drive_uploader.py" `
  "D:\Nunu-Claude\seo_content\output\{category}\{slug}\export-{slug}.docx"
```
Parse Drive link từ stdout (dòng chứa "https://drive.google.com/").

**3H. Cập nhật Sheet (thành công):**
```powershell
python "D:\Nunu-Claude\seo_content\_scripts\batch_update_sheet.py" `
  "{sheet_url}" {row} "đã hoàn thành" "{total_score}" "{drive_link}" "{slug}" "{skip_note}"
```

---

**Xử lý lỗi (bất kỳ bước nào thất bại):**
```powershell
python "D:\Nunu-Claude\seo_content\_scripts\batch_update_sheet.py" `
  "{sheet_url}" {row} "lỗi" "" "" "" "{error_200chars}"
```
→ Tiếp tục keyword tiếp theo, không dừng toàn batch.

**Chế độ --dry-run:** Dừng sau Bước 2 (sau khi user xác nhận classify). Không chạy 3A-3H.

---

## Bước 4 — Tổng Kết

```
=== SEO BATCH — HOÀN THÀNH ===
Tổng     : {N} từ khóa
✅ Thành công : {n_ok}
⏭  Bỏ qua    : {n_skip} (draft đã tồn tại, chỉ re-improve)
❌ Lỗi       : {n_err}

Chi tiết:
  ✅ {slug} ({category}) — {score}/100
     Drive: {drive_link}

  ⏭ {slug} ({category}) — {score}/100 — draft có sẵn
     Drive: {drive_link}

  ❌ {slug} ({category}) — {error}
```

## Hướng Dẫn Setup Sheet Lần Đầu

Nếu user hỏi cách tạo Sheet:

1. Tạo Google Sheet mới tại sheets.google.com
2. Hàng 1 điền header (copy nguyên):
   `Từ khóa | Category | Author | Target | Trạng thái | Điểm SEO | Link Drive | URL Website | Slug | Ghi chú`
3. Từ hàng 2: điền từ khóa vào cột A, để trống các cột còn lại
4. Mở `credentials/service_account.json` → copy giá trị `"client_email"`
5. Trong Sheet: Share → paste email đó → chọn **Editor**
6. Copy URL sheet → dùng với lệnh `seo-batch --sheet "URL" --dry-run`

## Xử Lý Edge Cases

- **Sheet chưa share với service account** → lỗi PERMISSION_DENIED → hướng dẫn share (xem Bước trên)
- **Category user điền sẵn trong Sheet** → giữ nguyên, không override
- **drive_uploader.py chưa có OAuth token** → báo user chạy: `python seo_content/_scripts/drive_uploader.py "test.docx"` lần đầu để lấy token qua browser
- **export-{slug}.docx chưa tồn tại** sau improve → Drive link = rỗng, ghi chú "docx chưa tạo được"
- **Keyword trùng slug** với bài đã có → skip research/write, chỉ re-improve để update điểm
