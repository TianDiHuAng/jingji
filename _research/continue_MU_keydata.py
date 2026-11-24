# -*- coding: utf-8 -*-
"""续作MU：为 5 条核心/重要案例补 key_data（数字均来自来源全文）。"""
import json

ADD = {
 'london-econ-1933': [
   ('参会国数', 66, '国', 1933, '原文：a meeting of representatives of 66 nations',
    'w-en-london-economic-conference'),
 ],
 'panic-1825': [
   ('因危机倒闭的银行数（英国）', 12, '家', 1825, '原文：it led to the closure of twelve banks',
    'w-en-panic-of-1825'),
 ],
 'gold-bloc': [
   ('金集团国家数', 7, '国（以法国为首）', 1933,
    '原文：The gold bloc were seven countries led by France', 'w-en-gold-bloc'),
 ],
 'tripartite-1936': [
   ('协定签署国数', 3, '国（美／法／英）', 1936,
    '原文：entered into by the United States, France, and Great Britain',
    'w-en-tripartite-1936'),
 ],
 'tulip-mania-1637': [
   ('最贵品种 Semper Augustus 顶峰售价', 10000, '荷兰盾', 1637,
    '原文：at its peak sold for ƒ10,000', 'w-en-tulip-mania'),
   ('顶峰球茎价格相当于熟练工匠年收入的倍数（超过）', 10, '倍', 1637,
    '原文：certain tulip bulbs sold for more than 10 times the annual income of a skilled artisan',
    'w-en-tulip-mania'),
 ],
}

# 先确认来源 id 存在；不存在则尝试匹配
import glob
srcs = {s['id']: s for s in json.load(open('data/sources.json', encoding='utf-8'))['sources']}

for eid, rows in ADD.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    have = {k['label'] for k in (d.get('key_data') or [])}
    for label, val, unit, year, note, sid in rows:
        if label in have:
            continue
        if sid not in srcs:
            print('  [警告] 来源不存在:', sid, '（条目', eid, '）')
        d.setdefault('key_data', []).append({
            'label': label, 'value': val, 'unit': unit, 'year': year,
            'comparable_price': False, 'note': note + '；单一来源，待第二来源核实。',
            'sources': [sid],
        })
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作MU】补 key_data（数字据来源全文）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('%-26s key_data += %d' % (eid, len(rows)))
