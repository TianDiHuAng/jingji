# -*- coding: utf-8 -*-
"""续作GN：为剩余 16 个薄弱条目提取 timeline / schools 候选（含人名与年份）。"""
import json
import os
import re

IDS = ['equity-premium', 'eurodollar', 'expectations', 'fractional-reserve', 'inequality',
       'investment', 'labour-market', 'modigliani-miller', 'mutual-fund', 'nasdaq',
       'payment-system', 'population', 'property-rights', 'proprietary-trading',
       'specialization', 'subordination']

YEAR = re.compile(r'\b(1[5-9]\d\d|20[0-2]\d)\b')
NAME = re.compile(r'\b([A-Z][a-z]{2,15})\s+(?:and\s+)?([A-Z][a-z]{2,15})?\b')
DISPUTE = re.compile(r'(critics?|dispute|controvers|however|by contrast|on the other hand|'
                     r'argued? that|some economists|others argue|alternative view|'
                     r'is debated|remains? unclear)', re.I)

out = {}
for eid in IDS:
    p = '_research/wiki_full/%s.txt' % eid
    if not os.path.exists(p):
        continue
    t = ' '.join(open(p, encoding='utf-8').read().split())
    parts = re.split(r'\n', open(p, encoding='utf-8').read())
    heads = re.findall(r'\n==+\s*(.+?)\s*==+\n', open(p, encoding='utf-8').read())
    sents = re.split(r'(?<=[.!?])\s+', t)
    ys = [s for s in sents if YEAR.search(s) and 60 < len(s) < 280][:3]
    ds = [s for s in sents if DISPUTE.search(s) and 60 < len(s) < 280][:3]
    out[eid] = {'heads': heads[:8], 'years': ys, 'disputes': ds}

json.dump(out, open('_research/thin2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
for eid in IDS[:6]:
    if eid not in out:
        continue
    print('===', eid, '===')
    print('  章节:', ' / '.join(out[eid]['heads'][:6]))
    for s in out[eid]['years'][:1]:
        print('  [Y]', s[:180])
    for s in out[eid]['disputes'][:1]:
        print('  [D]', s[:180])
    print()
