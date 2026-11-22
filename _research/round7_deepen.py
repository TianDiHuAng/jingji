# -*- coding: utf-8 -*-
"""轮次7 DEEPEN-L2：为2条重要条目补入来源核实的timeline与数值。
事件与数字直接来自已抓取的Wikipedia正文，注明来源，单源标注待核实。"""
import json

DATA={
 'panic-1837':{
  'timeline':[
   {'year':1834,'display':'1834年中—1836年中','event':'经济扩张期，为随后的危机埋下信贷与投机基础（据 Wikipedia Panic of 1837）','sources':['w-en-panic-of-1837']},
   {'year':1837,'display':'1837年2—3月','event':'棉花价格下跌25%（同上）','sources':['w-en-panic-of-1837']},
   {'year':1837,'display':'1837年初','event':'投资者恐慌，发生银行挤兑，"恐慌"由此得名（同上）','sources':['w-en-panic-of-1837']},
   {'year':1837,'display':'1837年3月','event':'马丁·范布伦就任总统（就职仅五周后危机爆发，故被归责）（同上）','sources':['w-en-panic-of-1837']},
   {'year':1839,'display':'1839年','event':'农产品价格下跌，压力传导至农业部门（同上）','sources':['w-en-panic-of-1837']},
   {'year':1848,'display':'1848年','event':'加州发现黄金，淘金热增加货币供给，加速复苏（同上）','sources':['w-en-panic-of-1837']},
  ],
  'key_data':[
   {'label':'棉花价格跌幅(1837年2—3月)','value':25,'unit':'%（美国棉花价格，月内累计）','year':1837,'comparable_price':False,
    'note':'原文：The price of cotton fell by 25% in February and March 1837；单一来源 w-en-panic-of-1837，待第二来源核实。','sources':['w-en-panic-of-1837']},
  ],
 },
 'panic-1893':{
  'timeline':[
   {'year':1890,'display':'1890年','event':'巴林银行危机与阿根廷投资受挫，构成前奏（据 Wikipedia Panic of 1893）','sources':['w-en-panic-of-1893']},
   {'year':1893,'display':'1893年2月','event':'恐慌开始，持续约八个月后正式结束（同上）','sources':['w-en-panic-of-1893']},
   {'year':1893,'display':'1893年5月5日','event':'国家绳索公司破产后，道琼斯工业平均指数单日下跌24%（同上）','sources':['w-en-panic-of-1893']},
   {'year':1893,'display':'1893年','event':'约四分之一铁路里程进入破产管理（同上）','sources':['w-en-panic-of-1893']},
   {'year':1895,'display':'1895年','event':'铁路扩张资本支出回升（同上）','sources':['w-en-panic-of-1893']},
  ],
  'key_data':[
   {'label':'道指单日跌幅(1893-05-05)','value':24,'unit':'%（道琼斯工业平均指数，单日）','year':1893,'comparable_price':False,
    'note':'原文：on May 5, 1893, the Dow Jones Industrial Average fell 24% in a single day；单一来源，待第二来源核实。','sources':['w-en-panic-of-1893']},
  ],
 },
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    # timeline 去重（按display）
    have={t.get('display') for t in d.get('timeline',[])}
    for t in add['timeline']:
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    # key_data 去重（按label）
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in add['key_data']:
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','')+' 【轮次7深化】补入来源核实的timeline与数值，单源部分待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'timeline',len(d['timeline']),'keydata',len(d['key_data']))
