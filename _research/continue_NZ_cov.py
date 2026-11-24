# -*- coding: utf-8 -*-
"""round 142：coverage.json 与 data/entries 的一致性。"""
import glob, json

es = {json.load(open(f, encoding='utf-8'))['id']: json.load(open(f, encoding='utf-8'))
      for f in glob.glob('data/entries/*.json')}
cov = json.load(open('coverage.json', encoding='utf-8'))
ce = {c['id']: c for c in cov['entries']}
print('data entries:', len(es), '| coverage entries:', len(ce), '| coverage.total:', cov.get('total'))
print('仅在 entries 不在 coverage:', sorted(set(es) - set(ce))[:10])
print('仅在 coverage 不在 entries:', sorted(set(ce) - set(es))[:10])
# 字段一致性
mismatch = []
for i in set(es) & set(ce):
    e, c = es[i], ce[i]
    for f in ('level', 'tier', 'unit', 'region', 'crisis_type'):
        if f in c and c.get(f) != e.get(f):
            mismatch.append((i, f, c.get(f), e.get(f)))
print('字段不一致:', len(mismatch), mismatch[:8])
