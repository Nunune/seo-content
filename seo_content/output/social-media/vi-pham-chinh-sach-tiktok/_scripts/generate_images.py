"""Tao anh cho bai: vi-pham-chinh-sach-tiktok"""
import os, sys, asyncio
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.patches import FancyBboxPatch

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\vi-pham-chinh-sach-tiktok\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# Colors
C_BLUE   = '#3B82F6'
C_GREEN  = '#10B981'
C_YELLOW = '#F59E0B'
C_RED    = '#EF4444'
C_GRAY   = '#6B7280'
C_LIGHT  = '#F3F4F6'
C_WHITE  = '#FFFFFF'
C_DARK   = '#111827'


# ── CHART 1: Infographic phan biet 3 loai chinh sach TikTok ──────────────

def make_chart_1():
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis('off')
    fig.patch.set_facecolor(C_WHITE)

    ax.text(6, 5.6, 'Phan Biet 3 Loai Chinh Sach TikTok',
            ha='center', va='center', fontsize=16, fontweight='bold', color=C_DARK)

    cols = [
        {'x': 0.3, 'color': C_BLUE,   'title': 'Tieu Chuan Cong Dong',
         'sub': 'Community Guidelines',
         'apply': 'Tat ca nguoi dung TikTok',
         'penalty': 'Xoa video\nHan che tai khoan\nKhoa tai khoan',
         'who': 'Creator, nguoi dung'},
        {'x': 4.3, 'color': C_GREEN,  'title': 'Chinh Sach TikTok Shop',
         'sub': 'Seller Policy',
         'apply': 'Nguoi ban hang TikTok Shop',
         'penalty': 'Xoa san pham\nDinh chi shop\nCam ban vinh vien',
         'who': 'Seller, Affiliate'},
        {'x': 8.3, 'color': C_YELLOW, 'title': 'Chinh Sach TikTok Ads',
         'sub': 'Ads Policy',
         'apply': 'Nha quang cao, agency',
         'penalty': 'Tu choi chien dich\nKhoa tai khoan QC\nGiu tien nap',
         'who': 'Brand, Agency'},
    ]

    labels = ['Ap dung cho', 'Hinh phat', 'Phu hop cho']

    for col in cols:
        x = col['x']
        c = col['color']
        # Header box
        header = FancyBboxPatch((x, 4.0), 3.5, 1.3,
                                boxstyle='round,pad=0.1', facecolor=c, edgecolor='none')
        ax.add_patch(header)
        ax.text(x+1.75, 4.95, col['title'], ha='center', va='center',
                fontsize=11, fontweight='bold', color=C_WHITE)
        ax.text(x+1.75, 4.45, col['sub'], ha='center', va='center',
                fontsize=9, color=C_WHITE, alpha=0.9)

        # Body rows
        row_data = [col['apply'], col['penalty'], col['who']]
        row_colors = [C_LIGHT, C_WHITE, C_LIGHT]
        row_ys = [3.1, 1.6, 0.5]
        row_hs = [0.8, 1.4, 0.8]

        for i, (label, data, rc, ry, rh) in enumerate(zip(labels, row_data, row_colors, row_ys, row_hs)):
            body = FancyBboxPatch((x, ry), 3.5, rh,
                                  boxstyle='round,pad=0.05', facecolor=rc, edgecolor='#E5E7EB')
            ax.add_patch(body)
            ax.text(x+1.75, ry+rh-0.2, label, ha='center', va='top',
                    fontsize=8, fontweight='bold', color=c)
            ax.text(x+1.75, ry+rh-0.45, data, ha='center', va='top',
                    fontsize=8.5, color=C_DARK, linespacing=1.4)

    path = os.path.join(OUT, 'infographic-3-loai-chinh-sach-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=C_WHITE)
    plt.close(fig)
    print(f'[OK] infographic-3-loai-chinh-sach-tiktok.png ({os.path.getsize(path)//1024}KB)')


# ── CHART 2: Bang tu bi cam TikTok Shop ──────────────────────────────────

def make_chart_2():
    fig, ax = plt.subplots(figsize=(11, 7))
    ax.axis('off')
    fig.patch.set_facecolor(C_WHITE)

    ax.text(0.5, 0.97, 'Tu Bi Cam Tren TikTok Shop Khi Quang Cao San Pham',
            transform=ax.transAxes, ha='center', va='top',
            fontsize=14, fontweight='bold', color=C_DARK)
    ax.text(0.5, 0.92, 'Su dung cac cum tu nay trong mo ta san pham se bi vi pham chinh sach',
            transform=ax.transAxes, ha='center', va='top',
            fontsize=10, color=C_GRAY)

    categories = [
        {
            'label': 'TUYEN BO VE HIEU QUA',
            'color': C_RED,
            'items': [
                '"chua khoi hoan toan"',
                '"100% hieu qua"',
                '"khoi benh nhanh chong"',
                '"dac tri" / "tri tuyet doi"',
                '"khong can dieu tri"',
            ]
        },
        {
            'label': 'TUYEN BO AN TOAN TUYET DOI',
            'color': C_YELLOW,
            'items': [
                '"100% tu nhien"',
                '"khong tac dung phu"',
                '"an toan tuyet doi"',
                '"khong kich ung"',
                '"benh nhan ung thu co the dung"',
            ]
        },
        {
            'label': 'TUYEN BO THUONG HIEU / CHUNG NHAN',
            'color': C_BLUE,
            'items': [
                '"so 1 Viet Nam" (khong CO chung nhan)',
                '"duoc Bo Y te chung nhan" (sai)',
                '"dat giai nhat" (khong co bang chung)',
                '"100.000 khach hang tin dung"',
                '"bac si khuyen dung" (sai)',
            ]
        },
    ]

    y = 0.83
    for cat in categories:
        # Category header
        ax.add_patch(FancyBboxPatch(
            (0.02, y-0.035), 0.96, 0.052,
            transform=ax.transAxes,
            boxstyle='round,pad=0.005', facecolor=cat['color'], edgecolor='none'
        ))
        ax.text(0.5, y-0.008, cat['label'], transform=ax.transAxes,
                ha='center', va='center', fontsize=10, fontweight='bold', color=C_WHITE)
        y -= 0.06

        for item in cat['items']:
            ax.add_patch(FancyBboxPatch(
                (0.04, y-0.03), 0.92, 0.042,
                transform=ax.transAxes,
                boxstyle='round,pad=0.003', facecolor=C_LIGHT, edgecolor='#E5E7EB'
            ))
            ax.text(0.08, y-0.007, '✗  ' + item, transform=ax.transAxes,
                    ha='left', va='center', fontsize=9.5, color=C_RED, fontweight='bold')
            y -= 0.05

        y -= 0.01

    ax.text(0.5, 0.02, 'Nguon: TikTok Shop Seller Policy 2026 | seongon.com',
            transform=ax.transAxes, ha='center', va='bottom',
            fontsize=8, color=C_GRAY, style='italic')

    path = os.path.join(OUT, 'bang-tu-bi-cam-tiktok-shop.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=C_WHITE)
    plt.close(fig)
    print(f'[OK] bang-tu-bi-cam-tiktok-shop.png ({os.path.getsize(path)//1024}KB)')


# ── CHART 3: Checklist 10 dieu tranh vi pham TikTok ─────────────────────

def make_chart_3():
    fig, ax = plt.subplots(figsize=(11, 8))
    ax.axis('off')
    fig.patch.set_facecolor(C_WHITE)

    ax.text(0.5, 0.97, 'Checklist 10 Dieu Can Tranh Truoc Khi Dang Video TikTok',
            transform=ax.transAxes, ha='center', va='top',
            fontsize=13, fontweight='bold', color=C_DARK)
    ax.text(0.5, 0.925, 'Kiem tra tung muc nay truoc khi an "Dang" de tranh bi xoa bai',
            transform=ax.transAxes, ha='center', va='top',
            fontsize=9.5, color=C_GRAY)

    items = [
        (C_BLUE,   'Nhac nen', 'Lay tu TikTok Sound Library hoac nhac tu san xuat — khong dung nhac YouTube/Spotify'),
        (C_BLUE,   'Hinh anh/video', 'Khong chua logo, thuong hieu hoac khuon mat nguoi khac chua duoc dong y'),
        (C_GREEN,  'Tuyen bo suc khoe', 'Co ghi nguon ro rang; khong dung tu "chua khoi", "100% an toan"'),
        (C_GREEN,  'San pham TikTok Shop', 'Khong thuoc danh sach cam; mo ta san pham dung voi thuc te'),
        (C_GREEN,  'Hashtag', 'Khong chua tu khoa bi cam lien quan den chat cam, noi dung nhay cam'),
        (C_YELLOW, 'Caption', 'Khong chua loi keu goi follow/like kieu spam ("follow toi neu muon xem tiep")'),
        (C_YELLOW, 'Noi dung nhay cam tuoi', 'Bat tuy chon "Danh cho nguoi lon" trong cai dat bai dang'),
        (C_YELLOW, 'Thu thach', 'Khong yeu cau nguoi xem lam hanh dong nguy hiem the chat'),
        (C_RED,    'Link trong bio', 'Dan den trang web hop le — khong phai trang lua dao hoac chua ma doc'),
        (C_RED,    'Tan suat dang', 'Khong qua 5 video/ngay lien tuc (co the kich hoat bo loc spam tu dong)'),
    ]

    y = 0.88
    for i, (color, title, desc) in enumerate(items):
        # Number circle
        circle = plt.Circle((0.04, y - 0.025), 0.018,
                             transform=ax.transAxes,
                             color=color, zorder=3)
        ax.add_patch(circle)
        ax.text(0.04, y - 0.025, str(i+1),
                transform=ax.transAxes,
                ha='center', va='center',
                fontsize=9, fontweight='bold', color=C_WHITE, zorder=4)

        # Row bg
        bg_color = C_LIGHT if i % 2 == 0 else C_WHITE
        ax.add_patch(FancyBboxPatch(
            (0.065, y - 0.057), 0.92, 0.052,
            transform=ax.transAxes,
            boxstyle='round,pad=0.003', facecolor=bg_color, edgecolor='#E5E7EB'
        ))
        ax.text(0.075, y - 0.025, title + ':', transform=ax.transAxes,
                ha='left', va='center', fontsize=9.5, fontweight='bold', color=color)
        ax.text(0.075, y - 0.042, desc, transform=ax.transAxes,
                ha='left', va='center', fontsize=8.5, color=C_DARK)
        y -= 0.075

    ax.text(0.5, 0.015, 'seongon.com | Chinh sach TikTok 2026',
            transform=ax.transAxes, ha='center', va='bottom',
            fontsize=8, color=C_GRAY, style='italic')

    path = os.path.join(OUT, 'infographic-checklist-10-dieu-tranh-vi-pham-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor=C_WHITE)
    plt.close(fig)
    print(f'[OK] infographic-checklist-10-dieu-tranh-vi-pham-tiktok.png ({os.path.getsize(path)//1024}KB)')


# ── DIAGRAM: So do he thong diem vi pham TikTok (Mermaid flowchart) ──────

MERMAID_SODIEM = """flowchart TD
    A([Dang video / Livestream / Ban hang]) --> B{Bi phat hien vi pham?}
    B -- Khong --> Z([Binh thuong])
    B -- Co --> C[TikTok xet muc do]

    C --> D1[Vi pham nhe\\nlan dau]
    C --> D2[Vi pham trung binh\\nhoac lan 2+]
    C --> D3[Vi pham nghiem trong]

    D1 --> E1[CANH BAO\\nXoa video\\nKhong han che chuc nang]
    D2 --> E2[HAN CHE TINH NANG\\n7-30 ngay\\nkhong live, comment, FYF]
    D3 --> E3[KHOA TAI KHOAN\\nTam thoi 24h-30 ngay\\nhoac Vinh vien]

    E1 --> F1{Tich luy >5 lan\\ntrong 90 ngay?}
    F1 -- Co --> E2
    F1 -- Khong --> G1[Ghi nhan\\nHo so vi pham]

    E2 --> H[Khang nghi trong ung dung]
    E3 --> H

    H --> I{Ket qua khang nghi}
    I -- Thanh cong 40-60 percent --> Z
    I -- That bai --> J[Lien he support.tiktok.com]
    J --> K{Lan 2}
    K -- Thanh cong --> Z
    K -- That bai --> L([Chap nhan hoac tao tai khoan moi])
"""


def make_mermaid_html(mermaid_code, title):
    return f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8">
<style>
  * {{ margin:0; padding:0; box-sizing:border-box; }}
  body {{ background:#fff; display:flex; flex-direction:column; align-items:center;
         padding:32px 40px; min-width:900px; }}
  h2 {{ font-family:Arial,sans-serif; font-size:16px; font-weight:bold;
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
    fontSize:'14px',fontFamily:'Arial,sans-serif'}},
  flowchart:{{htmlLabels:true,curve:'linear',nodeSpacing:50,rankSpacing:60,padding:20}}
}});
</script></body></html>"""


async def make_diagrams():
    from playwright.async_api import async_playwright

    jobs = [
        ('tmp_sodiem.html', MERMAID_SODIEM,
         'He Thong Diem Vi Pham TikTok — Tu Canh Bao Den Khoa Tai Khoan',
         'so-do-diem-vi-pham-tiktok.png', 1200, 900, 700),
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
            try:
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
                    await page.set_viewport_size({'width': max(vw, new_w+80), 'height': new_h+100})
                    await page.wait_for_timeout(400)

                out_path = os.path.join(OUT, out_file)
                await page.screenshot(path=out_path, full_page=True)
                size = os.path.getsize(out_path) // 1024
                print(f'[OK] {out_file} ({size}KB)')
            except Exception as e:
                print(f'[WARN] Diagram {out_file} failed: {e}')
            finally:
                if os.path.exists(html_path):
                    os.remove(html_path)

        await browser.close()


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/4] infographic-3-loai-chinh-sach-tiktok.png ...')
    make_chart_1()
    print('[2/4] bang-tu-bi-cam-tiktok-shop.png ...')
    make_chart_2()
    print('[3/4] infographic-checklist-10-dieu-tranh-vi-pham-tiktok.png ...')
    make_chart_3()
    print('[4/4] so-do-diem-vi-pham-tiktok.png (Mermaid) ...')
    asyncio.run(make_diagrams())
    print('Done!')
