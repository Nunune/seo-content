"""
Generate 2 images for cho-thue-can-ho-novaland-pho-quang article:
  - so-sanh-the-botanica-golden-mansion.png  (comparison infographic)
  - vi-tri-novaland-pho-quang-ban-do.png     (distance schematic map)
"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

OUT = r"D:\Nunu-Claude\seo_content\output\bat-dong-san\cho-thue-can-ho-novaland-pho-quang\images"

# ─────────────────────────────────────────────
# IMAGE 1 — Comparison infographic
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 5))
fig.patch.set_facecolor('#F9FAFB')
ax.set_facecolor('#F9FAFB')
ax.axis('off')

# Title
ax.text(0.5, 0.95, 'So sánh 2 dự án Novaland trên đường Phổ Quang',
        ha='center', va='top', fontsize=13, fontweight='bold',
        color='#111827', transform=ax.transAxes)

# Column headers
for x, label, color in [(0.26, 'The Botanica', '#10B981'),
                         (0.74, 'Golden Mansion', '#3B82F6')]:
    ax.text(x, 0.84, label, ha='center', va='center', fontsize=12,
            fontweight='bold', color='white', transform=ax.transAxes,
            bbox=dict(boxstyle='round,pad=0.4', facecolor=color, edgecolor='none'))

# Row data: (icon, label, botanica_val, golden_val)
rows = [
    ('Vị trí',       '104 Phổ Quang,\nQ.Tân Bình',     'Phổ Quang,\nQ.Phú Nhuận'),
    ('Quy mô',       '3 tòa tháp · ~700 căn',           '4 tòa tháp · 1.000+ căn'),
    ('Diện tích',    '50–120 m²  (1–3 PN)',             '50–130 m²  (1–3 PN)'),
    ('Giá thuê',     'Từ 12 triệu/tháng',               'Từ 14 triệu/tháng'),
    ('Phù hợp',      'Gia đình Việt\nyên tĩnh hơn',     'Expat, chuyên gia\nquốc tế'),
]

row_colors = ['#FFFFFF', '#F0FDF4', '#FFFFFF', '#F0FDF4', '#FFFFFF']
y_positions = [0.70, 0.55, 0.41, 0.28, 0.14]

for idx, (row, y, bg) in enumerate(zip(rows, y_positions, row_colors)):
    label, b_val, g_val = row

    # Row background
    ax.add_patch(FancyBboxPatch((0.03, y - 0.07), 0.94, 0.13,
                                 boxstyle='round,pad=0.01',
                                 facecolor=bg, edgecolor='#E5E7EB',
                                 linewidth=0.5, transform=ax.transAxes))

    # Label column
    ax.text(0.10, y, label, ha='center', va='center',
            fontsize=9.5, color='#374151', fontweight='bold',
            transform=ax.transAxes)

    # The Botanica value
    ax.text(0.295, y, b_val, ha='center', va='center',
            fontsize=9, color='#065F46', transform=ax.transAxes)

    # Golden Mansion value
    ax.text(0.745, y, g_val, ha='center', va='center',
            fontsize=9, color='#1E40AF', transform=ax.transAxes)

# Vertical dividers for columns
for xv in [0.195, 0.50]:
    ax.plot([xv, xv], [0.08, 0.79], color='#D1D5DB', linewidth=1.0,
            transform=ax.transAxes)

# Footer note
ax.text(0.5, 0.03, 'Nguồn: batdongsan.com.vn, dotproperty.com.vn — tổng hợp tháng 5/2026',
        ha='center', va='bottom', fontsize=7.5, color='#9CA3AF',
        transform=ax.transAxes, style='italic')

plt.tight_layout(pad=0.3)
plt.savefig(f'{OUT}/so-sanh-the-botanica-golden-mansion.png',
            dpi=150, bbox_inches='tight', facecolor='#F9FAFB')
plt.close()
print('Saved: so-sanh-the-botanica-golden-mansion.png')

# ─────────────────────────────────────────────
# IMAGE 2 — Distance schematic map
# ─────────────────────────────────────────────
fig, ax = plt.subplots(figsize=(9, 6))
fig.patch.set_facecolor('#F0F9FF')
ax.set_facecolor('#F0F9FF')
ax.set_xlim(0, 10)
ax.set_ylim(0, 7)
ax.axis('off')

# Title
ax.text(5, 6.6, 'Vị trí căn hộ Novaland Phổ Quang — Khoảng cách đến các điểm trọng yếu',
        ha='center', va='center', fontsize=11, fontweight='bold', color='#111827')

# Central node — Novaland Phổ Quang
cx, cy = 5, 3.5
circle_main = plt.Circle((cx, cy), 0.85, color='#3B82F6', zorder=5)
ax.add_patch(circle_main)
ax.text(cx, cy + 0.15, 'Novaland', ha='center', va='center',
        fontsize=9, fontweight='bold', color='white', zorder=6)
ax.text(cx, cy - 0.25, 'Phổ Quang', ha='center', va='center',
        fontsize=8, color='#DBEAFE', zorder=6)

# Surrounding nodes: (x, y, label_line1, label_line2, distance, color, emoji)
nodes = [
    (2.2, 5.8, 'San bay', 'Tan Son Nhat', '3–5 phut', '#EF4444'),
    (7.8, 5.8, 'Quan 1', 'Trung tam TP', '15–20 phut', '#8B5CF6'),
    (2.0, 1.4, 'Truong QT', 'BVIS / BV Intl', '5–10 phut', '#10B981'),
    (8.0, 1.4, 'Benh vien', 'Vinmec / FV', '10–15 phut', '#F59E0B'),
    (5.0, 0.5, 'Phu My Hung', 'Quan 7', '25–35 phut', '#6366F1'),
]

for nx, ny, l1, l2, dist, color in nodes:
    # Draw circle
    circ = plt.Circle((nx, ny), 0.65, color=color, alpha=0.15, zorder=3)
    ax.add_patch(circ)
    circ2 = plt.Circle((nx, ny), 0.65, color=color, fill=False,
                         linewidth=2, zorder=4)
    ax.add_patch(circ2)

    ax.text(nx, ny + 0.18, l1, ha='center', va='center',
            fontsize=8.5, fontweight='bold', color=color, zorder=5)
    ax.text(nx, ny - 0.18, l2, ha='center', va='center',
            fontsize=7.5, color='#374151', zorder=5)

    # Arrow from center to node
    dx, dy = nx - cx, ny - cy
    dist_len = (dx**2 + dy**2)**0.5
    shrink = 0.9
    ex = cx + dx * shrink
    ey = cy + dy * shrink
    ax.annotate('', xy=(nx - dx/dist_len*0.7, ny - dy/dist_len*0.7),
                xytext=(ex, ey),
                arrowprops=dict(arrowstyle='->', color=color,
                                lw=1.5, connectionstyle='arc3,rad=0'))

    # Distance label (midpoint)
    mx = (cx + nx) / 2 + 0.1
    my = (cy + ny) / 2 + 0.1
    ax.text(mx, my, dist, ha='center', va='center', fontsize=8,
            color=color, fontweight='bold',
            bbox=dict(boxstyle='round,pad=0.2', facecolor='white',
                      edgecolor=color, linewidth=1, alpha=0.9))

# Footer
ax.text(5, 0.1, 'Sơ đồ minh họa khoảng cách — không theo tỷ lệ thực tế | NuNu / seongon.com',
        ha='center', va='bottom', fontsize=7, color='#9CA3AF', style='italic')

plt.tight_layout(pad=0.2)
plt.savefig(f'{OUT}/vi-tri-novaland-pho-quang-ban-do.png',
            dpi=150, bbox_inches='tight', facecolor='#F0F9FF')
plt.close()
print('Saved: vi-tri-novaland-pho-quang-ban-do.png')

print('Done. Both images created.')
