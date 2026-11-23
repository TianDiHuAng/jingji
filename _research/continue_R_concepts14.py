# -*- coding: utf-8 -*-
"""续作R：新增14条经济史/发展经济学/宏观模型概念(L2,据REST摘要)。"""
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
 ('industrial-revolution', '工业革命', '其他',
  '全球经济转向更广泛、高效与稳定制造过程的过渡时期。',
  '工业革命（相对其后的第二次工业革命，有时称第一次工业革命）是全球经济向更广泛、更高效、更稳定的制造过程过渡的时期，接续第二次农业革命。它带来生产方式、城市化与收入结构的深刻变化，被视为现代经济增长的起点。具体时间与国别差异待核实。',
  [('农业革命与要素供给改善 → 为工业化创造条件', 'w-en-industrial-revolution'),
   ('机器生产与工厂制度扩散 → 制造效率大幅提升', 'w-en-industrial-revolution'),
   ('生产率与收入结构转变 → 现代经济增长启动', 'w-en-great-divergence')],
  [('技术/要素视角', '技术与资本积累推动工业化', 'w-en-industrial-revolution'),
   ('制度/全球视角', '制度与全球贸易格局决定各国工业化速度', 'w-en-great-divergence')],
  ['w-en-industrial-revolution', 'w-en-great-divergence'], []),
 ('great-divergence', '大分流', '其他',
  '西欧及其海外移民殖民地突破前现代增长约束、跃居世界最富强文明的社会经济转变。',
  '大分流（或称"欧洲奇迹"）指这样一种社会经济转变：西欧连同北美与澳大拉西亚的移民殖民地，突破了前现代的增长约束，崛起为最强大富有的世界文明，超越了此前占主导的其他地区。其成因（制度、资源、殖民、技术等）是经济史的核心争论。具体论述待核实。',
  [('制度、科学与商业组织变化 → 突破前现代增长上限', 'w-en-great-divergence'),
   ('工业化与殖民贸易 → 西欧及其殖民地的产出与收入跃升', 'w-en-industrial-revolution'),
   ('与其他地区差距扩大 → 形成"大分流"', 'w-en-great-divergence')],
  [('制度视角', '产权、市场与科学文化是关键', 'w-en-great-divergence'),
   ('全球/殖民视角', '殖民掠夺与全球贸易格局塑造差距', 'w-en-industrial-revolution')],
  ['w-en-great-divergence', 'w-en-industrial-revolution'], []),
 ('marshall-plan', '马歇尔计划', '制度',
  '1948年美国向西欧提供大规模对外援助、支持战后经济复苏的计划。',
  '马歇尔计划是美国于1948年实施的倡议，向西欧提供对外援助。美国在二战后西欧经济复苏计划中向17个欧洲国家转移了133亿美元（US$13.3 billion）。该计划取代了此前的临时援助安排，被视为战后欧洲复兴与国际经济秩序重建的重要一环。具体效果待核实。',
  [('二战后西欧经济凋敝、政治不稳 → 需要外部援助', 'w-en-marshall-plan'),
   ('美国提供资金与技术援助（133亿美元、17国）', 'w-en-marshall-plan'),
   ('支持复苏与贸易重建 → 稳定战后欧洲经济秩序', 'w-en-bretton-woods-system')],
  [('援助/复兴视角', '外部资金填补缺口、加速重建', 'w-en-marshall-plan'),
   ('地缘政治视角', '计划兼具遏制与秩序构建目的', 'w-en-bretton-woods-system')],
  ['w-en-marshall-plan', 'w-en-bretton-woods-system'],
  [('援助总额(1948年起)', 13.3, '十亿美元（US$13.3 billion，17个欧洲国家）', 1948,
    '原文：The United States transferred US$13.3 billion to 17 European countries；单一来源待核实。')]),
 ('washington-consensus', '华盛顿共识', '制度',
  '1980—90年代被视为针对危机中国家的"标准"改革方案的一套十项经济政策处方。',
  '华盛顿共识是一套十项经济政策处方，在1980与1990年代被认为构成针对受危机困扰的发展中国家的"标准"改革方案，由设在华盛顿的国际货币基金组织（IMF）、世界银行与美国政府等机构推动。其内容与效果存在广泛争议。具体条目待核实。',
  [('发展中国家陷入危机 → 向国际金融机构求援', 'w-en-washington-consensus'),
   ('以十项政策处方（自由化、私有化、稳定化等）作为贷款条件', 'w-en-washington-consensus'),
   ('改革效果参差，引发对"标准方案"的批评', 'w-en-import-substitution')],
  [('主流改革视角', '宏观稳定与市场化为增长奠定基础', 'w-en-washington-consensus'),
   ('批判视角', '忽视制度差异与社会代价，成效有限', 'w-en-import-substitution')],
  ['w-en-washington-consensus', 'w-en-import-substitution'], []),
 ('import-substitution', '进口替代工业化', '制度',
  '主张以本国生产替代外国进口的保护主义贸易与产业政策。',
  '进口替代工业化（ISI）是一种保护主义贸易与经济政策，主张以本国生产替代外国进口。其前提是一国应通过本地生产工业制成品来减少对外依赖。该战略在拉美等地广泛采用，其成效与局限（效率、外汇约束等）存在争论。具体案例待核实。',
  [('对制成品进口依赖 → 外汇压力与产业薄弱', 'w-en-import-substitution'),
   ('以关税与非关税壁垒保护本国工业 → 本地生产替代进口', 'w-en-import-substitution'),
   ('可能效率不足、出口竞争力弱（成效有争议）', 'w-en-export-oriented')],
  [('结构主义视角', '保护幼稚产业、减少外部依赖', 'w-en-import-substitution'),
   ('出口导向视角', '外向型战略更利于效率与增长', 'w-en-export-oriented')],
  ['w-en-import-substitution', 'w-en-export-oriented'], []),
 ('export-oriented', '出口导向工业化', '制度',
  '通过出口本国具有优势的商品以加速工业化进程的贸易与经济政策。',
  '出口导向工业化（EOI，亦称出口替代工业化、出口带动型增长）是一种贸易与经济政策，旨在通过出口本国具有优势的商品来加速一国的工业化进程。东亚经济体常被视为该战略的成功案例，与进口替代形成对照。具体机制待核实。',
  [('发挥比较优势 → 出口劳动密集型等优势产品', 'w-en-export-oriented'),
   ('参与国际市场竞争 → 提升效率与技术升级', 'w-en-export-oriented'),
   ('带动工业化与增长（东亚经验常被引用）', 'w-en-import-substitution')],
  [('外向型视角', '出口竞争促进效率与技术升级', 'w-en-export-oriented'),
   ('结构主义视角', '过度依赖外需带来脆弱性', 'w-en-import-substitution')],
  ['w-en-export-oriented', 'w-en-import-substitution'], []),
 ('gini', '基尼系数', '理论',
  '衡量一国或社会群体内部收入、财富或消费不平等程度的统计离散度指标。',
  '基尼系数（亦称基尼指数或基尼比率）是经济学中衡量统计离散度的指标，意在表示一国或社会群体内部的收入不平等、财富不平等或消费不平等。该指标由意大利统计学家与社会学家基尼（Corrado Gini）提出。数值解读与局限待核实。',
  [('个体收入/财富分布 → 计算洛伦兹曲线与离散度', 'w-en-gini'),
   ('形成 0 到 1 之间的不平等度量', 'w-en-gini'),
   ('用于比较国家间与跨期不平等变化', 'w-en-poverty-trap')],
  [('分配度量视角', '基尼系数提供可比的总体不平等度量', 'w-en-gini'),
   ('局限视角', '单一指标无法反映分布结构与流动性', 'w-en-poverty-trap')],
  ['w-en-gini', 'w-en-poverty-trap'], []),
 ('poverty-trap', '贫困陷阱（贫困循环）', '其他',
  '贫困似被继承、使后代难以摆脱的自我强化状态。',
  '贫困循环（或称贫困陷阱、代际贫困）指贫困看似被继承、阻碍后代摆脱的状况。它由自我强化机制造成：贫困一旦存在便会持续，除非有外力介入。机制包括教育、健康、信贷与资产的代际传递。具体机制与证据待核实。',
  [('初始贫困 → 教育、健康与资产积累受限', 'w-en-poverty-trap'),
   ('能力与机会不足传递给下一代 → 贫困持续', 'w-en-poverty-trap'),
   ('需外部干预（转移支付、教育、信贷可及）打破循环', 'w-en-microfinance')],
  [('自我强化视角', '多重反馈机制使贫困持久', 'w-en-poverty-trap'),
   ('政策干预视角', '外部资源与制度可打破循环', 'w-en-microfinance')],
  ['w-en-poverty-trap', 'w-en-microfinance'], []),
 ('demographic-dividend', '人口红利', '其他',
  '人口年龄结构变化（劳动年龄人口占比上升）带来的经济增长潜力。',
  '人口红利按联合国人口基金（UNFPA）的定义，是"人口年龄结构变化可能带来的经济增长潜力，主要发生在劳动年龄人口占比高于非劳动年龄人口时"。换言之，抚养比下降时期可能带来储蓄、劳动力供给与增长的窗口期。具体条件待核实。',
  [('生育率下降 → 劳动年龄人口占比上升、抚养比下降', 'w-en-demographic-dividend'),
   ('劳动力供给与储蓄增加 → 增长潜力提升', 'w-en-demographic-dividend'),
   ('窗口期后老龄化 → 红利转为压力', 'w-en-lewis-turning-point')],
  [('人口结构视角', '抚养比下降创造增长窗口', 'w-en-demographic-dividend'),
   ('就业/制度视角', '需足够就业与人力资本投资才能兑现红利', 'w-en-lewis-turning-point')],
  ['w-en-demographic-dividend', 'w-en-lewis-turning-point'], []),
 ('lewis-turning-point', '刘易斯拐点', '其他',
  '经济发展中农村剩余劳动力被制造业完全吸收的阶段，此后实际工资开始上升。',
  '刘易斯拐点指经济发展中的一种情形：农村剩余劳动力被制造业部门完全吸收，这通常导致农业与非熟练工业实际工资上升。该术语以经济学家 W. Arthur Lewis 命名。拐点之后，增长模式与工资、通胀动态随之变化。具体判断标准待核实。',
  [('农村剩余劳动力充裕 → 制造业以低工资扩张', 'w-en-lewis-turning-point'),
   ('剩余劳动力被吸收完毕 → 达到刘易斯拐点', 'w-en-lewis-turning-point'),
   ('实际工资上升 → 增长模式与通胀动态改变', 'w-en-wage-price-spiral')],
  [('二元经济视角', '劳动力无限供给阶段结束后工资上升', 'w-en-lewis-turning-point'),
   ('结构转型视角', '拐点标志增长动力需转向效率提升', 'w-en-middle-income-trap')],
  ['w-en-lewis-turning-point', 'w-en-middle-income-trap'], []),
 ('is-lm', 'IS-LM 模型', '理论',
  '刻画短期利率与产出关系的二维宏观模型（希克斯-汉森模型）。',
  'IS-LM 模型（或称希克斯-汉森模型）是用于宏观经济学教学的二维模型，展示短期内利率与产出之间的关系。其交点由"投资-储蓄"（IS）曲线与"流动性偏好-货币供给"（LM）曲线的相交决定。该模型是总需求分析的基础框架。具体推导待核实。',
  [('产品市场均衡 → 导出 IS 曲线（利率与产出的组合）', 'w-en-is-lm'),
   ('货币市场均衡 → 导出 LM 曲线', 'w-en-is-lm'),
   ('两曲线交点 → 决定短期均衡利率与产出', 'w-en-aggregate-demand')],
  [('凯恩斯-希克斯视角', 'IS-LM 是短期总需求分析的标准框架', 'w-en-is-lm'),
   ('开放经济扩展视角', '加入外部部门得到蒙代尔-弗莱明模型', 'w-en-mundell-fleming')],
  ['w-en-is-lm', 'w-en-aggregate-demand'], []),
 ('laffer-curve', '拉弗曲线', '理论',
  '说明税率与政府税收收入之间理论关系的曲线。',
  '拉弗曲线在经济学中描绘税率与由此产生的政府税收收入之间的理论关系。其推理是：由于在 0% 与 100% 的极端税率下都收不到税收，那么在 0% 与 100% 之间必定存在使税收最大化的税率。该曲线的实证重要性存在争议。具体论述待核实。',
  [('税率为0或100%时税收均为零 → 曲线两端归零', 'w-en-laffer-curve'),
   ('中间存在使税收最大化的税率', 'w-en-laffer-curve'),
   ('超过该税率后提高税率反而减少税收（理论推论）', 'w-en-fiscal-policy')],
  [('供给侧视角', '过高税率抑制经济活动、减少税收', 'w-en-laffer-curve'),
   ('主流/实证视角', '现实税率多未处于曲线不利一侧，减税未必增收', 'w-en-fiscal-multiplier')],
  ['w-en-laffer-curve', 'w-en-fiscal-policy'], []),
 ('okuns-law', '奥肯定律', '理论',
  '失业率与产出损失之间经验观察到的关系。',
  '奥肯定律是经济学中关于失业率与一国生产损失之间经验观察到的关系，以阿瑟·奥肯（Arthur Melvin Okun）命名，他于1962年首次提出该关系。"缺口版本"表述为：失业率每上升1%，一国的GDP将相应变化（具体系数待核实）。该关系并非严格定律。具体表述待核实。',
  [('经济增长放缓 → 失业率上升', 'w-en-okuns-law'),
   ('失业率每上升一定幅度 → 产出出现相应缺口损失', 'w-en-okuns-law'),
   ('用于将失业预测转换为产出损失估计', 'w-en-output-gap')],
  [('经验规律视角', '失业与产出变动存在稳定经验比例', 'w-en-okuns-law'),
   ('批判视角', '系数随国家与时期显著变化，非严格定律', 'w-en-output-gap')],
  ['w-en-okuns-law', 'w-en-output-gap'], []),
 ('durable-goods', '耐用品', '理论',
  '不会迅速磨损、可在多次使用中持续提供效用的商品。',
  '耐用品（或称硬商品、消费耐用品）是经济学中不会迅速磨损、更准确地说可在时间中持续提供效用而非一次性被完全消费的商品。耐用品的需求对收入与利率、以及经济周期更为敏感，其支出波动常放大周期。具体界定待核实。',
  [('商品可长期使用 → 购买可推迟、需求易波动', 'w-en-durable-goods'),
   ('经济不确定性上升 → 耐用品支出首先被推迟', 'w-en-durable-goods'),
   ('耐用品需求波动放大经济周期', 'w-en-business-cycle')],
  [('消费理论视角', '耐用品支出具有跨期替代特性', 'w-en-durable-goods'),
   ('周期视角', '耐用品是周期波动中最易波动的部分', 'w-en-business-cycle')],
  ['w-en-durable-goods', 'w-en-business-cycle'], []),
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
        'comparison': '经济学/经济史概念条目，与其他概念互补；具体适用与争论待核实。',
        'svg': svg(title, [causal[0][0][:12], causal[1][0][:12], causal[2][0][:12]]),
        'sources': srcs, 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作R】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r36_concepts.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid == 'bretton-woods':
        continue  # 已有 w-en-bretton-woods-system
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
