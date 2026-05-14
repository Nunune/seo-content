---
name: seo-review
description: |
  Kiểm tra chất lượng toàn bộ pipeline SEO: review research → writing alignment →
  audit accuracy → improvement effectiveness. Đưa ra report card với letter grades
  và recommendations cụ thể.
  Trigger: "review pipeline", "check pipeline", "kiểm tra pipeline", "đánh giá pipeline",
  "check chất lượng bài", "review content", "kiểm tra hiệu suất", "QA bài viết",
  "check lại bài", "pipeline có ổn không", "review kết quả", "đánh giá kết quả".
argument-hint: --keyword "từ khóa" --category slug --slug bai-viet-slug
allowed-tools: [Read, Write, Glob]
---

# SEO Review — Kiểm Tra Chất Lượng Pipeline

Đọc toàn bộ output của pipeline (research → write → audit → improve) và đưa ra báo cáo
"report card" đánh giá chất lượng từng bước + hiệu suất tổng thể.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--keyword "X"` — **BẮT BUỘC**: từ khóa chính của bài viết
- `--category slug` — **BẮT BUỘC**: danh mục (VD: `digital-marketing`, `social-media`)
- `--slug bai-viet-slug` — **BẮT BUỘC**: slug bài viết (VD: `content-marketing-la-gi`)

Nếu thiếu bất kỳ argument nào → hỏi user trước khi tiếp tục.

`article_dir` = `D:\Nunu-Claude\seo_content\output\{category}\{slug}\`

---

## Bước 0 — Kiểm Tra Files Tồn Tại

Dùng Read tool thử đọc từng file (1-2 dòng đầu). Ghi nhận:
- `{article_dir}\research.md` → có/không
- `{article_dir}\draft.md` → **BẮT BUỘC** (nếu không có → dừng, báo lỗi)
- `{article_dir}\audit.json` → có/không (nếu không có → bỏ qua Bước 3-4)
- `{article_dir}\audit.md` → có/không

In trạng thái:
```
=== SEO REVIEW ===
Keyword  : {keyword}
Category : {category}
Slug     : {slug}

Files kiểm tra:
  [✅/❌] research.md
  [✅/❌] draft.md
  [✅/❌] audit.json
  [✅/❌] audit.md

Review sẽ chạy:
  [✅/⏭] Phase 1 — Research Quality
  [✅] Phase 2 — Writing Quality (luôn chạy)
  [✅/⏭] Phase 3 — Audit Accuracy
  [✅/⏭] Phase 4 — Improvement Efficiency
```

---

## Bước 1 — Review Research Quality

*(Bỏ qua nếu research.md không tồn tại — ghi `N/A`)*

Đọc toàn bộ `{article_dir}\research.md`. Chấm điểm theo bảng:

| Tiêu chí | Điểm | Cách kiểm tra |
|----------|------|---------------|
| Keyword intent được xác định | 10 | Có dòng "Search intent:" hoặc phân tích rõ loại intent (informational/commercial/...) |
| Keyword map đầy đủ | 10 | Có keyword chính + ≥3 keyword phụ/LSI |
| PAA / FAQ questions | 15 | Có ≥5 câu hỏi PAA hoặc FAQ cụ thể, không generic |
| Phân tích đối thủ | 20 | Có ≥3 URL đối thủ + nhận xét điểm mạnh/yếu từng URL |
| Content gap | 20 | Liệt kê rõ chủ đề/góc độ đối thủ bỏ sót hoặc chưa cover tốt |
| Format recommendation | 15 | Đề xuất rõ format (listicle/how-to/pillar/...) kèm lý do |
| Outline gợi ý | 10 | Có ít nhất outline H1 + 3 H2 gợi ý |

**Thang điểm → Grade:**
- 90-100 → A
- 75-89 → B
- 60-74 → C
- 40-59 → D
- <40 → F

---

## Bước 2 — Review Writing Quality

*(Luôn chạy — draft.md BẮT BUỘC)*

Đọc toàn bộ `{article_dir}\draft.md`. Chấm 2 nhóm:

### Nhóm 2A — Chất lượng bài độc lập (không cần research.md)

| Tiêu chí | Điểm | Cách kiểm tra |
|----------|------|---------------|
| H1 chứa keyword chính | 5 | Dòng `# ...` có keyword không? |
| Keyword trong 100 từ đầu | 5 | Đọc đoạn mở bài |
| TL;DR box ngay sau H1 | 5 | Có block `> **TL;DR` hoặc tương đương không? |
| Direct Answer dưới H2 câu hỏi | 10 | Mỗi H2 dạng "X là gì?/Làm thế nào?" có câu trả lời 40-80 từ ngay bên dưới? |
| Có ≥3 câu hỏi FAQ | 10 | Đếm số heading `### {Câu hỏi}?` trong section FAQ |
| Đoạn văn ≤4 câu | 5 | Kiểm tra 5 đoạn ngẫu nhiên — có đoạn nào >4 câu không? |
| Số liệu/thống kê có nguồn | 10 | Có ≥2 trích dẫn `(Nguồn, năm)` trong bài? |
| Internal Links block | 5 | Có `<!-- Internal Links` hoặc `<!-- Internal links` không? |
| TODO block | 5 | Có `<!-- TODO` không? |

