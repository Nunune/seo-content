"""Tao anh cho bai: nha-o-xa-hoi-quan-10"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.gridspec as gridspec
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\bat-dong-san\nha-o-xa-hoi-quan-10\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def make_location_diagram():
    """So do vi tri du an Phu Tho DMC quan 10 - schematic map style"""
    fig, ax = plt.subplots(figsize=(11, 8), facecolor='#F0F4F8')
    ax.set_facecolor('#F0F4F8')

    # Background grid (duong pho schematic)
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)

    # Veduong chinh: Ly Thuong Kiet (horizontal)
    ax.axhline(y=4, xmin=0.05, xmax=0.95, color='#9CA3AF', linewidth=3, zorder=1)
    ax.text(5, 4.25, 'Duong Ly Thuong Kiet', ha='center', fontsize=9,
            color='#374151', fontweight='bold')

    # Duong doc: Nguyen Tri Phuong (vertical)
    ax.axvline(x=5, ymin=0.1, ymax=0.9, color='#9CA3AF', linewidth=2, zorder=1)
    ax.text(5.1, 7.5, 'Nguyen\nTri Phuong', ha='left', fontsize=8, color='#374151')

    # Duong doc: Nguyen Chi Thanh
    ax.axvline(x=2, ymin=0.1, ymax=0.9, color='#D1D5DB', linewidth=1.5, zorder=1)
    ax.text(2.1, 7.5, 'Nguyen\nChi Thanh', ha='left', fontsize=7.5, color='#6B7280')

    # Duong doc: Hung Vuong
    ax.axvline(x=8, ymin=0.1, ymax=0.9, color='#D1D5DB', linewidth=1.5, zorder=1)
    ax.text(8.1, 7.5, 'Hung Vuong', ha='left', fontsize=7.5, color='#6B7280')

    # Du an chinh: Phu Tho DMC
    project = mpatches.FancyBboxPatch((3.8, 3.4), 2.4, 1.2,
                                       boxstyle="round,pad=0.1",
                                       facecolor='#3B82F6', edgecolor='#1D4ED8',
                                       linewidth=2, zorder=5)
    ax.add_patch(project)
    ax.text(5, 4.0, 'PHU THO DMC\n324 Ly Thuong Kiet', ha='center', va='center',
            fontsize=8.5, fontweight='bold', color='white', zorder=6)

    # San van dong Phu Tho
    svd = mpatches.FancyBboxPatch((6.5, 4.8), 2.0, 1.2,
                                   boxstyle="round,pad=0.1",
                                   facecolor='#10B981', edgecolor='#059669',
                                   linewidth=1.5, zorder=4)
    ax.add_patch(svd)
    ax.text(7.5, 5.4, 'San van dong\nPhu Tho', ha='center', va='center',
            fontsize=8, color='white', fontweight='bold', zorder=5)

    # Distance SVD
    ax.annotate('', xy=(6.5, 5.0), xytext=(6.2, 4.5),
                arrowprops=dict(arrowstyle='->', color='#10B981', lw=1.5))
    ax.text(5.8, 4.7, '~500m', fontsize=8, color='#059669', fontweight='bold')

    # Benh vien Trung Vuong
    bv = mpatches.FancyBboxPatch((1.0, 5.2), 2.0, 1.0,
                                  boxstyle="round,pad=0.1",
                                  facecolor='#EF4444', edgecolor='#DC2626',
                                  linewidth=1.5, zorder=4)
    ax.add_patch(bv)
    ax.text(2.0, 5.7, 'BV Trung Vuong', ha='center', va='center',
            fontsize=8, color='white', fontweight='bold', zorder=5)

    # Distance BV
    ax.annotate('', xy=(3.5, 5.4), xytext=(3.8, 4.5),
                arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.5))
    ax.text(3.3, 5.5, '~1km', fontsize=8, color='#DC2626', fontweight='bold')

    # Metro so 2
    metro = mpatches.FancyBboxPatch((5.8, 1.5), 2.5, 0.9,
                                     boxstyle="round,pad=0.1",
                                     facecolor='#F59E0B', edgecolor='#D97706',
                                     linewidth=1.5, zorder=4)
    ax.add_patch(metro)
    ax.text(7.05, 1.95, 'Ga Metro so 2\n(dang xay)', ha='center', va='center',
            fontsize=8, color='#111827', fontweight='bold', zorder=5)

    # Distance Metro
    ax.annotate('', xy=(5.8, 2.0), xytext=(5.5, 3.4),
                arrowprops=dict(arrowstyle='->', color='#F59E0B', lw=1.5))
    ax.text(5.1, 2.6, '~700m', fontsize=8, color='#D97706', fontweight='bold')

    # Legend
    legend_elements = [
        mpatches.Patch(facecolor='#3B82F6', label='Du an Phu Tho DMC'),
        mpatches.Patch(facecolor='#10B981', label='San van dong Phu Tho (~500m)'),
        mpatches.Patch(facecolor='#EF4444', label='BV Trung Vuong (~1km)'),
        mpatches.Patch(facecolor='#F59E0B', label='Ga Metro so 2 (~700m)'),
    ]
    ax.legend(handles=legend_elements, loc='lower left', fontsize=8.5,
              framealpha=0.95, edgecolor='#D1D5DB', fancybox=True)

    ax.set_title('Vi tri Du an Nha o Xa hoi Phu Tho DMC - Quan 10, TP.HCM',
                 fontsize=12, fontweight='bold', color='#111827', pad=12)
    ax.axis('off')

    # North arrow
    ax.annotate('B', xy=(0.5, 7.2), fontsize=11, fontweight='bold', color='#374151',
                ha='center', va='center')
    ax.annotate('', xy=(0.5, 7.5), xytext=(0.5, 6.8),
                arrowprops=dict(arrowstyle='->', color='#374151', lw=2))

    path = os.path.join(OUT, 'vi-tri-phu-tho-dmc-quan-10.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#F0F4F8')
    plt.close(fig)
    print(f'[OK] vi-tri-phu-tho-dmc-quan-10.png ({os.path.getsize(path)//1024}KB)')


def make_ho_so_infographic():
    """Infographic 4 nhom ho so can chuan bi khi mua nha o xa hoi"""
    fig = plt.figure(figsize=(12, 8), facecolor='#FFFFFF')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis('off')
    ax.set_facecolor('#FFFFFF')

    # Title
    ax.text(6, 7.5, 'Ho So Mua Nha o Xa Hoi Phu Tho DMC Quan 10',
            ha='center', va='center', fontsize=14, fontweight='bold', color='#111827')
    ax.text(6, 7.1, '4 nhom giay to can chuan bi day du truoc khi nop',
            ha='center', va='center', fontsize=10, color='#6B7280')

    # 4 boxes in 2x2 grid
    boxes = [
        # (x, y, color, edge_color, title, items)
        (0.4, 4.2, '#EFF6FF', '#3B82F6', '#3B82F6',
         'Nhom 1: Don dang ky & Cam ket',
         ['Mau 01: Don de nghi mua NOXH', 'Mau 02: Ban ke khai nha o', 'Mau 03: Cam ket chua huong', 'Mau 04: Xac nhan UBND phuong', 'Mau 05: Xac nhan co quan/DN']),
        (6.4, 4.2, '#F0FDF4', '#10B981', '#10B981',
         'Nhom 2: Giay to tuy than & Ho gia dinh',
         ['CCCD/CMND (ban sao cong chung)', 'So ho khau / giay xac nhan cu tru', 'Giay DKKH hoac xac nhan doc than']),
        (0.4, 0.4, '#FFFBEB', '#F59E0B', '#D97706',
         'Nhom 3: Chung minh thu nhap',
         ['Cong nhan: HD lao dong + bang luong 3T', 'Vien chuc: QD tuyen dung + bang luong', 'Ho ngheo: So ho ngheo tu UBND', 'Nguoi co cong: Giay chung nhan'],),
        (6.4, 0.4, '#FFF1F2', '#EF4444', '#DC2626',
         'Nhom 4: Chung minh khong co nha',
         ['Xac nhan chua co nha tu UBND phuong', 'Neu dang thue: HD thue + xac nhan', 'Trich luc so ho khau (chung minh)']),
    ]

    for (bx, by, fc, ec, tc, title, items) in boxes:
        # Box background
        box = mpatches.FancyBboxPatch((bx, by), 5.2, 3.5,
                                       boxstyle="round,pad=0.15",
                                       facecolor=fc, edgecolor=ec,
                                       linewidth=2, zorder=2)
        ax.add_patch(box)

        # Title bar
        title_bar = mpatches.FancyBboxPatch((bx+0.05, by+2.85), 5.1, 0.55,
                                             boxstyle="round,pad=0.05",
                                             facecolor=ec, edgecolor='none', zorder=3)
        ax.add_patch(title_bar)
        ax.text(bx+2.6, by+3.12, title, ha='center', va='center',
                fontsize=8.5, fontweight='bold', color='white', zorder=4)

        # Items
        for j, item in enumerate(items):
            y_pos = by + 2.45 - j * 0.52
            # Bullet
            ax.text(bx+0.25, y_pos, '•', fontsize=12, color=tc, va='center', zorder=3)
            ax.text(bx+0.55, y_pos, item, fontsize=8, color='#374151', va='center', zorder=3)

    # Footer note
    ax.text(6, 0.15,
            '* Tat ca ban sao phai duoc cong chung trong vong 6 thang truoc ngay nop ho so',
            ha='center', fontsize=7.5, color='#6B7280', style='italic')

    path = os.path.join(OUT, 'ho-so-mua-nha-o-xa-hoi-quan-10.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] ho-so-mua-nha-o-xa-hoi-quan-10.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/2] Tao so do vi tri...')
    make_location_diagram()
    print('[2/2] Tao infographic ho so...')
    make_ho_so_infographic()
    print('Done!')
