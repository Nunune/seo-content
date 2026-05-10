---
name: seo-improve
description: |
  Tự động cải thiện bài SEO theo vòng lặp: đọc audit → áp dụng fixes → audit lại
  cho đến khi đạt điểm mục tiêu hoặc hết số vòng. Sau đó tự động tạo ảnh và xuất .docx.
  Kích hoạt khi user nói "cải thiện bài", "sửa lỗi audit", "tăng điểm SEO", "auto improve",
  "loop đến 85", "tự động sửa cho đến khi đạt", "/seo-improve".
argument-hint: --draft output/{category}/{slug}/draft.md --keyword "từ khóa" [--target 85] [--max-iter 3]
allowed-tools: [Read, Edit, Write, WebSearch, WebFetch, Bash, PowerShell]
---

# SEO Improve — Tự động cải thiện → Tạo ảnh → Xuất .docx

Đọc audit report → áp dụng fixes → re-audit → lặp cho đến khi đạt target.
Sau khi vòng lặp kết thúc: **tự động tạo ảnh** và **xuất file .docx**.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--draft path` — **BẮT BUỘC**: đường dẫn file draft (VD: `output/social-media/kiem-tien-voi-tiktok/draft.md`)
- `--keyword "X"` — **BẮT BUỘC**: từ khóa chính
- `--target N` — điểm mục tiêu 0-100 (mặc định: **85**)
- `--max-iter N` — số vòng lặp tối đa (mặc định: **3**)

Nếu thiếu `--draft` hoặc `--keyword`, hỏi user trước khi tiếp tục.

---

## Bước 1 — Khởi tạo

**1a. Đọc file draft:**
Dùng Read tool đọc toàn bộ nội dung `--draft`.

**1b. Xác định slug và category:**
Từ path file draft `output/{category}/{slug}/draft.md`:
- `category` = component thứ 2 (VD: `social-media`)
- `slug` = component thứ 3 (VD: `kiem-tien-voi-tiktok`)
- `article_dir` = `D:\Nunu-Claude\seo_content\output\{category}\{slug}`

**1c. Tìm audit JSON:**
Tìm file `{article_dir}\audit.json`.
- Nếu **có**: đọc → lấy `total_score` và `phases`
- Nếu **không có**: chạy toàn bộ quy trình `/seo-audit` trước, rồi đọc JSON vừa tạo

**1d. Kiểm tra ngay:**
```
[Vòng 0] Điểm hiện tại: {score}/100 (mục tiêu: {target})
```
Nếu `score >= target` → báo **"Bài đã đạt {score}/100."** → bỏ qua Bước 2, chuyển thẳng sang Bước 3.

---

## Bước 2 — Vòng lặp cải thiện

Lặp tối đa `max-iter` lần. Mỗi vòng: **Phân tích → Fix → Re-audit**.

### 2A. Phân tích lỗi

Đọc `{article_dir}\audit.json` → liệt kê phases `"fail"` hoặc `"warn"`.
Đọc `{article_dir}\audit.md` → lấy danh sách lỗi cụ thể.

**Thứ tự ưu tiên fix:**
1. Phase 3 — E-E-A-T (max 30pt)
2. Phase 2 — Cấu trúc (max 15pt)
3. Phase 5 — Linking (max 10pt)
4. Phase 6 — Technical (max 10pt)
5. Phase 4 — Media (max 10pt)
6. Phase 7B — AIO (max 8pt)

### 2B. Áp dụng fixes vào draft

Dùng Edit tool chỉnh sửa trực tiếp file draft.

**FIX PHASE 5 — Linking (nếu score < 8/10):**

*Bước đầu tiên — Đọc content index:*
- Đọc `D:\Nunu-Claude\seo_content\content-index.md` để biết bài nào thực sự tồn tại
- Chỉ nhúng link vào body cho slug **có trong index**
- Phantom links (slug không có trong index) → đổi thành `<!-- TODO: thêm link khi bài "{chủ đề}" được viết -->`

*External links thiếu:*
- Xác định tất cả trích dẫn `(Nguồn, Năm)` chưa có hyperlink
- WebSearch: `"{tên tổ chức}" official site` để tìm URL thực
- Edit draft: thêm hyperlink vào text

*Internal links từ comment sang body:*
- Tìm block `<!-- Internal Links gợi ý -->` trong draft
- Với mỗi anchor, kiểm tra slug trong content-index.md trước
- Nếu slug tồn tại → tìm đoạn văn tự nhiên trong body → chèn anchor text + link
- Nếu slug không tồn tại → giữ nguyên trong comment, thêm TODO note

**FIX PHASE 6 — Technical Schema (nếu score < 8/10):**

Append block JSON-LD đầy đủ vào cuối draft (Article + FAQPage + HowTo nếu bài hướng dẫn).
Đọc `D:\Nunu-Claude\seo_content\profiles\default.json` để điền author/publisher.

**FIX PHASE 3 — E-E-A-T (nếu score < 24/30):**

- Thêm bảng tính toán gốc phù hợp chủ đề (original data)
- Thêm note authority: `> *Bài viết được biên soạn bởi {author_name}...*`
- Thêm ví dụ minh họa cụ thể với số liệu

**FIX PHASE 2 — Cấu trúc (nếu score < 12/15):**

- Rút gọn H3 > 60 ký tự
- Kiểm tra meta description 140-160 ký tự, có CTA

**FIX PHASE 4 — Media (nếu score < 7/10):**

- Cập nhật `<!-- [ẢNH] -->` comments: thêm `File:` và `Alt:` có keyword nếu chưa có
- Thêm comment ảnh tại chỗ có bảng số liệu/list dài mà chưa có visual

**FIX PHASE 7B — AIO (nếu score < 6/8):**

- Thêm disambiguation nếu chưa có
- Kiểm tra Direct Answer sau mỗi H2 câu hỏi

### 2C. Re-audit sau khi fix

- Đọc draft đã sửa + checklist `D:\Nunu-Claude\seo_content\checklist.md`
- Chấm điểm lại 8 phases
- Ghi đè `{article_dir}\audit.json` và `{article_dir}\audit.md`
- In tiến độ:
```
[Vòng {n}] {new_score}/100 (+{delta})
  ✅ Tăng: {phases tăng}
  ⚠️ Còn: {phases chưa đạt}
