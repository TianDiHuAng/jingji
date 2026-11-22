# -*- coding: utf-8 -*-
"""轮次12：3条新条目按tier升级到目标层级（核心L3/重要L2），补真实timeline+数值。"""
import json
FRAME={'泡沫':{'chain':[('估值叙事+信贷可得 → 价格上涨','w-en-speculative-bubble'),('价格上涨自我强化 → 脱离基本面','w-en-speculative-bubble'),('信心逆转/流动性枯竭 → 抛售崩塌','w-en-financial-crisis')],
  'schools':[('非理性泡沫视角','群体投机导致价格远离基本面','w-en-speculative-bubble'),('有效市场视角','认为价格可由基本面解释','w-en-financial-crisis')]},
 '其他':{'chain':[('政策收紧/外部冲击 → 需求下降','w-en-fiscal-policy'),('产出与就业下降 → 衰退','w-en-recession'),('政策转向 → 复苏','w-en-monetary-policy')],
  'schools':[('需求管理视角','总需求政策可缓冲冲击','w-en-fiscal-policy'),('供给冲击视角','外部冲击改变增长路径','w-en-economic-history')]},
 '恶性通胀':{'chain':[('财政赤字货币化 → 货币供给过快增长','w-en-hyperinflation'),('通胀预期固化 → 价格加速','w-en-inflation'),('币值失序 → 改革','w-en-hyperinflation')],
  'schools':[('货币主义视角','通胀是货币现象','w-en-hyperinflation'),('财政视角','赤字货币化是根源','w-en-inflation')]}}
def svg(title,ct,feedback=False):
    e=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:26]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 780 280' role='img'>",f"<text x='20' y='26' class='ttl'>{e(title)}：机制{'+反馈' if feedback else ''}示意（{ct}）</text>"]
    nodes=[(30,'触发条件','冲击来源'),(215,'放大机制','信贷/预期'),(400,'临界转折','信心逆转'),(585,'后果与应对','崩盘/政策')] if feedback else [(20,'触发条件','冲击来源'),(270,'传导过程','风险扩散'),(520,'后果与应对','结果与政策')]
    for x,t,sub in nodes:
        w=160 if feedback else 210
        s.append(f"<g><rect x='{x}' y='60' width='{w}' height='52' rx='6' class='box'/><text x='{x+9}' y='83' class='lbl'>{t}</text><text x='{x+9}' y='101' class='sub'>{sub}</text></g>")
    if feedback:
        for a,b in [(190,215),(375,400),(560,585)]: s.append(f"<line x1='{a}' y1='86' x2='{b}' y2='86' class='ar'/>")
        s.append("<path d='M665 112 L665 170 L295 170 L295 112' fill='none' class='ar' style='stroke-dasharray:5,4'/>")
        s.append("<text x='400' y='163' class='sub'>反馈：后果强化放大机制</text>")
    else:
        s.append("<line x1='230' y1='86' x2='265' y2='86' class='ar'/><line x1='480' y1='86' x2='515' y2='86' class='ar'/>")
    s.append("<text x='20' y='230' class='note'>框架来源见本页来源列表；具体数值以正文为准。</text></svg>")
    return ''.join(s)
DATA={
 'black-monday-1987':{
  'level':'L3',
  'tl':[
   {'year':1982,'display':'1982年8月','event':'道指从776点开始牛市；标普500从102.42点起涨（据 Wikipedia Black Monday 1987）','sources':['w-en-black-monday-1987']},
   {'year':1987,'display':'1987年8月','event':'道指峰值2722点；标普500达336.77点（同上）','sources':['w-en-black-monday-1987']},
   {'year':1987,'display':'1987年10月16日','event':'道指下跌108.35点(4.6%)（同上）','sources':['w-en-black-monday-1987']},
   {'year':1987,'display':'1987年10月19日','event':'黑色星期一：道指单日下跌508点(22.6%)，为史上最大单日百分比跌幅；标普500跌20%（同上）','sources':['w-en-black-monday-1987']},
   {'year':1989,'display':'1989年7月26日','event':'道指才恢复至崩盘前高点（同上）','sources':['w-en-black-monday-1987']},
  ],
  'kd':[
   {'label':'道指单日跌幅(1987-10-19)','value':22.6,'unit':'%（道琼斯工业平均指数，单日）','year':1987,'comparable_price':False,
    'note':'原文：the DJIA fell 508 points (22.6 percent) ... largest one-day percentage drop in history；单一来源待核实。','sources':['w-en-black-monday-1987']},
   {'label':'标普500单日跌幅(1987-10-19)','value':20,'unit':'%（标普500，单日）','year':1987,'comparable_price':False,
    'note':'原文：By the end of the day, the S&P 500 had fallen 20%；单一来源待核实。','sources':['w-en-black-monday-1987']},
  ],
 },
 'recession-1937-1938':{
  'level':'L2',
  'tl':[
   {'year':1937,'display':'1937—1938年','event':'大萧条期间美国经济二次衰退（据 Wikipedia Recession of 1937–1938）','sources':['w-en-recession-1937-1938']},
   {'year':1938,'display':'1938年中','event':'经济开始复苏，但就业直到1941年末参战时恢复至1937初水平（同上）','sources':['w-en-recession-1937-1938']},
  ],
 },
 'rodrigazo-1975':{
  'level':'L2',
  'tl':[
   {'year':1975,'display':'1975年','event':'阿根廷"罗德里加索"经济计划，旨在应对通胀（据 Wikipedia Rodrigazo）','sources':['w-en-rodrigazo-1975']},
   {'year':1975,'display':'1975年内','event':'通胀率从1974年24.4%升至182.4%，年末更高达444%（同上）','sources':['w-en-rodrigazo-1975']},
  ],
  'kd':[
   {'label':'通胀率(1975年末)','value':444,'unit':'%（阿根廷CPI，1975年末）','year':1975,'comparable_price':False,
    'note':'原文：inflation rate rose from 24.4% in 1974 to 182.4% in 1975 and 444%（年末）；单一来源待核实。','sources':['w-en-rodrigazo-1975']},
  ],
 },
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']=add['level']; ct=d['crisis_type']; fr=FRAME.get(ct,FRAME['其他'])
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
    if add['level']=='L3':
        if not d.get('svg'): d['svg']=svg(d['title'],ct,True)
        if not d.get('l3_detail'): d['l3_detail']={'data_caveat':'数值须注明来源/年份/口径；本条目跌幅数据单一来源待核实。','controversy_summary':'各方解释并列，不替读者下结论。','framework_type':ct}
    elif not d.get('svg'): d['svg']=svg(d['title'],ct,False)
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+f' 【轮次12】升至{add["level"]}，补真实timeline与数值，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'→',add['level'],'tl',len(d['timeline']),'kd',len(d['key_data']))
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in DATA: e['level']=DATA[e['id']]['level']; e['last_updated']='2026-11-22'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage同步')
