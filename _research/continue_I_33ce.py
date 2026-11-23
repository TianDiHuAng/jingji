# -*- coding: utf-8 -*-
"""续作I：crisis-33ce 升L2（罗马33年金融危机,据REST摘要）。"""
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

f = 'data/entries/crisis-33ce.json'
d = json.load(open(f, encoding='utf-8'))
sid = 'w-en-crisis-33ce'
d['level'] = 'L2'
d['timeline'] = [
    {'year': 33, 'display': '公元33年', 'event': '罗马帝国提比略皇帝在位期间发生金融与经济危机（据 Wikipedia Financial crisis of 33）', 'sources': [sid]},
    {'year': 33, 'display': '公元33年', 'event': '政府政策转向与一系列没收减少了罗马货币供给；旧法被援引致贷款提前召回（同上）', 'sources': [sid]},
    {'year': 33, 'display': '公元33年', 'event': '危机最终以无息贷款形式注入流动性而化解（同上）', 'sources': [sid]},
]
d['causal_chain'] = [
    {'step': '政策转向+没收 → 罗马货币供给减少', 'sources': [sid]},
    {'step': '援引旧法致贷款被提前召回 → 信贷紧缩、房地产价格崩盘', 'sources': [sid]},
    {'step': '以无息贷款注入流动性 → 危机化解', 'sources': [sid]},
]
d['schools'] = [
    {'holder': '货币供给视角', 'view': '货币供给收缩是危机的根源', 'basis': '据维基摘要；待核实', 'sources': [sid]},
    {'holder': '流动性救助视角', 'view': '以无息贷款注入流动性是有效解法', 'basis': '据维基摘要；待核实', 'sources': [sid]},
]
d['policy_response'] = [{'holder': '罗马当局', 'view': '以无息贷款注入流动性化解危机（据维基摘要）', 'basis': '据维基摘要；细节待核实', 'sources': [sid]}]
d['comparison'] = '古代金融危机的著名案例，其"货币收缩→信贷紧缩→资产崩盘→流动性救助"链条与现代危机高度相似。具体异同待核实。'
if not d.get('svg'):
    d['svg'] = svg(d['title'], ['货币收缩', '信贷紧缩', '流动性救助'])
d['needs_verification'] = True
d['pending_notes'] = d.get('pending_notes', '').replace('L1骨架：内容待核实补充。', '') + ' 【续作I】升L2(据REST摘要)。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('crisis-33ce -> L2')

cov = json.load(open('coverage.json', encoding='utf-8'))
for e in cov['entries']:
    if e['id'] == 'crisis-33ce':
        e['level'] = 'L2'
        e['last_updated'] = '2026-11-23'
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage synced')
