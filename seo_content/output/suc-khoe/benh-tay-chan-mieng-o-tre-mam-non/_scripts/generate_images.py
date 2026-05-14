"""Tao anh cho bai: benh-tay-chan-mieng-o-tre-mam-non"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\suc-khoe\benh-tay-chan-mieng-o-tre-mam-non\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def make_giai_doan_tay_chan_mieng():
    """Timeline 3 giai doan benh tay chan mieng"""
    fig, ax = plt.subplots(figsize=(14, 7))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 14); ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.5, 'Cac Giai Doan Benh Tay Chan Mieng', ha='center', va='center',
            fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(7, 9.0, '(Theo doi va hanh dong theo tung ngay)',
            ha='center', va='center', fontsize=9, color='#64748B')

    # Timeline arrow
    ax.annotate('', xy=(13.5, 6.5), xytext=(0.5, 6.5),
                arrowprops=dict(arrowstyle='->', color='#94A3B8', lw=2.5))
    ax.text(7, 6.0, 'NGAY 1                NGAY 3                NGAY 5                NGAY 7               NGAY 10',
            ha='center', va='center', fontsize=7.5, color='#94A3B8')

    # Phase 1: Ngay 1-2
    box1 = mpatches.FancyBboxPatch((0.3, 7.1), 3.8, 1.6, boxstyle='round,pad=0.1',
                                    facecolor='#FEF3C7', edgecolor='#F59E0B', linewidth=2)
    ax.add_patch(box1)
    ax.text(2.2, 8.45, 'GIAI DOAN 1: Ngay 1-2', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#92400E')
    ax.text(2.2, 8.1, 'U benh - Khoi phat', ha='center', va='center',
            fontsize=8, color='#B45309')
    ax.text(2.2, 7.75, 'Sot nhe 37.5-38.5°C', ha='center', va='center',
            fontsize=7.5, color='#78350F')
    ax.text(2.2, 7.45, 'Dau hong, chay nuoc mieng', ha='center', va='center',
            fontsize=7.5, color='#78350F')

    # Phase 1 action
    act1 = mpatches.FancyBboxPatch((0.3, 4.2), 3.8, 1.5, boxstyle='round,pad=0.1',
                                    facecolor='#FFFBEB', edgecolor='#FCD34D', linewidth=1.5)
    ax.add_patch(act1)
    ax.text(2.2, 5.4, 'Hanh dong:', ha='center', va='center',
            fontsize=8, fontweight='bold', color='#92400E')
    ax.text(2.2, 5.05, 'Ha sot + bu nuoc', ha='center', va='center',
            fontsize=7.5, color='#78350F')
    ax.text(2.2, 4.7, 'Theo doi nhiet do 4h/lan', ha='center', va='center',
            fontsize=7.5, color='#78350F')
    ax.text(2.2, 4.4, 'Chua co bong nuoc o tay/chan', ha='center', va='center',
            fontsize=7, color='#A16207', fontstyle='italic')

    # Arrow
    ax.annotate('', xy=(2.2, 7.1), xytext=(2.2, 5.7),
                arrowprops=dict(arrowstyle='->', color='#F59E0B', lw=1.5))

    # Phase 2: Ngay 3-5
    box2 = mpatches.FancyBboxPatch((5.1, 7.1), 3.8, 1.6, boxstyle='round,pad=0.1',
                                    facecolor='#FEE2E2', edgecolor='#EF4444', linewidth=2)
    ax.add_patch(box2)
    ax.text(7.0, 8.45, 'GIAI DOAN 2: Ngay 3-5', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#991B1B')
    ax.text(7.0, 8.1, 'Bong nuoc xuat hien (DINH CAO LAY LAN)', ha='center', va='center',
            fontsize=7.5, color='#DC2626')
    ax.text(7.0, 7.75, 'Loet mieng, bong nuoc long ban tay/chan', ha='center', va='center',
            fontsize=7.5, color='#7F1D1D')
    ax.text(7.0, 7.45, 'Sot co the keo dai hoac giam', ha='center', va='center',
            fontsize=7.5, color='#7F1D1D')

    # Phase 2 action
    act2 = mpatches.FancyBboxPatch((5.1, 4.2), 3.8, 1.5, boxstyle='round,pad=0.1',
                                    facecolor='#FFF1F2', edgecolor='#FCA5A5', linewidth=1.5)
    ax.add_patch(act2)
    ax.text(7.0, 5.4, 'Hanh dong:', ha='center', va='center',
            fontsize=8, fontweight='bold', color='#991B1B')
    ax.text(7.0, 5.05, 'CACH LY - Thong bao truong hoc', ha='center', va='center',
            fontsize=7.5, fontweight='bold', color='#DC2626')
    ax.text(7.0, 4.7, 'An mem nguoi, bu nuoc', ha='center', va='center',
            fontsize=7.5, color='#7F1D1D')
    ax.text(7.0, 4.4, 'Theo doi 7 dau hieu bien chung', ha='center', va='center',
            fontsize=7, color='#B91C1C', fontstyle='italic')

    ax.annotate('', xy=(7.0, 7.1), xytext=(7.0, 5.7),
                arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.5))

    # Phase 3: Ngay 7-10
    box3 = mpatches.FancyBboxPatch((9.9, 7.1), 3.8, 1.6, boxstyle='round,pad=0.1',
                                    facecolor='#DCFCE7', edgecolor='#22C55E', linewidth=2)
    ax.add_patch(box3)
    ax.text(11.8, 8.45, 'GIAI DOAN 3: Ngay 7-10', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#14532D')
    ax.text(11.8, 8.1, 'Hoi phuc (90%) hoac Bien chung (10%)', ha='center', va='center',
            fontsize=7.5, color='#15803D')
    ax.text(11.8, 7.75, 'Bong nuoc teo, loet mieng lanh dan', ha='center', va='center',
            fontsize=7.5, color='#166534')
    ax.text(11.8, 7.45, 'Tre an uong tro lai binh thuong', ha='center', va='center',
            fontsize=7.5, color='#166534')

    # Phase 3 action
    act3 = mpatches.FancyBboxPatch((9.9, 4.2), 3.8, 1.5, boxstyle='round,pad=0.1',
                                    facecolor='#F0FDF4', edgecolor='#86EFAC', linewidth=1.5)
    ax.add_patch(act3)
    ax.text(11.8, 5.4, 'Hanh dong:', ha='center', va='center',
            fontsize=8, fontweight='bold', color='#14532D')
    ax.text(11.8, 5.05, 'Cho di hoc lai khi het bong nuoc', ha='center', va='center',
            fontsize=7.5, color='#166534')
    ax.text(11.8, 4.7, 'Va khong sot 48h (khong dung thuoc)', ha='center', va='center',
            fontsize=7.5, color='#166534')
    ax.text(11.8, 4.4, 'Neu co dau hieu TK -> Cap cuu ngay', ha='center', va='center',
            fontsize=7, color='#DC2626', fontstyle='italic')

    ax.annotate('', xy=(11.8, 7.1), xytext=(11.8, 5.7),
                arrowprops=dict(arrowstyle='->', color='#22C55E', lw=1.5))

    # Warning box at bottom
    warn = mpatches.FancyBboxPatch((1.5, 0.5), 11, 1.6, boxstyle='round,pad=0.15',
                                    facecolor='#FFF7ED', edgecolor='#F97316', linewidth=2)
    ax.add_patch(warn)
    ax.text(7, 1.8, '7 DAU HIEU CAN CAP CUU NGAY (xuat hien bat ky giai doan nao):', ha='center', va='center',
            fontsize=8.5, fontweight='bold', color='#C2410C')
    ax.text(7, 1.35, 'Sot >39°C keo dai  |  Giat minh lien tuc  |  Run tay chan  |  Kho tho  |  Da noi van tim  |  Non oi nhieu  |  Li bi', ha='center', va='center',
            fontsize=8, color='#9A3412')
    ax.text(7, 0.9, 'Neu co bat ky dau hieu tren -> Dua tre di benh vien NGAY, khong cho den sang', ha='center', va='center',
            fontsize=7.5, color='#7C2D12', fontstyle='italic')

    plt.tight_layout(pad=0.5)
    path = os.path.join(OUT, 'giai-doan-tay-chan-mieng.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] giai-doan-tay-chan-mieng.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/1] Tao timeline giai doan benh tay chan mieng...')
    make_giai_doan_tay_chan_mieng()
    print('Done!')
