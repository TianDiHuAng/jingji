# -*- coding: utf-8 -*-
"""续作IR：修复"见 xxx"式引用未接入 related，并扩展检查规则到正文引用。"""
import glob
import json
import re

es = {}
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    es[d['id']] = d
ids = set(es)
PAT = re.compile(r'见\s*[（(]?\s*([a-z][a-z0-9\-]{3,})')


def kind(x):
    return 'C' if x['unit'].startswith('U6') else 'K'


added = 0
for eid, e in es.items():
    refs = set()
    for field in ('overview', 'comparison', 'one_line'):
        txt = e.get(field) or ''
        for m in PAT.finditer(txt):
            if m.group(1) in ids and m.group(1) != eid:
                refs.add(m.group(1))
    for t in e.get('timeline', []) or []:
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

print('从"见 xxx"补入 related:', added)

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
    rel = set(e.get('related', []))
    for field in ('overview', 'comparison', 'one_line'):
        for m in PAT.finditer(e.get(field) or ''):
            if m.group(1) in es2 and m.group(1) != eid and m.group(1) not in rel:
                bad += 1
print('仍缺接线的"见 xxx"引用:', bad)
