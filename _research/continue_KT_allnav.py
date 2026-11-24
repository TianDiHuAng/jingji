# -*- coding: utf-8 -*-
"""续作KT：复用 round 94 的扫描逻辑，批量修复所有"见 xxx"未接线。"""
import glob
import json
import re

PAT = re.compile(r'见\s*[（(]?\s*([a-z][a-z0-9\-]{3,})')
es = {}
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    es[d['id']] = d
ids = set(es)


def kind(x):
    return 'C' if x['unit'].startswith('U6') else 'K'


added = 0
for eid, e in es.items():
    refs = set()
    for fld in ('overview', 'comparison', 'one_line'):
        for m in PAT.finditer(e.get(fld) or ''):
            if m.group(1) in ids and m.group(1) != eid:
                refs.add(m.group(1))
    for t in e.get('timeline') or []:
        for m in PAT.finditer(t.get('event') or ''):
            if m.group(1) in ids and m.group(1) != eid:
                refs.add(m.group(1))
    if refs:
        rel = e.setdefault('related', [])
        for r in refs:
            if r not in rel:
                rel.append(r)
                added += 1
        e['related'] = sorted(set(rel))
print('补入 related:', added)

# 对称化
sym = 0
for eid, e in es.items():
    for r in list(e.get('related', [])):
        if r not in es or kind(e) != kind(es[r]):
            continue
        back = es[r].setdefault('related', [])
        if eid not in back:
            back.append(eid)
            sym += 1
print('对称化:', sym)

for eid, e in es.items():
    if e.get('related'):
        e['related'] = sorted(set(e['related']))
    json.dump(e, open('data/entries/%s.json' % eid, 'w', encoding='utf-8'),
              ensure_ascii=False, indent=2)
print('写入完成')
