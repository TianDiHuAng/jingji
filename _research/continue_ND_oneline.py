# -*- coding: utf-8 -*-
"""round 133：案例 one_line 中的日期/数字 vs 来源全文，找出"简介与来源不符"的线索。"""
import glob
import json
import os
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
FULL = '_research/wiki_full'

def variants(num):
    out = set(); s = num.replace(',', '')
    out.add(num); out.add(s)
    try:
        f = float(s)
        if f == int(f):
            out.add(str(int(f))); out.add('{:,}'.format(int(f)))
        else:
            out.add('%.1f' % f); out.add('%.2f' % f)
    except ValueError:
        pass
    return out

MON = {'1月': ['january'], '2月': ['february'], '3月': ['march'], '4月': ['april'],
       '5月': ['may'], '6月': ['june'], '7月': ['july'], '8月': ['august'],
       '9月': ['september'], '10月': ['october'], '11月': ['november'], '12月': ['december']}

DATE = re.compile(r'(\d{4})年(\d{1,2})月(\d{1,2})?日?')
NUM = re.compile(r'(\d[\d,]*\.?\d*)\s*(亿|万|%|％|倍|点|美元|英镑)')

flags = []
for e in es:
    if e['unit'].startswith('U6'):
        continue
    p = os.path.join(FULL, e['id'] + '.txt')
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8').read()
    tl = t.lower()
    ol = e.get('one_line') or ''
    # 1) 明确日期 年X月
    for m in DATE.finditer(ol):
        y, mo, d = m.group(1), int(m.group(2)), m.group(3)
        mon = MON.get('%d月' % mo, [])
        # 年份在文中？月份（英）在文中？
        y_ok = y in t
        m_ok = any(mm in tl for mm in mon) if mon else False
        if not (y_ok and m_ok):
            flags.append((e['id'], 'ONE_LINE 日期', m.group(0), 'year_in=%s month_in=%s' % (y_ok, m_ok)))
    # 2) 带单位数字（粗查）
    for m in NUM.finditer(ol):
        num = m.group(1)
        if not any(v and v in t for v in variants(num)) and not any(v and '{:,}'.format(int(float(num.replace(',', '')))) in t for v in ['x']):
            flags.append((e['id'], 'ONE_LINE 数字', m.group(0), ''))

print('=== one_line 日期/数字 疑似不在来源全文 ===')
print('条数:', len(flags))
for f in flags:
    print('  %-26s %-14s %-12s %s' % f)
