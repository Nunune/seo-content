import json, sys

path = sys.argv[1]
with open(path, encoding='utf-8') as f:
    for i, line in enumerate(f):
        if not line.strip():
            continue
        obj = json.loads(line)
        t = obj.get('type', '')
        if t in ('user', 'assistant'):
            msg = obj.get('message', {})
            content = msg.get('content', '')
            print(f'Line {i}: type={t}')
            print(f'  msg keys: {list(msg.keys())}')
            if isinstance(content, str):
                print(f'  content str[:150]: {content[:150]}')
            elif isinstance(content, list):
                print(f'  content list len={len(content)}, [0]={str(content[0])[:200]}')
            break
