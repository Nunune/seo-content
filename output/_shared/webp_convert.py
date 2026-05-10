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
