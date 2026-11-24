# -*- coding: utf-8 -*-
"""续作BO：新增新西兰金融公司倒闭潮(大洋洲21世纪)与结构调整计划概念。"""
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
 dict(id='nz-finance-collapse', title='新西兰金融公司倒闭潮(2006–2012)', cat='银行',
  unit='U5 21世纪', period='21世纪', region='大洋洲', tier='重要', level='L2',
  ol='2006年5月至2012年底新西兰共67家金融公司倒闭，议会调查估计损失超30亿美元、影响15—20万存款人。',
  ov='2006年5月至2012年底，新西兰共发生67起金融公司倒闭，包括进入清算、接管或延期偿付的公司。新西兰议会的一项调查估计损失超过30亿美元，影响了15万至20万名存款人。据储备银行，在2008年金融危机前的金融扩张高峰，非银行贷款机构资产约250亿美元，占（贷款市场的）8%；到2013年末，金融部门规模缩减至此前的一半，仅占机构贷款的3%。这是发达国家中较少被讨论的非银行金融（影子银行）挤兑案例。具体细节待核实。',
  tl=[
    {'year':2006,'display':'2006年5月起','event':'新西兰金融公司倒闭潮开始，至2012年底共67家（据 Wikipedia）','sources':['w-en-nz-finance-collapse']},
    {'year':2008,'display':'2008年前后','event':'非银行贷款机构资产约250亿美元，占市场8%（储备银行口径）','sources':['w-en-nz-finance-collapse']},
    {'year':2013,'display':'2013年末','event':'金融部门规模减半，仅占机构贷款3%','sources':['w-en-nz-finance-collapse']},
  ],
  causal=[('非银行金融公司高速扩张（2008年前资产约250亿美元、占8%）','w-en-nz-finance-collapse'),
          ('2006年起陆续倒闭 → 67家、损失超30亿美元','w-en-nz-finance-collapse'),
          ('存款人信心受损 + 监管收紧 → 部门规模减半（2013年占3%）','w-en-nz-finance-collapse')],
  schools=[('影子银行视角','非银机构缺乏审慎监管与存款保险，风险更易累积','w-en-shadow-banking'),
           ('监管覆盖视角','危机后监管扩展至非银部门，规模随之收缩','w-en-prudential-regulation')],
  kd=[
    {'label':'倒闭金融公司数量(2006-05—2012末)','value':67,'unit':'家','year':2012,'comparable_price':False,
     'note':'原文：Between May 2006 and the end of 2012 there were 67 finance company collapses in New Zealand；单一来源待核实。','sources':['w-en-nz-finance-collapse']},
    {'label':'议会估计损失','value':3,'unit':'十亿美元（超过30亿）','year':2012,'comparable_price':False,
     'note':'原文：An inquiry by the New Zealand Parliament estimated losses at over $3 billion；单一来源待核实。','sources':['w-en-nz-finance-collapse']},
    {'label':'受影响存款人数','value':200000,'unit':'人（15万—20万区间上限）','year':2012,'comparable_price':False,
     'note':'原文：affected between 150,000 and 200,000 depositors；单一来源待核实。','sources':['w-en-nz-finance-collapse']},
    {'label':'非银行贷款机构资产(危机前高峰)','value':25,'unit':'十亿美元（约250亿，占8%）','year':2008,'comparable_price':False,
     'note':'原文：non-bank lenders had assets of about $25 billion and made up 8% of [...]；单一来源待核实。','sources':['w-en-nz-finance-collapse']},
    {'label':'金融部门占机构贷款比重(2013末)','value':3,'unit':'%（规模减半）','year':2013,'comparable_price':False,
     'note':'原文：the size of the finance sector was half its previous size and accounted for only 3 percent of institutional lending；单一来源待核实。','sources':['w-en-nz-finance-collapse']},
  ],
  cmp='与2007年英国北岩银行挤兑（受存款保险保护的正规银行）不同，新西兰案例集中在**不受审慎监管的非银行金融公司**，存款人保护更弱。具体异同待核实。'),
 dict(id='structural-adjustment', title='结构调整计划(SAP)', cat='制度',
  unit='U6 理论与制度', period='理论制度', region='全球', tier='重要', level='L2',
  ol='IMF与世界银行向遭遇经济危机的国家提供的结构调整贷款，以调整其经济结构为条件。',
  ov='结构调整计划（SAP）由国际货币基金组织（IMF）和世界银行（WB）向遭遇经济危机的国家提供的贷款（结构调整贷款，SAL）构成。其公开目的是调整该国的经济结构（以恢复增长与国际收支平衡），通常附带财政紧缩、私有化与贸易自由化等条件。批评者指出，1980—1992年间因价格下跌，发展中国家损失了52%的出口收入，且伴随社会代价。具体争论待核实。',
  tl=[],
  causal=[('发展中国家陷入债务与国际收支危机 → 求助于 IMF/世行','w-en-debt-crisis'),
          ('以结构调整贷款为条件 → 推动紧缩、私有化与自由化','w-en-structural-adjustment'),
          ('1980–1992 初级产品价格下跌 → 发展中国家损失52%出口收入','w-en-structural-adjustment')],
  schools=[('调整视角','结构调整恢复宏观平衡与增长潜力','w-en-structural-adjustment'),
           ('批判视角','条件性加重社会代价、且外部价格冲击抵消调整效果','w-en-washington-consensus')],
  kd=[
    {'label':'发展中国家出口收入损失(1980–1992)','value':-52,'unit':'%（因价格下跌）','year':1992,'comparable_price':False,
     'note':'原文：developing countries lost 52% of their revenues from exports between 1980 and 1992 because of the decline in prices；单一来源待核实。','sources':['w-en-structural-adjustment']},
  ],
  cmp='与"华盛顿共识"高度重叠；拉美债务危机后与亚洲1997年后均有大规模应用。具体异同待核实。'),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': sp['level'], 'tier': sp['tier'],
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
        'pending_notes': 'L2：结构与数据据维基全文，单源待核实。【续作BO】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r81_data.json', encoding='utf-8'))
for eid, sid, key in [('nz-finance-collapse','w-en-nz-finance-collapse','nz-finance-collapse'),
                      ('structural-adjustment','w-en-structural-adjustment','structural-adjustment')]:
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
        'id': sp['id'], 'level': sp['level'], 'tier': sp['tier'], 'status': 'written',
        'source_count': 1, 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
