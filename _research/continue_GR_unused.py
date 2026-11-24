# -*- coding: utf-8 -*-
"""续作GR：为 11 个条目补上"已存在但未被引用"的来源；为 blue-monday 补数据。

背景：检查发现 65 个来源未被任何条目引用，其中 11 个与现有条目明确对应——
来源库里就有，条目却没引用。最典型的是 w-en-blue-monday-crash-2009：
round 61 我曾判定"维基无专属条目"，实为测试时用了错误的大小写
（正确 Blue_Monday_Crash_2009，我用 Blue_Monday_crash_2009，维基 URL 大小写敏感）。
"""
import json
import os

# 条目 -> 要补的来源
FIX = {
 'blue-monday-2009': 'w-en-blue-monday-crash-2009',
 'steel-crisis-1973': 'w-en-steel-crisis',
 'copper-panic-1789': 'w-en-copper-panic-of-1789',
 'british-credit-1772': 'w-en-british-credit-1772',
 'israel-bank-1983': 'w-en-israel-bank-1983',
 'us-state-defaults-1840s': 'w-en-us-state-defaults-1840s',
 'great-depression': 'w-en-great-depression-in-us',
 'crisis-33ce': 'w-en-crisis-33ce',
 'crisis-1914': 'w-en-financial-crisis-of-1914',
 'venezuela-energy-2010': 'w-en-energy-crisis-in-venezuela',
 'great-recession-russia': 'w-en-great-recession',
}

# blue-monday 的补充数据（取自新抓全文）
KD = {
 'blue-monday-2009': [
   ('RBS 2008财年亏损', 28, '十亿英镑', 2008,
    '原文：News reports on RBS indicated a £28 billion loss for 2008'),
   ('英国政府持股比例（危机后）', 70, '%', 2009,
    '原文：the UK government pledged to increase its stake in the company to 70%'),
   ('英国银行股单日跌幅（以上）', 67, '%', 2009,
    '原文：The shares fell over 67% in a single day'),
 ],
}

n, nk = 0, 0
for eid, sid in FIX.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    srcs = d.setdefault('sources', [])
    if sid not in srcs:
        srcs.append(sid)
        n += 1
        print('补来源 %-26s += %s' % (eid, sid))
    if eid in KD and not d.get('key_data'):
        d['key_data'] = [{
            'label': label, 'value': value, 'unit': unit, 'year': year,
            'comparable_price': False,
            'note': note + '；单一来源待核实。', 'sources': [sid],
        } for label, value, unit, year, note in KD[eid]]
        nk += len(d['key_data'])
        print('  并补 key_data %d 条' % len(d['key_data']))
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作GR】补上已注册但未引用的来源 %s。' % sid)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('\n补入来源 %d 处、key_data %d 条' % (n, nk))

# 复核未引用来源数
import glob
from collections import Counter
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
used = Counter()
for e in es:
    for s in e.get('sources', []):
        used[s] += 1
unused = [s['id'] for s in srcs if used[s['id']] == 0]
print('剩余未被引用来源:', len(unused))
