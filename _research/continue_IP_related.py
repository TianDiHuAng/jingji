# -*- coding: utf-8 -*-
"""续作IP：把 comparison 中提到的条目补入 related，并做同类对称化。

理由：comparison 里写"与 X 的区别/相近"，若 related 中没有 X，读者无法跳转——
这是文案与导航的不一致。补入后同时对称化（同类互链），保持 round 69 的约定。
"""
import glob
import json
import re

es = {}
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    es[d['id']] = d
ids = set(es)


def kind(x):
    return 'C' if x['unit'].startswith('U6') else 'K'


added = 0
for eid, e in es.items():
    comp = e.get('comparison') or ''
    if not comp:
        continue
    mentioned = {i for i in ids if i != eid and i in comp}
    rel = e.setdefault('related', [])
    for m in mentioned:
        if m not in rel:
            rel.append(m)
            added += 1
    if mentioned:
        e['related'] = sorted(set(rel))

print('从 comparison 补入 related:', added)

# 同类对称化（概念↔概念、案例↔案例）
sym = 0
for eid, e in es.items():
    for r in list(e.get('related', [])):
        if r not in es or kind(e) != kind(es[r]):
            continue
        back = es[r].setdefault('related', [])
        if eid not in back:
            back.append(eid)
            sym += 1
print('对称化补入:', sym)

for eid, e in es.items():
    if e.get('related'):
        e['related'] = sorted(set(e['related']))
    json.dump(e, open('data/entries/%s.json' % eid, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)

# 复核
es2 = {json.load(open(f, encoding='utf-8'))['id']: json.load(open(f, encoding='utf-8'))
       for f in glob.glob('data/entries/*.json')}
bad = 0
for eid, e in es2.items():
    comp = e.get('comparison') or ''
    if not comp:
        continue
    mentioned = {i for i in es2 if i != eid and i in comp}
    if mentioned - set(e.get('related', [])):
        bad += 1
print('仍存在文案与导航不一致的条目:', bad)
n = [len(e.get('related', [])) for e in es2.values()]
print('related 平均 %.1f 条、最多 %d 条' % (sum(n) / len(n), max(n)))
