import urllib.request
import os
import sys

IMAGES_DIR = r"D:\Nunu-Claude\seo_content\output\social-media\vi-pham-chinh-sach-tiktok\images"

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'image/webp,image/apng,image/*,*/*;q=0.8',
    'Referer': 'https://www.google.com/',
}

DOWNLOADS = [
    {
        'filename': 'screenshot-thong-bao-vi-pham-tiktok.png',
        'urls': [
            'https://blog.dktcdn.net/files/cach-go-vi-pham-tieu-chuan-cong-dong-tiktok.png',
            'https://cellphones.com.vn/sforum/wp-content/uploads/2023/09/cach-go-vi-pham-tieu-chuan-cong-dong-tiktok-5.jpg',
            'https://cellphones.com.vn/sforum/wp-content/uploads/2023/09/cach-go-vi-pham-tieu-chuan-cong-dong-tiktok-8.jpg',
            'https://cdnv2.tgdd.vn/mwg-static/common/News/1574036/cach-kiem-tra-tai-khoan-tiktok-co-vi-pham-khong-2.jpg',
        ]
    },
    {
        'filename': 'screenshot-thu-vien-am-nhac-tiktok.png',
        'urls': [
            'https://cdn.rankyak.com/31314/accessing-cml-on-mobile.png',
            'https://www.petsonq.com/wp-content/uploads/2023/08/PETS-ON-Q-14.png',
            'https://boksi.com/hs-fs/hubfs/Blog%20images/Screenshot_2022-12-08-14-39-24-38_50ef9f5a0f3fc24b6f0ffc8843167fe4.jpg',
            'https://cdn.rankyak.com/31316/tiktok-commercial-music-library-infographic.png',
        ]
    },
    {
        'filename': 'screenshot-khang-nghi-tiktok.png',
        'urls': [
            'https://blog.dktcdn.net/files/cach-go-vi-pham-tieu-chuan-cong-dong-tiktok-4.png',
            'https://images.squarespace-cdn.com/content/v1/6028101b47193120a4863356/2222f06d-4837-45d5-80e0-8b9b625aadb4/2+report+a+problem',
            'https://images.squarespace-cdn.com/content/v1/6028101b47193120a4863356/a719f437-20d2-4b03-aeac-42fb45c90b45/3+report+video',
            'https://blog.dktcdn.net/files/cach-go-vi-pham-tieu-chuan-cong-dong-tiktok-1.png',
        ]
    },
]


def download(url, dest):
    req = urllib.request.Request(url, headers=HEADERS)
    with urllib.request.urlopen(req, timeout=20) as resp:
        data = resp.read()
    if len(data) < 5000:
        raise ValueError(f'File quá nhỏ ({len(data)} bytes) — có thể bị redirect hoặc 404')
    with open(dest, 'wb') as f:
        f.write(data)
    return len(data)


os.makedirs(IMAGES_DIR, exist_ok=True)

for item in DOWNLOADS:
    dest = os.path.join(IMAGES_DIR, item['filename'])
    success = False
    for url in item['urls']:
        try:
            size = download(url, dest)
            print(f"[OK] {item['filename']} ({size // 1024}KB) ← {url}")
            success = True
            break
        except Exception as e:
            print(f"[FAIL] {url} → {e}")
    if not success:
        print(f"[SKIP] {item['filename']} — không tải được từ bất kỳ URL nào")
