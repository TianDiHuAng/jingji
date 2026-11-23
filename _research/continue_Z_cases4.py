# -*- coding: utf-8 -*-
"""续作Z：新增4条(埃及2023-24/巴西2014-16/债务陷阱外交/全球债务)。"""
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

CASES = [
 ('egypt-2023', '埃及金融危机(2023–2024)', '货币', 'U5 21世纪', '21世纪', '中东', '重要',
  '2023年起埃及遭遇经济危机，政府与埃及央行被迫贬值埃镑，主因外汇持续短缺。',
  '2023—2024年埃及金融危机是自2023年起冲击埃及的经济危机，导致埃及政府与埃及中央银行贬值埃及镑。危机的重要背景是持续的外汇短缺。埃及长期依赖外部融资与进口，外汇紧张使汇率与偿付承压。具体汇率、通胀与外债数据待核实。',
  [{'year': 2023, 'display': '2023年起', 'event': '埃及遭遇经济危机，政府与央行贬值埃及镑（据 Wikipedia 2023–2024 Egyptian financial crisis）', 'sources': ['w-en-egypt-2023']},
   {'year': 2023, 'display': '持续过程', 'event': '外汇持续短缺是危机的核心背景（同上）', 'sources': ['w-en-egypt-2023']}],
  [{'step': '外部融资紧张 + 外汇持续短缺 → 汇率承压', 'sources': ['w-en-egypt-2023']},
   {'step': '央行与政府被迫贬值埃镑', 'sources': ['w-en-egypt-2023']},
   {'step': '贬值推高进口成本与通胀 → 居民购买力受损', 'sources': ['w-en-currency-crisis']}],
  [{'holder': '外部融资视角', 'view': '外汇短缺与外部融资紧张是核心约束', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-egypt-2023']},
   {'holder': '货币危机视角', 'view': '固定或管理浮动汇率在外汇枯竭时被迫调整', 'basis': '待核实', 'sources': ['w-en-currency-crisis']}],
  '与2016年埃及（此前贬值）、阿根廷2018、土耳其2021共享"外汇短缺→被迫贬值→通胀上升"机制。具体异同待核实。'),
 ('brazil-2014', '巴西经济危机(2014–2016)', '其他', 'U5 21世纪', '21世纪', '美洲', '重要',
  '2014年中至2016年末巴西经历严重经济危机：GDP在2015年下降3.5%、2016年下降3.3%。',
  '从2014年中至2016年末，巴西经历了严重的经济危机。该国国内生产总值（GDP）在2015年下降3.5%，2016年下降3.3%，此后开始小幅经济复苏，该复苏持续至2020年。这是巴西历史上最深的衰退之一，兼具周期性下滑与结构性、政治因素。具体成因待核实。',
  [{'year': 2014, 'display': '2014年中', 'event': '巴西经济危机开始（据 Wikipedia 2014 Brazilian economic crisis）', 'sources': ['w-en-brazil-2014']},
   {'year': 2015, 'display': '2015年', 'event': '巴西 GDP 下降 3.5%（同上）', 'sources': ['w-en-brazil-2014']},
   {'year': 2016, 'display': '2016年', 'event': '巴西 GDP 再下降 3.3%，此后开始小幅复苏（同上）', 'sources': ['w-en-brazil-2014']}],
  [{'step': '大宗商品价格下行 + 国内政策与政治不确定性 → 投资与消费收缩', 'sources': ['w-en-brazil-2014']},
   {'step': 'GDP 连续两年大幅负增长（-3.5%、-3.3%）', 'sources': ['w-en-brazil-2014']},
   {'step': '2017年起小幅复苏，持续至2020年疫情前', 'sources': ['w-en-brazil-2014']}],
  [{'holder': '大宗商品/外部视角', 'view': '商品周期下行冲击资源出口型经济', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-brazil-2014']},
   {'holder': '政策/政治视角', 'view': '国内政策失误与政治危机加剧衰退', 'basis': '待核实', 'sources': ['w-en-fiscal-policy']}],
  '与其他新兴市场衰退相比，巴西本轮以国内因素与商品周期叠加为主，而非货币或银行危机。具体异同待核实。'),
]

CONCEPTS = [
 ('debt-trap-diplomacy', '债务陷阱外交', '债务', 'U6 理论与制度', '理论制度', '全球', '补充',
  '债权国或机构向借款国提供债务，部分或完全是为了增加贷款方的政治影响力。',
  '债务陷阱外交是一种国际金融关系：债权国或机构向借款国提供债务，部分或全部目的是增加贷款方的政治杠杆。据说债权国借此扩大影响力，但这一概念在学界与政策界存在较大争议，具体案例的认定亦无共识。具体论述待核实。',
  [{'year': 2017, 'display': '概念提出', 'event': '债务陷阱外交作为分析概念被用于讨论债权国的政治杠杆（据 Wikipedia Debt-trap diplomacy；具体提出时间待核实）', 'sources': ['w-en-debt-trap-diplomacy']}],
  [{'step': '债权国向借款国提供大额贷款 → 债务依存上升', 'sources': ['w-en-debt-trap-diplomacy']},
   {'step': '借款国偿付困难 → 债权国获得谈判筹码', 'sources': ['w-en-debt-trap-diplomacy']},
   {'step': '以资产或政策让步换取重组 → 政治杠杆兑现（争议概念）', 'sources': ['w-en-sovereign-default']}],
  [{'holder': '地缘政治视角', 'view': '债务可作为施加政治影响的工具', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-debt-trap-diplomacy']},
   {'holder': '批判视角', 'view': '经验证据薄弱，借款国多为主动借款', 'basis': '待核实', 'sources': ['w-en-debt-crisis']}],
  '与巴黎俱乐部式的协调重组（paris-club）形成对照：前者强调集体协商，后者被指双边杠杆。具体异同待核实。'),
 ('global-debt', '全球债务', '债务', 'U6 理论与制度', '理论制度', '全球', '补充',
  '全球范围内所有部门（政府、企业与家庭）所欠货币的总量。',
  '全球债务指全球范围内所有部门——包括政府、企业与家庭——所欠货币的总量。它是观察全球杠杆水平与金融脆弱性的总量指标，其构成（公共与私人、国内与跨境）对风险评估至关重要。具体规模数据待核实。',
  [{'year': 2020, 'display': '持续累积', 'event': '政府、企业与家庭部门债务在全球范围内持续累积（据 Wikipedia Global debt）', 'sources': ['w-en-global-debt']}],
  [{'step': '各部门借贷扩张 → 全球债务总量上升', 'sources': ['w-en-global-debt']},
   {'step': '利率上升或收入下降 → 偿付负担加重', 'sources': ['w-en-debt-crisis']},
   {'step': '集中去杠杆 → 需求收缩与金融压力', 'sources': ['w-en-deleveraging']}],
  [{'holder': '杠杆累积视角', 'view': '债务总量上升提高金融脆弱性', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-global-debt']},
   {'holder': '结构视角', 'view': '需区分公共/私人、本币/外币结构', 'basis': '待核实', 'sources': ['w-en-government-debt']}],
  '与单一国家的债务问题相比，全球债务视角关注跨境联动与总杠杆水平。具体异同待核实。'),
]

for eid, title, cat, unit, period, region, tier, ol, ov, tl, causal, schools, comp in CASES + CONCEPTS:
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': tier,
        'unit': unit, 'period': period, 'region': region, 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': tl,
        'causal_chain': causal,
        'key_data': [],
        'schools': schools,
        'policy_response': [{'holder': '政策当局', 'view': '应对措施及效果待核实', 'basis': '需多来源印证', 'sources': [causal[0]['sources'][0]]}],
        'comparison': comp,
        'svg': svg(title, [tl[0]['event'][:12], '传导', '后果']),
        'sources': list(dict.fromkeys([s for c in causal for s in c['sources']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值与影响程度待核实补充。【续作Z】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

# 巴西 GDP 数值补入（单一来源，标待核实）
f = 'data/entries/brazil-2014.json'
d = json.load(open(f, encoding='utf-8'))
d['key_data'] = [
    {'label': '巴西GDP增速(2015)', 'value': -3.5, 'unit': '%（巴西，2015年）', 'year': 2015,
     'comparable_price': False,
     'note': '原文：GDP fell by 3.5% in 2015；单一来源待核实。', 'sources': ['w-en-brazil-2014']},
    {'label': '巴西GDP增速(2016)', 'value': -3.3, 'unit': '%（巴西，2016年）', 'year': 2016,
     'comparable_price': False,
     'note': '原文：and 3.3% in 2016；单一来源待核实。', 'sources': ['w-en-brazil-2014']},
]
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('brazil-2014 补 key_data')

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r44_cases.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid == 'list-sovereign-debt-crises':
        continue
    sid = 'w-en-' + eid
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科', 'url': 'https://en.wikipedia.org/wiki/' + v['slug'], 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'Wikipedia REST API核对(本会话抓取摘要)'
    })
    ex.add(sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for eid, title, cat, unit, period, region, tier, ol, ov, tl, causal, schools, comp in CASES + CONCEPTS:
    if eid in have:
        continue
    cov['entries'].append({
        'id': eid, 'level': 'L2', 'tier': tier, 'status': 'written',
        'source_count': 2, 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': unit, 'period': period, 'region': region, 'crisis_type': cat})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
