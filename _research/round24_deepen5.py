# -*- coding: utf-8 -*-
"""轮次24 DEEPEN-SEMANTIC 第五批：5条L2案例化（据本地维基语料）。"""
import json
SPEC={
 'black-wednesday-1992':{
  'causal':[
   ('英国加入欧洲汇率机制(ERM)后，英镑需维持在规定下限之上；投机压力下难以维持','w-en-black-wednesday'),
   ('1992年9月16日英国在保卫汇率失败后，被迫让英镑退出ERM（"黑色星期三"）','w-en-black-wednesday'),
   ('当日英镑遭大规模抛售，英国央行干预未能奏效','w-en-black-wednesday')],
  'schools':[
   ('固定汇率/不可能三角视角','在资本自由流动下维持固定汇率与独立货币政策不可兼得','w-en-currency-crisis'),
   ('投机攻击视角','对冲基金等对高估汇率发动投机攻击，耗尽央行储备','w-en-black-wednesday')],
 },
 'australian-banking-1893':{
  'causal':[
   ('1880年代澳大利亚房地产投机繁荣(受商业银行助长) → 资产泡沫与过度放贷','w-en-australian-banking-crisis-of-1893'),
   ('泡沫破裂 → 大量商业银行与建房社团倒闭、普遍经济萧条','w-en-australian-banking-crisis-of-1893'),
   ('与美国1893年恐慌同期发生，相互叠加','w-en-australian-banking-crisis-of-1893')],
  'schools':[
   ('房地产泡沫视角','1880年代地产投机与银行过度放贷是根源','w-en-australian-banking-crisis-of-1893'),
   ('银行挤兑视角','银行连锁倒闭放大萧条','w-en-australian-banking-crisis-of-1893')],
 },
 'irish-banking-2008':{
  'causal':[
   ('房地产繁荣与银行过度扩张后，2008年全球危机中爱尔兰多家金融机构因资不抵债濒临崩溃','w-en-post-2008-irish-banking-crisis'),
   ('爱尔兰政府实施约640亿欧元银行救助','w-en-post-2008-irish-banking-crisis'),
   ('救助叠加国内衰退，酿成"世界史上最昂贵银行危机之一"(央行行长语)','w-en-post-2008-irish-banking-crisis')],
  'schools':[
   ('房地产泡沫/银行杠杆视角','地产繁荣与银行过度杠杆致资不抵债','w-en-post-2008-irish-banking-crisis'),
   ('主权-银行关联视角','政府大规模救助银行将银行风险转为主权负担','w-en-systemic-risk')],
 },
 'turkish-crisis-2018':{
  'causal':[
   ('土耳其长期经常账户赤字 + 大量私人外币计价债务 → 外部融资脆弱','w-en-turkish-economic-crisis'),
   ('里拉大幅贬值、通胀高企、借贷成本上升、贷款违约增加 → 危机','w-en-turkish-economic-crisis'),
   ('2023年起转向正统货币政策以遏制通胀','w-en-turkish-economic-crisis')],
  'schools':[
   ('国际收支/外债视角','经常账户赤字与外币债务使里拉易受冲击','w-en-turkish-economic-crisis'),
   ('政策/信心视角','非正统货币政策与地缘因素加剧资本外流','w-en-monetary-policy')],
 },
 'uruguay-2002':{
  'causal':[
   ('自1950年代以来高度美元化(对披索信心弱) → 经济对美元与外部冲击高度敏感','w-en-uruguay-2002'),
   ('本国经济收缩 + 对邻国阿根廷的过度依赖(阿根廷危机传染) → 2002年7月银行危机','w-en-uruguay-2002'),
   ('银行挤兑与储备流失，危机深化','w-en-uruguay-2002')],
  'schools':[
   ('美元化/外部脆弱视角','长期美元化使货币错配、抗冲击能力弱','w-en-uruguay-2002'),
   ('区域传染视角','阿根廷危机通过贸易与金融渠道传染乌拉圭','w-en-financial-contagion')],
 },
}
for eid,spec in SPEC.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基原文归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['pending_notes']=d.get('pending_notes','')+' 【轮次24】causal_chain/schools案例化（据本地维基语料）。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'案例化 causal',len(d['causal_chain']),'schools',len(d['schools']))
