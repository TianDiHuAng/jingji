# -*- coding: utf-8 -*-
"""续作V：新增10条非传统政策/危机处置概念(L2,据REST摘要)。"""
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
 ('helicopter-money', '直升机撒钱', '制度',
  '为通胀目标服务的拟议货币政策：央行直接向个人付款，常被视为流动性陷阱下QE的替代。',
  '直升机撒钱是一种为通胀目标服务的拟议货币政策，有时被建议作为经济陷入流动性陷阱时量化宽松（QE）的替代方案。尽管最初的概念指中央银行直接向个人付款，其具体形式仍有讨论。该方案涉及央行与财政的紧密配合。具体机制待核实。',
  [('经济陷入流动性陷阱 → 常规降息与QE传导受阻', 'w-en-helicopter-money'),
   ('央行直接向个人转移资金 → 直接形成需求', 'w-en-helicopter-money'),
   ('绕开金融中介，但模糊货币与财政边界', 'w-en-fiscal-dominance')],
  [('直接刺激视角', '直达居民可绕过传导阻塞、提振需求', 'w-en-helicopter-money'),
   ('纪律/边界视角', '模糊央行与财政边界，损害政策可信度', 'w-en-fiscal-dominance')],
  ['w-en-helicopter-money', 'w-en-liquidity-trap'], []),
 ('mmt', '现代货币理论(MMT)', '理论',
  '关于以本币借款并发行政府债务的主权政府之财政与货币政策作用的非主流宏观理论。',
  '现代货币理论（MMT）是一种非主流的宏观经济理论，关注以本币借款并发行政府债务的主权政府中财政与货币政策的作用。该理论认为本币发行国在通胀约束前不存在名义财政约束。其主张在主流学界存在广泛争议。具体论述待核实。',
  [('主权政府以本币发行货币与债务 → 名义上不受融资约束', 'w-en-mmt'),
   ('约束来自实际资源与通胀（而非预算）', 'w-en-mmt'),
   ('主张以财政扩张实现充分就业（争议很大）', 'w-en-fiscal-dominance')],
  [('MMT视角', '本币发行国的真实约束是通胀而非预算', 'w-en-mmt'),
   ('主流批判视角', '忽视通胀预期、汇率与可信度风险', 'w-en-fiscal-dominance')],
  ['w-en-mmt', 'w-en-fiscal-dominance'], []),
 ('fiscal-dominance', '财政主导', '理论',
  '政府财政压力实际支配或约束一国货币政策的宏观状况。',
  '财政主导是一种宏观经济状况：政府的财政压力实际上支配或约束了一国的货币政策。在财政主导体制下，中央银行控制通胀的常规目标从属于财政部的预算融资需要。这可能损害央行独立性与物价稳定。具体表现待核实。',
  [('财政赤字与债务压力上升 → 迫使央行配合融资', 'w-en-fiscal-dominance'),
   ('货币政策从属财政需要 → 通胀控制目标弱化', 'w-en-fiscal-dominance'),
   ('央行独立性受损、通胀预期失锚', 'w-en-central-bank-independence')],
  [('财政主导视角', '财政压力可实质性绑架货币政策', 'w-en-fiscal-dominance'),
   ('货币主导视角', '央行独立设定利率以控制通胀', 'w-en-central-bank-independence')],
  ['w-en-fiscal-dominance', 'w-en-central-bank-independence'], []),
 ('yield-curve-control', '收益率曲线控制(YCC)', '制度',
  '中央银行通过购买不同数量政府债券等资产，将收益率曲线或利率目标定在特定水平的货币政策操作。',
  '收益率曲线控制（YCC）是一种货币政策操作：中央银行购买数量可变的政府债券或其他金融资产，以将收益率曲线或利率目标定在某一水平。其购买债券的速度通常慢于其他操作方式。YCC 是量化宽松的延伸形式，用于压低特定期限利率。具体实施待核实。',
  [('央行设定特定期限收益率目标 → 承诺无限量购债', 'w-en-yield-curve-control'),
   ('购买规模随市场变化调整 → 将收益率锚定在目标', 'w-en-yield-curve-control'),
   ('压低长期利率支持需求，但退出困难', 'w-en-quantitative-easing')],
  [('政策支持视角', 'YCC 可强力压低长期利率、支持复苏', 'w-en-yield-curve-control'),
   ('退出/风险视角', '资产负债表膨胀、退出时市场动荡', 'w-en-quantitative-tightening')],
  ['w-en-yield-curve-control', 'w-en-quantitative-easing'], []),
 ('debt-ceiling', '美国债务上限', '债务',
  '限制美国联邦政府可借款总额的法律，2025年经立法提高后为41.1万亿美元。',
  '在美国，债务上限是一项限制联邦政府可借款总额的法律。据维基条目，自2025年起，在通过"One Big Beautiful Bill Act"（OBBBA）提高5万亿美元后，债务上限为41.1万亿美元。债务上限之争可能引发技术性违约风险与市场波动。具体进展待核实。',
  [('联邦支出与税收形成赤字 → 需持续借款', 'w-en-debt-ceiling'),
   ('借款总额触及法定上限 → 需国会立法提高', 'w-en-debt-ceiling'),
   ('僵局导致技术性违约风险与市场波动', 'w-en-government-debt')],
  [('财政纪律视角', '上限为债务扩张设置程序性约束', 'w-en-debt-ceiling'),
   ('功能/风险视角', '僵局带来违约尾部风险、损害信用', 'w-en-government-debt')],
  ['w-en-debt-ceiling', 'w-en-government-debt'],
  [('债务上限(2025年起)', 41.1, '万亿美元（经OBBBA提高5万亿后）', 2025,
    '原文：Since 2025, the debt ceiling is $41.1 trillion after being raised by $5 trillion；单一来源待核实。')]),
 ('bailout', '救助与减记（bailout / bail-in）', '制度',
  'bailout指向本会破产的公司或国家提供财务帮助；bail-in则强制债权人或存款人参与承担损失。',
  '救助（bailout）是向本会破产的公司或国家提供财务帮助。它与"减记"（bail-in）不同：在 bail-in 下，全球系统重要性金融机构（G-SIFI）的债券持有人或存款人被强制参与承担损失。二者是危机处置中纳税人负担与私人承担之间的关键分野。具体机制待核实。',
  [('机构或国家面临破产 → 需外部财务帮助或内部损失分摊', 'w-en-bailout'),
   ('bailout 由纳税人出资；bail-in 由债权人/存款人承担', 'w-en-bailout'),
   ('处置框架选择影响道德风险与系统性风险', 'w-en-sifi')],
  [('稳定优先视角', '救助可防止系统性崩溃与连锁反应', 'w-en-bailout'),
   ('道德风险视角', '救助诱发过度冒险，bail-in 可内化成本', 'w-en-moral-hazard')],
  ['w-en-bailout', 'w-en-sifi'], []),
 ('bad-bank', '坏账银行', '制度',
  '隔离银行或金融组织持有的非流动与高风险资产的公司结构。',
  '坏账银行是一种公司结构，用于隔离某家银行或金融组织（或一组机构）持有的非流动性、高风险资产。通过把问题资产移出，原机构可恢复资产负债表清晰度与放贷能力，坏账银行则负责逐步处置这些资产。具体案例待核实。',
  [('银行积累不良与高风险资产 → 资产负债表受损', 'w-en-bad-bank'),
   ('将问题资产剥离至专门载体 → 恢复原机构健康', 'w-en-bad-bank'),
   ('由坏账银行逐步处置，纳税人可能承担损失', 'w-en-bailout')],
  [('处置效率视角', '隔离问题资产可加速恢复信贷', 'w-en-bad-bank'),
   ('成本视角', '定价与损失分担易引发争议', 'w-en-bailout')],
  ['w-en-bad-bank', 'w-en-bailout'], []),
 ('paris-club', '巴黎俱乐部', '债务',
  '主要债权国组成的非正式集团，旨在为债务国的债务问题提供可持续解决方案。',
  '巴黎俱乐部是由主要债权国组成的集团，旨在为债务国的债务问题提供可持续的解决方式。其创立可追溯至1956年的首次非正式会议，当时阿根廷同意与其公共债权人举行会议。巴黎俱乐部是主权债务重组协调的重要平台。具体机制待核实。',
  [('债务国偿付困难 → 需与多边公共债权人协调', 'w-en-paris-club'),
   ('债权国集团协商重组条件（展期、减记等）', 'w-en-paris-club'),
   ('形成协调一致的重组方案，避免各自追债', 'w-en-debt-restructuring')],
  [('协调视角', '集体协商提高重组效率与可预期性', 'w-en-paris-club'),
   ('局限视角', '非正式、覆盖范围有限，私人债权人需另议', 'w-en-debt-restructuring')],
  ['w-en-paris-club', 'w-en-debt-restructuring'], []),
 ('basel-iii', '巴塞尔III', '制度',
  '巴塞尔银行监管委员会针对2008年危机暴露的监管缺陷发布的框架，含资本、压力测试与流动性标准。',
  '巴塞尔III是巴塞尔银行监管委员会（BCBS）针对2008年金融危机所暴露的金融监管缺陷而发布的框架。它为银行资本要求、压力测试与流动性（如流动性覆盖率LCR、净稳定资金比率NSFR）设定国际标准与建议。具体标准与实施进度待核实。',
  [('2008危机暴露资本与流动性监管不足 → 需要新标准', 'w-en-basel-iii'),
   ('设定更高资本要求与流动性比率（LCR/NSFR）', 'w-en-basel-iii'),
   ('各国转化为国内法实施，进度不一', 'w-en-basel-accords')],
  [('审慎强化视角', '提高资本与流动性要求增强体系韧性', 'w-en-basel-iii'),
   ('成本视角', '更高要求可能抑制信贷供给', 'w-en-capital-requirement')],
  ['w-en-basel-iii', 'w-en-basel-accords'], []),
 ('tobin-tax', '托宾税', '制度',
  '对所有即期外汇兑换征收的税，最初由詹姆斯·托宾提出以惩罚短期投机性资金往返。',
  '托宾税最初被定义为对所有即期外汇兑换征收的税，由获诺贝尔经济学奖的经济学家詹姆斯·托宾提出。托宾的税原本意在惩罚短期的金融资金往返投机，从而降低汇率波动与投机冲击。该思路也延伸出更广泛的金融交易税讨论。具体设计待核实。',
  [('短期外汇往返投机 → 加剧汇率波动', 'w-en-tobin-tax'),
   ('对即期兑换征税 → 提高短期投机成本', 'w-en-tobin-tax'),
   ('抑制热钱、但也降低市场流动性（有争议）', 'w-en-capital-control')],
  [('稳定视角', '托宾税可抑制短期投机、稳定汇率', 'w-en-tobin-tax'),
   ('效率视角', '税负降低流动性、可能扭曲市场', 'w-en-capital-control')],
  ['w-en-tobin-tax', 'w-en-capital-control'], []),
]

