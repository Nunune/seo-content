"""Tao anh cho bai: cach-tang-tuong-tac-page-facebook"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\cach-tang-tuong-tac-page-facebook\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def make_thu_bac_tuong_tac():
    """Pyramid chart: Thu bac tuong tac Facebook 2026"""
    fig, ax = plt.subplots(figsize=(11, 7))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.axis('off')

    levels = [
        # (y_center, height, width, color, label, sublabel, stars)
        (8.8, 1.4, 3.2, '#EF4444', 'MESSENGER SHARE', 'Chia se qua tin nhan', '5 sao'),
        (7.1, 1.4, 4.5, '#F97316', 'LUU BAI (SAVE)',  'Muon xem lai noi dung', '5 sao'),
        (5.4, 1.4, 5.8, '#F59E0B', 'COMMENT',         'Thao luan, giu nguoi lai', '4 sao'),
        (3.7, 1.4, 7.1, '#3B82F6', 'SHARE LEN TUONG', 'Lan truyen noi dung', '3 sao'),
        (2.0, 1.4, 8.4, '#6366F1', 'REACTION (cam xuc)', 'Tim hieu nhanh', '2 sao'),
        (0.3, 1.4, 9.7, '#94A3B8', 'LIKE (thumb up)', 'Tuong tac thap nhat', '1 sao'),
    ]

    center_x = 5.0
    for (yc, h, w, color, label, sublabel, stars) in levels:
        x0 = center_x - w / 2
        rect = mpatches.FancyBboxPatch((x0, yc - h/2), w, h,
                                        boxstyle='round,pad=0.05',
                                        facecolor=color, edgecolor='white',
                                        linewidth=1.5, alpha=0.92)
        ax.add_patch(rect)
        ax.text(center_x, yc + 0.18, label, ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')
        ax.text(center_x, yc - 0.28, sublabel, ha='center', va='center',
                fontsize=8, color='white', alpha=0.9)
        ax.text(x0 + w - 0.15, yc, stars, ha='right', va='center',
                fontsize=8.5, color='white', alpha=0.85)

    ax.text(center_x, 9.75, 'Thu Bac Tuong Tac Facebook 2026',
            ha='center', va='center', fontsize=13, fontweight='bold', color='#0F172A')
    ax.text(center_x, 9.35, '(Theo trong so thuat toan — cao hon = Facebook thuong manh hon)',
            ha='center', va='center', fontsize=8.5, color='#64748B')

    ax.annotate('', xy=(center_x - 5.1, 9.2), xytext=(center_x - 5.1, 0.0),
                arrowprops=dict(arrowstyle='<->', color='#94A3B8', lw=1.5))
    ax.text(center_x - 5.5, 4.6, 'TRONG SO\nCAO HUN', ha='center', va='center',
            fontsize=7.5, color='#94A3B8', rotation=90)

    plt.tight_layout(pad=0.5)
    path = os.path.join(OUT, 'thu-bac-tuong-tac-facebook.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] thu-bac-tuong-tac-facebook.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/1] Tao pyramid thu bac tuong tac Facebook...')
    make_thu_bac_tuong_tac()
    print('Done!')
