# -*- coding: utf-8 -*-
"""续作AL：新增14条货币史/金融制度史概念(L2)。"""
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
 dict(id='bill-of-exchange', title='可转让票据（汇票）', cat='制度',
  ol='保证支付特定金额、见票即付或定期支付、通常载明付款人的凭证。',
  ov='可转让票据是一份保证支付特定金额的凭证，或见票即付、或在约定时间支付，付款人通常载明于票据之上。汇票是中世纪以来远程贸易融资的核心工具，可背书转让从而充当信用与支付手段。具体沿革待核实。',
  causal=[('远程贸易需避免运送现金 → 以票据结算','w-en-bill-of-exchange'),
          ('票据可背书转让 → 形成信用流通','w-en-bill-of-exchange'),
          ('票据贴现与再贴现 → 早期货币市场与央行操作','w-en-central-bank')],
  schools=[('信用工具视角','票据扩展了信用与支付体系','w-en-bill-of-exchange'),
           ('货币史视角','票据是信用货币的早期形态','w-en-credit-money')],
  srcs=['w-en-bill-of-exchange','w-en-credit-money']),
 dict(id='double-entry', title='复式记账', cat='制度',
  ol='每笔财务交易都以相等且相反的分录记录、从而"平衡"的记账方法。',
  ov='复式记账（或称复式会计）是一种记账方法：每笔财务交易都以相等且相反的分录记录，从而"平衡"。该方法使资本、损益与资产负债关系清晰可查，被视为现代商业与金融核算的基础。具体沿革待核实。',
  causal=[('每笔交易双分录记录 → 账目自动平衡','w-en-double-entry'),
          ('资产负债与损益关系透明 → 便于审计与管理','w-en-double-entry'),
          ('支撑股份公司与资本市场的信息基础','w-en-joint-stock')],
  schools=[('会计视角','复式记账提升核算可靠性与可审计性','w-en-double-entry'),
           ('经济史视角','被视为资本主义核算理性的技术基础','w-en-institutional-economics')],
  srcs=['w-en-double-entry','w-en-joint-stock']),
 dict(id='joint-stock', title='股份公司', cat='制度',
  ol='股份可由股东买卖的商业实体，每位股东按比例持有公司股份。',
  ov='股份公司（JSC）是一种商业实体，其公司股份可由股东买卖，每位股东按比例持有公司股份并以（股票）为凭证。股份公司实现了资本集中与风险分担，是东印度公司等早期殖民贸易企业与现代资本市场的基础。具体沿革待核实。',
  causal=[('需大规模长期资本 → 以股份募集并分担风险','w-en-joint-stock'),
          ('股份可转让 → 形成二级市场与价格发现','w-en-stock-exchange'),
          ('有限责任与股份流通 → 催生投机泡沫','w-en-south-sea-bubble-1720')],
  schools=[('资本动员视角','股份公司集中资本、分散风险','w-en-joint-stock'),
           ('投机视角','股份可交易也带来泡沫与欺诈','w-en-speculative-bubble')],
  srcs=['w-en-joint-stock','w-en-stock-exchange']),
 dict(id='usury', title='高利贷（重利）', cat='制度',
  ol='被视为不公平地使贷方获利的放贷行为；可从道德或法律意义理解。',
  ov='高利贷是从事被视为不公平地使贷方获利的放贷行为。该词可用于道德意义——谴责利用他人不幸——或用于法律意义（设定利率上限）。历史上对利息的道德与法律态度深刻影响了金融发展。具体沿革待核实。',
  causal=[('对利息的道德/宗教禁令 → 限制信贷供给','w-en-usury'),
          ('或设定法定利率上限 → 影响信贷可及性','w-en-usury'),
          ('金融创新绕开限制 → 票据与信用工具发展','w-en-bill-of-exchange')],
  schools=[('道德/宗教视角','收取过高利息有悖公正','w-en-usury'),
           ('金融视角','利率是资金的价格与风险补偿','w-en-interest-rate')],
  srcs=['w-en-usury','w-en-interest-rate']),
 dict(id='bimetallism', title='复本位制', cat='货币',
  ol='货币单位的价值被定义为两种金属特定数量的货币本位，形成固定比价。',
  ov='复本位制（或称双金属本位）是一种货币本位，其中货币单位的价值被定义为等同于特定数量的两种金属，从而形成（两者之间的）固定比价。复本位制在19世纪引发关于金银比价与货币供给的长期争论（如美国的"自由银币"运动）。具体机制待核实。',
  causal=[('法定金银固定比价 → 形成复本位','w-en-bimetallism'),
          ('市场比价偏离法定比价 → 劣币驱逐良币','w-en-greshams-law'),
          ('转向金本位 → 白银需求与价格剧变','w-en-silver-standard')],
  schools=[('复本位视角','双金属可增加货币供给弹性','w-en-bimetallism'),
           ('金本位视角','单一金属本位更稳定可信','w-en-gold-standard')],
  srcs=['w-en-bimetallism','w-en-greshams-law']),
 dict(id='silver-standard', title='银本位', cat='货币',
  ol='以固定重量白银作为标准记账单位的货币体系。',
  ov='银本位是一种货币体系，其中标准的记账经济单位是一定固定重量的白银。历史上白银作为货币标准在全球远比黄金普遍。19世纪后期主要国家转向金本位，白银地位下降，对银本位国家造成通缩与债务压力。具体沿革待核实。',
  causal=[('以固定重量白银作为记账单位 → 形成银本位','w-en-silver-standard'),
          ('主要国家转向金本位 → 白银货币地位下降','w-en-gold-standard'),
          ('银本位国家面临通缩与偿债压力','w-en-panic-of-1893')],
  schools=[('货币史视角','银本位曾是最普遍的货币标准','w-en-silver-standard'),
           ('本位转换视角','本位转换带来分配与债务冲击','w-en-gold-standard')],
  srcs=['w-en-silver-standard','w-en-gold-standard']),
 dict(id='fiat-money', title='法定货币（法币）', cat='货币',
  ol='由政府发行、一般由央行创造、经法规授权为法定清偿但不以贵金属为支撑的货币。',
  ov='法定货币（法币）是一种政府发行的货币，一般由中央银行创造，经政府法规授权成为法定清偿手段，但不以贵金属作为支撑。法币的价值依赖政府信用与货币政策纪律，因而与通胀控制密切相关。具体论述待核实。',
  causal=[('脱离贵金属支撑 → 货币价值依赖政府信用','w-en-fiat-money'),
          ('发行纪律决定物价稳定','w-en-fiat-money'),
          ('过度发行 → 通胀乃至恶性通胀','w-en-hyperinflation')],
  schools=[('法币视角','信用货币可提供政策弹性','w-en-fiat-money'),
           ('硬通货视角','缺乏约束易导致通胀与贬值','w-en-gold-standard')],
  srcs=['w-en-fiat-money','w-en-hyperinflation']),
 dict(id='legal-tender', title='法定清偿地位', cat='制度',
  ol='法律承认可用于清偿货币债务的货币形式；具体规定因司法辖区而异。',
  ov='法定清偿是一种货币形式，法律承认其在该辖区内可用于清偿货币债务。何种货币构成法定清偿因司法辖区而异。法定清偿地位与"必须接受"并非完全等同，其与合同约定之间的关系在实践中较为复杂。具体规定待核实。',
  causal=[('法律赋予某货币法定清偿地位 → 债权人须接受','w-en-legal-tender'),
          ('强化该货币的流通与接受度','w-en-legal-tender'),
          ('与合同货币选择、外币债务产生交互','w-en-dollarization')],
  schools=[('法律视角','法定清偿界定债务清偿的有效手段','w-en-legal-tender'),
           ('货币竞争视角','实际接受度取决于信心而非仅法律','w-en-fiat-money')],
  srcs=['w-en-legal-tender','w-en-fiat-money']),
 dict(id='commodity-money', title='商品货币', cat='货币',
  ol='价值来自其所由商品的货币；该物自身有价值或用途。',
  ov='商品货币是其价值来自所由商品的货币。商品货币由本身具有价值或用途、同时也具有购买商品价值的物品构成（如金银、贝壳、盐、牲畜）。商品货币的供给受商品生产约束，这是其稳定性的来源与局限。具体沿革待核实。',
  causal=[('商品本身具有价值 → 可充当交换媒介','w-en-commodity-money'),
          ('供给受开采/生产约束 → 货币增长有限','w-en-commodity-money'),
          ('产量冲击（如美洲白银）→ 物价剧烈变动','w-en-kipper-wipper-1618')],
  schools=[('商品货币视角','内在价值提供可信锚','w-en-commodity-money'),
           ('信用货币视角','货币本质是信用关系而非商品','w-en-credit-money')],
  srcs=['w-en-commodity-money','w-en-credit-money']),
 dict(id='representative-money', title='代表货币', cat='货币',
  ol='代表某物价值、但自身几乎无价值的交换媒介（可为实物或数字）。',
  ov='代表货币（或称收据货币）是任何代表某种有价值之物、但自身几乎没有价值的交换媒介，可为实物或数字形式。例如以金银为储备发行的可兑换凭证。代表货币是可兑换性与法币之间的过渡形态。具体沿革待核实。',
  causal=[('以储备资产为支撑发行凭证 → 代表货币','w-en-representative-money'),
          ('凭证可兑换为储备 → 维持平价','w-en-representative-money'),
          ('停止兑换 → 转为法币','w-en-fiat-money')],
  schools=[('可兑换视角','代表货币兼顾便利与硬约束','w-en-representative-money'),
           ('法币视角','脱离兑换后依赖政策纪律','w-en-fiat-money')],
  srcs=['w-en-representative-money','w-en-fiat-money']),
 dict(id='credit-money', title='信用货币理论', cat='理论',
  ol='关于信用与货币之间关系的货币经济理论，亦称债务货币理论。',
  ov='信用货币理论（或称债务货币理论）是关于信用与货币之间关系的货币经济理论。该理论的支持者主张货币本质上源于债权债务关系，而非商品。这一视角与商品货币论、金属主义形成对照，并影响内生货币与现代货币理论。具体论述待核实。',
  causal=[('债权债务关系先于货币 → 货币是信用记账','w-en-credit-money'),
          ('银行信贷创造存款 → 货币供给内生','w-en-endogenous-money'),
          ('危机中信用链条断裂 → 货币收缩','w-en-debt-deflation')],
  schools=[('信用/债务视角','货币本质是信用与债务关系','w-en-credit-money'),
           ('商品货币视角','货币价值源于其商品属性','w-en-commodity-money')],
  srcs=['w-en-credit-money','w-en-endogenous-money']),
 dict(id='token-money', title='名目货币（代币）', cat='货币',
  ol='内在价值低于面值的货币形式；其被接受并非因内在价值。',
  ov='名目货币（或代币）是一种内在价值低于其面值的货币形式。名目货币是指任何因其（法定地位或信用）而非内在价值被接受为货币的东西。现代硬币与纸币在很大程度上属于名目货币。具体沿革待核实。',
  causal=[('面值高于内在价值 → 名目货币','w-en-token-money'),
          ('依法律或信用被接受 → 得以流通','w-en-legal-tender'),
          ('若铸造过滥 → 贬值与通胀','w-en-kipper-wipper-1618')],
  schools=[('名目视角','货币价值来自社会约定与法律','w-en-token-money'),
           ('金属主义视角','货币价值应源于金属含量','w-en-commodity-money')],
  srcs=['w-en-token-money','w-en-legal-tender']),
 dict(id='stock-exchange', title='证券交易所', cat='制度',
  ol='股票经纪人与交易者买卖股票、债券及其他金融工具的场所。',
  ov='证券交易所（或称证券交易市场）是股票经纪人与交易者可以买卖股票、债券及其他金融工具的交易场所。交易所提供流动性、价格发现与清算基础设施，是现代资本市场的核心机构。具体沿革待核实。',
  causal=[('证券需集中交易 → 形成交易所','w-en-stock-exchange'),
          ('提供流动性与价格发现','w-en-stock-exchange'),
          ('投机与杠杆交易 → 泡沫与崩盘的场所','w-en-speculative-bubble')],
  schools=[('市场基础设施视角','交易所降低交易成本、提升流动性','w-en-stock-exchange'),
           ('投机视角','集中交易放大情绪与波动','w-en-speculative-bubble')],
  srcs=['w-en-stock-exchange','w-en-speculative-bubble']),
 dict(id='insurance-history', title='保险史', cat='制度',
  ol='针对货物、财产、死亡、汽车事故与医疗等风险的现代保险业务的发展历程。',
  ov='保险史追溯针对风险的现代保险业务的发展，尤其涉及货物、财产、死亡、汽车事故与医疗等（领域）。海上保险是早期最发达的险种，与远程贸易和金融创新相互促进。保险业的发展为风险管理与资本市场提供了重要工具。具体沿革待核实。',
  causal=[('远程贸易风险 → 催生海上保险','w-en-insurance-history'),
          ('精算与风险分散技术发展 → 保险品种扩展','w-en-insurance-history'),
          ('保险与再保险网络 → 风险跨机构传导','w-en-systemic-risk')],
  schools=[('风险管理视角','保险将个体风险分散至集合','w-en-insurance-history'),
           ('系统性视角','再保险与衍生品使风险高度互联（如AIG案例）','w-en-aig')],
  srcs=['w-en-insurance-history','w-en-systemic-risk']),
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
        'comparison': '货币史/金融制度史概念，与相关案例互补；具体沿革待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体年代与细节待核实。【续作AL】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r57_history.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid == 'bourse':
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
