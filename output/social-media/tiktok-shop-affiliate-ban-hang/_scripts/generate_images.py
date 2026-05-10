"""
Tao 3 anh cho bai: tiktok-shop-affiliate-ban-hang
- so-sanh-affiliate-vs-ban-hang-tiktok-shop.png : Flowchart 2 co che (Playwright + Mermaid.js)
- bang-so-sanh-affiliate-seller-tiktok.png       : Bar chart thu nhap tiem nang (matplotlib)
- mo-hinh-ket-hop-seller-affiliate-tiktok.png    : Flowchart mo hinh ket hop (Playwright + Mermaid.js)
"""
import os, sys, asyncio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\tiktok-shop-affiliate-ban-hang\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ═══════════════════════════════════════════════════════
# CHART — Thu nhap tiem nang: Affiliate vs Seller theo thoi gian
# ═══════════════════════════════════════════════════════
def make_chart():
    stages = ['0-3 thang\n(Bat dau)', '3-6 thang\n(Tang toc)', '6+ thang\n(Scale)']
    affiliate = [2, 10, 50]
    seller    = [0, 5, 80]

    x = np.arange(len(stages))
    w = 0.35

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F9FAFB')

    bars_a = ax.bar(x - w/2, affiliate, w, label='TikTok Shop Affiliate',
                    color='#3B82F6', edgecolor='#2563EB', linewidth=0.8, alpha=0.9)
    bars_s = ax.bar(x + w/2, seller, w, label='Ban hang TikTok Shop',
                    color='#10B981', edgecolor='#059669', linewidth=0.8, alpha=0.9)

    for bar in bars_a:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2., h + 1,
                    f'{int(h)}tr', ha='center', va='bottom', fontsize=10,
                    fontweight='bold', color='#1D4ED8')

    for bar in bars_s:
        h = bar.get_height()
        if h > 0:
            ax.text(bar.get_x() + bar.get_width()/2., h + 1,
                    f'{int(h)}tr', ha='center', va='bottom', fontsize=10,
                    fontweight='bold', color='#065F46')

    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontsize=11, color='#374151')
    ax.set_ylabel('Thu nhap uoc tinh (trieu dong/thang)', fontsize=11, color='#374151', labelpad=8)
    ax.set_title('Thu Nhap Tiem Nang: TikTok Shop Affiliate vs Ban Hang TikTok Shop',
                 fontsize=13, fontweight='bold', color='#111827', pad=14)
    ax.set_ylim(0, 95)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{int(v)}tr'))
    ax.grid(axis='y', color='#E5E7EB', linewidth=0.8, zorder=0)
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['bottom', 'left']].set_color('#D1D5DB')
    ax.tick_params(colors='#374151', labelsize=10)
    ax.legend(fontsize=11, loc='upper left', framealpha=0.9)

    ax.annotate('Uoc tinh thi truong Viet Nam 2026 | Phu thuoc niche, audience va chien luoc',
                xy=(0.5, 0), xycoords='axes fraction',
                fontsize=9, color='#9CA3AF', ha='center', va='bottom',
                xytext=(0, -42), textcoords='offset points')

    fig.tight_layout()
    path = os.path.join(OUT, 'bang-so-sanh-affiliate-seller-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] bang-so-sanh-affiliate-seller-tiktok.png ({os.path.getsize(path)//1024}KB)')

# ═══════════════════════════════════════════════════════
# DIAGRAMS — Playwright + Mermaid.js
# ═══════════════════════════════════════════════════════

MERMAID_DIAGRAM1 = """
mindmap
  root(("TikTok Shop\nKiem Tien"))
    Affiliate
      Dang ky: 1K followers
      Chon san pham tu Showcase
      Tao video gan link
      Nhan hoa hong 3-40%
      Khong can von
      Khong quan ly kho
    Ban Hang
      Dang ky Seller CCCD
      Nhap hang va dang san pham
      Quan ly don va giao van
      Nhan loi nhuan 20-60%
      Can von ban dau
      Kiem soat thuong hieu
"""

