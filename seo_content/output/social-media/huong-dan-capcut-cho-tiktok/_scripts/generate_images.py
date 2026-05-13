"""
Generate 2 images for huong-dan-capcut-cho-tiktok article:
  1. giao-dien-capcut-chu-thich.png      -- CapCut UI mockup with labels (1000x600)
  2. capcut-timeline-before-after.png    -- Before/After timeline comparison (1000x500)
"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import matplotlib.patches as mpatches

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\huong-dan-capcut-cho-tiktok\images"
os.makedirs(OUT, exist_ok=True)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ─────────────────────────────────────────────
# IMAGE 1 -- CapCut UI Mockup with labels
# ─────────────────────────────────────────────
def make_ui_mockup():
    fig, ax = plt.subplots(figsize=(12, 7))
    fig.patch.set_facecolor('#1C1C1E')
    ax.set_facecolor('#1C1C1E')
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 7)
    ax.axis('off')

    def box(x, y, w, h, fc, ec='#3A3A3C', lw=1):
        p = FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.08',
                           facecolor=fc, edgecolor=ec, linewidth=lw, zorder=2)
        ax.add_patch(p)

    def label(x, y, text, size=8.5, color='white', bold=False, ha='center', va='center'):
        ax.text(x, y, text, ha=ha, va=va, fontsize=size, color=color,
                fontweight='bold' if bold else 'normal', zorder=5)

    def callout(ax_x, ax_y, label_x, label_y, text, color='#F59E0B'):
        ax.annotate(text,
            xy=(ax_x, ax_y), xytext=(label_x, label_y),
            fontsize=8, color='#1C1C1E', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.35', facecolor=color, edgecolor='none', alpha=0.95),
            arrowprops=dict(arrowstyle='->', color=color, lw=1.5),
            zorder=6)

    # Title bar
    box(0.1, 6.3, 11.8, 0.55, '#2C2C2E')
    label(1.5, 6.57, '< Back', 8.5, '#3B82F6')
    label(6, 6.57, 'CapCut  --  Du an moi', 9, '#FFFFFF', bold=True)
    label(10.8, 6.57, 'Xuat', 8.5, '#3B82F6')

    # Preview panel (center)
    box(3.5, 2.5, 5.0, 3.7, '#000000', '#3A3A3C', lw=2)
    label(6.0, 4.35, '[PREVIEW VIDEO]', 9, '#555555', bold=True)
    # Vertical phone frame hint
    box(4.8, 2.65, 2.4, 3.35, '#111111', '#3B82F6', lw=1.5)
    label(6.0, 4.32, 'Preview', 7, '#888888')
    # Play button
    ax.plot([5.85, 5.85, 6.25], [4.05, 3.75, 3.9], color='#FFFFFF', lw=2, zorder=5)

    # Left toolbar
    box(0.1, 2.5, 1.5, 3.7, '#2C2C2E')
    label(0.85, 6.0, 'CONG CU', 7, '#9CA3AF', bold=True)
    tools = ['Cat/Ghep', 'Sub', 'Text', 'Nhac', 'Bo loc', 'Hieu ung']
    for i, t in enumerate(tools):
        fy = 5.55 - i * 0.52
        box(0.18, fy - 0.18, 1.34, 0.38, '#3A3A3C' if i != 1 else '#3B82F6')
        label(0.85, fy, t, 8, '#FFFFFF' if i != 1 else '#FFFFFF')

    # Right panel (properties)
    box(8.6, 2.5, 3.3, 3.7, '#2C2C2E')
    label(10.25, 6.0, 'THUOC TINH', 7, '#9CA3AF', bold=True)
    props = [
        ('Do phan giai:', '1080p'),
        ('FPS:', '30 fps'),
        ('Watermark:', 'Tat'),
        ('Dinh dang:', 'MP4'),
        ('Chat luong:', 'Cao'),
    ]
    for i, (k, v) in enumerate(props):
        py = 5.55 - i * 0.52
        label(8.85, py, k, 7.5, '#9CA3AF', ha='left')
        label(11.7, py, v, 7.5, '#10B981', ha='right')

    # Timeline bar at bottom
    box(0.1, 0.8, 11.8, 1.55, '#2C2C2E')
    label(6, 2.2, 'TIMELINE', 7, '#9CA3AF', bold=True)
    # Timeline clips
    clip_colors = ['#3B82F6', '#8B5CF6', '#10B981', '#F59E0B', '#EF4444', '#3B82F6', '#8B5CF6']
    clip_widths = [1.4, 0.8, 1.2, 0.6, 1.0, 0.9, 1.1]
    cx = 0.3
    for i, (cc, cw) in enumerate(zip(clip_colors, clip_widths)):
        if cx + cw > 11.8: break
        box(cx, 1.05, cw, 0.7, cc + '55', cc, lw=1)
        if cw > 0.7:
            label(cx + cw/2, 1.4, f'Clip {i+1}', 7, '#FFFFFF')
        cx += cw + 0.08
    # Playhead
    ax.plot([3.8, 3.8], [0.85, 2.35], color='#EF4444', lw=2, zorder=6)
    ax.plot([3.8], [2.35], 'v', color='#EF4444', markersize=8, zorder=6)

    # Time indicator
    label(0.5, 0.88, '00:00', 7, '#9CA3AF')
    label(11.7, 0.88, '00:45', 7, '#9CA3AF')
    label(6, 0.88, '00:22', 7.5, '#EF4444', bold=True)

    # Callout annotations
    callout(0.85, 4.8, 0.2, 4.8, ' A: Cong cu chinh ', '#3B82F6')
    callout(6.0, 3.9, 6.0, 6.78, ' B: Preview ', '#10B981')
    callout(10.25, 4.8, 10.6, 4.8, ' C: Thuoc tinh ', '#8B5CF6')
    callout(3.8, 1.75, 2.2, 1.55, ' D: Timeline + Playhead ', '#F59E0B')

    ax.text(6, 0.35, 'Mo phong giao dien CapCut -- Thuc te co the khac do phien ban | seongon.com',
            ha='center', va='center', fontsize=7, color='#555555', style='italic')

    plt.tight_layout(pad=0.2)
    path = os.path.join(OUT, 'giao-dien-capcut-chu-thich.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#1C1C1E')
    plt.close(fig)
    print(f'[OK] giao-dien-capcut-chu-thich.png ({os.path.getsize(path)//1024}KB)')


# ─────────────────────────────────────────────
# IMAGE 2 -- Before / After timeline comparison
# ─────────────────────────────────────────────
def make_before_after():
    fig, axes = plt.subplots(1, 2, figsize=(13, 5.5),
                             gridspec_kw={'width_ratios': [1, 1]})
    fig.patch.set_facecolor('#F8FAFC')

    titles  = ['TRUOC (Video thu)', 'SAU (Da dung CapCut)']
    bgcols  = ['#FEF2F2', '#F0FDF4']
    hcols   = ['#EF4444', '#10B981']

    # Left: messy raw timeline
    raw_clips = [
        (0.05, 0.55, '#FCA5A5', 'Clip 1\n(dai)', 'X'),
        (0.62, 0.15, '#FBBF24', 'Clip 2', ''),
        (0.79, 0.30, '#FCA5A5', 'Clip 3', ''),
        (1.11, 0.45, '#FBBF24', 'C4 (khong\ncan thiet)', 'X'),
        (1.58, 0.20, '#FCA5A5', 'C5', ''),
        (1.80, 0.35, '#D1D5DB', '...', ''),
    ]
    # Right: clean edited timeline
    edit_clips = [
        (0.05, 0.28, '#6EE7B7', 'Intro\n3s', ''),
        (0.35, 0.40, '#34D399', 'Hook\n5s', ''),
        (0.77, 0.35, '#6EE7B7', 'ND1\n8s', ''),
        (1.14, 0.35, '#34D399', 'ND2\n8s', ''),
        (1.51, 0.32, '#6EE7B7', 'ND3\n7s', ''),
        (1.85, 0.25, '#10B981', 'CTA\n4s', ''),
    ]

    for ax_i, (ax, clips, title, bg, hc, total_dur, extra_row) in enumerate(zip(
        axes,
        [raw_clips, edit_clips],
        titles, bgcols, hcols,
        ['~2:30', '~35 giay'],
        [True, False]
    )):
        ax.set_facecolor(bg)
        ax.set_xlim(0, 2.3)
        ax.set_ylim(-0.25, 2.5)
        ax.axis('off')

        # Header
        hdr = FancyBboxPatch((0, 2.2), 2.3, 0.28,
                              boxstyle='round,pad=0.04', facecolor=hc, edgecolor='none')
        ax.add_patch(hdr)
        ax.text(1.15, 2.34, title, ha='center', va='center',
                fontsize=11, fontweight='bold', color='white')

        # Timeline track
        ax.add_patch(FancyBboxPatch((0, 0.85), 2.3, 0.6,
                     boxstyle='square,pad=0', facecolor='#E5E7EB', edgecolor='#D1D5DB'))

        # Clips
        for cx, cw, cc, lbl, mark in clips:
            p = FancyBboxPatch((cx, 0.87), cw, 0.56,
                               boxstyle='round,pad=0.03', facecolor=cc,
                               edgecolor='white', linewidth=1.5)
            ax.add_patch(p)
            ax.text(cx + cw/2, 1.15, lbl, ha='center', va='center',
                    fontsize=7.5, color='#1C1C1E', linespacing=1.3)
            if mark == 'X':
                ax.text(cx + cw - 0.03, 0.9 + 0.5, 'X', ha='right', va='top',
                        fontsize=10, color='#EF4444', fontweight='bold')

        # Duration label
        ax.text(2.2, 0.7, f'Tong: {total_dur}', ha='right', va='center',
                fontsize=8.5, color=hc, fontweight='bold')

        # Audio track
        ax.add_patch(FancyBboxPatch((0, 0.55), 2.3, 0.25,
                     boxstyle='square,pad=0', facecolor='#FEF3C7' if ax_i == 0 else '#D1FAE5',
                     edgecolor='#E5E7EB'))
        ax.text(0.05, 0.675, 'Nhac nen' if ax_i == 1 else 'Khong nhac', ha='left', va='center',
                fontsize=7.5, color='#92400E' if ax_i == 0 else '#065F46')

        # Caption track
        cap_col = '#D1D5DB' if ax_i == 0 else '#BFDBFE'
        ax.add_patch(FancyBboxPatch((0, 0.28), 2.3, 0.22,
                     boxstyle='square,pad=0', facecolor=cap_col, edgecolor='#E5E7EB'))
        ax.text(0.05, 0.39, 'Phu de: chua co' if ax_i == 0 else 'Auto Caption (30s)',
                ha='left', va='center', fontsize=7.5,
                color='#6B7280' if ax_i == 0 else '#1E40AF')

        # Track labels on left
        for y, lbl, fc in [(1.15, 'Video', '#6B7280'), (0.675, 'Audio', '#6B7280'), (0.39, 'Sub', '#6B7280')]:
            ax.text(-0.02, y, lbl, ha='right', va='center', fontsize=7, color=fc)

        # Bottom stats
        if ax_i == 0:
            stats = ['Canh qua dai', 'Khong nhac', 'Khong phu de', 'Thoi gian: ~2h']
            icons = ['X', 'X', 'X', 'X']
            sc = '#EF4444'
        else:
            stats = ['Da cat dung nhip', 'Nhac trending', 'Auto Caption', 'Thoi gian: ~20 phut']
            icons = ['+', '+', '+', '+']
            sc = '#10B981'

        for si, (st, ic) in enumerate(zip(stats, icons)):
            ax.text(0.05 + si * 0.56, -0.1, f'{ic} {st}', ha='left', va='center',
                    fontsize=7.5, color=sc)

    # Center arrow
    fig.text(0.5, 0.52, '  →  CapCut  →  ', ha='center', va='center',
             fontsize=14, color='#3B82F6', fontweight='bold',
             bbox=dict(boxstyle='round,pad=0.4', facecolor='#EFF6FF', edgecolor='#3B82F6'))

    fig.suptitle('Timeline video truoc va sau khi dung CapCut -- tiep kiem ~100 phut/video',
                 fontsize=11, color='#111827', fontweight='bold', y=0.97)
    fig.text(0.5, 0.01, 'seongon.com -- minh hoa quy trinh dung CapCut 2026',
             ha='center', va='bottom', fontsize=7.5, color='#9CA3AF', style='italic')

    plt.tight_layout(pad=1.0, rect=[0, 0.03, 1, 0.95])
    path = os.path.join(OUT, 'capcut-timeline-before-after.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close(fig)
    print(f'[OK] capcut-timeline-before-after.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/2] CapCut UI mockup...')
    make_ui_mockup()
    print('[2/2] Before/After timeline...')
    make_before_after()
    print('Done! 2 anh da tao tai:', OUT)
