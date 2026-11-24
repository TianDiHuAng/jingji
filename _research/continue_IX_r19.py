# -*- coding: utf-8 -*-
"""续作IX：加入 R19——timeline/schools/policy_response 的每条都必须带 sources。"""
P = 'tools/check.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

old = "    # R14 分层顺序"
new = """    # R19 结构化内容字段必须逐条带来源
    for _e in entries:
        _wid = _e.get('id', '?')
        for _f in ('timeline', 'schools', 'policy_response'):
            for _i, _item in enumerate(_e.get(_f) or []):
                if not (_item.get('sources') if isinstance(_item, dict) else None):
                    err('R19', _wid, '%s[%d] 缺 sources' % (_f, _i))
    # R14 分层顺序"""

if 'R19' not in s and old in s:
    s = s.replace(old, new, 1)
    with open(P, 'w', encoding='utf-8', newline='') as f:
        f.write(s)
    print('已加入 R19 检查')
else:
    print('已存在或未匹配')
