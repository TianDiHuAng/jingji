# -*- coding: utf-8 -*-
"""续作CS：新增纽约市1975财政危机与瑞典1990-94金融危机(U4)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20,270,520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

D = [
 dict(id='nyc-fiscal-1975', title='纽约市财政危机(1975)', cat='债务',
  region='北美', tier='重要',
  ol='纽约市累积140亿美元债务（含60亿短期债）后预算耗尽，被信贷市场拒之门外，靠州与联邦协调度过。',
  ov=('1975年纽约市爆发严重财政危机：该市累积了 **140亿美元** 债务，其中 **60亿美元** 是**短期债务**；'
   '预算耗尽，经营赤字超过 **6亿美元**，有估计将其推高至 **22亿美元**。'
   '由于信用评级恶化，该市实际上被**排除在信贷市场之外**——无法再滚动其短期债务。'
   '危机是1973—75年衰退的一部分，但根源更深：制造业岗位长期流失（20世纪后三分之一，'
   '该市失去数十万个工作岗位，包括约 **50%** 的制造业岗位与约 **60%** 的（相关行业岗位）），'
   '而市政就业持续扩张，'
   '"服务、政府与金融"类岗位占到全市（就业）的 **46%**——税基收缩与支出刚性同时恶化。'
   '削减福利的政治阻力极大：1971年布鲁克林布朗斯维尔居民在听闻拟削减福利 **10%** 后发生骚乱。'
   '危局最终通过州层面设立财政监督机构（Municipal Assistance Corporation / EFCB）与联邦贷款安排缓解；'
   '"Ford to City: Drop Dead"成为当时的著名标题（具体财政安排待核实）。'
   '该案例是**地方政府财政危机**（而非银行或货币危机）的经典样本。'),
  tl=[
   {'year':1971,'display':'1971年','event':'布朗斯维尔骚乱：反对削减福利10%的提议','sources':['w-en-nyc-fiscal-1975']},
   {'year':1975,'display':'1975年','event':'债务达140亿美元（含60亿短期债），赤字超6亿（估计达22亿），被拒于信贷市场之外','sources':['w-en-nyc-fiscal-1975']},
  ],
  causal=[('制造业岗位长期流失 + 市政就业扩张 → 税基收缩而支出刚性上升','w-en-nyc-fiscal-1975'),
         ('以短期债务滚动弥补赤字 → 债务累积至140亿（60亿为短期）','w-en-nyc-fiscal-1975'),
         ('信用评级恶化 → 被排除在信贷市场之外，需州与联邦协调救助','w-en-nyc-fiscal-1975')],
  schools=[{'holder':'结构视角','view':'产业空心化与支出刚性是根本原因','basis':'据就业与债务数据归纳','sources':['w-en-nyc-fiscal-1975']},
           {'holder':'周期视角','view':'1973—75衰退只是触发器，脆弱性早已累积','basis':'据危机时序归纳','sources':['w-en-nyc-fiscal-1975']}],
  kd=[
   {'label':'纽约市累积债务(1975)','value':14,'unit':'十亿美元（140亿）','year':1975,'comparable_price':False,
    'note':'原文：New York City had a severe fiscal crisis after accumulating $14 billion of debt；单一来源待核实。','sources':['w-en-nyc-fiscal-1975']},
   {'label':'其中短期债务','value':6,'unit':'十亿美元（60亿）','year':1975,'comparable_price':False,
    'note':'原文：of which $6 billion was short-term debt；单一来源待核实。','sources':['w-en-nyc-fiscal-1975']},
   {'label':'经营赤字(1975，估计下限)','value':600,'unit':'百万美元（超6亿）','year':1975,'comparable_price':False,
    'note':'原文：had an operating deficit of more than $600 million；单一来源待核实。','sources':['w-en-nyc-fiscal-1975']},
   {'label':'经营赤字(1975，部分估计)','value':2200,'unit':'百万美元（22亿）','year':1975,'comparable_price':False,
    'note':'原文：with some estimates placing the deficit at $2.2 billion；单一来源待核实。','sources':['w-en-nyc-fiscal-1975']},
  ],
  cmp=('与主权债务危机不同，纽约市没有货币与汇率工具，也不能像主权国家那样重组外债；'
   '与波多黎各2014年危机（见 puerto-rico-debt-2014）同属美国次级主权实体的财政困境，'
   '但纽约市最终避免了破产。具体异同待核实。')),
 dict(id='swedish-crisis-1990s', title='瑞典金融危机(1990–1994)', cat='银行',
  region='欧洲', tier='重要',
  ol='房价泡沫通缩引发严重信贷紧缩与银行危机，政府救助成本约为GDP的4%（后降至0—2%）。',
  ov=('1990—1994年瑞典金融危机源于**房价泡沫的通缩**，由此引发严重的**信贷紧缩、银行危机与深度衰退**。'
   '同期芬兰也发生了类似危机，美国则有储贷危机；'
   '有分析指出其成因与2007—2008年次贷危机**相似**（资产泡沫＋杠杆＋批发融资）。'
   '政策应对的关键是"救助+处置"并行：**Nordbanken 与 Götabanken 获得财政支持并被国有化，成本达 640亿克朗**；'
   '救助的初始成本约为瑞典GDP的 **4%**，'
   '后因（被国有化银行）股票此后售出而回收，净成本降至 **0%—2%** 之间（取决于假设）。'
   '瑞典案例常被引为"银行危机处置得当、财政净成本显著低于预期"的正面参照——'
   '关键在于**及时确认损失、国有化问题机构、并设立资产管理公司剥离不良资产**，'
   '而非拖延与"假装与宽容"(forbearance)。具体处置细节待核实。'),
  tl=[
   {'year':1990,'display':'1990—1994年','event':'房价泡沫通缩，信贷紧缩与银行危机','sources':['w-en-swedish-crisis-1990s']},
   {'year':1992,'display':'危机期间','event':'Nordbanken 与 Götabanken 获财政支持并被国有化（成本640亿克朗）','sources':['w-en-swedish-crisis-1990s']},
  ],
  causal=[('金融自由化后信贷扩张 → 房价与资产价格泡沫','w-en-finnish-banking-crisis'),
         ('泡沫通缩 → 抵押品价值下跌、信贷紧缩与银行损失','w-en-swedish-crisis-1990s'),
         ('政府注资并国有化问题银行（640亿克朗）→ 净财政成本约GDP的0—2%','w-en-swedish-crisis-1990s')],
  schools=[{'holder':'及时处置视角','view':'快速确认损失、国有化与剥离不良资产，可显著降低净财政成本','basis':'据瑞典净成本0—2%归纳','sources':['w-en-swedish-crisis-1990s']},
           {'holder':'拖延视角','view':'日本的"宽容"式处置使问题长期化，与瑞典形成对照','basis':'据两国处置比较归纳；因果待核实','sources':['w-en-japan-asset-bubble-1990']}],
  kd=[
   {'label':'Nordbanken与Götabanken救助成本','value':64,'unit':'十亿瑞典克朗','year':1992,'comparable_price':False,
    'note':'原文：Nordbanken and Götabanken were granted financial support and nationalized at a cost of 64 billion kronor；单一来源待核实。','sources':['w-en-swedish-crisis-1990s']},
   {'label':'救助初始成本占GDP','value':4,'unit':'%（后降至0—2%）','year':1992,'comparable_price':False,
    'note':'原文：This bailout initially cost about 4% of Sweden\'s GDP, later lowered to between 0–2% of GDP；单一来源待核实。','sources':['w-en-swedish-crisis-1990s']},
   {'label':'救助净成本占GDP(下界)','value':0,'unit':'%（0—2%区间下界）','year':1996,'comparable_price':False,
    'note':'原文：later lowered to between 0–2% of GDP depending on various assumptions due to the value of stock later sold；单一来源待核实。','sources':['w-en-swedish-crisis-1990s']},
  ],
  cmp=('与芬兰(1990s)、挪威(1988—1992)同属北欧银行危机群，共同背景是金融自由化后的信贷泡沫与1990年代初的深度衰退；'
   '瑞典的独特之处在于**处置方式的透明度与国有化力度**，其净财政成本显著低于日本。'
   '与2007—08次贷危机的成因相似性也常被强调。具体异同待核实。')),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': 'U4 20世纪下半', 'period': '20世纪下半', 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sorted(sp['tl'], key=lambda t:t.get('year',0)),
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': sp['kd'],
        'schools': sp['schools'],
        'policy_response': [],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st,s in sp['causal']] + [sp['cmp'] and 'w-en-finnish-banking-crisis'])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基全文；单源待核实。【续作CS】'
    }
    # 去重并清理 None
    entry['sources'] = list(dict.fromkeys([s for s in entry['sources'] if s]))
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r104_data.json', encoding='utf-8'))
for sid, key in [('w-en-nyc-fiscal-1975','nyc-1975'), ('w-en-swedish-crisis-1990s','sweden-1990s')]:
    if sid in ex: continue
    v = meta.get(key)
    if not v: continue
    sd['sources'].append({'id':sid,'title':v['title'],'author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+v['title'].replace(' ','_').replace('–','%E2%80%93'),
      'url2':None,'verified':True,'link_ok':True,'note':'Wikipedia API(full extract)核对(本会话抓取)'})
    ex.add(sid); print('新增来源',sid,'|',v['title'])
sd['count']=len(sd['sources'])
json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':sp['tier'],'status':'written',
      'source_count':2,'needs_verification':1,'last_updated':'2026-11-24',
      'unit':'U4 20世纪下半','period':'20世纪下半','region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