**Max Nhóm 2A: 60 điểm**

### Nhóm 2B — Alignment với research *(chỉ khi research.md có)*

| Tiêu chí | Điểm | Cách kiểm tra |
|----------|------|---------------|
| ≥3 PAA từ research dùng làm H2/H3 | 15 | So sánh câu hỏi trong research.md với heading trong draft |
| Content gap từ research được cover | 10 | Các section/chủ đề được đề xuất trong gap có xuất hiện trong draft không? |
| Format khớp với recommendation | 10 | Research đề xuất listicle → draft có cấu trúc listicle không? |
| Keyword phụ từ research xuất hiện | 5 | Ít nhất 2-3 keyword phụ trong research xuất hiện tự nhiên trong draft? |

**Max Nhóm 2B: 40 điểm**

**Nếu không có research.md:** Chỉ chấm Nhóm 2A → quy đổi: `score_2A / 60 × 100`.

**Nếu có research.md:** Tổng = 2A + 2B (max 100).

**Thang điểm → Grade:** 90+=A, 75-89=B, 60-74=C, 40-59=D, <40=F

---

## Bước 3 — Review Audit Accuracy

*(Bỏ qua nếu audit.json không tồn tại — ghi `N/A`)*

Đọc `{article_dir}\audit.json` → lấy `phases` scores.
Đọc `{article_dir}\draft.md` → spot-check 3 phases quan trọng nhất:

### Spot-check Phase 2 — Cấu trúc

Từ draft.md, đếm thực tế:
- Số thẻ H1 (dòng bắt đầu bằng `# `)
- Số thẻ H2 (bắt đầu bằng `## `)
- Có meta description trong SEO block không?

So sánh với `phases.phase2.score` trong audit.json.

**Flag mâu thuẫn nếu:**
- Draft không có H1 nhưng phase2 score ≥ 10/15
- Draft có 2+ H1 nhưng phase2 score cao
- Draft không có meta description nhưng phase2 score = 15/15

### Spot-check Phase 3 — E-E-A-T

Từ draft.md, kiểm tra thực tế:
- Có ≥2 trích dẫn số liệu với nguồn không?
- Có author block (`<!-- Author`) không?
- Có ví dụ cụ thể/case study không?

So sánh với `phases.phase3.score` trong audit.json.

**Flag mâu thuẫn nếu:**
- Không có số liệu nguồn nào nhưng phase3 ≥ 25/30
- Không có author block nhưng phase3 = max

### Spot-check Phase 7B — AIO

Từ draft.md, kiểm tra:
- Có TL;DR box không?
- Có ≥1 H2 dạng câu hỏi không?
- Câu đầu tiên sau H2 câu hỏi có phải Direct Answer ngắn gọn không?

So sánh với `phases.phase7b.score` trong audit.json.

**Flag mâu thuẫn nếu:**
- Không có TL;DR box nhưng phase7b ≥ 6/8
- Không có H2 câu hỏi nhưng phase7b cao

### Scoring Bước 3

| Kết quả | Điểm | Grade |
|---------|------|-------|
| 0 mâu thuẫn tìm thấy | 100 | A |
| 1 mâu thuẫn nhỏ | 80 | B |
| 1 mâu thuẫn lớn hoặc 2 mâu thuẫn nhỏ | 60 | C |
| 2+ mâu thuẫn lớn | 40 | D |

---

## Bước 4 — Review Improvement Efficiency

*(Bỏ qua nếu audit.json không tồn tại — ghi `N/A`)*

Đọc `{article_dir}\audit.json` → tìm:
- `initial_score` hoặc `score_before_improve` (điểm trước khi improve)
- `total_score` (điểm cuối)
- `rounds` hoặc `improve_rounds` (số vòng improve)
- `target` (điểm mục tiêu)

**Nếu `initial_score` không có trong JSON:** Đọc `{article_dir}\audit.md` → tìm dòng "Vòng 0", "Điểm ban đầu", hoặc "initial score". Nếu vẫn không tìm được → ghi "N/A" cho phase này.

**Tính:**
- `delta = total_score - initial_score`
- `efficiency = delta / max(rounds, 1)` (điểm tăng mỗi vòng)

| Tiêu chí | Grade |
|----------|-------|
| Đạt target VÀ delta ≥ 15 | A |
| Đạt target VÀ delta < 15 | B |
| Chưa đạt target nhưng delta ≥ 10 | C |
| Chưa đạt target, delta 1-9 | D |
| delta = 0 hoặc không rõ | F |

