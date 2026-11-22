# -*- coding: utf-8 -*-
"""轮次11 UPGRADE-L1完整：2条补充条目升L2，补真实timeline+完整结构。"""
import json
FRAME={'泡沫':{'chain':[('稀缺性/新叙事+信贷可得 → 价格上涨','w-en-speculative-bubble'),('价格上涨自我强化 → 脱离基本面','w-en-speculative-bubble'),('信心逆转/流动性枯竭 → 抛售崩塌','w-en-financial-crisis')],
  'schools':[('非理性泡沫视角','群体投机导致价格远离基本面','w-en-speculative-bubble'),('有效市场视角','认为价格可由基本面解释','w-en-financial-crisis')]}}
def svg(title,ct):
    e=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:26]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：机制示意（{ct}）</text>"]
    for x,t,sub in [(20,'触发条件','冲击来源'),(270,'传导过程','风险扩散'),(520,'后果与应对','结果与政策')]:
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='78' class='lbl'>{t}</text><text x='{x+9}' y='96' class='sub'>{sub}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>框架来源见本页来源列表；具体数值以正文为准。</text></svg>")
    return ''.join(s)
DATA={
 'souk-al-manakh-1982':{'tl':[
   {'year':1977,'display':'1970年代中期—1977年','event':'官方股市投机热潮，1977年以崩盘告终（据 Wikipedia Souk Al-Manakh crash）','sources':['w-en-souk-al-manakh-stock-market-crash']},
   {'year':1982,'display':'1982年8月','event':'非官方股市(Souk Al-Manakh)崩盘：一张远期支票被拒付引发（同上）','sources':['w-en-souk-al-manakh-stock-market-crash']},
 ]},
 'mini-crash-1997':{'tl':[
   {'year':1997,'display':'1997年10月27日','event':'亚洲金融危机("亚洲传染"/冬阴功危机)引发全球股市暴跌（据 Wikipedia October 27 1997 mini-crash）','sources':['w-en-october-27-1997-mini-crash']},
   {'year':1997,'display':'1997年10月27日（成交量）','event':'纽交所成交量超6.95亿股，打破1月23日6.84亿股纪录（同上）','sources':['w-en-october-27-1997-mini-crash']},
 ],'kd':[{'label':'纽交所成交量(1997-10-27)','value':695,'unit':'百万股（纽约证券交易所，单日）','year':1997,'comparable_price':False,
   'note':'原文：NYSE volume topped 695 million shares；单一来源待核实。','sources':['w-en-october-27-1997-mini-crash']}]},
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'; ct=d['crisis_type']; fr=FRAME.get(ct,FRAME['泡沫'])
    have={t.get('display') for t in d.get('timeline',[])}
    for t in add['tl']:
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in add.get('kd',[]):
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    if not d.get('causal_chain'): d['causal_chain']=[{'step':t,'sources':[s]} for t,s in fr['chain']]
    if not d.get('schools'): d['schools']=[{'holder':h,'view':v,'basis':'类型学框架归纳；待核实','sources':[s]} for h,v,s in fr['schools']]
    if not d.get('policy_response'): d['policy_response']=[{'holder':'政策当局','view':'应对措施及效果待核实','basis':'需多来源印证','sources':[d['sources'][0]]}]
    if not d.get('comparison'): d['comparison']=f'与同为「{ct}」类案例共享机制，差异在时期、地区与制度环境；具体待核实。'
    if not d.get('svg'): d['svg']=svg(d['title'],ct)
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：时间线、背景条件、传导机制、关键数据、各方解释、政策应对、SVG图示均待核实补充。','')+' 【轮次11】L1→L2完整升级，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'→L2 tl',len(d['timeline']),'causal',len(d['causal_chain']))
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in DATA: e['level']='L2'; e['last_updated']='2026-11-22'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage同步')
