---
name: seo-export
description: |
  Xuất bài viết SEO từ file Markdown sang .docx sẵn sàng upload CMS.
  Tự động phát hiện pandoc hoặc python-docx, chèn ảnh thật nếu file tồn tại (kèm alt text),
  dùng placeholder nếu chưa có ảnh. Comment block SEO meta được loại bỏ khỏi bài.
  Kích hoạt khi user yêu cầu "xuất docx", "export bài viết", "tạo file word", "tạo doc",
  "seo export", "xuất word", "xuất bài", "export docx", "tạo .doc", "file word cho bài".
argument-hint: --draft output/{category}/{slug}/draft.md [--font Arial|Times]
allowed-tools: [Read, Write, Bash]
---

# SEO Export — Xuất Bài Viết Sang .docx

Chuyển đổi draft Markdown sang file Word (.docx) chuẩn — heading styles, bảng, ảnh embed với alt text,
loại bỏ comment block kỹ thuật (SEO meta, schema, TODO). Sẵn sàng upload thẳng lên CMS hoặc Google Docs.

## Arguments

Parse arguments:
- `--draft path` — **BẮT BUỘC**: đường dẫn file draft Markdown (ví dụ: `output/digital-marketing/ung-dung-ai-vao-seo/draft.md`)
- `--font Arial|Times` — font chữ body (mặc định: Arial)

Từ `--draft output/{category}/{slug}/draft.md`:
- `article_dir` = thư mục chứa draft (`output/{category}/{slug}/`)
- `images_dir` = `{article_dir}/images/`
- `scripts_dir` = `{article_dir}/_scripts/`

Nếu không có `--draft`, hỏi user trước khi tiếp tục.

## Quy trình thực hiện

### Bước 1 — Phát hiện và cài đặt tool

Chạy theo thứ tự ưu tiên:

```powershell
# Thử pandoc trước — PHẢI dùng PowerShell (Bash tool trả false positive trên Windows)
Get-Command pandoc -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
```

Nếu pandoc có → ghi nhận: dùng pandoc path.
Nếu pandoc không có → thử cài:
```powershell
winget install JohnMacFarlane.Pandoc --silent
```

Nếu winget thành công → dùng pandoc.
Nếu winget thất bại hoặc không có winget → chuyển sang python-docx:
```powershell
python -m pip install python-docx Pillow --quiet
```

Ghi nhận tool sẽ dùng: `pandoc` hoặc `python-docx`.

> **Lưu ý Windows:** Không dùng Bash tool để check pandoc — Bash chạy trong WSL và có thể trả "PANDOC_OK" dù pandoc không có trên Windows PATH. Luôn dùng PowerShell để check.

### Bước 2 — Đọc file đầu vào

Dùng Read tool đọc `--draft` file. Ghi nhận:
- Tiêu đề bài (H1, dòng bắt đầu bằng `# `)
- Slug (từ SEO Meta block hoặc tên file)

### Bước 3 — Xác định image paths

Kiểm tra ảnh: Với mỗi `<!-- [ẢNH] -->` block trong draft, lấy `File:` và kiểm tra trong `{article_dir}/images/` (WebP hoặc PNG hoặc JPG, thử tất cả extensions).

Ghi nhận: ảnh nào có sẵn (embed thật), ảnh nào chưa có (placeholder).

### Bước 4 — Pre-process Markdown

Viết Python script `{scripts_dir}/preprocess.py` và chạy để tạo file `{article_dir}/preprocessed.md`:

**Các biến đổi cần thực hiện:**

1. **Loại bỏ comment block kỹ thuật** (không phải ảnh):
   - `<!-- SEO Meta ... -->` → xóa hoàn toàn
   - `<!-- Author ... -->` → xóa
   - `<!-- Schema Markup ... -->` → xóa
   - `<!-- Internal Links ... -->` → xóa
   - `<!-- TODO ... -->` → xóa
   - `<!-- [TODO] ... -->` single-line → xóa

2. **Xử lý image block** `<!-- [ẢNH] ... -->`:
   - Trích xuất `Alt text`, `File name`
   - Nếu file ảnh TỒN TẠI: chuyển thành `![{alt text}]({image_path})`
   - Nếu file ảnh CHƯA CÓ: chuyển thành dòng text `> 📷 **[CHỖ NÀY CHÈN ẢNH: {file_name}]**`

