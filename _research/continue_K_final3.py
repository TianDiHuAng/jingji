# -*- coding: utf-8 -*-
"""续作K：blue-monday-2009 / dutch-collapse-1780 / dutch-stock-crashes 升L2（据REST摘要）。"""
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

D = {
 'blue-monday-2009': {
  'sid': 'w-en-blue-monday-crash-2009',
  'tl': [
    (2009, '2009年1月19日（周一）', '苏格兰皇家银行(RBS)宣布英国史上最大企业亏损后，英国银行股遭抛售崩跌（据 Wikipedia Blue Monday Crash 2009）'),
    (2009, '2009年1月19日', '银行股单日跌幅超过67%；英国其他银行股亦重挫（同上）'),
    (2009, '2009年1月20日', '劳埃德银行集团与巴克莱再度大跌，RBS与汇丰继续下跌（同上）'),
  ],
  'causal': [
    'RBS宣布英国史上最大企业亏损 → 市场对英国银行业资本状况信心崩塌',
    '英国银行股遭恐慌性抛售，单日跌幅超过67%；其他银行股同步重挫',
    '次日劳埃德、巴克莱续跌，抛压蔓延至整个英国银行板块',
  ],
  'schools': [
    ('信用/资本充足视角', '巨额亏损暴露资本缺口，引发对整个银行板块偿付能力的重估'),
    ('恐慌传染视角', '单家银行公告触发板块性抛售，恐慌跨机构蔓延'),
  ],
  'kd': [
    ('英国银行股单日跌幅(2009-01-19)', -67, '%（单日，跌超67%，取67）', 2009,
     '原文：The shares fell over 67% in a single day；单一来源待核实。'),
  ],
  'cmp': '与大萧条1930年代银行恐慌、2008年雷曼冲击同属银行信心危机；但本次以单家银行公告为触发点、表现为股价崩跌。具体异同待核实。',
 },
 'dutch-collapse-1780': {
  'sid': 'w-en-financial-history-of-the-dutch-republic',
  'tl': [
    (1585, '1585—1620年', '荷兰起义后经济快速发展、储蓄大量积累，产生获利投资需求（据 Wikipedia Financial history of the Dutch Republic）'),
    (1602, '17世纪', '公共债券、承兑信用、保险、VOC股票及其衍生品等现代投资工具发展；阿姆斯特丹证交所与阿姆斯特丹银行居中媒介（同上）'),
    (1700, '17世纪末', '荷兰经济结构性问题使国内投资机会不足，资本大量转向海外主权债、外国股票债券与基建（同上）'),
    (1780, '18世纪末', '系列危机导致荷兰共和国衰亡，其国际资本市场主导地位终结（同上）'),
  ],
  'causal': [
    '经济快速发展与储蓄积累 → 需要可获利的投资渠道，催生现代金融工具与机构',
    '17世纪末国内投资机会枯竭 → 资本大规模转向海外主权债与外国证券',
    '18世纪末系列危机爆发、海外资产受损 → 共和国金融地位崩溃并走向衰亡',
  ],
  'schools': [
    ('金融发展/储蓄中介视角', '储蓄积累与金融创新（债券、股票、衍生品、银行）支撑了荷兰的资本市场主导地位'),
    ('结构性/资本外流视角', '国内投资机会枯竭迫使资本外流，海外风险暴露最终引发18世纪末危机'),
  ],
  'cmp': '与英国1720南海泡沫、法国密西西比泡沫同期但形态不同：荷兰以成熟的多层次资本市场与对外贷款为主，危机源于海外资产质量。具体异同待核实。',
 },
 'dutch-stock-crashes': {
  'sid': 'w-en-financial-history-of-the-dutch-republic',
  'tl': [
    (1602, '1602年起', '荷兰东印度公司(VOC)股票公开交易，为最早的可交易股份之一（据 Wikipedia Financial history of the Dutch Republic）'),
    (1610, '17世纪', '阿姆斯特丹证交所、阿姆斯特丹银行与商人银行家共同媒介投资，衍生品等工具同步发展（同上）'),
    (1680, '17世纪末', '资本市场高度成熟、资本存量巨大并产生自身收益流；国内投资机会随后枯竭（同上）'),
  ],
  'causal': [
    'VOC等公开交易公司出现 → 股票与衍生品市场形成，阿姆斯特丹证交所成为交易中心',
    '资本存量膨胀并产生收益流 → 市场深度与工具复杂度提升',
    '国内投资机会枯竭 → 资本转向海外，市场脆弱性随之转移',
  ],
  'schools': [
    ('金融创新视角', '荷兰创造了股票、衍生品、债券与中央银行等现代金融要素的早期形态'),
    ('市场脆弱性视角', '复杂的交易工具与对外敞口也带来投机与波动风险'),
  ],
  'cmp': '被视为现代证券市场与投机交易的起源之一，早于伦敦与纽约市场；具体异同待核实。',
 },
}

for eid, sp in D.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    sid = sp['sid']
    d['level'] = 'L2'
    have = {t.get('display') for t in d.get('timeline', [])}
    for y, disp, ev in sp['tl']:
        if disp not in have:
            d.setdefault('timeline', []).append({'year': y, 'display': disp, 'event': ev, 'sources': [sid]})
    d['timeline'].sort(key=lambda t: t.get('year', 0))
    d['causal_chain'] = [{'step': st, 'sources': [sid]} for st in sp['causal']]
    d['schools'] = [{'holder': h, 'view': v, 'basis': '据维基摘要归纳；具体表述待核实', 'sources': [sid]}
                    for h, v in sp['schools']]
    hk = {k.get('label') for k in d.get('key_data', [])}
    for kd in sp.get('kd', []):
        if kd[0] not in hk:
            d.setdefault('key_data', []).append({
                'label': kd[0], 'value': kd[1], 'unit': kd[2], 'year': kd[3],
                'comparable_price': False, 'note': kd[4], 'sources': [sid]})
    if not d.get('policy_response'):
        d['policy_response'] = [{'holder': '政策当局', 'view': '应对措施及效果待核实',
                                 'basis': '需多来源印证', 'sources': [sid]}]
    d['comparison'] = sp['cmp']
    if not d.get('svg'):
        d['svg'] = svg(d['title'], [sp['tl'][0][2][:12], '传导', '后果'])
    d['needs_verification'] = True
    d['pending_notes'] = d.get('pending_notes', '').replace('L1骨架：内容待核实补充。', '') + ' 【续作K】升L2(据REST摘要)。'
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '-> L2')

cov = json.load(open('coverage.json', encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in D:
        e['level'] = 'L2'
        e['last_updated'] = '2026-11-23'
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage synced')
