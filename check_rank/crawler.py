"""
Playwright crawler với:
- Chrome thật (channel="chrome") thay vì Chromium → khó detect hơn
- Persistent browser profile (lưu cookie giữa các lần chạy)
- Tor SOCKS5 proxy (chỉ browser dùng, không ảnh hưởng hệ thống)
- Pixel 7 mobile emulation + geolocation
- playwright-stealth evasion
"""

import os
import sys
import time
import urllib.parse
from typing import Optional

from . import ad_parser, human_behavior

# Thư mục lưu Chrome profile (cookie, localStorage...)
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CHROME_PROFILE_DIR = os.path.join(_ROOT, "data", "chrome_profile")


def build_search_url(keyword: str) -> str:
    q = urllib.parse.quote(keyword)
    return f"https://www.google.com.vn/search?q={q}&gl=vn&hl=vi&pws=0&num=10"


def search(
    keyword: str,
    lat: float,
    lng: float,
    headed: bool = True,
    max_ads: int = 10,
    proxy_url: Optional[str] = None,
    tor_manager=None,
    max_retries: int = 3,
) -> dict:
    """
    Tìm kiếm Google mobile và trả về paid ads.
    Khi dùng Tor và bị timeout/CAPTCHA, tự xoay circuit và retry tối đa max_retries lần.
    """
    from playwright.sync_api import sync_playwright
    try:
        from playwright_stealth import Stealth
        use_stealth = True
    except ImportError:
        use_stealth = False

    search_url = build_search_url(keyword)
    result = {"ads": [], "captcha": False, "error": None, "url": search_url}

    os.makedirs(CHROME_PROFILE_DIR, exist_ok=True)

    # Timeout lâu hơn khi dùng Tor (exit node chậm hơn IP thường)
    goto_timeout = 60000 if proxy_url else 35000

    def _single_attempt(playwright) -> dict:
        """Một lần thử duy nhất, trả về dict kết quả."""
        attempt_result = {"ads": [], "captcha": False, "error": None}

        device = playwright.devices.get("Pixel 7") or playwright.devices.get("Pixel 5")

        launch_args = [
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-setuid-sandbox",
            "--lang=vi-VN,vi",
            "--disable-notifications",
            "--disable-popup-blocking",
        ]

        launch_kwargs = dict(
            headless=False,
            args=launch_args,
            channel="chrome",
        )

        if proxy_url:
            launch_kwargs["proxy"] = {"server": proxy_url}

        browser = playwright.chromium.launch(**launch_kwargs)

        context_kwargs = dict(
            **device,
            locale="vi-VN",
            timezone_id="Asia/Ho_Chi_Minh",
            geolocation={"latitude": lat, "longitude": lng, "accuracy": 10},
            permissions=["geolocation"],
            extra_http_headers={
                "Accept-Language": "vi-VN,vi;q=0.9,en-US;q=0.8,en;q=0.7",
                "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                "Accept-Encoding": "gzip, deflate, br",
                "Upgrade-Insecure-Requests": "1",
            },
        )

        profile_state = os.path.join(CHROME_PROFILE_DIR, "storage_state.json")
        if os.path.exists(profile_state):
            context_kwargs["storage_state"] = profile_state

        context = browser.new_context(**context_kwargs)
        page = context.new_page()

        try:
            human_behavior.pre_search_behavior(page)
            page.goto(search_url, timeout=goto_timeout, wait_until="domcontentloaded")
            time.sleep(2.0)

            if ad_parser.is_captcha_page(page):
                attempt_result["captcha"] = True
                attempt_result["error"] = "CAPTCHA detected"
                _save_debug_screenshot(page, keyword)
            else:
                human_behavior.simulate_reading_scroll(page)
                attempt_result["ads"] = ad_parser.detect_ads(page, max_ads=max_ads)
                context.storage_state(path=profile_state)

        except Exception as e:
            attempt_result["error"] = str(e)
            _save_debug_screenshot(page, keyword)
        finally:
            context.close()
            browser.close()

        return attempt_result

    def _run_with_retry(playwright):
        attempts = max_retries if (proxy_url and tor_manager) else 1
        for attempt in range(1, attempts + 1):
            if attempt > 1:
                print(f"  [Tor] Retry {attempt}/{attempts} với circuit mới ...", flush=True)

            r = _single_attempt(playwright)

            if not r["error"] and not r["captcha"]:
                result["ads"] = r["ads"]
                return

            is_tor_error = proxy_url and (
                "ERR_TIMED_OUT" in (r["error"] or "")
                or "ERR_CONNECTION_REFUSED" in (r["error"] or "")
                or "ERR_EMPTY_RESPONSE" in (r["error"] or "")
                or r["captcha"]
            )

            if is_tor_error and tor_manager and attempt < attempts:
                print(f"  [Tor] Đổi exit node (circuit {attempt}) ...", flush=True)
                tor_manager.new_circuit()
                continue

            # Lỗi cuối hoặc không phải Tor error
            result["captcha"] = r["captcha"]
            result["error"] = r["error"]
            return

    if use_stealth:
        stealth = Stealth(
            navigator_platform_override="Linux armv8l",
            navigator_languages_override=("vi-VN", "vi", "en-US", "en"),
        )
        with stealth.use_sync(sync_playwright()) as p:
            _run_with_retry(p)
    else:
        with sync_playwright() as p:
            _run_with_retry(p)

    return result


def _save_debug_screenshot(page, keyword: str):
    """Lưu screenshot khi gặp lỗi để dễ debug."""
    try:
        debug_dir = os.path.join(_ROOT, "data", "debug_screenshots")
        os.makedirs(debug_dir, exist_ok=True)
        safe_kw = keyword[:30].replace(" ", "_").replace("/", "_")
        path = os.path.join(debug_dir, f"{safe_kw}.png")
        page.screenshot(path=path, full_page=False)
        print(f"  [Debug] Screenshot: {path}")
    except Exception:
        pass
