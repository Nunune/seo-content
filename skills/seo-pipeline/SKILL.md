---
name: seo-pipeline
description: |
  Chạy toàn bộ pipeline SEO từ đầu đến cuối trong 1 lệnh duy nhất:
  research → viết bài → audit → improve loop → tạo ảnh → xuất .docx.
  Kích hoạt khi user nói: "chạy full pipeline", "viết và tối ưu bài",
  "seo-pipeline", "pipeline cho từ khóa", "làm bài từ đầu đến docx",
  "viết bài và audit luôn", "full chain SEO", "tạo bài hoàn chỉnh".
  Cú pháp: --keyword "X" --category slug [--competitor URLs] [--author "Tên, Chức danh"] [--target 85] [--max-iter 3] [--lang vi|en]
allowed-tools: [Skill, Read, Write, WebSearch, WebFetch, Glob, Bash, PowerShell]
---

# SEO Pipeline — Full Chain từ Keyword đến .docx

Chạy tuần tự 4 skills: `seo-research` → `seo-write` → `seo-audit` → `seo-improve`.
Không tự viết hoặc sửa content — chỉ điều phối skills và theo dõi tiến độ.

## Input

User gọi với: $ARGUMENTS

Parse các tham số:
- `--keyword "X"` — BẮT BUỘC
- `--category slug` — BẮT BUỘC (VD: digital-marketing, social-media, suc-khoe, gia-dung)
- `--competitor URL1 URL2` — tùy chọn, tối đa 5 URL đối thủ để phân tích
- `--author "Tên, Chức danh"` — tùy chọn, override tác giả trong draft
- `--target N` — điểm audit mục tiêu (mặc định: 85)
- `--max-iter N` — số vòng improve tối đa (mặc định: 3)
- `--lang vi|en` — ngôn ngữ (mặc định: vi)

Nếu thiếu `--keyword` hoặc `--category`: hỏi user ngay, không tiếp tục.

## Quy trình

### 0. Chuẩn bị

Tạo slug từ keyword: bỏ dấu tiếng Việt → thay space/ký tự đặc biệt bằng `-` → viết thường.
VD: "content marketing là gì" → `content-marketing-la-gi`

```
=== SEO PIPELINE ===
Keyword  : {keyword}
Category : {category}
Slug     : {slug}
Target   : {target}/100
Output   : seo_content/output/{category}/{slug}/
```

### 1. Research

```
[1/4] seo-research đang chạy...
```

Gọi Skill `seo-research`:
```
--keyword "{keyword}" --category {category} [--competitor URL1 URL2] [--lang {lang}]
```

Kết quả: `seo_content/output/{category}/{slug}/research.md`

```
[1/4] seo-research: DONE
```

### 2. Viết bài

```
[2/4] seo-write đang chạy...
```

Gọi Skill `seo-write`:
```
--keyword "{keyword}" --category {category} --research seo_content/output/{category}/{slug}/research.md [--author "{author}"] [--lang {lang}]
```

Kết quả: `seo_content/output/{category}/{slug}/draft.md`

```
[2/4] seo-write: DONE
```

### 3. Audit baseline

```
[3/4] seo-audit đang chạy (lấy điểm ban đầu)...
```

Gọi Skill `seo-audit`:
```
--file seo_content/output/{category}/{slug}/draft.md --keyword "{keyword}"
```

Sau khi xong, dùng Read tool đọc `audit.json` → lấy `total_score` làm `initial_score`.

```
[3/4] seo-audit: DONE — Điểm ban đầu: {initial_score}/100
```

### 4. Improve loop + ảnh + export

```
[4/4] seo-improve đang chạy (target: {target}/100, max {max_iter} vòng)...
```

Gọi Skill `seo-improve`:
```
--draft seo_content/output/{category}/{slug}/draft.md --keyword "{keyword}" --target {target} --max-iter {max_iter}
```

Skill này tự động xử lý:
- Vòng lặp fix cho đến khi đạt target (hoặc hết max-iter)
- Tải ảnh screenshot từ web (tự động)
- Tạo ảnh diagram/chart bằng matplotlib
- Xuất `export-{slug}.docx` với ảnh nhúng
- Tạo `README.md` (điểm + TODO + tips)
- Cập nhật `content-index.md`

### 5. Báo cáo tổng kết

Đọc lại `audit.json` → lấy `final_score`.

```
=== SEO PIPELINE — HOÀN THÀNH ===

Keyword  : {keyword}
Category : {category}
Slug     : {slug}

Điểm SEO : {initial_score} → {final_score}/100 ({delta:+} điểm)
Target   : {target}/100 → {ĐẠT ✓ | CHƯA ĐẠT ✗}

Files tạo ra:
  research.md
  draft.md (đã tối ưu)
  audit.md + audit.json
  export-{slug}.docx
  README.md
  images/ ({n} ảnh)

Vị trí: seo_content/output/{category}/{slug}/
```

Nếu đạt target: `Bài sẵn sàng đăng — xem TODO trong README.md trước khi upload CMS.`
Nếu chưa đạt: `Đạt {final_score}/100. Xem audit.md để sửa thủ công phần còn lại.`

## Xử lý lỗi

- Nếu bất kỳ skill nào báo lỗi: dừng lại, thông báo skill nào lỗi và lý do, hỏi user có muốn tiếp tục không.
- Không tự ý skip skill để đẩy nhanh tiến độ.
- Nếu seo-audit tạo `audit.json` nhưng không đọc được: tiếp tục với `initial_score = "N/A"`, không dừng pipeline.
