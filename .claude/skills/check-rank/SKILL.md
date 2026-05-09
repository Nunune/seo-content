---
name: check-rank
description: |
  Kiểm tra thứ hạng quảng cáo Google Ads trả phí trên giao diện mobile.
  Kích hoạt khi user hỏi về "thứ hạng từ khóa", "vị trí quảng cáo", "check rank",
  "kiểm tra quảng cáo Google", "đối thủ đang quảng cáo", "check my ad",
  "ad rank", "paid search rank", "thứ hạng trả phí", "quảng cáo đang chạy vị trí mấy".
argument-hint: --sheet <URL_GOOGLE_SHEET> [--headed] [--no-vpn] [--dry-run]
allowed-tools: [Bash]
---

# Check Google Ads Mobile Rank

Kiểm tra vị trí quảng cáo Google Ads trả phí trên giao diện mobile (giả lập Pixel 7),
đọc danh sách từ khóa từ CSV, xoay IP qua Windscribe, mô phỏng hành vi người thật,
ghi kết quả vào Google Sheets với màu sắc cạnh tranh và cảnh báo đối thủ mới.

## Arguments

User đã gọi với: $ARGUMENTS

Parse arguments:
- `--sheet <URL hoặc ID>` — **BẮT BUỘC**: URL hoặc ID Google Sheet để ghi kết quả
- `--headed` — Hiện trình duyệt (dùng khi bị CAPTCHA)
- `--no-vpn` — Tắt xoay VPN (dùng IP hiện tại)
- `--dry-run` — Chạy thử, không ghi Sheets
- `--input <path>` — File CSV từ khóa (default: data/keywords.csv)

Nếu user không cung cấp --sheet, hỏi lại URL Google Sheet trước khi chạy.

## Lệnh chạy

```bash
cd D:\Nunu-Claude && python -m check_rank.main --sheet "<URL_HOẶC_ID>" [args...]
```

Ví dụ:
```bash
cd D:\Nunu-Claude && python -m check_rank.main --sheet "https://docs.google.com/spreadsheets/d/ABC123/edit" --headed
cd D:\Nunu-Claude && python -m check_rank.main --sheet "ABC123" --no-vpn --dry-run
```

## Xử lý kết quả

Sau khi script kết thúc, đọc output và báo cáo:
- Số từ khóa đã check
- Số ads tìm thấy
- Có đối thủ mới xuất hiện không (🆕 / ⚠️)
- Link Google Sheet để xem kết quả chi tiết
- Nếu có CAPTCHA: gợi ý thêm --headed

## Setup lần đầu (nếu chưa cài)

```bash
cd D:\Nunu-Claude
pip install -r requirements.txt
python -m playwright install chromium
```

Cần cài thủ công:
1. Windscribe app: https://windscribe.com/download → đăng nhập CLI: `windscribe login`
2. Google Service Account JSON → đặt vào `credentials/service_account.json`
3. Chia sẻ Google Sheet cho email service account