3. **Dòng freshness** `> **Cập nhật:** ...` → giữ nguyên (sẽ render là blockquote)

4. **TL;DR block** (`> **TL;DR...**` + `> - ...`) → giữ nguyên

**Python script mẫu để write và execute:**

```python
import re, os, sys

draft_path = sys.argv[1]
output_path = sys.argv[2]
images_dir = sys.argv[3] if len(sys.argv) > 3 else ''

with open(draft_path, encoding='utf-8') as f:
    content = f.read()

result = []
lines = content.split('\n')
i = 0
skip_comment = False

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    # Detect start of comment block
    if stripped.startswith('<!--'):
        is_image_block = stripped.startswith('<!-- [ẢNH]')
        
        # Collect entire comment block
        block_lines = [line]
        if '-->' not in stripped:
            i += 1
            while i < len(lines) and '-->' not in lines[i]:
                block_lines.append(lines[i])
                i += 1
            if i < len(lines):
                block_lines.append(lines[i])
        
        block_text = '\n'.join(block_lines)
        
        if is_image_block:
            # Extract alt text and file name
            # NOTE: Alt text may or may not have quotes — handle both cases
            alt_match = re.search(r'Alt text:\s*"?([^"\n]+)"?', block_text)
            file_match = re.search(r'File name:\s*(\S+\.(?:webp|png|jpg|jpeg))', block_text)
            
            alt_text = alt_match.group(1).strip() if alt_match else 'image'
            file_name = file_match.group(1) if file_match else ''
            
            # Check if image file exists
            image_found = False
            image_path = ''
            if file_name and images_dir:
                for ext in ['', '.webp', '.png', '.jpg', '.jpeg']:
                    base = os.path.splitext(file_name)[0]
                    check_paths = [
                        os.path.join(images_dir, file_name),
                        os.path.join(images_dir, base + ext),
                    ]
                    for cp in check_paths:
                        if os.path.exists(cp):
                            image_found = True
                            image_path = cp
                            break
                    if image_found:
                        break
            
            if image_found:
                result.append(f'![{alt_text}]({image_path})')
            else:
                result.append(f'> 📷 **[CHỖ NÀY CHÈN ẢNH: {file_name}]**')
        # else: skip non-image comment block entirely
        
        i += 1
        continue

    result.append(line)
    i += 1

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print('Preprocessed:', output_path)
```

Lưu script, chạy bằng PowerShell:
```powershell
$base   = "D:\Nunu-Claude\seo_content\output\{category}\{slug}"
$shared = "D:\Nunu-Claude\seo_content\_scripts"
python "$base\_scripts\preprocess.py" "$base\draft.md" "$base\_preprocessed.md" "$base\images"
# Gắn README vào cuối (phụ lục hướng dẫn đăng bài)
python "$shared\append_readme.py" "$base\_preprocessed.md" "$base\README.md"
```

### Bước 5 — Chuyển đổi sang .docx

#### Con đường A — Pandoc (nếu có)

```powershell
$base = "D:\Nunu-Claude\seo_content\output\{category}\{slug}"
pandoc "$base\preprocessed.md" -o "$base\export.docx" --from markdown --to docx -V lang:vi --wrap=none
```

Pandoc tự động xử lý: headings, bold, italic, tables, images (nếu path hợp lệ).
Sau khi pandoc chạy xong, chuyển sang Bước 6.

#### Con đường B — python-docx (fallback)

Viết Python script `{scripts_dir}/convert.py` và execute:

