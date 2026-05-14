"""
Đọc Google Sheet → JSON list các hàng cần xử lý.
Điều kiện: có Từ khóa VÀ (Trạng thái == "chưa viết" HOẶC Trạng thái trống).
Category để trống → agent sẽ tự classify.
Usage: python batch_read_sheet.py <sheet_url> [worksheet_name]
Output: JSON array to stdout
"""
import json
import sys

import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT = r"D:\Nunu-Claude\credentials\service-account.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def main():
    if len(sys.argv) < 2:
        print("Usage: batch_read_sheet.py <sheet_url> [worksheet_name]", file=sys.stderr)
        sys.exit(1)

    sheet_url = sys.argv[1]
    ws_name = sys.argv[2] if len(sys.argv) > 2 else None

    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT, scopes=SCOPES)
    gc = gspread.authorize(creds)
    sh = gc.open_by_url(sheet_url)
    ws = sh.worksheet(ws_name) if ws_name else sh.get_worksheet(0)

    headers = ws.row_values(1)
    col = {h: i for i, h in enumerate(headers)}  # 0-based index

    all_rows = ws.get_all_values()[1:]  # skip header row
    pending = []
    for i, row in enumerate(all_rows, start=2):

        def cell(name, r=row):
            idx = col.get(name)
            if idx is None or idx >= len(r):
                return ""
            return r[idx].strip()

        keyword = cell("Từ khóa")
        status = cell("Trạng thái")

        # Xử lý hàng có keyword VÀ (status trống hoặc "chưa viết")
        if keyword and status in ("chưa viết", ""):
            target_raw = cell("Target")
            try:
                target = int(target_raw) if target_raw else 85
            except ValueError:
                target = 85

            pending.append({
                "row": i,
                "keyword": keyword,
                "category": cell("Category"),   # có thể trống — agent tự classify
                "author": cell("Author"),
                "target": target,
            })

    print(json.dumps(pending, ensure_ascii=False))


if __name__ == "__main__":
    main()
