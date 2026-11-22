# -*- coding: utf-8 -*-
"""轮次13 UPGRADE：2条"重要"新条目升L2（中文维基原文实证）。"""
import json
FRAME={'泡沫':{'chain':[('信贷可得+政策利好 → 资产价格上涨','w-en-speculative-bubble'),('价格上涨自我强化 → 脱离基本面','w-en-speculative-bubble'),('政策收紧/信心逆转 → 抛售崩塌','w-en-financial-crisis')],
  'schools':[('非理性泡沫视角','群体投机导致价格远离基本面','w-en-speculative-bubble'),('政策调控视角','宏观政策转向是崩盘的直接触发','w-en-fiscal-policy')]}}
def svg(title,ct):
    e=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:26]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：机制示意（{ct}）</text>"]
    for x,t,sub in [(20,'触发条件','政策/信贷'),(270,'传导过程','价格自我强化'),(520,'后果与应对','崩盘/调控')]:
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='78' class='lbl'>{t}</text><text x='{x+9}' y='96' class='sub'>{sub}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>框架来源见本页来源列表；具体数值以正文为准。</text></svg>")
    return ''.join(s)
DATA={
 'hainan-property-bubble-1992':{
  'sid':'w-zh-hainan-property-bubble-1992',
  'tl':[
   {'year':1988,'display':'1988年8月23日','event':'海南脱离广东独立建省并设经济特区，约10万人涌入（据中文维基海南房地产泡沫）','sources':['w-zh-hainan-property-bubble-1992']},
   {'year':1992,'display':'1992年','event':'南巡讲话与住房改革刺激下房价飙升，海口房价翻4倍多至约5000元/平方米（同上）','sources':['w-zh-hainan-property-bubble-1992']},
   {'year':1993,'display':'1993年6月23—24日','event':'国务院宣布终止房企上市并颁布"国16条"调控，房价一落千丈（同上）','sources':['w-zh-hainan-property-bubble-1992']},
   {'year':1998,'display':'1998年','event':'海南发展银行因挤兑倒闭（同上）','sources':['w-zh-hainan-property-bubble-1992']},
   {'year':2008,'display':'2008年','event':'政府才清理完海南烂尾楼（同上）','sources':['w-zh-hainan-property-bubble-1992']},
  ],
  'kd':[
   {'label':'房地产企业倒闭比例','value':95,'unit':'%（海南，调控后倒闭房企占比，"95%以上"取近似）','year':1993,'comparable_price':False,
    'note':'原文：95%以上的房地产公司在调控中倒闭；单一来源待核实。','sources':['w-zh-hainan-property-bubble-1992']},
   {'label':'四大行坏账','value':300,'unit':'亿元人民币（中行/建行/工行/农行在海南的坏账，"300多亿"取近似）','year':1993,'comparable_price':False,
    'note':'原文：国有四大行坏账300多亿；单一来源待核实。','sources':['w-zh-hainan-property-bubble-1992']},
  ],
 },
 'us-video-game-crash-1983':{
  'sid':'w-zh-us-video-game-crash-1983',
  'tl':[
   {'year':1982,'display':'1982年春','event':'Commodore下调VIC-20与C64价格，家用电脑价格竞争加剧（据中文维基1983年游戏业大萧条）','sources':['w-zh-us-video-game-crash-1983']},
   {'year':1983,'display':'1983—1984年','event':'美国游戏业市场大萧条，终结第二世代电视游戏市场（同上）','sources':['w-zh-us-video-game-crash-1983']},
   {'year':1985,'display':'1985年底','event':'任天堂NES打破僵局（同上）','sources':['w-zh-us-video-game-crash-1983']},
   {'year':1987,'display':'1987年','event':'任天堂重新激活家用游戏机市场（同上）','sources':['w-zh-us-video-game-crash-1983']},
  ],
  'kd':[
   {'label':'北美游戏业营收跌幅(1983→1985)','value':97,'unit':'%（北美游戏业，32亿美元降至1亿美元）','year':1985,'comparable_price':False,
    'note':'原文：行业营收由1983年的32亿美元降至1985年的1亿美元，跌幅高达97%；单一来源待核实。','sources':['w-zh-us-video-game-crash-1983']},
  ],
 },
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
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【轮次13】升L2，补中文维基原文实证的timeline与数值，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'→L2 tl',len(d['timeline']),'kd',len(d['key_data']))
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in DATA: e['level']='L2'; e['last_updated']='2026-11-22'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage同步')
