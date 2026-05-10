import re, os, sys

draft_path = sys.argv[1]
output_path = sys.argv[2]
images_dir = sys.argv[3] if len(sys.argv) > 3 else ''

with open(draft_path, encoding='utf-8') as f:
    content = f.read()

result = []
lines = content.split('\n')
i = 0

while i < len(lines):
    line = lines[i]
    stripped = line.strip()

    if stripped.startswith('<!--'):
        is_image_block = stripped.startswith('<!-- [ẢNH]')
        block_lines = [line]
        if '-->' not in stripped:
            i += 1
            while i < len(lines) and '-->' not in lines[i]:
                block_lines.append(lines[i])
                i += 1
            if i < len(lines):
                block_lines.append(lines[i])
        block_text = '\n'.join(block_lines)

        if is_image_block:
            alt_match = re.search(r'[Aa]lt(?:\s+text)?[:\s]+["\']?([^"\'|\n\-\-]+)["\']?', block_text)
            file_match = re.search(r'File:\s*(\S+\.(?:webp|png|jpg|jpeg))', block_text, re.IGNORECASE)
            alt_text = alt_match.group(1).strip().rstrip('"\'') if alt_match else 'image'
            file_name = file_match.group(1) if file_match else ''

            image_found = False
            image_path = ''
            if file_name and images_dir:
                check_path = os.path.join(images_dir, file_name)
                if os.path.exists(check_path):
                    image_found = True
                    image_path = check_path
                else:
                    base = os.path.splitext(file_name)[0]
                    for ext in ['.webp', '.png', '.jpg', '.jpeg']:
                        cp = os.path.join(images_dir, base + ext)
                        if os.path.exists(cp):
                            image_found = True
                            image_path = cp
                            break

            if image_found:
                result.append(f'![{alt_text}]({image_path})')
            else:
                display_name = file_name if file_name else '(chua co ten file)'
                result.append(f'> [CHO NAY CHEN ANH: {display_name}]')

        i += 1
        continue

    result.append(line)
    i += 1

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print('Preprocessed:', output_path)
