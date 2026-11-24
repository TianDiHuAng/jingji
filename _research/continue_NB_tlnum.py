# -*- coding: utf-8 -*-
"""round 132：timeline 事件中的数字 vs 全文本，找出可能"无来源支撑的数字"。"""
import glob
import json
import os
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
FULL = '_research/wiki_full'
NUM = re.compile(r'(\d[\d,]*\.?\d*)\s*(%|％|亿|万|千|倍|个百分点|pp|美元|英镑|日元|点)')

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

suspects = []
for e in es:
    p = os.path.join(FULL, e['id'] + '.txt')
    if not os.path.exists(p):
        continue
    txt = open(p, encoding='utf-8').read()
    # 也把条目自身 key_data 值纳入"可接受"范围
    own = set()
    for k in e.get('key_data') or []:
        own |= variants(str(k['value']))
    for t in e.get('timeline') or []:
        ev = t.get('event') or ''
        for m in NUM.finditer(ev):
            num, unit = m.group(1), m.group(2)
            vs = variants(num)
            if any(v and (v in txt or v in own) for v in vs):
                continue
            suspects.append((e['id'], t.get('year'), num + unit, ev[:70]))
print('=== timeline 中带单位数字、未在全文/自身key_data找到 ===')
print('条数:', len(suspects))
for s in suspects:
    print('  %-26s %5s  %-8s | %s' % s)
