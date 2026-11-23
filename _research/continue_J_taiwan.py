# -*- coding: utf-8 -*-
"""续作J：taiwan-bubble 升L2（中文维基摘要,含精确股价与地价数据）。"""
import json
def svg(t, labels):
    e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

f = 'data/entries/taiwan-bubble.json'
d = json.load(open(f, encoding='utf-8'))
sid = 'w-zh-taiwan-bubble'
d['level'] = 'L2'
d['timeline'] = [
    {'year': 1985, 'display': '1985年7月30日', 'event': '台湾股价指数处于636点（据中文维基《台灣泡沫經濟》）', 'sources': [sid]},
    {'year': 1990, 'display': '1990年2月12日', 'event': '股价指数涨至12682点历史高点（同上）', 'sources': [sid]},
    {'year': 1990, 'display': '1990年10月12日', 'event': '股价指数暴跌至2485点（同上）', 'sources': [sid]},
    {'year': 1990, 'display': '1987—1990年', 'event': '政府公告地价逐年上涨：1987年9.74%、1988年11.54%、1989年47.31%、1990年103.05%，之后转跌（同上）', 'sources': [sid]},
]
d['causal_chain'] = [
    {'step': '1980年代末资金充裕与投机气氛 → 股价与房地产价格快速上涨', 'sources': [sid]},
    {'step': '股价自636点(1985)飙升至12682点(1990.2)、公告地价1990年涨103.05%', 'sources': [sid]},
    {'step': '泡沫破裂 → 股价跌至2485点(1990.10)、地价转跌', 'sources': [sid]},
]
d['schools'] = [
    {'holder': '资产泡沫视角', 'view': '股价与地价大幅脱离基本面后崩跌', 'basis': '据中文维基摘要；待核实', 'sources': [sid]},
    {'holder': '政策/资金视角', 'view': '资金宽松与投机推动资产价格，政策与外部环境变化触发反转', 'basis': '具体政策待核实', 'sources': ['w-en-japanese-asset-price-bubble']},
]
d['key_data'] = [
    {'label': '台湾股价指数(1985-07-30)', 'value': 636, 'unit': '点（台湾加权股价指数）', 'year': 1985, 'comparable_price': False,
     'note': '原文：台灣股價从1985年7月30日的636点；单一来源（中文维基）待核实。', 'sources': [sid]},
    {'label': '台湾股价指数峰值(1990-02-12)', 'value': 12682, 'unit': '点（台湾加权股价指数）', 'year': 1990, 'comparable_price': False,
     'note': '原文：1990年時股價於2月12日漲到12682点；单一来源待核实。', 'sources': [sid]},
    {'label': '台湾股价指数低点(1990-10-12)', 'value': 2485, 'unit': '点（台湾加权股价指数）', 'year': 1990, 'comparable_price': False,
     'note': '原文：到1990年10月12日，跌到2485点；单一来源待核实。', 'sources': [sid]},
    {'label': '公告地价涨幅(1990)', 'value': 103.05, 'unit': '%（台湾公告地价，1990年）', 'year': 1990, 'comparable_price': False,
     'note': '原文：到1990年更上涨103.05%；单一来源待核实。', 'sources': [sid]},
]
d['policy_response'] = [{'holder': '台湾当局', 'view': '应对措施及效果待核实', 'basis': '需多来源印证', 'sources': [sid]}]
d['comparison'] = '与日本资产价格泡沫(1990)同期且机制相似（股价与地产齐涨后崩跌）；具体异同待核实。'
if not d.get('svg'):
    d['svg'] = svg(d['title'], ['资金+投机', '股价地价齐涨', '崩跌'])
d['needs_verification'] = True
d['pending_notes'] = d.get('pending_notes', '').replace('L1骨架：内容待核实补充。', '') + ' 【续作J】升L2(据中文维基摘要,含精确股价/地价数据)。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('taiwan-bubble -> L2')

cov = json.load(open('coverage.json', encoding='utf-8'))
for e in cov['entries']:
    if e['id'] == 'taiwan-bubble':
        e['level'] = 'L2'
        e['last_updated'] = '2026-11-23'
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage synced')
