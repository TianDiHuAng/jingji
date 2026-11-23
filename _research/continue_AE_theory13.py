# -*- coding: utf-8 -*-
"""续作AE：新增13条危机理论/国际收支概念(L2,据REST摘要)。"""
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
 ('diamond-dybvig', '戴蒙德-迪布维格模型', '理论',
  '关于银行挤兑的重要模型：银行"非流动资产+流动负债"的组合可引发存款人自我实现的恐慌。',
  '戴蒙德-迪布维格模型是关于银行挤兑及相关金融危机的一个有影响力的模型，由 Douglas Diamond 与 Philip Dybvig 提出。该模型表明，银行的非流动资产与流动负债的组合，可能引发存款人之间自我实现的恐慌：即使银行资产本身健全，只要存款人相信他人会提款，挤兑就成为理性选择。该模型为存款保险与最后贷款人提供了理论依据。具体推导待核实。',
  [('银行以流动负债为长期非流动资产融资 → 期限转换', 'w-en-diamond-dybvig'),
   ('存款人担忧他人提款 → 抢先提款成为理性选择', 'w-en-diamond-dybvig'),
   ('自我实现的挤兑 → 银行被迫贱卖资产、危机实现', 'w-en-bank-run')],
  [('多重均衡视角', '挤兑是坏均衡，可由预期自我实现', 'w-en-diamond-dybvig'),
   ('政策视角', '存款保险与央行流动性支持可消除挤兑均衡', 'w-en-deposit-insurance')],
  ['w-en-diamond-dybvig', 'w-en-bank-run'], []),
 ('speculative-attack', '投机攻击', '货币',
  '此前不活跃的投机者突然抛售不可信资产并相应获取有价值资产的行为。',
  '在经济学中，投机攻击是此前并不活跃的投机者对不可信资产（如某国货币）的急剧抛售，并相应地获取某些有价值资产。第一个投机攻击模型出现在1975年的一篇讨论中。投机攻击是货币危机理论的核心机制。具体模型待核实。',
  [('某货币或资产被视为不可信 → 投机者预期贬值', 'w-en-speculative-attack'),
   ('集中抛售该资产、换入硬通货 → 储备迅速流失', 'w-en-speculative-attack'),
   ('当局耗尽储备 → 被迫贬值或放弃钉住', 'w-en-currency-crisis')],
  [('基本面视角', '攻击发生在基本面已不可持续之时', 'w-en-speculative-attack'),
   ('多重均衡视角', '攻击可自我实现、与基本面无关', 'w-en-self-fulfilling')],
  ['w-en-speculative-attack', 'w-en-currency-crisis'], []),
 ('self-fulfilling', '自我实现的预言', '理论',
  '因人们相信某预测会成真、并据此行动而使其部分成真的现象。',
  '自我实现的预言是一种预测，它至少部分地因人们相信该预测会成真而实现。在这一现象中，人们倾向于按他人对自己的预期行事，从而使预期成真。该概念是理解银行挤兑、货币攻击与多重均衡危机的关键。具体论述待核实。',
  [('形成某种预期或预言 → 主体据此改变行为', 'w-en-self-fulfilling'),
   ('行为改变使预言条件成立 → 预言实现', 'w-en-self-fulfilling'),
   ('危机可因此成为"坏均衡"而非基本面必然', 'w-en-coordination-games')],
  [('预期视角', '预期本身可改变结果，形成多重均衡', 'w-en-self-fulfilling'),
   ('基本面视角', '预言成真反映的是既存失衡', 'w-en-speculative-attack')],
  ['w-en-self-fulfilling', 'w-en-coordination-games'], []),
 ('fiscal-space', '财政空间', '债务',
  '政府在支出选择上的灵活性，更广义指政府的财政稳健程度。',
  '财政空间是政府在支出选择上的灵活性，更一般地指政府的财政健康状况。Peter Heller（2005）将其定义为"政府预算中的余裕，使其能够为预期需求提供资源"。财政空间的大小取决于债务水平、利率、增长与市场信心。具体度量待核实。',
  [('债务水平与利息负担 → 决定可动用的财政余裕', 'w-en-fiscal-space'),
   ('财政空间充足 → 危机时可扩张支出', 'w-en-fiscal-space'),
   ('空间耗尽 → 被迫紧缩、加剧下行', 'w-en-debt-crisis')],
  [('政策空间视角', '财政空间决定反周期能力', 'w-en-fiscal-space'),
   ('可持续性视角', '空间随市场信心与利率变化而收缩', 'w-en-debt-crisis')],
  ['w-en-fiscal-space', 'w-en-government-debt'], []),
 ('current-account', '经常账户', '货币',
  '记录一国商品与服务进出口及国际转移价值的账户，是国际收支两大组成部分之一。',
  '在宏观经济学与国际金融中，一国经常账户记录商品与服务进出口的价值以及国际转移。它是国际收支的两个组成部分之一，另一个是资本（与金融）账户。经常账户差额反映储蓄与投资的缺口。具体口径待核实。',
  [('商品与服务贸易 + 国际转移 → 记录于经常账户', 'w-en-current-account'),
   ('经常账户差额 = 储蓄 − 投资（恒等式）', 'w-en-current-account'),
   ('持续逆差需由资本流入弥补 → 外部脆弱性', 'w-en-sudden-stop')],
  [('收支视角', '经常账户反映实体贸易与转移', 'w-en-current-account'),
   ('储蓄-投资视角', '差额根源于国内储蓄与投资失衡', 'w-en-global-imbalances')],
  ['w-en-current-account', 'w-en-balance-of-payments'], []),
 ('twin-deficits', '双赤字假说', '债务',
  '认为政府预算平衡与经常账户平衡之间存在强因果联系的理论观察。',
  '在宏观经济学中，双赤字假说（或双赤字现象）是一种观察：理论上，一国的政府预算平衡与其经常账户平衡之间存在强因果联系——财政赤字扩大往往伴随经常账户赤字扩大。该假说在实证上存在争议。具体论述待核实。',
  [('财政赤字扩大 → 国内吸收上升、储蓄下降', 'w-en-twin-deficits'),
   ('进口增加、资本流入 → 经常账户恶化', 'w-en-twin-deficits'),
   ('形成"双赤字"并存（实证存在争议）', 'w-en-current-account')],
  [('双赤字视角', '财政赤字通过吸收渠道传导至经常账户', 'w-en-twin-deficits'),
   ('质疑视角', '私人储蓄与汇率调整可削弱该联系', 'w-en-ricardian-equivalence')],
  ['w-en-twin-deficits', 'w-en-current-account'], []),
 ('devaluation', '贬值（法定贬值）', '货币',
  '固定汇率制下货币当局正式下调本币汇率的官方行为。',
  '在宏观经济学与现代货币政策中，贬值指在固定汇率体系内官方下调一国货币的价值，即货币当局正式设定本币对外币更低的汇率。贬值可改善贸易竞争力，但会推高进口成本与外币债务负担。具体影响待核实。',
  [('国际收支持续逆差或储备流失 → 维持平价困难', 'w-en-devaluation'),
   ('当局正式下调本币汇率 → 法定贬值', 'w-en-devaluation'),
   ('出口竞争力改善、进口与外币债务负担上升', 'w-en-currency-crisis')],
  [('调整视角', '贬值是纠正汇率高估的必要调整', 'w-en-devaluation'),
   ('代价视角', '贬值推高通胀与外币债务负担', 'w-en-currency-crisis')],
  ['w-en-devaluation', 'w-en-currency-crisis'], []),
 ('capital-account', '资本账户', '货币',
  '记录流入一国经济的投资净额，是国际收支两大主要组成部分之一。',
  '在宏观经济学与国际金融中，资本账户（亦称资本与金融账户）记录流入一国经济的投资净额。它是国际收支的两大主要组成部分之一，另一为经常账户。资本账户的开放程度直接影响一国对资本流动冲击的暴露。具体口径待核实。',
  [('跨境投资流入与流出 → 记录于资本账户', 'w-en-capital-account'),
   ('与经常账户共同构成国际收支', 'w-en-balance-of-payments'),
   ('开放度越高对突然停止越敏感', 'w-en-sudden-stop')],
  [('开放视角', '资本账户开放可引入外资与技术', 'w-en-capital-account'),
   ('审慎视角', '过快开放增加资本流动冲击风险', 'w-en-capital-control')],
  ['w-en-capital-account', 'w-en-balance-of-payments'], []),
 ('financial-innovation', '金融创新', '制度',
  '创造新的金融工具以及新的金融技术、机构与市场的行为。',
  '金融创新是创造新的金融工具以及新的金融技术、机构与市场的行为。近期的金融创新包括对冲基金、私募股权、天气衍生品、零售结构化产品等。金融创新提升效率与风险管理能力，但也可能累积未被充分理解的复杂性风险。具体案例待核实。',
  [('技术进步与监管/竞争压力 → 催生新工具与市场', 'w-en-financial-innovation'),
   ('新工具改善风险分担与融资效率', 'w-en-financial-innovation'),
   ('复杂性上升、透明度和监管滞后 → 风险累积', 'w-en-systemic-risk')],
  [('创新视角', '金融创新提升效率与风险管理', 'w-en-financial-innovation'),
   ('审慎视角', '复杂性可能在危机中放大传染', 'w-en-systemic-risk')],
  ['w-en-financial-innovation', 'w-en-systemic-risk'], []),
 ('financial-fragility', '金融脆弱性', '理论',
  '金融体系对金融危机的易感程度，即小冲击可能带来不成比例的大影响。',
  '金融脆弱性是金融体系对金融危机的脆弱程度。Franklin Allen 与 Douglas Gale 将金融脆弱性定义为"小冲击产生不成比例的巨大影响"的程度。该概念是明斯基金融不稳定假说与宏观审慎监管的核心。具体论述待核实。',
  [('杠杆、期限与流动性错配 → 体系结构脆弱', 'w-en-financial-fragility'),
   ('小冲击经金融摩擦放大 → 不成比例的影响', 'w-en-financial-accelerator'),
   ('脆弱性累积 → 系统性危机概率上升', 'w-en-systemic-risk')],
  [('金融脆弱性视角', '结构性错配使体系易受小冲击放大', 'w-en-financial-fragility'),
   ('明斯基视角', '稳定期孕育不稳定、脆弱性内生累积', 'w-en-minsky-theory')],
  ['w-en-financial-fragility', 'w-en-minsky-theory'], []),
 ('credit-cycle', '信贷周期', '理论',
  '信贷获取随时间扩张与收缩的过程。',
  '信贷周期是信贷获取随时间扩张与收缩的过程。包括 Barry Eichengreen、Hyman Minsky 及其他后凯恩斯经济学家以及奥地利学派成员在内的部分经济学家，将信贷周期视为（经济周期的）核心驱动。信贷周期与杠杆周期相互作用。具体论述待核实。',
  [('信贷条件宽松 → 借贷与资产价格上升', 'w-en-credit-cycle'),
   ('风险积累与政策收紧 → 信贷收缩', 'w-en-credit-cycle'),
   ('信贷收缩加深下行（金融加速器）', 'w-en-financial-accelerator')],
  [('后凯恩斯/奥地利视角', '信贷周期是经济周期的核心', 'w-en-credit-cycle'),
   ('主流视角', '信贷是冲击的传导渠道而非根源', 'w-en-financial-accelerator')],
  ['w-en-credit-cycle', 'w-en-leverage'], []),
 ('leverage-cycle', '杠杆周期', '理论',
  '杠杆（资产价值与购买所需现金之比）在经济周期中的顺周期扩张与收缩。',
  '杠杆被定义为资产价值与购买该资产所需现金之比。杠杆周期可定义为杠杆在经济周期过程中的顺周期扩张与收缩。顺周期杠杆的存在意味着资产价格上涨时杠杆上升、下跌时被迫去杠杆，从而放大波动。具体机制待核实。',
  [('资产价格上涨 → 抵押价值上升、杠杆可提高', 'w-en-leverage-cycle'),
   ('杠杆顺周期扩张 → 进一步推高资产价格', 'w-en-leverage-cycle'),
   ('价格下跌 → 抵押品贬值、强制去杠杆与抛售', 'w-en-deleveraging')],
  [('杠杆周期视角', '杠杆顺周期性内生放大繁荣与萧条', 'w-en-leverage-cycle'),
   ('保证金视角', '保证金要求变化强化顺周期性', 'w-en-margin-finance')],
  ['w-en-leverage-cycle', 'w-en-leverage'], []),
 ('currency-union', '货币联盟', '货币',
  '两个或多个国家共享同一货币的政府间协议。',
  '货币联盟是一项政府间协议，涉及两个或多个国家共享同一种货币；这些国家未必在其他方面有更深入的一体化。货币联盟使成员国放弃独立货币政策，因而缺乏对本国特定冲击的汇率与利率调节手段。具体机制待核实。',
  [('多国协议共享同一货币 → 形成货币联盟', 'w-en-currency-union'),
   ('成员国放弃独立货币政策与汇率工具', 'w-en-currency-union'),
   ('面对非对称冲击时缺乏调节手段 → 需财政转移或调整', 'w-en-euro-area-crisis')],
  [('一体化视角', '共同货币降低交易成本、促进贸易', 'w-en-currency-union'),
   ('最优货币区视角', '需要素流动与财政一体化配套', 'w-en-impossible-trinity')],
  ['w-en-currency-union', 'w-en-euro-area-crisis'], []),
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
        'comparison': '金融危机/国际收支理论概念，与其他概念互补；具体争论待核实。',
        'svg': svg(title, [causal[0][0][:12], causal[1][0][:12], causal[2][0][:12]]),
        'sources': list(dict.fromkeys(srcs)), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作AE】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r50_concepts.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid == 'overvaluation':
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
