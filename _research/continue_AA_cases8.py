# -*- coding: utf-8 -*-
"""续作AA：新增8条(安然/世通/牙买加协定/史密森协定/欧洲货币体系/瑞典央行/英格兰银行/DeFi)。"""
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

D = [
 ('enron', '安然公司丑闻(2001)', '其他', 'U5 21世纪', '21世纪', '美洲', '重要',
  '2001年10月内部大规模欺诈曝光后美国能源公司安然申请破产引发的会计丑闻，并导致其审计机构解体。',
  '安然丑闻是一起会计丑闻：在美国能源公司安然（Enron Corporation）于2001年10月内部大规模欺诈的消息公开后申请破产之际爆发，并导致其审计机构解散。该案成为公司治理、审计独立性与信息披露监管改革的标志性事件。具体规模与判决待核实。',
  [{'year': 2001, 'display': '2001年10月', 'event': '安然内部大规模欺诈消息公开，随后申请破产（据 Wikipedia Enron scandal）', 'sources': ['w-en-enron']},
   {'year': 2002, 'display': '2001年后', 'event': '其审计机构随之解散，引发会计与治理监管改革（同上）', 'sources': ['w-en-enron']}],
  [{'step': '通过特殊目的实体与会计手法隐藏债务与亏损', 'sources': ['w-en-enron']},
   {'step': '内部欺诈曝光 → 股价崩跌、评级下调、申请破产', 'sources': ['w-en-enron']},
   {'step': '审计机构解体 → 引发审计独立性与披露监管改革', 'sources': ['w-en-corporate-governance-gap']}],
  [{'holder': '治理/审计视角', 'view': '审计独立性缺失与激励扭曲使欺诈长期隐藏', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-enron']},
   {'holder': '信息不对称视角', 'view': '复杂结构与表外安排加剧投资者信息劣势', 'basis': '待核实', 'sources': ['w-en-information-asymmetry']}],
  '与世通丑闻(2002)同期，共同推动美国公司治理与审计监管改革。具体异同待核实。'),
 ('worldcom', '世通公司丑闻(2002)', '其他', 'U5 21世纪', '21世纪', '美洲', '重要',
  '2002年6月发现的美国世通公司重大会计丑闻，该公司当时为美国第二大长途电话公司。',
  '世通丑闻是2002年6月在世通（WorldCom，当时美国第二大长途电话公司）被发现的重大会计丑闻。据维基条目，1999年至2002年间，由创始人兼首席执行官领导的高级管理人员参与其中。该案与安然并列，成为21世纪初美国公司治理危机的代表。具体金额与判决待核实。',
  [{'year': 2002, 'display': '2002年6月', 'event': '世通重大会计丑闻被揭露（据 Wikipedia WorldCom scandal）', 'sources': ['w-en-worldcom']},
   {'year': 2002, 'display': '1999—2002年', 'event': '高管层在此期间参与会计造假（同上）', 'sources': ['w-en-worldcom']}],
  [{'step': '管理层为维持业绩预期进行系统性会计造假', 'sources': ['w-en-worldcom']},
   {'step': '造假曝光 → 股价崩跌、公司破产', 'sources': ['w-en-worldcom']},
   {'step': '与安然案共同推动审计与披露监管强化', 'sources': ['w-en-enron']}],
  [{'holder': '治理视角', 'view': '高管激励与内控失效导致系统性造假', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-worldcom']},
   {'holder': '委托代理视角', 'view': '代理成本与监督缺位使管理层偏离股东利益', 'basis': '待核实', 'sources': ['w-en-principal-agent']}],
  '与安然丑闻同属2001—2002年美国会计丑闻潮，均涉及高管层系统性造假。具体异同待核实。'),
 ('jamaica-accords', '牙买加协定(1976)', '货币', 'U4 20世纪下半', '20世纪下半', '全球', '重要',
  '批准布雷顿森林货币体系终结的一组国际协议，形式为修改IMF协定条款的建议。',
  '牙买加协定是一组国际协议，批准了布雷顿森林货币体系的终结。它们以向国际货币基金组织（IMF）"协定条款"提出修改建议的形式出现。该协定使浮动汇率合法化，奠定了战后第二阶段的国际货币秩序。具体条款待核实。',
  [{'year': 1976, 'display': '1976年', 'event': '牙买加协定达成，批准布雷顿森林体系终结（据 Wikipedia Jamaica Accords）', 'sources': ['w-en-jamaica-accords']},
   {'year': 1976, 'display': '1976年后', 'event': '以修改IMF协定条款的形式确立新规则（同上）', 'sources': ['w-en-jamaica-accords']}],
  [{'step': '布雷顿森林固定汇率体系在1971年后瓦解 → 需新的法律框架', 'sources': ['w-en-nixon-shock']},
   {'step': '牙买加协定修改IMF协定条款 → 承认浮动汇率', 'sources': ['w-en-jamaica-accords']},
   {'step': '形成战后第二阶段国际货币秩序', 'sources': ['w-en-imf']}],
  [{'holder': '体系演化视角', 'view': '协定使既成的浮动汇率事实合法化', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-jamaica-accords']},
   {'holder': '制度视角', 'view': 'IMF角色从平价管理转向监督与融资', 'basis': '待核实', 'sources': ['w-en-imf']}],
  '与1944年布雷顿森林协定、1971年史密森协定共同构成国际货币体系演变的三步。具体异同待核实。'),
 ('smithsonian-agreement', '史密森协定(1971)', '货币', 'U4 20世纪下半', '20世纪下半', '全球', '重要',
  '1971年12月宣布，建立新的美元本位，多国工业国货币钉住美元、允许波动2.25%。',
  '史密森协定于1971年12月宣布，创建了一种新的美元本位：若干工业化国家的货币钉住美元，这些货币被允许相对美元波动2.25%。该协定是尼克松冲击后试图挽救固定汇率体系的短期安排，但未能持久。具体内容待核实。',
  [{'year': 1971, 'display': '1971年12月', 'event': '史密森协定宣布，建立新美元本位、波动区间2.25%（据 Wikipedia Smithsonian Agreement）', 'sources': ['w-en-smithsonian-agreement']},
   {'year': 1973, 'display': '1971年后', 'event': '该安排未能维持，主要货币转向浮动（待核实）', 'sources': ['w-en-jamaica-accords']}],
  [{'step': '尼克松冲击终止美元兑换黄金 → 固定汇率体系失锚', 'sources': ['w-en-nixon-shock']},
   {'step': '史密森协定重设美元平价与2.25%波动区间', 'sources': ['w-en-smithsonian-agreement']},
   {'step': '安排未能持久 → 最终由牙买加协定承认浮动汇率', 'sources': ['w-en-jamaica-accords']}],
  [{'holder': '修补视角', 'view': '协定试图以调整平价挽救固定汇率', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-smithsonian-agreement']},
   {'holder': '不可持续视角', 'view': '根本失衡未解决，安排迅速失效', 'basis': '待核实', 'sources': ['w-en-triffin-dilemma']}],
  '是布雷顿森林体系终结过程中的过渡安排，介于1971年尼克松冲击与1976年牙买加协定之间。具体异同待核实。'),
 ('ems', '欧洲货币体系(EMS)', '货币', 'U4 20世纪下半', '20世纪下半', '欧洲', '重要',
  '欧洲经济共同体多数国家将货币相互挂钩、以防相对价值大幅波动的多边可调整汇率协议。',
  '欧洲货币体系（EMS）是一项多边可调整汇率协议，欧洲经济共同体（EEC）的多数国家将各自货币相互挂钩，以防止相对价值出现大幅波动。它是欧洲货币一体化的重要阶段，为后来的欧元奠定基础。具体机制与危机待核实。',
  [{'year': 1979, 'display': '1979年起', 'event': 'EMS 建立，EEC 多数国家货币相互挂钩（据 Wikipedia European Monetary System；起始年份待核实）', 'sources': ['w-en-ems']},
   {'year': 1992, 'display': '1990年代', 'event': '体系经历严重汇率危机（如1992年黑色星期三，见相关条目）', 'sources': ['w-en-black-wednesday-1992']}],
  [{'step': '欧洲国家希望稳定汇率、推进一体化 → 建立多边可调整挂钩', 'sources': ['w-en-ems']},
   {'step': '各国须协调货币政策、限制汇率波动区间', 'sources': ['w-en-ems']},
   {'step': '资本流动下区间承压 → 1992年体系危机', 'sources': ['w-en-black-wednesday-1992']}],
  [{'holder': '一体化视角', 'view': 'EMS 是通向货币联盟的必要阶段', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-ems']},
   {'holder': '三元悖论视角', 'view': '固定区间+资本自由流动挤压货币政策独立性', 'basis': '待核实', 'sources': ['w-en-impossible-trinity']}],
  '是布雷顿森林之后最重要的区域汇率安排，其危机（1992）成为不可能三角的经典案例。具体异同待核实。'),
 ('riksbank', '瑞典央行(Sveriges Riksbank)', '制度', 'U6 理论与制度', '理论制度', '欧洲', '补充',
  '瑞典的中央银行，1668年由议会设立，为世界现存最古老的中央银行。',
  '瑞典央行（Sveriges Riksbank，简称 Riksbank）是瑞典的中央银行。它于1668年由瑞典议会（Riksdag）设立，是世界上现存最古老的中央银行，也是持续经营时间第三长的银行。其历史为理解央行的起源与职能演变提供了重要案例。具体沿革待核实。',
  [{'year': 1668, 'display': '1668年', 'event': '瑞典议会设立 Riksbank，为世界现存最古老央行（据 Wikipedia Sveriges Riksbank）', 'sources': ['w-en-riksbank']}],
  [{'step': '1668年由议会设立 → 承担发钞与政府融资职能', 'sources': ['w-en-riksbank']},
   {'step': '职能随时代扩展 → 货币政策、金融稳定', 'sources': ['w-en-central-bank']},
   {'step': '成为现代央行制度的早期范例', 'sources': ['w-en-riksbank']}],
  [{'holder': '制度起源视角', 'view': '央行最初源于政府融资与发钞需要', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-riksbank']},
   {'holder': '比较视角', 'view': '与1694年英格兰银行并列现代央行两大源头', 'basis': '待核实', 'sources': ['w-en-bank-of-england']}],
  '与英格兰银行(1694)并称现代中央银行的两大源头；瑞典央行历史更久。具体异同待核实。'),
 ('bank-of-england', '英格兰银行(Bank of England)', '制度', 'U6 理论与制度', '理论制度', '欧洲', '补充',
  '英国中央银行，1694年设立以充任英国政府的银行家与债务管理者，是现代多数央行的模板。',
  '英格兰银行（BoE）是英国的中央银行，也是多数现代中央银行所效仿的模板。它于1694年设立，充任英国政府的银行家与债务管理者，至今仍是（重要的央行之一）。其在最后贷款人、货币政策与监管方面的实践影响深远。具体沿革待核实。',
  [{'year': 1694, 'display': '1694年', 'event': '英格兰银行设立，充任英国政府银行家与债务管理者（据 Wikipedia Bank of England）', 'sources': ['w-en-bank-of-england']},
   {'year': 1800, 'display': '19世纪', 'event': '在危机中逐步发展最后贷款人职能（具体时间待核实）', 'sources': ['w-en-lender-of-last-resort']}],
  [{'step': '1694年设立 → 为政府融资与发行银行券', 'sources': ['w-en-bank-of-england']},
   {'step': '在金融危机中演化为最后贷款人', 'sources': ['w-en-lender-of-last-resort']},
   {'step': '成为现代央行的制度模板', 'sources': ['w-en-bank-of-england']}],
  [{'holder': '制度演化视角', 'view': '央行职能在危机应对中逐步成型', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-bank-of-england']},
   {'holder': '货币史视角', 'view': '其与金本位、货币学派争论密切相关', 'basis': '待核实', 'sources': ['w-en-banking-school']}],
  '与瑞典央行(1668)并称现代央行源头；英格兰银行更是各国央行制度设计的直接模板。具体异同待核实。'),
 ('defi', '去中心化金融(DeFi)', '货币', 'U5 21世纪', '21世纪', '全球', '补充',
  '通过可编程、无需许可的区块链上的智能合约提供金融工具与服务，减少对中介的依赖。',
  '去中心化金融（DeFi）通过可编程、无需许可（permissionless）区块链上的智能合约提供金融工具与服务。这一方式减少了对经纪商、交易所或银行等中介机构的需要。DeFi 带来效率与可及性，但也伴随智能合约漏洞、治理与监管风险。具体规模待核实。',
  [{'year': 2020, 'display': '2020年代', 'event': 'DeFi 通过智能合约提供借贷、交易等金融服务（据 Wikipedia Decentralized finance）', 'sources': ['w-en-defi']},
   {'year': 2022, 'display': '2022年', 'event': '加密市场崩盘中 DeFi 协议亦受冲击（细节待核实）', 'sources': ['w-en-crypto-bubble']}],
  [{'step': '智能合约替代中介 → 交易与借贷自动化', 'sources': ['w-en-defi']},
   {'step': '无需许可参与 → 提升可及性但减弱准入审查', 'sources': ['w-en-defi']},
   {'step': '代码漏洞、治理攻击与杠杆叠加 → 风险外溢', 'sources': ['w-en-crypto-bubble']}],
  [{'holder': '效率/普惠视角', 'view': 'DeFi 降低中介成本、提升可及性', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-defi']},
   {'holder': '风险/监管视角', 'view': '缺乏中介与监管使欺诈、漏洞与杠杆风险突出', 'basis': '待核实', 'sources': ['w-en-crypto-bubble']}],
  '与传统金融相比，DeFi 缺乏最后贷款人、存款保险与KYC/AML框架。具体异同待核实。'),
]

for eid, title, cat, unit, period, region, tier, ol, ov, tl, causal, schools, comp in D:
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
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值与影响程度待核实补充。【续作AA】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

# 史密森协定 2.25% 数值
f = 'data/entries/smithsonian-agreement.json'
d = json.load(open(f, encoding='utf-8'))
d['key_data'] = [{'label': '史密森协定允许波动区间(1971)', 'value': 2.25, 'unit': '%（相对美元波动幅度）', 'year': 1971,
                  'comparable_price': False,
                  'note': '原文：These currencies were allowed to fluctuate by 2.25% against the dollar；单一来源待核实。',
                  'sources': ['w-en-smithsonian-agreement']}]
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('smithsonian 补 key_data')

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r45_cases.json', encoding='utf-8'))
for eid, v in meta.items():
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
for eid, title, cat, unit, period, region, tier, ol, ov, tl, causal, schools, comp in D:
    if eid in have:
        continue
    cov['entries'].append({
        'id': eid, 'level': 'L2', 'tier': tier, 'status': 'written',
        'source_count': 2, 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': unit, 'period': period, 'region': region, 'crisis_type': cat})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
