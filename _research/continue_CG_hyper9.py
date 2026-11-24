# -*- coding: utf-8 -*-
"""续作CG：为「恶性通胀模板」9条定制因果链与学派观点。"""
import json

CAUSAL = {
 'brazil-hyper-1980': [
   ('1980年代外债危机与财政赤字 → 以印钞与指数化（工资/价格/金融资产挂钩通胀）应对', 'w-en-hyperinflation-in-brazil'),
   ('指数化使通胀具备惯性 → 月通胀在1990年1—3月达71.9%、71.7%、81.3%', 'w-en-hyperinflation-in-brazil'),
   ('多次冻结与货币改革失效（1990年冻结约80%流动性）→ 1994年雷亚尔计划以财政调整+汇率锚终结', 'w-en-hyperinflation-in-brazil'),
 ],
 'chinese-hyper-1937': [
   ('全面抗战使财政支出激增（一度+33%），而控制区与税基萎缩 → 缺口靠发行纸币弥补', 'w-en-chinese-hyperinflation'),
   ('沿海与交通线失守导致物资短缺 → 1938年末进口价格上涨72%，1944年进口仅及1937年的6%', 'w-en-chinese-hyperinflation'),
   ('货币超发与供给短缺叠加 → 物价螺旋；1948年金圆券改革未能止住（细节待核实）', 'w-en-chinese-hyperinflation'),
 ],
 'hungarian-hyper-1945': [
   ('战后赔偿负担、生产设施破坏与财政赤字 → 以中央银行融资弥补', 'w-en-hungarian-pengo'),
   ('货币供给爆炸性扩张 → 价格约每15小时翻倍，pengő约4天内失去90%价值', 'w-en-hungarian-pengo'),
   ('1945年12月曾以75%资本税等手段抑制未果 → 1946年以福林(forint)改革收场', 'w-en-hungarian-pengo'),
 ],
 'soviet-hyper-1917': [
   ('内战与"战时共产主义"使工业产出崩溃（1920年远低于战前60.59亿金卢布）→ 税基瓦解', 'w-en-soviet-hyperinflation'),
   ('财政缺口全靠发行纸币 → 货币职能丧失（"唯一繁荣的产业是纸币生产"）', 'w-en-soviet-hyperinflation'),
   ('1921年转向新经济政策 → 1922—1924年以切尔文(chevronets)金本位货币稳定币值', 'w-en-soviet-hyperinflation'),
 ],
 'venezuela-crisis-2013': [
   ('油价下跌与石油产量下滑 → 财政与进口能力骤降', 'w-en-crisis-in-venezuela'),
   ('价格与外汇管制扭曲供给 + 赤字货币化 → 恶性通胀与基本物资短缺', 'w-en-hyperinflation-in-venezuela'),
   ('产出崩塌与公共服务失灵 → 大规模人口外流（2024年达770万）与社会指标恶化（2021年贫困率95%）', 'w-en-crisis-in-venezuela'),
 ],
 'venezuela-hyper-2016': [
   ('财政赤字以央行融资弥补 → 货币供给失控（2014年通胀69%→2018年约170万%）', 'w-en-hyperinflation-in-venezuela'),
   ('价格管制与外汇管制造成短缺与黑市汇率 → 通胀预期固化、本币职能丧失', 'w-en-hyperinflation-in-venezuela'),
   ('多次货币改革（删除零）未能恢复信心 → 事实上的部分美元化（细节待核实）', 'w-en-hyperinflation-in-venezuela'),
 ],
 'weimar-hyper-1921': [
   ('一战赔款负担 + 1923年法比占领鲁尔 → 政府以印钞支持消极抵抗与财政缺口', 'w-en-hyperinflation'),
   ('货币供给爆炸 + 马克预期崩塌 → 物价失控、储蓄被抹去', 'w-en-hyperinflation'),
   ('1923年末以地租马克(Rentenmark)改革稳定币值（具体细节待核实）', 'w-en-hyperinflation'),
 ],
 'yugoslav-hyper-1992': [
   ('南斯拉夫解体战争 + 国际制裁 → 产出崩溃与税收瓦解', 'w-en-yugoslav-hyperinflation'),
   ('赤字货币化 → 1994年1月月通胀达3.13亿%、日均62%、时均2.03%', 'w-en-yugoslav-hyperinflation'),
   ('持续22个月后以"阿夫拉莫维奇计划"稳定（史上第三严重恶性通胀）', 'w-en-yugoslav-hyperinflation'),
 ],
 'zimbabwe-hyper-2007': [
   ('土地改革后农业产出与外汇收入下滑 → 财政与进口能力恶化', 'w-en-hyperinflation-in-zimbabwe'),
   ('赤字以印钞弥补 → 2008年11月峰值月通胀约7906亿%（月环比）', 'w-en-hyperinflation-in-zimbabwe'),
   ('货币职能崩溃（100万亿面额不够一趟车费）→ 2009年转向美元化', 'w-en-hyperinflation-in-zimbabwe'),
 ],
}