```

### 2D. Điều kiện dừng

- `new_score >= target` → dừng ✅
- `delta <= 0` → dừng, không thể tăng thêm tự động
- Đã đủ `max-iter` vòng → dừng

---

## Bước 3 — Báo cáo điểm cuối

```
=== KẾT QUẢ IMPROVE ===
Vòng 0: {score_0}/100
Vòng 1: {score_1}/100 (+{d1}) → {phases fixed}
...
{✅ Đạt {target}/100 | ⚠️ Tốt nhất: {best}/100}
```

---

## Bước 4 — Tạo ảnh tự động

**Bước này chạy luôn sau vòng lặp, không cần user yêu cầu thêm.**

### 4A. Trích xuất image blocks

Đọc draft (đã được cải thiện) → tìm tất cả `<!-- [ẢNH] ... -->`.
Với mỗi block, lấy: Mô tả, `File:`, `Alt:`.

Nếu không có block ảnh nào → bỏ qua Bước 4, chuyển sang Bước 5.

### 4B. Phân loại

- **diagram**: chứa "sơ đồ", "quy trình", "flow", "các bước", "mindmap", "lộ trình", "vòng tròn"
- **chart**: chứa "biểu đồ", "chart", "tăng trưởng", "thống kê", "so sánh số liệu"
- **screenshot**: chứa "screenshot", "giao diện", "màn hình", "công cụ"
- **stock**: còn lại

### 4C. Tạo generate_images.py

Viết script Python đầy đủ tại `{article_dir}\_scripts\generate_images.py`.
Tạo thư mục `{article_dir}\_scripts\` nếu chưa có.

**Cho ảnh `diagram` và `chart`**: tạo bằng code (matplotlib + Playwright/Mermaid).
**Cho ảnh `screenshot`** và **`stock`**: bỏ qua trong script (không thể tự động), sẽ để placeholder.

**Cấu trúc script:**

```python
"""Tao anh cho bai: {slug}"""
import os, sys, asyncio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\{category}\{slug}\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ── CHART functions (matplotlib) ──────────────────────

