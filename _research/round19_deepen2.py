# -*- coding: utf-8 -*-
"""轮次19 DEEPEN-SEMANTIC 第二批：5条L2案例化（据本地维基语料）。"""
import json
SPEC={
 'chinese-stock-bubble-2007':{
  'causal':[
   ('市场传言中国当局将加息抑通胀、打击借贷投机 → 上证综指单日暴跌9%(10年最大)','w-en-chinese-stock-bubble-of-2007'),
   ('跌势经亚洲市场传导至全球(道指单日跌416点/3.29%，标普-3.47%)','w-en-chinese-stock-bubble-of-2007'),
   ('上证综指2007年10月见顶6092点，随后2007-11至2008-11大幅下跌','w-en-chinese-stock-bubble-of-2007')],
  'schools':[
   ('政策预期触发视角','加息与打击借贷投机的预期直接触发了暴跌','w-en-chinese-stock-bubble-of-2007'),
   ('全球传染视角','中国市场暴跌经亚洲传导引发全球市场连锁反应','w-en-chinese-stock-bubble-of-2007')],
 },
 'showa-crisis-1927':{
  'causal':[
   ('一战后日本企业过度扩张产能形成泡沫；1920年放缓+1923关东大地震 → 经济萧条、企业倒闭','w-en-sh-wa-financial-crisis'),
   ('政府经日本银行发放"地震债券"救济过度扩张的银行；1927年1月提议兑付债券 → 银行破产谣言','w-en-sh-wa-financial-crisis'),
   ('挤兑致37家银行(含台湾银行)与铃木商店倒闭；若槻礼次郎内阁倒台，财阀势力上升','w-en-sh-wa-financial-crisis')],
  'schools':[
   ('货币与地震债券视角','震后救济债券的兑付传闻引爆银行偿付能力疑虑','w-en-sh-wa-financial-crisis'),
   ('结构/财阀视角','危机加速了五大财阀对日本银行业的支配','w-en-sh-wa-financial-crisis')],
 },
 'baring-crisis-1890':{
  'causal':[
   ('巴林银行对阿根廷主权债务过度敞口 → 1890年11月濒临破产','w-en-baring-crisis'),
   ('阿根廷违约风险与巴林困境波及全球，美国出现急剧衰退','w-en-baring-crisis'),
   ('(英格兰银行牵头组织担保/救助)避免巴林倒闭——19世纪最著名的主权债务危机','w-en-baring-crisis')],
  'schools':[
   ('主权债务视角','核心是主权债务敞口过大导致的银行危殆','w-en-baring-crisis'),
   ('最后贷款人视角','以集体担保避免系统性扩散，凸显央行协调作用','w-en-baring-crisis')],
 },
 'panic-1819':{
  'causal':[
   ('拿破仑战争后全球市场调整 + 银行与商业机构滥发纸币 → 公共土地过度投机','w-en-panic-of-1819'),
   ('第二美国银行(SBUS)深陷扩张，1818年收紧信贷、拒收州银行纸币','w-en-panic-of-1819'),
   ('1819年1月棉花价格单日跌25% → 恐慌引发衰退，持续至1821年','w-en-panic-of-1819')],
  'schools':[
   ('货币扩张视角','纸币滥发与信贷无序扩张放大了投机','w-en-panic-of-1819'),
   ('战后调整视角','拿破仑战争后的全球市场正常化是深层诱因','w-en-panic-of-1819')],
 },
 'indian-1991':{
  'causal':[
   ('十年大额财政赤字与外部借款累积 → 海湾战争油价上涨、政治不稳使预算难产、投资者信心流失','w-en-indian-1991'),
   ('1990-91外汇储备降至仅够三周进口 → 危机爆发','w-en-indian-1991'),
   ('向IMF借款、质押黄金获外国银行贷款以避免违约；1991年6月卢比大幅贬值','w-en-indian-1991')],
  'schools':[
   ('国际收支视角','核心是长期财政赤字与外部失衡导致的外汇枯竭','w-en-indian-1991'),
   ('外部冲击视角','海湾战争油价与政治不稳是直接触发','w-en-indian-1991')],
 },
}
for eid,spec in SPEC.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基原文归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['pending_notes']=d.get('pending_notes','')+' 【轮次19】causal_chain/schools已案例化（据本地维基语料）。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'案例化 causal',len(d['causal_chain']),'schools',len(d['schools']))
