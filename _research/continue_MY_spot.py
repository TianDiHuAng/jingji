# -*- coding: utf-8 -*-
"""round 131b：overview 中带单位的数字 vs 全文本，随机抽查 12 条有全文条目。"""
import glob
import json
import os
import random
import re
import sys

sys.path.insert(0, 'tools')
from check_kd import variants, unit_hints

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
FULL = '_research/wiki_full'
NUM = re.compile(r'(\d[\d,]*\.?\d*)\s*([%％]|亿美元|万亿美元|百万|十亿|亿|万|倍|百分点|美元|英镑|日元|人)?')

pool = []
for e in es:
    p = os.path.join(FULL, e['id'] + '.txt')
    if not os.path.exists(p):
        continue
    pool.append(e)

random.seed(131)
sample = random.sample(pool, 12)
print('抽查 12 条（overview 中带单位/百分号的数字是否能在全文找到）:\n')
bad = 0
for e in sample:
    txt = open(os.path.join(FULL, e['id'] + '.txt'), encoding='utf-8').read()
    ov = e.get('overview') or ''
    checks = []
    for m in NUM.finditer(ov):
        num, unit = m.group(1), m.group(2)
        if not unit:      # 只查带单位的，避免年份
            continue
        vs = variants(num, unit)
        found = any(v and v in txt for v in vs)
        checks.append((num + unit, found))
    fails = [c for c in checks if not c[1]]
    print('%-26s 检查 %d 个带单位数字, 未找到 %d 个 %s'
          % (e['id'], len(checks), len(fails), [f[0] for f in fails][:4]))
    bad += len(fails)
print('\n合计未找到:', bad)