```python
import re, sys, os
from io import BytesIO
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from PIL import Image as PILImage

# ---- CONFIG ----
FONT_NAME = 'Arial'   # hoặc 'Times New Roman' theo --font flag
FONT_SIZE_BODY = 11
FONT_SIZE_H1 = 18
FONT_SIZE_H2 = 15
FONT_SIZE_H3 = 13
COLOR_H1 = RGBColor(0x1D, 0x4E, 0xD8)   # xanh đậm
COLOR_H2 = RGBColor(0x1E, 0x40, 0xAF)
COLOR_H3 = RGBColor(0x37, 0x41, 0x51)   # xám đậm
MAX_IMG_WIDTH = Inches(5.5)

preprocessed_path = sys.argv[1]
output_path = sys.argv[2]

doc = Document()

# Page margins
for section in doc.sections:
    section.left_margin = Cm(2.54)
    section.right_margin = Cm(2.54)
    section.top_margin = Cm(2.54)
    section.bottom_margin = Cm(2.54)

# Default style
style = doc.styles['Normal']
style.font.name = FONT_NAME
style.font.size = Pt(FONT_SIZE_BODY)
style.paragraph_format.space_after = Pt(6)

def set_heading_style(para, level):
    sizes = {1: FONT_SIZE_H1, 2: FONT_SIZE_H2, 3: FONT_SIZE_H3}
    colors = {1: COLOR_H1, 2: COLOR_H2, 3: COLOR_H3}
    for run in para.runs:
        run.font.size = Pt(sizes.get(level, 12))
        run.font.color.rgb = colors.get(level, RGBColor(0,0,0))
        run.font.bold = True
        run.font.name = FONT_NAME

def set_img_alt(inline, alt_text):
    try:
        pic = inline._inline.findall('.//' + qn('pic:pic'))[0]
        nvPicPr = pic.find(qn('pic:nvPicPr'))
        cNvPr = nvPicPr.find(qn('pic:cNvPr'))
        cNvPr.set('descr', alt_text)
    except Exception:
        pass

def _add_runs(para, text, bold=False, italic=False, color=None):
    """Add text as Word runs, parsing [link](url) within. Preserves bold/italic flags."""
    LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    pos = 0
    for m in LINK.finditer(text):
        before = text[pos:m.start()]
        if before:
            run = para.add_run(before)
            run.font.name = FONT_NAME
            run.bold = bold
            run.italic = italic
            if color: run.font.color.rgb = color
        run = para.add_run(m.group(1))
        run.font.name = FONT_NAME
        run.bold = bold
        run.italic = italic
        run.font.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
        pos = m.end()
    tail = text[pos:]
    if tail:
        run = para.add_run(tail)
        run.font.name = FONT_NAME
        run.bold = bold
        run.italic = italic
        if color: run.font.color.rgb = color


def parse_inline(para, text, color=None):
    """Parse **bold**, *italic*, [link](url) — handles links nested inside bold/italic."""
    TOKEN = re.compile(
        r'\*\*(.+?)\*\*'               # group 1: bold content
        r'|\[([^\]]+)\]\(([^)]+)\)'    # group 2: link text, group 3: url
        r'|\*([^*\n]+)\*',             # group 4: italic content
        re.DOTALL
    )
    pos = 0
    for m in TOKEN.finditer(text):
        before = text[pos:m.start()]
        if before:
            _add_runs(para, before, color=color)
        if m.group(1) is not None:          # bold — recurse for nested links
            _add_runs(para, m.group(1), bold=True, color=color)
        elif m.group(2) is not None:        # standalone link
            run = para.add_run(m.group(2))
            run.font.name = FONT_NAME
            run.font.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
        elif m.group(4) is not None:        # italic — recurse for nested links
            _add_runs(para, m.group(4), italic=True, color=color)
        pos = m.end()
    tail = text[pos:]
    if tail:
        _add_runs(para, tail, color=color)

def add_paragraph(text, style_name='Normal'):
    p = doc.add_paragraph(style=style_name)
    parse_inline(p, text)
    return p

# ---- PARSE FILE ----
with open(preprocessed_path, encoding='utf-8') as f:
    lines = f.readlines()

i = 0
table_buffer = []
in_table = False

while i < len(lines):
    line = lines[i].rstrip('\n')
    stripped = line.strip()

    # Image placeholder
    if stripped.startswith('> 📷 **[CHỖ NÀY CHÈN ẢNH:'):
        p = doc.add_paragraph()
        run = p.add_run(stripped[2:])
        run.font.color.rgb = RGBColor(0xEF, 0x44, 0x44)
        run.italic = True
        run.font.name = FONT_NAME
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        i += 1
        continue

    # Markdown image: ![alt](path)
    img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
    if img_match:
        alt = img_match.group(1)
        path = img_match.group(2)
        if os.path.exists(path):
            try:
                p = doc.add_paragraph()
                p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run()
                # python-docx không hỗ trợ WebP — convert sang JPEG in-memory
                if path.lower().endswith('.webp'):
                    with PILImage.open(path) as pil_img:
                        if pil_img.mode in ('RGBA', 'LA', 'P'):
                            pil_img = pil_img.convert('RGB')
                        buf = BytesIO()
                        pil_img.save(buf, format='JPEG', quality=90)
                        buf.seek(0)
                    inline = run.add_picture(buf, width=MAX_IMG_WIDTH)
                else:
                    inline = run.add_picture(path, width=MAX_IMG_WIDTH)
                set_img_alt(inline, alt)
                cap = doc.add_paragraph(alt)
                cap.alignment = WD_ALIGN_PARAGRAPH.CENTER
                for r in cap.runs:
                    r.font.size = Pt(9)
                    r.font.color.rgb = RGBColor(0x6B, 0x72, 0x80)
                    r.font.name = FONT_NAME
            except Exception as e:
                p = doc.add_paragraph(f'[Không tải được ảnh: {path}]')
        i += 1
        continue

    # Headings
    if stripped.startswith('### '):
        p = doc.add_heading(stripped[4:], level=3)
        set_heading_style(p, 3)
        i += 1
        continue
    if stripped.startswith('## '):
        p = doc.add_heading(stripped[3:], level=2)
        set_heading_style(p, 2)
        i += 1
        continue
    if stripped.startswith('# '):
        p = doc.add_heading(stripped[2:], level=1)
        set_heading_style(p, 1)
        i += 1
        continue

    # Horizontal rule
    if stripped in ('---', '***', '___'):
        p = doc.add_paragraph('─' * 60)
        for r in p.runs:
            r.font.color.rgb = RGBColor(0xD1, 0xD5, 0xDB)
        i += 1
        continue

    # Blockquote bullet: > - text  (e.g. TL;DR list items)
    if stripped.startswith('> - ') or stripped.startswith('> * '):
        text = stripped[4:]
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.5)
        p.paragraph_format.first_line_indent = Cm(-0.4)
        p.paragraph_format.space_before = Pt(1)
        p.paragraph_format.space_after = Pt(2)
        bullet_run = p.add_run('• ')
        bullet_run.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)
        bullet_run.font.name = FONT_NAME
        bullet_run.font.size = Pt(10)
        parse_inline(p, text)
        for r in p.runs:
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)
        i += 1
        continue

    # Blockquote plain: > text
    if stripped.startswith('> '):
        text = stripped[2:]
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.space_before = Pt(3)
        p.paragraph_format.space_after = Pt(3)
        parse_inline(p, text)
        for r in p.runs:
            r.font.size = Pt(10)
            r.font.color.rgb = RGBColor(0x4B, 0x55, 0x63)
        i += 1
        continue

    # Table detection
    if '|' in stripped and stripped.startswith('|'):
        table_buffer = [stripped]
        i += 1
        # Collect all table rows
        while i < len(lines):
            tline = lines[i].rstrip('\n').strip()
            if '|' in tline and tline.startswith('|'):
                table_buffer.append(tline)
                i += 1
            else:
                break
        # Parse table
        rows = []
        for trow in table_buffer:
            if re.match(r'^\|[-| :]+\|$', trow):
                continue  # skip separator row
            cells = [c.strip() for c in trow.split('|') if c.strip()]
            if cells:
                rows.append(cells)
        if len(rows) >= 1:
            col_count = max(len(r) for r in rows)
            table = doc.add_table(rows=len(rows), cols=col_count)
            table.style = 'Table Grid'
            for r_i, row_data in enumerate(rows):
                for c_i, cell_text in enumerate(row_data):
                    if c_i < col_count:
                        cell = table.rows[r_i].cells[c_i]
                        cell.text = ''
                        p = cell.paragraphs[0]
                        parse_inline(p, cell_text)
                        for run in p.runs:
                            run.font.name = FONT_NAME
                            run.font.size = Pt(10)
                        if r_i == 0:
                            for run in p.runs:
                                run.bold = True
            doc.add_paragraph()  # space after table
        continue

    # Bullet list
    if stripped.startswith('- ') or stripped.startswith('* '):
        p = doc.add_paragraph(style='List Bullet')
        parse_inline(p, stripped[2:])
        for r in p.runs:
            r.font.name = FONT_NAME
            r.font.size = Pt(FONT_SIZE_BODY)
        i += 1
        continue

    # Numbered list — manual hanging indent (avoids Word XML numbering bugs)
    num_match = re.match(r'^(\d+)\. (.+)', stripped)
    if num_match:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.first_line_indent = Cm(-0.63)
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after = Pt(4)
        num_run = p.add_run(num_match.group(1) + '. ')
        num_run.font.name = FONT_NAME
        num_run.font.size = Pt(FONT_SIZE_BODY)
        parse_inline(p, num_match.group(2))
        for r in p.runs:
            r.font.name = FONT_NAME
            r.font.size = Pt(FONT_SIZE_BODY)
        i += 1
        continue

    # Regular paragraph
    if stripped:
        p = add_paragraph(stripped)
        p.paragraph_format.space_after = Pt(8)
    else:
        # Empty line = paragraph break (skip extra blank lines)
        pass

    i += 1

doc.save(output_path)
print('Saved:', output_path)
```

