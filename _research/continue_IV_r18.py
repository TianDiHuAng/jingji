# -*- coding: utf-8 -*-
"""续作IV：加入 R18（link_ok 不得为空）。"""
P = 'tools/check.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

old = "    # R14 分层顺序"
new = """    # R18 来源 link_ok 不得为空
    for _s in (src_data or {}).get('sources', []):
        if _s.get('link_ok') is None:
            err('R18', _s.get('id', '?'), 'link_ok 未设置（须为 true/false）')
    # R14 分层顺序"""

if 'R18' not in s and old in s:
    s = s.replace(old, new, 1)
    with open(P, 'w', encoding='utf-8', newline='') as f:
        f.write(s)
    print('已加入 R18 检查')
else:
    print('已存在或未匹配')
