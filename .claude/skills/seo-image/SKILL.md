---
name: seo-image
description: |
  Tìm ảnh và tạo ảnh minh họa cho bài viết SEO từ các comment <!-- [ẢNH] --> trong draft.
  Kích hoạt khi user yêu cầu "tìm ảnh", "làm ảnh", "tạo ảnh bài viết", "seo image",
  "image cho bài", "xử lý ảnh draft", "ảnh seo", "tạo diagram", "tạo chart bài viết",
  "cần ảnh cho bài", "xử lý ảnh", "làm hình minh họa".
argument-hint: --draft output/draft_{slug}.md [--type diagram|chart|stock|screenshot|all]
allowed-tools: [WebSearch, WebFetch, Read, Write]
---

# SEO Image — Tìm & Tạo Ảnh Cho Bài Viết

Đọc file draft, tìm tất cả comment `<!-- [ẢNH] -->`, phân loại theo type, rồi xử lý từng ảnh:
sinh Mermaid/Chart.js code cho ảnh có thể tạo, tìm stock photo trên Unsplash/Pexels,
viết hướng dẫn chụp screenshot thủ công. Output là manifest đầy đủ + file code sẵn dùng.

## Arguments

Parse arguments:
- `--draft path` — **BẮT BUỘC**: đường dẫn file draft Markdown cần xử lý ảnh
- `--type diagram|chart|stock|screenshot|all` — lọc chỉ xử lý 1 loại (mặc định: all)

Nếu không có `--draft`, hỏi user đường dẫn trước khi tiếp tục.

## Quy trình thực hiện

### Bước 1 — Đọc draft và trích xuất image blocks

Dùng Read tool đọc toàn bộ file draft.

Tìm tất cả block `<!-- [ẢNH]`. Với mỗi block, trích xuất:
- `Mô tả` — nội dung mô tả ảnh cần tạo
- `Alt text` — text thay thế cho ảnh (đã có sẵn)
- `File name` — tên file WebP gợi ý
- `Kỹ thuật` — width × height từ dòng `width="X" height="Y"`

Đếm tổng số image blocks tìm được. Nếu không tìm thấy block nào, thông báo và dừng.

### Bước 2 — Phân loại từng ảnh

Đọc từ khóa trong field `Mô tả` để phân loại:

- **`diagram`**: chứa "sơ đồ", "quy trình", "flow", "diagram", "cycle", "vòng tròn", "mindmap", "các bước", "so sánh cấu trúc"
- **`chart`**: chứa "biểu đồ", "chart", "graph", "tăng trưởng", "xu hướng", "thống kê", "so sánh số liệu", "market share", "phần trăm"
- **`screenshot`**: chứa "screenshot", "giao diện", "màn hình", "UI", "interface", "demo", "ví dụ công cụ", "phần mềm"
- **`stock`**: tất cả còn lại — ảnh minh họa khái niệm, con người, thiên nhiên, văn phòng

Nếu `--type` được chỉ định, bỏ qua các ảnh không thuộc type đó.

### Bước 3 — Tạo slug và thư mục output

Tạo slug từ file draft (lấy phần `{slug}` từ `draft_{slug}.md`).

Output files:
- Manifest: `D:\Nunu-Claude\seo_content\output\images_{slug}.md`
- File con: `D:\Nunu-Claude\seo_content\output\images\{slug}\`

### Bước 4 — Xử lý từng ảnh theo loại

#### Loại `diagram` — Sinh Mermaid code + gợi ý Canva

**Phân tích nội dung:**
Đọc section bài viết xung quanh comment ảnh để hiểu:
- Các thành phần/bước cần hiển thị
- Mối quan hệ giữa chúng (tuần tự, vòng tròn, phân nhánh, so sánh)
- Số lượng items

**Chọn Mermaid diagram type:**
- Quy trình tuần tự (3–8 bước) → `flowchart LR` hoặc `flowchart TD`
- Vòng tròn / cycle → `flowchart LR` với arrows quay lại
- So sánh / phân nhánh → `flowchart TD` với nhánh
- Phân cấp khái niệm → `graph TD`
- Thống kê / tỷ lệ → `pie`

**Viết Mermaid code** đầy đủ với:
- Tiêu đề rõ ràng
- Node label bằng tiếng Việt (ngắn gọn, ≤ 30 ký tự/node)
- Styling cơ bản (`style NodeID fill:#...,stroke:#...`)
- Màu sắc: xanh lam `#3B82F6` cho node chính, xanh lá `#10B981` cho kết quả, vàng `#F59E0B` cho highlight

