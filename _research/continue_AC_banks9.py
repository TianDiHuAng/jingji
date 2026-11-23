# -*- coding: utf-8 -*-
"""续作AC：新增9条银行/机构倒闭案例。"""
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
 ('freddie-mac', '房地美(Freddie Mac)', '制度', 'U6 理论与制度', '理论制度', '美洲', '补充',
  '美国联邦住房贷款抵押公司（FHLMC），1970年创建的政府支持企业，总部弗吉尼亚州麦克莱恩。',
  '联邦住房贷款抵押公司（FHLMC），通称房地美（Freddie Mac），是一家美国上市交易的政府支持企业（GSE），总部位于弗吉尼亚州麦克莱恩。FHLMC 于1970年创建。它与房利美共同构成美国住房抵押贷款二级市场的两大支柱，2008年危机中被接管。具体细节待核实。',
  [{'year': 1970, 'display': '1970年', 'event': '房地美（FHLMC）创建（据 Wikipedia Freddie Mac）', 'sources': ['w-en-freddie-mac']},
   {'year': 2008, 'display': '2008年', 'event': '危机中被政府接管（同上；具体安排待核实）', 'sources': ['w-en-freddie-mac']}],
  [{'step': 'GSE 购买并证券化住房按揭 → 提供二级市场流动性', 'sources': ['w-en-freddie-mac']},
   {'step': '隐性政府担保下的高杠杆扩张 → 风险累积', 'sources': ['w-en-moral-hazard']},
   {'step': '房价下跌致损失剧增 → 2008年被接管', 'sources': ['w-en-fannie-mae']}],
  [{'holder': '住房政策视角', 'view': 'GSE 扩大住房融资可及性', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-freddie-mac']},
   {'holder': '道德风险视角', 'view': '隐性担保导致风险社会化', 'basis': '待核实', 'sources': ['w-en-moral-hazard']}],
  '与房利美（Fannie Mae）同为美国两大住房 GSE，2008年同期被接管；房利美1938年成立、房地美1970年成立。具体异同待核实。'),
 ('indymac', 'IndyMac 银行倒闭(2008)', '银行', 'U5 21世纪', '21世纪', '美洲', '重要',
  '美国加州银行 IndyMac（Independent National Mortgage Corporation 缩称）于2008年倒闭并被FDIC接管。',
  'IndyMac 是 "Independent National Mortgage Corporation" 的缩称，是一家总部位于加利福尼亚州的美国银行，于2008年倒闭并被美国联邦存款保险公司（FDIC）接管。它是次贷危机中存款保险机构处置的典型案例之一。具体规模待核实。',
  [{'year': 2008, 'display': '2008年', 'event': 'IndyMac 倒闭，被 FDIC 接管（据 Wikipedia IndyMac）', 'sources': ['w-en-indymac']}],
  [{'step': '专注Alt-A等高风险按揭 → 房价下跌中资产质量恶化', 'sources': ['w-en-indymac']},
   {'step': '存款流失、流动性枯竭 → 监管接管', 'sources': ['w-en-bank-run']},
   {'step': 'FDIC 接管并处置 → 存款保险介入', 'sources': ['w-en-deposit-insurance']}],
  [{'holder': '资产质量视角', 'view': '高风险按揭集中导致资本耗尽', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-indymac']},
   {'holder': '存款保险视角', 'view': 'FDIC 接管保护小额存款人、限制挤兑传染', 'basis': '待核实', 'sources': ['w-en-deposit-insurance']}],
  '与华盛顿互惠（2008）同属次贷危机中的美国银行倒闭，但 IndyMac 规模较小、由 FDIC 直接接管。具体异同待核实。'),
 ('merrill-lynch', '美林(Merrill Lynch)', '银行', 'U5 21世纪', '21世纪', '美洲', '补充',
  '美国跨国投资管理与财富管理机构，2008年危机中被美国银行收购，现为美银旗下分部。',
  '美林（Merrill Lynch, Pierce, Fenner & Smith Incorporated，现以 Merrill 名义经营）是一家美国跨国投资管理与财富管理机构，现为美国银行（Bank of America）旗下的投资管理与财富管理分部。此前以 Merrill Lynch 品牌闻名。2008年金融危机期间被美国银行收购。具体条款待核实。',
  [{'year': 2008, 'display': '2008年', 'event': '美林在金融危机中被美国银行收购（据 Wikipedia Merrill (company)；具体日期与条款待核实）', 'sources': ['w-en-merrill-lynch']}],
  [{'step': '持有大量按揭相关资产 → 危机中损失扩大', 'sources': ['w-en-merrill-lynch']},
   {'step': '流动性压力与信心下滑 → 寻求并购', 'sources': ['w-en-bank-run']},
   {'step': '被美国银行收购 → 避免破产', 'sources': ['w-en-too-big-to-fail']}],
  [{'holder': '并购处置视角', 'view': '紧急并购避免无序破产与外溢', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-merrill-lynch']},
   {'holder': '系统性视角', 'view': '大型券商倒闭会冲击对手方网络', 'basis': '待核实', 'sources': ['w-en-sifi']}],
  '与贝尔斯登（被摩根大通收购）、雷曼（破产）、AIG（救助）共同构成2008年9月的多种处置路径。具体异同待核实。'),
 ('silicon-valley-bank', '硅谷银行倒闭(2023)', '银行', 'U5 21世纪', '21世纪', '美洲', '重要',
  '硅谷银行（SVB）原为独立商业银行，2023年倒闭，现为 First Citizens 旗下分部。',
  '硅谷银行（Silicon Valley Bank, SVB）曾是一家独立商业银行，现作为 First Citizens BancShares 的分部运营；据维基条目，2026年第四季度 First Citizens 将完全整合 SVB 并停用该名称。SVB 于2023年倒闭，是当年美国银行业危机的起点。具体规模待核实。',
  [{'year': 2023, 'display': '2023年', 'event': '硅谷银行倒闭，成为2023年美国银行业危机起点（据 Wikipedia Silicon Valley Bank）', 'sources': ['w-en-silicon-valley-bank']},
   {'year': 2026, 'display': '2026年第四季度', 'event': 'First Citizens 计划完全整合 SVB 并停用该名称（同上）', 'sources': ['w-en-silicon-valley-bank']}],
  [{'step': '存款高度集中于科技企业 + 长期债券久期风险', 'sources': ['w-en-silicon-valley-bank']},
   {'step': '利率急升致债券浮亏 + 存款集中提取 → 挤兑', 'sources': ['w-en-interest-rate']},
   {'step': '银行倒闭、被收购 → 引发区域性银行连锁压力', 'sources': ['w-en-bank-crisis-2023']}],
  [{'holder': '利率风险视角', 'view': '资产久期错配在加息中形成巨额浮亏', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-interest-rate']},
   {'holder': '数字化挤兑视角', 'view': '网络银行时代挤兑速度远超以往', 'basis': '待核实', 'sources': ['w-en-bank-run']}],
  '与北岩银行(2007)、华盛顿互惠(2008)同属挤兑型倒闭，但SVB挤兑在数日内完成（数字化提款）。具体异同待核实。'),
 ('first-republic', '第一共和银行倒闭(2023)', '银行', 'U5 21世纪', '21世纪', '美洲', '补充',
  '总部旧金山的美国商业银行与财富管理机构，服务高净值客户，2023年倒闭。',
  '第一共和银行（First Republic Bank）是一家总部位于美国加利福尼亚州旧金山的商业银行与财富管理服务提供者，服务高净值个人，在11个州运营93个办公室。该行于2023年倒闭，是当年美国银行业危机的又一案例。具体规模待核实。',
  [{'year': 2023, 'display': '2023年', 'event': '第一共和银行倒闭（据 Wikipedia First Republic Bank）', 'sources': ['w-en-first-republic']}],
  [{'step': '客户结构集中于高净值与未保险存款 → 脆弱性高', 'sources': ['w-en-first-republic']},
   {'step': 'SVB倒闭后信心传染 → 存款大量流失', 'sources': ['w-en-bank-crisis-2023']},
   {'step': '救助无效后被接管并出售', 'sources': ['w-en-bank-failure']}],
  [{'holder': '存款结构视角', 'view': '未保险存款占比高使挤兑更迅猛', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-first-republic']},
   {'holder': '传染视角', 'view': '区域性银行间信心传染是关键', 'basis': '待核实', 'sources': ['w-en-financial-contagion']}],
  '与硅谷银行、签名银行同属2023年美国区域性银行危机。具体异同待核实。'),
 ('signature-bank', '签名银行倒闭(2023)', '银行', 'U5 21世纪', '21世纪', '美洲', '补充',
  '总部纽约的美国全方位服务商业银行，2023年倒闭，为当年银行业危机的一部分。',
  '签名银行（Signature Bank）是一家总部位于纽约市的美国全方位服务商业银行，在纽约、康涅狄格、加利福尼亚、内华达与北卡罗来纳等州设有40个私人客户办公室。该行于2023年倒闭，为当年美国银行业危机的一部分。具体规模待核实。',
  [{'year': 2023, 'display': '2023年', 'event': '签名银行倒闭（据 Wikipedia Signature Bank）', 'sources': ['w-en-signature-bank']}],
  [{'step': '存款集中于特定行业客户 → 集中度风险', 'sources': ['w-en-signature-bank']},
   {'step': 'SVB 倒闭后信心崩塌 → 存款快速流失', 'sources': ['w-en-bank-crisis-2023']},
   {'step': '被监管关闭并处置', 'sources': ['w-en-bank-failure']}],
  [{'holder': '集中度视角', 'view': '客户与存款集中放大挤兑冲击', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-signature-bank']},
   {'holder': '传染视角', 'view': '同期倒闭事件相互强化信心危机', 'basis': '待核实', 'sources': ['w-en-financial-contagion']}],
  '与硅谷银行（2023-03）、第一共和银行（2023）构成当年美国三家主要倒闭银行。具体异同待核实。'),
 ('bcci', 'BCCI 国际信贷商业银行倒闭(1991)', '银行', 'U4 20世纪下半', '20世纪下半', '全球', '重要',
  '1972年由巴基斯坦金融家 Agha Hasan Abedi 创立的国际银行，注册卢森堡、总部卡拉奇与伦敦，1991年因欺诈被关闭。',
  '国际信贷商业银行（BCCI）是一家国际银行，1972年由巴基斯坦金融家 Agha Hasan Abedi 创立。该行在卢森堡注册，总部设于卡拉奇与伦敦。1991年该行因大规模欺诈与洗钱被多国监管机构关闭，成为跨境银行监管失效的经典案例。具体细节待核实。',
  [{'year': 1972, 'display': '1972年', 'event': 'BCCI 由 Agha Hasan Abedi 创立，注册卢森堡（据 Wikipedia BCCI）', 'sources': ['w-en-bcci']},
   {'year': 1991, 'display': '1991年', 'event': 'BCCI 因欺诈等问题被多国监管关闭（同上；具体细节待核实）', 'sources': ['w-en-bcci']}],
  [{'step': '跨境多头注册与分散监管 → 监管真空', 'sources': ['w-en-bcci']},
   {'step': '利用结构从事欺诈、洗钱等违法活动', 'sources': ['w-en-bcci']},
   {'step': '多国联合行动关闭银行 → 暴露跨境监管协作缺陷', 'sources': ['w-en-bank-regulation']}],
  [{'holder': '跨境监管视角', 'view': '监管套利与协调缺失使欺诈长期存续', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-bcci']},
   {'holder': '治理/欺诈视角', 'view': '所有权不透明与内控失效是根源', 'basis': '待核实', 'sources': ['w-en-market-manipulation']}],
  '与安达信、安然等欺诈案相比，BCCI 的特殊性在于跨境监管真空。具体异同待核实。'),
 ('drexel', '德崇证券破产(1990)', '银行', 'U4 20世纪下半', '20世纪下半', '美洲', '重要',
  '美国跨国投资银行德崇证券因垃圾债券市场非法活动于1990年被迫破产，核心人物为 Michael Milken。',
  '德崇证券（Drexel Burnham Lambert Inc.）是一家美国跨国投资银行，因涉入垃圾债券市场的非法活动、由高管 Michael Milken 主导，于1990年被迫破产。该案是1980年代杠杆收购与垃圾债券热潮的终结标志。具体细节待核实。',
  [{'year': 1990, 'display': '1990年', 'event': '德崇证券因垃圾债券市场非法活动被迫破产（据 Wikipedia Drexel Burnham Lambert）', 'sources': ['w-en-drexel']}],
  [{'step': '主导垃圾债券承销与杠杆收购融资 → 高速扩张', 'sources': ['w-en-drexel']},
   {'step': '内幕交易等违法行为被查处 → 声誉与业务崩塌', 'sources': ['w-en-insider-trading']},
   {'step': '客户流失、融资中断 → 1990年破产', 'sources': ['w-en-drexel']}],
  [{'holder': '监管执法视角', 'view': '违法行为的执法终结了其商业模式', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-drexel']},
   {'holder': '市场结构视角', 'view': '垃圾债券市场过度扩张本身不可持续', 'basis': '待核实', 'sources': ['w-en-leverage']}],
  '与1980年代储贷危机（savings-loan-1986）同期，共同标志美国1980年代金融扩张周期的终结。具体异同待核实。'),
 ('barings-1995', '巴林银行倒闭(1995)', '银行', 'U4 20世纪下半', '20世纪下半', '欧洲', '重要',
  '英国商人银行巴林银行1762年由 Francis Baring 创立，1995年因一名交易员的违规交易而倒闭。',
  '巴林银行（Barings Bank）是一家总部位于伦敦的英国商人银行，由 Francis Baring 于1762年创立，是英格兰最古老的商人银行之一（仅次于 Berenberg Bank）。1995年该行因一名交易员的未授权交易造成巨额亏损而倒闭，成为操作风险的经典案例。具体细节待核实。',
  [{'year': 1762, 'display': '1762年', 'event': '巴林银行由 Francis Baring 创立（据 Wikipedia Barings Bank）', 'sources': ['w-en-barings-1995']},
   {'year': 1995, 'display': '1995年', 'event': '巴林银行因未授权交易巨额亏损而倒闭（同上；细节待核实）', 'sources': ['w-en-barings-1995']}],
  [{'step': '交易员同时负责前台交易与后台结算 → 内控失效', 'sources': ['w-en-barings-1995']},
   {'step': '未授权衍生品交易累积巨额亏损并被隐瞒', 'sources': ['w-en-derivative']},
   {'step': '亏损暴露 → 资本金不足、银行倒闭被收购', 'sources': ['w-en-barings-1995']}],
  [{'holder': '操作风险视角', 'view': '职责分离与内控缺失是根本原因', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-barings-1995']},
   {'holder': '衍生品风险视角', 'view': '杠杆化衍生品交易可迅速摧毁资本', 'basis': '待核实', 'sources': ['w-en-derivative']}],
  '与法兴银行(2008)交易员违规案类似，均属操作风险而非系统性金融危机。具体异同待核实。'),
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
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值与影响程度待核实补充。【续作AC】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

# 补 key_data
kd_map = {
 'freddie-mac': [{'label': '房地美成立年份', 'value': 1970, 'unit': '年', 'year': 1970, 'comparable_price': False,
                  'note': '原文：The FHLMC was created in 1970；单一来源待核实。', 'sources': ['w-en-freddie-mac']}],
 'bcci': [{'label': 'BCCI 成立年份', 'value': 1972, 'unit': '年', 'year': 1972, 'comparable_price': False,
           'note': '原文：founded in 1972 by Agha Hasan Abedi；单一来源待核实。', 'sources': ['w-en-bcci']}],
 'barings-1995': [{'label': '巴林银行成立年份', 'value': 1762, 'unit': '年', 'year': 1762, 'comparable_price': False,
                   'note': '原文：It was founded in 1762 by Francis Baring；单一来源待核实。', 'sources': ['w-en-barings-1995']}],
 'first-republic': [{'label': '第一共和银行网点数', 'value': 93, 'unit': '个办公室（分布于11州）', 'year': 2023, 'comparable_price': False,
                     'note': '原文：operated 93 offices in 11 states；单一来源待核实。', 'sources': ['w-en-first-republic']}],
 'signature-bank': [{'label': '签名银行私人客户办公室', 'value': 40, 'unit': '个', 'year': 2023, 'comparable_price': False,
                     'note': '原文：with 40 private client offices；单一来源待核实。', 'sources': ['w-en-signature-bank']}],
}
for eid, kd in kd_map.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    d['key_data'] = kd
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('补 key_data:', list(kd_map))

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r47_cases.json', encoding='utf-8'))
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
