---
name: seo-write
description: |
  Viết bài content SEO hoàn chỉnh theo chuẩn Google 2025-2026 (E-E-A-T + GEO).
  Kích hoạt khi user yêu cầu "viết bài SEO", "viết content", "seo write",
  "tạo bài viết chuẩn SEO", "viết blog", "tạo content", "write article",
  "viết bài cho website", "tạo bài blog", "viết bài chuẩn Google".
argument-hint: --keyword "từ khóa" --category slug-linh-vuc [--research path/to/research.md] [--author "Tên, Chức danh"] [--draft path/to/draft.md] [--lang vi|en]
allowed-tools: [WebSearch, WebFetch, Read, Write]
---

# SEO Write — Viết bài chuẩn SEO

Tạo bài viết SEO đầy đủ theo checklist 8 giai đoạn: cấu trúc chuẩn, E-E-A-T, tối ưu AI Search (GEO),
sẵn sàng copy vào CMS và đăng. Lưu ra file Markdown với đầy đủ metadata.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: từ khóa chính của bài viết
- `--category slug` — **BẮT BUỘC**: lĩnh vực/danh mục (VD: `digital-marketing`, `gia-dung`, `bat-dong-san`, `social-media`)
- `--research path` — đường dẫn file research brief từ `/seo-research` (nếu có)
- `--author "Tên, Chức danh"` — thông tin tác giả (override default.json)
- `--draft path` — đường dẫn draft có sẵn cần cải thiện (không viết từ đầu)
- `--lang vi|en` — ngôn ngữ bài viết (mặc định: vi)

Nếu không có `--keyword` hoặc `--category`, hỏi user trước khi tiếp tục.

## Quy trình thực hiện

### Bước 1 — Thu thập thông tin đầu vào

**Nếu có `--research`:** Đọc file research brief bằng Read tool.
Trích xuất: keyword map, intent, outline đề xuất, content gap, tiêu đề gợi ý.

**Nếu không có `--research`:** Thực hiện quick research:
- WebSearch keyword để nắm intent và định dạng SERP ưu tiên
- WebSearch "{keyword} câu hỏi thường gặp" để lấy 3-5 PAA
- Không cần crawl đối thủ sâu (dành cho /seo-research)

**Nếu có `--draft`:** Đọc file draft bằng Read tool. Bài sẽ được CẢI THIỆN thay vì viết từ đầu.

**Đọc profile:** Đọc `D:\Nunu-Claude\seo_content\profiles\default.json` để lấy:
- brand_name, brand_tone, target_audience, internal_link_base_url
- author_name, author_title, author_bio (nếu không có `--author`)

Nếu `--author "Tên, Chức danh"` được cung cấp, dùng thay cho default.json.

**Đọc content index:** Đọc `D:\Nunu-Claude\seo_content\content-index.md` để biết danh sách bài đã viết.
- Dùng để gợi ý internal links trong `<!-- Internal Links gợi ý -->` — **chỉ dùng slug có trong index**
- Bài liên quan chưa có trong index → để `<!-- TODO: thêm link khi bài "{chủ đề}" được viết -->`

### Bước 2 — Viết bài hoàn chỉnh

Viết bài theo cấu trúc dưới đây. **Áp dụng nghiêm ngặt mọi nguyên tắc từ checklist.**

#### Nguyên tắc bắt buộc khi viết

**Cấu trúc:**
- Chỉ 1 thẻ H1 (tiêu đề bài), chứa keyword chính, 50-60 ký tự
- H2/H3 phân cấp logic, chứa keyword phụ tự nhiên
- Mỗi H2 có thể đứng độc lập → AI Search dễ trích dẫn

**Mở bài (100-150 từ):**
- Hook 2-3 câu: nêu vấn đề/nỗi đau người đọc đang gặp
- BLUF: câu trả lời / lợi ích chính ngay đầu (đừng để người đọc tìm)
- Keyword chính xuất hiện tự nhiên trong 100 từ đầu

**Thân bài:**
- Đoạn ngắn 2-4 câu, dễ đọc trên mobile
- Dùng bullet list hoặc bảng khi liệt kê 3 items trở lên
- Mỗi section: câu chủ đề → giải thích → ví dụ cụ thể / số liệu
- Mật độ keyword ~1-2%, dùng biến thể và entity liên quan
- Không nhồi nhét keyword

**FAQ block (bắt buộc, ít nhất 3 câu):**
- Mỗi câu hỏi → trả lời ngắn gọn 2-4 câu ngay bên dưới
- Cấu trúc Q&A rõ ràng → tối ưu AI Overview, PAA

**Kết bài:**
- Tóm tắt 3-5 ý chính
- CTA rõ ràng (phù hợp brand_tone từ profile)

**E-E-A-T:**
- Nếu topic cần experience: thêm ví dụ/số liệu thực tế
- Đề xuất chỗ cần thêm ảnh bằng comment `<!-- [ẢNH] mô tả ảnh cần dùng -->`
- Đề xuất chỗ cần trích dẫn nguồn bằng comment `<!-- [NGUỒN] tìm nghiên cứu về X -->`