SCHOOLS = {
 'brazil-hyper-1980': [
   {'holder':'惯性通胀视角','view':'指数化使通胀具备自我延续的惯性，需"冻结+财政调整"同时切断','basis':'据多次计划经验归纳','sources':['w-en-hyperinflation-in-brazil']},
   {'holder':'财政视角','view':'根本症结是财政赤字，货币改革只能争取时间','basis':'据雷亚尔计划设计归纳；因果待核实','sources':['w-en-hyperinflation-in-brazil']},
 ],
 'chinese-hyper-1937': [
   {'holder':'战争财政视角','view':'领土与税基丧失使赤字货币化成为唯一选择','basis':'据战时财政数据归纳','sources':['w-en-chinese-hyperinflation']},
   {'holder':'供给视角','view':'物资短缺（进口仅剩6%）与货币超发同等重要','basis':'据进口与物价数据归纳','sources':['w-en-chinese-hyperinflation']},
 ],
 'hungarian-hyper-1945': [
   {'holder':'货币主义视角','view':'史上最严重恶性通胀源于纯粹的赤字货币化','basis':'据Cagan传统归纳','sources':['w-en-hungarian-pengo']},
   {'holder':'战后赔偿视角','view':'赔款负担是外生约束，使财政调整空间极小','basis':'据战后赔款安排归纳；规模待核实','sources':['w-en-hungarian-pengo']},
 ],
 'soviet-hyper-1917': [
   {'holder':'战争共产主义视角','view':'产出崩溃+税基瓦解使印钞成为唯一财源','basis':'据工业产出数据归纳','sources':['w-en-soviet-hyperinflation']},
   {'holder':'制度转轨视角','view':'切尔文改革的关键是重建税收与预算约束，而非仅更换货币','basis':'据NEP与币改时序归纳','sources':['w-en-soviet-hyperinflation']},
 ],
 'venezuela-crisis-2013': [
   {'holder':'政策失当视角','view':'价格与外汇管制摧毁供给，赤字货币化摧毁货币','basis':'据危机过程归纳','sources':['w-en-crisis-in-venezuela']},
   {'holder':'石油依赖视角','view':'油价下行暴露了单一资源财政的结构性脆弱','basis':'据财政与出口结构归纳','sources':['w-en-crisis-in-venezuela']},
 ],
 'venezuela-hyper-2016': [
   {'holder':'财政主导视角','view':'央行融资是恶性通胀的直接机制','basis':'据通胀数据归纳；官方数据中断使验证困难','sources':['w-en-hyperinflation-in-venezuela']},
   {'holder':'数据可靠性视角','view':'官方统计长期中断，各方估算分歧极大（世行2016年254.9% vs 800%）','basis':'据两源并列结果归纳','sources':['owid-inflation']},
 ],
 'weimar-hyper-1921': [
   {'holder':'赔款-货币视角','view':'赔款与占领导致的赤字货币化是通胀根源','basis':'据Cagan的经典研究归纳','sources':['w-en-hyperinflation']},
   {'holder':'政治经济学视角','view':'通胀的分配后果削弱了对共和制度的支持','basis':'据历史叙述归纳；因果待核实','sources':['w-en-hyperinflation']},
 ],
 'yugoslav-hyper-1992': [
   {'holder':'战争财政视角','view':'战争与制裁使税收瓦解，印钞成为唯一融资方式','basis':'据危机过程归纳','sources':['w-en-yugoslav-hyperinflation']},
   {'holder':'稳定计划视角','view':'阿夫拉莫维奇计划以汇率锚+财政约束成功终结通胀','basis':'据稳定过程归纳；可持续性待核实','sources':['w-en-yugoslav-hyperinflation']},
 ],
 'zimbabwe-hyper-2007': [
   {'holder':'供给崩溃视角','view':'土地改革后农业与出口崩塌是通胀的起点','basis':'据经济结构变化归纳','sources':['w-en-hyperinflation-in-zimbabwe']},
   {'holder':'货币视角','view':'赤字货币化把冲击放大为恶性通胀；美元化是外部锚的替代方案','basis':'据2009年美元化经验归纳','sources':['w-en-hyperinflation-in-zimbabwe']},
 ],
}

for eid, chain in CAUSAL.items():
    f='data/entries/'+eid+'.json'
    d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':s,'sources':[src]} for s,src in chain]
    if eid in SCHOOLS:
        d['schools']=SCHOOLS[eid]
    d['pending_notes']=d.get('pending_notes','')+' 【续作CG】因果链与学派观点已按本条目史实定制。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('定制',eid)
