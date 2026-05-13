"""
Generate 3 images for xay-kenh-tiktok-tu-con-so-0 article:
  1. so-do-6-buoc-xay-kenh-tiktok.png      -- flowchart 6 buoc (matplotlib)
  2. content-pillar-tiktok-ti-le.png       -- pie chart content pillar (matplotlib)
  3. bang-theo-doi-tang-truong-kenh-tiktok.png -- growth tracking table (matplotlib)
"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\xay-kenh-tiktok-tu-con-so-0\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ─────────────────────────────────────────────
# IMAGE 1 -- 6-step flowchart
# ─────────────────────────────────────────────
def make_chart_1():
    fig, ax = plt.subplots(figsize=(12, 5))
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis('off')

    ax.text(6, 4.6, 'Quy trinh xay kenh TikTok tu con so 0 -- 6 buoc co thu tu',
            ha='center', va='center', fontsize=13, fontweight='bold', color='#111827')

    steps = [
        ('1', 'Chon\nNiche', '#3B82F6', 'Ngay 1-2'),
        ('2', 'Setup\nProfile', '#8B5CF6', 'Ngay 3'),
        ('3', 'Nghien cuu\nContent', '#10B981', 'Ngay 4-8'),
        ('4', 'San xuat\nVideo', '#F59E0B', 'Lien tuc'),
        ('5', 'Dang &\nToi uu', '#EF4444', 'Lien tuc'),
        ('6', 'Phan tich\nDu lieu', '#6366F1', 'Hang tuan'),
    ]

    xs = [1.0, 2.9, 4.8, 6.7, 8.6, 10.5]
    y_center = 2.5
    box_w, box_h = 1.5, 1.8

    for i, ((num, label, color, timeline), x) in enumerate(zip(steps, xs)):
        rect = FancyBboxPatch((x - box_w/2, y_center - box_h/2), box_w, box_h,
                              boxstyle='round,pad=0.12', facecolor=color, edgecolor='white',
                              linewidth=2, zorder=3)
        ax.add_patch(rect)

        ax.text(x, y_center + 0.35, num, ha='center', va='center',
                fontsize=18, fontweight='bold', color='white', zorder=4)
        ax.text(x, y_center - 0.25, label, ha='center', va='center',
                fontsize=9, color='white', zorder=4, linespacing=1.4)
        ax.text(x, y_center - box_h/2 - 0.25, timeline, ha='center', va='center',
                fontsize=8, color='#6B7280', zorder=4)

        if i < len(steps) - 1:
            ax.annotate('', xy=(xs[i+1] - box_w/2 - 0.05, y_center),
                        xytext=(x + box_w/2 + 0.05, y_center),
                        arrowprops=dict(arrowstyle='->', color='#9CA3AF', lw=2))

    ax.text(6, 0.4, 'Nguon: seongon.com -- Quy trinh thuc chien xay kenh TikTok 2026',
            ha='center', va='center', fontsize=7.5, color='#9CA3AF', style='italic')

    plt.tight_layout(pad=0.5)
    path = os.path.join(OUT, 'so-do-6-buoc-xay-kenh-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close(fig)
    print(f'[OK] so-do-6-buoc-xay-kenh-tiktok.png ({os.path.getsize(path)//1024}KB)')


# ─────────────────────────────────────────────
# IMAGE 2 -- Content Pillar pie chart
# ─────────────────────────────────────────────
def make_chart_2():
    fig, (ax_pie, ax_legend) = plt.subplots(1, 2, figsize=(9, 5),
                                             gridspec_kw={'width_ratios': [1, 1]})
    fig.patch.set_facecolor('#F8FAFC')

    labels = ['Education\n(Giao duc)', 'Entertainment\n(Giai tri)', 'Engagement\n(Tuong tac)']
    sizes = [50, 30, 20]
    colors = ['#3B82F6', '#F59E0B', '#10B981']
    explode = (0.05, 0.05, 0.05)

    wedges, texts, autotexts = ax_pie.pie(
        sizes, explode=explode, labels=None,
        colors=colors, autopct='%1.0f%%',
        startangle=90, pctdistance=0.7,
        wedgeprops=dict(linewidth=2, edgecolor='white')
    )
    for autotext in autotexts:
        autotext.set_fontsize(14)
        autotext.set_fontweight('bold')
        autotext.set_color('white')

    ax_pie.set_title('Ti le 3 loai Content Pillar\nkhi xay kenh TikTok',
                     fontsize=12, fontweight='bold', color='#111827', pad=15)
    ax_pie.set_facecolor('#F8FAFC')

    # Legend panel
    ax_legend.axis('off')
    ax_legend.set_facecolor('#F8FAFC')

    legend_data = [
        ('#3B82F6', 'Education (50%)', '"3 loi nguoi moi hay mac"', '"Huong dan lam X"'),
        ('#F59E0B', 'Entertainment (30%)', 'POV, trend, thu thach', 'Noi dung vui, chia se'),
        ('#10B981', 'Engagement (20%)', 'Q&A, poll, hoi cong dong', '"Binh luan X neu ban..."'),
    ]
    y_start = 0.85
    for color, title, ex1, ex2 in legend_data:
        rect = FancyBboxPatch((0.02, y_start - 0.15), 0.96, 0.28,
                              boxstyle='round,pad=0.02',
                              facecolor=color + '20', edgecolor=color,
                              linewidth=1.5, transform=ax_legend.transAxes)
        ax_legend.add_patch(rect)
        ax_legend.text(0.07, y_start + 0.04, title, transform=ax_legend.transAxes,
                       fontsize=10, fontweight='bold', color=color, va='center')
        ax_legend.text(0.07, y_start - 0.06, f'VD: {ex1}', transform=ax_legend.transAxes,
                       fontsize=8, color='#374151', va='center')
        y_start -= 0.34

    ax_legend.text(0.5, 0.02, 'Nguon: seongon.com', ha='center', va='bottom',
                   transform=ax_legend.transAxes, fontsize=7.5, color='#9CA3AF', style='italic')

    plt.tight_layout(pad=1.0)
    path = os.path.join(OUT, 'content-pillar-tiktok-ti-le.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close(fig)
    print(f'[OK] content-pillar-tiktok-ti-le.png ({os.path.getsize(path)//1024}KB)')


# ─────────────────────────────────────────────
# IMAGE 3 -- Growth tracking table
# ─────────────────────────────────────────────
def make_chart_3():
    fig, ax = plt.subplots(figsize=(10, 4.5))
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.axis('off')

    ax.text(0.5, 0.96, 'Bang theo doi chi so tang truong kenh TikTok theo tuan',
            ha='center', va='top', transform=ax.transAxes,
            fontsize=12, fontweight='bold', color='#111827')

    col_labels = ['Tuan', 'So video', 'Follower', 'View TB', 'Completion\nRate', 'Follow\nRate', 'Ghi chu']
    col_widths = [0.10, 0.10, 0.12, 0.12, 0.14, 0.12, 0.30]

    rows = [
        ['Tuan 1',  '7',   '45',    '380',   '62%', '1.2%', 'Dang 1/ngay, test hook'],
        ['Tuan 2',  '7',   '120',   '520',   '67%', '1.8%', 'Format nghi van hoat dong tot'],
        ['Tuan 3',  '7',   '280',   '890',   '71%', '2.1%', 'Video #14 dat 8K view'],
        ['Tuan 4',  '7',   '510',   '1.240', '74%', '2.4%', 'Dat 500 follower, tang toc'],
        ['Tuan 8',  '28',  '1.050', '2.100', '76%', '2.9%', '1K follower, bat dau collab'],
        ['Thang 3', '90+', '3.500', '3.800', '79%', '3.2%', 'Bat dau nhan Brand Deal nho'],
    ]

    header_colors = ['#1E40AF'] * len(col_labels)
    row_colors = [['#EFF6FF' if i % 2 == 0 else '#FFFFFF'] * len(col_labels) for i in range(len(rows))]

    # Draw header
    x_positions = []
    x = 0.01
    for w in col_widths:
        x_positions.append(x + w/2)
        x += w

    y_header = 0.82
    x = 0.01
    for j, (label, w, color) in enumerate(zip(col_labels, col_widths, header_colors)):
        rect = FancyBboxPatch((x, y_header - 0.06), w - 0.005, 0.12,
                              boxstyle='square,pad=0.0', facecolor=color,
                              edgecolor='white', linewidth=1,
                              transform=ax.transAxes)
        ax.add_patch(rect)
        ax.text(x + w/2, y_header, label, ha='center', va='center',
                transform=ax.transAxes, fontsize=8.5, fontweight='bold',
                color='white', linespacing=1.3)
        x += w

    # Draw data rows
    row_height = 0.10
    y_start = 0.70
    for i, row in enumerate(rows):
        bg = '#EFF6FF' if i % 2 == 0 else '#FFFFFF'
        x = 0.01
        for j, (cell, w) in enumerate(zip(row, col_widths)):
            rect = FancyBboxPatch((x, y_start - i*row_height - 0.05), w - 0.005, row_height,
                                  boxstyle='square,pad=0.0', facecolor=bg,
                                  edgecolor='#E5E7EB', linewidth=0.5,
                                  transform=ax.transAxes)
            ax.add_patch(rect)
            color = '#1E40AF' if j == 0 else '#111827'
            bold = (j == 0)
            ax.text(x + w/2, y_start - i*row_height, cell, ha='center', va='center',
                    transform=ax.transAxes, fontsize=8, color=color,
                    fontweight='bold' if bold else 'normal')
            x += w

    ax.text(0.5, 0.02, 'Bang minh hoa -- con so tham khao trung binh | seongon.com',
            ha='center', va='bottom', transform=ax.transAxes,
            fontsize=7.5, color='#9CA3AF', style='italic')

    plt.tight_layout(pad=0.3)
    path = os.path.join(OUT, 'bang-theo-doi-tang-truong-kenh-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close(fig)
    print(f'[OK] bang-theo-doi-tang-truong-kenh-tiktok.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/3] Flowchart 6 buoc...')
    make_chart_1()
    print('[2/3] Pie chart content pillar...')
    make_chart_2()
    print('[3/3] Bang theo doi tang truong...')
    make_chart_3()
    print('Done! 3 anh da tao tai:', OUT)