---

## Bước 5 — Tạo Report Card

Tổng hợp tất cả phases và lưu file.

**Tính Overall Grade:**
- Nếu đủ 4 phases: average của 4 điểm số
- Nếu thiếu phase (N/A): average của các phase có dữ liệu

**Thang Overall:** 90+=A, 75-89=B, 60-74=C, 40-59=D, <40=F

Lưu `{article_dir}\review.md` với format sau:

```markdown
# SEO Review Report — {H1 lấy từ draft.md}

**Keyword:** {keyword}
**Slug:** `{slug}`
**Category:** {category}
**Review date:** {YYYY-MM-DD}

---

## Tổng quan

| Phase | Grade | Điểm | Nhận xét ngắn |
|-------|-------|------|---------------|
| Research Quality | {A-F/N/A} | {n}/100 | {1 câu nhận xét} |
| Writing Quality | {A-F} | {n}/100 | {1 câu nhận xét} |
| Audit Accuracy | {A-F/N/A} | {n}/100 | {1 câu nhận xét} |
| Improvement Efficiency | {A-F/N/A} | {n}/100 | {1 câu nhận xét} |
| **Overall Pipeline** | **{A-F}** | **{avg}/100** | |

**SEO Score cuối:** {total_score}/100

---

## Chi tiết từng Phase

### Phase 1 — Research Quality ({grade} — {n}/100)

{Nếu N/A: "research.md không tồn tại — không thể đánh giá."}

**Điểm mạnh:**
- {tiêu chí đạt điểm tốt, cụ thể}

**Gaps cần cải thiện:**
- {tiêu chí thiếu hoặc yếu, cụ thể}

---

### Phase 2 — Writing Quality ({grade} — {n}/100)

**Điểm mạnh:**
- {tiêu chí đạt — ví dụ: "TL;DR box có ngay sau H1 ✅"}

**Gaps:**
- {tiêu chí thiếu — ví dụ: "Không tìm thấy trích dẫn số liệu có nguồn"}

**Alignment với research:** {Tốt / Trung bình / Yếu / N/A}
{Nếu có research: liệt kê PAA nào được dùng, gap nào được cover}

---

### Phase 3 — Audit Accuracy ({grade})

{Nếu N/A: "audit.json không tồn tại — không thể đánh giá."}

**Spot-check kết quả:**
- Phase 2 (Cấu trúc): {Nhất quán ✅ / Mâu thuẫn ⚠️} — {lý do cụ thể}
- Phase 3 (E-E-A-T): {Nhất quán ✅ / Mâu thuẫn ⚠️} — {lý do cụ thể}
- Phase 7B (AIO): {Nhất quán ✅ / Mâu thuẫn ⚠️} — {lý do cụ thể}

---

### Phase 4 — Improvement Efficiency ({grade})

{Nếu N/A: "Không đủ dữ liệu để đánh giá (thiếu audit.json hoặc initial_score)."}

| Metric | Giá trị |
|--------|---------|
| Điểm ban đầu | {initial}/100 |
| Điểm cuối | {final}/100 |
| Delta | +{delta} điểm |
| Số vòng improve | {rounds} vòng |
| Hiệu suất | +{efficiency:.1f} điểm/vòng |
| Target | {target}/100 — {ĐẠT ✅ / CHƯA ĐẠT ❌} |

---

## Recommendations

### Ưu tiên cao — Cần làm trước khi đăng
{Chỉ xuất hiện nếu có vấn đề nghiêm trọng (Grade D hoặc F ở Phase 2)}
- [ ] {recommendation cụ thể}

### Cải thiện tiếp theo
- [ ] {suggestion — ví dụ: "Thêm 2 PAA còn thiếu từ research vào draft"}
- [ ] {suggestion}

### Nhận xét về quy trình pipeline
{Chỉ khi phát hiện pattern bất thường giữa các phases}
- {VD: "Research Phase A nhưng Writing chỉ B → draft chưa tận dụng hết insight từ research"}
- {VD: "Audit cho 22/30 E-E-A-T nhưng spot-check thấy không có số liệu nguồn → cần re-audit"}
- {VD: "Improve chỉ tăng 5 điểm sau 3 vòng → xem xét manual fix trước khi chạy lại"}
```

---

## Thông báo hoàn thành

Sau khi lưu file:
```
=== REVIEW HOÀN THÀNH ===
Report: seo_content/output/{category}/{slug}/review.md

Overall: {grade} ({avg}/100)
  Research  : {grade_r} ({n_r}/100)
  Writing   : {grade_w} ({n_w}/100)
  Audit     : {grade_a}
  Efficiency: {grade_e}

Xem report đầy đủ tại review.md
```
