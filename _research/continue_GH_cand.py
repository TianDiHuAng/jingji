# -*- coding: utf-8 -*-
"""续作GH：从薄弱条目的全文中提取 timeline 与 schools 候选。"""
import glob
import json
import os
import re

es = {}
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    es[d['id']] = d

YEARS = re.compile(r'\b(1[6-9]\d\d|20[0-2]\d)\b')
SCHOOL = re.compile(r'(critics?|argued?|argues?|some economists|others?|school|'
                    r'dispute|controvers|however|by contrast|alternative)', re.I)

out = {}
for e in es.values():
    if e.get('timeline') or e.get('schools'):
        continue
    p = '_research/wiki_full/%s.txt' % e['id']
    if not os.path.exists(p):
        continue
    t = ' '.join(open(p, encoding='utf-8').read().split())
    sents = re.split(r'(?<=[.!?])\s+', t)
    ys, ss = [], []
    for s in sents:
        if 60 < len(s) < 300:
            if YEARS.search(s) and len(ys) < 4:
                ys.append(s)
            if SCHOOL.search(s) and len(ss) < 3:
                ss.append(s)
    out[e['id']] = {'years': ys, 'schools': ss}

json.dump(out, open('_research/thin_cand.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('有候选的条目:', len(out))
for eid in list(out)[:6]:
    print('===', eid, '===')
    for s in out[eid]['years'][:2]:
        print('  [Y]', s[:170])
    for s in out[eid]['schools'][:1]:
        print('  [S]', s[:170])
