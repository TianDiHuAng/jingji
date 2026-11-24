# -*- coding: utf-8 -*-
"""续作AV：新增12条风险/市场微观结构概念(L2)。"""
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
 dict(id='volatility', title='波动率', cat='制度',
  ol='交易价格序列随时间的变动程度，通常以对数收益率的标准差衡量。',
  ov='在金融中，波动率是交易价格序列随时间的变动程度，通常以对数收益率的标准差来衡量。波动率是期权定价、风险度量（VaR）与资产配置的核心参数；波动率的突然上升常与市场压力相伴。具体度量方法待核实。',
  causal=[('价格序列的离散程度 → 形成波动率','w-en-volatility'),
          ('波动率上升 → 风险溢价与对冲成本上升','w-en-volatility'),
          ('极端波动 → 保证金追缴与去杠杆','w-en-margin-finance')],
  schools=[('统计视角','以收益率标准差刻画风险','w-en-volatility'),
           ('风险度量视角','波动率是VaR与压力测试的输入','w-en-value-at-risk')],
  srcs=['w-en-volatility','w-en-value-at-risk']),
 dict(id='diversification', title='分散化', cat='制度',
  ol='通过配置资本以降低对任一特定资产或风险敞口的方式。',
  ov='在金融中，分散化是以降低对任一特定资产或风险敞口的方式配置资本的过程。通往分散化的常见路径是持有一篮子资产。分散化可降低非系统性风险，但无法消除系统性风险——危机中相关性上升会削弱其效果。具体机制待核实。',
  causal=[('配置于多类资产 → 单一风险敞口下降','w-en-diversification'),
          ('非系统性风险被抵消 → 组合波动下降','w-en-diversification'),
          ('危机中相关性趋同 → 分散效果削弱','w-en-systemic-risk')],
  schools=[('组合理论视角','分散化可降低非系统性风险','w-en-diversification'),
           ('系统性视角','危机中相关性上升、分散失效','w-en-systemic-risk')],
  srcs=['w-en-diversification','w-en-systemic-risk']),
 dict(id='risk-management', title='风险管理', cat='制度',
  ol='对风险进行识别、评估与排序，并最小化、监测和控制其影响或概率的过程。',
  ov='风险管理是对风险进行识别、评估与排序，随后最小化、监测并控制这些风险的影响或概率（的过程）。在金融中，它涵盖信用、市场、流动性与操作风险的度量与治理。其有效性依赖模型假设与激励设计。具体方法待核实。',
  causal=[('识别与评估风险 → 形成风险画像','w-en-risk-management'),
          ('以限额、对冲与资本缓冲控制风险','w-en-risk-management'),
          ('模型或激励失灵 → 风险在危机中集中暴露','w-en-value-at-risk')],
  schools=[('量化视角','以VaR/压力测试度量与管理风险','w-en-risk-management'),
           ('治理视角','激励、文化与问责决定有效性','w-en-principal-agent')],
  srcs=['w-en-risk-management','w-en-value-at-risk']),
 dict(id='alm', title='资产负债管理(ALM)', cat='制度',
  ol='银行或企业通过匹配资产与负债来最小化市场风险与流动性风险的工具与技术。',
  ov='资产负债管理（ALM）是涵盖银行或其他企业所用工具与技术的术语，通过（匹配资产与负债）来最小化市场和流动性风险敞口。ALM 关注利率敏感性、期限结构与流动性缓冲，是银行稳健经营的核心职能。具体方法待核实。',
  causal=[('资产与负债的期限/利率特征不匹配 → 产生风险敞口','w-en-alm'),
          ('以久期匹配、衍生品对冲等工具管理','w-en-duration-finance'),
          ('管理失效 → 利率或流动性冲击放大损失','w-en-silicon-valley-bank')],
  schools=[('匹配视角','以久期与现金流匹配降低风险','w-en-alm'),
           ('收益视角','主动错配可提升利差但增加风险','w-en-maturity-transformation')],
  srcs=['w-en-alm','w-en-duration-finance']),
 dict(id='prudential-regulation', title='金融监管', cat='制度',
  ol='适用于金融部门的广泛政策集合，其正当性主要来自系统性风险与信息不对称等特征。',
  ov='金融监管是适用于多数辖区金融部门的广泛政策集合。其正当性主要来自金融的两个特征：系统性风险（个体失败可波及整个体系）等。监管涵盖准入、资本、流动性、行为与消费者保护等维度。具体框架待核实。',
  causal=[('金融体系存在系统性风险与信息不对称 → 需要公共监管','w-en-prudential-regulation'),
          ('以资本、流动性与行为规则约束机构','w-en-capital-requirement'),
          ('降低危机概率与消费者受损','w-en-systemic-risk')],
  schools=[('公共利益视角','监管纠正市场失灵与系统性风险','w-en-prudential-regulation'),
           ('成本视角','监管负担可能抑制效率与创新','w-en-financial-innovation')],
  srcs=['w-en-prudential-regulation','w-en-capital-requirement']),
 dict(id='fx-intervention', title='外汇干预', cat='货币',
  ol='政府或中央银行为影响本币汇率而在外汇市场进行的操作。',
  ov='外汇干预（亦称外汇市场干预）是一种货币政策操作：政府或中央银行（在外汇市场买卖本币/外币）以影响汇率。干预可为冲销式或非冲销式，其效果取决于规模、持续性与市场预期。具体实践待核实。',
  causal=[('本币汇率偏离目标 → 当局决定干预','w-en-fx-intervention'),
          ('在外汇市场买卖本币 → 影响供求与汇率','w-en-fx-intervention'),
          ('非冲销干预改变货币供给（冲销则不然）','w-en-sterilization')],
  schools=[('干预有效视角','大规模持续干预可改变汇率路径','w-en-fx-intervention'),
           ('无效视角','与基本面不符的干预难以持久','w-en-currency-crisis')],
  srcs=['w-en-fx-intervention','w-en-sterilization']),
 dict(id='sterilization', title='冲销操作', cat='货币',
  ol='中央银行为抵消国际收支差额对货币供给影响而采取的操作。',
  ov='在宏观经济学中，冲销是中央银行采取的行动，用以抵消国际收支顺差或逆差对货币供应造成的影响。典型做法是在外汇市场买入外汇的同时，通过公开市场操作或准备金要求回笼本币，从而隔离货币供给。具体机制待核实。',
  causal=[('外汇流入导致本币投放增加 → 货币供给扩张','w-en-sterilization'),
          ('以公开市场操作/提高准备金回笼本币 → 抵消影响','w-en-open-market-operation'),
          ('冲销有成本（如央行票据利息），且难以无限持续','w-en-sterilization')],
  schools=[('货币控制视角','冲销可维持货币供给目标','w-en-sterilization'),
           ('成本视角','冲销成本与资本流入压力可能使其不可持续','w-en-capital-control')],
  srcs=['w-en-sterilization','w-en-open-market-operation']),
 dict(id='hedging', title='套期保值', cat='制度',
  ol='降低另一项投资或业务活动亏损风险的投资或合约；进行此类操作称为对冲。',
  ov='在金融中，套期保值（hedge）是一种投资或合约，用以降低在另一项投资或业务活动中亏损的风险；进行这种操作称为对冲（hedging）。它通常通过衍生品、反向头寸或自然对冲实现，可降低风险但也可能牺牲部分收益。具体工具待核实。',
  causal=[('持有风险敞口 → 面临价格不利变动风险','w-en-hedging'),
          ('建立反向头寸或买入衍生品 → 抵消风险','w-en-derivative'),
          ('对冲比率与基差风险决定效果','w-en-hedging')],
  schools=[('风险管理视角','对冲降低波动、提升可预测性','w-en-hedging'),
           ('成本视角','对冲有成本且可能引入基差与对手方风险','w-en-otc')],
  srcs=['w-en-hedging','w-en-derivative']),
 dict(id='speculation', title='投机', cat='理论',
  ol='购买资产以期其在短期内升值的行为；亦指卖空等操作。',
  ov='在金融中，投机是购买资产、期望该资产在短时间内变得更有价值的行为。该词也可指卖空等操作。投机提供流动性并推动价格发现，但过度投机可能催生泡沫；其与投资的界限在实践中并不清晰。具体论述待核实。',
  causal=[('预期价格短期上涨 → 买入资产','w-en-speculation'),
          ('买盘推高价格 → 吸引更多投机资金','w-en-speculative-bubble'),
          ('预期逆转 → 价格崩跌','w-en-speculative-bubble')],
  schools=[('功能视角','投机提供流动性与价格发现','w-en-speculation'),
           ('泡沫视角','过度投机使价格脱离基本面','w-en-speculative-bubble')],
  srcs=['w-en-speculation','w-en-speculative-bubble']),
 dict(id='arbitrage', title='套利', cat='制度',
  ol='利用两个或多个市场之间的价差、通过一组匹配交易获利的行为。',
  ov='套利是利用两个或多个市场之间的价格差异——通过进行一组匹配的交易来赚取该差价——的行为。套利活动通常推动价格趋于一致，从而提升市场效率；但在现实中套利受限于资本、风险与市场摩擦。具体机制待核实。',
  causal=[('同一资产在不同市场价格不同 → 出现套利机会','w-en-arbitrage'),
          ('同时买入低价、卖出高价 → 赚取价差','w-en-arbitrage'),
          ('套利推动价格趋同、价差收敛','w-en-efficient-market')],
  schools=[('有效市场视角','套利使价格趋于一致','w-en-arbitrage'),
           ('套利限制视角','资本与风险约束使偏离可持续','w-en-behavioral-finance')],
  srcs=['w-en-arbitrage','w-en-efficient-market']),
 dict(id='market-maker', title='做市商', cat='制度',
  ol='通过持续报出愿意买入与卖出资产的价格来提供流动性的机构或个人。',
  ov='做市商是通过持续报出愿意买入和卖出资产的价格来提供流动性的机构或个人。其目标是赚取买卖价差，同时管理库存风险。做市商是市场流动性的核心提供者，但在压力时期可能迅速撤出。具体机制待核实。',
  causal=[('持续双向报价 → 为市场提供即时流动性','w-en-market-maker'),
          ('赚取买卖价差、管理库存风险','w-en-bid-ask'),
          ('压力期撤出报价 → 流动性骤降','w-en-liquidity-risk')],
  schools=[('流动性视角','做市商降低交易成本、提升连续性','w-en-market-maker'),
           ('脆弱性视角','做市商撤离会放大价格波动','w-en-liquidity-risk')],
  srcs=['w-en-market-maker','w-en-bid-ask']),
 dict(id='bid-ask', title='买卖价差', cat='制度',
  ol='立即卖出（要价）与立即买入（出价）所报价格之间的差额。',
  ov='买卖价差是股票、期货、期权或货币等工具立即卖出所报价格（ask）与立即买入所报价格（bid）之间的差额。价差是流动性的直接度量：价差越小，流动性越好；压力时期价差显著扩大。具体机制待核实。',
  causal=[('做市商报出买价与卖价 → 形成价差','w-en-bid-ask'),
          ('价差反映流动性、库存与信息风险','w-en-bid-ask'),
          ('压力期价差扩大 → 交易成本上升、流动性恶化','w-en-liquidity-risk')],
  schools=[('微观结构视角','价差补偿做市商的订单处理与库存成本','w-en-bid-ask'),
           ('流动性视角','价差扩大是流动性紧张的先行信号','w-en-liquidity')],
  srcs=['w-en-bid-ask','w-en-liquidity']),
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
        'comparison': '风险/市场微观结构概念，与相关理论及案例互补；具体适用待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体细节待核实。【续作AV】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r67_concepts.json', encoding='utf-8'))
used = {'volatility','diversification','risk-management','alm','prudential-regulation','fx-intervention',
        'sterilization','hedging','speculation','arbitrage','market-maker','bid-ask'}
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
        'source_count': len(sp['srcs']), 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
