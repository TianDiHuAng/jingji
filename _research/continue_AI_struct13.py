# -*- coding: utf-8 -*-
"""续作AI：新增13条结构化金融与市场基础设施概念(L2)。"""
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
 dict(id='tranche', title='分层(tranche)', cat='制度',
  ol='结构化金融中，同一笔交易下发行的若干相关证券之一，各代表该交易风险的不同切片。',
  ov='在结构化金融中，分层（tranche）是作为同一交易的一部分而发行的若干相关证券之一。就金融意义而言，每一档债券都是该交易风险的不同切片：优先级先获偿付、次级先承担损失。分层是 CDO 与 MBS 的核心结构。具体结构待核实。',
  causal=[('汇集底层资产现金流 → 按优先级切分为多档','w-en-tranche'),
          ('优先级先获偿付、股权档先担损失','w-en-tranche'),
          ('底层违约上升 → 次级各档依次受损','w-en-collateralized-debt-obligation')],
  schools=[('结构化视角','分层满足不同风险偏好','w-en-tranche'),
           ('风险放大视角','分层与评级依赖掩盖了相关性风险','w-en-systemic-risk')],
  srcs=['w-en-tranche','w-en-collateralized-debt-obligation']),
 dict(id='collateral', title='抵押品', cat='制度',
  ol='借款人为担保贷款偿还而向贷款方质押的特定财产。',
  ov='在借贷协议中，抵押品是借款人向贷款方质押特定财产以担保贷款偿还的安排。抵押品为贷款方提供防范借款人违约的保护，并在违约时可就其受偿。抵押品价值波动直接影响融资能力与保证金要求。具体规则待核实。',
  causal=[('借款人质押财产 → 贷款方获得违约保护','w-en-collateral'),
          ('抵押品价值下跌 → 融资能力下降、需追加保证金','w-en-collateral'),
          ('集中抛售抵押品 → 价格螺旋下跌','w-en-fire-sale')],
  schools=[('风险缓释视角','抵押品降低信用风险与融资成本','w-en-collateral'),
           ('顺周期视角','抵押品估值顺周期放大波动','w-en-leverage-cycle')],
  srcs=['w-en-collateral','w-en-credit-risk']),
 dict(id='haircut-finance', title='折扣(haircut)', cat='制度',
  ol='资产市值与其用于计算监管资本或贷款抵押时所计价值之间的差额。',
  ov='在金融中，折扣（haircut）是资产当前市场价值与该资产在计算监管资本或作为贷款抵押时所被赋予价值之间的差额。折扣反映抵押品价格波动与流动性风险，压力时期折扣上升会收紧融资。具体规则待核实。',
  causal=[('抵押品存在价格与流动性风险 → 融资时打折计价','w-en-haircut-finance'),
          ('折扣上升 → 同等抵押品可借资金减少','w-en-haircut-finance'),
          ('压力期折扣骤升 → 强制去杠杆与贱卖','w-en-deleveraging')],
  schools=[('审慎视角','折扣防范抵押品价值下跌损失','w-en-haircut-finance'),
           ('顺周期视角','折扣在压力期上升、放大紧缩','w-en-leverage-cycle')],
  srcs=['w-en-haircut-finance','w-en-repo']),
 dict(id='fire-sale', title='贱卖(fire sale)', cat='制度',
  ol='以极低折扣价格出售商品或资产的行为。',
  ov='贱卖（fire sale）是以极低折扣价格出售商品的行为，该词最初源于因火灾受损而以大折扣出售货物。在金融中，贱卖指机构在压力下被迫快速出售资产、接受远低于内在价值的价格，从而加剧价格下跌。具体机制待核实。',
  causal=[('流动性需求紧迫 → 被迫快速出售资产','w-en-fire-sale'),
          ('买家稀少、须大幅折价成交','w-en-fire-sale'),
          ('贱卖价格被用作估值基准 → 传染与螺旋','w-en-mark-to-market')],
  schools=[('流动性视角','贱卖反映流动性溢价急剧上升','w-en-fire-sale'),
           ('会计传染视角','市值计价把贱卖价格传导至其他机构','w-en-mark-to-market')],
  srcs=['w-en-fire-sale','w-en-liquidity']),
 dict(id='mark-to-market', title='市值计价（公允价值会计）', cat='制度',
  ol='按当前市场价格（或类似资产价格）计量资产或负债"公允价值"的会计方法。',
  ov='市值计价（或称公允价值会计）是依据当前市场价格、或类似资产与负债的价格、或其他（估值方法）来计量资产或负债"公允价值"的会计方法。它在危机中被批评为放大顺周期波动（贱卖价格被立即确认），支持者则强调透明度。具体规则待核实。',
  causal=[('按市价计量资产 → 价格下跌即时反映为损失','w-en-mark-to-market'),
          ('资本受侵蚀 → 被动抛售以满足要求','w-en-fire-sale'),
          ('抛售压低价格 → 进一步减值（顺周期螺旋）','w-en-leverage-cycle')],
  schools=[('透明视角','市值计价及时揭示风险、避免掩盖损失','w-en-mark-to-market'),
           ('顺周期视角','危机中贱卖价格被机械确认、放大螺旋','w-en-fire-sale')],
  srcs=['w-en-mark-to-market','w-en-fire-sale']),
 dict(id='off-balance-sheet', title='表外（表外杠杆）', cat='制度',
  ol='未列示于公司资产负债表上的资产、债务或融资活动，亦称隐性杠杆。',
  ov='在会计中，"表外"（OBS，或称隐性杠杆）通常描述未列示于公司资产负债表上的资产、债务或融资活动。总收益互换即为表外安排的一个例子。表外结构可掩盖真实杠杆，是安然事件与2008危机中的重要问题。具体规则待核实。',
  causal=[('通过特殊实体转移资产或负债 → 不列示于资产负债表','w-en-off-balance-sheet'),
          ('真实杠杆被低估 → 风险隐蔽累积','w-en-off-balance-sheet'),
          ('风险暴露后集中暴露 → 信任崩塌','w-en-enron')],
  schools=[('透明视角','表外结构损害信息可比性与监管有效性','w-en-off-balance-sheet'),
           ('业务视角','部分表外安排具有真实经济目的（如资产证券化）','w-en-spv')],
  srcs=['w-en-off-balance-sheet','w-en-spv']),
 dict(id='spv', title='特殊目的实体(SPE/SPV)', cat='制度',
  ol='为实现狭窄、特定或临时目标而设立的法律实体。',
  ov='特殊目的实体（SPE，亦称特殊目的载体 SPV 或金融载体公司 FVC）是为实现狭窄、特定或临时目标而设立的法律实体。SPE 常用于资产证券化、项目融资与风险隔离，但也可能被用于表外融资而掩盖风险。具体用法待核实。',
  causal=[('设立隔离实体持有特定资产 → 实现破产隔离','w-en-spv'),
          ('发起人转移资产 → 可能形成表外融资','w-en-off-balance-sheet'),
          ('若风险未被充分披露 → 危机中集中暴露','w-en-enron')],
  schools=[('风险隔离视角','SPE 实现破产隔离与定向融资','w-en-spv'),
           ('透明度视角','SPE 易被用于隐藏杠杆','w-en-off-balance-sheet')],
  srcs=['w-en-spv','w-en-off-balance-sheet']),
 dict(id='rwa', title='风险加权资产(RWA)', cat='制度',
  ol='按风险加权的银行资产，含留存分层与表外敞口，用于确定资本要求。',
  ov='风险加权资产（RWA）是银行的资产，包括留存的分层与表外敞口，并按风险加以加权。这类资产计算被用于确定（银行的）资本要求。RWA 是巴塞尔资本充足率的分母，其计量方法（标准法/内部模型法）存在争论。具体规则待核实。',
  causal=[('识别资产风险权重 → 计算风险加权资产','w-en-rwa'),
          ('以 RWA 为分母计算资本充足率','w-en-rwa'),
          ('权重低估风险 → 资本要求不足','w-en-capital-requirement')],
  schools=[('审慎视角','风险加权使资本与风险相匹配','w-en-rwa'),
           ('批判视角','内部模型可能低估权重、形成监管套利','w-en-basel-iii')],
  srcs=['w-en-rwa','w-en-capital-requirement']),
 dict(id='seniority', title='优先级（清偿顺序）', cat='制度',
  ol='发行人出售或破产时债务的偿付顺序；优先级债务须先于次级债务偿付。',
  ov='在金融中，优先级指在发行人出售或破产时偿付的顺序。它可适用于债务或优先股：优先级债务必须在次级债务之前获得偿付。清偿顺序决定了不同证券持有人的风险与收益，是结构化金融与资本结构设计的核心。具体规则待核实。',
  causal=[('设定偿付顺序 → 划分优先级与次级','w-en-seniority'),
          ('违约时先偿优先级 → 次级承担首损','w-en-seniority'),
          ('清偿顺序影响各档定价与评级','w-en-tranche')],
  schools=[('风险分层视角','清偿顺序将风险分配给不同偏好者','w-en-seniority'),
           ('危机视角','误判相关性使"优先级"亦可能受损','w-en-collateralized-debt-obligation')],
  srcs=['w-en-seniority','w-en-tranche']),
 dict(id='credit-enhancement', title='信用增级', cat='制度',
  ol='改善结构化金融交易或其产品信用状况的方法。',
  ov='信用增级是改善结构化金融交易信用状况、或用于改善此类产品与交易信用状况的方法。它是结构化金融的关键环节，常见手段包括超额抵押、次级分层、担保与保险。信用增级的效果依赖其真实性与相关性假设。具体方式待核实。',
  causal=[('以超额抵押/次级档/担保等方式 → 提升优先级信用','w-en-credit-enhancement'),
          ('评级随之提高 → 吸引更多投资者','w-en-credit-enhancement'),
          ('底层相关性上升 → 增级可能不足','w-en-collateralized-debt-obligation')],
  schools=[('结构化视角','信用增级扩大投资者基础','w-en-credit-enhancement'),
           ('批判视角','模型低估尾部相关性使增级失效','w-en-systemic-risk')],
  srcs=['w-en-credit-enhancement','w-en-tranche']),
 dict(id='capital-structure', title='资本结构', cat='制度',
  ol='企业用于融资的各种外部资金形式的组合，包括股东权益、债务与优先股。',
  ov='在公司金融中，资本结构指企业用于融资的各种外部资金形式（即资本）的组合，包括股东权益、债务与优先股。资本结构影响企业的风险、成本与清偿顺序，其最优选择是公司金融的核心议题之一。具体理论待核实。',
  causal=[('选择股权与债务的比例 → 形成资本结构','w-en-capital-structure'),
          ('债务占比上升 → 杠杆与财务风险上升','w-en-leverage'),
          ('压力下高杠杆企业更易违约','w-en-leverage-cycle')],
  schools=[('权衡理论视角','在税盾收益与财务困境成本间权衡','w-en-capital-structure'),
           ('MM 视角','无摩擦条件下资本结构不影响价值','w-en-leverage')],
  srcs=['w-en-capital-structure','w-en-leverage']),
 dict(id='netting', title='净额结算（抵销）', cat='制度',
  ol='在互有债权债务的双方之间以净头寸替代总头寸的法律技术。',
  ov='在法律中，净额结算（或抵销，set-off）是应用于互有权利与负债的各方之间的一种法律技术：以净头寸替代总头寸。它允许（一方）以自身债权抵销负债。净额结算降低了衍生品市场的对手方敞口，是中央清算的基础。具体规则待核实。',
  causal=[('双方互有债权债务 → 以净额替代总额','w-en-netting'),
          ('对手方敞口下降 → 系统性风险降低','w-en-netting'),
          ('跨境净额可执行性存疑 → 危机中或失效','w-en-central-counterparty')],
  schools=[('风险缓释视角','净额结算显著降低敞口','w-en-netting'),
           ('法律风险视角','跨境破产中净额效力不确定','w-en-central-counterparty')],
  srcs=['w-en-netting','w-en-central-counterparty']),
 dict(id='central-counterparty', title='中央对手方(CCP)', cat='制度',
  ol='承担交易双方对手方信用风险的金融市场基础设施机构。',
  ov='中央对手方（CCP）是一种金融市场基础设施机构，它承担交易各方的对手方信用风险。CCP 通过多边净额、保证金与违约瀑布管理风险，被危机后监管改革广泛采用以减少对手方网络风险；但其自身也成为风险集中点。具体机制待核实。',
  causal=[('交易双方通过 CCP 清算 → CCP 成为共同对手方','w-en-central-counterparty'),
          ('以多边净额与保证金管理风险','w-en-netting'),
          ('成员违约时动用违约瀑布 → CCP 自身成风险集中点','w-en-systemic-risk')],
  schools=[('稳定视角','CCP 降低网络关联与对手方风险','w-en-central-counterparty'),
           ('集中风险视角','CCP 失败将成为系统性事件','w-en-sifi')],
  srcs=['w-en-central-counterparty','w-en-systemic-risk']),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': [],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [],
        'comparison': '结构化金融/市场基础设施概念，与相关理论及2008危机案例互补；具体适用待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作AI】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r54_concepts.json', encoding='utf-8'))
used = {'tranche','collateral','haircut-finance','fire-sale','mark-to-market','off-balance-sheet',
        'spv','rwa','seniority','credit-enhancement','capital-structure','netting','central-counterparty'}
for eid, v in meta.items():
    if eid not in used:
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
for sp in D:
    if sp['id'] in have:
        continue
    cov['entries'].append({
        'id': sp['id'], 'level': 'L2', 'tier': '重要', 'status': 'written',
        'source_count': len(sp['srcs']), 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
