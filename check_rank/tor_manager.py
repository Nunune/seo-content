"""
Quản lý Tor daemon: khởi động, xoay circuit, tắt.
Tor chạy local như SOCKS5 proxy → chỉ Playwright dùng proxy này,
Claude Code và phần còn lại của hệ thống vẫn dùng IP thật.
"""

import os
import random
import subprocess
import sys
import time
from pathlib import Path
from typing import Optional

# Tor SOCKS5 port và control port
TOR_SOCKS_PORT = 9052        # Dùng 9052 để không conflict với Tor Browser đang mở
TOR_CONTROL_PORT = 9053
TOR_CONTROL_PASS = "checkrank_tor_2026"

# Thử tìm tor.exe ở các vị trí phổ biến
_TOR_CANDIDATES = [
    r"C:\Users\{user}\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe",
    r"C:\Users\{user}\Desktop\Tor Browser\Browser\TorBrowser\Tor\tor.exe",
    r"C:\Program Files\Tor Browser\Browser\TorBrowser\Tor\tor.exe",
    r"C:\Users\{user}\AppData\Local\Tor Browser\Browser\TorBrowser\Tor\tor.exe",
    r"C:\Users\{user}\AppData\Roaming\Tor Browser\Browser\TorBrowser\Tor\tor.exe",
    r"C:\Program Files\Tor\tor.exe",
]


def find_tor_exe() -> Optional[str]:
    """Tìm đường dẫn tor.exe trên hệ thống."""
    username = os.environ.get("USERNAME", "")
    for candidate in _TOR_CANDIDATES:
        path = candidate.format(user=username)
        if os.path.exists(path):
            return path

    # Thử tìm trong PATH
    import shutil
    found = shutil.which("tor") or shutil.which("tor.exe")
    if found:
        return found

    return None


def _hash_password(tor_exe: str, password: str) -> str:
    """Dùng tor --hash-password để tạo hash cho control password."""
    try:
        result = subprocess.run(
            [tor_exe, "--hash-password", password],
            capture_output=True, text=True, timeout=10,
            encoding="utf-8", errors="replace",
        )
        # Output có dạng: "16:XXXXX..."
        for line in result.stdout.splitlines():
            if line.startswith("16:"):
                return line.strip()
    except Exception:
        pass
    return ""


