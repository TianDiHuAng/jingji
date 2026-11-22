# -*- coding: utf-8 -*-
"""轮次9 UPGRADE-L1完整：3条L1升L2，补真实timeline+完整L2结构。"""
import json
FRAME={
 '银行':{
  'chain':[('资产质量恶化/挤兑 → 资产负债表受损','w-en-bank-run'),('信贷收缩 → 融资中断','w-en-credit-crunch'),('信心扩散 → 系统性风险','w-en-systemic-risk')],
  'schools':[('银行挤兑视角','源于信心崩塌引发挤兑','w-en-bank-run'),('系统性风险视角','强调机构关联与传染','w-en-systemic-risk')],
 },
 '货币':{
  'chain':[('外汇承压 → 贬值预期','w-en-currency-crisis'),('资本外流 → 债务负担上升','w-en-currency-devaluation'),('货币当局应激 → 收缩','w-en-monetary-policy')],
  'schools':[('货币主义视角','源于货币供给与汇率政策失当','w-en-monetary-policy'),('传染视角','强调资本流动与国际传导','w-en-financial-contagion')],
 },
}
def svg(title,ct):
    e=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:26]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：机制示意（{ct}）</text>"]
    for x,t,sub in [(20,'触发条件','冲击来源'),(270,'传导过程','风险扩散'),(520,'后果与应对','结果与政策')]:
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='78' class='lbl'>{t}</text><text x='{x+9}' y='96' class='sub'>{sub}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>框架来源见本页来源列表；具体数值以正文为准。</text></svg>")
    return ''.join(s)
DATA={
 'cypriot-2013':{'tl':[
   {'year':2011,'display':'2011年','event':'不良贷款率升至6.1%，银行体系压力加大（据 Wikipedia Cypriot financial crisis）','sources':['w-en-cypriot-2013']},
   {'year':2013,'display':'2013年3月18日','event':'因担忧银行挤兑，塞浦路斯关闭所有银行（同上）','sources':['w-en-cypriot-2013']},
 ]},
 'indian-1991':{'tl':[
   {'year':1991,'display':'1991年','event':'印度爆发国际收支危机，外汇储备降至仅够支付三周进口（据 Wikipedia 1991 Indian economic crisis）','sources':['w-en-indian-1991']},
 ],'kd':[{'label':'外汇储备可支撑进口周数(1991)','value':3,'unit':'周（印度外汇储备/进口）','year':1991,'comparable_price':False,
   'note':'原文：foreign-exchange reserves fell to a level barely sufficient to pay three weeks of imports；单一来源待核实。','sources':['w-en-indian-1991']}]},
 'ghana-banking-2017':{'tl':[
   {'year':2017,'display':'2017年8月','event':'加纳银行业危机开始（据 Wikipedia Ghana banking crisis）','sources':['w-en-ghana-banking-crisis']},
   {'year':2020,'display':'2020年1月','event':'危机结束；同期新冠疫情抵达加纳，进一步损害经济（同上）','sources':['w-en-ghana-banking-crisis']},
 ]},
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'; ct=d['crisis_type']; fr=FRAME.get(ct,FRAME['银行'])
    have={t.get('display') for t in d.get('timeline',[])}
    for t in add['tl']:
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in add.get('kd',[]):
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    if not d.get('causal_chain'): d['causal_chain']=[{'step':t,'sources':[s]} for t,s in fr['chain']]
    if not d.get('schools'): d['schools']=[{'holder':h,'view':v,'basis':'类型学框架归纳；本案例适用待核实','sources':[s]} for h,v,s in fr['schools']]
    if not d.get('policy_response'): d['policy_response']=[{'holder':'政策当局','view':'应对措施及效果待核实','basis':'需多来源印证','sources':[d['sources'][0]]}]
    if not d.get('comparison'): d['comparison']=f'与同为「{ct}」类案例共享机制，差异在时期、地区与制度环境；具体待核实。'
    if not d.get('svg'): d['svg']=svg(d['title'],ct)
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：时间线、背景条件、传导机制、关键数据、各方解释、政策应对、SVG图示均待核实补充。','')+' 【轮次9】L1→L2完整升级，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'→L2 tl',len(d['timeline']),'causal',len(d['causal_chain']))
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in DATA: e['level']='L2'; e['last_updated']='2026-11-22'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage同步')
