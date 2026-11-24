# -*- coding: utf-8 -*-
"""round 135：核验"两源差异并列"区块——每条须在同一指标上并列两个不同数值。"""
import glob, json, sys
sys.path.insert(0, 'tools')
from kdclass import classify

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
discrep = []
for e in es:
    for k in e.get('key_data') or []:
        if classify(k) == 'discrepant':
            discrep.append((e['id'], k))
print('两源差异并列 条数:', len(discrep))
# 按 entry 分组，检查是否同一 label（同指标）出现两个不同 value
from collections import defaultdict
by_e = defaultdict(list)
for eid, k in discrep:
    by_e[eid].append(k)
for eid, rows in by_e.items():
    print('\n===', eid)
    for k in rows:
        print('   %-34s = %-10s %-6s | %s' % (k['label'][:32], k['value'], k['unit'][:5], (k.get('note') or '')[:50]))
