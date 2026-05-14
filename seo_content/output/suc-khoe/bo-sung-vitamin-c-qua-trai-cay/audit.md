# Audit Report: Bổ Sung Vitamin C Qua Trái Cây

**Từ khóa:** bổ sung vitamin C qua trái cây
**Slug:** bo-sung-vitamin-c-qua-trai-cay
**Ngày audit:** 2026-05-13
**Vòng lặp:** 1 (75 → 90/100)

---

## Kết quả tổng hợp

| Phase | Điểm | Max | Trạng thái |
|-------|------|-----|------------|
| GĐ1 — Nghiên cứu | 9 | 10 | ✅ Pass |
| GĐ2 — Cấu trúc | 15 | 15 | ✅ Pass |
| GĐ3 — E-E-A-T | 28 | 30 | ✅ Pass |
| GĐ4 — Media | 6 | 10 | ⚠️ Warn |
| GĐ5 — Linking | 9 | 10 | ✅ Pass |
| GĐ6 — Technical | 9 | 10 | ✅ Pass |
| GĐ7A — GEO cơ bản | 6 | 7 | ✅ Pass |
| GĐ7B — AIO chuyên sâu | 8 | 8 | ✅ Pass |
| **TỔNG** | **90** | **100** | **✅ Đạt mục tiêu** |

---

## Chi tiết từng phase

### GĐ1 — Nghiên cứu: 9/10
- ✅ Primary keyword + 5 secondary + LSI đầy đủ
- ✅ Search intent: Informational xác định đúng
- ✅ PAA 7 câu hỏi
- ✅ 3 competitors phân tích sâu
- ✅ Content gap 6 điểm rõ ràng
- ⚠️ Volume/difficulty chưa có số liệu chính xác

### GĐ2 — Cấu trúc: 15/15
- ✅ Title: 59 ký tự, keyword đầu, có năm 2026
- ✅ Meta description: ~155 ký tự, có CTA
- ✅ Slug chuẩn: `bo-sung-vitamin-c-qua-trai-cay`
- ✅ H1 duy nhất, có keyword
- ✅ H2/H3 logic, standaloneable

### GĐ3 — E-E-A-T: 28/30
- ✅ Authority note tác giả ngay đầu bài
- ✅ Phân tích giá tác giả (original data) về chi phí bổ sung vitamin C
- ✅ 5 nguồn uy tín có hyperlink thực (National Academies, USDA, JAFC, Nutrients, WHO)
- ✅ BLUF + hook + keyword trong 100 từ đầu
- ✅ FAQ block 5 câu hỏi từ PAA
- ✅ Số liệu cụ thể: mg/100g, %, liều RDA theo nhóm
- ⚠️ Còn thiếu first-hand experience thật từ tác giả
- ⚠️ Chưa có expert quote từ chuyên gia dinh dưỡng thứ ba

### GĐ4 — Media: 6/10
- ✅ 2 image blocks với Alt text và File name
- ⚠️ Chưa có ảnh thật — cần chạy generate_images.py
- ⚠️ Biểu đồ hàm lượng vitamin C sẽ tạo tự động bằng matplotlib

### GĐ5 — Linking: 9/10
- ✅ External: Nutrients, National Academies (×2), USDA, JAFC, WHO (×2) — tất cả có hyperlink
- ✅ Internal: `kham-suc-khoe-tong-quat` active trong body text
- ⚠️ Chỉ có 1 internal link (chuẩn yêu cầu 3-5) — 2 bài còn lại chưa viết

### GĐ6 — Technical: 9/10
- ✅ JSON-LD Article schema (headline, description, datePublished, author, publisher)
- ✅ JSON-LD FAQPage schema (5 Q&A)
- ✅ Author (Person) + Organization embedded
- ⚠️ Chưa test Google Rich Results Test (cần sau khi đăng)
- ⚠️ Core Web Vitals chưa kiểm tra (cần sau khi đăng)

### GĐ7A — GEO Cơ bản: 6/7
- ✅ Q&A structure rõ ràng
- ✅ BLUF đầu mỗi section
- ✅ Bảng so sánh 2 bảng
- ✅ 8+ số liệu cụ thể với nguồn
- ✅ Định nghĩa thuật ngữ rõ ràng
- ⚠️ JavaScript-independent rendering chưa verify

### GĐ7B — AIO Chuyên sâu: 8/8
- ✅ Direct Answer 40-60 từ sau mỗi H2 câu hỏi
- ✅ Semantic Triple (Subject-Predicate-Object)
- ✅ Question-based headings khớp PAA
- ✅ Definition block ("Vitamin C (axit ascorbic) là...")
- ✅ Listicle có tiêu đề + giải thích
- ✅ 8+ số liệu có nguồn và năm
- ✅ Bảng so sánh có cột "Phù hợp cho ai"
- ✅ TL;DR box ngay sau H1
- ✅ Freshness: "Cập nhật: 13/05/2026"
- ✅ Disambiguation: vitamin C tự nhiên vs tổng hợp
- ✅ Original data: phân tích chi phí tác giả

---

## Tiến độ cải thiện

| Vòng | Điểm | Delta | Thay đổi chính |
|------|------|-------|----------------|
| 0 (baseline) | 75 | — | Bài viết gốc |
| 1 | **90** | **+15** | Title fix, authority note, hyperlinks, JSON-LD schema, disambiguation, original data |

---

## Việc còn lại

1. **Tạo ảnh** (sẽ tự động): `generate_images.py` → biểu đồ cột hàm lượng vitamin C
2. **Xuất .docx** (tự động): `export-bo-sung-vitamin-c-qua-trai-cay.docx`
3. **Sau khi đăng:** Test JSON-LD tại Google Rich Results Test, kiểm tra Core Web Vitals
