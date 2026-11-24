# -*- coding: utf-8 -*-
"""续作OA：同步 coverage.json 的字段（level/tier/unit/region/crisis_type）与 entries 一致。"""
import glob
import json

es = {json.load(open(f, encoding='utf-8'))['id']: json.load(open(f, encoding='utf-8'))
      for f in glob.glob('data/entries/*.json')}
cov = json.load(open('coverage.json', encoding='utf-8'))
n = 0
for c in cov['entries']:
    e = es.get(c['id'])
    if not e:
        continue
    for f in ('level', 'tier', 'unit', 'region', 'crisis_type'):
        if f in c and c.get(f) != e.get(f):
            c[f] = e.get(f)
            n += 1
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('同步字段数:', n)
# 复核
mis = 0
for c in cov['entries']:
    e = es.get(c['id'])
    if e:
        for f in ('level', 'tier', 'unit', 'region', 'crisis_type'):
            if f in c and c.get(f) != e.get(f):
                mis += 1
print('剩余不一致:', mis)
