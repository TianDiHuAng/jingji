# -*- coding: utf-8 -*-
"""续作P：新增14条宏观经济理论概念(L2,据REST摘要)。"""
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
 ('core-inflation', '核心通货膨胀', '理论',
  '剔除短期价格波动显著项目、以反映价格水平潜在长期趋势的通胀度量。',
  '核心通胀是一种通胀度量，试图反映经济中总体价格水平的潜在长期趋势。其做法是从整体消费篮子中剔除某些短期价格波动显著的项目，因而被用作潜在长期通胀的指标与预测器。具体剔除范围与政策用法待核实。',
  [('整体价格篮子包含短期剧烈波动项目 → 掩盖趋势', 'w-en-core-inflation'),
   ('剔除这些项目 → 得到反映潜在趋势的核心通胀', 'w-en-core-inflation'),
   ('作为潜在长期通胀的指标与预测器用于政策判断', 'w-en-inflation')],
  [('核心度量视角', '剔除波动项能更好识别通胀趋势', 'w-en-core-inflation'),
   ('总体度量视角', '居民实际感受更接近总体通胀（含食品能源）', 'w-en-inflation')],
  ['w-en-core-inflation', 'w-en-inflation'], []),
 ('aggregate-demand', '总需求', '理论',
  '一定时期经济中对最终商品与服务的总需求，即对一国GDP的需求。',
  '总需求（AD），亦称国内最终需求（DFD），是一定时期经济中对最终商品与服务的总需求，常被称为有效需求。它是对一国国内生产总值的需求，指明在所有可能价格水平下将被购买的商品与服务数量。与总供给共同构成 AD-AS 模型。具体构成待核实。',
  [('家庭消费、投资、政府支出与净出口 → 构成总需求', 'w-en-aggregate-demand'),
   ('在各价格水平下确定需求量 → 形成总需求曲线', 'w-en-aggregate-demand'),
   ('与总供给共同决定产出与价格水平', 'w-en-aggregate-supply')],
  [('凯恩斯视角', '总需求不足是衰退与失业的主因，需政策扩张', 'w-en-aggregate-demand'),
   ('古典视角', '供给创造自身需求，总需求自动匹配', 'w-en-neutrality-of-money')],
  ['w-en-aggregate-demand', 'w-en-aggregate-supply'], []),
 ('aggregate-supply', '总供给', '理论',
  '一国企业在特定时期计划出售的商品与服务总供给。',
  '总供给（AS），亦称国内最终供给（DFS），是一国经济中企业在特定时期内计划出售的商品与服务总供给，即在给定价格水平下企业愿意且有能力的供给总量。它与总需求共同构成 AD-AS 模型的两个组成部分。具体形状与假设待核实。',
  [('企业依据成本与价格 → 决定供给量', 'w-en-aggregate-supply'),
   ('在各价格水平下形成总供给曲线（短期与长期不同）', 'w-en-aggregate-supply'),
   ('与总需求相交决定均衡产出与价格', 'w-en-aggregate-demand')],
  [('短期视角', '短期总供给向上倾斜，价格上升可刺激产出', 'w-en-aggregate-supply'),
   ('长期视角', '长期总供给由要素与技术决定，垂直', 'w-en-solow-model')],
  ['w-en-aggregate-supply', 'w-en-aggregate-demand'], []),
 ('natural-rate-unemployment', '自然失业率', '理论',
  '经济在长期趋向的、与通胀稳定相容的失业水平。',
  '自然失业率是经济活动研究中的关键概念，由米尔顿·弗里德曼与埃德蒙·费尔普斯在1960年代提出，两人因相关工作获得诺贝尔经济学奖，该概念的发展被视为获奖的主要动因之一。简化而言，它指经济在长期趋向的失业水平，与通胀加速或减速无关。具体界定与测算待核实。',
  [('摩擦与结构性因素 → 形成长期失业基准', 'w-en-natural-rate-unemployment'),
   ('实际失业围绕自然率波动（周期性部分）', 'w-en-natural-rate-unemployment'),
   ('长期无法以需求政策持续压低失业', 'w-en-phillips-curve')],
  [('货币主义/新古典视角', '长期失业趋向自然率，扩张只带来通胀', 'w-en-natural-rate-unemployment'),
   ('凯恩斯视角', '需求不足可致长期偏离自然率', 'w-en-aggregate-demand')],
  ['w-en-natural-rate-unemployment', 'w-en-phillips-curve'], []),
 ('automatic-stabilizer', '自动稳定器', '制度',
  '现代政府预算结构（尤其所得税与福利支出）中自动减少实际GDP波动的特征。',
  '自动稳定器是宏观经济学中现代政府预算结构的特征，尤其包括所得税与福利支出，其作用是在不另行立法的情况下减少实际GDP的波动。经济下行时税收自动减少、福利支出自动增加，从而缓冲需求下滑。具体效果待核实。',
  [('经济下行 → 收入下降使所得税自动减少', 'w-en-automatic-stabilizer'),
   ('失业与贫困上升 → 福利支出自动增加', 'w-en-automatic-stabilizer'),
   ('缓冲可支配收入与需求的下滑幅度', 'w-en-fiscal-policy')],
  [('稳定器视角', '无需立法的自动调节可及时缓冲周期', 'w-en-automatic-stabilizer'),
   ('相机抉择视角', '主动财政措施可在深度衰退中补充', 'w-en-fiscal-multiplier')],
  ['w-en-automatic-stabilizer', 'w-en-fiscal-policy'], []),
 ('government-debt', '政府债务', '债务',
  '政府部门的金融负债；其变化主要反映过去财政赤字导致的借贷。',
  '一国政府债务总额是政府部门的金融负债。政府债务随时间的变化主要反映过去财政赤字导致的借贷：当政府支出超过收入时形成赤字。政府债务可能欠国内居民，也可能欠外国居民；若欠外国居民，则该部分计入外债。具体口径待核实。',
  [('政府支出超过收入 → 形成财政赤字', 'w-en-government-debt'),
   ('赤字通过借贷融资 → 政府债务累积', 'w-en-government-debt'),
   ('债务可持续性取决于利率与增长（及币种结构）', 'w-en-debt-crisis')],
  [('可持续性视角', '债务/GDP 与利率-增长差决定可持续性', 'w-en-debt-crisis'),
   ('功能财政视角', '适度债务可支持需求与公共投资', 'w-en-fiscal-multiplier')],
  ['w-en-government-debt', 'w-en-debt-crisis'], []),
 ('money-multiplier', '货币乘数', '货币',
  '货币供应量与货币基础之比。',
  '在货币经济学中，货币乘数是货币供应量与货币基础之比。在一些简化表述中，货币乘数被简单地呈现为中央银行所要求准备金率的倒数；更一般地，乘数取决于家庭偏好、法律规定以及商业银行的经营政策。具体测算待核实。',
  [('央行投放基础货币 → 银行体系通过放贷派生存款', 'w-en-money-multiplier'),
   ('货币供应量按乘数扩张（受准备金率等约束）', 'w-en-money-multiplier'),
   ('乘数变化影响货币政策效果', 'w-en-money-supply')],
  [('乘数视角', '基础货币通过银行体系倍数扩张', 'w-en-money-multiplier'),
   ('内生货币视角', '信贷需求与银行行为决定货币创造', 'w-en-monetary-policy')],
  ['w-en-money-multiplier', 'w-en-money-supply'], []),
 ('neutrality-of-money', '货币中性', '理论',
  '货币供给变化只影响名义变量、不影响实际变量的观点。',
  '货币中性是指货币供给变化只影响经济中的名义变量（如价格、工资与汇率），而对实际变量（如就业、实际GDP与实际消费）没有影响的观点。它是古典经济学的重要思想，与"古典二分法"相关，意味着中央银行不影响实际变量。其成立时限（长期或短期）存在争论。具体论述待核实。',
  [('货币供给变化 → 名义价格与工资同比例调整', 'w-en-neutrality-of-money'),
   ('实际变量（产出、就业）不受影响', 'w-en-neutrality-of-money'),
   ('货币政策只决定名义尺度（长期视角）', 'w-en-monetary-policy')],
  [('古典/新古典视角', '长期货币中性，货币只是面纱', 'w-en-neutrality-of-money'),
   ('凯恩斯视角', '短期货币非中性，可影响产出与就业', 'w-en-aggregate-demand')],
  ['w-en-neutrality-of-money', 'w-en-monetary-policy'], []),
 ('seigniorage', '铸币税', '货币',
  '政府从发行货币中获得的利润，即货币面值与生产成本的差额。',
  '铸币税（亦拼作 seignorage / seigneurage）指政府从发行货币中获得的利润，即货币面值与生产该货币的成本之间的差额。在纸币体系下，铸币税与货币发行量及相关通胀密切相关；恶性通胀时期政府常依赖铸币税融资。具体规模待核实。',
  [('政府发行货币 → 获得面值与成本之差', 'w-en-seigniorage'),
   ('以发行收入弥补财政缺口', 'w-en-seigniorage'),
   ('过度依赖 → 货币超发与通胀（乃至恶性通胀）', 'w-en-hyperinflation')],
  [('财政视角', '铸币税是一种隐性税收与融资手段', 'w-en-seigniorage'),
   ('货币纪律视角', '过度依赖铸币税导致通胀失控', 'w-en-hyperinflation')],
  ['w-en-seigniorage', 'w-en-hyperinflation'], []),
 ('purchasing-power-parity', '购买力平价', '货币',
  '以不同国家特定商品价格衡量、用于比较各国货币绝对购买力的指标。',
  '购买力平价（PPP）是衡量不同国家特定商品价格的指标，用于比较各国货币的绝对购买力。PPP 实质上一地市场篮子的价格除以另一地同一篮子商品价格之比。PPP 通胀与汇率可能不同于市场汇率。该概念是长期汇率决定理论之一。具体测算待核实。',
  [('同一篮子商品在不同国家的价格差异 → 形成PPP比率', 'w-en-purchasing-power-parity'),
   ('作为长期汇率"锚"（实际汇率趋向PPP）', 'w-en-purchasing-power-parity'),
   ('短期汇率可显著偏离PPP', 'w-en-exchange-rate-regime')],
  [('长期视角', 'PPP 为汇率提供长期基准', 'w-en-purchasing-power-parity'),
   ('短期视角', '价格粘性与资本流动使汇率短期偏离PPP', 'w-en-interest-rate-parity')],
  ['w-en-purchasing-power-parity', 'w-en-exchange-rate-regime'], []),
 ('interest-rate-parity', '利率平价', '货币',
  '投资者比较两国存款利率时的无套利均衡条件。',
  '利率平价是一种无套利条件，表示投资者比较两国银行存款利率时所处的均衡状态。该条件并不总是成立，从而为抛补利率套利留下获取无风险利润的机会。利率平价的两个核心假设是资本流动性与资产的完全替代性。具体形式待核实。',
  [('比较两国利率与远期汇率 → 形成套利条件', 'w-en-interest-rate-parity'),
   ('偏离时出现抛补套利机会', 'w-en-interest-rate-parity'),
   ('套利活动推动条件趋于恢复（受资本流动限制影响）', 'w-en-capital-control')],
  [('无套利视角', '利率与汇率联动受套利约束', 'w-en-interest-rate-parity'),
   ('摩擦视角', '资本管制与风险溢价使平价长期偏离', 'w-en-capital-control')],
  ['w-en-interest-rate-parity', 'w-en-capital-control'], []),
 ('mundell-fleming', '蒙代尔-弗莱明模型', '理论',
  '描述小型开放经济的 IS-LM-BoP 模型，由 Mundell 与 Fleming 分别提出。',
  '蒙代尔-弗莱明模型（又称 IS-LM-BoP 模型）由罗伯特·蒙代尔与马库斯·弗莱明分别提出，是对 IS-LM 模型的扩展：传统 IS-LM 处理封闭经济，而该模型描述小型开放经济。它用于分析不同汇率制度下财政与货币政策的效果。具体结论待核实。',
  [('小型开放经济 → 引入外部部门（BoP）到 IS-LM 框架', 'w-en-mundell-fleming'),
   ('在固定/浮动汇率下政策效果不同', 'w-en-mundell-fleming'),
   ('与不可能三角的政策权衡直接相关', 'w-en-impossible-trinity')],
  [('开放宏观视角', '汇率制度决定财政货币政策相对有效性', 'w-en-mundell-fleming'),
   ('三元悖论视角', '资本流动下政策独立性受汇率制度约束', 'w-en-impossible-trinity')],
  ['w-en-mundell-fleming', 'w-en-impossible-trinity'], []),
 ('solow-model', '索洛-斯旺模型', '理论',
  '以外生技术进步解释长期经济增长的总量增长模型。',
  '索洛-斯旺模型（或称外生增长模型）是关于长期经济增长的模型，试图通过资本积累、劳动或人口增长以及主要由技术进步驱动的生产率提升来解释长期增长。其核心是一个总量生产函数，通常设为柯布-道格拉斯型。模型显示长期人均增长最终依赖技术进步。具体推导待核实。',
  [('资本积累与劳动增长 → 人均资本深化（边际递减）', 'w-en-solow-model'),
   ('技术进步 → 推动长期人均产出持续增长', 'w-en-solow-model'),
   ('趋同假说：条件相近的经济体人均收入趋于收敛', 'w-en-total-factor-productivity')],
  [('外生增长视角', '长期增长最终由外生技术进步决定', 'w-en-solow-model'),
   ('内生增长视角', '技术与人力资本可由政策与研发内生决定', 'w-en-total-factor-productivity')],
  ['w-en-solow-model', 'w-en-total-factor-productivity'], []),
 ('total-factor-productivity', '全要素生产率', '理论',
  '通常以总产出与总投入之比衡量的多要素生产率。',
  '全要素生产率（TFP，亦称多要素生产率）通常以总产出与总投入之比来衡量。在对生产技术作某些简化假设下，全要素生产率的增长成为产出增长中不能由传统测量的劳动与资本投入增长所解释的部分（即"索洛余值"）。它被视为长期增长的关键来源。具体测算待核实。',
  [('产出增长中扣除要素投入贡献 → 剩余部分即TFP增长', 'w-en-total-factor-productivity'),
   ('TFP 提升 → 相同投入获得更多产出', 'w-en-total-factor-productivity'),
   ('长期人均增长主要依赖TFP（技术进步、效率改善）', 'w-en-solow-model')],
  [('增长核算视角', 'TFP 是长期增长的核心驱动', 'w-en-total-factor-productivity'),
   ('测算批判视角', '余值法可能混入测量误差与配置效率等因素', 'w-en-total-factor-productivity')],
  ['w-en-total-factor-productivity', 'w-en-solow-model'], []),
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
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作P】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r34_concepts.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid == 'inflation-expectations':
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
