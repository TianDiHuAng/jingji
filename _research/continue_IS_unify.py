# -*- coding: utf-8 -*-
"""续作IS：统一 schools 的来源字段为 sources（列表），消除 src/sources 并存。

理由：key_data 与 policy_response 均用 sources 列表；schools 中有 27 条用单值 src、
1222 条用 sources 列表，两种形式并存增加渲染与检查的复杂度。
"""
import glob
import json

n = 0
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    ch = False
    for sc in d.get('schools', []) or []:
        if sc.get('src'):
            s = sc.pop('src')
            cur = sc.get('sources') or []
            if s not in cur:
                cur.append(s)
            sc['sources'] = cur
            ch = True
            n += 1
    if ch:
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('已把 %d 处 schools.src 改为 schools.sources' % n)

# 复核
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
left = sum(1 for e in es for sc in (e.get('schools') or []) if sc.get('src'))
print('仍含 src 字段的 schools:', left)

# 检查 gen_site.py 是否还引用 sc["src"]
P = 'tools/gen_site.py'
s = open(P, 'r', encoding='utf-8', newline='').read()
if "sc.get('src')" in s or 'sc["src"]' in s:
    print('注意：gen_site.py 仍引用 schools.src，需同步修改')
else:
    print('gen_site.py 未引用 schools.src')
