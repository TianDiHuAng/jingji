# -*- coding: utf-8 -*-
"""轮次19 DEEPEN-SEMANTIC：把5条L2条目的通用模板 schools/causal_chain 改写为案例专属（据本地维基语料，不编造）。"""
import json
SPEC={
 'shanghai-rubber-1910':{
  'causal':[
   ('20世纪初汽车与橡胶需求激增(美橡胶出口1908年5700万美元→1909年7000万美元)→橡胶股受追捧','w-en-shanghai-rubber-stock-market-crisis'),
   ('外资银行推出橡胶股票的证券贷款便利 → 投机与股价自我强化','w-en-shanghai-rubber-stock-market-crisis'),
   ('泡沫破裂 → 天津、广州等地大量华资银行倒闭，上海市场受重创','w-en-shanghai-rubber-stock-market-crisis')],
  'schools':[
   ('基本面驱动视角','橡胶需求当时确有真实增长，股价上涨有基本面因素','w-en-shanghai-rubber-stock-market-crisis'),
   ('投机过度视角','银行与股东过度炒作橡胶股、提供证券贷款便利，吹大泡沫','w-en-shanghai-rubber-stock-market-crisis')],
 },
 'souk-al-manakh-1982':{
  'causal':[
   ('1970年代石油收入使私人积聚大量资金 → 70年代中期官方股市投机热潮(1977崩盘)','w-en-souk-al-manakh-stock-market-crash'),
   ('政府对1977崩盘的救助与加强监管 → 最激进的投机者被挤向非法的平行市场 Souk Al-Manakh','w-en-souk-al-manakh-stock-market-crash'),
   ('该市场市值一度全球第三；1982年8月因一张远期支票被拒付而崩盘','w-en-souk-al-manakh-stock-market-crash')],
  'schools':[
   ('监管套利/道德风险视角','政府救助与监管将风险偏好最高的投机者推入不受监管的平行市场，反而酿成更大崩盘','w-en-souk-al-manakh-stock-market-crash'),
   ('过度投机视角','远期支票(postdated check)等杠杆工具助长投机，最终因兑付失败崩塌','w-en-souk-al-manakh-stock-market-crash')],
 },
 'mini-crash-1997':{
  'causal':[
   ('1997亚洲金融危机(亚洲传染)→ 香港恒生指数隔夜跌6%','w-en-october-27-1997-mini-crash'),
   ('跌势蔓延至欧洲(伦敦FTSE -2%)与美国市场','w-en-october-27-1997-mini-crash'),
   ('道指单日大跌(史上第18大单日百分比跌幅)，被视为1990年代繁荣见顶的开端信号','w-en-october-27-1997-mini-crash')],
  'schools':[
   ('传染视角','由亚洲危机经金融传染跨市场传导至欧美','w-en-october-27-1997-mini-crash'),
   ('情绪/估值视角','视为美国长期牛市见顶的早期信号，信心与增长随后放缓','w-en-october-27-1997-mini-crash')],
 },
 'cypriot-2013':{
  'causal':[
   ('塞浦路斯银行对过度杠杆的本地地产公司及希腊主权债务的敞口 → 评级被下调至垃圾级','w-en-cypriot-2013'),
   ('无法从国际市场融资、政府不愿重组问题银行 → 危机深化','w-en-cypriot-2013'),
   ('2013年3月欧元集团等提供100亿欧元救助，代价是关闭第二大银行、对未保险存款征一次税','w-en-cypriot-2013')],
  'schools':[
   ('主权-银行关联视角','银行大量持有本国与希腊主权债，主权风险与银行风险相互放大','w-en-cypriot-2013'),
   ('银行挤兑/救助视角','救助附带存款减记(bail-in)引发对存款安全的担忧','w-en-cypriot-2013')],
 },
 'icelandic-crisis-2008':{
  'causal':[
   ('三大银行(Kaupthing/Landsbanki/Glitnir)借国际货币市场信贷急剧扩张','w-en-icelandic-crisis-2008'),
   ('2008年危机中外债达9.553万亿克朗(约500亿欧元)、超GDP 7倍；三行资产超GDP 11倍 → 融资与挤兑压力','w-en-icelandic-crisis-2008'),
   ('2008年末三大私有商业银行全部违约 → 严重衰退与2009年抗议','w-en-icelandic-crisis-2008')],
  'schools':[
   ('银行规模/杠杆视角','银行体系相对经济体量过大(资产超GDP 11倍)，短期外债依赖度高','w-en-icelandic-crisis-2008'),
   ('挤兑/传染视角','荷兰、英国的存款挤兑与市场信心消退触发再融资失败','w-en-icelandic-crisis-2008')],
 },
}
for eid,spec in SPEC.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基原文归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['pending_notes']=d.get('pending_notes','')+' 【轮次19】causal_chain/schools已案例化（据本地维基语料），非通用模板。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'案例化完成 causal',len(d['causal_chain']),'schools',len(d['schools']))
