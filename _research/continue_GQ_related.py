# -*- coding: utf-8 -*-
"""续作GQ：对称化同类关联（概念↔概念、案例↔案例），保留跨类单向。

理由：两个概念互相关联、两个案例互为参照时，读者从任一侧都应能跳转。
跨类关联（案例→概念）保持单向：案例可指向多个概念，概念不必回指所有案例。
"""
import glob
import json
import os

es = {}
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    es[d['id']] = d


def kind(x):
    return 'C' if x['unit'].startswith('U6') else 'K'   # C=概念 K=案例


added = 0
for eid, e in es.items():
    for r in list(e.get('related', [])):
        if r not in es:
            continue
        if kind(e) != kind(es[r]):
            continue                       # 跨类保持单向
        back = es[r].setdefault('related', [])
        if eid not in back:
            back.append(eid)
            added += 1

for eid, e in es.items():
    if e.get('related'):
        e['related'] = sorted(set(e['related']))
    json.dump(e, open('data/entries/%s.json' % eid, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)

print('补入反向关联: %d 条' % added)

# 复核
es2 = {json.load(open(f, encoding='utf-8'))['id']: json.load(open(f, encoding='utf-8'))
       for f in glob.glob('data/entries/*.json')}
oneway = [(a, r) for a, e in es2.items() for r in e.get('related', [])
          if r in es2 and a not in es2[r].get('related', [])]
both = sum(1 for a, e in es2.items() for r in e.get('related', [])
           if r in es2 and a in es2[r].get('related', [])) // 2
print('对称化后：双向 %d 对 | 单向 %d 条' % (both, len(oneway)))
from collections import Counter


def k2(x):
    return '概念' if x['unit'].startswith('U6') else '案例'


print('剩余单向类型:', dict(Counter((k2(es2[a]), k2(es2[r])) for a, r in oneway)))
