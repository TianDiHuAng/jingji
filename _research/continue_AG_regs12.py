# -*- coding: utf-8 -*-
"""续作AG：新增12条金融监管法规与市场概念(L2,据REST摘要)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：概念示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)

D = [
 ('optimum-currency-area', '最优货币区', '货币',
  '共享单一货币能使经济效率最大化的地理区域。',
  '在经济学中，最优货币区（OCA）或最优货币区域（OCR）是这样一种地理区域：让整个区域共享单一货币将最大化经济效率。该理论用于评估货币联盟（如欧元区）的合理性，强调要素流动性、开放度与冲击对称性等条件。具体标准待核实。',
  [('区域内要素流动充分、冲击对称 → 单一货币效率最高', 'w-en-optimum-currency-area'),
   ('缺乏这些条件时 → 单一货币带来调整成本', 'w-en-optimum-currency-area'),
   ('构成评估货币联盟的理论基准', 'w-en-currency-union')],
  [('最优货币区视角', '满足条件时共享货币提升效率', 'w-en-optimum-currency-area'),
   ('主权/调整视角', '不满足条件时丧失汇率与货币政策工具', 'w-en-euro-area-crisis')],
  ['w-en-optimum-currency-area', 'w-en-currency-union'], []),
 ('glass-steagall', '格拉斯-斯蒂格尔法案(1933)', '制度',
  '美国1933年银行法中分离商业银行与投资银行的四项条款。',
  '格拉斯-斯蒂格尔立法指美国1933年《银行法》中分离商业银行与投资银行的四项条款。该法案在大萧条后建立了商业银行业务与投资银行业务之间的"防火墙"，后于1990年代被大幅废止，常被引为2008年危机的一个背景因素。具体条款待核实。',
  [('1929危机后 → 国会立法分离两类银行业务', 'w-en-glass-steagall'),
   ('商业银行与投资银行分业经营 → 降低利益冲突与风险交叉', 'w-en-glass-steagall'),
   ('1990年代放松/废止 → 混业重新扩张（争议）', 'w-en-subprime-crisis-2007')],
  [('分业视角', '防火墙降低存款机构承担证券风险', 'w-en-glass-steagall'),
   ('混业视角', '分业限制规模经济与多元化', 'w-en-too-big-to-fail')],
  ['w-en-glass-steagall', 'w-en-bank-regulation'], []),
 ('dodd-frank', '多德-弗兰克法案(2010)', '制度',
  '2010年7月21日颁布的美国联邦法律，是应对2007—2008年金融危机的主要立法。',
  '《多德-弗兰克华尔街改革与消费者保护法》（通称多德-弗兰克法案）是一部美国联邦法律，于2010年7月21日颁布，作为对2007—2008年金融危机的主要立法回应。它涉及系统性风险监管、消费者保护、衍生品与处置机制等。具体条款待核实。',
  [('2007—2008 金融危机暴露监管缺口 → 立法回应', 'w-en-dodd-frank'),
   ('2010年7月21日颁布 → 建立宏观审慎与消费者保护框架', 'w-en-dodd-frank'),
   ('引入沃尔克规则、压力测试与处置规划等工具', 'w-en-volcker-rule')],
  [('改革视角', '填补系统性风险与消费者保护缺口', 'w-en-dodd-frank'),
   ('负担视角', '合规成本上升、抑制信贷与做市', 'w-en-bank-regulation')],
  ['w-en-dodd-frank', 'w-en-bank-regulation'], []),
 ('volcker-rule', '沃尔克规则', '制度',
  '多德-弗兰克法案第619条，限制银行以自有账户从事自营交易等高风险业务。',
  '沃尔克规则是《多德-弗兰克华尔街改革与消费者保护法》第619条。该规则最初由美国经济学家、前美联储主席保罗·沃尔克（Paul Volcker）于2010年提出，用以限制（银行从事高风险自营交易等）。其具体实施与豁免存在争论。具体条款待核实。',
  [('银行以自有账户自营交易 → 承担高风险并可能获隐性担保', 'w-en-volcker-rule'),
   ('规则限制自营交易与相关基金投资', 'w-en-volcker-rule'),
   ('降低存款机构的风险承担与道德风险', 'w-en-moral-hazard')],
  [('风险隔离视角', '限制自营交易可保护存款与 taxpayer', 'w-en-volcker-rule'),
   ('流动性视角', '限制做市可能削弱市场流动性（有争议）', 'w-en-liquidity')],
  ['w-en-volcker-rule', 'w-en-dodd-frank'], []),
 ('tarp', '问题资产救助计划(TARP)', '制度',
  '美国政府购买金融机构有毒资产与股权以强化金融部门的计划。',
  '问题资产救助计划（TARP）是美国政府的一项计划，通过从金融机构购买有毒资产与股权来强化其金融部门，由国会通过并由（总统）签署成为法律。该计划是2008年危机中规模最大的直接干预之一，其成本与效果存在争议。具体规模待核实。',
  [('2008年危机中金融机构资产恶化 → 需要直接资本注入', 'w-en-tarp'),
   ('政府购买有毒资产与股权 → 稳定金融部门', 'w-en-tarp'),
   ('道德风险与纳税人成本引发争议', 'w-en-moral-hazard')],
  [('救助视角', '直接注资阻止系统性崩溃', 'w-en-tarp'),
   ('道德风险视角', '救助鼓励冒险、成本社会化', 'w-en-bailout')],
  ['w-en-tarp', 'w-en-bailout'], []),
 ('sarbanes-oxley', '萨班斯-奥克斯利法案(2002)', '制度',
  '2002年7月30日颁布的美国联邦法律，规定公司财务记录与报告的特定做法。',
  '《萨班斯-奥克斯利法案》（2002年）是一部美国联邦法律，强制要求公司在财务记录与报告中遵循特定做法。该法于2002年7月30日颁布，是对安然与世通等会计丑闻的立法回应，强化了内控、审计独立性与高管责任。具体条款待核实。',
  [('安然、世通等会计丑闻 → 投资者信心受损', 'w-en-sarbanes-oxley'),
   ('2002年7月30日立法 → 强化内控与审计独立性', 'w-en-sarbanes-oxley'),
   ('提高披露要求与高管责任', 'w-en-principal-agent')],
  [('监管强化视角', '更严内控与审计提升信息可信度', 'w-en-sarbanes-oxley'),
   ('成本视角', '合规成本对小企业负担较重', 'w-en-bank-regulation')],
  ['w-en-sarbanes-oxley', 'w-en-enron'], []),
 ('financial-inclusion', '金融包容', '制度',
  '获得金融服务的机会的可及性与平等性。',
  '金融包容是获得金融服务的机会的可及性与平等性。它指个人与企业能够获得适当、可负担且及时的金融产品与服务的过程。金融包容被视为减贫与包容性增长的重要条件，其与金融稳定的关系存在讨论。具体度量待核实。',
  [('部分群体缺乏金融服务可及性 → 被排除在正规金融之外', 'w-en-financial-inclusion'),
   ('提升储蓄、信贷与保险可及 → 平滑消费与投资', 'w-en-financial-inclusion'),
   ('过快扩张而监管不足 → 可能累积风险', 'w-en-microfinance')],
  [('普惠视角', '金融包容支持减贫与机会平等', 'w-en-financial-inclusion'),
   ('审慎视角', '需与消费者保护、审慎监管平衡', 'w-en-microfinance')],
  ['w-en-financial-inclusion', 'w-en-microfinance'], []),
 ('financial-disintermediation', '金融脱媒', '制度',
  '在经济或供应链中去除中介环节，即"去掉中间人"。',
  '金融脱媒是在经济或供应链中去除中介的过程，即在进行一笔或一系列交易时"去掉中间人"，而非通过传统的分销渠道。在金融领域，它表现为资金绕过银行等中介直接融通，既提升效率也可能削弱监管覆盖。具体表现待核实。',
  [('资金供求双方直接对接 → 绕过银行等中介', 'w-en-financial-disintermediation'),
   ('降低中介成本、提升效率', 'w-en-financial-disintermediation'),
   ('但可能移出监管与存款保险覆盖 → 新的脆弱性', 'w-en-shadow-banking')],
  [('效率视角', '脱媒降低融资成本、拓宽渠道', 'w-en-financial-disintermediation'),
   ('监管视角', '脱媒可能形成监管盲区', 'w-en-shadow-banking')],
  ['w-en-financial-disintermediation', 'w-en-shadow-banking'], []),
 ('credit-rationing', '信贷配给', '理论',
  '贷款方在既定报价利率下限制对借款人的新增信贷供给，而非仅靠价格出清。',
  '信贷配给按定义是贷款方在既定报价利率下限制对需要资金的借款人的新增信贷供给。它是市场失灵的一个例子：价格机制未能出清市场，部分愿付更高利率的借款人仍被拒贷，原因在于信息不对称与逆向选择。具体机制待核实。',
  [('信息不对称 → 提高利率吸引高风险借款人（逆向选择）', 'w-en-credit-rationing'),
   ('贷款方宁愿配给信贷而非提价 → 市场不出清', 'w-en-credit-rationing'),
   ('信贷可得性下降 → 投资与产出受抑', 'w-en-credit-crunch')],
  [('信息不对称视角', '逆向选择使利率无法出清信贷市场', 'w-en-credit-rationing'),
   ('均衡视角', '价格可出清、配给为暂时现象', 'w-en-adverse-selection')],
  ['w-en-credit-rationing', 'w-en-adverse-selection'], []),
 ('odious-debt', '恶债', '债务',
  '国际法中的一种法律理论：专制政权所借国债不应被强制执行。',
  '在国际法中，恶债（亦称非法债务）是一种法律理论，主张由专制政权所产生的国家债务不应具有可执行性。按此学说，此类债务被视为（不应由继任政府承担）。该理论在实践中的适用极具争议。具体论述待核实。',
  [('专制政权借债用于非公益目的 → 债务合法性受质疑', 'w-en-odious-debt'),
   ('继任政府主张债务不可执行 → 拒绝偿付', 'w-en-odious-debt'),
   ('与主权债务重组、债权人协调相交织', 'w-en-sovereign-default')],
  [('恶债视角', '非代表人民利益的债务不应继承', 'w-en-odious-debt'),
   ('债权人视角', '广义适用会破坏债务契约的可预期性', 'w-en-sovereign-default')],
  ['w-en-odious-debt', 'w-en-sovereign-default'], []),
 ('hot-money', '热钱', '货币',
  '为赚取短期利差或预期汇率变动而跨境流动的投机性资金。',
  '在经济学中，热钱是为赚取利率差异和/或预期汇率变动所带来的短期利润而从一个国家流向另一个国家的资金。这些投机性资本流动被称为"热钱"，因其流动迅速、易加剧汇率与资产价格波动。具体规模待核实。',
  [('两国利差或预期升值 → 资金跨境逐利', 'w-en-hot-money'),
   ('短期大规模流入 → 推高汇率与资产价格', 'w-en-hot-money'),
   ('情绪逆转时迅速流出 → 加剧危机', 'w-en-sudden-stop')],
  [('逐利视角', '热钱提高市场流动性、压低利差', 'w-en-hot-money'),
   ('稳定视角', '短期资本流动放大波动、需管制', 'w-en-capital-control')],
  ['w-en-hot-money', 'w-en-capital-control'], []),
 ('carry-trade', '套利交易(carry)', '制度',
  '资产的持有回报（carry）：持有它的收益或成本；常见为借低息货币买高息资产。',
  '资产的 carry 是持有它所得的回报，或持有它的成本。例如商品通常是负 carry 资产，因为持有需承担仓储成本或可能贬值。在汇率语境中，carry trade 指借入低利率货币、投资高利率资产以赚取利差。该类交易在波动骤升时可能集中平仓。具体机制待核实。',
  [('低利率货币借款 → 投资高利率资产', 'w-en-carry-trade'),
   ('赚取利差（carry）→ 若汇率稳定则收益可观', 'w-en-carry-trade'),
   ('波动骤升或汇率逆转 → 集中平仓、放大冲击', 'w-en-leverage')],
  [('收益视角', 'carry trade 提供利差收益与流动性', 'w-en-carry-trade'),
   ('风险视角', '拥挤交易在逆转时引发踩踏式平仓', 'w-en-leverage-cycle')],
  ['w-en-carry-trade', 'w-en-leverage'], []),
]

for row in D:
    eid, title, cat, ol, ov, causal, schools, srcs, _kd = row
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': [],
        'causal_chain': [{'step': (st if isinstance(st, str) else '1929危机后 → 国会立法分离两类银行业务'), 'sources': [s]} for st, s in causal],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in schools],
        'policy_response': [],
        'comparison': '金融监管/市场概念，与相关法规和案例互补；具体适用待核实。',
        'svg': svg(title, [str(causal[0][0])[:12], str(causal[1][0])[:12], str(causal[2][0])[:12]]),
        'sources': list(dict.fromkeys(srcs)), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作AG】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r52_concepts.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid in ('shadow-bank', 'debt-moratorium'):
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
for row in D:
    eid, title, cat = row[0], row[1], row[2]
    if eid in have:
        continue
    cov['entries'].append({
        'id': eid, 'level': 'L2', 'tier': '重要', 'status': 'written',
        'source_count': 2, 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
