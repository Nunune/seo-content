"""Tao anh cho bai: kham-suc-khoe-tong-quat"""
import os, sys, asyncio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\suc-khoe\kham-suc-khoe-tong-quat\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Mau sac nhat quan
C_BLUE   = '#3B82F6'
C_GREEN  = '#10B981'
C_YELLOW = '#F59E0B'
C_RED    = '#EF4444'
C_GRAY   = '#6B7280'
C_LIGHT  = '#F3F4F6'
C_DARK   = '#111827'
C_INDIGO = '#4F46E5'


# ── CHART 1: So sanh goi kham suc khoe (3 goi) ───────────────────────────────

def make_chart_goi_kham():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    categories = ['Gio kham\n(tieng)', 'Xet nghiem\nmau', 'Sieu am\nbung', 'X-quang\nnguc', 'Tam soat\nung thu', 'Noi soi\ntieu hoa', 'MRI/CT']
    goi_co_ban =  [1, 1, 1, 1, 0, 0, 0]
    goi_nang_cao= [1, 1, 1, 1, 1, 0, 0]
    goi_cao_cap = [1, 1, 1, 1, 1, 1, 1]

    x = np.arange(len(categories))
    w = 0.25

    bars1 = ax.bar(x - w, goi_co_ban,  w, label='Co ban (1.5-4tr)',  color=C_GREEN,  alpha=0.85, edgecolor='white', linewidth=1.5)
    bars2 = ax.bar(x,     goi_nang_cao,w, label='Nang cao (4-8tr)',  color=C_BLUE,   alpha=0.85, edgecolor='white', linewidth=1.5)
    bars3 = ax.bar(x + w, goi_cao_cap, w, label='Cao cap (8-20tr)', color=C_INDIGO, alpha=0.85, edgecolor='white', linewidth=1.5)

    ax.set_xticks(x)
    ax.set_xticklabels(categories, fontsize=10, color=C_DARK)
    ax.set_yticks([0, 1])
    ax.set_yticklabels(['Khong co', 'Co trong goi'], fontsize=9, color=C_GRAY)
    ax.set_ylim(0, 1.5)
    ax.set_title('So sanh Hang muc Kham Suc Khoe Tong Quat theo Goi', fontsize=14, fontweight='bold', color=C_DARK, pad=16)
    ax.legend(loc='upper right', fontsize=10, framealpha=0.9)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.grid(True, linestyle='--', alpha=0.4)
    ax.set_axisbelow(True)

    for bars in [bars1, bars2, bars3]:
        for bar in bars:
            if bar.get_height() == 1:
                ax.text(bar.get_x() + bar.get_width()/2, 1.05, 'V', ha='center', va='bottom', fontsize=11, color='white' if bars == bars3 else 'white', fontweight='bold')

    plt.tight_layout(pad=2)
    path = os.path.join(OUT, 'so-sanh-goi-kham-suc-khoe-tong-quat.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] so-sanh-goi-kham-suc-khoe-tong-quat.png ({os.path.getsize(path)//1024}KB)')


# ── CHART 2: Chi phi kham dinh ky vs dieu tri benh muon ──────────────────────

def make_chart_chi_phi():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#FFFFFF')

    labels = ['Kham tong\nquat/nam', 'Dieu tri\ntieu duong\ncó bien chung', 'Dieu tri\nung thu\ndai trang GD3', 'Cap cuu\nnhoi mau\nco tim']
    values = [3, 27.5, 325, 225]
    colors = [C_GREEN, C_YELLOW, C_RED, C_RED]

    bars = ax.barh(labels, values, color=colors, alpha=0.85, edgecolor='white', linewidth=1.5, height=0.55)

    for bar, val in zip(bars, values):
        label = f'{val:.0f}tr' if val < 10 else (f'~{val:.0f}tr' if val < 100 else f'~{val:.0f}tr')
        ax.text(bar.get_width() + 5, bar.get_y() + bar.get_height()/2,
                label, va='center', fontsize=11, fontweight='bold', color=C_DARK)

    ax.set_xlabel('Chi phi trung binh (trieu dong)', fontsize=11, color=C_GRAY)
    ax.set_title('Chi phi Kham Dinh Ky vs Chi phi Dieu tri Benh Muon\n(Uoc tinh tai Viet Nam 2025-2026)', fontsize=13, fontweight='bold', color=C_DARK, pad=14)
    ax.set_xlim(0, 430)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.grid(True, linestyle='--', alpha=0.3)
    ax.set_axisbelow(True)

    legend_patches = [
        mpatches.Patch(color=C_GREEN,  label='Phong ngua (kham dinh ky)'),
        mpatches.Patch(color=C_YELLOW, label='Dieu tri man tinh'),
        mpatches.Patch(color=C_RED,    label='Cap cuu / benh nang'),
    ]
    ax.legend(handles=legend_patches, loc='lower right', fontsize=9, framealpha=0.9)

    plt.tight_layout(pad=2)
    path = os.path.join(OUT, 'bieu-do-chi-phi-kham-vs-dieu-tri.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] bieu-do-chi-phi-kham-vs-dieu-tri.png ({os.path.getsize(path)//1024}KB)')


