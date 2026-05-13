"""
Tao 3 anh cho bai: kiem tien voi tiktok
- kiem-tien-voi-tiktok-7-cach.png          : Mindmap 7 cach (Playwright + Mermaid.js)
- bang-so-sanh-7-cach-kiem-tien-tiktok.png : Bar chart thu nhap tiem nang (matplotlib)
- lo-trinh-kiem-tien-tiktok-3-giai-doan.png: Flowchart lo trinh (Playwright + Mermaid.js)
"""
import os, sys, asyncio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\kiem-tien-voi-tiktok\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ═══════════════════════════════════════════════════════
# CHART — Thu nhap tiem nang theo phuong phap (trieu VND/thang)
# ═══════════════════════════════════════════════════════
def make_chart():
    methods = [
        'TikTok LIVE Donate',
        'TikTok Shop Affiliate',
        'Ban hang TikTok Shop',
        'KOL / Brand Deal',
        'San pham so / Khoa hoc',
        'Creator Marketplace',
    ]
    min_vals = [2, 1, 5, 2, 5, 5]
    max_vals = [20, 30, 100, 100, 50, 50]
    colors   = ['#3B82F6', '#10B981', '#F59E0B', '#EF4444', '#8B5CF6', '#06B6D4']
    edge     = ['#2563EB', '#059669', '#D97706', '#DC2626', '#7C3AED', '#0891B2']

    y = np.arange(len(methods))
    h = 0.45

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F9FAFB')

    # Range bars (min to max)
    for i, (lo, hi, c, e) in enumerate(zip(min_vals, max_vals, colors, edge)):
        ax.barh(y[i], hi - lo, left=lo, height=h,
                color=c, edgecolor=e, linewidth=0.8, alpha=0.85, zorder=3)
        ax.barh(y[i], lo, height=h,
                color=c, edgecolor=e, linewidth=0.8, alpha=0.4, zorder=3)
        ax.text(hi + 1.5, y[i], f'{lo}–{hi}tr', va='center', fontsize=10,
                fontweight='bold', color='#111827')

    ax.set_yticks(y)
    ax.set_yticklabels(methods, fontsize=11, color='#374151')
    ax.set_xlabel('Thu nhap uoc tinh (trieu dong/thang)', fontsize=11, color='#374151', labelpad=8)
    ax.set_title('Thu Nhap Tiem Nang Theo Phuong Phap Kiem Tien TikTok',
                 fontsize=14, fontweight='bold', color='#111827', pad=14)
    ax.set_xlim(0, 120)
    ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{int(v)}tr'))
    ax.grid(axis='x', color='#E5E7EB', linewidth=0.8, zorder=0)
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['bottom', 'left']].set_color('#D1D5DB')
    ax.tick_params(colors='#374151', labelsize=10)

    ax.annotate('Uoc tinh thi truong Viet Nam 2026 | Phu thuoc niche va engagement rate',
                xy=(0.5, 0), xycoords='axes fraction',
                fontsize=9, color='#9CA3AF', ha='center', va='bottom',
                xytext=(0, -38), textcoords='offset points')

    fig.tight_layout()
    path = os.path.join(OUT, 'bang-so-sanh-7-cach-kiem-tien-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] bang-so-sanh-7-cach-kiem-tien-tiktok.png ({os.path.getsize(path)//1024}KB)')

# ═══════════════════════════════════════════════════════
# DIAGRAMS — Playwright + Mermaid.js
# ═══════════════════════════════════════════════════════
MERMAID_DIAGRAM1 = """
mindmap
  root((7 Cach<br/>Kiem Tien<br/>TikTok 2026))
    Khong Can Von
      1. TikTok LIVE Donate
      2. TikTok Shop Affiliate
      3. KOL / Brand Deal
    Can Von
      4. Ban Hang TikTok Shop
    Can Chuyen Mon
      5. San Pham So
      6. Creator Marketplace
    Nen Tang Tra Truc Tiep
      7. Creativity Program
"""

MERMAID_DIAGRAM2 = """
flowchart LR
    A["GIAI DOAN 1<br/>0-3 thang<br/>0 to 1K followers<br/>Xay nen tang"] --> B["GIAI DOAN 2<br/>3-6 thang<br/>1K to 10K followers<br/>Kiem tien dau tien"]
    B --> C["GIAI DOAN 3<br/>6+ thang<br/>10K+ followers<br/>Scale thu nhap"]

    A --- A1["1-2 video/ngay<br/>Chon niche hep<br/>Toi uu hook 3s"]
    B --- B1["Mo Affiliate<br/>TikTok LIVE donate<br/>2-10 trieu/thang"]
    C --- C1["KOL / Brand Deal<br/>Ban hang TikTok Shop<br/>10-100 trieu/thang"]

    style A fill:#3B82F6,stroke:#2563EB,color:#FFFFFF
    style B fill:#10B981,stroke:#059669,color:#FFFFFF
    style C fill:#F59E0B,stroke:#D97706,color:#FFFFFF
    style A1 fill:#EFF6FF,stroke:#BFDBFE,color:#1E40AF
    style B1 fill:#ECFDF5,stroke:#A7F3D0,color:#065F46
    style C1 fill:#FFFBEB,stroke:#FDE68A,color:#92400E
"""

