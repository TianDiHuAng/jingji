# -*- coding: utf-8 -*-
"""轮次10 DEEPEN：3条重要条目补来源核实的timeline与数值（维基原文实证）。"""
import json
DATA={
 'bank-crisis-2023':{
  'tl':[
   {'year':2023,'display':'2023年3月','event':'五天内三家中小型美国银行倒闭，引发全球银行股下跌与监管快速反应（据 Wikipedia 2023 US banking crisis）','sources':['w-en-2023-united-states-banking-crisis']},
   {'year':2023,'display':'2023年3月10日','event':'硅谷银行(SVB)因出售国债组合遭遇大额亏损引发挤兑，被监管机构接管（同上）','sources':['w-en-2023-united-states-banking-crisis']},
   {'year':2023,'display':'2023年3月12日','event':'签名银行因系统性风险被监管机构关闭（同上）','sources':['w-en-2023-united-states-banking-crisis']},
   {'year':2023,'display':'2023年3月16日','event':'美联储贴现窗口向各银行放贷约1500亿美元（同上）','sources':['w-en-2023-united-states-banking-crisis']},
   {'year':2023,'display':'2023年5月1日','event':'FDIC宣布第一共和银行被关闭并出售给摩根大通（同上）','sources':['w-en-2023-united-states-banking-crisis']},
  ],
  'kd':[{'label':'美联储贴现窗口借款(截至2023-03-16)','value':150,'unit':'十亿美元（美元，贴现窗口累计借款）','year':2023,'comparable_price':False,
   'note':'原文：The Federal Reserve discount window ... approximately $150 billion in borrowing ... by March 16；单一来源待核实。','sources':['w-en-2023-united-states-banking-crisis']}],
 },
 'lebanese-liquidity-2019':{
  'tl':[
   {'year':2019,'display':'2019年10月17日','event':'"十月革命"首次大型示威后，黎巴嫩商业银行史无前例关闭两周（据 Wikipedia Lebanese liquidity crisis）','sources':['w-en-lebanese-liquidity-crisis']},
   {'year':2021,'display':'至2021年4月','event':'储户转购Solidere公司股票，推动其股价自流动性危机起上涨约500%（同上）','sources':['w-en-lebanese-liquidity-crisis']},
   {'year':2022,'display':'2022年1月起','event':'多名武装储户在银行网点实施抢劫与静坐以提取存款（同上）','sources':['w-en-lebanese-liquidity-crisis']},
  ],
 },
 'shanghai-rubber-1910':{
  'tl':[
   {'year':1910,'display':'1910年','event':'上海橡皮股票风潮爆发，银行家与股东过度炒作橡胶股票（据 Wikipedia Shanghai rubber stock market crisis）','sources':['w-en-shanghai-rubber-stock-market-crisis']},
   {'year':1911,'display':'1911年3月','event':'怡和洋行(原 spelling)破产后，本国与外国银行（如渣打银行）均蒙受巨额损失（同上）','sources':['w-en-shanghai-rubber-stock-market-crisis']},
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
    d['pending_notes']=d.get('pending_notes','')+' 【轮次10深化】补入来源核实的timeline与数值，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'timeline',len(d['timeline']),'kd',len(d['key_data']))
