# -*- coding: utf-8 -*-
"""round 129：结构性数据一致性审计（不依赖网络）。"""
import glob
import json
import re
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]

# 1) timeline 年份是否落在条目 period 的合理范围
RANGE = {
 'U1 早期—17世纪': (-3000, 1699),
 'U2 18—19世纪': (1700, 1899),
 'U3 20世纪上半': (1900, 1949),
 'U4 20世纪下半': (1950, 1999),
 'U5 21世纪': (2000, 2100),
 'U6 理论与制度': (-3000, 2100),
}
bad = []
for e in es:
    lo, hi = RANGE.get(e['unit'], (-3000, 2100))
    for t in e.get('timeline') or []:
        y = t.get('year')
        if isinstance(y, int) and not (lo <= y <= hi):
            bad.append((e['id'], e['unit'], y, (t.get('event') or '')[:30]))
print('=== timeline 年份越出所属时期范围 ===')
print('条数:', len(bad))
for b in bad[:15]:
    print('  %-26s %-14s %5d %s' % b)

# 2) crisis_type 分布
print('\n=== crisis_type 分布 ===')
for k, v in Counter(e['crisis_type'] for e in es).most_common():
    print('  %-8s %d' % (k, v))

# 3) 近重复标题（去掉括号与标点后比较）
def norm(t):
    t = re.sub(r'[（(].*?[）)]', '', t)
    return re.sub(r'[^\w\u4e00-\u9fff]', '', t)
seen = {}
dup = []
for e in es:
    k = norm(e['title'])
    if k in seen:
        dup.append((seen[k], e['id'], e['title']))
    else:
        seen[k] = e['id']
print('\n=== 近重复标题 ===')
print('对数:', len(dup))
for d in dup:
    print('  ', d)

# 4) 有 key_data 但数值为字符串的
print('\n=== key_data value 非数值 ===')
badk = [(e['id'], k.get('label'), k.get('value')) for e in es
        for k in (e.get('key_data') or []) if not isinstance(k.get('value'), (int, float))]
print('条数:', len(badk))
for b in badk[:10]:
    print('  ', b)
