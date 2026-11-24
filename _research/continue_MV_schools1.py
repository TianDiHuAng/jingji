# -*- coding: utf-8 -*-
"""round 130：审计 schools 只有 1 条的条目（未构成两派对照）。"""
import glob
import json
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cnt = Counter(len(e.get('schools') or []) for e in es)
print('schools 条数分布:', dict(sorted(cnt.items())))
one = [e for e in es if len(e.get('schools') or []) == 1]
print('\n只有 1 条 schools 的条目: %d' % len(one))
for e in one:
    s = e['schools'][0]
    print('  %-30s %-4s | holder=%s' % (e['id'], e['tier'], (s.get('holder') or '')[:16]))