class TorManager:
    def __init__(
        self,
        rotations_per_ip_range: tuple = (3, 7),
        enabled: bool = True,
    ):
        self.enabled = enabled
        self.rotations_per_ip_range = rotations_per_ip_range
        self.search_count = 0
        self.threshold = random.randint(*rotations_per_ip_range)
        self._process: Optional[subprocess.Popen] = None
        self.tor_exe: Optional[str] = None
        self.current_ip: Optional[str] = None
        self.data_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
            "data", "tor_data"
        )

    @property
    def proxy_url(self) -> str:
        return f"socks5://localhost:{TOR_SOCKS_PORT}"

    @staticmethod
    def _kill_on_port(port: int):
        """Kill bất kỳ process nào đang listen trên port (Windows netstat)."""
        try:
            r = subprocess.run(
                ["netstat", "-ano"],
                capture_output=True, text=True, timeout=5
            )
            for line in r.stdout.splitlines():
                if f":{port} " in line and "LISTENING" in line:
                    pid = int(line.split()[-1])
                    subprocess.run(["taskkill", "/F", "/PID", str(pid)],
                                   capture_output=True, timeout=5)
                    print(f"[Tor] Đã dừng process cũ (PID {pid}) trên port {port}")
                    time.sleep(1)
                    break
        except Exception:
            pass

    def start(self) -> bool:
        """Khởi động Tor daemon. Trả về True nếu thành công."""
        if not self.enabled:
            return True

        self.tor_exe = find_tor_exe()
        if not self.tor_exe:
            print(
                "[Tor] Không tìm thấy tor.exe. Cài Tor Browser từ torproject.org",
                file=sys.stderr
            )
            return False

        print(f"[Tor] Dùng: {self.tor_exe}")
        os.makedirs(self.data_dir, exist_ok=True)

        # Kill process cũ còn giữ port (tránh "address already in use")
        self._kill_on_port(TOR_SOCKS_PORT)
        self._kill_on_port(TOR_CONTROL_PORT)

        # Xóa lock + state để Tor chọn guard node mới (tránh guard cũ chậm/bị block)
        for fname in ("lock", "state"):
            fp = os.path.join(self.data_dir, fname)
            if os.path.exists(fp):
                try:
                    os.remove(fp)
                except Exception:
                    pass

        # Tạo torrc config
        hashed_pass = _hash_password(self.tor_exe, TOR_CONTROL_PASS)
        torrc_path = os.path.join(self.data_dir, "torrc")
        with open(torrc_path, "w") as f:
            f.write(f"""SocksPort {TOR_SOCKS_PORT}
ControlPort {TOR_CONTROL_PORT}
HashedControlPassword {hashed_pass}
DataDirectory {self.data_dir}
Log notice stderr
""")

        print(f"[Tor] Khởi động daemon (SOCKS5 port {TOR_SOCKS_PORT}) ...", flush=True)
        log_path = os.path.join(self.data_dir, "tor.log")
        try:
            log_file = open(log_path, "w", encoding="utf-8", errors="replace")
            self._process = subprocess.Popen(
                [self.tor_exe, "-f", torrc_path],
                stdout=log_file,
                stderr=log_file,
            )
        except Exception as e:
            print(f"[Tor] THẤT BẠI: {e}")
            return False

        # Chờ Tor bootstrap 100% bằng cách đọc log (tối đa 300 giây)
        print("[Tor] Đang kết nối mạng Tor ...", end=" ", flush=True)
        for _ in range(300):
            time.sleep(1)
            if self._process.poll() is not None:
                print("CRASHED")
                return False
            # Đọc log tìm "Bootstrapped 100%"
            try:
                with open(log_path, "r", encoding="utf-8", errors="replace") as f:
                    log_content = f.read()
                if "Bootstrapped 100%" in log_content or "Done" in log_content:
                    # Chờ 15 giây để circuit ổn định và guard relay sẵn sàng
                    time.sleep(15)
                    print("OK (100% bootstrapped)")
                    return True
            except Exception:
                pass

        print("TIMEOUT (300s)")
        return False

    def _is_ready(self) -> bool:
        """Kiểm tra Tor đã sẵn sàng nhận kết nối chưa."""
        import socket
        try:
            s = socket.create_connection(("localhost", TOR_SOCKS_PORT), timeout=1)
            s.close()
            return True
        except Exception:
            return False

    def new_circuit(self) -> bool:
        """Yêu cầu Tor xoay sang circuit mới (IP mới)."""
        if not self.enabled:
            return False
        try:
            from stem import Signal
            from stem.control import Controller
            with Controller.from_port(port=TOR_CONTROL_PORT) as ctrl:
                ctrl.authenticate(password=TOR_CONTROL_PASS)
                ctrl.signal(Signal.NEWNYM)
            # Chờ circuit mới sẵn sàng (NEWNYM có minimum 10s cooldown)
            wait = random.uniform(12, 18)
            print(f"[Tor] Đợi {wait:.0f}s circuit mới ...", end=" ", flush=True)
            time.sleep(wait)
            print("OK")
            return True
        except ImportError:
            print("[Tor] stem chưa cài: pip install stem", file=sys.stderr)
            return False
        except Exception as e:
            print(f"[Tor] Lỗi xoay circuit: {e}", file=sys.stderr)
            return False

    def rotate_if_needed(self) -> bool:
        """Gọi sau mỗi search. Xoay circuit nếu đủ N search."""
        self.search_count += 1
        if not self.enabled:
            return False
        if self.search_count >= self.threshold:
            self.search_count = 0
            self.threshold = random.randint(*self.rotations_per_ip_range)
            print(f"[Tor] Xoay circuit sau {self.threshold} search tiếp theo")
            return self.new_circuit()
        return False

    def stop(self):
        if self._process and self._process.poll() is None:
            self._process.terminate()
            self._process.wait(timeout=5)
            print("[Tor] Daemon đã dừng")
