"""Windscribe CLI wrapper với IP rotation ngẫu nhiên."""

import random
import subprocess
import sys
import time
from typing import Optional

import requests

CLI_PATH = r"C:\Program Files\Windscribe\windscribe-cli.exe"

# Server miễn phí của Windscribe (dùng country code hoặc city name)
WINDSCRIBE_SERVERS = ["US", "CA", "GB", "FR", "NL", "HK", "DE", "NO"]

# Thời gian chờ sau khi đổi server (giây)
CONNECT_WAIT_RANGE = (5, 10)


def _run_windscribe(args: list[str], timeout: int = 40) -> tuple[int, str]:
    """Chạy lệnh windscribe-cli, trả về (returncode, stdout)."""
    try:
        result = subprocess.run(
            [CLI_PATH] + args,
            capture_output=True, text=True, timeout=timeout,
            encoding="utf-8", errors="replace",
        )
        return result.returncode, (result.stdout + result.stderr).strip()
    except FileNotFoundError:
        print(f"[VPN] Không tìm thấy: {CLI_PATH}", file=sys.stderr)
        return -1, "not_found"
    except subprocess.TimeoutExpired:
        return -1, "timeout"


def get_current_ip() -> Optional[str]:
    """Lấy IP hiện tại qua ipify."""
    try:
        r = requests.get("https://api.ipify.org?format=json", timeout=8)
        return r.json().get("ip")
    except Exception:
        return None


class VPNManager:
    def __init__(self, searches_per_ip_range: tuple = (3, 7), enabled: bool = True):
        self.enabled = enabled
        self.searches_per_ip_range = searches_per_ip_range
        self.search_count = 0
        self.threshold = random.randint(*searches_per_ip_range)
        self.current_server: Optional[str] = None
        self.current_ip: Optional[str] = None

        # Xáo trộn thứ tự server mỗi phiên
        self.server_pool = WINDSCRIBE_SERVERS.copy()
        random.shuffle(self.server_pool)
        self.server_idx = 0

    def _next_server(self) -> str:
        server = self.server_pool[self.server_idx % len(self.server_pool)]
        self.server_idx += 1
        return server

    def connect(self, server: Optional[str] = None) -> bool:
        if not self.enabled:
            return True
        if server is None:
            server = self._next_server()

        print(f"[VPN] Kết nối → {server} ...", end=" ", flush=True)
        code, out = _run_windscribe(["connect", server])
        if code != 0:
            print(f"THẤT BẠI ({out[:80]})")
            return False

        wait = random.uniform(*CONNECT_WAIT_RANGE)
        time.sleep(wait)
        self.current_server = server
        self.current_ip = get_current_ip()
        print(f"OK (IP: {self.current_ip})")
        return True

    def rotate_if_needed(self) -> bool:
        """Gọi sau mỗi search. Trả về True nếu đã xoay IP."""
        self.search_count += 1
        if not self.enabled:
            return False
        if self.search_count >= self.threshold:
            self.search_count = 0
            self.threshold = random.randint(*self.searches_per_ip_range)
            print(f"[VPN] Đã {self.search_count} lần → xoay IP (next threshold: {self.threshold})")
            self.connect()
            return True
        return False

    def disconnect(self):
        if not self.enabled:
            return
        print("[VPN] Ngắt kết nối ...", end=" ", flush=True)
        _run_windscribe(["disconnect"])
        print("OK")

    def status(self) -> dict:
        return {
            "enabled": self.enabled,
            "server": self.current_server,
            "ip": self.current_ip,
            "searches_this_ip": self.search_count,
            "threshold": self.threshold,
        }


