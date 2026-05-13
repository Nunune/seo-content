# Báo cáo SEO Audit: Khám Sức Khỏe Tổng Quát

**Ngày audit:** 2026-05-11
**Keyword chính:** khám sức khỏe tổng quát
**Nguồn:** output/suc-khoe/kham-suc-khoe-tong-quat/draft.md

---

## Tổng điểm: 73/100 — Trung bình (cần cải thiện đáng kể)

| Giai đoạn | Điểm tối đa | Điểm đạt | Trạng thái |
|-----------|------------|---------|-----------|
| GĐ1 — Nghiên cứu | 10 | 9 | ✅ |
| GĐ2 — Cấu trúc | 15 | 14 | ✅ |
| GĐ3 — E-E-A-T / Nội dung | 30 | 24 | ⚠️ |
| GĐ4 — Media | 10 | 4 | ❌ |
| GĐ5 — Linking | 10 | 3 | ❌ |
| GĐ6 — Technical | 10 | 6 | ⚠️ |
| GĐ7A — GEO cơ bản | 7 | 6 | ✅ |
| GĐ7B — AIO chuyên sâu | 8 | 7 | ✅ |

---

## Lỗi cần sửa ngay (❌ Ưu tiên cao)

### 1. Không có external links thực tế (Phase 5)
- **Vấn đề:** Bài trích dẫn "Bộ Y tế, 2023" và "WHO, 2022" nhưng không có hyperlink URL nào. AI và Google không thể xác minh nguồn → mất tin cậy, Phase 5 chỉ đạt 3/10.
- **Hiện tại:** `...những bệnh chiếm hơn 74% tổng số ca tử vong tại Việt Nam (Bộ Y tế, 2023).`
- **Gợi ý sửa:** `...những bệnh chiếm hơn 74% tổng số ca tử vong tại Việt Nam ([Bộ Y tế, 2023](https://moh.gov.vn/...)).` — Cần tìm URL thực từ moh.gov.vn hoặc WHO.

### 2. Không có ảnh thực tế (Phase 4)
- **Vấn đề:** Ba vị trí ảnh chỉ là `<!-- [ẢNH] ... -->` placeholder. Không có `![alt text](path)` nào trong bài. Phase 4 chỉ đạt 4/10.
- **Hiện tại:** `<!-- [ẢNH] Sơ đồ quy trình khám sức khỏe tổng quát từ đăng ký → lấy kết quả -->`
- **Cần làm:** Chạy `/seo-image` để tạo ảnh diagram/chart, sau đó replace comment bằng `![Sơ đồ quy trình khám sức khỏe tổng quát](images/so-do-quy-trinh-kham-tong-quat.png)`.

### 3. Thiếu schema JSON-LD thực tế (Phase 6)
- **Vấn đề:** Chỉ có gợi ý schema trong TODO comment, không có JSON-LD block trong file. Mất khả năng xuất hiện Rich Results (FAQ cards, HowTo steps) trên SERP.
- **Hiện tại:** Không có `<script type="application/ld+json">` block nào
- **Gợi ý sửa:** Thêm block JSON-LD Article + FAQPage vào cuối bài (xem mục Schema bên dưới).

---

## Cần cải thiện (⚠️ Ưu tiên trung)

### 1. Thiếu trải nghiệm first-hand (Phase 3 — Experience)
- **Hiện tại:** Bài thuần tổng hợp thông tin, không có ví dụ/case study thực tế từ tác giả.
- **Cần làm:** Thêm 1-2 câu trải nghiệm cá nhân VD: _"Trong lần khám tổng quát gần nhất tại [bệnh viện X], tôi phát hiện chỉ số cholesterol vượt ngưỡng dù không có triệu chứng gì — đây là lý do vì sao tôi tin vào giá trị của khám định kỳ."_

### 2. Số liệu "80%" không có nguồn (Phase 3 — Expertise)
- **Hiện tại:** `...trong khi 80% bệnh lý nguy hiểm hoàn toàn có thể phát hiện sớm nếu được tầm soát đúng cách.`
- **Cần làm:** Tìm nguồn cho con số 80% hoặc thay bằng số liệu có nguồn cụ thể. Nếu không có nguồn → xóa hoặc dùng "phần lớn".

### 3. Không có internal links (Phase 5)
- **Hiện tại:** Toàn bộ internal link là TODO comment — hợp lý vì chưa có bài sức khỏe nào trong content-index. Tuy nhiên vẫn trừ điểm.
- **Cần làm:** Viết thêm bài cùng cluster sức khỏe (bảo hiểm, dinh dưỡng, tập thể dục) → quay lại nhúng link.

