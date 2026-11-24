# -*- coding: utf-8 -*-
"""round 133b：one_line 中出现的年份是否都能在来源全文中找到（更强信号）。"""
import glob, json, os, re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
FULL = '_research/wiki_full'
YEAR = re.compile(r'(?<!\d)(1[5-9]\d{2}|20[0-2]\d)(?!\d)')

flags = []
for e in es:
    if e['unit'].startswith('U6'):
        continue
    p = os.path.join(FULL, e['id'] + '.txt')
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8').read()
    ol = e.get('one_line') or ''
    yrs = set(int(m.group(1)) for m in YEAR.finditer(ol))
    missing = sorted(y for y in yrs if str(y) not in t)
    if missing:
        flags.append((e['id'], missing, ol[:60]))
print('=== one_line 年份不在来源全文 ===')
print('条数:', len(flags))
for f in flags:
    print('  %-28s 缺 %s | %s' % (f[0], f[1], f[2]))
