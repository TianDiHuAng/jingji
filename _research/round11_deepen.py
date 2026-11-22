# -*- coding: utf-8 -*-
"""轮次11 DEEPEN：2条史料丰富的重要条目补真实timeline与数值。"""
import json
DATA={
 'chinese-stock-bubble-2007':{
  'tl':[
   {'year':2007,'display':'2007年2月27日','event':'上证综指单日暴跌9%，为10年来最大跌幅；传言政府将加息并打击借贷投机（据 Wikipedia Chinese stock bubble of 2007）','sources':['w-en-chinese-stock-bubble-of-2007']},
   {'year':2007,'display':'2007年2月27日（全球传导）','event':'道琼斯工业指数下跌416.02点（3.29%），为2001年九一一以来最大单日跌幅；标普500跌3.47%（同上）','sources':['w-en-chinese-stock-bubble-of-2007']},
   {'year':2007,'display':'2007年10月','event':'上证综指升至6092点峰值（同上）','sources':['w-en-chinese-stock-bubble-of-2007']},
   {'year':2007,'display':'2007年11月—2008年11月','event':'股市自峰值大幅下跌（同上）','sources':['w-en-chinese-stock-bubble-of-2007']},
  ],
  'kd':[
   {'label':'上证综指单日跌幅(2007-02-27)','value':9,'unit':'%（上证综指，单日）','year':2007,'comparable_price':False,
    'note':'原文：the SSE Composite Index ... tumbled 9%, the largest drop in 10 years；单一来源待核实。','sources':['w-en-chinese-stock-bubble-of-2007']},
   {'label':'上证综指峰值(2007-10)','value':6092,'unit':'点（上证综指，2007年10月峰值）','year':2007,'comparable_price':False,
    'note':'原文：Shanghai Composite then raised to peak 6,092 in October 2007；单一来源待核实。','sources':['w-en-chinese-stock-bubble-of-2007']},
  ],
 },
 'showa-crisis-1927':{
  'tl':[
   {'year':1923,'display':'1923年','event':'关东大地震加剧日本经济萧条，企业倒闭增多（据 Wikipedia Shōwa financial crisis）','sources':['w-en-sh-wa-financial-crisis']},
   {'year':1927,'display':'1927年1月','event':'政府提议兑付"地震债券"引发银行破产谣言（同上）','sources':['w-en-sh-wa-financial-crisis']},
   {'year':1927,'display':'1927年','event':'挤兑爆发，全国37家银行（含台湾银行）与铃木商店倒闭，若槻礼次郎首相辞职（同上）','sources':['w-en-sh-wa-financial-crisis']},
   {'year':1927,'display':'1927年（后续）','event':'田中义一首相以三周银行假期与紧急贷款控制局面（同上）','sources':['w-en-sh-wa-financial-crisis']},
  ],
 },
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    have={t.get('display') for t in d.get('timeline',[])}
    for t in add['tl']:
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in add.get('kd',[]):
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','')+' 【轮次11深化】补入来源核实的timeline与数值，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'timeline',len(d['timeline']),'kd',len(d['key_data']))
