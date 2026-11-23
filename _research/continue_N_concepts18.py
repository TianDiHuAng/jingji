# -*- coding: utf-8 -*-
"""续作N：新增18条宏观/货币/信息经济学概念(L2,据REST摘要)。"""
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
 ('liquidity-trap', '流动性陷阱', '理论',
  '凯恩斯经济学描述的情形：利率降至一定水平后，流动性偏好近乎绝对，人们宁愿持有现金。',
  '流动性陷阱是凯恩斯经济学描述的情形：当利率已降至某一水平后，流动性偏好可能变得近乎绝对——几乎所有人都宁愿持有现金，而不愿持有收益率如此之低的债务工具。此时常规货币政策难以再刺激需求。具体临界条件与实证待核实。',
  [('利率降至很低水平 → 持现与持债收益相近', 'w-en-liquidity-trap'),
   ('流动性偏好近乎绝对 → 增加货币供给被持币吸收', 'w-en-liquidity-trap'),
   ('货币政策失效 → 需财政政策直接扩张需求', 'w-en-fiscal-policy')],
  [('凯恩斯视角', '流动性陷阱下货币政策传导中断，需财政干预', 'w-en-liquidity-trap'),
   ('货币主义视角', '认为货币供给仍可通过其他渠道影响名义收入', 'w-en-money-supply')],
  ['w-en-liquidity-trap', 'w-en-fiscal-policy'], []),
 ('stagflation', '滞胀', '理论',
  '高通胀、增长停滞与高失业并存的经济状况。',
  '滞胀指高通胀、经济增长停滞与失业率上升同时出现的状况，该词由 "stagnation" 与 "inflation" 合成，由英国政治家 Iain Macleod 在1960年代英国经济困难时期推广（很可能由其创造）。1970年代一系列全球冲击（如1967—1975年苏伊士运河关闭、1973年石油危机）后该现象获得更广泛关注。具体成因与案例待核实。',
  [('供给冲击（如油价飙升）→ 成本上升推高通胀', 'w-en-stagflation'),
   ('同时产出停滞、失业上升 → 通胀与停滞并存', 'w-en-stagflation'),
   ('传统需求管理政策陷入两难（抑通胀则加剧失业）', 'w-en-phillips-curve')],
  [('供给冲击视角', '滞胀源于供给侧冲击而非单纯需求过热', 'w-en-stagflation'),
   ('政策困境视角', '菲利普斯曲线式权衡失效，政策面临两难', 'w-en-phillips-curve')],
  ['w-en-stagflation', 'w-en-phillips-curve'], []),
 ('phillips-curve', '菲利普斯曲线', '理论',
  '描述宏观中失业与通胀之间存在权衡关系的曲线。',
  '菲利普斯曲线表示宏观经济中失业与通胀之间的关系，即低失业与物价稳定之间存在权衡。该曲线由经济学家 Bill Phillips 识别，显示失业下降与工资上升之间的关系；菲利普斯本人并未直接把就业与通胀相联系，但这是从其统计发现中的直接推论。后续学者（如萨缪尔森等）对其进行了发展。具体理论演变待核实。',
  [('失业率下降 → 工资与价格上行压力上升', 'w-en-phillips-curve'),
   ('形成失业-通胀的短期权衡关系', 'w-en-phillips-curve'),
   ('预期调整与供给冲击 → 权衡关系可能失效（如滞胀）', 'w-en-stagflation')],
  [('凯恩斯-新古典综合视角', '短期存在失业与通胀的稳定权衡，可供政策利用', 'w-en-phillips-curve'),
   ('理性预期/货币主义视角', '长期不存在权衡，扩张只带来通胀', 'w-en-monetary-policy')],
  ['w-en-phillips-curve', 'w-en-stagflation'], []),
 ('inflation-targeting', '通胀目标制', '制度',
  '中央银行公开宣布中期通胀目标并以其为货币政策框架的制度。',
  '通胀目标制是一种货币政策框架：中央银行设定并公开宣布中期通胀目标，并以此约束政策。其假设是货币政策对长期经济增长的最好贡献是维持物价稳定，而物价稳定通过控制通胀实现；央行以短期利率作为主要货币政策工具。具体实施差异待核实。',
  [('央行公开宣布中期通胀目标 → 锚定公众预期', 'w-en-inflation-targeting'),
   ('以短期利率为主要工具调节需求与物价', 'w-en-inflation-targeting'),
   ('维持物价稳定以支持长期增长', 'w-en-monetary-policy')],
  [('目标制视角', '明确目标提升政策可信度与预期锚定', 'w-en-inflation-targeting'),
   ('灵活目标制视角', '需兼顾产出与就业，允许一定灵活性', 'w-en-taylor-rule')],
  ['w-en-inflation-targeting', 'w-en-monetary-policy'], []),
 ('taylor-rule', '泰勒规则', '制度',
  '1992年由 John B. Taylor 提出的货币政策目标规则，用于设定短期利率。',
  '泰勒规则是一种货币政策目标规则，1992年由美国经济学家 John B. Taylor 提出，供央行通过恰当设定短期利率来稳定经济活动。该规则考虑联邦基金利率、价格水平与实际收入的变化，依据目标通胀率与实际通胀率之差以及产出缺口来计算最优联邦基金利率。具体系数与适用性待核实。',
  [('观察通胀偏离目标与产出缺口 → 计算合意政策利率', 'w-en-taylor-rule'),
   ('据此调整短期利率以稳定经济', 'w-en-taylor-rule'),
   ('为政策提供可预期的规则化基准', 'w-en-inflation-targeting')],
  [('规则派视角', '规则化政策提升可信度、减少相机抉择的随意性', 'w-en-taylor-rule'),
   ('相机抉择视角', '危机与结构变化时需要灵活判断', 'w-en-monetary-policy')],
  ['w-en-taylor-rule', 'w-en-inflation-targeting'], []),
 ('information-asymmetry', '信息不对称', '理论',
  '交易一方拥有比另一方更多或更好信息的情形。',
  '信息不对称是契约理论、机制设计与经济学中的情形：一方拥有比另一方更多或更好的信息。它是逆向选择、道德风险与委托代理问题的共同根源，也是金融中介与监管存在的理由之一。具体应用待核实。',
  [('一方掌握更多信息 → 交易双方信息地位不对等', 'w-en-information-asymmetry'),
   ('引发逆向选择与道德风险', 'w-en-adverse-selection'),
   ('需要信号、筛选、抵押与监管等机制缓解', 'w-en-credit-rating')],
  [('契约理论视角', '信息不对称是市场失灵与制度设计的核心', 'w-en-information-asymmetry'),
   ('金融中介视角', '银行与评级机构以信息生产缓解不对称', 'w-en-credit-rating')],
  ['w-en-information-asymmetry', 'w-en-adverse-selection'], []),
 ('adverse-selection', '逆向选择', '理论',
  '因信息不对称，一方利用未披露信息从合同或交易中获取更多利益的市场情形。',
  '逆向选择是经济学、保险与风险管理中的市场情形：信息不对称导致一方利用未披露的信息，从合同或交易中获得更多利益。典型如高风险者更倾向购买保险，迫使保费上升、低风险者退出。具体机制与案例待核实。',
  [('信息不对称 → 高风险方更积极签约', 'w-en-adverse-selection'),
   ('低风险方退出、整体风险上升', 'w-en-adverse-selection'),
   ('需筛选、强制参保或差别定价缓解', 'w-en-information-asymmetry')],
  [('保险市场视角', '逆向选择推高保费并可能使市场萎缩', 'w-en-adverse-selection'),
   ('机制设计视角', '以信号与筛选机制分离不同类型', 'w-en-information-asymmetry')],
  ['w-en-adverse-selection', 'w-en-information-asymmetry'], []),
 ('principal-agent', '委托代理问题', '理论',
  '一方代表另一方行动时产生的利益与优先事项冲突。',
  '委托代理问题指当一个人或实体代表另一个人或实体行动时产生的利益与优先事项冲突。当委托人与代理人之间的利益和信息差距越大、且委托人缺乏惩罚代理人的手段时，问题越严重；代理人行为偏离委托人利益的程度称为"代理成本"。具体治理机制待核实。',
  [('委托人授权代理人行动 → 双方利益与信息不一致', 'w-en-principal-agent'),
   ('代理人可能偏离委托人利益 → 产生代理成本', 'w-en-principal-agent'),
   ('需激励合约、监督与治理机制约束', 'w-en-moral-hazard')],
  [('契约/激励视角', '以激励相容合约降低代理成本', 'w-en-principal-agent'),
   ('公司治理视角', '董事会、披露与薪酬设计约束管理层', 'w-en-information-asymmetry')],
  ['w-en-principal-agent', 'w-en-moral-hazard'], []),
 ('maturity-transformation', '期限转换', '银行',
  '金融机构以较短期限借入、以较长期限贷出的做法。',
  '期限转换是金融机构以更短期限借入资金、而以更长期限贷出的做法。金融市场同样具有期限转换效应：股东与债券持有人可在二级市场随时卖出，而发行公司仍能作为长期借款方从短期资金市场中融资。这一功能带来流动性创造，也带来挤兑脆弱性。具体度量待核实。',
  [('短借长贷 → 为长期投资提供融资', 'w-en-maturity-transformation'),
   ('负债端短期可撤回、资产端长期不可变现', 'w-en-maturity-transformation'),
   ('信心动摇时易发生挤兑 → 需存款保险与央行支持', 'w-en-bank-run')],
  [('功能视角', '期限转换是社会融资与流动性创造的核心功能', 'w-en-maturity-transformation'),
   ('脆弱性视角', '期限错配使银行天然易受挤兑冲击', 'w-en-bank-run')],
  ['w-en-maturity-transformation', 'w-en-bank-run'], []),
 ('repo', '回购协议(repo)', '制度',
  '以证券为抵押的短期借款：卖出证券并约定稍后以略高价格回购。',
  '回购协议（repo、RP，或称卖出回购）是一种有担保的短期借款形式，通常（但并非总是）以政府证券作为抵押。交易一方将证券卖给贷款方，并按约定在不久后以略高的约定价格买回；买卖价差与时间间隔构成实际利率。回购市场是货币市场与央行操作的重要环节。具体规模待核实。',
  [('借款人卖出证券换取现金 → 获得短期融资', 'w-en-repo'),
   ('约定稍后以略高价格回购 → 价差形成实际利率', 'w-en-repo'),
   ('抵押品价值波动 → 可能引发追加保证金与挤兑式收缩', 'w-en-credit-crunch')],
  [('货币市场视角', '回购是抵押化短期融资与流动性管理工具', 'w-en-repo'),
   ('系统性风险视角', '抵押品折价与展期风险可在压力下放大冲击', 'w-en-credit-crunch')],
  ['w-en-repo', 'w-en-credit-crunch'], []),
 ('capital-control', '资本管制', '货币',
  '一国政府基于居民身份对资本账户流入流出实施的限制措施。',
  '资本管制是基于居民身份的措施，如交易税、其他限制或直接禁止，用于规范资本市场资金进出本国资本账户。这类措施可适用于整个经济、特定部门或行业，可针对全部资金流动，或按流动类型与期限区别对待。具体效果与争议待核实。',
  [('对跨境资本流动征税或设限 → 减少短期资本冲击', 'w-en-capital-control'),
   ('保留货币政策独立性（在固定汇率下）', 'w-en-impossible-trinity'),
   ('可能降低资本配置效率、推高融资成本', 'w-en-capital-control')],
  [('审慎/稳定视角', '管制可遏制热钱冲击、维护金融稳定', 'w-en-capital-control'),
   ('自由化视角', '管制扭曲配置、提高融资成本', 'w-en-exchange-rate-regime')],
  ['w-en-capital-control', 'w-en-monetary-policy'], []),
 ('dollarization', '美元化（货币替代）', '货币',
  '使用外币与本国货币并行、或替代本国货币的现象。',
  '货币替代（又称美元化）指使用外币与本国货币并行或替代本国货币的现象。常见于高通胀或货币信心崩溃的经济体，可缓解本币贬值与通胀，但会丧失独立货币政策与最后贷款人能力。具体程度与影响待核实。',
  [('本币信心崩溃/高通胀 → 居民与企业转持外币', 'w-en-dollarization'),
   ('外币承担计价、交易与储藏职能', 'w-en-dollarization'),
   ('货币政策自主性下降、铸币税流失', 'w-en-monetary-policy')],
  [('货币替代视角', '美元化是本币信用缺失的市场化应对', 'w-en-dollarization'),
   ('政策约束视角', '美元化削弱独立货币政策与汇率工具', 'w-en-impossible-trinity')],
  ['w-en-dollarization', 'w-en-monetary-policy'], []),
 ('currency-board', '货币局制度', '货币',
  '要求货币当局以外国资产全额支持、维持与外币固定汇率的机制。',
  '货币局制度是一种机制：货币当局须以持有的外国资产（储备）全额支持其承诺，从而维持与某一外币的固定汇率。该政策目标要求把央行的常规目标从属于汇率目标。其可信度较高但丧失货币政策独立性。具体运作待核实。',
  [('以外国储备全额支持本币发行 → 承诺可信', 'w-en-currency-board'),
   ('维持与锚定货币的固定汇率', 'w-en-currency-board'),
   ('央行常规目标从属于汇率目标 → 丧失货币政策独立性', 'w-en-impossible-trinity')],
  [('可信承诺视角', '全额储备支持提升汇率承诺可信度', 'w-en-currency-board'),
   ('政策约束视角', '牺牲货币政策独立性、难以充当最后贷款人', 'w-en-impossible-trinity')],
  ['w-en-currency-board', 'w-en-monetary-policy'], []),
 ('debt-restructuring', '债务重组', '债务',
  '面临现金流问题与财务困境的债务人重新协商、减少拖欠债务的过程。',
  '债务重组是一种过程：允许面临现金流问题与财务困境的私营或上市公司、或主权实体，减少并重新协商其拖欠债务，以改善或恢复流动性从而继续经营。重组形式包括展期、减记与债转股等。具体机制与案例待核实。',
  [('债务人现金流紧张 → 无法按原条款偿付', 'w-en-debt-restructuring'),
   ('与债权人协商展期/减记/转换 → 恢复流动性', 'w-en-debt-restructuring'),
   ('避免清算、维持经营；债权人承担损失', 'w-en-debt-crisis')],
  [('债务可持续视角', '重组在保全经营价值与债权人回收间权衡', 'w-en-debt-restructuring'),
   ('主权债务视角', '主权重组缺乏强制执行机制，依赖协调', 'w-en-sovereign-default')],
  ['w-en-debt-restructuring', 'w-en-debt-crisis'], []),
 ('fiscal-multiplier', '财政乘数', '理论',
  '国民收入（或收入）变化与政府支出变化之比。',
  '财政乘数是国民收入或收入变化相对于政府支出变化的比率；更广义地，外生支出乘数是任何自主性支出变化所引起的国民收入变化之比。当乘数大于1时，对国民收入的放大效应称为乘数效应。其机制是初始增量支出引发后续多轮支出。具体数值待核实。',
  [('政府增加支出 → 直接形成需求', 'w-en-fiscal-multiplier'),
   ('受益者再支出 → 多轮派生需求（乘数效应）', 'w-en-fiscal-multiplier'),
   ('乘数大于1时放大对国民收入的影响', 'w-en-fiscal-policy')],
  [('凯恩斯视角', '衰退期财政乘数较大，扩张政策有效', 'w-en-fiscal-multiplier'),
   ('新古典视角', '挤出与预期因素使乘数较小甚至为零', 'w-en-crowding-out')],
  ['w-en-fiscal-multiplier', 'w-en-fiscal-policy'], []),
 ('crowding-out', '挤出效应', '理论',
  '政府在一个部门的参与增加，实质影响市场经济其余部分（供给或需求侧）的现象。',
  '挤出效应是经济学中的现象：当政府对市场经济的某一部门参与增加时，会实质影响市场的其余部分——或作用于供给侧、或作用于需求侧。常见机制包括政府借贷推高利率、挤占私人投资。其程度存在争议。具体实证待核实。',
  [('政府扩大支出/借贷 → 争夺有限资源与资金', 'w-en-crowding-out'),
   ('利率上升或资源被占用 → 私人投资与消费受抑', 'w-en-crowding-out'),
   ('财政扩张的净效果被部分抵消', 'w-en-fiscal-multiplier')],
  [('古典/新古典视角', '政府借贷推高利率、挤出私人投资', 'w-en-crowding-out'),
   ('凯恩斯视角', '闲置资源条件下挤出有限，乘数效应占优', 'w-en-fiscal-multiplier')],
  ['w-en-crowding-out', 'w-en-fiscal-multiplier'], []),
 ('triffin-dilemma', '特里芬难题', '货币',
  '本币充当全球储备货币的国家在短期国内目标与长期国际目标之间的利益冲突。',
  '特里芬难题是国际金融中的利益冲突：对本国货币充当全球储备货币的国家而言，其短期国内目标与长期国际目标之间存在矛盾。该难题由比利时裔美国经济学家 Robert Triffin 在1960年代提出——储备货币发行国须持续对外供给本币以满足全球储备需求，但这与其国内货币纪律相冲突。具体论述待核实。',
  [('本币充当全球储备货币 → 全球需要其持续外流供给', 'w-en-triffin-dilemma'),
   ('长期对外供给与短期国内货币纪律冲突', 'w-en-triffin-dilemma'),
   ('储备体系内在不稳定性 → 最终引发调整或危机', 'w-en-bretton-woods-system')],
  [('国际货币视角', '储备货币国面临"提供流动性"与"维持信心"的两难', 'w-en-triffin-dilemma'),
   ('体系改革视角', '超主权储备资产可缓解该难题', 'w-en-bretton-woods-system')],
  ['w-en-triffin-dilemma', 'w-en-bretton-woods-system'], []),
 ('output-gap', '产出缺口', '理论',
  '实际GDP（实际产出）与潜在GDP之间的差额。',
  '产出缺口（GDP缺口）是实际GDP或实际产出与潜在GDP之间的差额，用于判断经济在周期中所处的位置，在宏观政策中被广泛使用。该概念受到较多批评，主要因为潜在GDP并非可观测变量，通常由历史GDP数据推导，可能导致系统性的下偏。具体测算待核实。',
  [('实际产出相对潜在产出偏离 → 形成正或负缺口', 'w-en-output-gap'),
   ('负缺口意味着资源闲置、通胀压力较小', 'w-en-output-gap'),
   ('用于判断政策空间（测算争议较大）', 'w-en-fiscal-multiplier')],
  [('周期分析视角', '产出缺口刻画经济过热或闲置程度', 'w-en-output-gap'),
   ('批判视角', '潜在产出不可观测、由历史推导，存在系统性偏误', 'w-en-output-gap')],
  ['w-en-output-gap', 'w-en-fiscal-multiplier'], []),
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
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与学派细节待核实。【续作N】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r32_concepts.json', encoding='utf-8'))
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