**GEO 7A — AI Search cơ bản:**
- Mỗi section bắt đầu bằng câu tóm tắt (BLUF per section)
- Định nghĩa thuật ngữ quan trọng rõ ràng trong văn bản
- Có số liệu / thống kê cụ thể (dù là ước tính có căn cứ)

**GEO 7B — AIO chuyên sâu (bắt buộc áp dụng):**
- **TL;DR Box**: thêm block tóm tắt 3-5 ý bullet ngay sau H1, trước phần mở bài
- **Direct Answer**: mỗi heading dạng câu hỏi → câu đầu tiên của section phải trả lời ngắn gọn 40-60 từ, tự đứng được không cần ngữ cảnh trước
- **Question-based Headings**: đặt heading dạng "X là gì?", "Làm thế nào để X?", "Tại sao X?" — khớp PAA
- **Definition Block**: mỗi thuật ngữ chính có 1-2 câu định nghĩa độc lập, format "[Thuật ngữ] là [định nghĩa]."
- **Semantic Triple**: câu theo cấu trúc Subject–Predicate–Object, không dùng đại từ mơ hồ ("nó", "điều này") — nhắc lại entity đầy đủ
- **Statistics với nguồn + năm**: ít nhất 3 số liệu cụ thể, đặt ngay sau luận điểm, format "X% người dùng... (Nguồn, năm)"
- **Comparison Table**: nếu so sánh 2+ đối tượng, dùng bảng có cột "Phù hợp cho ai"
- **Disambiguation**: có ít nhất 1 đoạn phân biệt với khái niệm dễ nhầm
- **Freshness**: thêm "Cập nhật: {ngày}" ở đầu bài và đề xuất `<!-- [TODO] dateModified schema -->`
- **Conversational Tone**: kết hợp câu ngắn (mobile) và câu dài tự nhiên, trả lời được "làm thế nào / tại sao / khi nào"

### Bước 3 — Tạo slug và lưu file

Tạo slug từ keyword: ASCII, gạch ngang, không dấu, không stopword.
Ví dụ: "hướng dẫn học lái xe ô tô 2025" → `hoc-lai-xe-o-to-2025`

Thư mục bài viết: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\`
Tạo thư mục nếu chưa có (dùng PowerShell `New-Item -ItemType Directory -Force`).

Lưu tại: `D:\Nunu-Claude\seo_content\output\{category}\{slug}\draft.md`

## Định dạng file output

```markdown
<!-- SEO Meta
Title: {tiêu đề bài — keyword đầu, 50-60 ký tự}
Meta Description: {140-160 ký tự, có keyword, có CTA}
Slug: {slug-khong-dau}
Schema types gợi ý: Article, FAQPage[, HowTo nếu bài hướng dẫn]
Keyword chính: {keyword}
Keyword phụ: {kw1}, {kw2}, {kw3}
Ngày viết: {YYYY-MM-DD}
-->

<!-- Author
Tên: {author_name}
Chức danh: {author_title}
Bio: {author_bio}
Social: {author_social}
-->

# {H1 — Tiêu đề bài viết chứa keyword chính}

{Đoạn mở bài — hook + BLUF + keyword trong 100 từ đầu}

---

## {H2 — Section 1: sub-topic quan trọng nhất}

{Nội dung section — đoạn ngắn 2-4 câu, có số liệu/ví dụ}

### {H3 — Sub-point nếu cần}

{Nội dung}

---

## {H2 — Section 2}

{Nội dung}

---

## {H2 — Section N}

{Nội dung}

---

## Câu hỏi thường gặp (FAQ)

### {Câu hỏi 1 từ PAA}

{Trả lời ngắn gọn 2-4 câu, tự đứng được không cần ngữ cảnh}

### {Câu hỏi 2}

{Trả lời}

### {Câu hỏi 3}

{Trả lời}

---

## Kết luận

{Tóm 3-5 ý chính}

{CTA phù hợp brand_tone}

---

<!-- Internal Links gợi ý
- Anchor: "{anchor text tự nhiên}" → {brand_website}/slug-bai-lien-quan
- Anchor: "{anchor text}" → {brand_website}/slug-khac
-->

<!-- TODO — Cần bổ sung trước khi đăng
- [ ] Thêm ảnh thực tế tại: [vị trí 1]
- [ ] Kiểm tra/cập nhật số liệu tại: [đoạn nào]
- [ ] Điền link internal thực tế thay cho gợi ý
- [ ] Tác giả review và thêm trải nghiệm cá nhân
-->
```

## Thông báo hoàn thành

Sau khi lưu file, báo cáo:
- Đường dẫn file đã lưu (dạng link clickable)
- Số từ ước tính
- Tiêu đề được chọn
- Danh sách TODO cần làm trước khi đăng
- Schema types gợi ý cần cài
- Gợi ý: "Dùng `/seo-audit --file seo_content/output/{category}/{slug}/draft.md --keyword "{keyword}"` để kiểm tra chất lượng trước khi đăng"
