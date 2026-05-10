---
name: seo-webp
description: |
  Tự động convert ảnh PNG/JPG sang định dạng WebP bằng Python Pillow.
  Kích hoạt khi user yêu cầu "convert webp", "chuyển webp", "đổi sang webp",
  "convert ảnh", "webp ảnh", "nén ảnh webp", "seo webp", "tạo webp",
  "convert png webp", "convert jpg webp", "đổi ảnh sang webp".
argument-hint: --slug {slug} | --input path/ [--quality 85] [--keep-original]
allowed-tools: [Read, Write, PowerShell]
---

# SEO WebP — Tự động convert ảnh sang WebP

Convert hàng loạt PNG/JPG sang WebP bằng Python Pillow.
Giữ nguyên alpha channel (PNG transparent), báo cáo kích thước tiết kiệm được.

## Arguments

Parse arguments:
- `--slug {slug}` — shorthand: tự resolve thành `D:\Nunu-Claude\seo_content\output\images\{slug}\`
- `--input path` — file hoặc directory cụ thể (override --slug)
- `--quality N` — WebP quality 1–100 (mặc định: **85**)
- `--keep-original` — giữ file PNG/JPG gốc sau khi convert (mặc định: xóa gốc)

Nếu không có `--slug` và không có `--input`, hỏi user trước khi tiếp tục.

## Quy trình thực hiện

### Bước 1 — Resolve input path

Nếu có `--slug`:
- `input_path = D:\Nunu-Claude\seo_content\output\images\{slug}\`

Nếu có `--input`:
- Nếu path bắt đầu bằng `output/` → prepend `D:\Nunu-Claude\seo_content\`
- Nếu path tuyệt đối → dùng nguyên

Ghi nhận: `quality` (mặc định 85), `keep_original` (mặc định False).

### Bước 2 — Kiểm tra Python Pillow

```powershell
python -c "from PIL import Image; print('pillow_ok')"
```

Nếu output không chứa `pillow_ok`:
```powershell
python -m pip install Pillow --quiet
```

### Bước 3 — Viết convert script

Write file `D:\Nunu-Claude\seo_content\output\webp_convert.py` với nội dung sau:

```python
import os, sys, glob
from PIL import Image

input_path = sys.argv[1]
quality = int(sys.argv[2]) if len(sys.argv) > 2 else 85
keep_original = '--keep' in sys.argv

if os.path.isfile(input_path):
    files = [input_path]
elif os.path.isdir(input_path):
    files = []
    for ext in ['*.png', '*.jpg', '*.jpeg', '*.PNG', '*.JPG', '*.JPEG']:
        files.extend(glob.glob(os.path.join(input_path, ext)))
    files = [f for f in files if not f.lower().endswith('.webp')]
    # Deduplicate (Windows glob is case-insensitive: *.png and *.PNG match same file)
    seen = set(); deduped = []
    for f in files:
        k = f.lower()
        if k not in seen: seen.add(k); deduped.append(f)
    files = deduped
else:
    print(f'ERROR: {input_path} not found'); sys.exit(1)

if not files:
    print('No PNG/JPG files found.'); sys.exit(0)

results = []
for f in sorted(files):
    out = os.path.splitext(f)[0] + '.webp'
    try:
        img = Image.open(f)
        if img.mode in ('RGBA', 'LA') or (img.mode == 'P' and 'transparency' in img.info):
            img = img.convert('RGBA')
        else:
            img = img.convert('RGB')
        img.save(out, 'WEBP', quality=quality, method=6)
        orig_sz = os.path.getsize(f)
        webp_sz = os.path.getsize(out)
        saving = (1 - webp_sz / orig_sz) * 100
        if not keep_original:
            os.remove(f)
        results.append((os.path.basename(f), os.path.basename(out), orig_sz, webp_sz, saving))
        print(f'OK  {os.path.basename(f):50s} {orig_sz//1024:>5}KB -> {webp_sz//1024:>5}KB  ({saving:.0f}% smaller)')
    except Exception as e:
        print(f'ERR {os.path.basename(f)}: {e}')
        results.append(None)

ok = [r for r in results if r]
total_orig = sum(r[2] for r in ok)
total_webp = sum(r[3] for r in ok)
total_pct  = (1 - total_webp / total_orig) * 100 if total_orig else 0
print(f'\nDone: {len(ok)}/{len(results)} files converted')
print(f'Total: {total_orig//1024}KB -> {total_webp//1024}KB ({total_pct:.0f}% smaller)')
```

### Bước 4 — Chạy script

```powershell
python "D:\Nunu-Claude\seo_content\output\webp_convert.py" "{input_path}" {quality} {keep_flag}
```

Trong đó `{keep_flag}` = `--keep` nếu `--keep-original` được chỉ định, hoặc bỏ trống.

### Bước 5 — Đọc output và báo cáo

Capture output từ script, parse và hiển thị:

```
Files converted:
  so-sanh-the-botanica-golden-mansion.png  83KB -> 52KB  (37% smaller)
  vi-tri-novaland-pho-quang-ban-do.png     96KB -> 61KB  (36% smaller)

Total: 179KB -> 113KB (37% smaller)
```

Nếu có lỗi ERR, liệt kê riêng và gợi ý kiểm tra file.

## Thông báo hoàn thành

Báo cáo:
- Số file đã convert / tổng
- Dung lượng tiết kiệm tổng
- Danh sách file WebP mới tạo (đường dẫn đầy đủ)
- Gợi ý bước tiếp: "Chạy `/seo-export --draft output/{category}/{slug}/draft.md` để embed ảnh WebP vào .docx"

Nếu không có file nào: thông báo "Không tìm thấy PNG/JPG tại {input_path}" và dừng.
