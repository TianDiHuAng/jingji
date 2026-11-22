# -*- coding: utf-8 -*-
"""轮次23 DEEPEN-SEMANTIC 第四批：6条L2案例化（据本地维基语料）。"""
import json
SPEC={
 'black-friday-1869':{
  'causal':[
   ('Jay Gould、James Fisk 与 Abel Corbin 组成"黄金集团"(Gold Ring)，试图逼空黄金、抬升纽约金价','w-en-black-friday-1869'),
   ('1869年9月24日逼空失败、政府抛售黄金 → 黄金恐慌(黑色星期五)爆发','w-en-black-friday-1869'),
   ('恐慌引发金融危机','w-en-black-friday-1869')],
  'schools':[
   ('市场操纵/逼空视角','少数投机者合谋逼空黄金市场，失败后引发恐慌','w-en-black-friday-1869'),
   ('政府干预视角','联邦政府抛售黄金打破逼空，成为转折','w-en-black-friday-1869')],
 },
 'panic-1792':{
  'causal':[
   ('新成立的美国银行扩张信贷 + 杜尔(Duer)、麦科姆(Macomb)等银行家对国债与银行股的投机 → 信用膨胀','w-en-panic-of-1792'),
   ('投机者贷款违约、资产价格下跌，美国银行同时收紧信贷 → 银行挤兑','w-en-panic-of-1792'),
   ('1792年3—4月爆发信用危机(恐慌)','w-en-panic-of-1792')],
  'schools':[
   ('信贷扩张/投机视角','信贷膨胀叠加投机，违约后价格崩塌','w-en-panic-of-1792'),
   ('央行/信用收缩视角','美国银行同时收紧信贷加剧了挤兑','w-en-panic-of-1792')],
 },
 'kennedy-slide-1962':{
  'causal':[
   ('1929后数十年增长、1961年末股市见顶 → 1962年上半年暴跌','w-en-kennedy-slide-of-1962'),
   ('1962年5月28日道指单日大跌(被称为"1962闪崩")；标普500期内跌22.5%','w-en-kennedy-slide-of-1962'),
   ('直到古巴导弹危机结束后市场才稳定复苏','w-en-kennedy-slide-of-1962')],
  'schools':[
   ('估值/情绪视角','长期上涨后估值过高与情绪逆转引发抛售','w-en-kennedy-slide-of-1962'),
   ('事件冲击视角','古巴导弹危机等地缘事件延长了市场动荡','w-en-kennedy-slide-of-1962')],
 },
 'sterling-crisis-1976':{
  'causal':[
   ('1972年保守党"增长冲刺"预算开启通胀周期 → 1975年通胀近25%、国际收支与财政双赤字','w-en-1976-sterling-crisis'),
   ('1973石油危机加剧 → 英镑在1976年6月跌至对美元历史低点','w-en-1976-sterling-crisis'),
   ('卡拉汉工党政府向IMF借款39亿美元并实施紧缩','w-en-1976-sterling-crisis')],
  'schools':[
   ('通胀/财政视角','高通胀与双赤字削弱英镑信心','w-en-1976-sterling-crisis'),
   ('外部冲击视角','石油危机放大国际收支压力','w-en-1976-sterling-crisis')],
 },
 'panic-1837':{
  'causal':[
   ('1834年中—1836年中经济扩张积累投机与信贷；棉花价格1837年2—3月跌25%','w-en-panic-of-1837'),
   ('1837年初投资者恐慌、银行挤兑爆发(危机得名)','w-en-panic-of-1837'),
   ('萧条持续至1840年代中期；1848加州淘金增加货币供给加速复苏','w-en-panic-of-1837')],
  'schools':[
   ('商品价格/信贷视角','棉花价格暴跌与前期信贷扩张共同触发','w-en-panic-of-1837'),
   ('银行挤兑视角','银行挤兑使危机自我强化','w-en-panic-of-1837')],
 },
 'panic-1893':{
  'causal':[
   ('1880年代铁路等过度投资(准"股市泡沫")+巴林危机后外资撤离 → 1893年2月恐慌开始','w-en-panic-of-1893'),
   ('1893年5月5日国家绳索公司破产后道指单日跌24%','w-en-panic-of-1893'),
   ('约四分之一铁路里程进入破产管理，萧条加深','w-en-panic-of-1893')],
  'schools':[
   ('过度投资/泡沫视角','铁路过度扩张与投机泡沫破裂','w-en-panic-of-1893'),
   ('银行/信贷视角','银行倒闭与信贷收缩放大萧条','w-en-panic-of-1893')],
 },
}
for eid,spec in SPEC.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基原文归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['pending_notes']=d.get('pending_notes','')+' 【轮次23】causal_chain/schools案例化（据本地维基语料）。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'案例化 causal',len(d['causal_chain']),'schools',len(d['schools']))
