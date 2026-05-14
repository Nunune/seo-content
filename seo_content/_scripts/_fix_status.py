# -*- coding: utf-8 -*-
import sys
sys.path.insert(0, r'D:\Nunu-Claude\seo_content\_scripts')
import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT = r"D:\Nunu-Claude\credentials\service-account.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

sheet_url = sys.argv[1]
row_num = int(sys.argv[2])
status = sys.argv[3] if len(sys.argv) > 3 else "đã hoàn thành"

creds = Credentials.from_service_account_file(SERVICE_ACCOUNT, scopes=SCOPES)
gc = gspread.authorize(creds)
sh = gc.open_by_url(sheet_url)
ws = sh.get_worksheet(0)

headers = ws.row_values(1)
col_idx = {h: i + 1 for i, h in enumerate(headers)}

def col_letter(idx_1based):
    idx = idx_1based - 1
    result = ""
    while True:
        result = chr(ord("A") + idx % 26) + result
        idx = idx // 26 - 1
        if idx < 0:
            break
    return result

if "Trạng thái" in col_idx:
    cell = f"{col_letter(col_idx['Trạng thái'])}{row_num}"
    ws.update(range_name=cell, values=[[status]])
    print(f"Updated {cell} = {status!r}")
else:
    print("Column 'Trang thai' not found")