Lưu script vào `{scripts_dir}/convert.py`, chạy bằng PowerShell:
```powershell
$base = "D:\Nunu-Claude\seo_content\output\{category}\{slug}"
python "$base\_scripts\convert.py" "$base\preprocessed.md" "$base\export.docx"
```

### Bước 6 — Kiểm tra output

Sau khi chạy xong, kiểm tra file đã tạo:
```powershell
$base = "D:\Nunu-Claude\seo_content\output\{category}\{slug}"
(Get-Item "$base\export-{slug}.docx").Length
```

Dọn dẹp file tạm (chỉ xóa _preprocessed — GIỮ LẠI scripts trong `_scripts/` để re-export):
```powershell
Remove-Item "$base\_preprocessed.md" -Force -ErrorAction SilentlyContinue
```

> **Lưu ý:** `_scripts/preprocess.py` và `_scripts/convert.py` được GIỮ LẠI để lần re-export chỉ cần chạy lại 2 script.

### Bước 7 — Upload lên Google Drive (nếu đã cấu hình)

Đọc `D:\Nunu-Claude\seo_content\profiles\default.json` → lấy `drive_folder_id`.

**Nếu `drive_folder_id` rỗng hoặc không có:** Bỏ qua bước này, ghi chú trong báo cáo cuối:
> "Drive upload: bỏ qua (chưa có drive_folder_id trong profiles/default.json)"

