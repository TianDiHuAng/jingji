# -*- coding: utf-8 -*-
"""轮次9：修正brexit-crash-2016错配来源 + 3条重要条目补真实timeline。"""
import json, urllib.parse
sd=json.load(open('data/sources.json',encoding='utf-8'))
sid='w-en-brexit'
if sid not in {x['id'] for x in sd['sources']}:
    sd['sources'].append({'id':sid,'title':'Brexit','author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/Brexit','url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia API核对(pageid=41688778)；轮次9修正brexit-crash-2016错配来源新增'})
    sd['count']=len(sd['sources'])
    json.dump(sd,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('新增',sid)

DATA={
 'brexit-crash-2016':{
  'fix_wrong':'w-en-black-monday-1987','fix_to':'w-en-brexit',
  'tl':[
   {'year':2016,'display':'2016年6月23日','event':'英国就继续留在欧盟举行公投（据 Wikipedia Brexit）','sources':['w-en-brexit']},
   {'year':2020,'display':'2020年12月31日','event':'过渡期结束（同上）','sources':['w-en-brexit']},
  ],
 },
 'irish-banking-2008':{
  'tl':[
   {'year':2005,'display':'2005年6月','event':'《经济学人》列爱尔兰于房价通胀名单，1997–2005房价涨幅192%为其列表最高（据 Wikipedia Post-2008 Irish banking crisis）','sources':['w-en-post-2008-irish-banking-crisis']},
   {'year':2008,'display':'2008年后','event':'多家爱尔兰金融机构因资不抵债濒临崩溃（同上）','sources':['w-en-post-2008-irish-banking-crisis']},
   {'year':2011,'display':'2011年3月','event':'央行行长Patrick Honohan称其为"世界史上最昂贵的银行危机之一"（同上）','sources':['w-en-post-2008-irish-banking-crisis']},
  ],
  'kd':[{'label':'房价涨幅(1997–2005)','value':192,'unit':'%（爱尔兰，1997–2005累计）','year':2005,'comparable_price':False,
         'note':'原文：Ireland’s price inflation of 192% in 1997–2005 was the highest on its list；单一来源待核实。','sources':['w-en-post-2008-irish-banking-crisis']}],
 },
 'turkish-crisis-2018':{
  'tl':[
   {'year':2018,'display':'2018年','event':'财政部长Albayrak公布新经济计划以应对危机（据 Wikipedia Turkish economic crisis）','sources':['w-en-turkish-economic-crisis']},
   {'year':2023,'display':'2023年','event':'埃尔多安在Şimşek与Erkan指导下转向正统银行方法（同上）','sources':['w-en-turkish-economic-crisis']},
   {'year':2024,'display':'2024年11月','event':'通胀降至47.09%，低于历史高点83%（同上；现状类数据，截至2024-11）','sources':['w-en-turkish-economic-crisis']},
  ],
  'kd':[{'label':'通胀率(2024年11月)','value':47.09,'unit':'%（土耳其CPI同比，2024-11；现状类数据）','year':2024,'comparable_price':False,
         'note':'原文：as of November 2024, inflation is at 47.09%, down from its all-time high of 83%；单一来源、现状类数据待核实。','sources':['w-en-turkish-economic-crisis']}],
 },
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    if 'fix_wrong' in add:
        d['sources']=[s for s in d['sources'] if s!=add['fix_wrong']]
        if add['fix_to'] not in d['sources']: d['sources'].append(add['fix_to'])
        d['pending_notes']=d.get('pending_notes','')+f' 【轮次9】修正错配来源{add["fix_wrong"]}→{add["fix_to"]}。'
    have={t.get('display') for t in d.get('timeline',[])}
    for t in add['tl']:
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in add.get('kd',[]):
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    d['needs_verification']=True
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'timeline',len(d['timeline']),'kd',len(d['key_data']))
