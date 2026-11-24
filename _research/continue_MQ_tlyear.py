# -*- coding: utf-8 -*-
"""round 129d：timeline 的 year 字段 vs event 文本中出现的年份是否矛盾。"""
import glob
import json
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
YEAR = re.compile(r'(?<!\d)(1[0-9]{3}|20[0-2][0-9]|3[0-9]{2})(?!\d)')

conflicts = []
for e in es:
    for i, t in enumerate(e.get('timeline') or []):
        y = t.get('year')
        ev = t.get('event') or ''
        if not isinstance(y, int):
            continue
        found = [int(m.group(1)) for m in YEAR.finditer(ev)]
        # 若事件文本明确出现了年份，且没有任何一个与 year 相差 <=2，则疑似矛盾
        if found and all(abs(f - y) > 2 for f in found):
            conflicts.append((e['id'], y, found, ev[:60]))
print('=== timeline year 与事件文本年份疑似矛盾 ===')
print('条数:', len(conflicts))
for c in conflicts:
    print('  %-24s year=%d 文本年份=%s | %s' % (c[0], c[1], c[2], c[3]))

# 另：key_data 的 year 与 label 中数字的粗检（只提示）
print('\n=== key_data year 超出 1000-2100 或为 0 ===')
bad = [(e['id'], k.get('label'), k.get('year')) for e in es for k in (e.get('key_data') or [])
       if isinstance(k.get('year'), int) and (k['year'] != 0 and not (1000 <= k['year'] <= 2100))]
print('条数:', len(bad), bad[:10])
