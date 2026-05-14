"""Tao anh cho bai: kham-phu-khoa-dinh-ky"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\suc-khoe\kham-phu-khoa-dinh-ky\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def make_lich_kham_phu_khoa():
    """Infographic: lich kham phu khoa theo nhom phu nu"""
    fig, ax = plt.subplots(figsize=(14, 8))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 14); ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.55, 'Lich Kham Phu Khoa Dinh Ky Theo Nhom', ha='center', va='center',
            fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(7, 9.05, '(Tan suat khuyen nghi theo tuoi va yeu to nguy co)',
            ha='center', va='center', fontsize=9, color='#64748B')

    groups = [
        # (x, y, w, h, color, border, title, subtitle, frequency, tests)
        (0.3, 4.8, 3.2, 3.8, '#EFF6FF', '#3B82F6', 'NHOM 1', 'Phu nu 21-29 tuoi', '1 LAN/NAM',
         'Sieu am phu khoa\nKham lam sang\nPap smear (3 nam/lan)'),
        (3.8, 4.8, 3.2, 3.8, '#F0FDF4', '#22C55E', 'NHOM 2', 'Phu nu 30-39 tuoi', '6-12 THANG/LAN',
         'Sieu am phu khoa\nPap smear + HPV test\nXet nghiem dich am dao'),
        (7.3, 4.8, 3.2, 3.8, '#FFF7ED', '#F97316', 'NHOM 3', 'Phu nu 40+ / Tien man kinh', '6 THANG/LAN',
         'Sieu am vu + phu khoa\nCA-125 mau\nNoi tiet to (FSH, estradiol)\nSieu am xuong'),
        (10.8, 4.8, 2.9, 3.8, '#FDF4FF', '#A855F7', 'NHOM 4', 'Co yeu to nguy co cao', 'THEO CHI DINH BS',
         'Tien su gia dinh ung thu\nDang dieu tri benh PK\nMang thai: kham thai dinh ky'),
    ]

    for (x, y, w, h, fc, ec, grp, sub, freq, tests) in groups:
        box = mpatches.FancyBboxPatch((x, y), w, h, boxstyle='round,pad=0.1',
                                       facecolor=fc, edgecolor=ec, linewidth=2)
        ax.add_patch(box)
        ax.text(x+w/2, y+h-0.25, grp, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='#0F172A')
        ax.text(x+w/2, y+h-0.6, sub, ha='center', va='center',
                fontsize=7.5, color='#374151')

        # Frequency badge
        badge = mpatches.FancyBboxPatch((x+0.15, y+h-1.35), w-0.3, 0.55,
                                         boxstyle='round,pad=0.05',
                                         facecolor=ec, edgecolor='none')
        ax.add_patch(badge)
        ax.text(x+w/2, y+h-1.07, freq, ha='center', va='center',
                fontsize=8, fontweight='bold', color='white')

        # Tests list
        for i, line in enumerate(tests.split('\n')):
            ax.text(x+w/2, y+h-1.8-i*0.42, '• ' + line, ha='center', va='center',
                    fontsize=6.8, color='#374151')

    # Bottom note: Tat ca nhom
    note = mpatches.FancyBboxPatch((0.3, 3.0), 13.4, 1.5, boxstyle='round,pad=0.15',
                                    facecolor='#F8FAFC', edgecolor='#CBD5E1', linewidth=1.5)
    ax.add_patch(note)
    ax.text(7, 4.15, 'TAT CA CAC NHOM: Kham bac si ngay khi co bieu hien bat thuong', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#EF4444')
    ax.text(7, 3.65, 'Huyet am dao bat thuong  |  Dau vung chau  |  Knh nguyet bat thuong  |  Cuc u bung duoi', ha='center', va='center',
            fontsize=8, color='#374151')
    ax.text(7, 3.2, 'Khong can doi den lich kham dinh ky neu co bat ky trieu chung tren', ha='center', va='center',
            fontsize=7.5, color='#64748B', fontstyle='italic')

    # Timeline at bottom
    ax.text(7, 2.2, 'NGUYEN TAC VANG:', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#0F172A')

    tips = [
        (2.5, 1.5, '#3B82F6', 'Sau sach kinh 3-7 ngay\nla thoi diem tot nhat'),
        (6.0, 1.5, '#10B981', 'Khong dung thuoc dat\nam dao 24h truoc kham'),
        (9.5, 1.5, '#F59E0B', 'Sieu am bung: uong 500ml nuoc\nSieu am am dao: di tieu truoc'),
        (12.5, 1.5, '#8B5CF6', 'Noi thong tin trung thuc\nvoi bac si'),
    ]

    for (tx, ty, clr, txt) in tips:
        circle = plt.Circle((tx, ty+0.15), 0.15, color=clr, zorder=3)
        ax.add_patch(circle)
        ax.text(tx, ty-0.25, txt, ha='center', va='center', fontsize=6.5, color='#374151')

    plt.tight_layout(pad=0.5)
    path = os.path.join(OUT, 'lich-kham-phu-khoa.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] lich-kham-phu-khoa.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/1] Tao infographic lich kham phu khoa...')
    make_lich_kham_phu_khoa()
    print('Done!')
