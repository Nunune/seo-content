"""Ghi kết quả vào Google Sheets với màu sắc theo mức cạnh tranh."""

import os
import sys
from datetime import datetime
from typing import Optional

import gspread
from google.oauth2.service_account import Credentials

from .competitor_tracker import TYPE_TRACKED, TYPE_NEW_UNTRACKED, TYPE_FIRST_TIME
from .config_loader import Thresholds


SCOPES = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive",
]

# Màu nền (RGB 0–1 scale cho gspread)
COLOR_GREEN  = {"red": 0.714, "green": 0.843, "blue": 0.659}
COLOR_YELLOW = {"red": 1.0,   "green": 0.898, "blue": 0.600}
COLOR_RED    = {"red": 0.918, "green": 0.600, "blue": 0.600}
COLOR_ORANGE = {"red": 1.0,   "green": 0.788, "blue": 0.502}  # first_time
COLOR_AMBER  = {"red": 1.0,   "green": 0.918, "blue": 0.620}  # new_untracked
COLOR_WHITE  = {"red": 1.0,   "green": 1.0,   "blue": 1.0}
COLOR_HEADER = {"red": 0.267, "green": 0.267, "blue": 0.267}
COLOR_HEADER_FONT = {"red": 1.0, "green": 1.0, "blue": 1.0}

HEADERS = [
    "Từ khóa", "Vị trí", "Danh mục", "Ad#",
    "Tên QC", "Domain", "TH viết tắt", "Loại ĐT",
    "Mức CT", "Mô tả QC", "Ghi chú", "IP check"
]


def _competition_level(tracked_count: int, thresholds: Thresholds) -> tuple[str, dict]:
    """Trả về (label, color) theo số đối thủ tracked."""
    if tracked_count <= thresholds.green_max:
        return "Thấp", COLOR_GREEN
    elif tracked_count <= thresholds.yellow_max:
        return "Trung bình", COLOR_YELLOW
    else:
        return "Cao", COLOR_RED


def _row_bg_color(competitor_type: str) -> Optional[dict]:
    if competitor_type == TYPE_FIRST_TIME:
        return COLOR_ORANGE
    if competitor_type == TYPE_NEW_UNTRACKED:
        return COLOR_AMBER
    return None


def _label_competitor_type(t: str) -> str:
    if t == TYPE_TRACKED:
        return "Theo dõi"
    if t == TYPE_NEW_UNTRACKED:
        return "⚠️ Mới (chưa theo dõi)"
    if t == TYPE_FIRST_TIME:
        return "🆕 Lần đầu thấy"
    return t