### 4. Author chưa có trang riêng + Person schema (Phase 7B — Author Entity)
- **Hiện tại:** Bio tác giả chỉ trong comment HTML, không xuất hiện trong body bài.
- **Cần làm:** Thêm block author visible cuối bài: `**Tác giả: Ngọc Như** — SEO Content Specialist...` + link LinkedIn.

---

## Chi tiết từng giai đoạn

### Giai đoạn 1 — Nghiên cứu (9/10)

- ✅ **Keyword map:** Từ khóa phụ ("khám tổng quát gồm những gì", "chi phí", "định kỳ") xuất hiện tự nhiên
- ✅ **Sub-topics bao phủ:** Định nghĩa, hạng mục, tần suất, chi phí, chuẩn bị, nơi khám, FAQ đầy đủ
- ✅ **PAA tích hợp:** 5 FAQ câu hỏi khớp với PAA phổ biến
- ⚠️ **Content gap:** Chưa có góc độ so sánh cụ thể giá từng bệnh viện (đây là thông tin người dùng tìm nhiều)

### Giai đoạn 2 — Cấu trúc (14/15)

- ✅ **Title tag:** "Khám Sức Khỏe Tổng Quát Gồm Những Gì? Chi Phí & Lịch Khám" — 57 ký tự, có keyword, kích thích CTR
- ✅ **Meta description:** ~158 ký tự, có keyword, có CTA "Hướng dẫn đầy đủ"
- ✅ **URL slug:** `kham-suc-khoe-tong-quat` — ngắn, chuẩn
- ✅ **H1:** Duy nhất 1, khớp title, 57 ký tự
- ⚠️ **H2/H3:** Tốt, nhưng title không có năm (2026) — có thể thêm để tăng CTR seasonal

### Giai đoạn 3 — E-E-A-T & Nội dung (24/30)

- ✅ **People-first:** Giải quyết đủ 5 câu hỏi cốt lõi, đọc xong không cần tìm thêm
- ⚠️ **Experience / số liệu:** Số liệu có (74%, 70%) nhưng một số chưa có URL nguồn; thiếu first-hand experience
- ✅ **Expertise:** Thuật ngữ y khoa dùng đúng (CEA, PSA, DEXA, ECG, PAP smear); trích dẫn WHO và Bộ Y tế
- ✅ **Authoritativeness:** Có ngày cập nhật, có tên tác giả (trong comment)
- ✅ **Mở bài:** Hook tốt, BLUF qua TL;DR, keyword trong 100 từ đầu
- ✅ **Thân bài:** Đoạn 2-4 câu, nhiều bảng/bullet, FAQ 5 câu, mật độ ~1.5%
- ✅ **Kết bài:** Tóm 4 ý chính, CTA "Đặt lịch ngay"

### Giai đoạn 4 — Media (4/10)

- ❌ **Ảnh thực tế:** Không có ảnh nào được nhúng
- ⚠️ **Alt text gợi ý:** 3 comment mô tả ảnh cần tạo rõ ràng (sơ đồ quy trình, bảng so sánh, checklist)
- ⚠️ **Tên file:** Chưa có vì chưa có ảnh

### Giai đoạn 5 — Linking (3/10)

- ❌ **Internal links:** 0 link trong body (hợp lý vì cluster sức khỏe chưa có bài nào)
- ❌ **External links:** Có 2 trích dẫn nguồn (Bộ Y tế, WHO) nhưng KHÔNG có hyperlink URL → không đếm là external link

### Giai đoạn 6 — Technical (6/10)

- ✅ **Schema types gợi ý:** Article + FAQPage + HowTo — đúng và đầy đủ
- ❌ **JSON-LD thực tế:** Chưa có block JSON-LD trong file
- ⚠️ **Author schema:** Thông tin tác giả chỉ trong comment, chưa có Person schema

### Giai đoạn 7A — GEO cơ bản (6/7)

- ✅ **Cấu trúc Q&A:** FAQ 5 câu, câu hỏi → trả lời ngay, cấu trúc rõ
- ✅ **BLUF per section:** Mỗi H2 bắt đầu bằng câu tóm tắt
- ✅ **Đoạn tự đứng được:** Hầu hết section đứng độc lập tốt
- ⚠️ **Số liệu / thống kê:** 3 số liệu nhưng "80%" thiếu nguồn
- ✅ **Định nghĩa thuật ngữ:** Block định nghĩa chuẩn "[Thuật ngữ] là [định nghĩa]"
- ✅ **Bảng so sánh / danh sách:** 5 bảng, nhiều danh sách bullet

