# -*- coding: utf-8 -*-
"""续作AH：新增10条金融技术概念(L2,据REST摘要)。使用dict结构避免元组长度问题。"""
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
 dict(id='sovereign-risk', title='主权信用风险', cat='债务',
  ol='一国政府不愿或无法履行其贷款或债券义务、导致主权违约的风险。',
  ov='主权信用风险是一国政府变得不愿或无法履行其贷款或债券义务、从而导致主权违约的风险。信用评级机构在评估时会考虑（经济、财政与政治因素）。该风险通过主权债收益率与信用违约互换等价格体现。具体度量待核实。',
  causal=[('财政与外部失衡累积 → 偿付能力受质疑','w-en-sovereign-risk'),
          ('市场要求更高风险溢价 → 融资成本上升','w-en-sovereign-risk'),
          ('融资中断或拒付 → 主权违约','w-en-sovereign-default')],
  schools=[('偿付能力视角','风险源于财政与外部基本面','w-en-sovereign-risk'),
           ('信心/自我实现视角','风险溢价上升本身可致违约','w-en-self-fulfilling')],
  srcs=['w-en-sovereign-risk','w-en-sovereign-default']),
 dict(id='country-risk', title='国家风险', cat='制度',
  ol='在某国投资或放贷的风险，源于商业环境可能的不利变化。',
  ov='国家风险指在某国投资或放贷的风险，它源于商业环境可能发生的不利变化，这些变化可能损害在该国的营业利润或资产价值。国家风险涵盖政治、经济、主权与转移（汇兑）风险等维度。具体评估方法待核实。',
  causal=[('政治或政策环境变化 → 商业环境恶化','w-en-country-risk'),
          ('利润与资产价值受损','w-en-country-risk'),
          ('跨境投资者要求更高回报或退出','w-en-capital-flight')],
  schools=[('风险溢价视角','国家风险通过更高要求回报定价','w-en-country-risk'),
           ('分散化视角','跨国分散可降低特定国家风险','w-en-globalization')],
  srcs=['w-en-country-risk','w-en-capital-flight']),
 dict(id='basis-point', title='基点(bp)', cat='制度',
  ol='一个基点为1个百分点的百分之一，即0.01%。',
  ov='一个基点（basis point）是1个百分点的百分之一，即0.01%。利率变化常以基点表示。例如，若既有利率10%上升1个基点，则新利率为10.01%。基点是描述利差与政策变动的标准单位。具体用法待核实。',
  causal=[('利率或利差发生变动 → 以基点计量幅度','w-en-basis-point'),
          ('1个基点 = 0.01个百分点','w-en-basis-point'),
          ('便于精确表达小幅政策调整与利差','w-en-interest-rate')],
  schools=[('市场惯例视角','基点避免"百分点"与"百分比"的混淆','w-en-basis-point'),
           ('政策视角','央行调整常以25个基点为单位','w-en-monetary-policy')],
  srcs=['w-en-basis-point','w-en-interest-rate']),
 dict(id='duration-finance', title='久期', cat='制度',
  ol='衡量固定收益工具价格对利率变化响应程度的指标。',
  ov='在金融中，久期是衡量固定收益工具价格对利率变化响应程度的指标。它被用于比较不同债券之间的利率风险并构建对冲，且常与凸性配对使用。久期越长，债券价格对利率变动越敏感。具体计算待核实。',
  causal=[('债券现金流期限结构 → 决定久期','w-en-duration-finance'),
          ('久期越长 → 对利率变动越敏感','w-en-duration-finance'),
          ('利率上升 → 长久期债券价格跌幅更大','w-en-interest-rate')],
  schools=[('利率风险视角','久期是利率风险的核心度量','w-en-duration-finance'),
           ('免疫/对冲视角','匹配资产负债久期可降低利率风险','w-en-1994-bond-crisis')],
  srcs=['w-en-duration-finance','w-en-interest-rate']),
 dict(id='convexity', title='凸性', cat='制度',
  ol='金融模型中价格对标的变量变化的非线性响应。',
  ov='在数理金融中，凸性指金融模型中的非线性：当标的变量的价格变化时，输出价格并非线性变化，而是取决于（该变量的变动幅度与曲率）。凸性是对久期的一阶近似的补充，用于更精确地估计债券价格对利率变动的反应。具体推导待核实。',
  causal=[('标的变量变动 → 价格非线性响应','w-en-convexity'),
          ('久期仅为一阶近似 → 需凸性修正','w-en-convexity'),
          ('大幅利率变动时估计误差更依赖凸性','w-en-duration-finance')],
  schools=[('二阶近似视角','凸性提高价格敏感性估计精度','w-en-convexity'),
           ('风险管理视角','凸性可正可负，影响对冲有效性','w-en-value-at-risk')],
  srcs=['w-en-convexity','w-en-duration-finance']),
 dict(id='money-creation', title='货币创造', cat='货币',
  ol='一国或经济区货币供给增加的过程。',
  ov='货币创造（或货币发行）是一国或经济区货币供给增加的过程。在多数现代经济中，中央银行与商业银行都创造货币：央行创造基础货币，商业银行通过放贷派生存款。理解货币创造机制对分析通胀与信贷周期至关重要。具体机制待核实。',
  causal=[('央行投放基础货币 → 银行体系获得准备金','w-en-money-creation'),
          ('银行放贷派生存款 → 广义货币扩张','w-en-money-creation'),
          ('信贷扩张 → 总需求与物价压力','w-en-inflation')],
  schools=[('内生货币视角','货币由信贷需求内生创造','w-en-endogenous-money'),
           ('外生视角','央行可通过基础货币控制货币总量','w-en-money-multiplier')],
  srcs=['w-en-money-creation','w-en-money-supply']),
 dict(id='endogenous-money', title='内生货币', cat='货币',
  ol='货币供给由其他经济变量相互作用内生决定，而非由外部权威外生设定。',
  ov='内生货币指一个经济的货币供给是内生决定的——即由其他经济变量的相互作用所决定，而不是由外部权威外生地（自主地）设定。该观点强调银行信贷需求在货币创造中的主导作用，与货币乘数的外生视角形成对照。具体论述待核实。',
  causal=[('企业信贷需求上升 → 银行放贷创造存款','w-en-endogenous-money'),
          ('货币供给随信贷需求扩张 → 内生增加','w-en-endogenous-money'),
          ('央行通过利率与准备金间接影响而非直接控制数量','w-en-monetary-policy')],
  schools=[('后凯恩斯/内生视角','贷款创造存款，货币供给内生','w-en-endogenous-money'),
           ('货币主义视角','央行可通过基础货币控制货币总量','w-en-money-multiplier')],
  srcs=['w-en-endogenous-money','w-en-money-creation']),
 dict(id='loanable-funds', title='可贷资金理论', cat='理论',
  ol='把银行贷款视为非银行储蓄者与非银行借款人之间真实储蓄中介的理论。',
  ov='在经济学中，"可贷资金理论"是把银行贷款视为在非银行储蓄者与非银行借款人之间对真实储蓄（即可贷资金）进行中介的理论。该理论以利率为可贷资金供求的均衡价格，与流动性偏好理论形成对照。具体论述待核实。',
  causal=[('储蓄者提供可贷资金 → 形成资金供给','w-en-loanable-funds'),
          ('借款人需求资金 → 形成资金需求','w-en-loanable-funds'),
          ('利率调节供求至均衡','w-en-interest-rate')],
  schools=[('可贷资金视角','利率由储蓄与投资决定','w-en-loanable-funds'),
           ('流动性偏好视角','利率由货币供求与流动性偏好决定','w-en-liquidity-preference')],
  srcs=['w-en-loanable-funds','w-en-interest-rate']),
 dict(id='liquidity-risk', title='流动性风险', cat='银行',
  ol='在某段时间内，某金融资产无法足够快速交易而不影响市场价格的风险。',
  ov='流动性风险是一种金融风险：在特定时间段内，某金融资产、证券或商品无法在市场上足够快速地交易，而不影响其市场价格。它与市场风险、信用风险并列为主要金融风险类别，在压力时期尤为突出。具体度量待核实。',
  causal=[('市场深度不足或交易中断 → 难以快速成交','w-en-liquidity-risk'),
          ('为快速出售须接受折价 → 造成损失','w-en-liquidity'),
          ('集中抛售 → 流动性螺旋与价格暴跌','w-en-credit-crunch')],
  schools=[('市场流动性视角','流动性风险源于市场深度不足','w-en-liquidity-risk'),
           ('融资流动性视角','机构无法续滚负债亦构成流动性风险','w-en-maturity-transformation')],
  srcs=['w-en-liquidity-risk','w-en-liquidity']),
 dict(id='market-risk', title='市场风险', cat='制度',
  ol='持仓因价格、波动率等市场变量变动而产生损失的风险。',
  ov='市场风险是持仓因价格与波动率等市场变量的变动而产生损失的风险。市场风险没有唯一分类方式，各类分类可能指向不同侧面。它是最基本的金融风险类别之一，常以 VaR 等指标度量。具体方法待核实。',
  causal=[('市场价格或波动率变动 → 持仓价值变化','w-en-market-risk'),
          ('杠杆放大损失幅度','w-en-leverage'),
          ('集中或相关性上升 → 组合损失超预期','w-en-systemic-risk')],
  schools=[('VaR 视角','以统计分布估计潜在损失','w-en-value-at-risk'),
           ('压力测试视角','以极端情景评估尾部风险','w-en-stress-test')],
  srcs=['w-en-market-risk','w-en-value-at-risk']),
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
        'comparison': '金融技术/风险概念，与相关理论及案例互补；具体适用待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作AH】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r53_concepts.json', encoding='utf-8'))
rename = {'sovereign-risk': 'sovereign-risk', 'country-risk': 'country-risk', 'basis-point': 'basis-point',
          'duration-finance': 'duration-finance', 'convexity': 'convexity', 'money-creation': 'money-creation',
          'endogenous-money': 'endogenous-money', 'loanable-funds': 'loanable-funds',
          'liquidity-risk': 'liquidity-risk', 'market-risk': 'market-risk'}
for eid, v in meta.items():
    if eid not in rename:
        continue
    sid = 'w-en-' + rename[eid]
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