class SheetsWriter:
    def __init__(self, credentials_path: str, spreadsheet_url_or_id: str):
        if not os.path.exists(credentials_path):
            print(f"[Sheets] Không tìm thấy credentials: {credentials_path}", file=sys.stderr)
            print("[Sheets] Xem hướng dẫn tại credentials/README.txt", file=sys.stderr)
            raise FileNotFoundError(credentials_path)

        creds = Credentials.from_service_account_file(credentials_path, scopes=SCOPES)
        self.gc = gspread.authorize(creds)

        # Mở spreadsheet theo URL hoặc ID
        if "docs.google.com" in spreadsheet_url_or_id:
            self.spreadsheet = self.gc.open_by_url(spreadsheet_url_or_id)
        else:
            self.spreadsheet = self.gc.open_by_key(spreadsheet_url_or_id)

        self.worksheet: Optional[gspread.Worksheet] = None
        self.current_row = 2  # Hàng 1 là header

    def create_tab(self, tab_name: Optional[str] = None) -> gspread.Worksheet:
        """Tạo tab mới với tên theo ngày giờ."""
        if tab_name is None:
            tab_name = datetime.now().strftime("%Y-%m-%d %H:%M")

        # Nếu đã tồn tại tab cùng tên thì thêm suffix
        existing = [ws.title for ws in self.spreadsheet.worksheets()]
        if tab_name in existing:
            tab_name = tab_name + " (2)"

        ws = self.spreadsheet.add_worksheet(title=tab_name, rows=500, cols=len(HEADERS))
        self.worksheet = ws
        self.current_row = 2
        self._write_header()
        return ws

    def _write_header(self):
        ws = self.worksheet
        ws.update("A1", [HEADERS])
        # Format header: nền tối, chữ trắng, bold
        ws.format("A1:L1", {
            "backgroundColor": COLOR_HEADER,
            "textFormat": {
                "foregroundColor": COLOR_HEADER_FONT,
                "bold": True,
                "fontSize": 10,
            },
            "horizontalAlignment": "CENTER",
        })
        # Freeze hàng header
        ws.freeze(rows=1)

    def write_keyword_results(
        self,
        keyword_row,
        ads: list[dict],
        thresholds: Thresholds,
        current_ip: Optional[str] = None,
    ):
        """Ghi tất cả ads của 1 keyword vào sheet, trả về số hàng đã ghi."""
        if self.worksheet is None:
            raise RuntimeError("Gọi create_tab() trước")

        tracked_count = sum(1 for a in ads if a.get("competitor_type") == TYPE_TRACKED)
        competition_label, competition_color = _competition_level(tracked_count, thresholds)

        if not ads:
            # Ghi 1 hàng báo không có ad
            row_data = [
                keyword_row.keyword,
                keyword_row.location_name,
                keyword_row.category,
                "", "", "", "", "",
                competition_label,
                "Không tìm thấy quảng cáo",
                "",
                current_ip or "",
            ]
            self.worksheet.update(f"A{self.current_row}", [row_data])
            self.current_row += 1
            return

        # Tính range cần ghi
        start_row = self.current_row
        rows_to_write = []

        for ad in ads:
            comp_type = ad.get("competitor_type", "")
            note = ""
            if comp_type == TYPE_FIRST_TIME:
                note = "🆕 Đối thủ lần đầu thấy"
            elif comp_type == TYPE_NEW_UNTRACKED:
                note = "⚠️ Chưa có trong danh sách theo dõi"

            rows_to_write.append([
                keyword_row.keyword,
                keyword_row.location_name,
                keyword_row.category,
                f"Ad #{ad['position']}",
                ad.get("title", ""),
                ad.get("domain", ""),
                ad.get("short_name", ad.get("domain", "")),
                _label_competitor_type(comp_type),
                competition_label,
                ad.get("description", "")[:200],
                note,
                current_ip or "",
            ])

        end_row = start_row + len(rows_to_write) - 1
        range_str = f"A{start_row}:L{end_row}"
        self.worksheet.update(range_str, rows_to_write)

        # --- Tô màu ---
        requests = []

        for i, ad in enumerate(ads):
            row_idx = start_row + i  # 1-based
            comp_type = ad.get("competitor_type", "")
            row_bg = _row_bg_color(comp_type)

            if row_bg:
                requests.append({
                    "repeatCell": {
                        "range": {
                            "sheetId": self.worksheet.id,
                            "startRowIndex": row_idx - 1,
                            "endRowIndex": row_idx,
                            "startColumnIndex": 0,
                            "endColumnIndex": len(HEADERS),
                        },
                        "cell": {
                            "userEnteredFormat": {
                                "backgroundColor": row_bg,
                            }
                        },
                        "fields": "userEnteredFormat.backgroundColor",
                    }
                })

            # Cột "Mức CT" (index 8, cột I)
            requests.append({
                "repeatCell": {
                    "range": {
                        "sheetId": self.worksheet.id,
                        "startRowIndex": row_idx - 1,
                        "endRowIndex": row_idx,
                        "startColumnIndex": 8,
                        "endColumnIndex": 9,
                    },
                    "cell": {
                        "userEnteredFormat": {
                            "backgroundColor": competition_color,
                            "textFormat": {"bold": True},
                        }
                    },
                    "fields": "userEnteredFormat(backgroundColor,textFormat)",
                }
            })

        if requests:
            self.spreadsheet.batch_update({"requests": requests})

        self.current_row = end_row + 1

    def auto_resize_columns(self):
        """Co giãn cột theo nội dung."""
        try:
            self.spreadsheet.batch_update({"requests": [{
                "autoResizeDimensions": {
                    "dimensions": {
                        "sheetId": self.worksheet.id,
                        "dimension": "COLUMNS",
                        "startIndex": 0,
                        "endIndex": len(HEADERS),
                    }
                }
            }]})
        except Exception:
            pass

    def write_raw_competitors(self, all_results: list[dict], competitors_db: dict):
        """
        Ghi sheet 'Raw_Competitors' với tất cả domain phát hiện được trong lần chạy này.
        Nếu sheet đã tồn tại thì cập nhật, không tạo mới.
        Trả về worksheet đã ghi.
        """
        RAW_TAB = "Raw_Competitors"
        RAW_HEADERS = ["domain", "brand_name", "short_name", "lan_dau_thay", "so_lan_xuat_hien"]

        # Thu thập tất cả domain + số lần xuất hiện
        domain_counts: dict[str, int] = {}
        domain_first_seen: dict[str, str] = {}
        for entry in all_results:
            for ad in entry.get("ads", []):
                d = ad.get("domain", "").lower().strip()
                if not d:
                    continue
                domain_counts[d] = domain_counts.get(d, 0) + 1
                if d not in domain_first_seen:
                    domain_first_seen[d] = entry.get("keyword", "")

        if not domain_counts:
            return None

        # Tìm hoặc tạo sheet Raw_Competitors
        existing = {ws.title: ws for ws in self.spreadsheet.worksheets()}
        if RAW_TAB in existing:
            ws = existing[RAW_TAB]
            # Đọc domain đã có để không ghi đè brand_name người dùng đã điền
            existing_data = ws.get_all_records()
            existing_domains = {row.get("domain", "").lower(): row for row in existing_data}
        else:
            ws = self.spreadsheet.add_worksheet(title=RAW_TAB, rows=200, cols=len(RAW_HEADERS))
            ws.update("A1", [RAW_HEADERS])
            ws.format("A1:E1", {
                "backgroundColor": COLOR_HEADER,
                "textFormat": {"foregroundColor": COLOR_HEADER_FONT, "bold": True},
            })
            ws.freeze(rows=1)
            existing_domains = {}

        # Xây dựng rows cần ghi
        rows_to_write = []
        for domain, count in sorted(domain_counts.items(), key=lambda x: -x[1]):
            if domain in existing_domains:
                # Giữ nguyên brand_name/short_name người dùng đã điền, chỉ cập nhật count
                existing_row = existing_domains[domain]
                rows_to_write.append([
                    domain,
                    existing_row.get("brand_name", ""),
                    existing_row.get("short_name", ""),
                    existing_row.get("lan_dau_thay", domain_first_seen.get(domain, "")),
                    count,
                ])
            else:
                # Domain mới: điền brand_name từ competitors_db nếu có
                if domain in competitors_db:
                    c = competitors_db[domain]
                    brand = c.brand_name
                    short = c.short_name
                else:
                    brand = ""
                    short = ""
                rows_to_write.append([
                    domain, brand, short,
                    domain_first_seen.get(domain, ""),
                    count,
                ])

        # Ghi toàn bộ (xóa dữ liệu cũ từ hàng 2 trở đi rồi ghi lại)
        if rows_to_write:
            # Clear dữ liệu cũ (giữ header)
            ws.batch_clear([f"A2:E{len(rows_to_write) + 100}"])
            ws.update(f"A2", rows_to_write)

        # Tô màu dòng chưa có brand_name (người dùng cần điền)
        format_requests = []
        for i, row in enumerate(rows_to_write, 2):
            if not row[1]:  # brand_name trống
                format_requests.append({
                    "repeatCell": {
                        "range": {
                            "sheetId": ws.id,
                            "startRowIndex": i - 1,
                            "endRowIndex": i,
                            "startColumnIndex": 1,
                            "endColumnIndex": 3,
                        },
                        "cell": {
                            "userEnteredFormat": {"backgroundColor": COLOR_AMBER}
                        },
                        "fields": "userEnteredFormat.backgroundColor",
                    }
                })
        if format_requests:
            self.spreadsheet.batch_update({"requests": format_requests})

        print(f"[Sheets] Raw_Competitors: {len(rows_to_write)} domain ghi xong")
        return ws
