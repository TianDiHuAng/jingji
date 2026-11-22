# -*- coding: utf-8 -*-
"""轮次25 DEEPEN-SEMANTIC 第六批：2核心L3 + 4条案例化（据本地维基语料）。"""
import json
SPEC={
 'asian-financial-crisis-1997':{
  'causal':[
   ('泰国等经济体外债高企、维持固定钉住+热钱涌入 → 脆弱性累积(东盟四国外债/GDP 1993→1996升至167%)','w-en-asian-financial-crisis'),
   ('1997年7月始于泰国的货币贬值 → 经金融传染波及东南亚、韩国、日本等','w-en-asian-financial-crisis'),
   ('货币贬值、股市与资产价格下挫、债务负担骤升；1998-99快速复苏','w-en-asian-financial-crisis')],
  'schools':[
   ('固定汇率/外债视角','钉住汇率+高外债+热钱使经济体易受投机攻击','w-en-asian-financial-crisis'),
   ('金融传染视角','危机经贸易与资本流动在区域内快速传播','w-en-financial-contagion')],
 },
 'black-monday-1987':{
  'causal':[
   ('1982-1987年强劲牛市使估值高企(道指776→2722)；程序化/组合保险交易盛行','w-en-black-monday-1987'),
   ('1987年10月19日全球同步抛售，道指单日跌508点(22.6%)，为史上最大单日百分比跌幅','w-en-black-monday-1987'),
   ('标普500当日跌20%；市场直到1989年才恢复前高','w-en-black-monday-1987')],
  'schools':[
   ('估值/程序交易视角','牛市高估叠加程序化交易的顺周期抛售放大跌幅','w-en-black-monday-1987'),
   ('国际传染视角','全球市场同步下跌，跨市场传染明显','w-en-financial-contagion')],
 },
 'brexit-crash-2016':{
  'causal':[
   ('2016年6月23日英国公投决定脱离欧盟，出乎市场预期','w-en-brexit'),
   ('结果公布后英镑急跌、全球股市下挫','w-en-brexit'),
   ('此后进入直至2020年底的过渡期','w-en-brexit')],
  'schools':[
   ('政治事件冲击视角','公投结果超预期，重估英国与欧盟关系风险','w-en-brexit'),
   ('不确定性/信心视角','贸易与监管不确定性打击市场信心','w-en-financial-crisis')],
 },
 'panic-1825':{
  'causal':[
   ('19世纪初英国金融体系快速扩张、对拉美投机性投资增加 → 投机泡沫','w-en-panic-of-1825'),
   ('1825年危机源于英格兰银行，股市崩盘、多家银行倒闭(英格兰银行自身亦近危)','w-en-panic-of-1825'),
   ('1826年破产数近乎翻倍','w-en-panic-of-1825')],
  'schools':[
   ('投机/信贷视角','对拉美等海外市场的投机与宽松信贷催生泡沫','w-en-panic-of-1825'),
   ('央行/黄金储备视角','英格兰银行储备与政策应对影响危机深度','w-en-gold-standard')],
 },
 'south-america-2002':{
  'causal':[
   ('2002年阿根廷、巴西、乌拉圭等国出现经济动荡','w-en-south-american-economic-crisis-of-2002'),
   ('阿根廷危机与货币贬值经贸易金融渠道波及邻国(乌拉圭、巴西)','w-en-south-american-economic-crisis-of-2002'),
   ('区域经济与金融承压','w-en-south-american-economic-crisis-of-2002')],
  'schools':[
   ('区域传染视角','阿根廷危机通过贸易与金融传染南美邻国','w-en-financial-contagion'),
   ('外部融资视角','外部融资收紧加剧区域脆弱性','w-en-debt-crisis')],
 },
 'ghana-banking-2017':{
  'causal':[
   ('加纳银行业治理与资本不足等问题累积 → 2017年8月银行业危机开始','w-en-ghana-banking-crisis'),
   ('多家银行被处置/重组，危机持续至2020年1月','w-en-ghana-banking-crisis'),
   ('2020年新冠疫情期间抵达，进一步冲击经济','w-en-ghana-banking-crisis')],
  'schools':[
   ('银行治理/资本视角','治理失效与资本不足导致银行危机','w-en-ghana-banking-crisis'),
   ('外部冲击视角','疫情叠加放大经济困境','w-en-financial-crisis')],
 },
}
for eid,spec in SPEC.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基原文归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['pending_notes']=d.get('pending_notes','')+' 【轮次25】causal_chain/schools案例化（据本地维基语料）。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'案例化(level',d['level'],') causal',len(d['causal_chain']),'schools',len(d['schools']))
