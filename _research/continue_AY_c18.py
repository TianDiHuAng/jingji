# -*- coding: utf-8 -*-
"""续作AY：新增2条18世纪恶性通胀案例（填补矩阵"18—19世纪×恶性通胀"空白）。"""
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
 dict(id='assignat-1790s', title='法国指券通胀(1789–1796)', cat='恶性通胀',
  unit='U2 18—19世纪', period='18—19世纪', region='欧洲', tier='重要',
  ol='法国大革命时期以没收教产为担保发行的指券（assignat），因持续超发导致严重通胀与货币贬值。',
  ov='指券（assignat）是法国大革命与法国革命战争期间使用的一种货币工具、一种支付命令。1789年12月21日通过首个法令，命令于1790年4月发行价值40万里弗的指券（作为债务凭证，附息）；1790年4月17日指券被宣布为法定清偿手段，但利率被降至3%。1790年8月27日制宪议会决定再发行19亿指券。指券一经流通即贬值5%。其后持续超发导致恶性通胀，最终于1796年被废止。具体过程待核实。',
  tl=[
    {'year':1789,'display':'1789年12月21日','event':'首个法令通过，命令1790年4月发行40万里弗指券（据 Wikipedia Assignat）','sources':['w-en-assignat']},
    {'year':1790,'display':'1790年4月17日','event':'指券被宣布为法定清偿，利率降至3%（同上）','sources':['w-en-assignat']},
    {'year':1790,'display':'1790年8月27日','event':'制宪议会决定再发行19亿指券（同上）','sources':['w-en-assignat']},
    {'year':1796,'display':'1796年','event':'指券体系废止（同上；具体日期待核实）','sources':['w-en-assignat']},
  ],
  causal=[('革命政府财政危机 + 没收教产作担保 → 以指券融资','w-en-assignat'),
          ('持续超发（1789年40万里弗 → 1790年再发19亿）→ 货币贬值、物价飞涨','w-en-assignat'),
          ('指券丧失货币职能 → 恶性通胀与体系废止','w-en-hyperinflation')],
  schools=[('财政/货币视角','以纸钞弥补财政缺口导致超发与通胀','w-en-assignat'),
           ('担保资产视角','以土地为担保并不自动约束发行量','w-en-fiat-money')],
  kd=[
    {'label':'首次指券发行额(1790年4月)','value':0.4,'unit':'百万里弗（40万）','year':1790,'comparable_price':False,
     'note':'原文：ordering the issue (in April 1790) of 400,000 livres\' worth of assignats；单一来源待核实。','sources':['w-en-assignat']},
    {'label':'第二次指券发行额(1790年8月27日)','value':1900,'unit':'百万里弗（19亿）','year':1790,'comparable_price':False,
     'note':'原文：another issue of 1,9 billion assignats；单一来源待核实。','sources':['w-en-assignat']},
    {'label':'指券初始贬值幅度','value':-5,'unit':'%（一经流通即贬值）','year':1790,'comparable_price':False,
     'note':'原文：As soon as the assignats started to circulate, their value decreased by 5 percent；单一来源待核实。','sources':['w-en-assignat']},
  ],
  cmp='与魏玛(1921–23)、匈牙利(1945–46)恶性通胀同属财政赤字货币化型；但指券以土地为名义担保，属早期纸币试验。具体异同待核实。'),
 dict(id='continental-currency-1775', title='大陆币通胀(1775–1780s)', cat='恶性通胀',
  unit='U2 18—19世纪', period='18—19世纪', region='北美', tier='重要',
  ol='美国独立战争期间大陆会议发行的大陆币，因超发而大幅贬值（"不值一个大陆币"）。',
  ov='大陆币（Continental currency）以美元计价，面额从1/6美元到80美元不等，其间还有许多奇特面额。独立战争期间，大陆会议共发行了199,990,000美元的大陆币。由于缺乏税收支撑而大量发行，大陆币急剧贬值，成为"not worth a Continental"（不值一个大陆币）这一说法的来源。1790年代美国宪法批准后，大陆币可按面值的1%兑换国债。具体过程待核实。',
  tl=[
    {'year':1775,'display':'1775年起','event':'大陆会议开始发行大陆币（据 Wikipedia Early American currency）','sources':['w-en-early-american-currency']},
    {'year':1779,'display':'独立战争期间','event':'累计发行199,990,000美元大陆币（同上）','sources':['w-en-early-american-currency']},
    {'year':1790,'display':'1790年代','event':'宪法批准后，大陆币可按面值1%兑换国债（同上）','sources':['w-en-early-american-currency']},
  ],
  causal=[('独立战争军费激增 + 无征税权 → 以发行纸钞融资','w-en-early-american-currency'),
          ('累计发行约2亿美元、缺乏回笼机制 → 币值崩溃','w-en-early-american-currency'),
          ('战后按面值1%兑换国债 → 持有者损失绝大部分','w-en-fiat-money')],
  schools=[('财政视角','无税收支撑的发行必然导致贬值','w-en-early-american-currency'),
           ('货币视角','缺乏约束的法定货币难以维持购买力','w-en-fiat-money')],
  kd=[
    {'label':'大陆币累计发行额','value':199.99,'unit':'百万美元（$199,990,000）','year':1779,'comparable_price':False,
     'note':'原文：During the Revolution, Congress issued $199,990,000 in Continental currency；单一来源待核实。','sources':['w-en-early-american-currency']},
    {'label':'战后兑换率','value':1,'unit':'%（按面值兑换国债）','year':1790,'comparable_price':False,
     'note':'原文：Continentals could be exchanged for treasury bonds at 1% of face value；单一来源待核实。','sources':['w-en-early-american-currency']},
  ],
  cmp='与法国指券同期（18世纪末），同为战争财政驱动的纸币通胀；美国案例以战后极低兑换率收场。具体异同待核实。'),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': sp['kd'],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [{'holder': '政策当局', 'view': '应对措施见时间线；效果待核实', 'basis': '需多来源印证',
                             'sources': [sp['causal'][0][1]]}],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st, s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：时间线与机制据维基全文；具体数值单源待核实。【续作AY】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r70_data.json', encoding='utf-8'))
for eid, sid, key in [('assignat-1790s','w-en-assignat','assignat-1790s'),
                      ('continental-currency-1775','w-en-early-american-currency','continental-currency-1775')]:
    if sid in ex:
        continue
    v = meta.get(key)
    if not v:
        continue
    sd['sources'].append({
        'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科',
        'url': 'https://en.wikipedia.org/wiki/' + v['title'].replace(' ', '_'),
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'Wikipedia API(full extract)核对(本会话抓取全文)'
    })
    ex.add(sid)
    print('新增来源', sid, '|', v['title'])
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
        'source_count': 2, 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
