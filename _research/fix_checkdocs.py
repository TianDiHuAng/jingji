# -*- coding: utf-8 -*-
"""改进 check_docs：只核对**最新**的"现状/当前"表述，历史轮次记录不参与比对。"""
p = 'tools/check_docs.py'
s = open(p, encoding='utf-8').read()

old = '''def scan(path, only_current=True):
    """返回 [(行号, 键, 文档值, 原文)]"""
    if not os.path.exists(path):
        return []
    out = []
    lines = open(path, encoding='utf-8').read().splitlines()
    for i, line in enumerate(lines, 1):
        # 只看"当前状态"型行：含"现状"、"当前"、"状态："
        if only_current and not re.search(r'(现状|当前|状态[:：])', line):
            continue
        for pat, key in PATTERNS:
            for m in re.finditer(pat, line):
                try:
                    v = int(m.group(1).replace(',', ''))
                except ValueError:
                    continue
                out.append((i, key, v, line.strip()[:110]))
    return out'''

new = '''def scan(path):
    """只返回**最后一条**"现状/当前"型表述中的数字（历史轮次记录不参与比对）。"""
    if not os.path.exists(path):
        return []
    lines = open(path, encoding='utf-8').read().splitlines()
    last = None
    for i, line in enumerate(lines, 1):
        if re.search(r'(现状|当前|状态[:：])', line):
            last = (i, line)
    if not last:
        return []
    i, line = last
    out = []
    for pat, key in PATTERNS:
        for m in re.finditer(pat, line):
            try:
                v = int(m.group(1).replace(',', ''))
            except ValueError:
                continue
            out.append((i, key, v, line.strip()[:110]))
    return out'''

if old in s:
    s = s.replace(old, new, 1)
    open(p, 'w', encoding='utf-8').write(s)
    print('已改为只核对最新记录')
else:
    print('未匹配')
