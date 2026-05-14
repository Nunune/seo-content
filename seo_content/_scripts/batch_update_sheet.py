"""
Cập nhật 1 hàng trong Google Sheet với kết quả pipeline.
Dùng named arguments để tránh lỗi PowerShell bỏ qua empty string positional args.

Usage:
  python batch_update_sheet.py <sheet_url> <row_num> [--status X] [--score X]
                               [--drive-link X] [--slug X] [--note X] [--category X]
"""
import argparse
import sys

import gspread
from google.oauth2.service_account import Credentials

SERVICE_ACCOUNT = r"D:\Nunu-Claude\credentials\service-account.json"
SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]


def col_letter(idx_1based):
    idx = idx_1based - 1
    result = ""
    while True:
        result = chr(ord("A") + idx % 26) + result
        idx = idx // 26 - 1
        if idx < 0:
            break
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("sheet_url")
    parser.add_argument("row_num", type=int)
    parser.add_argument("--status",     default="")
    parser.add_argument("--score",      default="")
    parser.add_argument("--drive-link", default="", dest="drive_link")
    parser.add_argument("--slug",       default="")
    parser.add_argument("--note",       default="")
    parser.add_argument("--category",   default="")
    args = parser.parse_args()

    creds = Credentials.from_service_account_file(SERVICE_ACCOUNT, scopes=SCOPES)
    gc = gspread.authorize(creds)
    sh = gc.open_by_url(args.sheet_url)
    ws = sh.get_worksheet(0)

    headers = ws.row_values(1)
    col_idx = {h: i + 1 for i, h in enumerate(headers)}  # 1-based

    updates = []
    for field, value in [
        ("Trạng thái", args.status),
        ("Category",   args.category),
        ("Điểm SEO",   args.score),
        ("Link Drive", args.drive_link),
        ("Slug",       args.slug),
        ("Ghi chú",   args.note),
    ]:
        if value and field in col_idx:
            updates.append({
                "range":  f"{col_letter(col_idx[field])}{args.row_num}",
                "values": [[value]],
            })

    if updates:
        ws.batch_update(updates)
        print(f"Updated row {args.row_num}: " +
              ", ".join(f"{u['range']}={u['values'][0][0]!r}" for u in updates))
    else:
        print(f"No updates for row {args.row_num}")


if __name__ == "__main__":
    main()
