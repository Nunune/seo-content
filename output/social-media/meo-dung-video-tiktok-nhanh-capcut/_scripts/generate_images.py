"""
Generate 2 images for meo-dung-video-tiktok-nhanh-capcut:
  1. so-sanh-thoi-gian-dung-video-tiktok.png  -- horizontal bar chart before/after (900x500)
  2. workflow-dung-video-tiktok-toi-uu.png    -- 5-step workflow diagram (1000x400)
"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\meo-dung-video-tiktok-nhanh-capcut\images"
os.makedirs(OUT, exist_ok=True)
plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False

# ─────────────────────────────────────────────
# IMAGE 1 -- Before/After horizontal bar chart
# ─────────────────────────────────────────────
def make_bar_chart():
    steps = [
        'Chuan bi / Script',
        'Quay video (amortized)',
        'Cat ghep thu cong',
        'Subtitle / Caption',
        'Chinh mau / Filter',
        'Them nhac',
        'Export & Dang',
    ]
    before = [0, 30, 20, 20, 8, 10, 5]   # khong co script but cost quay nhieu hon
    after  = [5, 15,  5,  3, 1,  3, 2]

    fig, ax = plt.subplots(figsize=(11, 6))
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')

    y = np.arange(len(steps))
    h = 0.35

    bars_before = ax.barh(y + h/2, before, h, color='#FCA5A5', edgecolor='#EF4444',
                           linewidth=0.8, label='Truoc khi toi uu (~93 phut/video)')
    bars_after  = ax.barh(y - h/2, after,  h, color='#6EE7B7', edgecolor='#10B981',
                           linewidth=0.8, label='Sau khi ap dung 10 meo (~34 phut/video)')

    for bar, val in zip(bars_before, before):
        if val > 0:
            ax.text(bar.get_width() + 0.4, bar.get_y() + bar.get_height()/2,
                    f'{val} phut', va='center', fontsize=8.5, color='#EF4444', fontweight='bold')
    for bar, val in zip(bars_after, after):
        ax.text(bar.get_width() + 0.4, bar.get_y() + bar.get_height()/2,
                f'{val} phut', va='center', fontsize=8.5, color='#10B981', fontweight='bold')

    ax.set_yticks(y)
    ax.set_yticklabels(steps, fontsize=10)
    ax.set_xlabel('Thoi gian (phut)', fontsize=10, color='#374151')
    ax.set_title('So sanh thoi gian dung video TikTok truoc va sau khi toi uu workflow CapCut',
                 fontsize=12, fontweight='bold', color='#111827', pad=14)
    ax.legend(loc='lower right', fontsize=9, framealpha=0.9)
    ax.set_xlim(0, 38)
    ax.spines[['top', 'right']].set_visible(False)
    ax.spines[['left', 'bottom']].set_color('#D1D5DB')
    ax.tick_params(colors='#6B7280')
    ax.xaxis.label.set_color('#6B7280')

    # Saving label
    ax.text(37, -0.7, 'Tiep kiem ~59 phut/video', ha='right', va='center',
            fontsize=10, color='#10B981', fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.35', facecolor='#D1FAE5', edgecolor='#10B981'))

    ax.text(0.5, -0.06, 'So lieu minh hoa dua tren quy trinh thuc chien | seongon.com',
            ha='center', va='bottom', transform=ax.transAxes,
            fontsize=7.5, color='#9CA3AF', style='italic')

    plt.tight_layout(pad=1.0)
    path = os.path.join(OUT, 'so-sanh-thoi-gian-dung-video-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close(fig)
    print(f'[OK] so-sanh-thoi-gian-dung-video-tiktok.png ({os.path.getsize(path)//1024}KB)')


# ─────────────────────────────────────────────
# IMAGE 2 -- 5-step optimized workflow diagram
# ─────────────────────────────────────────────
def make_workflow():
    fig, ax = plt.subplots(figsize=(13, 5))
    fig.patch.set_facecolor('#F8FAFC')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 13)
    ax.set_ylim(0, 5)
    ax.axis('off')

    ax.text(6.5, 4.65, 'Quy trinh dung video TikTok toi uu voi CapCut — 5 buoc',
            ha='center', va='center', fontsize=13, fontweight='bold', color='#111827')

    steps = [
        ('1', 'SCRIPT\n(3-5 cau)', '#3B82F6', 'Viet truoc\nkhi cam may', '~5 phut'),
        ('2', 'QUAY\n(Batch)', '#8B5CF6', 'Quay 5-7\nvideo / phien', '~15 phut\n/ video'),
        ('3', 'DUNGVIDEO\n(Auto tools)', '#10B981', 'Auto Caption\nBeat Sync\nPreset', '~12 phut'),
        ('4', 'REVIEW\n(Kiem tra)', '#F59E0B', 'Xem lai\nsua loi nho', '~5 phut'),
        ('5', 'EXPORT\n(TikTok)', '#EF4444', 'Xuat thang\nvao TikTok', '~2 phut'),
    ]

    xs = [1.2, 3.6, 6.0, 8.4, 10.8]
    y_center = 2.4
    box_w, box_h = 2.0, 2.2

    for i, ((num, title, color, desc, time_est), x) in enumerate(zip(steps, xs)):
        # Main box
        rect = FancyBboxPatch((x - box_w/2, y_center - box_h/2), box_w, box_h,
                              boxstyle='round,pad=0.15', facecolor=color + '22',
                              edgecolor=color, linewidth=2, zorder=3)
        ax.add_patch(rect)
        # Step circle
        circle = plt.Circle((x, y_center + box_h/2 - 0.3), 0.3,
                              color=color, zorder=4)
        ax.add_patch(circle)
        ax.text(x, y_center + box_h/2 - 0.3, num,
                ha='center', va='center', fontsize=11, fontweight='bold',
                color='white', zorder=5)
        # Title
        ax.text(x, y_center + 0.5, title, ha='center', va='center',
                fontsize=9.5, fontweight='bold', color=color, zorder=4, linespacing=1.3)
        # Description
        ax.text(x, y_center - 0.15, desc, ha='center', va='center',
                fontsize=8, color='#374151', zorder=4, linespacing=1.4)
        # Time estimate badge
        badge = FancyBboxPatch((x - 0.72, y_center - box_h/2 + 0.1), 1.44, 0.42,
                               boxstyle='round,pad=0.05', facecolor=color,
                               edgecolor='none', zorder=4)
        ax.add_patch(badge)
        ax.text(x, y_center - box_h/2 + 0.31, time_est,
                ha='center', va='center', fontsize=7.5, color='white',
                fontweight='bold', zorder=5, linespacing=1.2)

        # Arrow to next step
        if i < len(steps) - 1:
            ax.annotate('', xy=(xs[i+1] - box_w/2 - 0.08, y_center),
                        xytext=(x + box_w/2 + 0.08, y_center),
                        arrowprops=dict(arrowstyle='->', color='#9CA3AF', lw=2.2))

    # Total time badge
    total_box = FancyBboxPatch((4.5, 0.15), 4.0, 0.5,
                               boxstyle='round,pad=0.1', facecolor='#1E40AF',
                               edgecolor='none', zorder=3)
    ax.add_patch(total_box)
    ax.text(6.5, 0.4, 'Tong: ~34 phut / video  (so voi ~93 phut truoc khi toi uu)',
            ha='center', va='center', fontsize=9.5, color='white', fontweight='bold', zorder=4)

    ax.text(6.5, 0.02, 'seongon.com | So lieu minh hoa',
            ha='center', va='bottom', fontsize=7, color='#9CA3AF', style='italic')

    plt.tight_layout(pad=0.3)
    path = os.path.join(OUT, 'workflow-dung-video-tiktok-toi-uu.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F8FAFC')
    plt.close(fig)
    print(f'[OK] workflow-dung-video-tiktok-toi-uu.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/2] Bar chart truoc/sau...')
    make_bar_chart()
    print('[2/2] Workflow diagram...')
    make_workflow()
    print('Done! 2 anh da tao tai:', OUT)
