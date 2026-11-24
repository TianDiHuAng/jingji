# -*- coding: utf-8 -*-
import re

IDS = ['turkey-2001', 'bond-crisis-1994', 'edict-maximum-prices',
       'norwegian-banking-1988', 'tripartite-1936', 'gold-bloc']
for eid in IDS:
    t = open('_research/wiki_full/%s.txt' % eid, encoding='utf-8').read()
    print('=' * 70)
    print('### %s（%d 字符）' % (eid, len(t)))
    print('章节:', re.findall(r'\n==+\s*(.+?)\s*==+\n', t)[:8])
    print('--- 正文 ---')
    print(' '.join(t[:2200].split()))
    print()
