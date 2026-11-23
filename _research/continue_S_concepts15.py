# -*- coding: utf-8 -*-
"""续作S：新增15条贸易/经济思想/国际机构概念(L2,据REST摘要)。"""
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
 ('mercantilism', '重商主义', '理论',
  '旨在最大化出口、最小化进口的民族主义经济政策与经济体系。',
  '重商主义是一种经济体系与民族主义经济政策类型，旨在使一国最大化出口、最小化进口，追求在国内最大限度积累资源并用于单向贸易。重商主义政策在近代早期欧洲盛行，与后来的自由贸易思想形成对照。具体主张待核实。',
  [('追求贸易顺差与贵金属积累 → 限制进口、鼓励出口', 'w-en-mercantilism'),
   ('国家干预贸易与殖民扩张 → 积累国内资源', 'w-en-mercantilism'),
   ('被视为零和贸易观，后被自由贸易理论取代', 'w-en-comparative-advantage')],
  [('重商主义视角', '国家实力取决于积累的财富与贸易顺差', 'w-en-mercantilism'),
   ('古典/自由贸易视角', '贸易可互利，非零和', 'w-en-comparative-advantage')],
  ['w-en-mercantilism', 'w-en-comparative-advantage'], []),
 ('physiocracy', '重农学派', '理论',
  '18世纪法国启蒙经济学家提出的、认为国民财富唯一来自土地农业的经济理论。',
  '重农学派是18世纪启蒙时代一批法国经济学家发展出的经济理论。他们认为国民财富完全来自"土地农业"或"土地开发"的价值，并主张农产品应保持高价。重农学派被视为最早的系统性经济思想流派之一。具体主张待核实。',
  [('认为只有农业创造净产出 → 土地是财富唯一来源', 'w-en-physiocracy'),
   ('主张农产品高价与减轻农业税负', 'w-en-physiocracy'),
   ('反对重商主义的管制，倾向自然秩序', 'w-en-mercantilism')],
  [('重农视角', '农业是唯一生产性部门', 'w-en-physiocracy'),
   ('古典视角', '工业与服务业同样创造价值', 'w-en-classical-economics')],
  ['w-en-physiocracy', 'w-en-classical-economics'], []),
 ('quantity-theory-money', '货币数量论', '理论',
  '认为一般价格水平与流通中货币量成正比、且因果由货币指向价格的假说。',
  '货币数量论（QTM）是货币经济学中的假说：商品与服务的一般价格水平与流通中的货币量成正比，且因果关系由货币指向价格。这意味着货币量的变化主要影响物价而非实际产出（长期）。该理论是货币主义的核心之一。具体表述待核实。',
  [('货币量增加 → 名义需求上升', 'w-en-quantity-theory-money'),
   ('一般价格水平与货币量同比例上升', 'w-en-quantity-theory-money'),
   ('长期实际产出不受影响（货币中性）', 'w-en-neutrality-of-money')],
  [('货币主义视角', '通胀本质上是货币现象', 'w-en-quantity-theory-money'),
   ('凯恩斯视角', '货币流通速度可变、短期非中性', 'w-en-liquidity-trap')],
  ['w-en-quantity-theory-money', 'w-en-neutrality-of-money'], []),
 ('says-law', '萨伊定律', '理论',
  '古典经济学中"生产创造需求"的主张：产品的生产为其他产品提供可交换的价值。',
  '在古典经济学中，萨伊定律（或市场定律）主张：一种产品的生产会为另一种产品创造需求，因为生产提供了可用于交换其他产品的价值——即生产是需求的来源。该定律以让-巴蒂斯特·萨伊命名。凯恩斯对其提出根本性质疑。具体论述待核实。',
  [('生产创造收入 → 收入形成对其他产品的需求', 'w-en-says-law'),
   ('供给自动创造相应需求 → 不存在普遍生产过剩', 'w-en-says-law'),
   ('（凯恩斯反驳）需求可能不足，导致失业与过剩', 'w-en-keynesian-economics')],
  [('古典视角', '供给创造需求，市场自动出清', 'w-en-says-law'),
   ('凯恩斯视角', '总需求可能不足，需政策干预', 'w-en-keynesian-economics')],
  ['w-en-says-law', 'w-en-keynesian-economics'], []),
 ('ricardian-equivalence', '李嘉图等价', '理论',
  '认为前瞻性消费者会内化政府预算约束、使赤字融资与税收融资效果等价的假说。',
  '李嘉图等价命题是一种经济假说：消费者是前瞻性的，因而在作消费决策时会内化政府的预算约束。其结果是，对给定的政府支出路径，以债务融资还是以税收融资对总需求的影响相同。该假说在现实中受到广泛质疑。具体论述待核实。',
  [('政府以借债替代征税 → 消费者预期未来增税', 'w-en-ricardian-equivalence'),
   ('前瞻性消费者增加储蓄、抵消需求刺激', 'w-en-ricardian-equivalence'),
   ('财政政策的净效果被削弱（假说推论）', 'w-en-crowding-out')],
  [('新古典视角', '理性前瞻主体使债务与税收等价', 'w-en-ricardian-equivalence'),
   ('凯恩斯视角', '流动性约束与短视使减税确有刺激作用', 'w-en-fiscal-multiplier')],
  ['w-en-ricardian-equivalence', 'w-en-fiscal-multiplier'], []),
 ('comparative-advantage', '比较优势', '理论',
  '解释即使一方在所有产品上都更高效、各方仍可从贸易中获益的经济学原理。',
  '比较优势是一条经济学原理，解释为何个人、企业与国家即使在一方生产每种商品或服务都更具生产效率时，仍常能从贸易中获益。该原理指出：当每个参与者专注于其放弃机会成本较低的生产时，贸易收益更大。它是国际贸易理论的基石。具体推导待核实。',
  [('各方机会成本不同 → 专业化于相对成本较低的产品', 'w-en-comparative-advantage'),
   ('专业化与交换 → 总产出与双方福利提升', 'w-en-comparative-advantage'),
   ('构成自由贸易的理论基础', 'w-en-free-trade')],
  [('古典贸易视角', '比较优势使贸易互利，非零和', 'w-en-comparative-advantage'),
   ('保护主义视角', '关注分配、战略产业与调整成本', 'w-en-protectionism')],
  ['w-en-comparative-advantage', 'w-en-free-trade'], []),
 ('tariff', '关税', '制度',
  '一国政府、关税区或超国家联盟对进口货物征收、由进口商缴纳的税。',
  '关税（或进口税）是国家政府、关税辖区或超国家联盟对进口货物征收的税负，由进口商支付。例外情况下也可对出口货物或原材料征收出口税，由出口商支付。关税既增加财政收入，也用于保护国内产业。具体税率与效应待核实。',
  [('对进口征税 → 进口成本上升、进口量下降', 'w-en-tariff'),
   ('国内生产者获得价格保护 → 产出与就业可能上升', 'w-en-protectionism'),
   ('消费者承担更高价格，贸易量收缩', 'w-en-free-trade')],
  [('保护视角', '关税保护幼稚产业、增加财政收入', 'w-en-protectionism'),
   ('自由贸易视角', '关税抬高消费者成本、降低总福利', 'w-en-free-trade')],
  ['w-en-tariff', 'w-en-protectionism'], []),
 ('protectionism', '保护主义', '制度',
  '通过关税、进口配额与其他政府管制限制进口的经济政策。',
  '保护主义（或称贸易保护主义）是通过对进口商品征收关税、设置进口配额以及其他各种政府管制来限制从其他国家进口的经济政策。支持者认为保护主义政策可保护本国产业与就业；批评者强调效率损失与报复风险。具体争论待核实。',
  [('以关税与配额限制进口 → 国内产业受保护', 'w-en-protectionism'),
   ('国内产出与就业受支撑，但价格上升', 'w-en-tariff'),
   ('可能引发贸易伙伴报复、降低总体福利', 'w-en-free-trade')],
  [('保护视角', '保护幼稚产业、维护就业与安全', 'w-en-protectionism'),
   ('自由贸易视角', '保护降低效率、抬高成本并招致报复', 'w-en-free-trade')],
  ['w-en-protectionism', 'w-en-tariff'], []),
 ('free-trade', '自由贸易', '制度',
  '不通过法律壁垒限制进出口的贸易政策。',
  '自由贸易是一种不通过法律壁垒限制进出口的贸易政策。在政治光谱中，自由贸易主要由持经济自由主义立场的政党倡导，而经济民族主义政党通常支持保护主义。自由贸易的理论基础是比较优势。具体实践与争议待核实。',
  [('消除关税与非关税壁垒 → 商品与服务自由流动', 'w-en-free-trade'),
   ('按比较优势专业化 → 效率与总福利提升', 'w-en-comparative-advantage'),
   ('但带来调整成本与分配效应', 'w-en-protectionism')],
  [('自由主义视角', '自由贸易提升效率与总福利', 'w-en-free-trade'),
   ('民族主义/保护视角', '关注就业流失与战略产业', 'w-en-protectionism')],
  ['w-en-free-trade', 'w-en-comparative-advantage'], []),
 ('globalization', '全球化', '其他',
  '世界各国经济、市场、社会与文化之间相互依存与一体化程度提高的过程。',
  '全球化是世界范围内不同国家的经济、市场、社会与文化之间相互依存与一体化程度不断提高的过程。其驱动因素包括国际贸易壁垒的减少、资本流动自由化等。全球化在增长与减贫上的作用、以及其风险（冲击传导、不平等）存在争论。具体论述待核实。',
  [('贸易壁垒下降与资本流动自由化 → 跨境联系增强', 'w-en-globalization'),
   ('生产与金融网络跨国整合 → 相互依存上升', 'w-en-globalization'),
   ('冲击跨境传导更快，也带来增长与减贫效应（有争论）', 'w-en-financial-contagion')],
  [('一体化视角', '全球化提升效率、扩散技术与减贫', 'w-en-globalization'),
   ('批判视角', '加剧不平等、放大跨境冲击传导', 'w-en-financial-contagion')],
  ['w-en-globalization', 'w-en-financial-contagion'], []),
 ('sdr', '特别提款权(SDR)', '货币',
  '由国际货币基金组织定义与维持的补充性外汇储备资产。',
  '特别提款权是由国际货币基金组织（IMF）定义与维持的补充性外汇储备资产。SDR 是 IMF 的记账单位，而非一种货币；其价值基于一篮子货币，具体构成由 IMF 规定。SDR 可用于补充成员国储备、缓解流动性压力。具体构成与分配待核实。',
  [('IMF 创设并分配 SDR → 补充成员国储备资产', 'w-en-sdr'),
   ('价值按一篮子货币定值 → 相对稳定', 'w-en-sdr'),
   ('用于缓解全球储备流动性不足', 'w-en-triffin-dilemma')],
  [('超主权储备视角', 'SDR 可缓解对单一主权货币的依赖', 'w-en-sdr'),
   ('现实约束视角', 'SDR 规模有限、非直接交易货币', 'w-en-triffin-dilemma')],
  ['w-en-sdr', 'w-en-triffin-dilemma'], []),
 ('imf', '国际货币基金组织(IMF)', '制度',
  '总部位于华盛顿的国际金融机构与联合国专门机构，致力于促进全球货币合作与金融稳定。',
  '国际货币基金组织（IMF）是一个国际金融机构、联合国专门机构，总部设于华盛顿特区。它由191个成员国组成，其宣称的使命是"促进全球货币合作、保障金融稳定"等。IMF 在危机中提供贷款与政策条件。具体职能与争议待核实。',
  [('成员国出资形成资金池 → 向国际收支困难国提供贷款', 'w-en-imf'),
   ('附带政策条件 → 影响借款国宏观政策', 'w-en-washington-consensus'),
   ('监督全球与国别经济、促进货币合作', 'w-en-imf')],
  [('稳定/合作视角', 'IMF 提供流动性、促进协调', 'w-en-imf'),
   ('批判视角', '贷款条件被指加重紧缩与社会代价', 'w-en-washington-consensus')],
  ['w-en-imf', 'w-en-washington-consensus'],
  [('成员国数量', 191, '个（IMF成员国）', 2025,
    '原文：It consists of 191 member countries；单一来源待核实（成员国数随时间变化）。')]),
 ('world-bank', '世界银行集团', '制度',
  '由五个国际组织组成、向发展中国家提供贷款的最大发展银行家族。',
  '世界银行集团（WBG）是由五个国际组织组成的家族，向发展中国家提供杠杆化贷款，是全球最大的发展银行，总部设于美国华盛顿特区。其宣称使命涉及消除贫困与促进共享繁荣。具体机构构成与业务待核实。',
  [('成员国出资与市场融资 → 形成贷款能力', 'w-en-world-bank'),
   ('向发展中国家提供项目与政策贷款', 'w-en-world-bank'),
   ('支持基础设施、减贫与制度改革（效果有争论）', 'w-en-washington-consensus')],
  [('发展融资视角', '世行填补发展融资缺口、提供技术援助', 'w-en-world-bank'),
   ('批判视角', '贷款条件与发展模式受质疑', 'w-en-washington-consensus')],
  ['w-en-world-bank', 'w-en-washington-consensus'],
  [('组成机构数量', 5, '个国际组织（世界银行集团）', 2025,
    '原文：a family of five international organizations；单一来源待核实。')]),
 ('wto', '世界贸易组织(WTO)', '制度',
  '规范与促进国际贸易的政府间组织，1995年1月1日成立。',
  '世界贸易组织（WTO）是规范与促进国际贸易的政府间组织。它依据1994年《马拉喀什协定》于1995年1月1日成立，接替了更早创设的关税与贸易总协定（GATT）。WTO 提供贸易规则框架与争端解决机制。具体职能待核实。',
  [('GATT 谈判成果 → 1994马拉喀什协定', 'w-en-wto'),
   ('1995年1月1日 WTO 成立并接替 GATT', 'w-en-wto'),
   ('以规则与争端解决促进贸易自由化', 'w-en-free-trade')],
  [('规则体系视角', 'WTO 以多边规则降低贸易不确定性', 'w-en-wto'),
   ('批判视角', '规则被认为限制政策空间、争端机制受阻', 'w-en-protectionism')],
  ['w-en-wto', 'w-en-free-trade'],
  [('成立年份', 1995, '年（1995年1月1日）', 1995,
    '原文：Established on 1 January 1995, pursuant to the 1994 Marrakesh Agreement；单一来源待核实。')]),
 ('twin-crises', '双危机', '货币',
  '银行业危机与货币危机同时发生的状况（亦称国际收支危机）。',
  '在经济学中，双危机（亦称国际收支危机）指银行业危机与货币危机同时发生。该术语由经济学家 Graciela Kaminsky 与 Carmen Reinhart 在1990年代末、在若干此类危机于全球出现之后提出。双危机通常比单一危机更严重。具体机制待核实。',
  [('外部冲击或脆弱性 → 货币贬值压力与银行资产恶化并存', 'w-en-twin-crises'),
   ('货币危机与银行危机相互强化', 'w-en-twin-crises'),
   ('产出损失通常大于单一危机', 'w-en-currency-crisis')],
  [('双危机视角', '银行与货币脆弱性相互作用、放大冲击', 'w-en-twin-crises'),
   ('单一危机视角', '分别研究银行或货币危机机制', 'w-en-currency-crisis')],
  ['w-en-twin-crises', 'w-en-currency-crisis'], []),
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
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作S】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r37_concepts.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid == 'banking-crisis':
        continue  # 重定向到 Bank run，已有条目
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
