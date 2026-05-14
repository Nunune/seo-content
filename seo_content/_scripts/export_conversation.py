"""
export_conversation.py — Xuất cuộc trò chuyện từ Claude Code JSONL sang Markdown.
Usage: python export_conversation.py <jsonl_path> <output_md>
"""
import json, sys, os, re
from datetime import datetime

jsonl_path = sys.argv[1]
output_path = sys.argv[2]

turns = []

with open(jsonl_path, encoding='utf-8') as f:
    for raw in f:
        raw = raw.strip()
        if not raw:
            continue
        try:
            obj = json.loads(raw)
        except Exception:
            continue

        t = obj.get('type', '')
        if t not in ('user', 'assistant'):
            continue

        msg = obj.get('message', {})
        role = msg.get('role', t)
        content = msg.get('content', '')
        timestamp = obj.get('timestamp', '')

        # Xử lý content: string hoặc list of blocks
        if isinstance(content, list):
            text_parts = []
            for block in content:
                if not isinstance(block, dict):
                    continue
                btype = block.get('type', '')

                if btype == 'text':
                    txt = block.get('text', '').strip()
                    if txt:
                        text_parts.append(txt)

                elif btype == 'tool_use':
                    name = block.get('name', '')
                    inp = block.get('input', {})
                    if name in ('Write', 'Edit', 'Read'):
                        fp = inp.get('file_path', '')
                        label = os.path.basename(fp) if fp else ''
                        text_parts.append(f'> 🔧 **{name}** → `{label}`')
                    elif name in ('PowerShell', 'Bash'):
                        cmd = str(inp.get('command', ''))
                        if len(cmd) > 200:
                            cmd = cmd[:200] + '...'
                        text_parts.append(f'> 💻 **{name}:**\n> ```\n> {cmd}\n> ```')
                    elif name == 'Glob':
                        text_parts.append(f'> 🔍 **Glob:** `{inp.get("pattern","")}`')
                    elif name == 'Grep':
                        text_parts.append(f'> 🔍 **Grep:** `{inp.get("pattern","")}`')
                    elif name == 'Agent':
                        text_parts.append(f'> 🤖 **Agent:** {inp.get("description","")[:80]}')
                    elif name == 'Skill':
                        text_parts.append(f'> ⚡ **Skill:** `{inp.get("skill","")}` {inp.get("args","")[:60]}')
                    else:
                        text_parts.append(f'> 🔧 **{name}**')

                elif btype == 'tool_result':
                    rc = block.get('content', '')
                    if isinstance(rc, list):
                        for item in rc:
                            if isinstance(item, dict) and item.get('type') == 'text':
                                snippet = item.get('text', '')[:400].strip()
                                if snippet:
                                    text_parts.append(f'> ```\n> {snippet}\n> ```')
                                break
                    elif isinstance(rc, str) and rc.strip():
                        snippet = rc.strip()[:400]
                        text_parts.append(f'> ```\n> {snippet}\n> ```')

                elif btype == 'image':
                    src = block.get('source', {})
                    # Check for file path in source
                    url = src.get('url', src.get('data', ''))[:80]
                    text_parts.append(f'> 🖼️ **[Image]** {url}')

            content = '\n\n'.join(p for p in text_parts if p.strip())

        elif not isinstance(content, str):
            content = str(content)

        content = content.strip()
        if content:
            turns.append({
                'role': role,
                'content': content,
                'timestamp': timestamp,
            })

# Gộp các turn liên tiếp cùng role (tool_result nằm trong assistant turn)
merged = []
for turn in turns:
    if merged and merged[-1]['role'] == turn['role']:
        merged[-1]['content'] += '\n\n' + turn['content']
    else:
        merged.append(dict(turn))

# Build markdown
lines = []
lines.append('# Cuộc Trò Chuyện Claude Code — Bản Đầy Đủ')
lines.append(f'\n**Ngày xuất:** {datetime.now().strftime("%Y-%m-%d %H:%M")}')
lines.append(f'**File nguồn:** `{os.path.basename(jsonl_path)}`')
lines.append(f'**Tổng số lượt:** {len(merged)} (user: {sum(1 for t in merged if t["role"]=="user")} | assistant: {sum(1 for t in merged if t["role"]=="assistant")})')
lines.append('\n---\n')

for i, turn in enumerate(merged, 1):
    role = turn['role']
    ts = turn.get('timestamp', '')[:19].replace('T', ' ')
    if role == 'user':
        lines.append(f'## [{i}] 👤 User  <sub>{ts}</sub>\n')
    else:
        lines.append(f'## [{i}] 🤖 Assistant  <sub>{ts}</sub>\n')
    lines.append(turn['content'])
    lines.append('\n---\n')

output = '\n'.join(lines)
with open(output_path, 'w', encoding='utf-8') as f:
    f.write(output)

total_kb = os.path.getsize(output_path) // 1024
print(f'[OK] {len(merged)} luot → {output_path} ({total_kb}KB)')