def make_mermaid_html(mermaid_code, title):
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #fff; display: flex; flex-direction: column; align-items: center;
         padding: 32px 40px; min-width: 900px; }}
  h2 {{ font-family: Arial, sans-serif; font-size: 18px; font-weight: bold;
        color: #111827; margin-bottom: 24px; text-align: center; }}
  .mermaid {{ display: flex; justify-content: center; width: 100%; }}
  .mermaid svg {{ max-width: 100%; height: auto; }}
</style>
</head>
<body>
<h2>{title}</h2>
<div class="mermaid">
{mermaid_code}
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
  mermaid.initialize({{
    startOnLoad: true,
    theme: 'base',
    themeVariables: {{
      primaryColor: '#3B82F6',
      primaryTextColor: '#FFFFFF',
      primaryBorderColor: '#2563EB',
      lineColor: '#6B7280',
      secondaryColor: '#F3F4F6',
      tertiaryColor: '#FFFBEB',
      fontSize: '16px',
      fontFamily: 'Arial, sans-serif'
    }},
    flowchart: {{ htmlLabels: true, curve: 'linear',
                  nodeSpacing: 60, rankSpacing: 80, padding: 20 }},
    mindmap: {{ padding: 24 }}
  }});
</script>
</body>
</html>"""

async def make_diagrams():
    from playwright.async_api import async_playwright

    # min_h: minimum target height in px for the final image
    jobs = [
        ('diagram_1.html', MERMAID_DIAGRAM1, '7 Cach Kiem Tien Voi TikTok 2026',
         'kiem-tien-voi-tiktok-7-cach.png', 1200, 800, 600),
        ('diagram_2.html', MERMAID_DIAGRAM2, 'Lo Trinh Kiem Tien TikTok: 3 Giai Doan',
         'lo-trinh-kiem-tien-tiktok-3-giai-doan.png', 1300, 700, 520),
    ]

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        for html_file, code, title, out_file, vw, vh, min_h in jobs:
            html_content = make_mermaid_html(code, title)
            html_path = os.path.join(OUT, html_file)
            with open(html_path, 'w', encoding='utf-8') as f:
                f.write(html_content)

            page = await browser.new_page(viewport={'width': vw, 'height': vh})
            await page.goto(f'file:///{html_path}')
            await page.wait_for_selector('.mermaid svg', timeout=15000)
            await page.wait_for_timeout(2000)

            # Scale up SVG if it rendered smaller than min_h
            box = await page.locator('.mermaid svg').bounding_box()
            if box and box['height'] < min_h:
                scale = min_h / box['height']
                new_svg_w = int(box['width'] * scale)
                new_svg_h = int(box['height'] * scale)
                await page.evaluate(f"""() => {{
                    const svg = document.querySelector('.mermaid svg');
                    if (!svg) return;
                    svg.setAttribute('width', {new_svg_w});
                    svg.setAttribute('height', {new_svg_h});
                    svg.style.width  = '{new_svg_w}px';
                    svg.style.height = '{new_svg_h}px';
                }}""")
                # Resize viewport so full_page captures the new height
                new_vw = max(vw, new_svg_w + 80)
                await page.set_viewport_size({'width': new_vw, 'height': new_svg_h + 100})
                await page.wait_for_timeout(400)

            out_path = os.path.join(OUT, out_file)
            await page.screenshot(path=out_path, full_page=True)
            size = os.path.getsize(out_path) // 1024
            # Report final dimensions
            from PIL import Image as _Img
            with _Img.open(out_path) as _im:
                w, h = _im.size
            print(f'[OK] {out_file} — {w}x{h}px, {size}KB')
            os.remove(html_path)

        await browser.close()

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')

    print('[1/3] Tao bang-so-sanh-7-cach-kiem-tien-tiktok.png (bar chart)...')
    make_chart()

    print('[2-3/3] Tao diagram_1 + diagram_2 (Playwright + Mermaid)...')
    asyncio.run(make_diagrams())

    print('\nDone! Anh da luu tai:')
    print(f'  {OUT}')
