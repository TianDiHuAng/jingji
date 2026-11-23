# -*- coding: utf-8 -*-
"""续作Q：新增16条金融市场/风险/数字资产概念(L2,据REST摘要)。"""
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
 ('efficient-market', '有效市场假说', '理论',
  '资产价格已反映全部可得信息的假说，因而不可能持续获得风险调整后的超额收益。',
  '有效市场假说（EMH）是金融经济学中的假说：资产价格反映全部可得信息。其直接含义是，由于市场价格应只对新信息作出反应，因此不可能在风险调整基础上持续"战胜市场"。该假说与行为金融的解释存在长期争论。具体形式（弱式/半强式/强式）待核实。',
  [('全部可得信息被迅速反映 → 价格接近基本面价值', 'w-en-efficient-market'),
   ('仅新信息驱动价格变动 → 难以预测', 'w-en-efficient-market'),
   ('无法持续获得风险调整后超额收益', 'w-en-efficient-market')],
  [('有效市场视角', '价格已反映信息，主动管理难有持续超额收益', 'w-en-efficient-market'),
   ('行为金融视角', '认知偏差与套利限制使价格长期偏离', 'w-en-behavioral-finance')],
  ['w-en-efficient-market', 'w-en-behavioral-finance'], []),
 ('behavioral-finance', '行为经济学与行为金融', '理论',
  '研究个人或机构决策中的心理因素、以及这些决策如何偏离传统理论预测的学科。',
  '行为经济学研究个人或机构决策中涉及的心理因素，以及这些决策如何偏离传统经济理论所隐含的预测。在金融领域（行为金融）中，其用于解释羊群行为、过度自信、损失厌恶等导致的价格偏离。具体理论待核实。',
  [('认知偏差与情绪 → 决策偏离理性最优', 'w-en-behavioral-finance'),
   ('系统性偏差在市场中累积 → 价格偏离基本面', 'w-en-herd-behavior'),
   ('形成泡沫或恐慌等非理性现象', 'w-en-speculative-bubble')],
  [('行为视角', '心理因素系统影响决策与资产价格', 'w-en-behavioral-finance'),
   ('有效市场视角', '套利力量会纠正偏离', 'w-en-efficient-market')],
  ['w-en-behavioral-finance', 'w-en-herd-behavior'], []),
 ('minsky-moment', '明斯基时刻', '理论',
  '资产价值突然大幅崩塌、标志信贷市场或商业活动周期增长阶段终结的时刻。',
  '明斯基时刻指资产价值突然而重大的崩塌，标志着信贷市场或商业活动的周期增长阶段结束。该概念源自海曼·明斯基的金融不稳定假说，强调繁荣期杠杆与投机融资的累积如何埋下崩溃的种子。具体机制待核实。',
  [('繁荣期杠杆与投机性融资上升 → 脆弱性累积', 'w-en-minsky-theory'),
   ('现金流无法覆盖债务偿付 → 抛售资产', 'w-en-minsky-moment'),
   ('资产价值突然崩塌 → 周期增长阶段终结', 'w-en-financial-crisis')],
  [('金融不稳定假说视角', '稳定本身孕育不稳定，繁荣埋下危机', 'w-en-minsky-theory'),
   ('有效市场视角', '价格反映基本面，系统性错配难以持续存在', 'w-en-efficient-market')],
  ['w-en-minsky-moment', 'w-en-minsky-theory'], []),
 ('ponzi-scheme', '庞氏骗局', '其他',
  '以新投资者的资金支付早期投资者"收益"的欺诈形式。',
  '庞氏骗局是一种欺诈形式：它吸引投资者，并用来自较新投资者的资金向较早投资者支付表面上的利润。该骗局以意大利诈骗者 Charles Ponzi 命名，通过虚假暗示利润来自合法经营活动（或夸大收益）来误导投资者。具体案例待核实。',
  [('以高回报承诺吸引投资者 → 资金持续流入', 'w-en-ponzi-scheme'),
   ('用新资金支付早期投资者"收益" → 制造盈利假象', 'w-en-ponzi-scheme'),
   ('新增资金枯竭 → 骗局崩解、投资者损失', 'w-en-ponzi-scheme')],
  [('欺诈视角', '本质是资金链骗局而非投资经营', 'w-en-ponzi-scheme'),
   ('监管/投资者保护视角', '信息披露与监管可提前识别异常回报', 'w-en-market-manipulation')],
  ['w-en-ponzi-scheme', 'w-en-market-manipulation'], []),
 ('insider-trading', '内幕交易', '制度',
  '基于公司重大非公开信息买卖其证券的行为，多数国家视为违法。',
  '内幕交易指基于有关公司的重大非公开信息，买卖该公司股票或其他证券的行为。在许多国家，基于内幕信息交易属违法行为。禁止内幕交易的理由因国家与地区而异：有人认为它对其他投资者不公平。具体规则待核实。',
  [('内部人掌握重大非公开信息 → 信息不对称', 'w-en-insider-trading'),
   ('据此交易获取不正当优势', 'w-en-insider-trading'),
   ('损害市场公平与信心 → 需监管禁止', 'w-en-market-manipulation')],
  [('公平视角', '内幕交易对其他投资者不公平、损害信心', 'w-en-insider-trading'),
   ('市场效率视角', '有观点认为内幕交易加速信息入价', 'w-en-efficient-market')],
  ['w-en-insider-trading', 'w-en-market-manipulation'], []),
 ('market-manipulation', '市场操纵', '制度',
  '故意改变证券供求以影响其价格的行为。',
  '在经济学与金融学中，市场操纵指某人故意改变某一证券的供给或需求以影响其价格，手段可包括散布误导性信息、执行误导性交易、或操纵报价与价格。市场操纵破坏价格发现与市场信心，为证券监管所禁止。具体形式待核实。',
  [('故意改变供求或散布误导信息 → 影响价格', 'w-en-market-manipulation'),
   ('价格偏离基本面、误导其他投资者', 'w-en-market-manipulation'),
   ('损害价格发现与市场信心 → 需监管执法', 'w-en-insider-trading')],
  [('市场完整性视角', '操纵破坏价格发现与公平', 'w-en-market-manipulation'),
   ('监管执法视角', '需监测异常交易与信息披露', 'w-en-bank-regulation')],
  ['w-en-market-manipulation', 'w-en-bank-regulation'], []),
 ('capital-requirement', '资本充足要求', '制度',
  '银行在审慎框架下必须遵守的资本规则与指引，是银行监管的核心组成。',
  '资本充足要求指银行在多数现行银行审慎框架下必须遵守的规则与指引，具体形式因司法辖区而异。它们构成银行监管与监督的核心组成部分，旨在使银行以自有资本吸收损失、降低失败风险。具体标准待核实。',
  [('监管设定最低资本比率 → 约束银行资产扩张', 'w-en-capital-requirement'),
   ('以自有资本吸收损失 → 降低 insolvency 风险', 'w-en-capital-requirement'),
   ('维护银行体系稳定、减少系统性风险', 'w-en-systemic-risk')],
  [('审慎视角', '资本要求提升损失吸收能力', 'w-en-capital-requirement'),
   ('成本视角', '更高资本要求可能抑制信贷与增长', 'w-en-basel-accords')],
  ['w-en-capital-requirement', 'w-en-basel-accords'], []),
 ('credit-risk', '信用风险', '理论',
  '借款人未能偿还贷款或履行债务义务的可能性。',
  '信用风险是借款人未能偿还贷款或履行贷款义务的可能性。对贷款方而言，该风险包括利息与本金的延迟或损失，导致现金流中断与催收成本上升；损失可能是全部或部分的。在有效市场中，较高信用风险将对应更高的风险溢价。具体度量待核实。',
  [('借款人偿付能力或意愿不足 → 违约可能', 'w-en-credit-risk'),
   ('贷款方遭受利息与本金损失、催收成本上升', 'w-en-credit-risk'),
   ('以更高利率与抵押要求定价风险', 'w-en-credit-rating')],
  [('风险定价视角', '信用风险由利率与担保结构定价', 'w-en-credit-risk'),
   ('评级/信息视角', '以评级与信息生产缓释不对称', 'w-en-credit-rating')],
  ['w-en-credit-risk', 'w-en-credit-rating'], []),
 ('value-at-risk', '风险价值(VaR)', '制度',
  '在正常市场条件下、给定时间期内投资组合可能损失多少的风险度量。',
  '风险价值（VaR）是衡量投资或资本损失风险的指标，估计在正常市场条件下、某一时间期（如一天）内一组投资可能损失多少。金融机构与监管者常用 VaR 估算覆盖潜在损失所需的资产数量。其在极端情形下的局限受到批评。具体方法待核实。',
  [('以历史波动与相关性建模 → 估计损失分布', 'w-en-value-at-risk'),
   ('给出给定置信度下的最大可能损失', 'w-en-value-at-risk'),
   ('用于确定资本与限额；极端情形下可能低估', 'w-en-credit-risk')],
  [('风险管理视角', 'VaR 提供简洁统一的风险度量', 'w-en-value-at-risk'),
   ('批判视角', '尾部风险与相关性突变时 VaR 严重低估', 'w-en-systemic-risk')],
  ['w-en-value-at-risk', 'w-en-systemic-risk'], []),
 ('capm', '资本资产定价模型(CAPM)', '理论',
  '用于确定资产理论合理要求回报率、以构建充分分散组合的模型。',
  '资本资产定价模型（CAPM）是金融学中用于确定资产理论上合理的要求回报率的模型，以便决定是否将资产加入充分分散的投资组合。模型考虑资产对不可分散风险的敏感度（通常以贝塔系数表示）。其简化假设受到批评。具体推导待核实。',
  [('区分可分散与不可分散风险 → 只有系统性风险获补偿', 'w-en-capm'),
   ('以贝塔衡量系统性风险敏感度', 'w-en-capm'),
   ('据无风险利率与风险溢价确定要求回报率', 'w-en-capm')],
  [('均衡资产定价视角', '只有系统性风险应获得风险溢价', 'w-en-capm'),
   ('行为/实证批判视角', '实际收益与模型预测存在系统性偏离', 'w-en-behavioral-finance')],
  ['w-en-capm', 'w-en-behavioral-finance'], []),
 ('black-scholes', '布莱克-斯科尔斯模型', '理论',
  '描述含衍生品金融市场动态的数学模型，可导出期权定价公式。',
  '布莱克-斯科尔斯（或布莱克-斯科尔斯-默顿）模型是描述含衍生工具金融市场动态的数学模型。由模型中的抛物型偏微分方程（布莱克-斯科尔斯方程）可导出布莱克-斯科尔斯公式，给出期权价格的理论估计。该模型依赖若干理想化假设，在极端市场中局限明显。具体推导待核实。',
  [('假设标的资产价格服从几何布朗运动 → 建立偏微分方程', 'w-en-black-scholes'),
   ('通过复制组合与无套利 → 导出期权定价公式', 'w-en-black-scholes'),
   ('为衍生品定价与对冲提供基准（假设偏离时误差增大）', 'w-en-derivative')],
  [('无套利定价视角', '可复制组合决定衍生品唯一合理价格', 'w-en-black-scholes'),
   ('实证批判视角', '波动率微笑与尾部事件偏离模型假设', 'w-en-value-at-risk')],
  ['w-en-black-scholes', 'w-en-derivative'], []),
 ('financial-deepening', '金融深化', '理论',
  '金融服务供给的增加，包括服务种类更广与不同社会经济群体更易获得。',
  '金融深化是经济学家使用的术语，指金融服务供给的增加，既可指服务选择更广，也可指不同社会经济群体获得更好的可及性。金融深化会对个人与社会的经济状况产生影响。其与增长的关系及过度深化的风险存在争论。具体度量待核实。',
  [('金融服务供给增加 → 更多主体获得信贷与储蓄工具', 'w-en-financial-deepening'),
   ('改善资源配置与风险管理 → 支持增长', 'w-en-financial-deepening'),
   ('过快深化或监管不足 → 累积金融脆弱性', 'w-en-systemic-risk')],
  [('发展视角', '金融深化改善配置、支持增长与减贫', 'w-en-financial-deepening'),
   ('审慎视角', '过度深化与监管滞后会累积风险', 'w-en-macroprudential')],
  ['w-en-financial-deepening', 'w-en-macroprudential'], []),
 ('microfinance', '微型金融', '制度',
  '向个人与小企业（尤其低收入、难以获得常规银行服务者）提供金融服务。',
  '微型金融是向个人与小企业——特别是收入较低、获得常规银行及相关金融服务渠道有限者——提供金融服务。其涵盖小额信贷、储蓄、支票账户、小额保险与支付系统等服务。其在减贫上的效果与可持续性存在讨论。具体模式待核实。',
  [('低收入群体缺乏抵押与信用记录 → 难以获得常规银行服务', 'w-en-microfinance'),
   ('以小额信贷、储蓄与小额保险等方式提供金融可及性', 'w-en-microfinance'),
   ('支持微型经营与平滑消费（效果存在讨论）', 'w-en-financial-deepening')],
  [('普惠视角', '微型金融拓展金融可及性、支持微型创业', 'w-en-microfinance'),
   ('批判视角', '过度负债与高利率可能损害借款人', 'w-en-credit-risk')],
  ['w-en-microfinance', 'w-en-financial-deepening'], []),
 ('cryptocurrency', '加密货币', '货币',
  '使用分布式账本（区块链）技术实现安全交易的数字资产。',
  '加密货币是一种数字资产，使用分布式账本或区块链技术以实现安全交易。其价格波动剧烈，监管框架在各国差异很大。加密货币不具备法定货币地位（在多数辖区），也不具备中央银行的支持。具体机制与监管待核实。',
  [('分布式账本记录交易 → 无需中心化机构确认', 'w-en-cryptocurrency'),
   ('密码学保障交易安全与所有权', 'w-en-cryptocurrency'),
   ('价格波动剧烈、监管差异大 → 风险与争议', 'w-en-stablecoin')],
  [('技术创新视角', '分布式账本可降低中介成本', 'w-en-cryptocurrency'),
   ('货币/监管视角', '缺乏最后贷款人与价格锚，波动与风险突出', 'w-en-monetary-policy')],
  ['w-en-cryptocurrency', 'w-en-stablecoin'], []),
 ('stablecoin', '稳定币', '货币',
  '旨在相对特定资产（或资产池/篮子）保持价值稳定的加密货币。',
  '稳定币是一种加密货币，旨在相对某一特定资产、资产池或资产篮子保持价值稳定；指定资产可指法定货币、商品或其他加密货币。尽管名为"稳定"，稳定币并不必然稳定，其依赖各类稳定化工具维持锚定。具体机制与风险待核实。',
  [('以法币/商品/资产篮子作为价值锚 → 设计稳定机制', 'w-en-stablecoin'),
   ('通过储备、算法或抵押维持锚定', 'w-en-stablecoin'),
   ('储备不足或挤兑 → 脱锚与风险外溢', 'w-en-bank-run')],
  [('支付创新视角', '稳定币可提升跨境支付效率', 'w-en-stablecoin'),
   ('货币稳定/监管视角', '储备透明度不足时具挤兑与系统性风险', 'w-en-bank-run')],
  ['w-en-stablecoin', 'w-en-cryptocurrency'], []),
 ('cbdc', '中央银行数字货币(CBDC)', '货币',
  '由中央银行而非私人公司发行的官方货币的数字形式。',
  '中央银行数字货币（CBDC）是官方货币的数字版本，由中央银行而非私人公司创造。与比特币等加密货币不同，CBDC 由国家发行，并可能与实物现金并行流通。据维基条目，截至2024年巴哈马、牙买加与尼日利亚已推出CBDC，另有众多国家在研发或试点。具体进展待核实。',
  [('央行发行数字形式的法定货币 → 直接对公众或银行开放', 'w-en-cbdc'),
   ('与实物现金并行，提升支付效率与普惠', 'w-en-cbdc'),
   ('影响银行体系与货币政策传导（需审慎设计）', 'w-en-monetary-policy')],
  [('支付/普惠视角', 'CBDC 可提升支付效率与金融可及性', 'w-en-cbdc'),
   ('银行中介/隐私视角', '可能挤压存款与引发隐私、脱媒关切', 'w-en-bank-regulation')],
  ['w-en-cbdc', 'w-en-monetary-policy'], []),
]

for eid, title, cat, ol, ov, causal, schools, srcs, kds in D:
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': [],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in causal],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in schools],
        'policy_response': [],
        'comparison': '经济学/金融概念条目，与其他概念互补；具体适用与争论待核实。',
        'svg': svg(title, [causal[0][0][:12], causal[1][0][:12], causal[2][0][:12]]),
        'sources': srcs, 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作Q】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r35_concepts.json', encoding='utf-8'))
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
