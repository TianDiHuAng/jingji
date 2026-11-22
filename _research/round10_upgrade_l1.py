# -*- coding: utf-8 -*-
"""轮次10 UPGRADE-L1完整：3条L1升L2，补真实timeline+数值+完整结构。"""
import json
FRAME={
 '银行':{'chain':[('资产质量恶化/挤兑 → 资产负债表受损','w-en-bank-run'),('信贷收缩 → 融资中断','w-en-credit-crunch'),('信心扩散 → 系统性风险','w-en-systemic-risk')],
   'schools':[('银行挤兑视角','源于信心崩塌引发挤兑','w-en-bank-run'),('系统性风险视角','强调机构关联与传染','w-en-systemic-risk')]},
 '债务':{'chain':[('举债扩张+偿付假设 → 债务累积','w-en-debt-crisis'),('利率上升/收入下降 → 偿付困难暴露','w-en-sovereign-default'),('违约或重组 → 债权人损失与传染','w-en-financial-contagion')],
   'schools':[('债务周期视角','过度负债与通缩相互强化','w-en-debt-crisis'),('主权违约视角','强调偿付意愿与制度安排','w-en-sovereign-default')]},
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
 'icelandic-crisis-2008':{'tl':[
   {'year':2008,'display':'2008—2010年','event':'冰岛发生重大金融危机，导致严重衰退（据 Wikipedia Icelandic financial crisis）','sources':['w-en-icelandic-crisis-2008']},
   {'year':2008,'display':'2008年11月','event':'实施资本管制（同上）','sources':['w-en-icelandic-crisis-2008']},
   {'year':2009,'display':'2009年','event':'爆发金融危机抗议活动（同上）','sources':['w-en-icelandic-crisis-2008']},
   {'year':2011,'display':'2011年8月31日','event':'IMF主导的国际救助计划正式结束（同上）','sources':['w-en-icelandic-crisis-2008']},
 ]},
 'uruguay-2002':{'tl':[
   {'year':2001,'display':'2001年12月','event':'阿根廷金融危机期间实施资本管制与存款冻结，波及乌拉圭（据 Wikipedia 2002 Uruguay banking crisis）','sources':['w-en-uruguay-2002']},
   {'year':2002,'display':'2002年7月','event':'乌拉圭爆发重大银行危机（同上）','sources':['w-en-uruguay-2002']},
 ]},
 'pakistan-crisis-2021':{'sid':'w-en-pakistani-economic-crisis-2021-2024','tl':[
   {'year':2021,'display':'2021年末','event':'燃料短缺与通胀飙升助推危机（据 Wikipedia Pakistani economic crisis）','sources':['w-en-pakistani-economic-crisis-2021-2024']},
   {'year':2022,'display':'2022年6月','event':'通胀达历史高位，粮价上涨（同上）','sources':['w-en-pakistani-economic-crisis-2021-2024']},
   {'year':2022,'display':'2022年','event':'巴基斯坦洪灾加剧危机，造成约300亿美元经济损失（同上）','sources':['w-en-pakistani-economic-crisis-2021-2024']},
   {'year':2023,'display':'2023年初','event':'和平时期首次濒临主权违约（同上）','sources':['w-en-pakistani-economic-crisis-2021-2024']},
 ],'kd':[
   {'label':'2022洪灾经济损失','value':30,'unit':'十亿美元（巴基斯坦，2022洪灾，约数）','year':2022,'comparable_price':False,
    'note':'原文：2022 Pakistan floods caused major economic losses worth $30 billion；单一来源待核实。','sources':['w-en-pakistani-economic-crisis-2021-2024']},
   {'label':'贫困率(2018–19→2024–25)','value':28.8,'unit':'%（巴基斯坦，2024–25，起点2018–19为21.9%）','year':2025,'comparable_price':False,
    'note':'原文：national poverty rate ... from 21.9% in 2018–2019 to 28.8% in 2024–2025；单一来源、现状类数据待核实。','sources':['w-en-pakistani-economic-crisis-2021-2024']},
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
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：时间线、背景条件、传导机制、关键数据、各方解释、政策应对、SVG图示均待核实补充。','')+' 【轮次10】L1→L2完整升级，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'→L2 tl',len(d['timeline']),'kd',len(d['key_data']),'causal',len(d['causal_chain']))
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in DATA: e['level']='L2'; e['last_updated']='2026-11-22'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage同步')