# Tạo 1 function per chart image
# Dùng tên biến tiếng Latin (không dấu) trong code Python để tránh encoding issues
# Dùng màu sắc nhất quán: #3B82F6 (xanh), #10B981 (xanh lá), #F59E0B (vàng), #EF4444 (đỏ)
# Lưu với tên file khớp với `File:` trong comment ảnh (thay .webp → .png)

def make_chart_N():
    # ... matplotlib code ...
    path = os.path.join(OUT, '{filename}.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] {filename} ({os.path.getsize(path)//1024}KB)')

# ── DIAGRAM Mermaid code strings ──────────────────────

MERMAID_DIAGRAM_N = """
[mermaid code - dùng tiếng Latin không dấu trong node labels để tránh encoding]
"""

# ── HTML wrapper cho Mermaid ──────────────────────────

def make_mermaid_html(mermaid_code, title):
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#fff; display:flex; flex-direction:column; align-items:center;
         padding:32px 40px; min-width:900px; }}
  h2 {{ font-family:Arial,sans-serif; font-size:18px; font-weight:bold;
        color:#111827; margin-bottom:24px; text-align:center; }}
  .mermaid {{ display:flex; justify-content:center; width:100%; }}
  .mermaid svg {{ max-width:100%; height:auto; }}
</style></head><body>
<h2>{title}</h2>
<div class="mermaid">{mermaid_code}</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({{startOnLoad:true,theme:'base',
  themeVariables:{{primaryColor:'#3B82F6',primaryTextColor:'#FFFFFF',
    primaryBorderColor:'#2563EB',lineColor:'#6B7280',
    fontSize:'16px',fontFamily:'Arial,sans-serif'}},
  flowchart:{{htmlLabels:true,curve:'linear',nodeSpacing:60,rankSpacing:80,padding:20}},
  mindmap:{{padding:24}}
}});
</script></body></html>"""

# ── Playwright async renderer — SVG scale-up fix ──────
# min_h = chiều cao tối thiểu ảnh output (px)
# Mindmap 4-8 node: 600 | Flowchart LR: 520 | Flowchart TD: 700

async def make_diagrams():
    from playwright.async_api import async_playwright
    jobs = [
        # (html_tmp, mermaid_code, title, out_file, vw, vh, min_h)
        ('tmp_d1.html', MERMAID_DIAGRAM_N, 'Title', '{filename}.png', 1200, 800, 600),
        # thêm jobs cho các diagram khác
    ]
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for html_file, code, title, out_file, vw, vh, min_h in jobs:
            html_content = make_mermaid_html(code, title)
            html_path = os.path.join(OUT, html_file)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)
            page = await browser.new_page(viewport={{'width': vw, 'height': vh}})
            await page.goto(f'file:///{html_path}')
            await page.wait_for_selector('.mermaid svg', timeout=15000)
            await page.wait_for_timeout(2000)
            # Scale SVG len min_h neu Mermaid render nho hon
            box = await page.locator('.mermaid svg').bounding_box()
            if box and box['height'] < min_h:
                scale = min_h / box['height']
                new_w = int(box['width'] * scale)
                new_h = int(box['height'] * scale)
                await page.evaluate(f"""() => {{
                    const s = document.querySelector('.mermaid svg');
                    if (!s) return;
                    s.setAttribute('width', '{new_w}');
                    s.setAttribute('height', '{new_h}');
                    s.style.width = '{new_w}px';
                    s.style.height = '{new_h}px';
                }}""")
                await page.set_viewport_size({{'width': max(vw, new_w+80), 'height': new_h+100}})
                await page.wait_for_timeout(400)
            out_path = os.path.join(OUT, out_file)
            await page.screenshot(path=out_path, full_page=True)
            print(f'[OK] {out_file} ({os.path.getsize(out_path)//1024}KB)')
            os.remove(html_path)
        await browser.close()

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    # Gọi từng make_chart_N()
    # asyncio.run(make_diagrams())  # nếu có diagram
    print('Done!')
```

**Nguyên tắc khi viết script:**
- Label trong matplotlib và Mermaid dùng tiếng Latin không dấu (tránh Windows cp1252 crash)
- Tên file output `.png` phải khớp chính xác với `File:` trong comment ảnh của draft (chỉ đổi extension .webp → .png)
- Mỗi chart/diagram là 1 function riêng biệt
- Không dùng emoji trong print() — dùng `[OK]`, `[1/N]` thay thế

### 4D. Chạy generate_images script

```powershell
cd D:\Nunu-Claude
$env:PYTHONIOENCODING = 'utf-8'
python "seo_content/output/{category}/{slug}/_scripts/generate_images.py"
```

Nếu script lỗi: đọc error message → fix code → chạy lại (tối đa 2 lần retry).

### 4E. Cập nhật manifest

Lưu `{article_dir}\images.md` với danh sách ảnh đã tạo.

---

## Bước 5 — Xuất file .docx

**Bước này chạy ngay sau Bước 4, không cần user yêu cầu thêm.**

### 5A. Tạo preprocess.py

Nếu file chưa tồn tại, tạo mới tại `{article_dir}\_scripts\preprocess.py`.

Script preprocess chuẩn (copy y chang, chỉ thay đổi khi có logic đặc biệt):

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

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    if stripped.startswith('<!--'):
        is_image_block = stripped.startswith('<!-- [ẢNH]')
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
            alt_match = re.search(r'[Aa]lt(?:\s+text)?[:\s]+["\']?([^"\'|\n\-\-]+)["\']?', block_text)
            file_match = re.search(r'File:\s*(\S+\.(?:webp|png|jpg|jpeg))', block_text, re.IGNORECASE)
            alt_text = alt_match.group(1).strip().rstrip('"\'') if alt_match else 'image'
            file_name = file_match.group(1) if file_match else ''

            image_found = False
            image_path = ''
            if file_name and images_dir:
                check_path = os.path.join(images_dir, file_name)
                if os.path.exists(check_path):
                    image_found = True
                    image_path = check_path
                else:
                    base = os.path.splitext(file_name)[0]
                    for ext in ['.webp', '.png', '.jpg', '.jpeg']:
                        cp = os.path.join(images_dir, base + ext)
                        if os.path.exists(cp):
                            image_found = True
                            image_path = cp
                            break

            if image_found:
                result.append(f'![{alt_text}]({image_path})')
            else:
                display_name = file_name if file_name else '(chua co ten file)'
                result.append(f'> [CHO NAY CHEN ANH: {display_name}]')

        i += 1
        continue

    result.append(line)
    i += 1

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print('Preprocessed:', output_path)
```

### 5B. Tạo convert.py

Nếu file chưa tồn tại, tạo mới tại `{article_dir}\_scripts\convert.py`.

Script convert chuẩn — sử dụng đúng template sau (không thay đổi logic):

```python
import re, sys, os
from io import BytesIO
from docx import Document
from docx.shared import Inches, Pt, RGBColor, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from PIL import Image as PILImage

FONT_NAME = 'Arial'
FONT_SIZE_BODY = 11
FONT_SIZE_H1 = 18
FONT_SIZE_H2 = 15
FONT_SIZE_H3 = 13
COLOR_H1 = RGBColor(0x1D, 0x4E, 0xD8)
COLOR_H2 = RGBColor(0x1E, 0x40, 0xAF)
COLOR_H3 = RGBColor(0x37, 0x41, 0x51)
MAX_IMG_WIDTH = Inches(5.5)

preprocessed_path = sys.argv[1]
output_path = sys.argv[2]

doc = Document()
for section in doc.sections:
    section.left_margin = Cm(2.54); section.right_margin = Cm(2.54)
    section.top_margin = Cm(2.54); section.bottom_margin = Cm(2.54)

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
        run.font.bold = True; run.font.name = FONT_NAME

def set_img_alt(inline, alt_text):
    try:
        pic = inline._inline.findall('.//' + qn('pic:pic'))[0]
        cNvPr = pic.find(qn('pic:nvPicPr')).find(qn('pic:cNvPr'))
        cNvPr.set('descr', alt_text)
    except Exception: pass

def _add_runs(para, text, bold=False, italic=False, color=None):
    LINK = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    pos = 0
    for m in LINK.finditer(text):
        before = text[pos:m.start()]
        if before:
            run = para.add_run(before); run.font.name = FONT_NAME
            run.bold = bold; run.italic = italic
            if color: run.font.color.rgb = color
        run = para.add_run(m.group(1)); run.font.name = FONT_NAME
        run.bold = bold; run.italic = italic
        run.font.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
        pos = m.end()
    tail = text[pos:]
    if tail:
        run = para.add_run(tail); run.font.name = FONT_NAME
        run.bold = bold; run.italic = italic
        if color: run.font.color.rgb = color

def parse_inline(para, text, color=None):
    TOKEN = re.compile(r'\*\*(.+?)\*\*|\[([^\]]+)\]\(([^)]+)\)|\*([^*\n]+)\*', re.DOTALL)
    pos = 0
    for m in TOKEN.finditer(text):
        before = text[pos:m.start()]
        if before: _add_runs(para, before, color=color)
        if m.group(1) is not None: _add_runs(para, m.group(1), bold=True, color=color)
        elif m.group(2) is not None:
            run = para.add_run(m.group(2)); run.font.name = FONT_NAME
            run.font.color.rgb = RGBColor(0x3B, 0x82, 0xF6)
        elif m.group(4) is not None: _add_runs(para, m.group(4), italic=True, color=color)
        pos = m.end()
    tail = text[pos:]
    if tail: _add_runs(para, tail, color=color)

def add_paragraph(text, style_name='Normal'):
    p = doc.add_paragraph(style=style_name); parse_inline(p, text); return p

with open(preprocessed_path, encoding='utf-8') as f:
    lines = f.readlines()

i = 0
while i < len(lines):
    line = lines[i].rstrip('\n')
    stripped = line.strip()

    # Image placeholder (khi khong co file anh)
    if '[CHO NAY CHEN ANH:' in stripped:
        p = doc.add_paragraph()
        run = p.add_run(stripped.lstrip('> ').replace('**', ''))
        run.font.color.rgb = RGBColor(0xEF, 0x44, 0x44)
        run.italic = True; run.font.name = FONT_NAME
        p.paragraph_format.space_before = Pt(6)
        p.paragraph_format.space_after = Pt(6)
        i += 1; continue

    # Markdown image (co file anh that)
    img_match = re.match(r'!\[([^\]]*)\]\(([^)]+)\)', stripped)
    if img_match:
        alt, path = img_match.group(1), img_match.group(2)
        if os.path.exists(path):
            try:
                p = doc.add_paragraph(); p.alignment = WD_ALIGN_PARAGRAPH.CENTER
                run = p.add_run()
                if path.lower().endswith('.webp'):
                    with PILImage.open(path) as pil_img:
                        if pil_img.mode in ('RGBA','LA','P'): pil_img = pil_img.convert('RGB')
                        buf = BytesIO(); pil_img.save(buf, format='JPEG', quality=90); buf.seek(0)
                    inline = run.add_picture(buf, width=MAX_IMG_WIDTH)
                else:
                    inline = run.add_picture(path, width=MAX_IMG_WIDTH)
                set_img_alt(inline, alt)
            except Exception as e:
                doc.add_paragraph(f'[Loi anh: {path} - {e}]')
        i += 1; continue

    if stripped.startswith('### '):
        p = doc.add_heading(stripped[4:], level=3); set_heading_style(p, 3); i += 1; continue
    if stripped.startswith('## '):
        p = doc.add_heading(stripped[3:], level=2); set_heading_style(p, 2); i += 1; continue
    if stripped.startswith('# '):
        p = doc.add_heading(stripped[2:], level=1); set_heading_style(p, 1); i += 1; continue

    if stripped in ('---','***','___'):
        p = doc.add_paragraph('─' * 60)
        for r in p.runs: r.font.color.rgb = RGBColor(0xD1, 0xD5, 0xDB)
        i += 1; continue

    if stripped.startswith('> - ') or stripped.startswith('> * '):
        text = stripped[4:]; p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.5)
        p.paragraph_format.first_line_indent = Cm(-0.4)
        p.paragraph_format.space_before = Pt(1); p.paragraph_format.space_after = Pt(2)
        br = p.add_run('• '); br.font.color.rgb = RGBColor(0x4B,0x55,0x63)
        br.font.name = FONT_NAME; br.font.size = Pt(10)
        parse_inline(p, text)
        for r in p.runs: r.font.size = Pt(10); r.font.color.rgb = RGBColor(0x4B,0x55,0x63)
        i += 1; continue

    if stripped.startswith('> '):
        text = stripped[2:]; p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.0)
        p.paragraph_format.space_before = Pt(3); p.paragraph_format.space_after = Pt(3)
        parse_inline(p, text)
        for r in p.runs: r.font.size = Pt(10); r.font.color.rgb = RGBColor(0x4B,0x55,0x63)
        i += 1; continue

    if '|' in stripped and stripped.startswith('|'):
        table_buffer = [stripped]; i += 1
        while i < len(lines):
            tline = lines[i].rstrip('\n').strip()
            if '|' in tline and tline.startswith('|'): table_buffer.append(tline); i += 1
            else: break
        rows = []
        for trow in table_buffer:
            if re.match(r'^\|[-| :]+\|$', trow): continue
            cells = [c.strip() for c in trow.split('|') if c.strip()]
            if cells: rows.append(cells)
        if rows:
            col_count = max(len(r) for r in rows)
            table = doc.add_table(rows=len(rows), cols=col_count)
            table.style = 'Table Grid'
            for r_i, row_data in enumerate(rows):
                for c_i, cell_text in enumerate(row_data):
                    if c_i < col_count:
                        cell = table.rows[r_i].cells[c_i]; cell.text = ''
                        p = cell.paragraphs[0]; parse_inline(p, cell_text)
                        for run in p.runs: run.font.name = FONT_NAME; run.font.size = Pt(10)
                        if r_i == 0:
                            for run in p.runs: run.bold = True
            doc.add_paragraph()
        continue

    if stripped.startswith('- ') or stripped.startswith('* '):
        p = doc.add_paragraph(style='List Bullet'); parse_inline(p, stripped[2:])
        for r in p.runs: r.font.name = FONT_NAME; r.font.size = Pt(FONT_SIZE_BODY)
        i += 1; continue

    num_match = re.match(r'^(\d+)\. (.+)', stripped)
    if num_match:
        p = doc.add_paragraph()
        p.paragraph_format.left_indent = Cm(1.0); p.paragraph_format.first_line_indent = Cm(-0.63)
        p.paragraph_format.space_before = Pt(2); p.paragraph_format.space_after = Pt(4)
        nr = p.add_run(num_match.group(1) + '. '); nr.font.name = FONT_NAME; nr.font.size = Pt(FONT_SIZE_BODY)
        parse_inline(p, num_match.group(2))
        for r in p.runs: r.font.name = FONT_NAME; r.font.size = Pt(FONT_SIZE_BODY)
        i += 1; continue

    if stripped:
        p = add_paragraph(stripped); p.paragraph_format.space_after = Pt(8)
    i += 1

doc.save(output_path)
print('Saved:', output_path)
```

### 5C. Chạy export pipeline

```powershell
$env:PYTHONIOENCODING = 'utf-8'
$base    = "D:\Nunu-Claude\seo_content\output\{category}\{slug}"
$scripts = "$base\_scripts"
$shared  = "D:\Nunu-Claude\seo_content\_scripts"

# 1. Preprocess: chuyển <!-- [ẢNH] --> → ![alt](path)
python "$scripts\preprocess.py" "$base\draft.md" "$base\_preprocessed.md" "$base\images"

# 2. Gắn README vào cuối (phụ lục hướng dẫn đăng bài)
python "$shared\append_readme.py" "$base\_preprocessed.md" "$base\README.md"

# 3. Convert sang .docx
python "$scripts\convert.py" "$base\_preprocessed.md" "$base\export-{slug}.docx"
Remove-Item "$base\_preprocessed.md" -Force -ErrorAction SilentlyContinue
```

### 5D. Upload lên Google Drive

Đọc `D:\Nunu-Claude\seo_content\profiles\default.json` → lấy `drive_folder_id`.

**Nếu `drive_folder_id` rỗng:** bỏ qua, ghi `drive_link = null`.

**Nếu có `drive_folder_id`:** chạy uploader dùng chung:

```powershell
$env:PYTHONIOENCODING = 'utf-8'
$uploader = "D:\Nunu-Claude\seo_content\_scripts\drive_uploader.py"
$docx     = "D:\Nunu-Claude\seo_content\output\{category}\{slug}\export-{slug}.docx"
python $uploader $docx
```

- Nếu thành công: lấy dòng cuối output (URL Drive) → lưu làm `drive_link`
- Nếu lỗi (token hết hạn, chưa auth): báo user chạy lệnh upload thủ công, tiếp tục bước tiếp theo bình thường

---

## Bước 6 — Tạo README.md cho slug

**Bước này chạy ngay sau Bước 5, không cần user yêu cầu thêm.**

Tạo (hoặc ghi đè) file `{article_dir}\README.md` — tài liệu nhanh mô tả trạng thái bài viết,
dùng để tra cứu sau này mà không cần mở draft hay audit.

### Cách xây dựng nội dung README

**Lấy từ draft (SEO Meta block):**
- Title, Meta Description, Slug, Keyword chính, Keyword phụ, Ngày viết

**Lấy từ audit.json:**
- `total_score`, `grade`, từng `phases` (score/max)
- `critical_issues`, `warnings`, `suggestions`

**Lấy từ draft (TODO block):**
- Trích xuất danh sách `- [ ]` còn lại trong `<!-- TODO ... -->`

**Tips tối ưu — generate tự động dựa trên phases còn yếu:**

| Phase yếu | Tips tối ưu gợi ý |
|-----------|------------------|
| Phase 3 < 27/30 | Thêm 1 đoạn trải nghiệm first-hand với số liệu cụ thể; thêm case study thực tế |
| Phase 4 < 8/10 | Thay ảnh mockup bằng screenshot thực; thêm caption dưới mỗi ảnh trong CMS |
| Phase 5 < 9/10 | Xác nhận và activate internal links khi bài live; thêm external link nguồn mới |
| Phase 1 < 8/10 | Bổ sung sub-topic chưa cover (xem audit.md phần GĐ1); thêm FAQ từ PAA |
| Phase 7A < 6/7 | Thêm 1-2 số liệu có nguồn + năm rõ ràng vào từng section còn thiếu |
| Phase 7B < 7/8 | Kiểm tra mỗi H2 câu hỏi có Direct Answer 40-60 từ ngay bên dưới không |

### Định dạng README.md

```markdown
# {Tiêu đề bài viết}

**Keyword:** {keyword chính}
**Slug:** `{slug}`
**Category:** {category}
**Ngày viết:** {ngày từ SEO Meta}
**Cập nhật lần cuối:** {ngày chạy improve}

---

## Điểm audit: {score}/100 — {Xuất sắc / Tốt / Trung bình}

| Phase | Điểm | Max | Trạng thái |
|-------|------|-----|-----------|
| GĐ1 Research | {n} | 10 | ✅/⚠️/❌ |
| GĐ2 Cấu trúc | {n} | 15 | ✅/⚠️/❌ |
| GĐ3 E-E-A-T | {n} | 30 | ✅/⚠️/❌ |
| GĐ4 Media | {n} | 10 | ✅/⚠️/❌ |
| GĐ5 Linking | {n} | 10 | ✅/⚠️/❌ |
| GĐ6 Technical | {n} | 10 | ✅/⚠️/❌ |
| GĐ7A GEO | {n} | 7 | ✅/⚠️/❌ |
| GĐ7B AIO | {n} | 8 | ✅/⚠️/❌ |

---

## Files

| File | Kích thước | Ghi chú |
|------|-----------|---------|
| `draft.md` | — | Bài viết hoàn chỉnh |
| `export-{slug}.docx` | {size}KB | {n} ảnh nhúng ({n_real} thật / {n_mock} mockup) |
| Google Drive | — | {drive_link nếu có, hoặc "chưa upload"} |
| `audit.md` | — | Báo cáo chi tiết |
| `images/` | — | {n_img} files PNG |

---

## Còn lại trước khi đăng

{danh sách TODO từ draft — mỗi dòng `- [ ] ...`}

---

## Tips tối ưu lên {target+5}+

{1 bullet per weak phase — xem bảng ở trên}
```

**Quan trọng:** Nếu README.md đã tồn tại từ lần chạy trước, **ghi đè hoàn toàn** — không append.

---

## Bước 7 — Cập nhật Content Index

**Thêm bài vừa hoàn thành vào `D:\Nunu-Claude\seo_content\content-index.md`:**

- Nếu slug đã có trong index (bài đã được cải thiện) → cập nhật điểm mới
- Nếu slug chưa có → thêm dòng mới vào bảng và vào đúng cluster

```markdown
| `{slug}` | {category} | {keyword} | {final_score} | /{slug} |
```

Cũng cập nhật phần "Nhóm theo cluster" nếu bài thuộc cluster mới.

---

## Bước 8 — Báo cáo tổng kết cuối

```
=== HOÀN THÀNH ===
Keyword   : {keyword}
Điểm cuối : {final_score}/100 ({grade})

Ảnh đã tạo ({n_images} ảnh):
  ✅ {filename_1}.png
  ✅ {filename_2}.png
  [CHỖ CHÈN ẢNH] {filename_3} (screenshot/stock — cần tạo thủ công)

File xuất  : seo_content/output/{category}/{slug}/export-{slug}.docx ({size}KB)
Drive link : {drive_link | "—  (thêm drive_folder_id vào profiles/default.json để bật)"}
README     : seo_content/output/{category}/{slug}/README.md
Draft      : seo_content/output/{category}/{slug}/draft.md

Còn lại: xem README.md → mục "Còn lại trước khi đăng"
```

---

## Giới hạn — Những gì KHÔNG thể tự động

| Vấn đề | Lý do | Giải pháp |
|--------|-------|-----------|
| Ảnh screenshot / stock photo | Cần tải hoặc chụp thủ công | User tự làm → re-export |
| Trải nghiệm first-hand | Cần người thật xác nhận | Tác giả review |
| Internal links URL thực | Chưa chắc tồn tại trên seongon.com | Xác nhận rồi điền tay |
| Phase 4 Media 10/10 | Phụ thuộc ảnh thực | Accept ≤8/10 cho Media |

Target 85/100 vẫn đạt được dù Phase 4 ở mức 7–8/10.