MERMAID_DIAGRAM2 = """
flowchart LR
    Shop["Chu Shop<br/>TikTok Shop"] --> GH["Mo Gian Hang<br/>+ Dang San Pham"]
    GH --> Own["Tu Tao Video<br/>Ban Hang"]
    GH --> Collab["Mo Affiliate<br/>Collaboration"]
    Collab --> C1["Creator A<br/>Video Review"]
    Collab --> C2["Creator B<br/>TikTok LIVE"]
    Collab --> C3["Creator C..."]
    Own --> Rev["Doanh Thu<br/>TikTok Shop"]
    C1 --> Rev
    C2 --> Rev
    C3 --> Rev
    style Shop fill:#F59E0B,stroke:#D97706,color:#FFFFFF
    style GH fill:#FEF3C7,stroke:#F59E0B,color:#92400E
    style Own fill:#DBEAFE,stroke:#3B82F6,color:#1E40AF
    style Collab fill:#D1FAE5,stroke:#10B981,color:#065F46
    style C1 fill:#EFF6FF,stroke:#BFDBFE,color:#1E40AF
    style C2 fill:#EFF6FF,stroke:#BFDBFE,color:#1E40AF
    style C3 fill:#EFF6FF,stroke:#BFDBFE,color:#1E40AF
    style Rev fill:#EF4444,stroke:#DC2626,color:#FFFFFF
"""

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
<div class="mermaid">
{mermaid_code}
</div>
<script src="https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.min.js"></script>
<script>
mermaid.initialize({{
  startOnLoad: true, theme: 'base',
  themeVariables: {{
    primaryColor: '#3B82F6', primaryTextColor: '#FFFFFF',
    primaryBorderColor: '#2563EB', lineColor: '#6B7280',
    secondaryColor: '#F3F4F6', fontSize: '16px', fontFamily: 'Arial, sans-serif'
  }},
  flowchart: {{ htmlLabels: true, curve: 'linear', nodeSpacing: 60, rankSpacing: 80, padding: 20 }}
}});
</script></body></html>"""

async def make_diagrams():
    from playwright.async_api import async_playwright

    jobs = [
        ('tmp_d1.html', MERMAID_DIAGRAM1,
         'So Sanh TikTok Shop Affiliate va Ban Hang TikTok Shop',
         'so-sanh-affiliate-vs-ban-hang-tiktok-shop.png', 1200, 700, 560),
        ('tmp_d2.html', MERMAID_DIAGRAM2,
         'Mo Hinh Ket Hop: Seller + Affiliate TikTok Shop',
         'mo-hinh-ket-hop-seller-affiliate-tiktok.png', 1300, 700, 520),
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

            # Scale SVG len neu Mermaid render nho hon min_h
            box = await page.locator('.mermaid svg').bounding_box()
            if box and box['height'] < min_h:
                scale = min_h / box['height']
                new_w = int(box['width'] * scale)
                new_h = int(box['height'] * scale)
                await page.evaluate(f"""() => {{
                    const s = document.querySelector('.mermaid svg');
                    if (!s) return;
                    s.setAttribute('width', {new_w});
                    s.setAttribute('height', {new_h});
                    s.style.width  = '{new_w}px';
                    s.style.height = '{new_h}px';
                }}""")
                await page.set_viewport_size({'width': max(vw, new_w + 80), 'height': new_h + 100})
                await page.wait_for_timeout(400)

            out_path = os.path.join(OUT, out_file)
            await page.screenshot(path=out_path, full_page=True)
            from PIL import Image as _Img
            with _Img.open(out_path) as _im:
                w, h = _im.size
            print(f'[OK] {out_file} - {w}x{h}px, {os.path.getsize(out_path)//1024}KB')
            os.remove(html_path)

        await browser.close()

if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')

    print('[1/3] Tao bang-so-sanh-affiliate-seller-tiktok.png (bar chart)...')
    make_chart()

    print('[2-3/3] Tao diagram_1 + diagram_2 (Playwright + Mermaid)...')
    asyncio.run(make_diagrams())

    print('\nDone! Anh da luu tai:')
    print(f'  {OUT}')
