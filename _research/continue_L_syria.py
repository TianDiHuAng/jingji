# -*- coding: utf-8 -*-
"""续作L：syrian-crisis-2011 升L2（据 Economy of Syria + Caesar Act 摘要，内容克制、不夸大）。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

f = 'data/entries/syrian-crisis-2011.json'
d = json.load(open(f, encoding='utf-8'))
S_ECON = 'w-en-economy-of-syria'
S_CAESAR = 'w-en-caesar-act'

d['level'] = 'L2'
d['one_line'] = '2011年3月叙利亚内战爆发后经济持续恶化；2019年《凯撒法案》等外部制裁进一步施压，该法案于2025年12月被废除。'
d['overview'] = (
    '叙利亚经济在早期以农业为主，属于发展中混合经济；2011年3月内战爆发后经济状况恶化（据 Wikipedia Economy of Syria）。'
    '美国《2019年凯撒叙利亚平民保护法》（Caesar Act）以战争罪为由制裁叙利亚政府及相关人员，2019年12月由特朗普总统签署、2020年6月17日生效；'
    '在阿萨德政权倒台一年多后，2026财年国防授权法于2025年12月18日废除了该法案（据 Wikipedia Caesar Syria Civilian Protection Act）。'
    '关于产出、汇率、通胀与经济规模的具体数据待核实补充。'
)
d['timeline'] = [
    {'year': 2011, 'display': '2011年3月', 'event': '叙利亚内战爆发，经济状况随之恶化（据 Wikipedia Economy of Syria）', 'sources': [S_ECON]},
    {'year': 2019, 'display': '2019年12月', 'event': '美国《凯撒叙利亚平民保护法》由特朗普总统签署成为法律（据 Wikipedia Caesar Act）', 'sources': [S_CAESAR]},
    {'year': 2020, 'display': '2020年6月17日', 'event': '《凯撒法案》生效，对叙利亚政府及相关人员实施制裁（同上）', 'sources': [S_CAESAR]},
    {'year': 2025, 'display': '2025年12月18日', 'event': '阿萨德政权倒台一年多后，2026财年国防授权法废除《凯撒法案》（同上）', 'sources': [S_CAESAR]},
]
d['causal_chain'] = [
    {'step': '2011年3月内战爆发 → 生产、贸易与基础设施受损，经济持续恶化', 'sources': [S_ECON]},
    {'step': '外部制裁叠加（《凯撒法案》2020年6月生效）→ 进一步限制对外经济往来', 'sources': [S_CAESAR]},
    {'step': '2025年12月制裁废除 → 外部约束解除，经济恢复程度待观察', 'sources': [S_CAESAR]},
]
d['schools'] = [
    {'holder': '内部冲突视角', 'view': '内战导致的生产与基础设施破坏是经济恶化的主因', 'basis': '据维基Economy of Syria主题归纳；具体量化待核实', 'sources': [S_ECON]},
    {'holder': '外部制裁视角', 'view': '外部制裁叠加冲突，进一步压缩对外经济空间', 'basis': '据维基Caesar Act条目；影响程度待核实', 'sources': [S_CAESAR]},
]
d['policy_response'] = [
    {'holder': '美国（制裁方）', 'view': '以《凯撒法案》制裁叙利亚政府及相关人员，2025年12月废除', 'basis': '据维基Caesar Act条目', 'sources': [S_CAESAR]},
    {'holder': '叙利亚当局', 'view': '应对措施及效果待核实', 'basis': '需多来源印证', 'sources': [S_ECON]},
]
d['comparison'] = (
    '与同期的委内瑞拉危机类似，均为"内部治理/冲突 + 外部制裁"叠加型经济困境；'
    '但叙利亚以战争破坏为主、制裁于2025年底解除，委内瑞拉以石油与政策失灵为主。具体异同待核实。'
)
if not d.get('svg'):
    d['svg'] = svg(d['title'], ['2011内战', '制裁叠加', '2025解除'])
d['sources'] = [S_ECON, S_CAESAR, 'w-en-financial-crisis']
d['needs_verification'] = True
d['pending_notes'] = (
    'L2：时间线（2011内战/2019凯撒法案签署/2020-06-17生效/2025-12-18废除）据维基摘要；'
    '内战破坏的具体程度、GDP/汇率/通胀等数值、制裁的实际经济影响待核实补充。'
    '【续作L】升L2(据REST摘要)。'
)
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('syrian-crisis-2011 -> L2')

cov = json.load(open('coverage.json', encoding='utf-8'))
for e in cov['entries']:
    if e['id'] == 'syrian-crisis-2011':
        e['level'] = 'L2'
        e['last_updated'] = '2026-11-23'
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage synced')
