"""Phân loại và theo dõi đối thủ qua các lần chạy."""

import json
import os
import glob
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .config_loader import Competitor


# Loại đối thủ
TYPE_TRACKED = "tracked"         # Có trong competitors.csv
TYPE_NEW_UNTRACKED = "new_untracked"  # Chưa trong list nhưng đã thấy lần trước
TYPE_FIRST_TIME = "first_time"   # Chưa bao giờ thấy


def _load_all_seen_domains(history_dir: str) -> set[str]:
    """Đọc tất cả domain đã từng xuất hiện từ các file history cũ."""
    seen = set()
    pattern = os.path.join(history_dir, "*.json")
    for fpath in glob.glob(pattern):
        try:
            with open(fpath, encoding="utf-8") as f:
                data = json.load(f)
            for entry in data.get("results", []):
                for ad in entry.get("ads", []):
                    d = ad.get("domain", "").lower().strip()
                    if d:
                        seen.add(d)
        except Exception:
            continue
    return seen


def classify_ads(
    ads: list[dict],
    competitors_db: dict,
    history_dir: str,
) -> list[dict]:
    """
    Bổ sung trường 'competitor_type', 'short_name', 'brand_name' vào mỗi ad.
    """
    seen_domains = _load_all_seen_domains(history_dir)
    enriched = []
    for ad in ads:
        domain = ad.get("domain", "").lower().strip()
        ad = dict(ad)  # copy

        if domain in competitors_db:
            comp = competitors_db[domain]
            ad["competitor_type"] = TYPE_TRACKED
            ad["short_name"] = comp.short_name
            ad["brand_name"] = comp.brand_name
        elif domain in seen_domains:
            ad["competitor_type"] = TYPE_NEW_UNTRACKED
            ad["short_name"] = domain
            ad["brand_name"] = domain
        else:
            ad["competitor_type"] = TYPE_FIRST_TIME
            ad["short_name"] = domain
            ad["brand_name"] = domain

        enriched.append(ad)
    return enriched


def count_tracked(ads: list[dict]) -> int:
    return sum(1 for a in ads if a.get("competitor_type") == TYPE_TRACKED)


def has_new_competitors(ads: list[dict]) -> bool:
    return any(
        a.get("competitor_type") in (TYPE_NEW_UNTRACKED, TYPE_FIRST_TIME)
        for a in ads
    )


def save_history(results: list[dict], history_dir: str):
    """Lưu kết quả lần chạy vào file JSON theo timestamp."""
    os.makedirs(history_dir, exist_ok=True)
    ts = datetime.now().strftime("%Y-%m-%d_%H%M%S")
    fpath = os.path.join(history_dir, f"{ts}.json")
    payload = {
        "timestamp": datetime.now().isoformat(),
        "results": results,
    }
    with open(fpath, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return fpath
