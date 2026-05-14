"""Tao anh cho bai: tiktok-shadowban"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\tiktok-shadowban\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def make_trust_score_diagram():
    """Trust Score TikTok timeline: new account -> builds up -> violations pull down -> shadowban zone"""
    fig, ax = plt.subplots(figsize=(12, 6), facecolor='#FFFFFF')
    ax.set_facecolor('#F9FAFB')

    # X axis: thoi gian (thang)
    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])

    # Trust Score curve: tang dan, roi bi keo xuong do vi pham
    y = np.array([20, 30, 42, 55, 65, 72, 75, 68, 55, 40, 35, 38, 45])

    # Shadowban threshold line
    threshold = 45
    shadowban_zone_top = 45

    # Fill shadowban zone (do)
    ax.fill_between(x, 0, shadowban_zone_top, alpha=0.12, color='#EF4444', label='Shadowban zone')

    # Fill safe zone (xanh la)
    ax.fill_between(x, shadowban_zone_top, 100, alpha=0.06, color='#10B981')

    # Trust Score line
    ax.plot(x, y, color='#3B82F6', linewidth=2.5, zorder=5)
    ax.fill_between(x, y, 0, alpha=0.15, color='#3B82F6')

    # Threshold line
    ax.axhline(y=threshold, color='#EF4444', linewidth=1.5, linestyle='--', zorder=4)
    ax.text(12.1, threshold, 'Nguong\nshadowban', fontsize=8, color='#EF4444',
            va='center', fontweight='bold')

    # Annotations
    # Phase 1: Tai khoan moi
    ax.annotate('Tai khoan moi\n(Trust thap)', xy=(0, 20), xytext=(0.5, 10),
                fontsize=8, color='#6B7280', ha='center',
                arrowprops=dict(arrowstyle='->', color='#9CA3AF', lw=1.2))

    # Phase 2: Tang dan
    ax.annotate('Noi dung tot\nTrust tang dan', xy=(5, 72), xytext=(4, 85),
                fontsize=8, color='#059669', ha='center',
                arrowprops=dict(arrowstyle='->', color='#10B981', lw=1.2))

    # Phase 3: Vi pham
    ax.annotate('Vi pham chinh sach\nTrust bi keo xuong', xy=(7, 68), xytext=(8.5, 82),
                fontsize=8, color='#DC2626', ha='center',
                arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.2))

    # Phase 4: Shadowban
    ax.annotate('SHADOWBAN\nDuy tri 2-4 tuan', xy=(9.5, 37), xytext=(8, 18),
                fontsize=8.5, color='#DC2626', ha='center', fontweight='bold',
                arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.5))

    # Phase 5: Phuc hoi
    ax.annotate('Phuc hoi dan\n(neu fix dung cach)', xy=(11, 38), xytext=(11, 20),
                fontsize=8, color='#2563EB', ha='center',
                arrowprops=dict(arrowstyle='->', color='#3B82F6', lw=1.2))

    # Key events markers
    event_x = [6, 7]
    event_y = [75, 68]
    ax.scatter(event_x, event_y, color='#EF4444', s=60, zorder=6)

    event_x2 = [5]
    event_y2 = [72]
    ax.scatter(event_x2, event_y2, color='#10B981', s=60, zorder=6)

    # Labels
    ax.set_xlabel('Thoi gian hoat dong (thang)', fontsize=10, color='#374151', labelpad=10)
    ax.set_ylabel('Trust Score (0-100)', fontsize=10, color='#374151', labelpad=10)
    ax.set_title('Co che Trust Score TikTok va Nguong Shadowban', fontsize=13,
                 fontweight='bold', color='#111827', pad=15)

    # Axes config
    ax.set_xlim(-0.3, 12.8)
    ax.set_ylim(0, 100)
    ax.set_xticks(range(0, 13))
    ax.set_xticklabels([f'T{i}' for i in range(0, 13)], fontsize=8.5, color='#6B7280')
    ax.set_yticks([0, 20, 40, 45, 60, 80, 100])
    ax.set_yticklabels(['0', '20', '40', '45*', '60', '80', '100'], fontsize=8.5, color='#6B7280')
    ax.tick_params(axis='both', length=0)

    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#E5E7EB')
    ax.spines['bottom'].set_color('#E5E7EB')
    ax.grid(axis='y', linestyle='--', alpha=0.4, color='#D1D5DB')

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#3B82F6', alpha=0.7, label='Trust Score tai khoan'),
        mpatches.Patch(facecolor='#10B981', alpha=0.4, label='Vung an toan (reach day du)'),
        mpatches.Patch(facecolor='#EF4444', alpha=0.4, label='Shadowban zone (reach bi han che)'),
    ]
    ax.legend(handles=legend_elements, loc='upper left', fontsize=8.5,
              framealpha=0.9, edgecolor='#E5E7EB')

    # Footer note
    fig.text(0.5, 0.01,
             '* Nguong shadowban la uoc tinh cua cong dong creator. TikTok khong cong bo chinh thuc.',
             ha='center', fontsize=7.5, color='#9CA3AF', style='italic')

    path = os.path.join(OUT, 'trust-score-tiktok-shadowban.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] trust-score-tiktok-shadowban.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    make_trust_score_diagram()
    print('Done!')
