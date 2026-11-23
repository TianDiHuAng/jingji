# -*- coding: utf-8 -*-
"""续作AF：新增14条宏观政策与预期概念(L2,据REST摘要)。"""
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
 ('forward-guidance', '前瞻指引', '制度',
  '中央银行运用自身预测影响市场对未来利率水平预期的货币政策工具。',
  '前瞻指引是中央银行运用其货币政策权力、以自身预测来影响市场对未来利率水平预期的一种工具。它通过沟通未来政策路径来引导预期与长期利率，是零利率下限时期的重要非常规工具。其有效性存在讨论。具体实践待核实。',
  [('央行发布未来政策路径指引 → 影响市场预期', 'w-en-forward-guidance'),
   ('预期变化传导至长期利率与资产价格', 'w-en-forward-guidance'),
   ('支持需求（承诺"更长时间保持低利率"）', 'w-en-monetary-policy')],
  [('预期管理视角', '沟通可替代部分实际降息空间', 'w-en-forward-guidance'),
   ('可信度视角', '若不可信则指引无效（时间不一致性）', 'w-en-time-inconsistency')],
  ['w-en-forward-guidance', 'w-en-monetary-policy'], []),
 ('austerity', '紧缩（财政紧缩）', '制度',
  '通过削减支出、增税或两者组合以减少政府预算赤字的政治经济政策。',
  '紧缩是一组旨在通过削减支出、增加税收或两者结合来减少政府预算赤字的政治经济政策。紧缩措施主要有三种类型：增税等。紧缩的支持者强调债务可持续性与信心，批评者强调其对增长的抑制。具体效果待核实。',
  [('政府削减支出或增税 → 预算赤字下降', 'w-en-austerity'),
   ('总需求收缩 → 短期增长放缓', 'w-en-austerity'),
   ('债务/GDP 比率的走向取决于增长与利率的相对变化', 'w-en-debt-crisis')],
  [('紧缩视角', '削减赤字恢复信心与可持续性', 'w-en-austerity'),
   ('反紧缩视角', '衰退期紧缩加深下行、反而推高债务比率', 'w-en-fiscal-multiplier')],
  ['w-en-austerity', 'w-en-fiscal-policy'], []),
 ('structural-adjustment', '结构调整计划(SAP)', '制度',
  'IMF与世界银行向遭遇经济危机的国家提供的贷款，旨在调整该国经济结构。',
  '结构调整计划（SAP）由国际货币基金组织（IMF）与世界银行（WB）向经历经济危机的国家提供贷款构成。其宣称目的是调整该国的经济（结构）。这类计划通常附带政策条件，其效果与社会代价存在长期争议。具体内容待核实。',
  [('国家遭遇经济危机 → 向 IMF/世行求助', 'w-en-structural-adjustment'),
   ('贷款附带结构调整与政策条件', 'w-en-conditionality'),
   ('经济结构改变，但社会代价引发争议', 'w-en-washington-consensus')],
  [('调整视角', '结构改革纠正失衡、恢复可持续增长', 'w-en-structural-adjustment'),
   ('批判视角', '条件苛刻、社会成本高、成效有限', 'w-en-washington-consensus')],
  ['w-en-structural-adjustment', 'w-en-conditionality'], []),
 ('conditionality', '贷款条件性', '制度',
  '对贷款、债务减免或双边援助等利益附加条件以影响受援方政策的做法。',
  '在政治经济学与国际关系中，条件性是对贷款、债务减免或双边援助等利益附加条件的做法。这些条件通常由国际机构（如IMF）施加，用以推动受援国实施特定政策改革。条件性的有效性、所有权与合法性问题存在争论。具体实践待核实。',
  [('国际机构提供贷款 → 附加政策条件', 'w-en-conditionality'),
   ('受援国须实施改革（财政、结构、监管）', 'w-en-conditionality'),
   ('换取资金支持；政策自主性受限（有争议）', 'w-en-structural-adjustment')],
  [('机构视角', '条件确保资金用于纠正失衡', 'w-en-conditionality'),
   ('主权/批判视角', '条件侵蚀政策空间与民主问责', 'w-en-structural-adjustment')],
  ['w-en-conditionality', 'w-en-imf'], []),
 ('debt-overhang', '债务积压', '债务',
  '组织现有债务过重以致难以再融资、即使新借款是能自我偿付的好投资的情形。',
  '债务积压是一种状况：一个组织（或国家）的现有债务如此之大，以致难以再借到更多资金——即使新增借款实际上是一项能自我偿付的良好投资。债务积压使投资不足、抑制增长，是债务危机后复苏乏力的重要解释。具体机制待核实。',
  [('存量债务过重 → 新增融资的收益被债权人索取', 'w-en-debt-overhang'),
   ('潜在债权人担忧被稀释 → 不愿提供新资金', 'w-en-debt-overhang'),
   ('投资不足 → 增长乏力、债务比率难以下降', 'w-en-debt-crisis')],
  [('债务积压视角', '存量债务抑制新投资、形成停滞', 'w-en-debt-overhang'),
   ('重组视角', '减免存量债务可恢复投资激励', 'w-en-debt-restructuring')],
  ['w-en-debt-overhang', 'w-en-debt-crisis'], []),
 ('original-sin', '原罪（经济学）', '货币',
  '多数国家无法以本币在海外借款的情形；由 Eichengreen、Hausmann 与 Panizza 提出。',
  '原罪是经济学文献中的一个术语，由 Barry Eichengreen、Ricardo Hausmann 与 Ugo Panizza 在一系列论文中提出，指"多数国家无法以本国货币在海外借款"的情形。货币错配使这些国家在贬值时承受资产负债表冲击。具体论述待核实。',
  [('国际借贷多以少数储备货币计价 → 新兴市场难用本币借外债', 'w-en-original-sin'),
   ('外币负债与本币收入错配 → 贬值时债务负担骤升', 'w-en-original-sin'),
   ('加剧货币危机与"浮动恐惧"', 'w-en-fear-of-floating')],
  [('原罪视角', '货币错配是新兴市场脆弱性的结构根源', 'w-en-original-sin'),
   ('政策视角', '积累储备或区域货币合作可部分缓解', 'w-en-foreign-exchange-reserves')],
  ['w-en-original-sin', 'w-en-fear-of-floating'], []),
 ('fear-of-floating', '浮动恐惧', '货币',
  '一国不愿采用浮动汇率制、偏好固定汇率的现象，在新兴经济体更常见。',
  '浮动恐惧是一国不愿采用浮动汇率制度（而倾向固定汇率）的犹豫。该现象在新兴经济体中更为相关，尤其在它们近期经历金融危机之后。原因包括对汇率传递型通胀与外币债务的担忧。具体表现待核实。',
  [('外币负债与通胀传导担忧 → 不愿让汇率自由浮动', 'w-en-fear-of-floating'),
   ('倾向于干预或软钉住 → 削弱货币政策独立性', 'w-en-fear-of-floating'),
   ('外汇储备积累与"原罪"互为因果', 'w-en-original-sin')],
  [('浮动恐惧视角', '新兴市场理性地不愿完全浮动', 'w-en-fear-of-floating'),
   ('三元悖论视角', '软钉住牺牲货币政策独立性', 'w-en-impossible-trinity')],
  ['w-en-fear-of-floating', 'w-en-exchange-rate-regime'], []),
 ('rational-expectations', '理性预期', '理论',
  '宏观主体在不确定下形成预期的一组建模假设：主体使用所有相关可得信息。',
  '理性预期是一组描述宏观主体在不确定下如何形成对未来的预期的建模假设。在这些假设下，主体被假定使用所有相关且可得的信息。该假设深刻改变了宏观经济政策分析（见卢卡斯批判），也引发关于其现实性的争论。具体论述待核实。',
  [('主体收集并利用所有可得信息 → 形成无系统偏差的预期', 'w-en-rational-expectations'),
   ('预期影响工资、价格与投资决策', 'w-en-rational-expectations'),
   ('政策效果取决于是否被预期到（政策无效性命题）', 'w-en-lucas-critique')],
  [('理性预期视角', '系统性政策无法稳定产出', 'w-en-rational-expectations'),
   ('行为/凯恩斯视角', '有限理性与信息摩擦使预期偏离', 'w-en-behavioral-finance')],
  ['w-en-rational-expectations', 'w-en-lucas-critique'], []),
 ('lucas-critique', '卢卡斯批判', '理论',
  '认为仅凭历史数据观察到的关系来预测政策变化效果是幼稚的论点。',
  '卢卡斯批判认为，完全依据历史数据（尤其高度加总的历史数据）中观察到的关系来预测经济政策变化的效果是幼稚的。更正式地说，政策变化会改变主体的决策规则，从而使基于旧体制估计的参数失效。该批判深刻影响了宏观计量与政策评估。具体论述待核实。',
  [('政策变化 → 主体预期与行为规则改变', 'w-en-lucas-critique'),
   ('历史数据估计的参数不再适用 → 预测失效', 'w-en-lucas-critique'),
   ('需以结构性模型评估政策', 'w-en-rational-expectations')],
  [('卢卡斯视角', '政策评估须基于结构性参数', 'w-en-lucas-critique'),
   ('实证视角', '简化式模型在短期内仍有参考价值', 'w-en-taylor-rule')],
  ['w-en-lucas-critique', 'w-en-rational-expectations'], []),
 ('time-inconsistency', '动态不一致（时间不一致）', '理论',
  '决策者偏好随时间变化，使某一时点的偏好在另一时点变得不一致的情形。',
  '在经济学中，动态不一致（时间不一致）是一种情形：决策者的偏好随时间发生变化，使某项偏好在另一个时点上变得不一致。这可解释为何政策制定者会违背先前承诺，从而损害信誉——这是央行独立性理论的核心论据之一。具体论述待核实。',
  [('决策者事前宣布最优政策 → 事后有偏离的激励', 'w-en-time-inconsistency'),
   ('公众预期到偏离 → 事前承诺失去可信度', 'w-en-time-inconsistency'),
   ('需规则、独立机构或声誉机制约束', 'w-en-central-bank-independence')],
  [('规则视角', '以规则约束相机抉择、提升可信度', 'w-en-taylor-rule'),
   ('独立性视角', '授权独立央行可缓解通胀偏向', 'w-en-central-bank-independence')],
  ['w-en-time-inconsistency', 'w-en-central-bank-independence'], []),
 ('sticky-prices', '名义刚性（价格/工资粘性）', '理论',
  '名义价格调整缓慢或抗拒变化的情形，亦称价格粘性或工资粘性。',
  '在经济学中，名义刚性（亦称价格粘性或工资粘性）描述名义价格调整缓慢或抗拒变化的情形。完全的名义刚性指价格完全不变。名义刚性是货币政策在短期能够影响实际产出的关键前提，也是新凯恩斯模型的核心假设。具体论述待核实。',
  [('名义价格/工资调整缓慢 → 实际值随名义冲击变化', 'w-en-sticky-prices'),
   ('需求冲击在短期影响产出与就业', 'w-en-sticky-prices'),
   ('货币政策短期非中性', 'w-en-neutrality-of-money')],
  [('新凯恩斯视角', '粘性使短期政策有效', 'w-en-sticky-prices'),
   ('新古典视角', '价格灵活、货币短期亦中性', 'w-en-neutrality-of-money')],
  ['w-en-sticky-prices', 'w-en-menu-cost'], []),
 ('menu-cost', '菜单成本', '理论',
  '企业改变价格时所产生的成本；新凯恩斯经济学用以解释价格粘性。',
  '在经济学中，菜单成本是企业改变其价格时所承担的成本。该概念是对宏观经济中价格粘性的一种微观解释，尤其被新凯恩斯主义经济学家强调。菜单成本的存在使企业不愿频繁调价，从而使名义冲击产生实际影响。具体论述待核实。',
  [('调价需付出成本（重印菜单、通知客户等）', 'w-en-menu-cost'),
   ('企业因此不频繁调价 → 价格呈粘性', 'w-en-menu-cost'),
   ('名义冲击传导为产出波动', 'w-en-sticky-prices')],
  [('新凯恩斯视角', '小额菜单成本可产生显著的宏观粘性', 'w-en-menu-cost'),
   ('灵活价格视角', '数字化降低调价成本、削弱粘性', 'w-en-sticky-prices')],
  ['w-en-menu-cost', 'w-en-sticky-prices'], []),
 ('monetary-transmission', '货币政策传导机制', '理论',
  '货币政策决策通过资产价格、货币市场与总体经济状况等多渠道影响宏观经济的过程。',
  '货币政策传导机制是货币政策决策通过资产价格、货币市场与总体经济状况等多个渠道影响更广泛宏观经济的过程。传导渠道包括利率、信贷、资产价格、汇率与预期等；传导受阻会使政策失效。具体渠道待核实。',
  [('央行调整政策利率 → 货币市场与信贷条件变化', 'w-en-monetary-transmission'),
   ('经利率、信贷、资产价格与汇率渠道传导', 'w-en-monetary-transmission'),
   ('影响投资、消费与净出口 → 产出与物价', 'w-en-monetary-policy')],
  [('利率渠道视角', '以利率影响资本成本', 'w-en-monetary-transmission'),
   ('信贷渠道视角', '银行信贷供给与金融摩擦影响传导', 'w-en-financial-accelerator')],
  ['w-en-monetary-transmission', 'w-en-monetary-policy'], []),
 ('adaptive-expectations', '适应性预期', '理论',
  '人们基于过去发生的情况来形成对未来的预期的一种假说过程。',
  '在经济学中，适应性预期是一种假说过程：人们基于过去发生的情况来形成对未来的预期。与之相对的是理性预期。适应性预期意味着预期调整滞后，可能使通胀等变量呈现惯性。具体论述待核实。',
  [('过去的结果 → 作为形成未来预期的依据', 'w-en-adaptive-expectations'),
   ('预期调整滞后 → 变量呈现惯性', 'w-en-adaptive-expectations'),
   ('（对比）理性预期则利用全部可得信息', 'w-en-rational-expectations')],
  [('适应性视角', '预期基于历史、调整缓慢', 'w-en-adaptive-expectations'),
   ('理性预期视角', '主体利用全部信息、不犯系统错误', 'w-en-rational-expectations')],
  ['w-en-adaptive-expectations', 'w-en-rational-expectations'], []),
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
        'comparison': '宏观经济政策/预期理论概念，与其他概念互补；具体争论待核实。',
        'svg': svg(title, [causal[0][0][:12], causal[1][0][:12], causal[2][0][:12]]),
        'sources': list(dict.fromkeys(srcs)), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作AF】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r51_concepts.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid in ('fiscal-consolidation', 'inflation-bias'):
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
