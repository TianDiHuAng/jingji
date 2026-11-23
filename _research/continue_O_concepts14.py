# -*- coding: utf-8 -*-
"""续作O：新增14条监管/发展/国际金融概念(L2,据REST摘要)。"""
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
 ('basel-accords', '巴塞尔银行监管委员会', '制度',
  '汇集各国银行监管当局、制定共同审慎标准与政策的机构，秘书处设于国际清算银行。',
  '巴塞尔银行监管委员会是一个汇集银行监管当局、制定共同审慎标准与政策的机构，依托设于瑞士巴塞尔国际清算银行（BIS）的常设秘书处运作。其发布的标准（通称巴塞尔协议）成为各国银行资本与风险管理的重要参照。具体标准内容与实施差异待核实。',
  [('各国监管当局汇聚 → 协商共同审慎标准', 'w-en-basel-accords'),
   ('发布标准（如资本与风险管理要求）', 'w-en-basel-accords'),
   ('各国转化为国内监管 → 影响银行资本与经营', 'w-en-bank-regulation')],
  [('国际协调视角', '统一标准减少跨境监管套利、提升可比性', 'w-en-basel-accords'),
   ('主权与适用性视角', '统一标准可能不适配各国金融结构', 'w-en-bank-regulation')],
  ['w-en-basel-accords', 'w-en-bank-regulation'], []),
 ('macroprudential', '宏观审慎监管', '制度',
  '旨在缓解整个金融体系风险（而非单个机构）的监管方式。',
  '宏观审慎监管是旨在缓解金融体系整体风险的监管方式。2008年金融危机后，政策制定者与经济研究者之间逐渐形成共识：监管框架需要转向宏观审慎视角。其工具包括逆周期资本缓冲、贷款价值比限制等。具体工具与效果待核实。',
  [('识别系统性风险累积（信贷过快、杠杆上升）', 'w-en-macroprudential'),
   ('运用逆周期资本等工具抑制风险积累', 'w-en-macroprudential'),
   ('降低系统性危机概率与强度', 'w-en-systemic-risk')],
  [('系统性视角', '个体稳健不等于体系稳健，需整体视角', 'w-en-macroprudential'),
   ('微观审慎视角', '侧重单家机构的资本与合规', 'w-en-bank-regulation')],
  ['w-en-macroprudential', 'w-en-systemic-risk'], []),
 ('reserve-requirement', '存款准备金要求', '制度',
  '中央银行规定商业银行必须持有的流动资产最低数量。',
  '存款准备金要求是中央银行的规定，设定商业银行必须持有的流动资产最低数量。该最低数量通常由央行按银行存款负债的特定比例确定，这一比率常称现金准备金率或准备金率。调整准备金率可影响银行放贷能力与货币乘数。具体比率待核实。',
  [('央行设定准备金率 → 银行须留存一定比例资金', 'w-en-reserve-requirement'),
   ('可贷资金减少 → 信贷与货币创造收缩', 'w-en-money-supply'),
   ('作为货币政策工具调节流动性', 'w-en-monetary-policy')],
  [('货币控制视角', '准备金率直接约束货币乘数与信贷扩张', 'w-en-reserve-requirement'),
   ('审慎/流动性视角', '准备金提供缓冲、降低挤兑风险', 'w-en-bank-regulation')],
  ['w-en-reserve-requirement', 'w-en-monetary-policy'], []),
 ('sudden-stop', '突然停止（资本流动）', '货币',
  '新兴市场私人资本流入突然放缓、经常账户由大赤字急剧逆转的现象。',
  '突然停止指新兴市场经济体私人资本流入的突然放缓，以及经常账户由大额赤字急剧转为较小赤字或小额盈余。突然停止之后通常伴随产出、私人支出与对私人部门信贷的急剧下降，以及实际汇率贬值。这一术语为类比交通现象而造。具体案例待核实。',
  [('私人资本流入突然放缓 → 外部融资骤紧', 'w-en-sudden-stop'),
   ('经常账户由大赤字急剧逆转、实际汇率贬值', 'w-en-sudden-stop'),
   ('产出、私人支出与信贷急剧下降 → 深度衰退', 'w-en-currency-crisis')],
  [('外部融资视角', '突然停止是新兴市场危机的典型触发机制', 'w-en-sudden-stop'),
   ('资产负债表视角', '货币错配与杠杆放大贬值冲击', 'w-en-financial-accelerator')],
  ['w-en-sudden-stop', 'w-en-currency-crisis'], []),
 ('dutch-disease', '荷兰病', '其他',
  '某一部门经济发展与其他部门（尤其制造业）衰退之间的表面因果关系。',
  '荷兰病是经济学中描述某一特定部门经济发展与其他部门衰退之间表面因果关系的现象。该词由《经济学人》于1977年创造，用以描述荷兰在1959年发现格罗宁根大型气田后制造业的衰退。机制通常涉及资源出口带来的汇率升值与成本上升。具体案例待核实。',
  [('资源部门繁荣（如发现大油气田）→ 出口收入与外汇流入增加', 'w-en-dutch-disease'),
   ('本币升值、国内成本上升 → 其他可贸易部门竞争力下降', 'w-en-dutch-disease'),
   ('制造业等萎缩 → 结构性失衡', 'w-en-resource-curse')],
  [('汇率/竞争力视角', '资源繁荣通过实际汇率升值挤出其他部门', 'w-en-dutch-disease'),
   ('资源诅咒视角', '资源依赖可能带来长期增长与制度问题', 'w-en-resource-curse')],
  ['w-en-dutch-disease', 'w-en-resource-curse'], []),
 ('resource-curse', '资源诅咒', '其他',
  '自然资源丰富的国家反而增长更慢、发展结果更差的假说。',
  '资源诅咒（又称丰裕悖论）是一种假说：自然资源丰富的国家，其经济增长率、民主程度或发展结果反而低于资源较少的国家。关于其成因与例外存在大量理论与学术争论。具体机制与证据待核实。',
  [('资源出口带来租金 → 可能挤压其他产业与制度质量', 'w-en-resource-curse'),
   ('租金分配冲突、治理弱化 → 增长与发展受损', 'w-en-resource-curse'),
   ('结构性依赖 → 抵御商品价格冲击能力弱', 'w-en-dutch-disease')],
  [('制度视角', '制度质量决定资源是祝福还是诅咒', 'w-en-resource-curse'),
   ('经济结构视角', '资源繁荣挤出制造业、加剧波动', 'w-en-dutch-disease')],
  ['w-en-resource-curse', 'w-en-dutch-disease'], []),
 ('middle-income-trap', '中等收入陷阱', '其他',
  '一国人均GDP达中等水平后停滞、未能进入高收入国家行列的情形。',
  '中等收入陷阱是发展经济学中的情形：一国已发展至人均GDP达到中等收入水平，但此后不再进一步发展，未能获得高收入国家地位。该词由世界银行于2007年提出，用以描述人均国民生产总值长期停留在中等区间的国家。具体界定与案例待核实。',
  [('低成本优势丧失、创新能力不足 → 增长动力衰减', 'w-en-middle-income-trap'),
   ('无法与低收入经济体比成本、也难与高收入经济体比创新', 'w-en-middle-income-trap'),
   ('人均收入长期停滞于中等区间', 'w-en-middle-income-trap')],
  [('结构转型视角', '需从要素驱动转向效率与创新驱动', 'w-en-middle-income-trap'),
   ('制度视角', '制度与人力资本决定能否跨越', 'w-en-resource-curse')],
  ['w-en-middle-income-trap', 'w-en-resource-curse'], []),
 ('great-moderation', '大缓和', '理论',
  '美国（及发达国家）宏观经济波动显著趋缓的时期，与央行独立性上升同时出现。',
  '大缓和是美国一段宏观经济稳定时期，与中央银行独立性的上升同时出现，始于1980年的沃尔克冲击并延续至21世纪。其特征是发达国家经济周期波动总体较此前数十年更为温和，实际GDP增长、工业生产等主要经济变量波动下降。其成因存在争论。具体论述待核实。',
  [('货币政策框架改进与央行独立性上升 → 通胀与预期更稳定', 'w-en-great-moderation'),
   ('经济周期波动幅度下降 → 产出与通胀更平稳', 'w-en-great-moderation'),
   ('（争论）结构性变化或"好运气"亦可能贡献', 'w-en-great-moderation')],
  [('政策改进视角', '货币政策与独立性提升降低了波动', 'w-en-great-moderation'),
   ('运气/结构视角', '冲击变小或结构变化是主因', 'w-en-business-cycle')],
  ['w-en-great-moderation', 'w-en-business-cycle'], []),
 ('foreign-exchange-reserves', '外汇储备', '货币',
  '中央银行或其他货币当局持有的、可用于平衡国际收支与影响汇率的外币资产。',
  '外汇储备是中央银行或其他货币当局持有的现金及其他储备资产（如黄金、白银），主要用于平衡本国国际收支、影响本币汇率以及维持金融市场信心。储备以一种或多种储备货币持有，其中以美元为主，欧元次之。具体规模与构成待核实。',
  [('出口与资本流入形成外汇 → 央行积累储备资产', 'w-en-foreign-exchange-reserves'),
   ('用于干预外汇市场、平抑汇率波动', 'w-en-foreign-exchange-reserves'),
   ('充足储备维持市场信心、缓冲外部冲击', 'w-en-sudden-stop')],
  [('保险/信心视角', '充足储备可缓冲资本流动冲击、稳定信心', 'w-en-foreign-exchange-reserves'),
   ('成本视角', '持有储备存在机会成本与冲销压力', 'w-en-monetary-policy')],
  ['w-en-foreign-exchange-reserves', 'w-en-monetary-policy'], []),
 ('sovereign-wealth-fund', '主权财富基金', '制度',
  '国有投资基​​金，投资于股票、债券、房地产等实际与金融资产。',
  '主权财富基金（或称主权投资基金）是国有投资基金，投资于股票、债券、房地产、贵金属等实际与金融资产，或私募股权基金、对冲基金等另类投资，并在全球范围投资。多数主权财富基金的资金来自商品出口收入或中央银行持有的外汇储备。具体规模与治理待核实。',
  [('商品出口收入或外汇储备积累 → 形成可投资资金池', 'w-en-sovereign-wealth-fund'),
   ('全球配置股票、债券、地产与另类资产', 'w-en-sovereign-wealth-fund'),
   ('实现跨代储蓄与资产多元化', 'w-en-foreign-exchange-reserves')],
  [('储蓄/多元化视角', '主权基金实现跨代储蓄与资产多元化', 'w-en-sovereign-wealth-fund'),
   ('治理/透明度视角', '国有属性带来治理与透明度关切', 'w-en-bank-regulation')],
  ['w-en-sovereign-wealth-fund', 'w-en-foreign-exchange-reserves'], []),
 ('capital-flight', '资本外逃', '货币',
  '因经济或政治事件导致资产或资金迅速流出某国的现象。',
  '资本外逃是经济学中的现象：由于具有经济后果的事件，或政权更迭等政治事件，资产或资金迅速流出某国。此类事件可能包括领导层行为反复或不可信、对资本或资本持有者加税、政府债务违约等，令投资者降低对该国的信心。具体案例待核实。',
  [('政策或政治风险上升 → 投资者信心下降', 'w-en-capital-flight'),
   ('资产与资金迅速外流、本币承压', 'w-en-capital-flight'),
   ('储备流失、融资成本上升 → 危机加深', 'w-en-currency-crisis')],
  [('信心/风险视角', '制度与政策可信度决定资本去留', 'w-en-capital-flight'),
   ('管制视角', '资本管制可短期遏制外流但代价高', 'w-en-capital-control')],
  ['w-en-capital-flight', 'w-en-currency-crisis'], []),
 ('financial-repression', '金融抑制', '制度',
  '政府将国内资金导向公共部门的政策，用以降低政府债务占GDP比率。',
  '金融抑制指政府实施政策，把国内资金导向公共部门——这些资金在放开的市场环境下会流向别处。此类政策被用于降低政府的债务对GDP比率。常见手段包括利率上限、强制配置国债与资本管制。具体手段与影响待核实。',
  [('政府施加利率上限与配置要求 → 资金流向公共部门', 'w-en-financial-repression'),
   ('实际利率偏低 → 储蓄者向政府转移购买力', 'w-en-financial-repression'),
   ('政府债务/GDP比率下降，但储蓄配置效率受损', 'w-en-capital-control')],
  [('财政视角', '金融抑制是隐性债务削减工具', 'w-en-financial-repression'),
   ('金融发展视角', '抑制损害储蓄回报与金融深化', 'w-en-bank-regulation')],
  ['w-en-financial-repression', 'w-en-capital-control'], []),
 ('bank-regulation', '银行监管', '制度',
  '对银行施加特定要求、限制与指引的金融监管形式，由监管机构执行。',
  '银行监管与监督是对银行施加特定要求、限制与指引的金融监管形式，由金融监管当局执行，具体表述因司法辖区而异。总体而言，银行监管旨在确保银行业的稳定，并促进银行与个人之间的透明度。具体规则与架构待核实。',
  [('监管当局设定资本、流动性与业务规则 → 约束银行行为', 'w-en-bank-regulation'),
   ('监督检查与信息披露 → 提升透明度', 'w-en-bank-regulation'),
   ('降低银行失败与系统性风险', 'w-en-systemic-risk')],
  [('稳定视角', '监管通过资本与流动性要求降低失败概率', 'w-en-bank-regulation'),
   ('成本/效率视角', '监管合规成本可能抑制信贷与创新', 'w-en-macroprudential')],
  ['w-en-bank-regulation', 'w-en-systemic-risk'], []),
 ('wage-price-spiral', '工资-价格螺旋', '理论',
  '工资上涨引发价格上涨、价格上涨再推高工资的正反馈式通胀解释。',
  '工资-价格螺旋是宏观经济学中对通胀的一种解释：工资上涨导致价格上涨，价格上涨又导致工资上涨，形成正反馈循环。曼昆（Greg Mankiw）指出，某一时点这种工资与价格不断上升的螺旋将会放缓；长期来看，经济会回到总需求曲线与长期总供给曲线相交之处。具体机制待核实。',
  [('工资上涨 → 企业成本上升、提价', 'w-en-wage-price-spiral'),
   ('物价上涨 → 工人要求更高工资', 'w-en-wage-price-spiral'),
   ('正反馈循环；长期随总需求与长期总供给相交而收敛', 'w-en-inflation')],
  [('成本推动视角', '工资-价格互动是持续性通胀的机制之一', 'w-en-wage-price-spiral'),
   ('货币视角', '若无货币扩张，螺旋难以持续', 'w-en-money-supply')],
  ['w-en-wage-price-spiral', 'w-en-inflation'], []),
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
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作O】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r33_concepts.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid == 'inflation-expectations':
        continue  # 重定向到 Inflation，不建独立来源
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
