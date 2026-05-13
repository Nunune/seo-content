# SEO Content Workspace

Bộ công cụ viết và tối ưu nội dung SEO theo chuẩn Google 2025-2026, tích hợp với Claude Code.

Hỗ trợ toàn bộ quy trình từ nghiên cứu từ khóa → viết bài → chấm điểm → tự động cải thiện → xuất file Word sẵn sàng đăng.

---

## Quy trình

```
/seo-research → /seo-write → /seo-audit → /seo-improve
                                                 ↓ (tự động, không cần thêm lệnh)
                                          loop fix đến score ≥ 85
                                                 ↓
                                          tạo ảnh (matplotlib + Mermaid)
                                                 ↓
                                          xuất export-{slug}.docx
                                                 ↓
                                          tạo README.md (score + TODO + tips)
                                                 ↓
                                          → /seo-pagespeed (sau khi đăng live)
```

---

## Slash Commands

| Command | Mô tả |
|---------|-------|
| `/seo-research` | Phân tích SERP, đối thủ, content gap → research brief |
| `/seo-write` | Viết bài chuẩn E-E-A-T + GEO/AI Search |
| `/seo-audit` | Chấm điểm 8 giai đoạn (0-100), phát hiện lỗi cụ thể |
| `/seo-improve` | Auto-fix loop → ảnh → docx → README (all-in-one) |
| `/seo-image` | Tạo ảnh diagram/chart bằng matplotlib + Mermaid |
| `/seo-webp` | Convert PNG/JPG → WebP trước khi upload CMS |
| `/seo-export` | Xuất file `.docx` với ảnh đã nhúng |
| `/seo-pagespeed` | Kiểm tra Core Web Vitals qua Google PageSpeed API |

### Cú pháp

```bash
/seo-research  --keyword "từ khóa" --category slug-linh-vuc
/seo-write     --keyword "từ khóa" --category slug-linh-vuc
/seo-audit     --file output/{category}/{slug}/draft.md
/seo-improve   --draft output/{category}/{slug}/draft.md --keyword "từ khóa"
/seo-pagespeed --url https://example.com --strategy both
```

---

## Thang điểm audit

| Điểm | Ý nghĩa |
|------|---------|
| 90-100 | Xuất sắc — sẵn sàng đăng |
| 75-89 | Tốt — cần chỉnh nhỏ |
| 60-74 | Trung bình — cần cải thiện |
| 40-59 | Yếu — cần viết lại một số phần |
| 0-39 | Kém — nên viết lại toàn bộ |

Điểm tối thiểu để xuất file: **85/100**

---

## Cấu trúc thư mục

```
seo_content/
  .claude/skills/          # 8 SKILL.md dùng bởi Claude Code
  _scripts/                # Shared scripts: convert, preprocess, append_readme, drive_uploader
  checklist.md             # Checklist 8 giai đoạn đầy đủ
  content-index.md         # Index bài viết + điểm audit (dùng để validate internal links)
  profiles/
    default.example.json   # Template config (copy → default.json và điền thông tin)
  output/
    {category}/
      {slug}/
        README.md          # Tóm tắt: điểm + TODO + tips tối ưu
        draft.md           # Bài viết Markdown hoàn chỉnh
        audit.md / .json   # Báo cáo điểm chi tiết
        export-{slug}.docx # File Word sẵn sàng upload CMS
        images/            # Ảnh PNG đã render
        _scripts/          # generate_images.py, preprocess.py, convert.py
```

---

## Cài đặt

### 1. Clone repo

```bash
git clone https://github.com/Nunune/seo-content.git
cd seo-content
```

### 2. Cài dependencies

```bash
python -m pip install matplotlib numpy pillow python-docx playwright google-auth-httplib2 google-auth-oauthlib google-api-python-client
python -m playwright install chromium
```

### 3. Tạo file config

```bash
cp profiles/default.example.json profiles/default.json
# Mở profiles/default.json và điền thông tin tác giả, brand, API keys
```

### 4. Dùng với Claude Code

Đặt thư mục `seo_content/` làm working directory trong Claude Code. Các slash command sẽ tự động được load từ `.claude/skills/`.

---

## Bài viết hiện có

| Slug | Category | Keyword | Điểm |
|------|----------|---------|------|
| `xay-kenh-tiktok-tu-con-so-0` | social-media | Xây kênh TikTok từ con số 0 | 89 |
| `huong-dan-capcut-cho-tiktok` | social-media | Hướng dẫn CapCut cho TikTok | 88 |
| `tiktok-shop-affiliate-ban-hang` | social-media | TikTok Shop Affiliate và bán hàng | 88 |
| `su-dung-may-lanh-tiet-kiem-dien` | gia-dung | Sử dụng máy lạnh tiết kiệm điện | 88 |
| `meo-dung-video-tiktok-nhanh-capcut` | social-media | Mẹo dựng video TikTok nhanh với CapCut | 87 |
| `cach-chon-niche-tiktok` | social-media | Cách chọn niche TikTok | 86 |
| `kiem-tien-voi-tiktok` | social-media | Kiếm tiền với TikTok | 85 |
| `ung-dung-ai-vao-seo` | digital-marketing | Ứng dụng AI vào SEO | 92 |
| `content-marketing-la-gi` | digital-marketing | Content marketing là gì | 77 |
| `cho-thue-can-ho-novaland-pho-quang` | bat-dong-san | Cho thuê căn hộ Novaland Phổ Quang | 70 |
