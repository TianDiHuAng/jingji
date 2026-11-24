# -*- coding: utf-8 -*-
import glob
import json
import re
from collections import Counter

PAT = re.compile(r'[；。]?\s*具体[^。]{0,24}待(核实|补充|查)[。]?\s*$')
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
short = []
for e in es:
    ov = e.get('overview') or ''
    if PAT.search(ov):
        new = PAT.sub('', ov).rstrip()
        if len(new) < 150:
            short.append((e['id'], len(new), e['tier'], e['unit'][:6], e['title']))
print('仍含套话且正文<150字的条目: %d\n' % len(short))
print('按 tier:', dict(Counter(s[2] for s in short)))
print('按 unit:', dict(Counter(s[3] for s in short)))
print()
# 机构类 vs 概念类粗分
ORG = ('银行', '基金', '协会', '开发', '央行', '投资银行', '委员会', '交易所', '(ADB)', '(AfDB)',
       '(IDB)', '(EBRD)', '(AIIB)', '(IAIS)')
org = [s for s in short if any(k in s[4] for k in ORG)]
con = [s for s in short if s not in org]
print('机构/组织类: %d' % len(org))
print('概念/理论类: %d' % len(con))
print()
print('最短的 20 条（概念类）:')
for s in sorted(con, key=lambda x: x[1])[:20]:
    print('  %-30s %3d 字 | %s' % (s[0], s[1], s[4][:26]))
