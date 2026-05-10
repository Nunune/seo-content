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
            # NOTE: Alt text may or may not have quotes — handle both cases
            alt_match = re.search(r'Alt text:\s*"?([^"\n]+)"?', block_text)
            file_match = re.search(r'File name:\s*(\S+\.(?:webp|png|jpg|jpeg))', block_text)

            alt_text = alt_match.group(1).strip() if alt_match else 'image'
            file_name = file_match.group(1) if file_match else ''

            image_found = False
            image_path = ''
            if file_name and images_dir:
                for ext in ['', '.webp', '.png', '.jpg', '.jpeg']:
                    base = os.path.splitext(file_name)[0]
                    check_paths = [
                        os.path.join(images_dir, file_name),
                        os.path.join(images_dir, base + ext),
                    ]
                    for cp in check_paths:
                        if os.path.exists(cp):
                            image_found = True
                            image_path = cp
                            break
                    if image_found:
                        break

            if image_found:
                result.append(f'![{alt_text}]({image_path})')
            else:
                result.append(f'> 📷 **[CHỖ NÀY CHÈN ẢNH: {file_name}]**')

        i += 1
        continue

    result.append(line)
    i += 1

with open(output_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(result))

print('Preprocessed:', output_path)