**Lưu file:** `D:\Nunu-Claude\seo_content\output\images\{slug}\diagram_{n}.md`
Nội dung file chỉ chứa code block Mermaid, không gì khác:
```
```mermaid
[code]
```
```

**Gợi ý Canva template:**
Dựa trên loại diagram, gợi ý 1–2 template cụ thể:
- Quy trình vòng tròn 6 bước → tìm "Circular Process Infographic" trên Canva
- Timeline / flow → tìm "Process Flow Infographic" hoặc "Timeline Infographic"
- So sánh 2 loại → tìm "Comparison Infographic"
- Mind map → tìm "Mind Map Diagram"
Ghi kèm: màu brand NuNu gợi ý: xanh `#3B82F6`, text trắng, nền trắng.

#### Loại `chart` — Sinh Chart.js HTML

**Phân tích dữ liệu:**
Đọc bài viết để lấy số liệu cụ thể cần visualize (năm, con số, nguồn).
Nếu không tìm thấy số liệu cụ thể, dùng dữ liệu minh họa với chú thích "dữ liệu minh họa".

**Chọn Chart type:**
- Dữ liệu theo thời gian (năm/tháng) → `line`
- So sánh các hạng mục → `bar` (ngang nếu ≥ 6 items)
- Tỷ lệ phần trăm → `doughnut` hoặc `pie`
- So sánh 2 chiều → `bar` grouped

**Sinh HTML file tự chứa** với:
- Chart.js CDN từ `https://cdn.jsdelivr.net/npm/chart.js`
- Kích thước canvas khớp với `Kỹ thuật` block (width × height)
- Title bằng tiếng Việt
- Màu sắc nhất quán: `#3B82F6` (xanh), `#10B981` (xanh lá), `#F59E0B` (vàng), `#EF4444` (đỏ)
- Font: Arial, 14px, màu `#374151`
- Background trắng `#FFFFFF`
- Padding 20px để không bị crop khi screenshot
- `responsive: false` để giữ đúng kích thước

**Lưu file:** `D:\Nunu-Claude\seo_content\output\images\{slug}\chart_{n}.html`

#### Loại `screenshot` — Hướng dẫn chụp thủ công

Không thể tự động hóa. Viết hướng dẫn chi tiết gồm:
1. URL cụ thể cần mở (nếu biết — ví dụ: Semrush → `semrush.com/analytics/overview/`)
2. Thao tác cần làm (đăng nhập, navigate đến tính năng X, nhập keyword Y)
3. Vùng cần capture (mô tả rõ: "toàn bộ keyword cluster panel", "chỉ phần top metrics")
4. Tool capture gợi ý: Snipping Tool (Windows+Shift+S), Lightshot, hay trực tiếp Chrome DevTools
5. Crop về đúng kích thước trong `Kỹ thuật` block

#### Loại `stock` — Tìm Unsplash/Pexels

**Tạo search query:**
Rút gọn `Mô tả` thành 3–5 từ khóa tiếng Anh phù hợp với Unsplash/Pexels.
Ví dụ: "Sơ đồ quy trình SEO với AI" → query: "ai technology seo digital marketing"

**Tìm kiếm:**
Thực hiện 2 WebSearch:
1. `site:unsplash.com {query} free photo`
2. `site:pexels.com {query} free photo`

**WebFetch để lấy URL ảnh thực:**
Fetch trang kết quả Unsplash: `https://unsplash.com/s/photos/{query-với-dấu-gạch}`
Trích xuất 2–3 URL ảnh cụ thể (img src hoặc link trang ảnh cụ thể).

Fetch trang Pexels: `https://www.pexels.com/search/{query}/`
Trích xuất 1–2 URL ảnh.

**Cung cấp kết quả:**
- 3–5 lựa chọn: URL trang ảnh + mô tả ngắn + tên tác giả + license (CC0)
- Ưu tiên ảnh ngang (landscape) nếu width > height trong `Kỹ thuật`
- Ghi rõ: "Tất cả ảnh Unsplash/Pexels miễn phí thương mại, không cần attribution (nhưng nên credit)"

### Bước 5 — Viết manifest tổng hợp

Lưu file `D:\Nunu-Claude\seo_content\output\images_{slug}.md`.

## Định dạng file images_{slug}.md

