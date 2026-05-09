# Nunu-Claude — Google Ads Mobile Rank Checker

Tool tự động kiểm tra thứ hạng quảng cáo Google Ads trả phí trên giao diện mobile,
phát hiện đối thủ mới, ghi kết quả vào Google Sheets với màu sắc cạnh tranh.

## Slash command

```
/check-rank --sheet <URL_GOOGLE_SHEET> [--headed] [--no-vpn]
```

## Cấu trúc

```
check_rank/
  main.py               # Entry point
  crawler.py            # Playwright + Pixel 7 emulation
  vpn_manager.py        # Windscribe IP rotation
  human_behavior.py     # Mô phỏng hành vi người thật
  ad_parser.py          # Tìm quảng cáo trong SERP
  competitor_tracker.py # Phân loại đối thủ: tracked / mới / lần đầu
  sheets_writer.py      # Ghi Google Sheets + màu sắc
  config_loader.py      # Đọc CSV + JSON config

data/
  keywords.csv          # Danh sách từ khóa (keyword, lat, lng, location_name, competitor_domains, category)
  competitors.csv       # Đối thủ theo dõi (domain, brand_name, short_name)
  thresholds.json       # Ngưỡng màu cạnh tranh
  history/              # JSON lưu kết quả mỗi lần chạy

credentials/
  service_account.json  # Google Service Account key (tự tạo, không commit)
```

## Setup lần đầu

```bash
pip install -r requirements.txt
python -m playwright install chromium
windscribe login
```

## Chạy

```bash
python -m check_rank.main --sheet "https://docs.google.com/spreadsheets/d/ID/edit"
python -m check_rank.main --sheet ID --headed          # Có trình duyệt (ít bị CAPTCHA)
python -m check_rank.main --sheet ID --no-vpn          # Tắt VPN
python -m check_rank.main --sheet ID --dry-run         # Chạy thử không ghi Sheets
```

## Màu sắc trong Sheets

| Màu | Ý nghĩa |
|-----|---------|
| Xanh lá | Cạnh tranh thấp |
| Vàng | Cạnh tranh trung bình |
| Đỏ | Cạnh tranh cao |
| Cam | 🆕 Đối thủ lần đầu thấy |
| Vàng nhạt | ⚠️ Đối thủ chưa trong danh sách |

## Cột output Sheets

Từ khóa | Vị trí | Danh mục | Ad# | Tên QC | Domain | TH viết tắt | Loại ĐT | Mức CT | Mô tả QC | Ghi chú | IP check

## VPN (Windscribe Free)

- 10GB/tháng miễn phí → đủ cho ~1000+ lần check/tháng (30 KW × 3 lần/ngày = ~27MB/ngày)
- Servers miễn phí: US, Canada, GB, FR, NL, HK
- Tự xoay sau 3–7 lần search ngẫu nhiên
- Không có IP Việt Nam → bù bằng `gl=vn` URL param + Playwright geolocation API

## Khung giờ check gợi ý (cron)

```
# Ví dụ Windows Task Scheduler hoặc cron WSL
08:00  # Giờ bắt đầu ngày làm việc
12:00  # Giữa trưa (cạnh tranh thay đổi)
17:00  # Cuối giờ làm việc
```
