# -*- coding: utf-8 -*-
"""续作BA：新增5条1930年代货币制度案例（填补矩阵「20世纪上半×货币」空白）。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

D = [
 dict(id='tripartite-1936', title='三方货币协定(1936)', cat='货币',
  unit='U3 20世纪上半', period='20世纪上半', region='全球', tier='重要',
  ol='1936年9月美、法、英三国达成的国际货币协定，旨在稳定各国货币的国内与国际汇市。',
  ov='三方货币协定是美国、法国与英国于1936年9月达成的国际货币协定。该协定的目的是在大萧条与金本位瓦解之后，稳定这三个国家的货币在国内与国际外汇市场上的（价值）。它标志着主要国家从竞争性贬值转向有限度的货币合作。具体条款待核实。',
  tl=[
    {'year':1936,'display':'1936年9月','event':'美、法、英签署三方货币协定，旨在稳定货币（据 Wikipedia Tripartite Agreement of 1936）','sources':['w-en-tripartite-1936']},
  ],
  causal=[('金本位瓦解后各国竞争性贬值 → 汇率动荡','w-en-gold-bloc'),
          ('1936年9月三方协定 → 承诺相互协商、避免竞相贬值','w-en-tripartite-1936'),
          ('有限合作缓解汇率摩擦（但未恢复固定平价）','w-en-competitive-devaluation')],
  schools=[('合作视角','协定标志从以邻为壑转向有限协调','w-en-tripartite-1936'),
           ('局限视角','无约束力的协商难以稳定预期','w-en-international-monetary-system')],
  cmp='与1944年布雷顿森林体系相比，1936年协定只是无约束力的协商机制；但它是战时货币合作的先声。具体异同待核实。'),
 dict(id='gold-bloc', title='金集团(1930s)', cat='货币',
  unit='U3 20世纪上半', period='20世纪上半', region='欧洲', tier='重要',
  ol='大萧条期间以法国为首、坚持金本位的七个国家（法、比、卢、荷、意、波、瑞士）。',
  ov='金集团是在大萧条期间坚持金本位货币政策、而其他许多国家已放弃金本位的七个国家，以法国为首。除法国外，金集团还包括比利时、卢森堡、荷兰、意大利、波兰与瑞士。坚持金本位使这些国家丧失货币政策空间、承受通缩与竞争力损失，最终相继放弃。具体过程待核实。',
  tl=[
    {'year':1931,'display':'1930年代','event':'法、比、卢、荷、意、波、瑞士组成金集团，坚持金本位（据 Wikipedia Gold bloc）','sources':['w-en-gold-bloc']},
    {'year':1936,'display':'1936年前后','event':'金集团成员国相继放弃金本位（同上；具体时间待核实）','sources':['w-en-gold-bloc']}],
  causal=[('坚持金本位 → 货币供给受黄金约束、无法扩张','w-en-gold-standard'),
          ('通缩与竞争力下降 → 产出与就业恶化','w-en-gold-bloc'),
          ('最终被迫贬值/放弃金本位 → 集团瓦解','w-en-european-banking-1931')],
  schools=[('金本位约束视角','坚持金本位延长了通缩与萧条','w-en-gold-standard'),
           ('退出视角','及早退出金本位的国家复苏更快','w-en-great-depression')],
  cmp='与英国1931年退出金本位（较早复苏）形成对照；金集团案例常被引为"金本位束缚"的典型证据。具体异同待核实。'),
 dict(id='sterling-area', title='英镑区', cat='货币',
  unit='U3 20世纪上半', period='20世纪上半', region='全球', tier='补充',
  ol='采用英镑、或将本币钉住英镑的一组国家。',
  ov='英镑区是一组采用英镑、或将本币钉住英镑的国家。它以英镑作为储备与结算货币，是英国在帝国特惠与英联邦框架下维持货币影响力的安排。英镑区随英国经济地位变化与资本管制演进而消长。具体成员与时期待核实。',
  tl=[
    {'year':1931,'display':'1930年代起','event':'英镑区形成：一批国家采用或钉住英镑（据 Wikipedia Sterling area）','sources':['w-en-sterling-area']},
  ],
  causal=[('英国为重要贸易与金融伙伴 → 相关国家以英镑为储备与结算','w-en-sterling-area'),
          ('钉住英镑 → 汇率稳定但货币政策受英国影响','w-en-exchange-rate-regime'),
          ('英国地位下降与管制变化 → 英镑区逐步消解','w-en-gold-standard')],
  schools=[('货币集团视角','英镑区扩大英国货币影响力','w-en-sterling-area'),
           ('依附视角','成员国的货币政策自主性受限','w-en-impossible-trinity')],
  cmp='与法郎区、美元区等货币集团并列，反映1930年代世界货币的集团化。具体异同待核实。'),
 dict(id='exchange-equalisation', title='外汇平准账户(EEA)', cat='货币',
  unit='U3 20世纪上半', period='20世纪上半', region='欧洲', tier='补充',
  ol='英国财政部的基金，持有SDR、外汇与黄金储备，用于干预外汇市场。',
  ov='外汇平准账户（EEA）是英国财政部的一项基金。它持有英国在国际货币基金组织的特别提款权（SDR），以及外币与黄金储备。该账户设立的目的是提供资金（用于干预外汇市场）。EEA 是英国在不直接改变货币政策的情况下影响汇率的制度工具。具体运作待核实。',
  tl=[
    {'year':1932,'display':'1930年代起','event':'英国设立外汇平准账户用于外汇市场干预（据 Wikipedia Exchange Equalisation Account；设立年份待核实）','sources':['w-en-exchange-equalisation']},
  ],
  causal=[('英国退出金本位后需管理汇率 → 设立平准账户','w-en-exchange-equalisation'),
          ('以基金买卖外汇/黄金 → 影响汇率而不直接改变利率','w-en-fx-intervention'),
          ('储备资产（SDR、外币、黄金）集中于该账户','w-en-foreign-exchange-reserves')],
  schools=[('干预视角','平准账户使汇率管理可与货币政策分离','w-en-exchange-equalisation'),
           ('冲销视角','干预的货币影响需通过冲销隔离','w-en-sterilization')],
  cmp='与当代各国央行/财政部的汇率稳定基金同类；是"冲销式干预"制度化的重要先例。具体异同待核实。'),
 dict(id='gold-reserve-act-1934', title='美国黄金储备法(1934)', cat='货币',
  unit='U3 20世纪上半', period='20世纪上半', region='北美', tier='重要',
  ol='1934年1月30日美国法律，要求美联储持有的全部黄金与金券上缴财政部。',
  ov='美国《1934年1月30日黄金储备法》要求美联储持有的全部黄金与金券上交，并归属美国财政部所有。该法同时禁止财政部与金融机构（从事某些黄金交易）。它是罗斯福政府在大萧条中重塑货币体系的关键立法，实质上将黄金集中于国家。具体条款待核实。',
  tl=[
    {'year':1934,'display':'1934年1月30日','event':'美国《黄金储备法》生效，要求黄金与金券上缴财政部（据 Wikipedia Gold Reserve Act）','sources':['w-en-gold-reserve-act-1934']},
  ],
  causal=[('大萧条中金本位约束货币政策 → 需集中黄金以扩大货币弹性','w-en-gold-standard'),
          ('1934年黄金储备法 → 黄金国有化、禁止私人持有','w-en-gold-reserve-act-1934'),
          ('为货币扩张与美元贬值创造条件 → 支持复苏','w-en-great-depression')],
  schools=[('货币自主视角','集中黄金使货币政策摆脱金本位束缚','w-en-gold-reserve-act-1934'),
           ('财产权视角','强制上缴黄金引发产权与法治争议','w-en-fiat-money')],
  cmp='与英国1931年退出金本位、金集团坚持金本位形成三条对照路径：退出、国有化、坚持。具体异同待核实。'),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [{'holder': '政策当局', 'view': '应对措施见时间线；效果待核实', 'basis': '需多来源印证',
                             'sources': [sp['causal'][0][1]]}],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st, s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：时间线与机制据维基摘要；具体日期与数据待核实。【续作BA】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r72_cases.json', encoding='utf-8'))
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
for sp in D:
    if sp['id'] in have:
        continue
    cov['entries'].append({
        'id': sp['id'], 'level': 'L2', 'tier': sp['tier'], 'status': 'written',
        'source_count': len(sp['causal']), 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