**Nếu có `drive_folder_id`:** Chạy uploader dùng chung:
```powershell
$base = "D:\Nunu-Claude\seo_content\output\{category}\{slug}"
$uploader = "D:\Nunu-Claude\seo_content\_scripts\drive_uploader.py"
$env:PYTHONIOENCODING = 'utf-8'
python $uploader "$base\export-{slug}.docx"
```

Nếu muốn lưu dưới dạng Google Docs (chỉnh sửa được trực tiếp trên browser):
```powershell
python $uploader "$base\export-{slug}.docx" --convert
```

Script tự đọc `drive_folder_id` từ `profiles/default.json` và `service_account.json` từ `credentials/`.

**Nếu service account chưa có:**
- Hướng dẫn user tạo tại https://console.cloud.google.com/iam-admin/serviceaccounts
- Lưu JSON key vào `D:\Nunu-Claude\credentials\service_account.json`
- Share Drive folder với email service account (field `client_email` trong JSON key)
- Sau đó điền folder ID vào `profiles/default.json` → `drive_folder_id`

**Setup one-time (chỉ làm 1 lần, ghi nhớ để hướng dẫn user):**
1. Mở `credentials/service_account.json` → copy `"client_email"` (dạng `xxx@xxx.iam.gserviceaccount.com`)
2. Vào Google Drive → chuột phải folder muốn upload → Share → paste email trên → chọn Editor
3. Copy folder ID từ URL Drive: `https://drive.google.com/drive/folders/[FOLDER_ID]`
4. Paste vào `profiles/default.json` → `"drive_folder_id": "[FOLDER_ID]"`

## Thông báo hoàn thành

Báo cáo ngắn gọn:
- Đường dẫn file local: `seo_content/output/{category}/{slug}/export-{slug}.docx`
- Kích thước file (KB)
- Số ảnh đã embed thật / số ảnh placeholder
- Tool đã dùng (pandoc hoặc python-docx)
- Drive link (nếu upload thành công) — format: `https://drive.google.com/...`
- Gợi ý: "Mở file → kiểm tra heading styles và bảng → upload CMS hoặc import Google Docs"

Nếu file không tạo được, báo lỗi cụ thể và gợi ý sửa.
