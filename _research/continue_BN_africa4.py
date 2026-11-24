# -*- coding: utf-8 -*-
"""续作BN：补强非洲(3条)与大洋洲(1条)覆盖。"""
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
 dict(id='nz-1984-reform', title='新西兰 Rogernomics 改革(1984–)', cat='其他',
  unit='U4 20世纪下半', period='20世纪下半', region='大洋洲', tier='重要',
  ol='1984年起新西兰财政部长 Roger Douglas 推行的新自由主义经济改革（Rogernomics）。',
  ov='Rogernomics（"Roger"与"economics"的合成词，仿 Reaganomics 构词）是新西兰财政部长罗杰·道格拉斯（Roger Douglas）于1984年起推动的新自由主义经济改革。改革包括税制调整——实施减税并引入商品与服务税（GST，初始税率为10%）。这场改革被视为发达国家中最激进的市场化转向之一，其社会代价与成效长期存在争论。具体措施待核实。',
  tl=[
    {'year':1984,'display':'1984年起','event':'Roger Douglas 任财政部长，推行 Rogernomics 改革（据 Wikipedia Rogernomics）','sources':['w-en-rogernomics']},
  ],
  causal=[('高通胀、财政失衡与管制僵化 → 转向激进市场化改革','w-en-rogernomics'),
          ('放开管制、减税并引入 GST → 重塑税制与产业结构','w-en-rogernomics'),
          ('改革阵痛：失业上升与社会不平等加剧（争论）','w-en-rogernomics')],
  schools=[('市场化视角','结构性改革提升长期效率','w-en-rogernomics'),
           ('社会代价视角','激进改革带来失业与不平等上升','w-en-put-all-eggs-in-one-basket')],
  kd=[
    {'label':'商品与服务税(GST)初始税率','value':10,'unit':'%','year':1986,'comparable_price':False,
     'note':'原文：a Goods and Services Tax (initially set at 10%) was introduced（维基 Rogernomics）；单一来源待核实。','sources':['w-en-rogernomics']},
  ],
  cmp='与同期英国撒切尔、美国里根、智利芝加哥学派改革并列，属1980年代全球新自由主义转向的一部分。具体异同待核实。'),
 dict(id='nigeria-debt', title='尼日利亚债务与经济结构风险', cat='债务',
  unit='U5 21世纪', period='21世纪', region='非洲', tier='重要',
  ol='非洲最大经济体之一的尼日利亚，其财政高度依赖石油收入而石油占GDP比重有限，构成结构性脆弱。',
  ov='尼日利亚的债务与GDP之比在2021年据国际货币基金组织为36.63%。尽管石油收入贡献了国家收入的三分之二，石油对GDP的贡献却仅约9%；尼日利亚生产全球约2.7%的石油。这种"财政收入高度依赖石油、但石油在产出中占比不高"的结构，使财政对油价波动极为敏感。具体数据与年份待核实。',
  tl=[],
  causal=[('财政收入高度依赖石油（约2/3）→ 油价下跌直接冲击财政','w-en-nigeria-econ'),
          ('石油仅占GDP约9% → 收入结构与产出结构错配','w-en-nigeria-econ'),
          ('外部冲击（2014–16油价下跌）→ 汇率与财政压力','w-en-oil-price-war-2020')],
  schools=[('资源依赖视角','单一资源依赖放大外部冲击','w-en-nigeria-econ'),
           ('结构转型视角','需多元化以降低波动','w-en-resource-curse')],
  kd=[
    {'label':'尼日利亚债务/GDP(2021，IMF口径)','value':36.63,'unit':'%','year':2021,'comparable_price':False,
     'note':'原文：Nigeria\'s debt-to-GDP ratio was 36.63% in 2021 according to the IMF（维基 Economy of Nigeria）；单一来源待核实。','sources':['w-en-nigeria-econ']},
    {'label':'石油占GDP比重（约）','value':9,'unit':'%（而石油贡献约2/3的政府收入）','year':2021,'comparable_price':False,
     'note':'原文：Although oil revenues contributed 2/3 of state revenues, oil only contributes about 9% to the GDP；单一来源待核实。','sources':['w-en-nigeria-econ']},
    {'label':'尼日利亚占全球石油供给（约）','value':2.7,'unit':'%','year':2021,'comparable_price':False,
     'note':'原文：Nigeria produces about 2.7% of the world\'s oil supply；单一来源待核实。','sources':['w-en-nigeria-econ']},
  ],
  cmp='与安哥拉、委内瑞拉等石油依赖型经济体结构相似：财政收入与产出结构错配放大油价冲击。具体异同待核实。'),
 dict(id='southafrica-debt', title='南非国家债务与外资依赖', cat='债务',
  unit='U5 21世纪', period='21世纪', region='非洲', tier='重要',
  ol='南非政府债务规模与结构变化：本币债占比高降低汇率风险，但外资持有比例波动带来融资脆弱性。',
  ov='截至2025/26年度，南非政府债务总额为6.09万亿兰特（4120.4亿美元），债务与GDP之比为77.4%。2019/20年度约90%的国债以南非兰特计价，从而降低了因汇率波动带来的借款风险；到2020年9月约有1570亿美元的南非国债由外部持有。截至2021年12月，外资持有国内债券的份额为28.2%，降至十年低点。具体数据待核实。',
  tl=[],
  causal=[('财政赤字累积 → 政府债务/GDP 升至 77.4%（2025/26）','w-en-southafrica-debt'),
          ('本币计价占比高（约90%）→ 降低汇率错配风险','w-en-southafrica-debt'),
          ('外资持有比率波动 → 融资成本与再融资风险变化','w-en-southafrica-debt')],
  schools=[('债务结构视角','本币债为主降低货币错配','w-en-southafrica-debt'),
           ('外资依赖视角','非居民持有比例变化影响融资稳定性','w-en-capital-flight')],
  kd=[
    {'label':'南非政府债务总额(2025/26)','value':6.09,'unit':'万亿兰特（US$412.04bn）','year':2025,'comparable_price':False,
     'note':'原文：the gross South African government debt was R6.09 trillion (US$412.04 billion)；单一来源待核实。','sources':['w-en-southafrica-debt']},
    {'label':'南非债务/GDP(2025/26)','value':77.4,'unit':'%','year':2025,'comparable_price':False,
     'note':'原文：with a debt-to-GDP ratio of 77.4%；单一来源待核实。','sources':['w-en-southafrica-debt']},
    {'label':'本币计价国债占比(2019/20,约)','value':90,'unit':'%','year':2020,'comparable_price':False,
     'note':'原文：Roughly 90% of the national debt in 2019/20 was denominated in South African rand；单一来源待核实。','sources':['w-en-southafrica-debt']},
    {'label':'外资持有国内债券份额(2021-12)','value':28.2,'unit':'%（十年低点）','year':2021,'comparable_price':False,
     'note':'原文：the share of domestic bonds held by foreign investors was 28.2%, this represented a declined to a 10-year low；单一来源待核实。','sources':['w-en-southafrica-debt']},
  ],
  cmp='与"原罪"型外债经济体（外币债为主）不同，南非以本币债为主、货币错配较轻；但外资持有波动仍构成脆弱点。具体异同待核实。'),
 dict(id='angola-oil-dependence', title='安哥拉石油依赖型经济波动', cat='其他',
  unit='U5 21世纪', period='21世纪', region='非洲', tier='补充',
  ol='安哥拉经济高度依赖石油出口，油价与产量变化直接决定贸易与财政表现。',
  ov='安哥拉在21世纪头十年曾是全球增长最快的经济体之一，2001—（2010）年报告的年均GDP增速达11.1%。但该国仍高度依赖石油部门——2017年石油占出口价值的90%以上。2022年贸易顺差为300亿美元，而2012年为480亿美元。经济多元化不足使安哥拉易受油价与产量波动冲击。具体数据待核实。',
  tl=[],
  causal=[('石油占出口90%以上（2017）→ 贸易与财政高度依赖油价','w-en-angola-econ'),
          ('2001—2010 年均GDP增速11.1% → 油价上行期高速增长','w-en-angola-econ'),
          ('2014年后油价下行 → 贸易顺差由480亿(2012)降至300亿(2022)','w-en-angola-econ')],
  schools=[('资源诅咒视角','资源依赖抑制多元化与制度质量','w-en-resource-curse'),
           ('增长视角','油价上行期可带来高速增长','w-en-angola-econ')],
  kd=[
    {'label':'安哥拉年均GDP增速(2001–2010，报告值)','value':11.1,'unit':'%','year':2010,'comparable_price':False,
     'note':'原文：with reported annual average GDP growth of 11.1 percent from 2001 to [2010]（维基 Economy of Angola）；年份区间截断处待核实。','sources':['w-en-angola-econ']},
    {'label':'石油占出口价值比重(2017)','value':90,'unit':'%（以上）','year':2017,'comparable_price':False,
     'note':'原文：which in 2017 accounted for over 90 percent of exports by value；单一来源待核实。','sources':['w-en-angola-econ']},
    {'label':'安哥拉贸易顺差(2012)','value':48,'unit':'十亿美元','year':2012,'comparable_price':False,
     'note':'原文：2022 trade surplus was $30 billion, compared to $48 billion in 2012；单一来源待核实。','sources':['w-en-angola-econ']},
    {'label':'安哥拉贸易顺差(2022)','value':30,'unit':'十亿美元','year':2022,'comparable_price':False,
     'note':'原文：2022 trade surplus was $30 billion；单一来源待核实。','sources':['w-en-angola-econ']},
  ],
  cmp='与尼日利亚结构类似（石油主导财政与出口），但安哥拉出口集中度更高。具体异同待核实。'),
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
        'policy_response': [{'holder': '政策当局', 'view': '应对措施与效果待核实', 'basis': '需多来源印证',
                             'sources': [sp['causal'][0][1]]}],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st, s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：结构与数据据维基（含国家经济页；非危机专题页），单源待核实。【续作BN】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r79_data.json', encoding='utf-8'))
MAP = {'nz-1984-reform': ('w-en-rogernomics', 'nz-1984-reform'),
       'nigeria-debt': ('w-en-nigeria-econ', 'nigeria-econ'),
       'southafrica-debt': ('w-en-southafrica-debt', 'southafrica-debt'),
       'angola-oil-dependence': ('w-en-angola-econ', 'angola-econ')}
for eid, (sid, key) in MAP.items():
    if sid in ex:
        continue
    v = meta.get(key, {})
    t = v.get('title')
    if not t:
        continue
    sd['sources'].append({
        'id': sid, 'title': t, 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科',
        'url': 'https://en.wikipedia.org/wiki/' + t.replace(' ', '_'),
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'Wikipedia API(full extract)核对(本会话抓取全文)'
    })
    ex.add(sid)
    print('新增来源', sid, '|', t)
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
        'source_count': 1, 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
