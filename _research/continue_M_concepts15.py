# -*- coding: utf-8 -*-
"""续作M：新增15条经济学/金融概念(L2,据REST摘要)。"""
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

# (id, title, crisis_type, one_line, overview, [(step, src)], [(holder, view, src)], [src], [kd])
D = [
 ('shadow-banking', '影子银行体系', '银行',
  '在常规银行监管之外、提供类似银行服务的非银行金融中介集合。',
  '影子银行体系指在法律上提供类似传统商业银行服务、但处于常规银行监管之外的非银行金融中介（NBFI）组成的集合。据标普全球估算，2022年底主要司法辖区的影子银行持有约63万亿美元金融资产，相当于全球GDP的78%；2009年分别为28万亿美元和68%。该规模数据为单一来源，待核实。',
  [('非银行中介提供类银行服务（期限/流动性转换）→ 满足融资需求', 'w-en-shadow-banking'),
   ('处于常规银行监管之外 → 杠杆与期限错配可能累积', 'w-en-shadow-banking'),
   ('压力下流动性链条断裂 → 放大金融体系脆弱性', 'w-en-systemic-risk')],
  [('金融创新/补位视角', '影子银行填补银行融资空白、提升资金配置效率', 'w-en-shadow-banking'),
   ('监管套利/系统性风险视角', '监管之外的中介可能累积未被监测的杠杆与错配', 'w-en-systemic-risk')],
  ['w-en-shadow-banking', 'w-en-systemic-risk'],
  [('影子银行资产规模(2022年底)', 63, '万亿美元（主要辖区，S&P Global估算）', 2022,
    '原文：shadow banking held about $63 trillion in financial assets ... representing 78% of global GDP；单一来源待核实。')]),
 ('deflation', '通货紧缩', '理论',
  '一般价格水平持续下降、货币单位实际价值上升的现象。',
  '通货紧缩指货币记账单位的实际价值上升，表现为商品与服务一般价格水平下降，可通过广义价格指数衡量。与通胀相反，通缩可能加重实际债务负担并抑制需求。具体度量与影响待核实。',
  [('总需求不足或供给过剩 → 一般价格水平下降', 'w-en-deflation'),
   ('实际债务负担上升、消费推迟 → 需求进一步走弱', 'w-en-deflation'),
   ('通缩预期自我强化 → 经济下行加深', 'w-en-great-depression')],
  [('货币视角', '货币供给收缩可导致通缩', 'w-en-money-supply'),
   ('债务-通缩视角', '通缩抬高实际债务负担，加剧萧条', 'w-en-great-depression')],
  ['w-en-deflation', 'w-en-money-supply'], []),
 ('balance-of-payments', '国际收支', '货币',
  '一国一定时期内对外的全部资金流入与流出的对比。',
  '国际收支指一国在特定时期内从境外流入的资金与流向境外资金之间的差额，由个人、企业与政府机构的交易构成，比较商品与服务贸易以及国际投资产生的收支。具体口径待核实。',
  [('贸易与投资往来 → 记录各项外汇收支', 'w-en-balance-of-payments'),
   ('经常账户与资本/金融账户变动 → 形成整体差额', 'w-en-balance-of-payments'),
   ('失衡累积 → 汇率与外部融资压力', 'w-en-currency-crisis')],
  [('国际收支视角', '外部失衡反映储蓄-投资与竞争力状况', 'w-en-balance-of-payments'),
   ('货币/汇率视角', '失衡通过汇率与储备调整', 'w-en-exchange-rate-regime')],
  ['w-en-balance-of-payments', 'w-en-exchange-rate-regime'], []),
 ('exchange-rate-regime', '汇率制度', '货币',
  '一国货币当局管理本币对其他货币及外汇市场关系的方式。',
  '汇率制度是货币当局（或货币联盟）管理本币相对其他货币与外汇市场的方式，与货币政策密切相关，二者共同受经济规模与开放度、通胀率、劳动力市场弹性、金融市场发展与资本流动性等因素影响。具体分类待核实。',
  [('当局选择固定/浮动或中间制度 → 决定汇率形成机制', 'w-en-exchange-rate-regime'),
   ('资本流动与货币政策独立性受制度约束', 'w-en-impossible-trinity'),
   ('制度选择影响外部冲击的吸收方式', 'w-en-currency-crisis')],
  [('固定汇率视角', '钉住有助于稳定预期与贸易，但需承担干预成本', 'w-en-exchange-rate-regime'),
   ('浮动汇率视角', '浮动可吸收外部冲击、保留货币政策空间', 'w-en-monetary-policy')],
  ['w-en-exchange-rate-regime', 'w-en-impossible-trinity'], []),
 ('leverage', '杠杆（金融）', '理论',
  '通过借入资金进行投资的技术，又称 gearing。',
  '杠杆（又称 gearing）指任何涉及借入资金以购买投资的技巧。杠杆放大收益的同时也放大损失，是金融危机中放大脆弱性与传染的重要机制。具体度量与监管口径待核实。',
  [('借入资金投资 → 自有资本撬动更大头寸', 'w-en-leverage'),
   ('资产价格上涨时收益放大 → 吸引更多借贷', 'w-en-leverage'),
   ('价格下跌时损失放大 → 强制去杠杆与抛售', 'w-en-financial-accelerator')],
  [('杠杆收益视角', '杠杆提升资本回报与投资能力', 'w-en-leverage'),
   ('脆弱性视角', '高杠杆在冲击下引发强制平仓与连锁抛售', 'w-en-financial-accelerator')],
  ['w-en-leverage', 'w-en-financial-accelerator'], []),
 ('yield-curve', '收益率曲线', '制度',
  '一组可比债务证券的收益率与其到期期限之间的关系。',
  '收益率曲线展示一组可比债务证券的收益率与到期期限的关系。实践中通常基于单一发行人或同一市场板块构建，以使信用质量等特征尽量接近，例如美国政府债券（国债）曲线。曲线形态被用于观察市场对利率与增长的预期。具体解读待核实。',
  [('不同期限债券的收益率 → 连成曲线', 'w-en-yield-curve'),
   ('曲线形态（陡峭/平坦/倒挂）反映期限溢价与预期', 'w-en-yield-curve'),
   ('形态变化被视为经济与政策预期的信号（解读存在争议）', 'w-en-interest-rate')],
  [('预期理论视角', '长端收益率反映市场对未来短期利率的预期', 'w-en-yield-curve'),
   ('期限溢价视角', '风险与流动性偏好影响曲线形态', 'w-en-interest-rate')],
  ['w-en-yield-curve', 'w-en-interest-rate'], []),
 ('hedge-fund', '对冲基金', '制度',
  '持有流动资产、运用复杂交易与风险管理技术以追求绝对收益的集合投资基金。',
  '对冲基金是持有流动资产、运用复杂交易与风险管理技术以提升投资表现并使收益与市场风险隔离的集合投资基金，常用卖空、杠杆与衍生品等策略。在美国，监管要求其仅向机构投资者与高净值个人营销。具体监管与规模待核实。',
  [('募集资金形成集合投资池 → 运用多空/杠杆/衍生品策略', 'w-en-hedge-fund'),
   ('追求绝对收益、隔离市场风险', 'w-en-hedge-fund'),
   ('高杠杆运作在压力下可能放大市场波动', 'w-en-leverage')],
  [('绝对收益视角', '灵活策略可在不同市场环境获取收益', 'w-en-hedge-fund'),
   ('系统性风险视角', '高杠杆与集中头寸可能放大冲击', 'w-en-leverage')],
  ['w-en-hedge-fund', 'w-en-leverage'], []),
 ('derivative', '金融衍生品', '制度',
  '买卖双方之间以未来标的交易为内容的合约。',
  '金融衍生品是买方与卖方之间的合约，形式多样，但都包含四个要素：可或必须买卖的标的、必须发生的未来行为、未来交易必须执行的价格，以及该行为必须完成的未来日期。衍生品用于对冲与投机，其对手方与杠杆风险受关注。具体品种待核实。',
  [('双方约定标的、未来行为、价格与日期 → 形成合约', 'w-en-derivative'),
   ('用于对冲风险或投机获利', 'w-en-derivative'),
   ('杠杆与对手方风险在压力下放大传染', 'w-en-credit-default-swap')],
  [('风险管理视角', '衍生品便于对冲与价格发现', 'w-en-derivative'),
   ('系统性风险视角', '不透明与高杠杆可能放大传染', 'w-en-systemic-risk')],
  ['w-en-derivative', 'w-en-systemic-risk'], []),
 ('securitization', '证券化', '制度',
  '将合同债务义务汇集、并把其现金流出售给投资者的金融实践。',
  '证券化是汇集合同债务义务并将其相关现金流出售给投资者的金融实践，所售工具称为证券，包括债券、过手证券与债务抵押债券（CDO）。投资者从底层债务的本息现金流按新融资的资本结构获得偿付：以抵押贷款应收款支撑的称 MBS，以其他应收款支撑的称 ABS。具体结构待核实。',
  [('汇集多笔债务（贷款/应收款）→ 形成资产池', 'w-en-securitization'),
   ('按资本结构发行证券、以底层现金流偿付投资者', 'w-en-securitization'),
   ('底层违约上升 → 证券分层受损、风险传导至投资者', 'w-en-subprime-mortgage-crisis')],
  [('融资/分散视角', '证券化拓宽融资来源、分散风险', 'w-en-securitization'),
   ('复杂性/信息不对称视角', '层层结构与评级依赖放大系统性风险', 'w-en-systemic-risk')],
  ['w-en-securitization', 'w-en-subprime-mortgage-crisis'], []),
 ('gdp', '国内生产总值(GDP)', '理论',
  '一定时期内一国（或多国）生产与提供的全部最终商品与服务的市场价值货币度量。',
  '国内生产总值(GDP)是一定时期内一国或多国生产与提供的全部最终商品与服务的总市场价值的货币度量，常用于衡量一国或地区的经济活动。主要构成为消费、政府支出、净出口与投资。GDP 并非整体生活水平或福祉的度量，因为它不考虑收入分配；除以人口得到人均GDP的粗略指标；OECD、IMF等机构各有定义。具体口径待核实。',
  [('消费、政府支出、净出口与投资变动 → GDP 规模变化', 'w-en-gdp'),
   ('任一构成项变化可扩大或收缩经济体规模', 'w-en-gdp'),
   ('GDP 增长不等同于生活水平或就业改善（可能"无就业增长"）', 'w-en-gdp')],
  [('总量核算视角', 'GDP 是衡量经济活动的标准化总量指标', 'w-en-gdp'),
   ('福利/分配批判视角', 'GDP 不计收入分配与福祉，不能代表生活水平', 'w-en-gdp')],
  ['w-en-gdp', 'w-en-recession'], []),
 ('liquidity', '市场流动性', '理论',
  '市场使个体或机构能迅速买卖资产而不引起价格剧烈变化的特性。',
  '市场流动性指市场的一种特性：个体或企业能够迅速买入或卖出资产而不致资产价格发生剧烈变化。流动性涉及"能卖出什么价格"与"多快能卖出"之间的权衡：流动性好的市场权衡温和，流动性差的市场须折价才能快速出售。现金被视为最具流动性的资产。具体度量待核实。',
  [('买卖双方深度充足 → 大额交易对价格冲击小', 'w-en-liquidity'),
   ('流动性不足 → 快速出售须接受折价', 'w-en-liquidity'),
   ('压力下流动性骤降 → 抛售与价格螺旋', 'w-en-credit-crunch')],
  [('市场微观结构视角', '流动性与市场深度、买卖价差相关', 'w-en-liquidity'),
   ('流动性危机视角', '流动性可在压力下瞬间枯竭并放大冲击', 'w-en-credit-crunch')],
  ['w-en-liquidity', 'w-en-credit-crunch'], []),
 ('financial-accelerator', '金融加速器', '理论',
  '经济的不利冲击被恶化的金融市场条件所放大的机制。',
  '金融加速器是宏观经济学中的机制：对经济的不利冲击可能被不断恶化的金融市场条件所放大；更广泛地说，实体经济与金融市场的不利状况会相互传导，加深金融与宏观下行。该机制解释了金融摩擦如何放大周期波动。具体模型待核实。',
  [('不利冲击 → 资产净值下降、外部融资溢价上升', 'w-en-financial-accelerator'),
   ('融资成本上升 → 投资与产出进一步收缩', 'w-en-financial-accelerator'),
   ('实体与金融相互强化 → 下行被放大', 'w-en-credit-crunch')],
  [('金融摩擦视角', '信贷市场摩擦使冲击被放大而非自我修正', 'w-en-financial-accelerator'),
   ('周期放大视角', '金融条件与实体经济相互反馈', 'w-en-business-cycle')],
  ['w-en-financial-accelerator', 'w-en-business-cycle'], []),
 ('credit-rating', '信用评级', '制度',
  '对潜在债务人信用风险的评估，即预测其偿债或违约的能力。',
  '信用评级是对潜在债务人信用风险的评估，即预测该债务人偿还债务或违约的能力。评级由评级机构基于定性定量信息作出，包括债务人提供的信息以及分析师获取的其他非公开信息。评级在金融危机中的准确性与利益冲突受到质疑。具体方法待核实。',
  [('评级机构收集定性定量信息 → 评估违约概率', 'w-en-credit-rating'),
   ('给出评级 → 影响融资成本与投资者配置', 'w-en-credit-rating'),
   ('评级失准或骤然下调 → 放大市场波动', 'w-en-systemic-risk')],
  [('信息中介视角', '评级降低信息不对称、便利融资', 'w-en-credit-rating'),
   ('批判视角', '模型失准、顺周期下调与利益冲突放大风险', 'w-en-systemic-risk')],
  ['w-en-credit-rating', 'w-en-systemic-risk'], []),
 ('money-supply', '货币供应量', '货币',
  '公众在某一时点持有的货币总量。',
  '货币供应量指公众在某一特定时点持有的货币总量。"货币"有多个定义，标准度量通常包括流通中现金与活期存款；数据一般由该国统计机构或中央银行记录并发布。实证度量常按涵盖范围命名为 M1、M2、M3 等，具体定义因国而异，部分取决于各国金融制度传统。具体口径待核实。',
  [('中央银行与银行体系创造货币 → 公众持有量变化', 'w-en-money-supply'),
   ('按定义范围形成 M1/M2/M3 等层次', 'w-en-money-supply'),
   ('货币量变化影响物价与经济活动', 'w-en-inflation')],
  [('货币主义视角', '货币供应量是物价与名义收入的关键决定因素', 'w-en-inflation'),
   ('内生货币视角', '货币供给部分由信贷需求内生决定', 'w-en-monetary-policy')],
  ['w-en-money-supply', 'w-en-inflation'], []),
 ('interest-rate', '利率', '货币',
  '每期应付利息占所借贷（或存入）金额的比例。',
  '利率是每期应付利息相对于所借贷、存入或借出金额的比例，计息期通常为一年，不足一年时常年化。除利率外，本金、复利频率与时间长度共同决定利息总额。利率是货币政策传导与资产定价的核心变量。具体口径待核实。',
  [('资金供求与央行政策 → 决定利率水平', 'w-en-interest-rate'),
   ('利率影响借贷、投资与资产估值', 'w-en-monetary-policy'),
   ('利率变动传导至汇率、房价与总需求', 'w-en-fiscal-policy')],
  [('资金供求视角', '利率由可贷资金供求决定', 'w-en-interest-rate'),
   ('政策/期限结构视角', '央行政策利率与期限溢价共同塑造利率曲线', 'w-en-yield-curve')],
  ['w-en-interest-rate', 'w-en-yield-curve'], []),
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
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据、学派细节与实际应用待核实补充。【续作M】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

# sources.json 补充
sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r31_concepts.json', encoding='utf-8'))
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

# coverage
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