```markdown
# Image Plan: {Tiêu đề bài / Slug}

**Draft:** {draft path}
**Tổng số ảnh:** {n}
**Ngày tạo:** {YYYY-MM-DD}

---

## Tóm tắt

| # | File name | Loại | Kích thước | Trạng thái |
|---|-----------|------|-----------|-----------|
| 1 | {filename}.webp | Diagram | {w}×{h} | ✅ Mermaid + Canva guide |
| 2 | {filename}.webp | Chart | {w}×{h} | ✅ Chart.js HTML sẵn sàng |
| 3 | {filename}.webp | Screenshot | {w}×{h} | 📋 Hướng dẫn thủ công |
| 4 | {filename}.webp | Stock Photo | {w}×{h} | 🔗 3 lựa chọn |

---

## Ảnh {n} — {Mô tả ngắn}

**Loại:** {Diagram / Chart / Screenshot / Stock Photo}
**File:** `{filename}.webp` · **Kích thước:** {w}×{h}
**Alt text:** `{alt text}`

{Nội dung xử lý theo loại — xem format mẫu bên dưới}

---

## Hướng dẫn convert sang WebP (áp dụng cho tất cả ảnh)

**Cách 1 — Online (không cần cài gì):**
Dùng https://squoosh.app → kéo ảnh vào → chọn định dạng "WebP" → Quality 85 → Download

**Cách 2 — Windows CLI (libwebp):**
```
cwebp input.jpg -o output.webp -q 85
```
Cài libwebp: `winget install libwebp`

**Cách 3 — PowerShell batch convert:**
```powershell
Get-ChildItem *.jpg | ForEach-Object {
  cwebp $_.FullName -o ($_.BaseName + ".webp") -q 85
}
```
```

### Nội dung mẫu cho từng loại

**Diagram:**
```markdown
### Con đường A — Mermaid (nhanh, miễn phí)

Xem code tại: `images/{slug}/diagram_{n}.md`

**Cách render:**
1. Mở https://mermaid.live
2. Paste toàn bộ code từ file trên
3. Điều chỉnh nếu cần → Click "Download PNG"
4. Đổi tên: `{filename}.png` → convert sang WebP

### Con đường B — Canva (đẹp hơn cho production)

**Template gợi ý:** Tìm "{Tên template cụ thể}" trên canva.com
**Nội dung cần điền:** {liệt kê từng item/bước cần điền}
**Màu sắc brand:** Xanh chính `#3B82F6` · Text trắng `#FFFFFF` · Nền `#F9FAFB`
**Kích thước export:** {w}×{h}px → Download PNG → convert sang WebP

### Preview code Mermaid:

```mermaid
{code đầy đủ}
```
```

**Chart:**
```markdown
### Cách tạo ảnh từ file HTML

File đã tạo: `images/{slug}/chart_{n}.html`

**Bước 1:** Mở file trong Chrome/Edge
**Bước 2:** Mở DevTools (F12) → Console → gõ:
```javascript
document.querySelector('canvas').toBlob(b => {
  const a = document.createElement('a');
  a.href = URL.createObjectURL(b);
  a.download = '{filename}.png';
  a.click();
}, 'image/png');
```
**Bước 3:** Lưu PNG → convert sang WebP

**Dữ liệu dùng trong chart:**
{Bảng dữ liệu đã dùng để tạo chart}
```

**Screenshot:**
```markdown
### Hướng dẫn chụp màn hình

**URL:** {URL cụ thể}
**Thao tác:** {bước 1, 2, 3...}
**Vùng capture:** {mô tả vùng cần chụp}
**Tool gợi ý:** Windows Snipping Tool (Windows+Shift+S) → chọn vùng → Copy → Paste vào Paint → Lưu PNG
**Crop về:** {w}×{h}px — dùng Paint hoặc IrfanView
**Đổi tên:** `{filename}.png` → convert sang WebP
```

**Stock Photo:**
```markdown
### Lựa chọn ảnh (CC0 — miễn phí thương mại)

| # | Preview | Tác giả | Kích thước gốc | Link tải |
|---|---------|---------|--------------|---------|
| 1 | {Mô tả ảnh} | {Tên} | {kích thước} | [Unsplash]({URL}) |
| 2 | {Mô tả ảnh} | {Tên} | {kích thước} | [Unsplash]({URL}) |
| 3 | {Mô tả ảnh} | {Tên} | {kích thước} | [Pexels]({URL}) |

**Cách tải:** Click link → "Download free" → đổi tên → convert WebP
**Credit gợi ý (không bắt buộc):** "Ảnh: {Tên tác giả} / Unsplash"
```

## Thông báo hoàn thành

Sau khi lưu tất cả file, báo cáo:
- Đường dẫn manifest: `seo_content/output/images_{slug}.md`
- Danh sách file con đã tạo (diagram, chart HTML)
- Bảng tóm tắt: # ảnh × loại
- Bước tiếp theo: "Tạo ảnh → upload CMS → chạy lại `/seo-audit` để kiểm tra GĐ4 Media"
