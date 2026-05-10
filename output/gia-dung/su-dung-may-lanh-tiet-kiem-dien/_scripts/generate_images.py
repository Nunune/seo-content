"""
Tạo 4 ảnh cho bài: sử dụng máy lạnh tiết kiệm điện
- chart_1.png  : Bar chart tiêu thụ điện theo nhiệt độ (matplotlib)
- chart_2.png  : Grouped bar chart chi phí điện theo HP/giờ (matplotlib)
- diagram_1.png: Mindmap 10 mẹo (Playwright + Mermaid.js)
- diagram_2.png: Flowchart vệ sinh bộ lọc (Playwright + Mermaid.js)
"""
import os, sys, time, textwrap
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\gia-dung\su-dung-may-lanh-tiet-kiem-dien\images"
os.makedirs(OUT, exist_ok=True)

# ── FONT ───────────────────────────────────────────────
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ═══════════════════════════════════════════════════════
# CHART 1 — Tiêu thụ điện theo nhiệt độ cài đặt
# ═══════════════════════════════════════════════════════
def make_chart1():
    labels  = ['20°C', '22°C', '24°C\n(tham chiếu)', '26°C ⭐\n(khuyến nghị)', '28°C']
    values  = [150, 120, 100, 85, 70]
    colors  = ['#EF4444', '#F59E0B', '#6B7280', '#10B981', '#3B82F6']
    edge    = ['#DC2626', '#D97706', '#4B5563', '#059669', '#2563EB']

    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F9FAFB')

    bars = ax.bar(labels, values, color=colors, edgecolor=edge, linewidth=1.2,
                  width=0.55, zorder=3)

    # Value labels on bars
    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1.5,
                f'{val}%', ha='center', va='bottom', fontsize=12,
                fontweight='bold', color='#111827')

    ax.set_ylim(0, 175)
    ax.set_xlabel('Nhiệt độ cài đặt máy lạnh', fontsize=12, color='#374151', labelpad=8)
    ax.set_ylabel('Mức tiêu thụ điện (%)', fontsize=12, color='#374151', labelpad=8)
    ax.set_title('Mức Tiêu Thụ Điện Theo Nhiệt Độ Cài Đặt Máy Lạnh',
                 fontsize=15, fontweight='bold', color='#111827', pad=14)
    ax.tick_params(colors='#374151', labelsize=11)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{int(v)}%'))
    ax.grid(axis='y', color='#E5E7EB', linewidth=0.8, zorder=0)
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['bottom','left']].set_color('#D1D5DB')

    ax.annotate('Nguồn: EVN, Panasonic Vietnam',
                xy=(1, 0), xycoords='axes fraction',
                fontsize=9, color='#9CA3AF', ha='right', va='bottom',
                xytext=(0, -38), textcoords='offset points')

    fig.tight_layout()
    path = os.path.join(OUT, 'chart_1.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'✅ chart_1.png saved ({os.path.getsize(path)//1024}KB)')

# ═══════════════════════════════════════════════════════
# CHART 2 — Chi phí điện theo công suất và giờ dùng
# ═══════════════════════════════════════════════════════
def make_chart2():
    labels   = ['1 HP\n(9.000 BTU)', '1.5 HP\n(12.000 BTU)', '2 HP\n(18.000 BTU)', '2.5 HP\n(24.000 BTU)']
    h6  = [89400,  134000, 178700, 223400]
    h8  = [119200, 178600, 238300, 297800]
    h10 = [149000, 223300, 297800, 372300]

    x   = np.arange(len(labels))
    w   = 0.26

    fig, ax = plt.subplots(figsize=(11, 6.5))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F9FAFB')

    b1 = ax.bar(x - w,   h6,  width=w, label='6 giờ/ngày',  color='#3B82F6', edgecolor='#2563EB', linewidth=0.8, zorder=3)
    b2 = ax.bar(x,       h8,  width=w, label='8 giờ/ngày',  color='#10B981', edgecolor='#059669', linewidth=0.8, zorder=3)
    b3 = ax.bar(x + w,   h10, width=w, label='10 giờ/ngày', color='#F59E0B', edgecolor='#D97706', linewidth=0.8, zorder=3)

    def fmt(v):
        return f'{v//1000}k'

    for bars in [b1, b2, b3]:
        for bar in bars:
            h = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2, h + 3000,
                    fmt(h), ha='center', va='bottom', fontsize=9,
                    color='#374151', fontweight='bold')

    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=11, color='#374151')
    ax.set_ylabel('Chi phí điện (đồng/tháng)', fontsize=12, color='#374151', labelpad=8)
    ax.set_title('Chi Phí Điện Máy Lạnh Mỗi Tháng (VNĐ)',
                 fontsize=15, fontweight='bold', color='#111827', pad=14)
    ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{int(v/1000)}k'))
    ax.tick_params(colors='#374151', labelsize=10)
    ax.set_ylim(0, 430000)
    ax.grid(axis='y', color='#E5E7EB', linewidth=0.8, zorder=0)
    ax.spines[['top','right']].set_visible(False)
    ax.spines[['bottom','left']].set_color('#D1D5DB')
    ax.legend(fontsize=11, framealpha=0.8, edgecolor='#E5E7EB')

    ax.annotate('Giá điện bậc 3: 2.858 đ/kWh (EVN, 2024) · Hệ số tải 0.7 · Máy Inverter tiết kiệm thêm 15–20%',
                xy=(0.5, 0), xycoords='axes fraction',
                fontsize=9, color='#9CA3AF', ha='center', va='bottom',
                xytext=(0, -42), textcoords='offset points')

    fig.tight_layout()
    path = os.path.join(OUT, 'chart_2.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'✅ chart_2.png saved ({os.path.getsize(path)//1024}KB)')

# ═══════════════════════════════════════════════════════
# DIAGRAM 1 — Mindmap 10 mẹo (Playwright + Mermaid.js)
# ═══════════════════════════════════════════════════════
MERMAID_DIAGRAM1 = """
mindmap
  root((10 Mẹo<br/>Tiết Kiệm Điện<br/>Máy Lạnh))
    Cài đặt nhiệt độ
      1. Đặt 25-27°C
      2. Không bật tắt liên tục
    Tối ưu vận hành
      3. Kết hợp quạt
      7. Dùng chế độ Dry
      8. Hẹn giờ khi ngủ
    Môi trường phòng
      5. Che chắn cục nóng
      6. Đóng kín cửa
    Bảo trì định kỳ
      4. Vệ sinh bộ lọc 3-6 tháng
    Chọn thiết bị đúng
      9. Máy Inverter
      10. Đúng công suất BTU
"""

MERMAID_DIAGRAM2 = """
flowchart TD
    A["🔌 Bước 1: Tắt máy lạnh<br/>hoàn toàn"] --> B["🔧 Bước 2: Mở nắp, tháo<br/>bộ lọc không khí"]
    B --> C["💧 Bước 3: Rửa nhẹ bằng<br/>nước sạch hoặc hút bụi"]
    C --> D["☀️ Bước 4: Để khô tự nhiên<br/>hoàn toàn 15-30 phút"]
    D --> E["✅ Bước 5: Lắp lại bộ lọc<br/>đúng vị trí, bật kiểm tra"]
    E --> F{Còn bẩn?}
    F -->|Có| C
    F -->|Không| G["🎉 Hoàn thành!<br/>Nhắc lịch sau 3-6 tháng"]

    style A fill:#3B82F6,stroke:#2563EB,color:#FFFFFF
    style B fill:#3B82F6,stroke:#2563EB,color:#FFFFFF
    style C fill:#3B82F6,stroke:#2563EB,color:#FFFFFF
    style D fill:#3B82F6,stroke:#2563EB,color:#FFFFFF
    style E fill:#3B82F6,stroke:#2563EB,color:#FFFFFF
    style F fill:#F59E0B,stroke:#D97706,color:#FFFFFF
    style G fill:#10B981,stroke:#059669,color:#FFFFFF
"""

def make_mermaid_html(mermaid_code, title):
    escaped = mermaid_code.replace('`', r'\`').replace('$', r'\$')
    return f"""<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{ background: #fff; display: flex; flex-direction: column; align-items: center; padding: 24px; }}
  h2 {{ font-family: Arial, sans-serif; font-size: 16px; color: #111827; margin-bottom: 16px; }}
  #diagram {{ width: 100%; }}
  .mermaid {{ display: flex; justify-content: center; }}
</style>
</head>
<body>
<h2>{title}</h2>
<div id="diagram" class="mermaid">
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
      tertiaryColor: '#fff',
      fontSize: '14px'
    }},
    flowchart: {{ htmlLabels: true, curve: 'linear' }},
    mindmap: {{ padding: 16 }}
  }});
</script>
</body>
</html>"""

def make_diagrams_playwright():
    import asyncio
    from playwright.async_api import async_playwright

    async def _run():
        html_dir = r"D:\Nunu-Claude\seo_content\output\images\su-dung-may-lanh-tiet-kiem-dien"
        jobs = [
            ('diagram_1.html', MERMAID_DIAGRAM1, '10 Mẹo Sử Dụng Máy Lạnh Tiết Kiệm Điện', 'diagram_1.png', 1100, 700),
            ('diagram_2.html', MERMAID_DIAGRAM2, 'Quy Trình Vệ Sinh Bộ Lọc Máy Lạnh', 'diagram_2.png', 700, 750),
        ]

        async with async_playwright() as p:
            browser = await p.chromium.launch(headless=True)
            for html_file, code, title, out_file, vw, vh in jobs:
                html_content = make_mermaid_html(code, title)
                html_path = os.path.join(html_dir, html_file)
                with open(html_path, 'w', encoding='utf-8') as f:
                    f.write(html_content)

                page = await browser.new_page(viewport={'width': vw, 'height': vh})
                await page.goto(f'file:///{html_path}')
                # Wait for mermaid to render
                await page.wait_for_selector('.mermaid svg', timeout=15000)
                await page.wait_for_timeout(1500)

                out_path = os.path.join(html_dir, out_file)
                await page.screenshot(path=out_path, full_page=True)
                print(f'✅ {out_file} saved ({os.path.getsize(out_path)//1024}KB)')

                # Clean up temp HTML
                os.remove(html_path)

            await browser.close()

    asyncio.run(_run())

if __name__ == '__main__':
    import sys
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/4] Tao chart_1.png (tieu thu dien theo nhiet do)...')
    make_chart1()

    print('[2/4] Tao chart_2.png (chi phi dien theo HP/gio)...')
    make_chart2()

    print('[3/4] Tao diagram_1.png + diagram_2.png (Playwright + Mermaid)...')
    make_diagrams_playwright()

    print('\nDone! Tat ca anh da luu tai:')
    print(f'  {OUT}')