### Giai đoạn 7B — AIO chuyên sâu (7/8)

- ✅ **Direct Answer Format:** Mỗi H2 câu hỏi có câu trả lời 40-60 từ ngay đầu
- ✅ **Semantic Triple / Entity Clarity:** Không dùng "nó/điều này", entity đầy đủ
- ✅ **Question-based Headings:** 6/7 heading dạng câu hỏi tự nhiên
- ✅ **Definition Block:** "Khám sức khỏe tổng quát là gói dịch vụ y tế toàn diện..."
- ✅ **Statistics có nguồn + năm:** (Bộ Y tế, 2023), (WHO, 2022) — cần thêm URL
- ✅ **Comparison Table:** Bảng gói khám 3 tier có cột "Phù hợp cho ai"
- ✅ **TL;DR Box:** 5 ý bullet ngay sau H1
- ✅ **Freshness Signals:** "Cập nhật: 11/05/2026"
- ⚠️ **Original Research:** Không có — bài thuần tổng hợp
- ✅ **Disambiguation:** Blockquote "Khám sức khỏe tổng quát ≠ Khám bệnh thông thường"
- ✅ **Conversational Tone:** Ngôn ngữ thân thiện, trả lời "tại sao / khi nào / làm thế nào"

---

## Gợi ý nâng cấp (từ Trung bình lên Tốt/Xuất sắc)

1. **Thêm external links URL thực** → Phase 5 có thể lên 7/10 (+4 điểm tổng)
2. **Thêm JSON-LD schema** → Phase 6 lên 9/10 (+3 điểm tổng)
3. **Thêm first-hand experience** → Phase 3 lên 27/30 (+3 điểm tổng)
4. **Tạo và nhúng ít nhất 1 ảnh** → Phase 4 lên 6/10 (+2 điểm tổng)
5. **Fix nguồn "80%"** → tăng độ tin cậy Phase 3
6. **Thêm author block visible** trong body bài

---

## Schema Markup gợi ý

```json
{
  "@context": "https://schema.org",
  "@type": "Article",
  "headline": "Khám Sức Khỏe Tổng Quát Gồm Những Gì? Chi Phí & Lịch Khám",
  "description": "Khám sức khỏe tổng quát gồm những hạng mục gì, chi phí bao nhiêu và bao lâu nên đi khám một lần? Hướng dẫn đầy đủ giúp bạn chuẩn bị đúng cách.",
  "datePublished": "2026-05-11",
  "dateModified": "2026-05-11",
  "author": {
    "@type": "Person",
    "name": "Ngọc Như",
    "jobTitle": "SEO Content Specialist",
    "url": "https://linkedin.com/in/ngocnhu"
  },
  "publisher": {
    "@type": "Organization",
    "name": "NuNu",
    "url": "https://seongon.com"
  }
}
```

```json
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "Khám sức khỏe tổng quát mất bao lâu?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Một buổi khám sức khỏe tổng quát đầy đủ thường kéo dài từ 3 đến 5 tiếng, tùy số lượng hạng mục và mức độ đông của cơ sở."
      }
    },
    {
      "@type": "Question",
      "name": "Khám sức khỏe tổng quát có cần nhịn ăn không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Cần nhịn ăn 8–10 tiếng trước khi xét nghiệm máu (đường huyết, mỡ máu) và siêu âm bụng để có kết quả chính xác. Vẫn được phép uống nước lọc bình thường."
      }
    },
    {
      "@type": "Question",
      "name": "Chi phí khám sức khỏe tổng quát hết bao nhiêu tiền?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Chi phí gói cơ bản từ 1,5–4 triệu đồng. Gói nâng cao 4–8 triệu. Gói cao cấp có MRI/CT từ 8–20 triệu đồng."
      }
    },
    {
      "@type": "Question",
      "name": "Bảo hiểm y tế có chi trả khám sức khỏe tổng quát không?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "BHYT nhà nước hiện không chi trả khám tổng quát theo gói. Bảo hiểm sức khỏe tư nhân (AIA, Bảo Việt, Manulife) có thể bao gồm — kiểm tra hợp đồng của bạn."
      }
    },
    {
      "@type": "Question",
      "name": "Kết quả khám sức khỏe tổng quát bao lâu có?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Hầu hết cơ sở trả kết quả trong ngày (4–6 tiếng). Xét nghiệm đặc biệt như sinh thiết có thể cần 3–7 ngày."
      }
    }
  ]
}
```
