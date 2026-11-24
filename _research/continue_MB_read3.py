# -*- coding: utf-8 -*-
import re

IDS = ['brazil-2014', 'bernie-madoff', 'nigeria-debt']
for eid in IDS:
    t = open('_research/wiki_full/%s.txt' % eid, encoding='utf-8').read()
    print('=' * 70)
    print('### %s（%d 字符）' % (eid, len(t)))
    print('章节:', re.findall(r'\n==+\s*(.+?)\s*==+\n', t)[:9])
    print(' '.join(t[:1900].split()))
    print()
