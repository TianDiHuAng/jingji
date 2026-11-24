# -*- coding: utf-8 -*-
"""续作IZ：把 R4 的来源校验扩展到嵌套字段（timeline/schools/policy_response/key_data）。"""
P = 'tools/check.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

# 在 check_entry 的结尾（R19 检查之前）加入嵌套来源校验
old = "    # R19 结构化内容字段必须逐条带来源"
new = """    # R4b 嵌套字段的来源 id 也必须存在（timeline/schools/policy_response/key_data）
    for _f, _label in (('timeline', 'timeline'), ('schools', 'schools'),
                       ('policy_response', 'policy_response'), ('key_data', 'key_data')):
        for _i, _it in enumerate(e.get(_f) or []):
            if not isinstance(_it, dict):
                continue
            for _sid in (_it.get('sources') or []):
                if _sid not in sources:
                    err('R4', '%s.%s[%d]' % (os.path.basename(f_path) if 'f_path' in dir() else e.get('id', '?'),
                                             _label, _i),
                        '来源 id "%s" 未在 sources.json 中定义' % _sid)
    # R19 结构化内容字段必须逐条带来源"""

if 'R4b' not in s and old in s:
    s = s.replace(old, new, 1)
    with open(P, 'w', encoding='utf-8', newline='') as f:
        f.write(s)
    print('已加入 R4b 嵌套来源校验')
else:
    print('已存在或未匹配')
