# -*- coding: utf-8 -*-
import glob
import json
import re


def enr(s):
    zh = len(re.findall(r'[\u4e00-\u9fff]', s or ''))
    en = len(re.findall(r'[A-Za-z]', s or ''))
    return en / (zh + en) if (zh + en) else 0


es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]

print('=== one_line 英文占比 >45% ===')
bad = [(e['id'], round(enr(e.get('one_line')) * 100), e.get('one_line')) for e in es
       if enr(e.get('one_line')) > 0.45]
for b in sorted(bad, key=lambda x: -x[1]):
    print('  %-26s %d%% | %s' % (b[0], b[1], (b[2] or '')[:70]))
print('合计:', len(bad))

print('\n=== overview 末尾「待核实」类套话 ===')
PAT = re.compile(r'(具体[^。]{0,20}待核实|具体[^。]{0,20}待补充|具体[^。]{0,20}待查)')
hits = [(e['id'], PAT.findall(e.get('overview') or '')) for e in es
        if PAT.search(e.get('overview') or '')]
print('含该套话的条目:', len(hits))
for h in hits[:10]:
    print('  %-28s %s' % (h[0], h[1][:2]))

print('\n=== overview 含「摘要归纳」标记 ===')
h2 = [e['id'] for e in es if '摘要归纳' in (e.get('overview') or '')]
print('剩余:', len(h2), h2[:8])
