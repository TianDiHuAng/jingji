# -*- coding: utf-8 -*-
import re

IDS = ['nixon-shock', 'emergency-banking-act-1933', 'gold-reserve-act-1934',
       'argentina-2018', 'dawes-plan-1924']
for eid in IDS:
    t = open('_research/wiki_full/%s.txt' % eid, encoding='utf-8').read()
    print('=' * 70)
    print('### %s（%d 字符）' % (eid, len(t)))
    print('章节:', re.findall(r'\n==+\s*(.+?)\s*==+\n', t)[:8])
    print(' '.join(t[:2000].split()))
    print()
