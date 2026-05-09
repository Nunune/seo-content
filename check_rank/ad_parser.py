"""Extract paid ads từ Google mobile SERP."""

import re
import sys
from urllib.parse import urlparse


def _extract_domain(url: str) -> str:
    """Lấy domain chính từ URL hoặc display URL."""
    if not url:
        return ""
    # Display URL dạng "abc.com › trang-con"
    url = url.split("›")[0].strip()
    # Nếu có scheme thì parse bình thường
    if "://" not in url:
        url = "https://" + url
    try:
        parsed = urlparse(url)
        host = parsed.netloc.lower()
        # Bỏ www.
        return host.lstrip("www.")
    except Exception:
        return url.lower().strip()


def _js_extract_ad(container_js: str) -> str:
    """JavaScript chạy trong page.evaluate() để extract dữ liệu 1 ad."""
    return """
    (node) => {
        if (!node) return null;

        // Tiêu đề
        let titleEl = node.querySelector('[role="heading"]')
                   || node.querySelector('h3')
                   || node.querySelector('.CCgQ5')
                   || node.querySelector('.v5yQqb');
        let title = titleEl ? titleEl.innerText.trim() : '';

        // Display URL
        let urlEl = node.querySelector('cite')
                 || node.querySelector('.qzEoUe')
                 || node.querySelector('span[role="text"]');
        let displayUrl = urlEl ? urlEl.innerText.trim() : '';

        // Href thật
        let linkEl = node.querySelector('a[href]');
        let href = linkEl ? linkEl.href : '';

        // Mô tả
        let descEl = node.querySelector('.MUxGbd')
                  || node.querySelector('.VwiC3b')
                  || node.querySelector('.lyLwlc')
                  || node.querySelector('.yDYNvb');
        let description = descEl ? descEl.innerText.trim() : '';

        // Kiểm tra có label "Tài trợ" / "Sponsored" trong node không
        let txt = node.innerText || '';
        let isAd = txt.includes('Tài trợ') || txt.includes('Sponsored');

        if (!title && !displayUrl) return null;
        return { title, display_url: displayUrl, href, description, is_ad: isAd };
    }
    """


_JS_WALK_UP = """
(sponsoredEl) => {
    let node = sponsoredEl;
    for (let i = 0; i < 12; i++) {
        node = node.parentElement;
        if (!node) break;
        if (node.hasAttribute('data-text-ad')
            || node.classList.contains('uEierd')
            || node.classList.contains('commercial-unit-mobile-top')
            || node.classList.contains('mnr-c')) {
            break;
        }
    }
    if (!node) return null;

    let titleEl = node.querySelector('[role="heading"]')
               || node.querySelector('h3')
               || node.querySelector('.CCgQ5');
    let title = titleEl ? titleEl.innerText.trim() : '';

    let urlEl = node.querySelector('cite')
             || node.querySelector('.qzEoUe')
             || node.querySelector('span[role="text"]');
    let displayUrl = urlEl ? urlEl.innerText.trim() : '';

    let linkEl = node.querySelector('a[href]');
    let href = linkEl ? linkEl.href : '';

    let descEl = node.querySelector('.MUxGbd')
              || node.querySelector('.VwiC3b')
              || node.querySelector('.lyLwlc');
    let description = descEl ? descEl.innerText.trim() : '';

    if (!title && !displayUrl) return null;
    return { title, display_url: displayUrl, href, description };
}
"""


def is_captcha_page(page) -> bool:
    """Phát hiện trang CAPTCHA hoặc block của Google."""
    try:
        content = page.content()
        size_kb = len(content) / 1024
        if size_kb < 15:
            return True
        indicators = [
            "captcha", "unusual traffic", "lưu lượng truy cập bất thường",
            "not a robot", "verify you are human", "solvechallenge",
            "form id=\"captcha",
        ]
        content_lower = content.lower()
        return any(s in content_lower for s in indicators)
    except Exception:
        return False


def detect_ads(page, max_ads: int = 10) -> list[dict]:
    """
    Tìm tất cả paid ads trên trang SERP hiện tại.
    Trả về list dict với các key: position, title, display_url, href, domain, description
    """
    ads = []

    # --- Lớp 1: Tìm "Tài trợ" / "Sponsored" label ---
    sponsored_selectors = [
        'span:text-is("Tài trợ")',
        'span:text-is("Sponsored")',
        '[aria-label="Ads"]',
        'div:text-is("Tài trợ")',
    ]

    sponsored_elements = []
    for sel in sponsored_selectors:
        try:
            els = page.locator(sel).all()
            if els:
                sponsored_elements = els
                break
        except Exception:
            continue

    if sponsored_elements:
        seen_titles = set()
        for el in sponsored_elements:
            try:
                handle = el.element_handle(timeout=2000)
                if not handle:
                    continue
                data = page.evaluate(_JS_WALK_UP, handle)
                if data and data.get("title") and data["title"] not in seen_titles:
                    seen_titles.add(data["title"])
                    domain = _extract_domain(data.get("display_url") or data.get("href", ""))
                    ads.append({
                        "position": len(ads) + 1,
                        "title": data["title"],
                        "display_url": data.get("display_url", ""),
                        "href": data.get("href", ""),
                        "domain": domain,
                        "description": data.get("description", ""),
                    })
                    if len(ads) >= max_ads:
                        break
            except Exception:
                continue

    # --- Lớp 2 (fallback): [data-text-ad] containers ---
    if not ads:
        container_selectors = [
            '[data-text-ad="1"]',
            'div[data-text-ad]',
            '.uEierd',
            '.commercial-unit-mobile-top',
        ]
        for sel in container_selectors:
            try:
                containers = page.locator(sel).all()
                if not containers:
                    continue
                seen_titles = set()
                for container in containers:
                    try:
                        handle = container.element_handle(timeout=2000)
                        if not handle:
                            continue
                        data = page.evaluate(_js_extract_ad(""), handle)
                        if data and data.get("title") and data["title"] not in seen_titles:
                            seen_titles.add(data["title"])
                            domain = _extract_domain(data.get("display_url") or data.get("href", ""))
                            ads.append({
                                "position": len(ads) + 1,
                                "title": data["title"],
                                "display_url": data.get("display_url", ""),
                                "href": data.get("href", ""),
                                "domain": domain,
                                "description": data.get("description", ""),
                            })
                            if len(ads) >= max_ads:
                                break
                    except Exception:
                        continue
                if ads:
                    break
            except Exception:
                continue

    return ads
