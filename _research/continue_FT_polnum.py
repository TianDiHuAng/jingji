# -*- coding: utf-8 -*-
"""续作FT：检查 policy_response 中提到的数字能否在来源全文中找到。"""
import glob
import json
import os
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
NUM = re.compile(r'(\d[\d,]*\.?\d*)')

suspect, checked = [], 0
for e in es:
    pr = e.get('policy_response') or []
    if not pr:
        continue
    p = '_research/wiki_full/%s.txt' % e['id']
    if not os.path.exists(p):
        continue
    txt = open(p, encoding='utf-8').read()
    view = ' '.join(r.get('view', '') for r in pr)
    nums = NUM.findall(view)
    bad = []
    for n in nums:
        s = n.replace(',', '')
        cands = {n, s}
        try:
            f = float(s)
            if f == int(f):
                cands.add(str(int(f)))
                cands.add('{:,}'.format(int(f)))
            else:
                cands.add(('%.1f' % f))
        except ValueError:
            pass
        checked += 1
        if not any(c in txt for c in cands):
            bad.append(n)
    if bad:
        suspect.append((e['id'], bad[:6], view[:90]))

print('检查 policy_response 中的数字: %d 个' % checked)
print('存在"数字未在来源全文出现"的条目: %d' % len(suspect))
for eid, bad, v in suspect:
    print('  %-28s 未匹配:%s' % (eid, bad))
    print('      %s' % v)
