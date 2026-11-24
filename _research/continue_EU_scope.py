# -*- coding: utf-8 -*-
"""续作EU：把新建条目登记到 coverage.json 与 scope.md。"""
import json
import glob
import os

NEW = ['growth', 'recession', 'utility', 'market-failure', 'rent-seeking', 'expectations',
       'effective-demand', 'convergence', 'modigliani-miller', 'equity-premium',
       'counterparty-risk', 'fractional-reserve', 'subordination', 'proprietary-trading',
       'mutual-fund', 'nasdaq', 'eurodollar', 'dividend']

ents = {json.load(open(f, encoding='utf-8'))['id']: json.load(open(f, encoding='utf-8'))
        for f in glob.glob('data/entries/*.json')}

# 1) coverage.json
cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
added = 0
for eid in NEW:
    if eid in have or eid not in ents:
        continue
    e = ents[eid]
    cov['entries'].append({
        'id': eid, 'level': e.get('level', 'L2'), 'tier': e.get('tier', '重要'),
        'status': 'written', 'source_count': len(e.get('sources', [])),
        'needs_verification': 1 if e.get('needs_verification') else 0,
        'last_updated': '2026-11-24',
        'unit': e['unit'], 'period': e['period'], 'region': e['region'],
        'crisis_type': e['crisis_type'],
    })
    added += 1
cov['total'] = len(cov['entries'])
cov['date'] = '2026-11-24'
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage.json 新增:', added, '| total:', cov['total'])

# 2) scope.md：在 U6 表格末尾追加行
p = 'scope.md'
s = open(p, encoding='utf-8').read()
lines = s.split('\n')
# 找到 U6 段的表格结束位置（下一个 '## ' 之前）
start = None
for i, l in enumerate(lines):
    if l.startswith('## U6'):
        start = i
        break
end = len(lines)
if start is not None:
    for j in range(start + 1, len(lines)):
        if lines[j].startswith('## '):
            end = j
            break
rows = []
for eid in NEW:
    if eid not in ents:
        continue
    e = ents[eid]
    if any(eid in l for l in lines[start:end]):
        continue
    rows.append('| %s | %s | %s | %s | %s | %s | %s |' % (
        eid, e['title'], e['period'], e['region'], e['crisis_type'],
        e.get('level', 'L2'), len(e.get('sources', []))))
if rows:
    # 插在 U6 段最后一个非空行之后
    k = end - 1
    while k > start and not lines[k].strip():
        k -= 1
    lines[k + 1:k + 1] = rows
    open(p, 'w', encoding='utf-8').write('\n'.join(lines))
    print('scope.md 追加行:', len(rows))
else:
    print('scope.md 无需追加')
