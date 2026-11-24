# -*- coding: utf-8 -*-
"""续作AZ：新增8条宏观/衍生品概念(L2)。"""
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
 dict(id='nairu', title='非加速通胀失业率(NAIRU)', cat='理论',
  ol='理论上若低于该失业水平、通胀预期将上升的失业率。',
  ov='非加速通胀失业率（NAIRU）是一种理论上的失业水平：低于该水平，通胀预计将上升。它最初由（研究者）以 NIRU 之名提出。NAIRU 是货币政策与通胀目标的重要参考，但其估计不确定性与政策含义存在争议。具体论述待核实。',
  causal=[('失业低于 NAIRU → 工资与价格上行压力','w-en-nairu'),
          ('通胀加速 → 央行需收紧政策','w-en-nairu'),
          ('（争议）NAIRU 水平不可直接观测、估计不稳','w-en-natural-rate-unemployment')],
  schools=[('货币主义视角','长期失业趋向 NAIRU，扩张只带来通胀','w-en-nairu'),
           ('后凯恩斯视角','NAIRU 非自然常数、受政策与制度影响','w-en-post-keynesian')],
  srcs=['w-en-nairu','w-en-natural-rate-unemployment']),
 dict(id='disinflation', title='反通胀（通胀放缓）', cat='理论',
  ol='通胀率的下降，即商品与服务总体价格水平上升速度的放缓。',
  ov='反通胀（disinflation）是通胀率的下降——即一国国内生产总值中商品与服务总体价格水平相对上升速度的放缓。它与通缩（价格水平下降）不同。反通胀常伴随产出与就业的短期代价，其"牺牲率"是政策讨论焦点。具体论述待核实。',
  causal=[('紧缩政策或供给改善 → 通胀率下降','w-en-disinflation'),
          ('预期调整滞后 → 产出与就业短期受损','w-en-phillips-curve'),
          ('可信度高的政策可降低牺牲率','w-en-inflation-targeting')],
  schools=[('货币主义视角','以可控的短期产出代价换取通胀下降','w-en-disinflation'),
           ('通缩视角','需区分通胀放缓与价格下跌','w-en-deflation')],
  srcs=['w-en-disinflation','w-en-phillips-curve']),
 dict(id='potential-output', title='潜在产出', cat='理论',
  ol='长期可持续实现的最高实际GDP水平。',
  ov='在经济学中，潜在产出指长期可持续的最高实际国内生产总值水平。实际产出发生在现实中，而潜在产出（为估计值）。潜在产出是计算产出缺口与判断经济过热/闲置的基础，但因不可观测而争议较大。具体测算待核实。',
  causal=[('要素供给与技术决定潜在产出 → 形成长期上限','w-en-potential-output'),
          ('实际产出偏离潜在产出 → 形成产出缺口','w-en-output-gap'),
          ('政策据缺口判断松紧（估算误差影响决策）','w-en-monetary-policy')],
  schools=[('生产函数视角','以资本劳动与技术估算潜在产出','w-en-potential-output'),
           ('批判视角','潜在产出不可观测、估算偏差影响政策','w-en-output-gap')],
  srcs=['w-en-potential-output','w-en-output-gap']),
 dict(id='forward-contract', title='远期合约', cat='制度',
  ol='双方之间非标准化的、在未来特定时间以约定价格买卖某资产的合约。',
  ov='在金融中，远期合约（forward）是双方之间的一种非标准化合约：在未来特定时间、以合约中约定的价格买入或卖出某项资产。与期货不同，远期合约非标准化、通常在场外交易，因而存在对手方风险。具体机制待核实。',
  causal=[('双方约定未来价格与交割 → 签订非标合约','w-en-forward-contract'),
          ('锁定价格以对冲或投机','w-en-hedging'),
          ('场外交易 → 承担对手方信用风险','w-en-otc')],
  schools=[('对冲视角','远期可锁定未来价格、消除不确定性','w-en-forward-contract'),
           ('对手方风险视角','非标准化与非集中清算带来信用风险','w-en-otc')],
  srcs=['w-en-forward-contract','w-en-otc']),
 dict(id='call-option', title='看涨期权', cat='制度',
  ol='赋予买方在约定时间以约定价格买入一定数量标的资产权利的期权合约（非义务）。',
  ov='在金融中，看涨期权是一种期权合约，赋予其买方在约定时间以约定价格买入约定数量的特定商品、证券或其他金融工具的权利，而非义务。看涨期权是期权的基本类型之一，其价值随标的价格上升而增加。具体定价待核实。',
  causal=[('买方支付权利金 → 获得买入权利','w-en-call-option'),
          ('标的价格上涨 → 期权价值上升','w-en-call-option'),
          ('用于对冲上行风险或杠杆化投机','w-en-black-scholes')],
  schools=[('对冲视角','看涨期权可锁定买入成本上限','w-en-call-option'),
           ('杠杆视角','以小博大放大收益与损失','w-en-option')],
  srcs=['w-en-call-option','w-en-option']),
 dict(id='put-option', title='看跌期权', cat='制度',
  ol='赋予持有人按约定价格、在约定日期前卖出标的资产给期权卖方的权利的衍生工具。',
  ov='看跌期权（put）是金融市场中的一种衍生工具，赋予其持有人按约定价格、在约定日期之前向期权卖方卖出某项资产的权利。看跌期权可用于对冲下跌风险，其价值随标的价格下跌而增加。具体定价待核实。',
  causal=[('买方支付权利金 → 获得卖出权利','w-en-put-option'),
          ('标的价格下跌 → 期权价值上升','w-en-put-option'),
          ('用于对冲下行风险（如投资组合保险）','w-en-black-monday-1987')],
  schools=[('保险视角','看跌期权类似价格下跌保险','w-en-put-option'),
           ('系统视角','组合保险式对冲在崩盘中可能放大抛售','w-en-black-monday-1987')],
  srcs=['w-en-put-option','w-en-option']),
 dict(id='spot-contract', title='即期合约', cat='制度',
  ol='为在即期日（通常为交易后很短时间）立即交割而买卖商品、证券或货币的合约。',
  ov='在金融中，即期合约（spot contract，即期交易）是为在即期日（通常为交易后很短时间内）立即结算而买卖商品、证券或货币的合约。即期交易与远期、期货等未来交割的合约相对，是现货市场的基础。具体规则待核实。',
  causal=[('买卖双方按当前市价成交 → 短期交割结算','w-en-spot-contract'),
          ('形成现货价格（即期汇率/价格）','w-en-spot-contract'),
          ('与远期价格之差构成掉期点等','w-en-interest-rate-parity')],
  schools=[('现货视角','即期价格反映当前供求','w-en-spot-contract'),
           ('跨期视角','即期与远期价差反映利率与预期','w-en-interest-rate-parity')],
  srcs=['w-en-spot-contract','w-en-interest-rate-parity']),
 dict(id='interest-rate-swap', title='利率互换', cat='制度',
  ol='两方之间交换利息率的利率衍生品，属"线性"IRD，是最常见的互换类型。',
  ov='在金融中，利率互换（IRS）是一种利率衍生品（IRD），涉及两方之间交换利率。具体而言，它是一种"线性"利率衍生品，也是最常见的（互换类型）之一（通常一方付固定利率、另一方付浮动利率）。利率互换用于管理利率风险与调整资产负债敏感性。具体机制待核实。',
  causal=[('一方付固定、一方付浮动的利率 → 签订互换','w-en-interest-rate-swap'),
          ('用于调整资产负债的利率敏感性','w-en-alm'),
          ('场外交易 → 对手方与不透明风险','w-en-otc')],
  schools=[('风险管理视角','利率互换精细调整利率敞口','w-en-interest-rate-swap'),
           ('系统性视角','大规模场外互换在压力下放大传染','w-en-systemic-risk')],
  srcs=['w-en-interest-rate-swap','w-en-swap']),
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
        'comparison': '宏观/衍生品概念，与相关理论及案例互补；具体适用待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体细节待核实。【续作AZ】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r71_concepts.json', encoding='utf-8'))
used = {'nairu','disinflation','potential-output','forward-contract','call-option','put-option','spot-contract','interest-rate-swap'}
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
