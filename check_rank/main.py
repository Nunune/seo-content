"""
CLI entry point cho Google Ads Mobile Rank Checker.

Cách dùng:
  python -m check_rank.main --input data/keywords.csv --sheet <URL hoặc ID>
  python -m check_rank.main --input data/keywords.csv --sheet <URL> --headed
  python -m check_rank.main --input data/keywords.csv --sheet <URL> --no-vpn
"""

import argparse
import os
import sys
import time
from datetime import datetime

# Fix encoding cho Windows console (hỗ trợ tiếng Việt)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")

# Thêm thư mục gốc vào path để import hoạt động khi chạy từ bất kỳ đâu
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from check_rank import competitor_tracker, crawler, human_behavior
from check_rank.config_loader import load_keywords, load_competitors, load_thresholds
from check_rank.tor_manager import TorManager
from check_rank.sheets_writer import SheetsWriter

DEFAULT_KEYWORDS   = os.path.join(_ROOT, "data", "keywords.csv")
DEFAULT_COMPETITORS = os.path.join(_ROOT, "data", "competitors.csv")
DEFAULT_THRESHOLDS  = os.path.join(_ROOT, "data", "thresholds.json")
DEFAULT_HISTORY_DIR = os.path.join(_ROOT, "data", "history")
DEFAULT_CREDENTIALS = os.path.join(_ROOT, "credentials", "service_account.json")


