# -*- coding: utf-8 -*-
"""轮次7 UPGRADE-L1：3条有专属来源的L1补充条目升级到L2，补真实timeline与数值。"""
import json

DATA={
 'australian-banking-1893':{
  'sid':'w-en-australian-banking-crisis-of-1893',
  'timeline':[
   {'year':1893,'display':'1893年','event':'澳大利亚殖民地多家商业银行与建房社团倒闭，伴随普遍经济萧条（据 Wikipedia Australian banking crisis of 1893）','sources':['w-en-australian-banking-crisis-of-1893']},
   {'year':1893,'display':'1893年（同期）','event':'与美国1893年恐慌同时发生（同上）','sources':['w-en-australian-banking-crisis-of-1893']},
   {'year':1896,'display':'1896—1902年','event':'联邦干旱期开始，加剧经济困境（同上）','sources':['w-en-australian-banking-crisis-of-1893']},
  ],
 },
 'kennedy-slide-1962':{
  'sid':'w-en-kennedy-slide-of-1962',
  'timeline':[
   {'year':1961,'display':'1961年12月','event':'股市在长期上涨后见顶（据 Wikipedia Kennedy Slide of 1962）','sources':['w-en-kennedy-slide-of-1962']},
   {'year':1962,'display':'1962年5月28日','event':'道琼斯工业平均指数单日下跌5.7%，被称为"1962闪电崩盘"（同上）','sources':['w-en-kennedy-slide-of-1962']},
   {'year':1962,'display':'1962年6月','event':'标普500指数累计下跌22.5%；高点到低点股票纸面价值缩水约27%（同上）','sources':['w-en-kennedy-slide-of-1962']},
  ],
  'key_data':[
   {'label':'标普500跌幅(1961.12—1962.6)','value':22.5,'unit':'%（标普500指数，区间累计）','year':1962,'comparable_price':False,
    'note':'原文：Through June 1962, the S&P 500 experienced a 22.5% decline；单一来源待核实。','sources':['w-en-kennedy-slide-of-1962']},
  ],
 },
 'sterling-crisis-1976':{
  'sid':'w-en-1976-sterling-crisis',
  'timeline':[
   {'year':1972,'display':'1972年','event':'保守党"增长冲刺"预算开启通胀周期（据 Wikipedia 1976 sterling crisis）','sources':['w-en-1976-sterling-crisis']},
   {'year':1975,'display':'1975年','event':'通胀接近25%，推高债券收益率与借贷成本（同上）','sources':['w-en-1976-sterling-crisis']},
   {'year':1976,'display':'1976年6月','event':'英镑兑美元跌至历史低点，危机爆发（同上）','sources':['w-en-1976-sterling-crisis']},
  ],
  'key_data':[
   {'label':'英国通胀率(1975)','value':25,'unit':'%（接近25%，英国CPI，1975年）','year':1975,'comparable_price':False,
    'note':'原文：Inflation (at close to 25% in 1975)；"接近"为约数表述，单一来源待核实。','sources':['w-en-1976-sterling-crisis']},
  ],
 },
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'  # 升级
    have={t.get('display') for t in d.get('timeline',[])}
    for t in add['timeline']:
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in add.get('key_data',[]):
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    # causal_chain/shools 已有L2结构（之前通用升级），保留
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','')+' 【轮次7】L1→L2升级，补入来源核实时间线与数值，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'→L2, timeline',len(d['timeline']))

# 同步 coverage
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in DATA: e['level']='L2'; e['last_updated']='2026-11-22'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage 同步')
