# -*- coding: utf-8 -*-
"""续作FZ：芬兰条目——标注无源失业率，补充 GNP 成本数据。"""
import json

p = 'data/entries/finnish-banking-1990.json'
d = json.load(open(p, encoding='utf-8'))

old = '资产价格崩跌、失业率从近零升至近20%，储蓄银行体系陷入危机，政府不得不进行大规模注资与重组（含银行支持基金）。'
new = ('资产价格崩跌、失业率大幅上升（具体峰值待核实：现行来源页面未载"近零升至近20%"这一表述，需补充出处），'
       '储蓄银行体系陷入危机，政府不得不进行大规模注资与重组（含银行支持基金）。')
if old in d['overview']:
    d['overview'] = d['overview'].replace(old, new)
    print('overview 已标注失业率待核实')

if not d.get('key_data'):
    d['key_data'] = [{
        'label': '危机纳税人成本（占芬兰GNP）',
        'value': 8, 'unit': '%（占GNP）', 'year': 1993,
        'comparable_price': False,
        'note': '原文：Its total taxpayer cost was roughly 8% of the Finnish GNP, '
                'making it the most severe of the contemporary Nordic banking crises；单一来源待核实。',
        'sources': ['w-en-finnish-banking-1990'],
    }]
    print('已补 key_data：纳税人成本占GNP 8%')

d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作FZ】overview 中无来源支撑的失业率数值已改为待核实；补充 GNP 成本数据。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('完成')