def parse_args():
    p = argparse.ArgumentParser(
        description="Kiểm tra thứ hạng Google Ads trả phí trên mobile",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ví dụ:
  python -m check_rank.main --sheet "https://docs.google.com/spreadsheets/d/..."
  python -m check_rank.main --sheet <SHEET_ID> --headed --no-vpn
  python -m check_rank.main --input data/keywords.csv --sheet <URL>
        """,
    )
    p.add_argument("--input", default=DEFAULT_KEYWORDS,
                   help=f"File CSV từ khóa (default: {DEFAULT_KEYWORDS})")
    p.add_argument("--competitors", default=DEFAULT_COMPETITORS,
                   help="File CSV đối thủ")
    p.add_argument("--thresholds", default=DEFAULT_THRESHOLDS,
                   help="File JSON ngưỡng màu sắc")
    p.add_argument("--sheet", default=None,
                   help="URL hoặc ID Google Spreadsheet để ghi kết quả (bắt buộc nếu không --dry-run)")
    p.add_argument("--credentials", default=DEFAULT_CREDENTIALS,
                   help="Đường dẫn file Google Service Account JSON")
    p.add_argument("--headed", action="store_true",
                   help="Không dùng nữa (Chrome thật luôn headed). Giữ để tương thích.")
    p.add_argument("--no-tor", action="store_true",
                   help="Tắt Tor proxy (dùng IP thật hiện tại, không xoay IP)")
    p.add_argument("--no-vpn", action="store_true",
                   help="Alias cho --no-tor (tương thích ngược)")
    p.add_argument("--tab-name", default=None,
                   help="Tên tab trong Google Sheet (default: theo ngày giờ)")
    p.add_argument("--dry-run", action="store_true",
                   help="Chạy thử, không ghi vào Google Sheets")
    return p.parse_args()


def _print_competitor_summary(all_results: list, competitors_db: dict):
    """In bảng tổng hợp tất cả đối thủ tìm thấy ra terminal."""
    domain_info: dict[str, dict] = {}
    for entry in all_results:
        for ad in entry.get("ads", []):
            d = ad.get("domain", "").lower().strip()
            if not d:
                continue
            if d not in domain_info:
                comp_type = ad.get("competitor_type", "")
                short = ad.get("short_name", d)
                domain_info[d] = {
                    "short_name": short,
                    "type": comp_type,
                    "count": 0,
                    "keywords": [],
                }
            domain_info[d]["count"] += 1
            kw = entry.get("keyword", "")
            if kw not in domain_info[d]["keywords"]:
                domain_info[d]["keywords"].append(kw)

    if not domain_info:
        print("\n[Competitors] Khong tim thay quang cao nao.")
        return

    print("\n=== DANH SACH DOI THU PHAT HIEN ===")
    print(f"  {'Domain':<30} {'Loai':<18} {'So lan':>6}  Tu khoa")
    print("  " + "-" * 80)
    type_icon = {"tracked": "   ", "new_untracked": "⚠️ ", "first_time": "🆕 "}
    for d, info in sorted(domain_info.items(), key=lambda x: -x[1]["count"]):
        icon = type_icon.get(info["type"], "   ")
        kws = ", ".join(info["keywords"][:3])
        if len(info["keywords"]) > 3:
            kws += f" (+{len(info['keywords'])-3})"
        print(f"  {icon}{d:<28} {info['type']:<18} {info['count']:>6}  {kws}")
    print(f"\n  Tong: {len(domain_info)} domain | "
          f"{sum(1 for v in domain_info.values() if v['type']=='tracked')} tracked | "
          f"{sum(1 for v in domain_info.values() if v['type'] in ('new_untracked','first_time'))} chua theo doi")
    print("  => Xem sheet 'Raw_Competitors' trong Google Sheets de cap nhat brand_name/short_name")


def main():
    args = parse_args()

    if not args.dry_run and not args.sheet:
        print("[Error] --sheet là bắt buộc khi không dùng --dry-run", file=sys.stderr)
        sys.exit(1)

    # --- Load config ---
    print(f"[Init] Đọc từ khóa: {args.input}")
    keywords = load_keywords(args.input)
    print(f"[Init] Số từ khóa: {len(keywords)}")

    competitors_db = load_competitors(args.competitors)
    print(f"[Init] Số đối thủ theo dõi: {len(competitors_db)}")

    thresholds = load_thresholds(args.thresholds)

    # --- Setup Sheets ---
    sheets: SheetsWriter = None
    if not args.dry_run:
        print(f"[Init] Kết nối Google Sheets ...")
        sheets = SheetsWriter(args.credentials, args.sheet)
        tab_name = args.tab_name or datetime.now().strftime("%Y-%m-%d %H:%M")
        sheets.create_tab(tab_name)
        print(f"[Init] Tab tạo: '{tab_name}'")

    # --- Setup Tor ---
    use_tor = not (args.no_tor or args.no_vpn)
    tor = TorManager(enabled=use_tor)
    proxy_url = None
    if use_tor:
        ok = tor.start()
        if ok:
            proxy_url = tor.proxy_url
            print(f"[Tor] Proxy sẵn sàng: {proxy_url}")
        else:
            print("[Tor] Không khởi động được. Chạy không có proxy.", file=sys.stderr)

    # --- Chạy từng từ khóa ---
    all_results = []
    search_count = 0

    for idx, kw_row in enumerate(keywords, 1):
        print(f"\n[{idx}/{len(keywords)}] '{kw_row.keyword}' @ {kw_row.location_name} ({kw_row.lat}, {kw_row.lng})")

        # Xoay Tor circuit nếu đủ N search
        if search_count > 0:
            tor.rotate_if_needed()

        # Crawl bằng Chrome thật (luôn headed)
        result = crawler.search(
            keyword=kw_row.keyword,
            lat=kw_row.lat,
            lng=kw_row.lng,
            headed=True,
            max_ads=thresholds.max_ads,
            proxy_url=proxy_url,
            tor_manager=tor if use_tor else None,
            max_retries=3,
        )

        search_count += 1

        if result["captcha"]:
            print(f"  ⚠️  CAPTCHA! Xoay circuit ngay và thử lại sau.")
            all_results.append({
                "keyword": kw_row.keyword,
                "location": kw_row.location_name,
                "ads": [],
                "captcha": True,
                "error": result["error"],
            })
            # Xoay circuit ngay sau CAPTCHA
            if use_tor:
                tor.new_circuit()
            else:
                print("  Nghỉ 90 giây ...")
                time.sleep(90)
            continue

        if result["error"]:
            print(f"  ❌ Lỗi: {result['error']}")
            all_results.append({
                "keyword": kw_row.keyword,
                "location": kw_row.location_name,
                "ads": [],
                "error": result["error"],
            })
            continue

        # Phân loại đối thủ
        ads_classified = competitor_tracker.classify_ads(
            result["ads"], competitors_db, DEFAULT_HISTORY_DIR
        )

        tracked_count = competitor_tracker.count_tracked(ads_classified)
        has_new = competitor_tracker.has_new_competitors(ads_classified)

        print(f"  ✓ {len(ads_classified)} ads | {tracked_count} đối thủ tracked"
              + (" | 🆕 có đối thủ mới!" if has_new else ""))

        for ad in ads_classified:
            icon = {"tracked": "  ", "new_untracked": "⚠️", "first_time": "🆕"}.get(
                ad.get("competitor_type", ""), "  "
            )
            print(f"    {icon} Ad#{ad['position']} {ad.get('short_name','?'):12} | {ad.get('title','')[:50]}")

        record = {
            "keyword": kw_row.keyword,
            "location": kw_row.location_name,
            "category": kw_row.category,
            "lat": kw_row.lat,
            "lng": kw_row.lng,
            "ads": ads_classified,
            "ip": tor.current_ip if hasattr(tor, "current_ip") else None,
        }
        all_results.append(record)

        # Ghi vào Sheets
        if sheets:
            sheets.write_keyword_results(
                kw_row, ads_classified, thresholds,
                current_ip=tor.current_ip if hasattr(tor, "current_ip") else None,
            )

        # Pause giữa các search
        human_behavior.post_search_pause(
            search_count,
            thresholds.search_delay_range,
            thresholds.long_pause_every_n,
            thresholds.long_pause_range,
        )

    # --- Lưu history ---
    history_path = competitor_tracker.save_history(all_results, DEFAULT_HISTORY_DIR)
    print(f"\n[Done] Lưu history: {history_path}")

    # --- Auto resize cột ---
    if sheets:
        sheets.auto_resize_columns()
        # Ghi sheet Raw_Competitors với tất cả domain tìm thấy
        sheets.write_raw_competitors(all_results, competitors_db)
        print(f"[Done] Kết quả ghi vào Google Sheets ✓")

    # --- In bảng tổng hợp đối thủ ra terminal ---
    _print_competitor_summary(all_results, competitors_db)

    # --- Dừng Tor ---
    tor.stop()

    # --- Summary ---
    total = len(all_results)
    captcha_count = sum(1 for r in all_results if r.get("captcha"))
    error_count = sum(1 for r in all_results if r.get("error") and not r.get("captcha"))
    ok_count = total - captcha_count - error_count

    print(f"\n=== KẾT QUẢ ===")
    print(f"  Tổng từ khóa : {total}")
    print(f"  Thành công   : {ok_count}")
    print(f"  CAPTCHA      : {captcha_count}")
    print(f"  Lỗi khác     : {error_count}")

    if captcha_count > 0:
        print(f"\n  💡 Tor circuit tự xoay sau mỗi CAPTCHA. Nếu vẫn bị, chạy lại sau 10 phút.")


if __name__ == "__main__":
    main()
