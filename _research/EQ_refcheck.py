# -*- coding: utf-8 -*-
"""检查：从条目文本中提取英文术语引用，找出站内不存在的概念。
用法：python -X utf8 _research/EQ_refcheck.py
"""
import json, glob, re

es = {json.load(open(f, encoding='utf-8'))['id']: json.load(open(f, encoding='utf-8'))
      for f in glob.glob('data/entries/*.json')}
refs = {}
for eid, e in es.items():
    txt = (e.get('comparison') or '') + (e.get('overview') or '')
    for m in re.findall(r'[（(]([a-z][a-z0-9]+(?:-[a-z0-9]+)+)[）)]', txt):
        refs.setdefault(m, set()).add(eid)
    for m in re.findall(r'\*\*([a-z][a-z0-9_]+)\*\*', txt):
        if '-' in m:
            refs.setdefault(m, set()).add(eid)
missing = {k: v for k, v in refs.items() if k not in es}
print('引用总数:', len(refs), '| 站内不存在:', len(missing))
for k, v in sorted(missing.items(), key=lambda x: -len(x[1])):
    print('  %-30s 被 %d 条提及' % (k, len(v)))
