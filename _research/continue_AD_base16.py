# -*- coding: utf-8 -*-
"""续作AD：新增16条基础经济学概念(L2,据REST摘要)。"""
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
 ('liquidity-preference', '流动性偏好', '理论',
  '对货币的需求，即把货币视为流动性的需求；由凯恩斯在1936年《通论》中提出。',
  '在宏观经济理论中，流动性偏好是对货币的需求（把货币视为流动性）。该概念由约翰·梅纳德·凯恩斯在其《就业、利息和货币通论》（1936年）中首先提出，用以解释利率与持币行为。它是流动性陷阱概念的理论基础。具体论述待核实。',
  [('持有货币提供流动性便利 → 形成货币需求', 'w-en-liquidity-preference'),
   ('利率是放弃流动性的补偿 → 利率与持币需求反向', 'w-en-liquidity-preference'),
   ('利率极低时流动性偏好近绝对 → 流动性陷阱', 'w-en-liquidity-trap')],
  [('凯恩斯视角', '流动性偏好决定利率与持币行为', 'w-en-liquidity-preference'),
   ('货币数量视角', '货币需求相对稳定、由收入与利率决定', 'w-en-quantity-theory-money')],
  ['w-en-liquidity-preference', 'w-en-liquidity-trap'], []),
 ('velocity-of-money', '货币流通速度', '货币',
  '一单位货币在给定时期内用于购买商品与服务的次数。',
  '货币流通速度衡量一单位货币在给定时期内被用于购买商品与服务的次数。换言之，它表示单位时间内货币转手或流通到他人手中的次数。流通速度的变动会显著影响货币供给与名义收入之间的关系。具体测算待核实。',
  [('货币转手越快 → 同量货币支持更多交易', 'w-en-velocity-of-money'),
   ('流通速度上升 → 货币供给的扩张效应被放大', 'w-en-velocity-of-money'),
   ('速度不稳 → 货币目标制的有效性下降', 'w-en-money-supply')],
  [('货币数量视角', '假设速度稳定则货币量与物价直接相关', 'w-en-quantity-theory-money'),
   ('凯恩斯视角', '速度可变、受流动性偏好影响', 'w-en-liquidity-preference')],
  ['w-en-velocity-of-money', 'w-en-money-supply'], []),
 ('fisher-equation', '费雪方程式', '理论',
  '表达名义利率、实际利率与通胀之间关系的方程式，以欧文·费雪命名。',
  '在金融数学与经济学中，费雪方程式表达名义利率、实际利率与通胀之间的关系。它以美国经济学家欧文·费雪（Irving Fisher）命名。该关系是区分名义与实际利率、分析通胀对债务影响的基础工具。具体形式待核实。',
  [('名义利率 = 实际利率 + 预期通胀（近似）', 'w-en-fisher-equation'),
   ('通胀上升 → 名义利率随之调整', 'w-en-fisher-equation'),
   ('未预期的通胀 → 实际利率下降、债权人受损', 'w-en-debt-deflation')],
  [('费雪视角', '名义利率反映预期通胀', 'w-en-fisher-equation'),
   ('债务通缩视角', '未预期通缩抬高实际利率与实际债务', 'w-en-debt-deflation')],
  ['w-en-fisher-equation', 'w-en-interest-rate'], []),
 ('greshams-law', '格雷欣法则', '货币',
  '货币学原理："劣币驱逐良币"——成色低的货币把成色高的货币挤出流通。',
  '格雷欣法则（亦称格雷欣-哥白尼法则）是一条货币学原理，指出"劣币驱逐良币"。例如，若流通中有两种含不同价值金属的硬币、却按同一面值被接受，则人们会保留高价值硬币而花掉低价值硬币。该法则常用于解释货币贬值时期的行为。具体适用条件待核实。',
  [('两种货币按同一面值流通 → 高价值货币被窖藏', 'w-en-greshams-law'),
   ('低价值货币留在流通中 → 劣币驱逐良币', 'w-en-greshams-law'),
   ('铸币成色下降 → 货币信用与物价受影响', 'w-en-kipper-wipper-1618')],
  [('货币成色视角', '成色差异导致良币退出流通', 'w-en-greshams-law'),
   ('法定比价视角', '若比价合理则未必发生驱逐', 'w-en-monetary-policy')],
  ['w-en-greshams-law', 'w-en-money-supply'], []),
 ('opportunity-cost', '机会成本', '理论',
  '在资源有限、须在互斥选项间抉择时，所放弃的最佳替代方案的价值。',
  '在微观经济理论中，机会成本是一项选择的代价，即在资源有限、须在若干互斥替代方案间作出选择时，所放弃的最佳替代方案的价值。它是理解资源配​​置与比较优势的基础概念。具体应用待核实。',
  [('资源有限且用途互斥 → 选择一种即放弃其他', 'w-en-opportunity-cost'),
   ('放弃的最佳替代方案价值即机会成本', 'w-en-opportunity-cost'),
   ('构成比较优势与专业化决策的基础', 'w-en-comparative-advantage')],
  [('微观决策视角', '机会成本是理性选择的核心计价', 'w-en-opportunity-cost'),
   ('贸易视角', '相对机会成本差异形成比较优势', 'w-en-comparative-advantage')],
  ['w-en-opportunity-cost', 'w-en-comparative-advantage'], []),
 ('externality', '外部性', '理论',
  '一方活动对未参与第三方造成的成本或收益。',
  '在经济学中，外部性是一项活动对未参与的第三方所产生的成本或收益。许多外部性可视为未定价的组成部分，涉及消费或生产环节。负外部性（如污染）导致市场供给过多，正外部性导致供给不足，是政府干预的理由之一。具体应用待核实。',
  [('私人活动产生未计入价格的第三方成本或收益', 'w-en-externality'),
   ('私人决策未考虑外部性 → 资源配置偏离社会最优', 'w-en-externality'),
   ('需征税、补贴或管制内部化外部性', 'w-en-public-good')],
  [('庇古视角', '以税收/补贴使外部成本内部化', 'w-en-externality'),
   ('科斯视角', '明确产权与低交易成本下可私人协商解决', 'w-en-public-good')],
  ['w-en-externality', 'w-en-public-good'], []),
 ('public-good', '公共品', '理论',
  '同时具有非排他性与非竞争性、通常由政府提供并以税收支付的商品或服务。',
  '在经济学中，公共品是同时具备非排他性与非竞争性的商品、产品或服务，通常由政府提供并通过税收支付。一个人对它的使用既不阻碍他人获取，也不减少他人可用的数量。公共品难以由市场有效提供，是政府职能的理论依据之一。具体应用待核实。',
  [('非排他 + 非竞争 → 私人难以收费供给', 'w-en-public-good'),
   ('搭便车问题 → 市场供给不足', 'w-en-public-good'),
   ('通常由政府提供并以税收融资', 'w-en-public-good')],
  [('公共品视角', '公共品需政府提供或公共融资', 'w-en-public-good'),
   ('市场视角', '可通过技术或制度设计部分引入排他性', 'w-en-externality')],
  ['w-en-public-good', 'w-en-externality'], []),
 ('tragedy-commons', '公地悲剧', '理论',
  '共享资源可惠及个人却由群体承担成本时，个人理性地过度使用、集体却受损的现象。',
  '公地悲剧是这样一种观点：当一项资源被共享、且可为个人带来收益而以群体为代价时，对个人而言过度使用该资源是理性的，尽管这在集体层面导致资源耗竭。该概念广泛用于分析资源与环境治理。具体应用待核实。',
  [('资源共享、使用成本由群体分摊 → 个人收益大于个人成本', 'w-en-tragedy-commons'),
   ('个体理性导致过度使用 → 资源退化', 'w-en-tragedy-commons'),
   ('需产权界定、管制或集体治理机制', 'w-en-public-good')],
  [('哈丁视角', '缺乏约束时共享资源必然过度使用', 'w-en-tragedy-commons'),
   ('奥斯特罗姆视角', '社区自治制度可有效治理公地', 'w-en-public-good')],
  ['w-en-tragedy-commons', 'w-en-public-good'], []),
 ('marginal-utility', '边际效用', '理论',
  '一单位商品或服务所带来的效用变化，可为正、负或零。',
  '在主流经济学中，边际效用指一单位商品或服务所带来的效用变化。边际效用可为正、负或零；负边际效用意味着每多消费一单位反而降低效用。边际效用递减是需求曲线向下倾斜的基础之一。具体论述待核实。',
  [('消费增加一单位 → 效用发生边际变化', 'w-en-marginal-utility'),
   ('边际效用递减 → 愿付价格随数量下降', 'w-en-marginal-utility'),
   ('边际效用为零时总效用最大', 'w-en-marginal-utility')],
  [('边际主义视角', '价值由边际效用决定而非总效用', 'w-en-marginal-utility'),
   ('古典劳动价值视角', '价值源于生产所需的劳动', 'w-en-classical-economics')],
  ['w-en-marginal-utility', 'w-en-classical-economics'], []),
 ('elasticity', '弹性', '理论',
  '一个经济变量对另一变量变化的响应程度。',
  '在经济学中，弹性衡量一个经济变量对另一个变量变化的响应程度。例如，若某商品需求的价格弹性为−2，则价格上涨10%会使需求量下降20%。弹性是分析税收归宿、价格管制与市场结构影响的关键工具。具体测算待核实。',
  [('价格或收入变动 → 需求量相应变化', 'w-en-elasticity'),
   ('以弹性系数衡量响应幅度', 'w-en-elasticity'),
   ('弹性差异决定税负归宿与政策效果', 'w-en-fiscal-policy')],
  [('马歇尔视角', '弹性刻画需求与供给的响应程度', 'w-en-elasticity'),
   ('行为视角', '参照点与损失厌恶使弹性非对称', 'w-en-behavioral-finance')],
  ['w-en-elasticity', 'w-en-opportunity-cost'], []),
 ('invisible-hand', '看不见的手', '理论',
  '亚当·斯密提出的比喻：自由市场有时使自利者在无意中促进公共利益。',
  '看不见的手是由苏格兰经济学家与道德哲学家亚当·斯密引出的比喻，描述自由市场有时会为自利者创造出无意中服务公共利益的激励。该比喻成为自由市场经济学的重要象征，但其确切含义与适用范围存在学术争论。具体论述待核实。',
  [('个体追求自身利益 → 通过市场交换参与分工', 'w-en-invisible-hand'),
   ('价格信号协调分散决策 → 资源被配置到需求处', 'w-en-invisible-hand'),
   ('无意中促进公共利益（比喻，非严格定理）', 'w-en-invisible-hand')],
  [('古典自由市场视角', '市场自发协调优于人为干预', 'w-en-invisible-hand'),
   ('凯恩斯/批判视角', '市场失灵与外部性使自发协调不充分', 'w-en-externality')],
  ['w-en-invisible-hand', 'w-en-classical-economics'], []),
 ('division-of-labour', '分工', '理论',
  '将经济体系或组织中的任务分离，使参与者得以专业化。',
  '分工是任何经济体系或组织中任务的分离，以便参与者实现专业化。个人、组织与国家被赋予或获得专业化能力。分工提高生产率，但也增加协调成本与相互依赖。它是斯密《国富论》开篇的核心论题。具体论述待核实。',
  [('任务分离 → 参与者专业化', 'w-en-division-of-labour'),
   ('熟练度与效率提升 → 生产率提高', 'w-en-division-of-labour'),
   ('协调成本与相互依赖上升 → 需要市场与组织', 'w-en-invisible-hand')],
  [('斯密视角', '分工受市场范围限制、是财富增长源泉', 'w-en-division-of-labour'),
   ('管理视角', '过度分工带来协调与激励问题', 'w-en-principal-agent')],
  ['w-en-division-of-labour', 'w-en-invisible-hand'], []),
 ('laissez-faire', '自由放任', '理论',
  '不加限制、任其自然发生；在金融领域指私人间交易不受管制。',
  '自由放任意味着不加限制地任事情发生，不论潜在后果如何。在金融领域，它指一种经济体系，其中私人个体之间的交易不受任何形式的（政府）管制。该理念与自由市场经济学密切相关，其在金融稳定上的适用性存在争论。具体论述待核实。',
  [('减少政府干预 → 私人交易依自身利益进行', 'w-en-laissez-faire'),
   ('市场自发协调被视为更有效率', 'w-en-invisible-hand'),
   ('但可能忽视外部性与系统性风险', 'w-en-externality')],
  [('自由主义视角', '最少干预释放市场活力', 'w-en-laissez-faire'),
   ('审慎监管视角', '金融领域的外部性与系统性风险需要监管', 'w-en-macroprudential')],
  ['w-en-laissez-faire', 'w-en-invisible-hand'], []),
 ('savings-glut', '全球储蓄过剩', '理论',
  '意愿储蓄超过意愿投资的情形；伯南克在2005年对此表达关切。',
  '全球储蓄过剩是一种意愿储蓄超过意愿投资的情形。到2005年，时任美国联邦储备委员会主席本·伯南克对（全球储蓄的）"显著增加"表达了关切。该假说被用来解释长期利率偏低与资本跨境流动（尤其流向美国）。具体论述待核实。',
  [('多国高储蓄 + 投资需求不足 → 全球储蓄过剩', 'w-en-savings-glut'),
   ('过剩储蓄流向安全资产 → 长期利率被压低', 'w-en-savings-glut'),
   ('与美国经常账户赤字相联 → 全球失衡', 'w-en-global-imbalances')],
  [('储蓄过剩视角', '全球储蓄过剩压低利率、推动资本流向美国', 'w-en-savings-glut'),
   ('替代视角', '美国自身政策与金融深化是主因', 'w-en-global-imbalances')],
  ['w-en-savings-glut', 'w-en-global-imbalances'], []),
 ('global-imbalances', '全球失衡', '货币',
  '一些国家（相对其他国家）持有更多资产、经常账户长期失衡的状况。',
  '全球失衡指一些国家拥有的资产多于其他国家的状况。理论上，当经常账户平衡时其值为零：资本流入与流出相互抵消。持续的大规模顺差与逆差构成全球失衡，被认为与金融危机风险相关。具体论述待核实。',
  [('部分国家长期经常账户顺差、他国逆差', 'w-en-global-imbalances'),
   ('顺差国资本流向逆差国 → 资产与负债格局失衡', 'w-en-global-imbalances'),
   ('调整过程可能伴随汇率与资本流动冲击', 'w-en-sudden-stop')],
  [('失衡视角', '储蓄-投资失衡通过资本流动体现', 'w-en-global-imbalances'),
   ('储蓄过剩视角', '过剩储蓄是失衡的来源之一', 'w-en-savings-glut')],
  ['w-en-global-imbalances', 'w-en-balance-of-payments'], []),
 ('reserve-currency', '储备货币', '货币',
  '被政府、中央银行或其他货币当局作为外汇储备一部分持有的外币。',
  '储备货币是被政府、中央银行或其他货币当局作为外汇储备的一部分而持有的外币。储备货币可用于国际交易、国际结算与价值储藏。美元是最主要的储备货币，欧元次之。储备货币地位带来特权也带来责任（见特里芬难题）。具体格局待核实。',
  [('某货币被广泛用于国际交易 → 各国愿意持有', 'w-en-reserve-currency'),
   ('作为外汇储备 → 发行国获得低成本融资', 'w-en-foreign-exchange-reserves'),
   ('储备地位带来特里芬式两难', 'w-en-triffin-dilemma')],
  [('储备地位视角', '储备货币带来铸币税与融资优势', 'w-en-reserve-currency'),
   ('特里芬视角', '对外供给与国内纪律存在冲突', 'w-en-triffin-dilemma')],
  ['w-en-reserve-currency', 'w-en-triffin-dilemma'], []),
]

for row in D:
    eid, title, cat, ol, ov, causal, schools, srcs, _kd = row
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': [],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in causal],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in schools],
        'policy_response': [],
        'comparison': '经济学基础概念，与其他概念互补；具体争论待核实。',
        'svg': svg(title, [causal[0][0][:12], causal[1][0][:12], causal[2][0][:12]]),
        'sources': list(dict.fromkeys(srcs)), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作AD】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r49_concepts.json', encoding='utf-8'))
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
