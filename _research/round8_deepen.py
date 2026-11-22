# -*- coding: utf-8 -*-
"""轮次8 DEEPEN：为3条重要条目补来源核实的timeline与数值（维基原文实证）。"""
import json
DATA={
 'panic-1792':{
  'timeline':[
   {'year':1791,'display':'1791年冬','event':'威廉·杜尔、亚历山大·麦科姆等银行家的投机计划失败，成为银行挤兑主因之一（据 Wikipedia Panic of 1792）','sources':['w-en-panic-of-1792']},
   {'year':1791,'display':'1791年12月','event':'美国银行开始接受存款与贴现，大幅扩张信贷（同上）','sources':['w-en-panic-of-1792']},
   {'year':1792,'display':'1792年1月31日','event':'货币负债超过217万美元，贴现达268万美元（同上）','sources':['w-en-panic-of-1792']},
   {'year':1792,'display':'1792年3月21日','event':'委员会就是否允许公开市场购买出现分歧（同上）','sources':['w-en-panic-of-1792']},
  ],
 },
 'panic-1819':{
  'timeline':[
   {'year':1816,'display':'1816年4月','event':'国会通过并签署设立第二美国银行的法案（据 Wikipedia Panic of 1819）','sources':['w-en-panic-of-1819']},
   {'year':1817,'display':'1817年1月','event':'第二美国银行以20年特许状开始运营（同上）','sources':['w-en-panic-of-1819']},
   {'year':1818,'display':'1818年8月','event':'信贷过度扩张，银行分支机构开始拒收州特许银行纸币（同上）','sources':['w-en-panic-of-1819']},
   {'year':1819,'display':'1819年1月','event':'棉花价格单日下跌25%，恐慌爆发，经济陷入衰退（同上）','sources':['w-en-panic-of-1819']},
   {'year':1821,'display':'1821年','event':'国会通过《公共土地债务人救济法》（同上）','sources':['w-en-panic-of-1819']},
  ],
  'key_data':[
   {'label':'棉花价格单日跌幅(1819.1)','value':25,'unit':'%（美国棉花价格，单日）','year':1819,'comparable_price':False,
    'note':'原文：the value of cotton had broken—dropping 25% in a single day；单一来源待核实。','sources':['w-en-panic-of-1819']},
  ],
 },
 'panic-1825':{
  'timeline':[
   {'year':1821,'display':'1821年','event':'英格兰银行恢复纸币兑换黄金（据 Wikipedia Panic of 1825）','sources':['w-en-panic-of-1825']},
   {'year':1824,'display':'1824年','event':'伦敦交易所上市公司达624家（1770年仅5只股票），投机盛行（同上）','sources':['w-en-panic-of-1825']},
   {'year':1825,'display':'1825年','event':'源于英格兰银行的股市崩盘爆发，部分由拉美投机投资引发（同上）','sources':['w-en-panic-of-1825']},
   {'year':1826,'display':'1826年','event':'破产数量较危机前近乎翻倍（同上）','sources':['w-en-panic-of-1825']},
  ],
 },
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    have={t.get('display') for t in d.get('timeline',[])}
    for t in add['timeline']:
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in add.get('key_data',[]):
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','')+' 【轮次8深化】补入来源核实的timeline与数值，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'timeline',len(d['timeline']),'keydata',len(d['key_data']))
