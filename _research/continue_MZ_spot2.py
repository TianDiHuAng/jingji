# -*- coding: utf-8 -*-
"""round 131b-fix：overview 数字 vs 全文，简单子串抽查。"""
import glob
import json
import os
import random
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
FULL = '_research/wiki_full'
NUM = re.compile(r'(\d[\d,]*\.?\d*)')

def variants(num):
    out = set(); s = num.replace(',', '')
    out.add(num); out.add(s)
    try:
        f = float(s)
        if f == int(f):
            out.add(str(int(f))); out.add('{:,}'.format(int(f)))
        else:
            out.add('%.1f' % f); out.add('%.2f' % f); out.add('{:,}'.format(f))
    except ValueError:
        pass
    return out

pool = [e for e in es if os.path.exists(os.path.join(FULL, e['id'] + '.txt'))]
random.seed(131)
sample = random.sample(pool, 12)
total = miss = 0
for e in sample:
    txt = open(os.path.join(FULL, e['id'] + '.txt'), encoding='utf-8').read()
    ov = e.get('overview') or ''
    nums = [m.group(1) for m in NUM.finditer(ov)]
    # 过滤掉 4 位年份
    nums = [n for n in nums if not (n.isdigit() and len(n) == 4 and n.startswith(('1', '2')))]
    misses = []
    for n in nums:
        if not any(v and v in txt for v in variants(n)):
            misses.append(n)
    total += len(nums); miss += len(misses)
    print('%-26s 数字 %2d 个, 未在全文找到 %d 个 %s' % (e['id'], len(nums), len(misses), misses[:5]))
print('\n合计: %d 个数字, 未找到 %d' % (total, miss))