# ── MERMAID DIAGRAMS ──────────────────────────────────────────────────────────

MERMAID_QUYtrinh = """
flowchart LR
    A([Dang ky\n& dat lich]) --> B[Kham\nlam sang]
    B --> C[Xet nghiem\nmau & nuoc tieu]
    C --> D[Chan doan\nhinh anh]
    D --> E[Tham do\nchuc nang]
    E --> F([Nhan ket qua\n& tu van])

    style A fill:#3B82F6,color:#fff,stroke:#2563EB
    style B fill:#10B981,color:#fff,stroke:#059669
    style C fill:#10B981,color:#fff,stroke:#059669
    style D fill:#10B981,color:#fff,stroke:#059669
    style E fill:#10B981,color:#fff,stroke:#059669
    style F fill:#4F46E5,color:#fff,stroke:#4338CA
"""

MERMAID_CHECKLIST = """
mindmap
  root((Chuan bi\nkham tong quat))
    Toi hom truoc
      Nhin an 8-10 tieng
      Khong ruou bia 24h
      Ngu du giac
      Bo sung sat vitamin E
    Sang ngay kham
      Di luc doi
      Quan ao thoai mai
      CMND / CCCD
      The BHYT
      Ket qua xet nghiem cu
      Danh sach thuoc dang dung
    Luu y nu gioi
      Tranh ngay kinh nguyet
      Khong quan he 24h truoc
"""


def make_mermaid_html(mermaid_code, title):
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#fff; display:flex; flex-direction:column; align-items:center;
         padding:32px 40px; min-width:900px; }}
  h2 {{ font-family:Arial,sans-serif; font-size:17px; font-weight:bold;
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
    fontSize:'15px',fontFamily:'Arial,sans-serif'}},
  flowchart:{{htmlLabels:true,curve:'linear',nodeSpacing:60,rankSpacing:80,padding:20}},
  mindmap:{{padding:24}}
}});
</script></body></html>"""


async def make_diagrams():
    from playwright.async_api import async_playwright
    jobs = [
        ('tmp_quytrinh.html', MERMAID_QUYtrinh,  'Quy trinh Kham Suc Khoe Tong Quat (5 buoc)',
         'so-do-quy-trinh-kham-tong-quat.png', 1200, 500, 400),
        ('tmp_checklist.html', MERMAID_CHECKLIST, 'Checklist Chuan bi truoc khi Kham Suc Khoe Tong Quat',
         'checklist-chuan-bi-kham-suc-khoe-tong-quat.png', 1200, 700, 580),
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
                await page.set_viewport_size({'width': max(vw, new_w + 80), 'height': new_h + 100})
                await page.wait_for_timeout(400)
            out_path = os.path.join(OUT, out_file)
            await page.screenshot(path=out_path, full_page=True)
            print(f'[OK] {out_file} ({os.path.getsize(out_path)//1024}KB)')
            os.remove(html_path)
        await browser.close()


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/4] so-sanh-goi-kham-suc-khoe-tong-quat.png ...')
    make_chart_goi_kham()
    print('[2/4] bieu-do-chi-phi-kham-vs-dieu-tri.png ...')
    make_chart_chi_phi()
    print('[3/4] so-do-quy-trinh-kham-tong-quat.png ...')
    print('[4/4] checklist-chuan-bi-kham-suc-khoe-tong-quat.png ...')
    asyncio.run(make_diagrams())
    print('Done! 4 images created.')
