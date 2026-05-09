"""Mô phỏng hành vi người dùng thật trên trình duyệt."""

import random
import time


def type_like_human(page, selector: str, text: str):
    """Gõ text từng ký tự với delay ngẫu nhiên, đôi khi gõ sai rồi sửa."""
    page.click(selector)
    page.keyboard.press("Control+a")
    page.keyboard.press("Delete")
    time.sleep(random.uniform(0.3, 0.7))

    for i, char in enumerate(text):
        # 15% khả năng gõ sai 1 ký tự rồi xóa (chỉ với ký tự ascii)
        if i > 0 and random.random() < 0.15 and char.isascii() and char.isalpha():
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz")
            page.keyboard.press(wrong_char)
            time.sleep(random.uniform(0.08, 0.18))
            page.keyboard.press("Backspace")
            time.sleep(random.uniform(0.1, 0.25))

        page.keyboard.press(char)
        time.sleep(random.uniform(0.05, 0.18))

    time.sleep(random.uniform(0.4, 1.0))


def simulate_reading_scroll(page):
    """Cuộn trang xuống chậm rãi như đang đọc kết quả."""
    # Cuộn xuống theo từng đoạn nhỏ
    scroll_steps = random.randint(2, 4)
    total_scrolled = 0

    for _ in range(scroll_steps):
        delta = random.randint(120, 300)
        page.mouse.wheel(0, delta)
        total_scrolled += delta
        time.sleep(random.uniform(0.6, 2.2))

    # Hover qua 1-2 kết quả giả lập đọc
    try:
        links = page.locator("a[href]").all()
        if links:
            hover_count = min(random.randint(1, 2), len(links))
            for link in random.sample(links[:8], hover_count):
                try:
                    link.hover(timeout=1000)
                    time.sleep(random.uniform(0.3, 0.9))
                except Exception:
                    pass
    except Exception:
        pass

    # Cuộn lên một chút (quay lại đọc)
    scroll_back = random.randint(60, min(180, total_scrolled))
    page.mouse.wheel(0, -scroll_back)
    time.sleep(random.uniform(0.5, 1.2))


def pre_search_behavior(page):
    """Hành vi trước khi tìm kiếm: đôi khi vào homepage trước."""
    if random.random() < 0.40:
        try:
            page.goto("https://www.google.com.vn/", timeout=15000)
            page.wait_for_load_state("domcontentloaded")
            time.sleep(random.uniform(1.0, 3.0))

            # Đôi khi hover qua logo hoặc menu
            if random.random() < 0.3:
                try:
                    logo = page.locator("img[alt='Google']").first
                    logo.hover(timeout=2000)
                    time.sleep(random.uniform(0.3, 0.7))
                except Exception:
                    pass
        except Exception:
            pass


def post_search_pause(search_count: int, config_delay_range: tuple, long_pause_every_n: int, long_pause_range: tuple):
    """Dừng giữa các lần tìm kiếm. Đôi khi nghỉ dài để tránh bị phát hiện."""
    if search_count > 0 and search_count % long_pause_every_n == 0:
        wait = random.uniform(*long_pause_range)
        print(f"[Human] Nghỉ dài {wait:.0f}s sau {search_count} lần search ...")
        time.sleep(wait)
    else:
        wait = random.uniform(*config_delay_range)
        print(f"[Human] Chờ {wait:.1f}s ...")
        time.sleep(wait)