for eid, title, cat, ol, ov, causal, schools, srcs, kds in D:
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': [],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in causal],
        'key_data': [{'label': k[0], 'value': k[1], 'unit': k[2], 'year': k[3],
                      'comparable_price': False, 'note': k[4], 'sources': [srcs[0]]} for k in kds],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in schools],
        'policy_response': [],
        'comparison': '经济学/金融概念条目，与其他概念互补；具体适用与争论待核实。',
        'svg': svg(title, [causal[0][0][:12], causal[1][0][:12], causal[2][0][:12]]),
        'sources': srcs, 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作V】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r40_concepts.json', encoding='utf-8'))
# 只登记实际使用的来源（跳过重定向来源）
used = {'helicopter-money', 'mmt', 'fiscal-dominance', 'yield-curve-control', 'debt-ceiling',
        'bail-in', 'bad-bank', 'paris-club', 'lcr', 'tobin-tax'}
for eid, v in meta.items():
    if eid not in used:
        continue
    if eid == 'lcr':
        sid = 'w-en-basel-iii'
    elif eid == 'bail-in':
        sid = 'w-en-bailout'
    else:
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
for eid, title, cat, ol, ov, causal, schools, srcs, kds in D:
    if eid in have:
        continue
    cov['entries'].append({
        'id': eid, 'level': 'L2', 'tier': '重要', 'status': 'written',
        'source_count': len(srcs), 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
