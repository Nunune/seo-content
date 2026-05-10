"""
append_readme.py — Gắn README.md vào cuối _preprocessed.md trước khi convert sang .docx

Usage:
  python append_readme.py <preprocessed_path> <readme_path>

Kết quả: chèn thêm vào cuối preprocessed_path một section "Phụ lục: Hướng dẫn đăng bài"
với nội dung từ README.md (bỏ dòng H1 tiêu đề đầu, giữ nguyên phần còn lại).
"""

import sys, os, re

preprocessed_path = sys.argv[1]
readme_path       = sys.argv[2]

if not os.path.exists(readme_path):
    print(f'[SKIP] README not found: {readme_path}')
    sys.exit(0)

with open(readme_path, encoding='utf-8') as f:
    readme = f.read()

# Bỏ dòng H1 đầu tiên (tiêu đề bài — đã có trong docx rồi)
readme = re.sub(r'^#[^#][^\n]*\n', '', readme, count=1).lstrip('\n')

appendix = (
    '\n\n---\n\n'
    '## Phụ lục: Hướng dẫn đăng bài\n\n'
    + readme
)

with open(preprocessed_path, 'a', encoding='utf-8') as f:
    f.write(appendix)

print(f'[OK] README appended to: {os.path.basename(preprocessed_path)}')
