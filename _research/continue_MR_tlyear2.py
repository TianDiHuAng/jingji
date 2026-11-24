# -*- coding: utf-8 -*-
"""round 129e：严格匹配「XXXX年」形式的年份，与 year 字段比对。"""
import glob
import json
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
YEAR = re.compile(r'(?<!\d)(1[0-9]{3}|20[0-2][0-9])(?!\d)\s*年')

conflicts = []
for e in es:
    for t in e.get('timeline') or []:
        y = t.get('year')
        ev = t.get('event') or ''
        if not isinstance(y, int):
            continue
        found = [int(m.group(1)) for m in YEAR.finditer(ev)]
        if found and all(abs(f - y) > 2 for f in found):
            conflicts.append((e['id'], y, found, ev[:80]))
print('=== 严格「XXXX年」与 year 字段矛盾 ===')
print('条数:', len(conflicts))
for c in conflicts:
    print('  %-26s year=%d 文本=%s | %s' % (c[0], c[1], c[2], c[3]))
