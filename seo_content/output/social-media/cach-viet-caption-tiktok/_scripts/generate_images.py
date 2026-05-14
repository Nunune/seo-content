"""Tao anh cho bai: cach-viet-caption-tiktok"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import matplotlib.patheffects as pe
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\cach-viet-caption-tiktok\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def make_co_che_caption_tiktok():
    """2-panel diagram: algorithm classification + viewer behavior"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 7))
    fig.patch.set_facecolor('#FFFFFF')

    # ── Panel 1: Algorithm Classification ──────────────────────────
    ax1 = axes[0]
    ax1.set_facecolor('#F8FAFC')
    ax1.set_xlim(0, 10); ax1.set_ylim(0, 10)
    ax1.axis('off')

    ax1.text(5, 9.4, 'Co Che 1: Thuat Toan Phan Loai', ha='center', va='center',
             fontsize=12, fontweight='bold', color='#0F172A')
    ax1.text(5, 8.85, '(TikTok doc caption de phan phoi video)',
             ha='center', va='center', fontsize=8.5, color='#64748B')

    # Input box
    inp = mpatches.FancyBboxPatch((0.5, 7.0), 9, 1.3, boxstyle='round,pad=0.1',
                                   facecolor='#EFF6FF', edgecolor='#3B82F6', linewidth=1.5)
    ax1.add_patch(inp)
    ax1.text(5, 7.85, 'VIDEO CUA BAN', ha='center', va='center',
             fontsize=10, fontweight='bold', color='#1D4ED8')
    ax1.text(5, 7.35, 'Caption + Hashtag + Audio transcript', ha='center', va='center',
             fontsize=8.5, color='#3B82F6')

    # Arrow down
    ax1.annotate('', xy=(5, 5.9), xytext=(5, 6.95),
                 arrowprops=dict(arrowstyle='->', color='#6B7280', lw=2))
    ax1.text(5.4, 6.42, 'TikTok phan tich', ha='left', va='center', fontsize=7.5, color='#6B7280')

    # Algorithm box
    alg = mpatches.FancyBboxPatch((1.5, 4.8), 7, 1.0, boxstyle='round,pad=0.1',
                                   facecolor='#F0FDF4', edgecolor='#10B981', linewidth=1.5)
    ax1.add_patch(alg)
    ax1.text(5, 5.35, 'THUAT TOAN TIKTOK', ha='center', va='center',
             fontsize=9, fontweight='bold', color='#059669')
    ax1.text(5, 4.95, 'Hieu chu de → chon nhom nguoi xem phu hop', ha='center', va='center',
             fontsize=7.5, color='#10B981')

    # Arrow down
    ax1.annotate('', xy=(5, 3.6), xytext=(5, 4.75),
                 arrowprops=dict(arrowstyle='->', color='#6B7280', lw=2))

    # Two result boxes
    good = mpatches.FancyBboxPatch((0.3, 2.4), 4.0, 1.1, boxstyle='round,pad=0.1',
                                    facecolor='#DCFCE7', edgecolor='#22C55E', linewidth=1.5)
    ax1.add_patch(good)
    ax1.text(2.3, 3.1, 'Caption TU KHOA', ha='center', va='center',
             fontsize=8.5, fontweight='bold', color='#15803D')
    ax1.text(2.3, 2.7, '"cong thuc bun bo Hue"', ha='center', va='center',
             fontsize=7.5, color='#16A34A')
    ax1.text(2.3, 2.45, '→ Dung doi tuong ✅', ha='center', va='center',
             fontsize=7.5, color='#15803D')

    bad = mpatches.FancyBboxPatch((5.7, 2.4), 4.0, 1.1, boxstyle='round,pad=0.1',
                                   facecolor='#FEF2F2', edgecolor='#EF4444', linewidth=1.5)
    ax1.add_patch(bad)
    ax1.text(7.7, 3.1, 'Caption CHUNG CHUNG', ha='center', va='center',
             fontsize=8.5, fontweight='bold', color='#DC2626')
    ax1.text(7.7, 2.7, '"bua toi hom nay 🍜"', ha='center', va='center',
             fontsize=7.5, color='#EF4444')
    ax1.text(7.7, 2.45, '→ Phan phoi kho chinh xac ❌', ha='center', va='center',
             fontsize=7.5, color='#DC2626')

    ax1.annotate('', xy=(2.3, 3.5), xytext=(4.5, 3.58),
                 arrowprops=dict(arrowstyle='->', color='#22C55E', lw=1.5))
    ax1.annotate('', xy=(7.7, 3.5), xytext=(5.5, 3.58),
                 arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.5))

    ax1.text(5, 1.7, 'KET QUA CUOI', ha='center', va='center',
             fontsize=9, fontweight='bold', color='#0F172A')
    ax1.text(2.3, 1.25, 'VIEW DUNG\n+ ENGAGEMENT CAO', ha='center', va='center',
             fontsize=8, fontweight='bold', color='#15803D')
    ax1.text(7.7, 1.25, 'VIEW THIEU\nCHINH XAC', ha='center', va='center',
             fontsize=8, fontweight='bold', color='#DC2626')

    # ── Panel 2: Viewer Behavior ────────────────────────────────────
    ax2 = axes[1]
    ax2.set_facecolor('#F8FAFC')
    ax2.set_xlim(0, 10); ax2.set_ylim(0, 10)
    ax2.axis('off')

    ax2.text(5, 9.4, 'Co Che 2: Hanh Vi Nguoi Xem', ha='center', va='center',
             fontsize=12, fontweight='bold', color='#0F172A')
    ax2.text(5, 8.85, '(90% nguoi xem chi doc 2-3 dong dau)',
             ha='center', va='center', fontsize=8.5, color='#64748B')

    # Phone mockup
    phone = mpatches.FancyBboxPatch((3, 1.5), 4, 7.0, boxstyle='round,pad=0.2',
                                     facecolor='#1E293B', edgecolor='#334155', linewidth=2)
    ax2.add_patch(phone)

    # Screen
    screen = mpatches.FancyBboxPatch((3.2, 1.8), 3.6, 6.4, boxstyle='square,pad=0',
                                      facecolor='#000000', edgecolor='none')
    ax2.add_patch(screen)

    # Video area (dark)
    video_area = mpatches.FancyBboxPatch((3.2, 3.8), 3.6, 4.4, boxstyle='square,pad=0',
                                          facecolor='#0F172A', edgecolor='none')
    ax2.add_patch(video_area)
    ax2.text(5, 5.8, '[VIDEO]', ha='center', va='center',
             fontsize=11, color='#475569', fontstyle='italic')

    # Caption lines visible (green zone)
    green = mpatches.FancyBboxPatch((3.2, 2.8), 3.6, 0.9, boxstyle='square,pad=0',
                                     facecolor='#14532D', edgecolor='none', alpha=0.8)
    ax2.add_patch(green)
    ax2.text(5, 3.35, 'Dong 1: HOOK (tat ca moi nguoi doc)', ha='center', va='center',
             fontsize=6.5, color='#86EFAC', fontweight='bold')
    ax2.text(5, 3.0, 'Dong 2-3: body + CTA (90% con lai)', ha='center', va='center',
             fontsize=6, color='#86EFAC')

    # "Xem them" cutoff line
    ax2.plot([3.2, 6.8], [2.75, 2.75], color='#FBBF24', linewidth=1.5, linestyle='--')

    # Hidden area (gray zone)
    gray = mpatches.FancyBboxPatch((3.2, 1.8), 3.6, 0.9, boxstyle='square,pad=0',
                                    facecolor='#1E293B', edgecolor='none')
    ax2.add_patch(gray)
    ax2.text(5, 2.25, '"Xem them..." — 90% khong bam', ha='center', va='center',
             fontsize=6, color='#94A3B8', fontstyle='italic')

    # Stats annotations
    ax2.annotate('90%\ndoc den day', xy=(3.2, 3.25), xytext=(1.5, 3.25),
                 fontsize=8, color='#22C55E', fontweight='bold', ha='center',
                 arrowprops=dict(arrowstyle='->', color='#22C55E', lw=1.2))

    ax2.annotate('10%\nbam xem them', xy=(3.2, 2.25), xytext=(1.5, 2.25),
                 fontsize=8, color='#EF4444', fontweight='bold', ha='center',
                 arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.2))

    ax2.text(5, 1.2, 'QUY TAC VANG: Cau dau = Cau quan trong nhat', ha='center', va='center',
             fontsize=8.5, fontweight='bold', color='#F59E0B',
             bbox=dict(boxstyle='round,pad=0.3', facecolor='#FEF3C7', edgecolor='#F59E0B'))

    plt.tight_layout(pad=1.0)
    path = os.path.join(OUT, 'co-che-caption-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] co-che-caption-tiktok.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/1] Tao diagram co che caption TikTok...')
    make_co_che_caption_tiktok()
    print('Done!')
