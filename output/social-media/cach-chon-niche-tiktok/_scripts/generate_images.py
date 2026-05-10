"""
Generate 2 images for cach-chon-niche-tiktok article:
  1. so-do-loc-niche-tiktok.png      -- funnel diagram (900x500)
  2. bang-30-niche-tiktok-viet-nam.png -- 30-niche summary table (1000x600)
"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\cach-chon-niche-tiktok\images"
os.makedirs(OUT, exist_ok=True)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ─────────────────────────────────────────────
# IMAGE 1 -- Funnel: Broad → Sub-niche → Micro-niche
# ─────────────────────────────────────────────
def make_funnel():
    fig, ax = plt.subplots(figsize=(10, 5.5))
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(5, 9.5, 'Quy trinh chon niche TikTok: tu Broad → Micro-niche',
            ha='center', va='center', fontsize=13, fontweight='bold', color='#111827')

    levels = [
        (6.5, '#DBEAFE', '#3B82F6', 'BROAD TOPIC', 'Rong, canh tranh cao', 'VD: "Suc khoe"', 4.0),
        (5.0, '#D1FAE5', '#10B981', 'SUB-NICHE',   'Vua, de noi bat hon',  'VD: "Tap gym tai nha"', 3.0),
        (3.5, '#FEF3C7', '#F59E0B', 'MICRO-NICHE', 'Hep, tang truong nhanh','VD: "Workout khong dung cu\ncho dan van phong"', 2.2),
    ]

    y_positions = [8.2, 5.9, 3.5]
    for (width, fill, border, title, subtitle, example, _), y in zip(levels, y_positions):
        half = width / 2
        trapezoid = mpatches.FancyBboxPatch(
            (5 - half, y - 0.9), width, 1.5,
            boxstyle='round,pad=0.15',
            facecolor=fill, edgecolor=border, linewidth=2
        )
        ax.add_patch(trapezoid)
        ax.text(5, y + 0.3, title, ha='center', va='center',
                fontsize=11, fontweight='bold', color=border)
        ax.text(5, y - 0.15, subtitle, ha='center', va='center',
                fontsize=8.5, color='#374151')
        ax.text(5, y - 0.6, example, ha='center', va='center',
                fontsize=8, color='#6B7280', style='italic', linespacing=1.3)

    # Arrows between levels
    for y_top, y_bot in [(y_positions[0]-0.9, y_positions[1]+0.6),
                          (y_positions[1]-0.9, y_positions[2]+0.6)]:
        ax.annotate('', xy=(5, y_bot), xytext=(5, y_top),
                    arrowprops=dict(arrowstyle='->', color='#9CA3AF', lw=2.5))

    # Labels on right side
    labels_right = [
        (y_positions[0], '100+ kenh canh tranh', '#EF4444'),
        (y_positions[1], '20-50 kenh canh tranh', '#F59E0B'),
        (y_positions[2], '1-5 kenh canh tranh', '#10B981'),
    ]
    for y, text, color in labels_right:
        ax.text(8.8, y, text, ha='center', va='center',
                fontsize=8.5, color=color, fontweight='bold')
        ax.plot([5 + levels[labels_right.index((y, text, color))][0]/2 + 0.1, 7.2],
                [y, y], color=color, lw=1, linestyle='--', alpha=0.6)

    ax.text(5, 0.35, 'Chien luoc: Bat dau Micro-niche → Xay 10K follower → Mo rong tu nhien | seongon.com',
            ha='center', va='center', fontsize=7.5, color='#9CA3AF', style='italic')

    plt.tight_layout(pad=0.3)
    path = os.path.join(OUT, 'so-do-loc-niche-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close(fig)
    print(f'[OK] so-do-loc-niche-tiktok.png ({os.path.getsize(path)//1024}KB)')


# ─────────────────────────────────────────────
# IMAGE 2 -- 30-niche summary table
# ─────────────────────────────────────────────
def make_niche_table():
    fig, ax = plt.subplots(figsize=(13, 7.5))
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.axis('off')

    ax.text(0.5, 0.97, '30 niche TikTok tiem nang - Thi truong Viet Nam 2026',
            ha='center', va='top', transform=ax.transAxes,
            fontsize=13, fontweight='bold', color='#111827')
    ax.text(0.5, 0.93, '(Chon theo 3 tieu chi: Demand cao + Canh tranh vua + Monetize ro rang)',
            ha='center', va='top', transform=ax.transAxes,
            fontsize=9, color='#6B7280', style='italic')

    groups = [
        ('#3B82F6', 'Tai chinh &\nDau tu', [
            ('Tai chinh ca nhan', 'TB'), ('Chung khoan F0', 'Cao'),
            ('Quan ly chi tieu', 'Thap'), ('Bao hiem', 'Thap'), ('Freelance', 'TB'),
        ]),
        ('#10B981', 'Suc khoe &\nThe chat', [
            ('Tap gym tai nha', 'TB'), ('Meal prep', 'TB'),
            ('Suc khoe tam than', 'Thap'), ('Yoga buoi sang', 'Cao'), ('Skincare nam', 'Thap'),
        ]),
        ('#8B5CF6', 'Hoc tap &\nPhat trien', [
            ('Tieng Anh giao tiep', 'Cao'), ('Review sach', 'TB'),
            ('Ky nang mem', 'Thap'), ('Lap trinh Python', 'TB'), ('Productivity', 'Thap'),
        ]),
        ('#F59E0B', 'Am thuc &\nDoi song', [
            ('Mon an nhanh', 'TB'), ('Banh khong lo nuong', 'TB'),
            ('Review quan an', 'Cao'), ('Trong cay nha', 'Thap'), ('Decor phong tro', 'Thap'),
        ]),
        ('#EF4444', 'Cong nghe\n& AI', [
            ('AI tools mien phi', 'TB'), ('Review dien thoai', 'Cao'),
            ('Meo smartphone', 'TB'), ('No-code tools', 'Thap'), ('Game mobile VN', 'Cao'),
        ]),
        ('#06B6D4', 'Kinh doanh\n& Marketing', [
            ('Kinh doanh online', 'TB'), ('TikTok Shop', 'Thap'),
            ('Canva design', 'TB'), ('Freelance writing', 'Thap'), ('Personal branding', 'Thap'),
        ]),
    ]

    competition_colors = {'Cao': '#FEE2E2', 'TB': '#FEF3C7', 'Thap': '#D1FAE5'}
    competition_text   = {'Cao': '#B91C1C', 'TB': '#92400E', 'Thap': '#065F46'}

    cols = 3
    col_width  = 1.0 / cols
    row_height = 1.0 / (len(groups) // cols + 1)

    cell_x_pad = 0.01
    cell_y_pad = 0.01

    for idx, (color, group_name, niches) in enumerate(groups):
        col_i = idx % cols
        row_i = idx // cols
        x0 = col_i * col_width + 0.01
        y0 = 0.88 - row_i * 0.44

        # Group header
        hdr = FancyBboxPatch((x0, y0 - 0.06), col_width - 0.02, 0.075,
                              boxstyle='round,pad=0.01',
                              facecolor=color, edgecolor='none',
                              transform=ax.transAxes)
        ax.add_patch(hdr)
        ax.text(x0 + (col_width - 0.02)/2, y0 - 0.022, group_name,
                ha='center', va='center', transform=ax.transAxes,
                fontsize=9, fontweight='bold', color='white', linespacing=1.2)

        # Niche rows
        niche_row_h = 0.060
        for ni, (niche, comp) in enumerate(niches):
            ry = y0 - 0.065 - ni * niche_row_h - 0.005
            bg = '#FFFFFF' if ni % 2 == 0 else '#F9FAFB'
            row_box = FancyBboxPatch((x0, ry), col_width - 0.02, niche_row_h - 0.003,
                                     boxstyle='square,pad=0.0',
                                     facecolor=bg, edgecolor='#E5E7EB', linewidth=0.5,
                                     transform=ax.transAxes)
            ax.add_patch(row_box)
            ax.text(x0 + 0.01, ry + niche_row_h/2 - 0.003, niche,
                    ha='left', va='center', transform=ax.transAxes,
                    fontsize=7.8, color='#111827')
            # Competition badge
            badge_w = 0.055
            badge_x = x0 + col_width - 0.02 - badge_w - 0.005
            badge = FancyBboxPatch((badge_x, ry + 0.007), badge_w, niche_row_h - 0.018,
                                   boxstyle='round,pad=0.005',
                                   facecolor=competition_colors[comp],
                                   edgecolor='none',
                                   transform=ax.transAxes)
            ax.add_patch(badge)
            ax.text(badge_x + badge_w/2, ry + niche_row_h/2 - 0.003, comp,
                    ha='center', va='center', transform=ax.transAxes,
                    fontsize=7, color=competition_text[comp], fontweight='bold')

    # Legend
    legend_items = [('Canh tranh Cao', '#FEE2E2', '#B91C1C'),
                    ('Canh tranh TB',  '#FEF3C7', '#92400E'),
                    ('Canh tranh Thap','#D1FAE5', '#065F46')]
    lx = 0.01
    for label, bg, tc in legend_items:
        b = FancyBboxPatch((lx, 0.01), 0.14, 0.04,
                           boxstyle='round,pad=0.005', facecolor=bg, edgecolor='#D1D5DB',
                           transform=ax.transAxes)
        ax.add_patch(b)
        ax.text(lx + 0.07, 0.03, label, ha='center', va='center',
                transform=ax.transAxes, fontsize=7.5, color=tc, fontweight='bold')
        lx += 0.16

    ax.text(0.98, 0.01, 'seongon.com -- Du lieu tham khao 2026',
            ha='right', va='bottom', transform=ax.transAxes,
            fontsize=7, color='#9CA3AF', style='italic')

    plt.tight_layout(pad=0.3)
    path = os.path.join(OUT, 'bang-30-niche-tiktok-viet-nam.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close(fig)
    print(f'[OK] bang-30-niche-tiktok-viet-nam.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/2] Funnel diagram...')
    make_funnel()
    print('[2/2] 30-niche table...')
    make_niche_table()
    print('Done! 2 anh da tao tai:', OUT)
