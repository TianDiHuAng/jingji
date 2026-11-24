# -*- coding: utf-8 -*-
"""round 133c：统计 wiki_full 缓存中"通用页"占比（区别于专属来源）。"""
import glob, json, os

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
FULL = '_research/wiki_full'
GENERIC_HEADS = [
  'a currency crisis is', 'an economic bubble', 'a financial crisis is',
  'a speculative bubble', 'in economics, a recession', 'hyperinflation is',
  'a stock market crash', 'a bank run',
]
mismatch = []
for e in es:
    p = os.path.join(FULL, e['id'] + '.txt')
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8').read()
    head = t[:200].lower().strip()
    for g in GENERIC_HEADS:
        if head.startswith(g):
            mismatch.append((e['id'], g))
            break
print('wiki_full 缓存为"通用页"的条目数:', len(mismatch))
for m in mismatch:
    print('  %-30s <- %s...' % (m[0], m[1]))
