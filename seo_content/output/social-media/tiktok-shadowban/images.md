# Image Manifest: tiktok-shadowban

**Ngày tạo:** 2026-05-14

## Ảnh đã tạo

| File | Loại | Kích thước | Trạng thái |
|------|------|------------|------------|
| trust-score-tiktok-shadowban.png | diagram (matplotlib) | 116KB | ✅ Đã nhúng vào docx |

## Mô tả

### trust-score-tiktok-shadowban.png

Sơ đồ timeline Trust Score TikTok:
- Trục X: thời gian hoạt động (T0–T12)
- Trục Y: Trust Score (0–100)
- Đường xanh: Trust Score tăng dần → vi phạm kéo xuống → phục hồi
- Vùng đỏ: Shadowban zone (dưới ngưỡng 45*)
- Vùng xanh lá: Safe zone (reach đầy đủ)
- Annotations: 5 giai đoạn (tài khoản mới, tăng trust, vi phạm, shadowban, phục hồi)
- Footer: ghi chú ngưỡng là ước tính cộng đồng, TikTok không công bố chính thức

**Alt text:** Cơ chế Trust Score TikTok và ngưỡng shadowban

## Ảnh cần thêm (suggestions)

- `analytics-traffic-tiktok-shadowban.png` — stacked bar chart so sánh traffic source (FYP vs Profile vs Following vs Search) khi bình thường vs shadowban nhẹ vs shadowban nặng
- Có thể tạo bằng matplotlib với cùng script `generate_images.py`
