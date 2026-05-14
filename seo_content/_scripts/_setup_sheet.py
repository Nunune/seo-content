# -*- coding: utf-8 -*-
"""Setup Google Sheet: ghi header + data mẫu với tiếng Việt đầy đủ."""
import sys
import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT = r"D:\Nunu-Claude\credentials\service-account.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

sheet_url = sys.argv[1] if len(sys.argv) > 1 else (
    "https://docs.google.com/spreadsheets/d/1m4B3nbQtOy8FGVBJWd-iVBTSnVKaDTXkHUf2lMi6Ras/edit"
)

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT, scopes=SCOPES)
gc = gspread.authorize(creds)
sh = gc.open_by_url(sheet_url)
ws = sh.get_worksheet(0)

# Header row với tiếng Việt đầy đủ
headers = [
    "Từ khóa", "Category", "Author", "Target",
    "Trạng thái", "Điểm SEO", "Link Drive", "URL Website", "Slug", "Ghi chú"
]
ws.update(values=[headers], range_name="A1:J1")

# Format header
ws.format("A1:J1", {
    "backgroundColor": {"red": 0.2, "green": 0.2, "blue": 0.2},
    "textFormat": {
        "bold": True,
        "foregroundColor": {"red": 1.0, "green": 1.0, "blue": 1.0},
        "fontSize": 10,
    },
    "horizontalAlignment": "CENTER",
})
ws.freeze(rows=1)

# Data mẫu — từ khóa phù hợp seongon.com
rows = [
    ["SEO On-page là gì",              "", "", "", "chưa viết", "", "", "", "", ""],
    ["Google Analytics 4 là gì",       "", "", "", "chưa viết", "", "", "", "", ""],
    ["cách viết caption TikTok",       "", "", "", "chưa viết", "", "", "", "", ""],
    ["máy lọc không khí tốt nhất 2025","", "", "", "chưa viết", "", "", "", "", ""],
    ["đầu tư căn hộ Hà Nội có nên không","","","","chưa viết","", "", "", "", ""],
]
ws.update(values=rows, range_name="A2:J6")

print("Sheet setup OK — 5 từ khóa mẫu đã được thêm")
