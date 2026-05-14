"""Tao anh cho bai: bo-sung-vitamin-c-qua-trai-cay"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\suc-khoe\bo-sung-vitamin-c-qua-trai-cay\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def make_chart_vitamin_c():
    """Bieu do cot: Ham luong vitamin C (mg/100g) trong 10 loai trai cay"""
    fruits = [
        'Oi', 'Qua ly den', 'Kiwi', 'Du du', 'Dau tay',
        'Cam & chanh', 'Dua (thom)', 'Xoai', 'Buoi', 'Thanh long'
    ]
    values = [228, 200, 93, 62, 59, 53, 48, 37, 31, 9]

    colors = []
    for v in values:
        if v >= 100:
            colors.append('#10B981')
        elif v >= 50:
            colors.append('#3B82F6')
        elif v >= 20:
            colors.append('#F59E0B')
        else:
            colors.append('#94A3B8')

    fig, ax = plt.subplots(figsize=(11, 6.5))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F8FAFC')

    bars = ax.barh(fruits[::-1], values[::-1], color=colors[::-1],
                   edgecolor='white', linewidth=0.8, height=0.65)

    for bar, val in zip(bars, values[::-1]):
        ax.text(bar.get_width() + 3, bar.get_y() + bar.get_height() / 2,
                f'{val} mg', va='center', ha='left',
                fontsize=10, fontweight='bold', color='#1E293B')

    ax.set_xlabel('Ham luong Vitamin C (mg/100g)', fontsize=11, color='#475569', labelpad=10)
    ax.set_title('Top 10 Trai Cay Giau Vitamin C Nhat\n(mg tren 100g phan an duoc)',
                 fontsize=13, fontweight='bold', color='#0F172A', pad=16)

    ax.set_xlim(0, 275)
    ax.tick_params(axis='y', labelsize=10, colors='#1E293B')
    ax.tick_params(axis='x', labelsize=9, colors='#64748B')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_color('#E2E8F0')
    ax.spines['bottom'].set_color('#E2E8F0')
    ax.axvline(x=90, color='#EF4444', linestyle='--', linewidth=1.2, alpha=0.7)
    ax.text(91, 0.3, 'RDA nguoi lon\n(90 mg)', color='#EF4444', fontsize=8.5,
            va='bottom', ha='left', alpha=0.85)

    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#10B981', label='Rat giau (>=100mg)'),
        Patch(facecolor='#3B82F6', label='Giau (50-99mg)'),
        Patch(facecolor='#F59E0B', label='Kha (20-49mg)'),
        Patch(facecolor='#94A3B8', label='It (<20mg)'),
    ]
    ax.legend(handles=legend_elements, loc='lower right', fontsize=9,
              framealpha=0.9, edgecolor='#E2E8F0')

    ax.text(0.5, -0.08, 'Nguon: USDA FoodData Central, 2024',
            ha='center', transform=ax.transAxes, fontsize=8.5, color='#94A3B8')

    plt.tight_layout(pad=1.5)
    path = os.path.join(OUT, 'bang-so-sanh-vitamin-c-trai-cay.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] bang-so-sanh-vitamin-c-trai-cay.png ({os.path.getsize(path)//1024}KB)')


def make_vai_tro_vitamin_c():
    """3-panel infographic: Vai tro cua Vitamin C"""
    fig, axes = plt.subplots(1, 3, figsize=(13, 5.5))
    fig.patch.set_facecolor('#FFFFFF')

    panels = [
        {
            'title': 'He Mien Dich',
            'icon': '🛡',
            'color': '#10B981',
            'bg': '#ECFDF5',
            'points': [
                'Kich thich san xuat bach cau',
                'Giam thoi gian cam cum 8%',
                '(Nutrients, 2017)',
                'Tang suc de khang',
            ],
        },
        {
            'title': 'Tong hop Collagen',
            'icon': '💪',
            'color': '#3B82F6',
            'bg': '#EFF6FF',
            'points': [
                'Dong yeu to bat buoc',
                'Cau thanh da, gan, sun khop',
                'Lam lanh vet thuong nhanh',
                'Chong lao hoa da',
            ],
        },
        {
            'title': 'Chong Oxy Hoa',
            'icon': '⚡',
            'color': '#F59E0B',
            'bg': '#FFFBEB',
            'points': [
                'Trung hoa goc tu do',
                'Bao ve te bao khoi ton thuong',
                'Giam nguy co benh man tinh',
                'Ho tro hap thu sat',
            ],
        },
    ]

    for ax, panel in zip(axes, panels):
        ax.set_facecolor(panel['bg'])
        ax.set_xlim(0, 10); ax.set_ylim(0, 10)
        ax.axis('off')

        rect = plt.Rectangle((0.2, 0.2), 9.6, 9.6, linewidth=2,
                              edgecolor=panel['color'], facecolor='none',
                              transform=ax.transData)
        ax.add_patch(rect)

        ax.text(5, 8.5, panel['title'], ha='center', va='center',
                fontsize=13, fontweight='bold', color=panel['color'],
                wrap=True)

        ax.axhline(y=7.8, xmin=0.1, xmax=0.9, color=panel['color'], linewidth=1.5, alpha=0.5)

        for j, point in enumerate(panel['points']):
            y = 6.8 - j * 1.5
            ax.text(1.0, y, f'• {point}', ha='left', va='center',
                    fontsize=9.5, color='#374151', wrap=True)

    fig.suptitle('3 Vai Tro Chinh Cua Vitamin C Voi Co The Nguoi',
                 fontsize=14, fontweight='bold', color='#0F172A', y=1.01)

    plt.tight_layout(pad=0.8)
    path = os.path.join(OUT, 'vai-tro-vitamin-c.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] vai-tro-vitamin-c.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/2] Tao bieu do ham luong Vitamin C...')
    make_chart_vitamin_c()
    print('[2/2] Tao infographic 3 vai tro Vitamin C...')
    make_vai_tro_vitamin_c()
    print('Done!')
