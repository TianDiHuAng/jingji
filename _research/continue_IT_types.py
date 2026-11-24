# -*- coding: utf-8 -*-
"""续作IT：统一 sources.type 的词汇表。

发现的不一致：
  · "官方机构"(18) 与 "权威机构"(4) 同义不同名
  · "统计数据库"(5) 与 "dataset"(1) 中英混用
统一为四类：权威百科／学术著作／官方机构／统计数据库。
"""
import json
from collections import Counter

SP = 'data/sources.json'
sj = json.load(open(SP, encoding='utf-8'))
MAP = {'权威机构': '官方机构', 'dataset': '统计数据库'}
n = 0
for s in sj['sources']:
    t = s.get('type')
    if t in MAP:
        s['type'] = MAP[t]
        n += 1
json.dump(sj, open(SP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('已统一 %d 个来源的 type' % n)
print('统一后分布:', dict(Counter(s.get('type') for s in sj['sources'])))
