# -*- coding: utf-8 -*-
"""续作AB：新增8条2008危机机构案例与欺诈案例。"""
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
 ('lehman', '雷曼兄弟破产(2008)', '银行', 'U5 21世纪', '21世纪', '美洲', '核心',
  '美国全球金融服务公司雷曼兄弟1850年成立，2008年破产前为美国第四大投行、约2.5万员工。',
  '雷曼兄弟控股公司（Lehman Brothers Holdings Inc.）是一家美国全球金融服务公司，成立于1850年。在2008年申请破产之前，雷曼是美国第四大投资银行，拥有约25000名员工。其破产是2008年全球金融危机的标志性事件，引发系统性恐慌。具体资产负债规模与后续处置待核实。',
  [{'year': 1850, 'display': '1850年', 'event': '雷曼兄弟成立（据 Wikipedia Lehman Brothers）', 'sources': ['w-en-lehman']},
   {'year': 2008, 'display': '2008年', 'event': '雷曼申请破产，破产前为美国第四大投行、约2.5万员工（同上）', 'sources': ['w-en-lehman']}],
  [{'step': '高杠杆与大量按揭相关资产 → 房价下跌中损失放大', 'sources': ['w-en-lehman']},
   {'step': '融资市场信心丧失、流动性枯竭 → 无法续滚负债', 'sources': ['w-en-credit-crunch']},
   {'step': '2008年申请破产 → 引发全球金融体系系统性恐慌', 'sources': ['w-en-subprime-crisis-2007']}],
  [{'holder': '杠杆/流动性视角', 'view': '高杠杆叠加短期融资依赖导致挤兑式崩塌', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-lehman']},
   {'holder': '系统性风险视角', 'view': '不救助的决策放大了全局传染', 'basis': '待核实', 'sources': ['w-en-systemic-risk']}],
  '与贝尔斯登（被收购）、AIG（被救助）形成2008年三种处置路径的对照：破产、并购、救助。具体异同待核实。'),
 ('bear-stearns', '贝尔斯登(Bear Stearns)', '银行', 'U5 21世纪', '21世纪', '美洲', '重要',
  '美国控股公司，经营投资银行、证券交易与经纪业务，2008年危机中被摩根大通收购。',
  '贝尔斯登公司（The Bear Stearns Companies, Inc.）是一家美国控股公司，从事投资银行、证券交易与经纪业务，原总部位于纽约曼哈顿的贝尔斯登大楼。该公司在2008年危机中因流动性枯竭而被紧急收购。具体交易条款待核实。',
  [{'year': 2008, 'display': '2008年3月', 'event': '贝尔斯登在流动性危机中被摩根大通收购（据 Wikipedia Bear Stearns；具体日期与条款待核实）', 'sources': ['w-en-bear-stearns']}],
  [{'step': '大量持有按揭相关证券 → 抵押品价值下跌', 'sources': ['w-en-bear-stearns']},
   {'step': '对手方撤资、回购融资中断 → 流动性迅速枯竭', 'sources': ['w-en-repo']},
   {'step': '监管促成紧急收购 → 避免无序破产', 'sources': ['w-en-too-big-to-fail']}],
  [{'holder': '流动性视角', 'view': '回购依赖使机构在信心逆转时迅速失血', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-repo']},
   {'holder': '太大不能倒视角', 'view': '系统性关联迫使当局促成并购', 'basis': '待核实', 'sources': ['w-en-too-big-to-fail']}],
  '与雷曼（破产）、AIG（救助）并列2008年三种处置模式：并购、破产、救助。具体异同待核实。'),
 ('northern-rock', '北岩银行挤兑(2007)', '银行', 'U5 21世纪', '21世纪', '欧洲', '重要',
  '英国银行北岩（Northern Rock）原为建房互助社，2007年遭遇英国百余年来首次大规模挤兑。',
  '北岩银行（Northern Rock，前身为 Northern Rock Building Society）是一家英国银行，总部位于纽卡斯尔。它最初是建房互助社，后改制为银行。2007年该行因批发融资中断而遭遇挤兑，成为英国现代银行史上的标志性事件。具体细节待核实。',
  [{'year': 2007, 'display': '2007年', 'event': '北岩银行遭遇挤兑，成为英国现代银行危机标志事件（据 Wikipedia Northern Rock；具体日期待核实）', 'sources': ['w-en-northern-rock']},
   {'year': 1997, 'display': '1997年前后', 'event': '由建房互助社改制为银行（同上；具体年份待核实）', 'sources': ['w-en-northern-rock']}],
  [{'step': '依赖批发融资快速扩张按揭 → 负债端脆弱', 'sources': ['w-en-northern-rock']},
   {'step': '批发市场冻结 → 融资中断，消息引发储户挤兑', 'sources': ['w-en-bank-run']},
   {'step': '央行提供流动性支持、最终被国有化（待核实）', 'sources': ['w-en-lender-of-last-resort']}],
  [{'holder': '融资结构视角', 'view': '过度依赖批发融资使银行易受市场冻结冲击', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-northern-rock']},
   {'holder': '挤兑/存款保险视角', 'view': '存款保障不足放大零售挤兑', 'basis': '待核实', 'sources': ['w-en-deposit-insurance']}],
  '与1930年代美国银行挤兑、2023年硅谷银行同属"融资结构脆弱+信心崩塌"型挤兑。具体异同待核实。'),
 ('washington-mutual', '华盛顿互惠银行倒闭(2008)', '银行', 'U5 21世纪', '21世纪', '美洲', '重要',
  '美国储蓄银行控股公司，总部西雅图；其银行曾是美国最大储贷协会，2008年倒闭。',
  '华盛顿互惠公司（Washington Mutual, Inc）是一家总部位于西雅图的美国储蓄银行控股公司，是华盛顿互惠银行的母公司。该银行在倒闭之前是美国最大的储贷协会（savings and loan association）。2008年其在危机中倒闭，成为美国历史上最大的银行倒闭案之一。具体规模待核实。',
  [{'year': 2008, 'display': '2008年', 'event': '华盛顿互惠银行倒闭，此前为美国最大储贷协会（据 Wikipedia Washington Mutual）', 'sources': ['w-en-washington-mutual']}],
  [{'step': '大量发放高风险按揭贷款 → 房价下跌中损失剧增', 'sources': ['w-en-washington-mutual']},
   {'step': '存款流失与评级下调 → 流动性枯竭', 'sources': ['w-en-bank-run']},
   {'step': '被监管接管、资产出售 → 美国史上最大银行倒闭之一', 'sources': ['w-en-bank-failure']}],
  [{'holder': '资产质量视角', 'view': '高风险按揭集中导致资本迅速耗尽', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-washington-mutual']},
   {'holder': '处置视角', 'view': '监管接管与资产拆分降低系统性冲击', 'basis': '待核实', 'sources': ['w-en-bank-failure']}],
  '与IndyMac等2008年美国银行倒闭同属储贷机构在次贷危机中的失败。具体异同待核实。'),
 ('aig', 'AIG 救助(2008)', '银行', 'U5 21世纪', '21世纪', '美洲', '重要',
  '全球保险公司AIG（1919年成立，业务遍及200多国家）在2008年因衍生品损失被美国政府救助。',
  '美国国际集团（AIG）是一家总部位于纽约的全球保险公司，业务遍及200多个国家和地区，成立于1919年，主要提供商业与个人保险。2008年该集团因信用违约互换等衍生品巨额损失而濒临倒闭，最终获得美国政府大规模救助。具体金额待核实。',
  [{'year': 1919, 'display': '1919年', 'event': 'AIG 成立（据 Wikipedia American International Group）', 'sources': ['w-en-aig']},
   {'year': 2008, 'display': '2008年', 'event': 'AIG 因衍生品损失濒临倒闭，获美国政府救助（同上；具体规模待核实）', 'sources': ['w-en-aig']}],
  [{'step': '保险集团大量承保 CDS 等衍生品 → 隐性杠杆巨大', 'sources': ['w-en-aig']},
   {'step': '次贷违约上升 → 抵押品追缴与评级下调', 'sources': ['w-en-credit-default-swap']},
   {'step': '系统性关联迫使政府救助 → 避免连锁崩溃', 'sources': ['w-en-sifi']}],
  [{'holder': '影子银行视角', 'view': '保险机构从事类银行衍生品业务，监管不足', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-shadow-banking']},
   {'holder': '系统性风险视角', 'view': '与金融机构的对手方网络使救助成为必要', 'basis': '待核实', 'sources': ['w-en-sifi']}],
  '与雷曼（破产）形成对照：AIG 因对手方网络被视为不可破产，获得救助。具体异同待核实。'),
 ('fannie-mae', '房利美(Fannie Mae)', '制度', 'U6 理论与制度', '理论制度', '美洲', '重要',
  '美国联邦国民抵押贷款协会（FNMA），1938年大萧条期间成立，1968年起为上市公司，属政府支持企业。',
  '联邦国民抵押贷款协会（FNMA），通称房利美（Fannie Mae），是一家美国政府支持企业（GSE），自1968年起为上市公司。它于1938年大萧条期间成立。房利美在美国住房抵押贷款二级市场中扮演核心角色，2008年危机后被接管。具体细节待核实。',
  [{'year': 1938, 'display': '1938年', 'event': '房利美在大萧条期间成立（据 Wikipedia Fannie Mae）', 'sources': ['w-en-fannie-mae']},
   {'year': 1968, 'display': '1968年', 'event': '房利美成为上市公司（同上）', 'sources': ['w-en-fannie-mae']},
   {'year': 2008, 'display': '2008年', 'event': '危机中被政府接管（同上；具体安排待核实）', 'sources': ['w-en-fannie-mae']}],
  [{'step': 'GSE 为住房按揭提供二级市场流动性 → 扩大住房融资', 'sources': ['w-en-fannie-mae']},
   {'step': '隐性政府担保 + 高风险敞口 → 道德风险累积', 'sources': ['w-en-moral-hazard']},
   {'step': '房价下跌致损失剧增 → 2008年被接管', 'sources': ['w-en-subprime-crisis-2007']}],
  [{'holder': '住房政策视角', 'view': 'GSE 提升住房融资可及性', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-fannie-mae']},
   {'holder': '道德风险视角', 'view': '隐性担保鼓励过度冒险、私有化收益社会化损失', 'basis': '待核实', 'sources': ['w-en-moral-hazard']}],
  '与房地美（Freddie Mac）同为美国两大住房 GSE，2008年同期被接管。具体异同待核实。'),
 ('bernie-madoff', '麦道夫庞氏骗局', '其他', 'U5 21世纪', '21世纪', '美洲', '重要',
  '美国金融家麦道夫策划了史上已知最大的庞氏骗局，估计规模约650亿美元。',
  '伯纳德·劳伦斯·麦道夫（Bernard Lawrence Madoff）是一位美国金融家、股票经纪人与诈骗者，他承认是历史上已知最大庞氏骗局的主谋，估计规模约650亿美元。他曾一度担任纳斯达克（Nasdaq）主席。该案成为投资者保护与监管失效的经典案例。具体判决待核实。',
  [{'year': 2008, 'display': '2008年', 'event': '麦道夫庞氏骗局曝光（据 Wikipedia Bernie Madoff；具体日期待核实）', 'sources': ['w-en-bernie-madoff']},
   {'year': 2008, 'display': '规模', 'event': '估计约650亿美元，为史上已知最大庞氏骗局（同上）', 'sources': ['w-en-bernie-madoff']}],
  [{'step': '以稳定高回报为诱饵吸引投资者 → 资金持续流入', 'sources': ['w-en-bernie-madoff']},
   {'step': '以新资金支付旧投资者"收益" → 维持假象', 'sources': ['w-en-ponzi-scheme']},
   {'step': '赎回压力增大、资金链断裂 → 骗局暴露', 'sources': ['w-en-bernie-madoff']}],
  [{'holder': '欺诈视角', 'view': '本质是资金链骗局，收益从未真实产生', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-ponzi-scheme']},
   {'holder': '监管失效视角', 'view': '监管机构长期未识别异常回报与账目问题', 'basis': '待核实', 'sources': ['w-en-bernie-madoff']}],
  '是庞氏骗局（ponzi-scheme）概念的最大规模实例；与FTX等加密欺诈在机制上有相似性。具体异同待核实。'),
 ('arthur-andersen', '安达信(Arthur Andersen)', '制度', 'U6 理论与制度', '理论制度', '美洲', '补充',
  '美国芝加哥的会计师事务所，2001年已成为世界最大跨国专业服务机构之一，因安然案解体。',
  '安达信（Arthur Andersen LLP）是一家总部位于芝加哥的美国会计师事务所，提供审计、税务咨询与其他专业服务。到2001年，它已成为世界最大的跨国（专业服务）机构之一。因安然审计失败，该事务所随后解体，五大会计师事务所变为四大。具体细节待核实。',
  [{'year': 1913, 'display': '20世纪初', 'event': '安达信作为会计师事务所成立（据 Wikipedia Arthur Andersen；具体年份待核实）', 'sources': ['w-en-arthur-andersen']},
   {'year': 2001, 'display': '2001年', 'event': '已成为世界最大跨国专业服务机构之一（同上）', 'sources': ['w-en-arthur-andersen']},
   {'year': 2002, 'display': '2002年', 'event': '因安然审计失败而解体（同上）', 'sources': ['w-en-arthur-andersen']}],
  [{'step': '审计与咨询业务捆绑 → 独立性与利益冲突', 'sources': ['w-en-arthur-andersen']},
   {'step': '安然造假未被揭示 → 审计失败暴露', 'sources': ['w-en-enron']},
   {'step': '事务所信誉崩塌 → 解体，行业格局由五变四', 'sources': ['w-en-arthur-andersen']}],
  [{'holder': '审计独立性视角', 'view': '咨询收入依赖损害审计独立性', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-arthur-andersen']},
   {'holder': '声誉/信息中介视角', 'view': '声誉资本一旦崩塌即不可恢复', 'basis': '待核实', 'sources': ['w-en-credit-rating']}],
  '与安永、德勤、毕马威、普华永道原并称"五大"，安达信解体后成为"四大"。具体异同待核实。'),
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
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值与影响程度待核实补充。【续作AB】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

# 补 key_data（单一来源，标待核实）
kd_map = {
 'lehman': [{'label': '雷曼破产前员工数', 'value': 25000, 'unit': '人（约）', 'year': 2008, 'comparable_price': False,
             'note': '原文：with about 25,000 employees；单一来源待核实。', 'sources': ['w-en-lehman']}],
 'bernie-madoff': [{'label': '麦道夫骗局规模(估计)', 'value': 65, 'unit': '十亿美元（约650亿美元，估计）', 'year': 2008, 'comparable_price': False,
             'note': '原文：worth an estimated $65 billion；单一来源待核实。', 'sources': ['w-en-bernie-madoff']}],
 'fannie-mae': [{'label': '房利美成立年份', 'value': 1938, 'unit': '年', 'year': 1938, 'comparable_price': False,
             'note': '原文：Founded in 1938 during the Great Depression；单一来源待核实。', 'sources': ['w-en-fannie-mae']}],
 'aig': [{'label': 'AIG 成立年份', 'value': 1919, 'unit': '年', 'year': 1919, 'comparable_price': False,
             'note': '原文：Founded in 1919；单一来源待核实。', 'sources': ['w-en-aig']}],
}
for eid, kd in kd_map.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    d['key_data'] = kd
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('补 key_data:', list(kd_map))

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r46_cases.json', encoding='utf-8'))
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
