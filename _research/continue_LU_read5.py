# -*- coding: utf-8 -*-
import re

IDS = ['aig', 'enron', 'drexel', 'worldcom', 'barings-1995']
for eid in IDS:
    t = open('_research/wiki_full/%s.txt' % eid, encoding='utf-8').read()
    print('=' * 70)
    print('### %s（%d 字符）' % (eid, len(t)))
    print('章节:', re.findall(r'\n==+\s*(.+?)\s*==+\n', t)[:8])
    print(' '.join(t[:1700].split()))
    print()
