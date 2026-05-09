"""Load keywords, competitors, and thresholds config."""

import csv
import json
import os
from dataclasses import dataclass, field
from typing import Optional


@dataclass
class KeywordRow:
    keyword: str
    lat: float
    lng: float
    location_name: str
    competitor_domains: list[str]
    category: str


@dataclass
class Competitor:
    domain: str
    brand_name: str
    short_name: str


@dataclass
class Thresholds:
    green_max: int
    yellow_max: int
    red_above: int
    new_competitor_alert: bool
    max_ads: int
    search_delay_range: tuple[int, int]
    long_pause_every_n: int
    long_pause_range: tuple[int, int]


def load_keywords(path: str) -> list[KeywordRow]:
    rows = []
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            domains_raw = row.get("competitor_domains", "").strip()
            domains = [d.strip() for d in domains_raw.split(",") if d.strip()]
            rows.append(KeywordRow(
                keyword=row["keyword"].strip(),
                lat=float(row["lat"]),
                lng=float(row["lng"]),
                location_name=row["location_name"].strip(),
                competitor_domains=domains,
                category=row.get("category", "").strip(),
            ))
    return rows


def load_competitors(path: str) -> dict[str, Competitor]:
    """Returns dict keyed by domain (lowercase)."""
    result = {}
    if not os.path.exists(path):
        return result
    with open(path, encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            domain = row["domain"].strip().lower()
            result[domain] = Competitor(
                domain=domain,
                brand_name=row["brand_name"].strip(),
                short_name=row["short_name"].strip(),
            )
    return result


def load_thresholds(path: str) -> Thresholds:
    with open(path, encoding="utf-8") as f:
        cfg = json.load(f)
    rules = cfg.get("color_rules", {})
    return Thresholds(
        green_max=rules.get("green", {}).get("max", 2),
        yellow_max=rules.get("yellow", {}).get("max", 5),
        red_above=rules.get("red", {}).get("above", 5),
        new_competitor_alert=cfg.get("new_competitor_alert", True),
        max_ads=cfg.get("max_ads_to_report", 10),
        search_delay_range=tuple(cfg.get("search_delay_range_sec", [10, 30])),
        long_pause_every_n=cfg.get("long_pause_every_n_searches", 7),
        long_pause_range=tuple(cfg.get("long_pause_range_sec", [60, 120])),
    )
