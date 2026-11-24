# -*- coding: utf-8 -*-
"""续作GS：补上第二批"有源未引"——多为可做跨语言对照的维基来源。"""
import json
import os
import glob

FIX = {
 'panic-1796': ['w-en-panic-of-1796'],
 'panic-1910': ['w-en-panic-of-1910'],
 'greek-hyper-1941': ['w-en-greek-hyper-1941'],
 'bernie-madoff': ['w-en-madoff'],
 'sdr': ['w-en-sdr'],
 'weimar-hyper-1921': ['w-zh-weimar-hyper'],
 'black-monday-1987': ['w-de-schwarzer-montag'],
 'wall-street-1929': ['w-fr-krach-1929'],
 'japan-asset-bubble-1990': ['w-zh-011'],
 'dotcom-bubble-2000': ['w-zh-012'],
 'subprime-crisis-2007': ['w-zh-018'],
 'great-depression': ['w-zh-002'],
 'gold-standard': ['w-zh-008'],
 'hyperinflation': ['w-zh-013'],
 'inflation': ['w-zh-007'],
 'unemployment': ['w-zh-009'],
 'monetary-policy': ['w-zh-010'],
 'financial-crisis': ['w-zh-014'],
 'business-cycle': ['w-zh-017'],
 'fiscal-policy': ['w-zh-019'],
 'dutch-stock-crashes': ['w-en-financial-history-of-the-dutch-republic'],
}

n = 0
for eid, sids in FIX.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    srcs = d.setdefault('sources', [])
    added = []
    for sid in sids:
        if sid not in srcs:
            srcs.append(sid)
            added.append(sid)
    if added:
        d['pending_notes'] = (d.get('pending_notes', '')
                              + ' 【续作GS】补上已注册但未引用的来源 %s。' % '、'.join(added))
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n += 1
        print('%-24s += %s' % (eid, ','.join(added)))

# 复核
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
used = set()
for e in es:
    used.update(e.get('sources', []))
unused = [s['id'] for s in srcs if s['id'] not in used]
print('\n补入 %d 个条目 | 剩余未引用来源 %d 个' % (n, len(unused)))
print('  ', ', '.join(unused[:30]))
