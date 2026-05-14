"""Tao anh cho bai: video-tiktok-0-view"""
import os, sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\social-media\video-tiktok-0-view\images"
os.makedirs(OUT, exist_ok=True)

plt.rcParams['font.family'] = 'DejaVu Sans'
plt.rcParams['axes.unicode_minus'] = False


def make_quy_trinh_phan_phoi_tiktok():
    """Flowchart: quy trinh phan phoi video TikTok - 3 vong"""
    fig, ax = plt.subplots(figsize=(14, 9))
    fig.patch.set_facecolor('#FFFFFF')
    ax.set_facecolor('#F8FAFC')
    ax.set_xlim(0, 14); ax.set_ylim(0, 10)
    ax.axis('off')

    ax.text(7, 9.6, 'Quy Trinh Phan Phoi Video TikTok', ha='center', va='center',
            fontsize=14, fontweight='bold', color='#0F172A')
    ax.text(7, 9.15, '(Tu luc nhan "Dang" den FYP — hoac bi dung lai)',
            ha='center', va='center', fontsize=9, color='#64748B')

    # Step 0: Upload
    up = mpatches.FancyBboxPatch((5.5, 8.0), 3, 0.8, boxstyle='round,pad=0.1',
                                   facecolor='#1E293B', edgecolor='#475569', linewidth=2)
    ax.add_patch(up)
    ax.text(7, 8.4, 'BAN NHAN "DANG"', ha='center', va='center',
            fontsize=10, fontweight='bold', color='white')

    ax.annotate('', xy=(7, 7.6), xytext=(7, 7.95),
                arrowprops=dict(arrowstyle='->', color='#6B7280', lw=2))

    # Stage 1: AI Review
    s1 = mpatches.FancyBboxPatch((3, 6.5), 8, 1.0, boxstyle='round,pad=0.1',
                                   facecolor='#FEF3C7', edgecolor='#F59E0B', linewidth=2)
    ax.add_patch(s1)
    ax.text(7, 7.2, 'VONG 1: AI REVIEW (0 - 48 GIO)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#92400E')
    ax.text(7, 6.8, 'Quet hinh anh | am thanh | caption | chat luong ky thuat', ha='center', va='center',
            fontsize=8, color='#78350F')

    # Fail branch from Stage 1
    ax.annotate('', xy=(1.5, 5.8), xytext=(3.5, 6.5),
                arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.8))
    fail1 = mpatches.FancyBboxPatch((0.3, 5.2), 2.4, 0.55, boxstyle='round,pad=0.08',
                                     facecolor='#FEF2F2', edgecolor='#EF4444', linewidth=1.5)
    ax.add_patch(fail1)
    ax.text(1.5, 5.48, 'Vi pham', ha='center', va='center', fontsize=8, color='#DC2626', fontweight='bold')
    ax.text(0.5, 5.0, 'Xoa / Han che vinh vien', ha='left', va='center', fontsize=7, color='#EF4444')

    # Pass from Stage 1
    ax.annotate('', xy=(7, 6.1), xytext=(7, 6.5),
                arrowprops=dict(arrowstyle='->', color='#22C55E', lw=2))
    ax.text(7.3, 6.3, 'Qua review', ha='left', va='center', fontsize=7.5, color='#15803D')

    # Stage 2: Test Pool
    s2 = mpatches.FancyBboxPatch((3, 5.0), 8, 1.0, boxstyle='round,pad=0.1',
                                   facecolor='#EFF6FF', edgecolor='#3B82F6', linewidth=2)
    ax.add_patch(s2)
    ax.text(7, 5.65, 'VONG 2: TEST POOL (100-500 NGUOI)', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#1D4ED8')
    ax.text(7, 5.25, 'Do Watch Time% + Comment rate + Save/Share rate', ha='center', va='center',
            fontsize=8, color='#1E40AF')

    # Fail branch from Stage 2
    ax.annotate('', xy=(1.5, 4.3), xytext=(3.5, 5.0),
                arrowprops=dict(arrowstyle='->', color='#EF4444', lw=1.8))
    fail2 = mpatches.FancyBboxPatch((0.3, 3.75), 2.4, 0.55, boxstyle='round,pad=0.08',
                                     facecolor='#FEF2F2', edgecolor='#EF4444', linewidth=1.5)
    ax.add_patch(fail2)
    ax.text(1.5, 4.03, 'Engagement thap', ha='center', va='center', fontsize=8, color='#DC2626', fontweight='bold')
    ax.text(0.5, 3.55, 'Dung phan phoi\n(video ton tai, khong ai thay)', ha='left', va='center', fontsize=7, color='#EF4444')

    # Pass from Stage 2
    ax.annotate('', xy=(7, 4.6), xytext=(7, 5.0),
                arrowprops=dict(arrowstyle='->', color='#22C55E', lw=2))
    ax.text(7.3, 4.82, 'Chi so tot', ha='left', va='center', fontsize=7.5, color='#15803D')

    # Stage 3: Expand
    s3 = mpatches.FancyBboxPatch((3, 3.5), 8, 1.0, boxstyle='round,pad=0.1',
                                   facecolor='#F0FDF4', edgecolor='#22C55E', linewidth=2)
    ax.add_patch(s3)
    ax.text(7, 4.15, 'VONG 3: MO RONG PHA', ha='center', va='center',
            fontsize=10, fontweight='bold', color='#15803D')
    ax.text(7, 3.75, '5,000 nguoi  -->  50,000 nguoi  -->  FYP toan cau', ha='center', va='center',
            fontsize=8, color='#166534')

    ax.annotate('', xy=(7, 3.1), xytext=(7, 3.5),
                arrowprops=dict(arrowstyle='->', color='#22C55E', lw=2.5))

    # FYP badge
    fyp = mpatches.FancyBboxPatch((4.5, 2.3), 5, 0.8, boxstyle='round,pad=0.12',
                                    facecolor='#EE1D52', edgecolor='none', linewidth=0)
    ax.add_patch(fyp)
    ax.text(7, 2.7, 'FYP — FOR YOU PAGE', ha='center', va='center',
            fontsize=12, fontweight='bold', color='white')

    # Bottom key: 7 nguyen nhan 0 view
    kbox = mpatches.FancyBboxPatch((0.3, 0.4), 13.4, 1.7, boxstyle='round,pad=0.15',
                                    facecolor='#FFFBEB', edgecolor='#F59E0B', linewidth=1.5)
    ax.add_patch(kbox)
    ax.text(7, 1.8, '7 NGUYEN NHAN VIDEO BI 0 VIEW:', ha='center', va='center',
            fontsize=9, fontweight='bold', color='#92400E')
    reasons = ['1. Tai khoan moi (Trust Score thap)', '2. Dang trong hang cho AI review',
               '3. Shadowban', '4. Quyen rieng tu bi sai', '5. Noi dung trung lap',
               '6. Caption tu cam', '7. Watch Time kem (bi dung o vong 2)']
    col1 = reasons[:4]; col2 = reasons[3:]
    for i, r in enumerate(reasons):
        col = 1.0 if i < 4 else 7.5
        row_y = 1.42 - (i % 4) * 0.28
        ax.text(col, row_y, r, ha='left', va='center', fontsize=7.2, color='#78350F')

    plt.tight_layout(pad=0.5)
    path = os.path.join(OUT, 'quy-trinh-phan-phoi-tiktok.png')
    fig.savefig(path, dpi=150, bbox_inches='tight', facecolor='#FFFFFF')
    plt.close(fig)
    print(f'[OK] quy-trinh-phan-phoi-tiktok.png ({os.path.getsize(path)//1024}KB)')


if __name__ == '__main__':
    sys.stdout.reconfigure(encoding='utf-8')
    print('[1/1] Tao flowchart quy trinh phan phoi TikTok...')
    make_quy_trinh_phan_phoi_tiktok()
    print('Done!')
