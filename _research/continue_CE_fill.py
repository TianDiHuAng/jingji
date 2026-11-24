# -*- coding: utf-8 -*-
"""续作CE：为6条案例补timeline、5条概念扩写overview。"""
import json

TL = {
 'angola-oil-dependence': [
   {'year':2002,'display':'2002年','event':'内战结束后经济重建，石油驱动高速增长','sources':['w-en-angola-econ']},
   {'year':2010,'display':'2001—2010年','event':'年均GDP增速报告值11.1%','sources':['w-en-angola-econ']},
   {'year':2012,'display':'2012年','event':'贸易顺差约480亿美元','sources':['w-en-angola-econ']},
   {'year':2017,'display':'2017年','event':'石油占出口价值90%以上','sources':['w-en-angola-econ']},
   {'year':2022,'display':'2022年','event':'贸易顺差降至约300亿美元','sources':['w-en-angola-econ']},
 ],
 'bankruptcy-ftx': [
   {'year':2022,'display':'2022年11月','event':'客户提款激增暴露约80亿美元账目窟窿','sources':['w-en-bankruptcy-of-ftx']},
   {'year':2022,'display':'2022年11月11日','event':'FTX 申请破产保护（通说；具体日期待核实）','sources':['w-en-bankruptcy-of-ftx']},
   {'year':2023,'display':'2023年','event':'创始人 Bankman-Fried 被定罪（细节待核实）','sources':['w-en-bankruptcy-of-ftx']},
 ],
 'nigeria-debt': [
   {'year':2016,'display':'2014—2016年','event':'油价下跌冲击财政与汇率（结构性脆弱显现）','sources':['w-en-nigeria-econ']},
   {'year':2021,'display':'2021年','event':'债务/GDP 36.63%（IMF口径）','sources':['w-en-nigeria-econ']},
 ],
 'railway-mania': [
   {'year':1845,'display':'1840年代中期','event':'英国铁路狂热：股份可以10%定金认购','sources':['w-en-railway-mania']},
   {'year':1847,'display':'1847年','event':'泡沫破裂引发商业与银行震荡（见 panic-1847）','sources':['w-en-panic-of-1847']},
 ],
 'recession-1920-1921': [
   {'year':1920,'display':'1920年1月','event':'衰退开始（NBER测定）','sources':['w-en-recession-1920-1921']},
   {'year':1921,'display':'1921年7月','event':'衰退结束，持续18个月','sources':['w-en-recession-1920-1921']},
 ],
 'southafrica-debt': [
   {'year':2020,'display':'2019/20年度','event':'约90%国债以南非兰特计价；9月外债约1570亿美元','sources':['w-en-southafrica-debt']},
   {'year':2021,'display':'2021年12月','event':'外资持有国内债券份额28.2%，降至十年低点','sources':['w-en-southafrica-debt']},
   {'year':2025,'display':'2025/26年度','event':'政府债务R6.09万亿（US$412.04bn），债务/GDP 77.4%','sources':['w-en-southafrica-debt']},
 ],
}

for eid, tl in TL.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    d['timeline'] = sorted(tl, key=lambda t: t.get('year', 0))
    d['pending_notes'] = (d.get('pending_notes','') + ' 【续作CE】补齐时间线。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补timeline', eid, len(tl))

# 概念 overview 扩写
OV = {
 'credit-crunch': ('信贷紧缩指银行因资本充足率下降、不良资产上升或对未来不确定性加剧而**急剧收缩信贷供给**的现象。'
   '其关键特征是：紧缩源于**供给端**（银行不愿或不能放贷），而非借款需求下降。'
   '传导机制包括：资本受损失挤压→去杠杆→出售资产→价格下跌→资本进一步受损（"金融加速器"）；'
   '以及银行间市场信任崩塌导致批发性融资枯竭。'
   '信贷紧缩使企业投资与家庭消费受限，把金融冲击放大为实体经济的深度下滑——'
   '1930—1933年美国货币供给收缩近30%即为极端案例。'
   '政策应对包括降息、量化宽松、资本注入与信贷便利工具。具体机制与度量待核实。'),
 'debt-crisis': ('债务危机指债务累积超出偿付能力、在冲击下暴露违约风险而引发的危机，'
   '可发生于**主权、银行、企业或家庭**部门，也可跨部门叠加（如"银行-主权循环"）。'
   '共同机制是：杠杆上升→冲击使收入或资产价值下降→偿付能力恶化→再融资困难→'
   '被迫抛售或违约→价格进一步下跌（费雪的"债务通缩"）。'
   '典型形态包括：主权债务危机（拉美1980s、欧债2010s）、外债危机（货币错配的"原罪"）、'
   '以及家庭部门去杠杆（2008年后的美国）。'
   '化解路径通常为紧缩、重组（延期/减记）、通胀稀释或外部救助，各自伴随不同的分配后果。具体分类与案例待核实。'),
 'sovereign-default': ('主权违约指政府无法或不愿履行债务偿付义务，可表现为**拒付、重组（延期或减记）或贬值偿还**。'
   '与私人债务的关键区别是：主权债缺乏超国家强制执行机制——债权人无法扣押国家资产，'
   '只能通过市场准入、贸易与法律管辖等渠道施压。'
   '这带来"抵赖成本"与"履约意愿"的核心张力（Eaton-Gersovitz 传统）：'
   '违约可缓解当期负担，但会推高未来借款成本并可能触发挤兑与贸易制裁。'
   '历史上主权违约并不罕见（拉美1980s、俄罗斯1998、阿根廷2001、希腊2012）；'
   '据记载最大主权违约为2012年3月的希腊（1380亿美元）。'
   '近年发展出集体行动条款(CACs)与"巴黎俱乐部"等多边重组机制。具体机制与史例待核实。'),
 'speculative-bubble': ('投机泡沫指资产价格因**投机性买盘与乐观预期**而远超其基本面价值、最终破裂回落的现象。'
   '成因涉及多重因素：信贷与流动性扩张、羊群行为与"更大的傻瓜"预期、'
   '新技术的真实叙事被过度外推、以及卖空受限与杠杆可得性。'
   '"泡沫"的定义本身存在争议——事后看价格确曾回落，但事前难以确认价格是否已脱离基本面；'
   '有效市场论者认为多数"泡沫"可由风险溢价与基本面解释。'
   '经典案例包括郁金香(1637)、南海与密西西比(1720)、1929、日本(1989)、互联网(2000)、次贷(2007)。'
   '识别方法（市盈率、房价收入比、信贷/GDP缺口）均有局限。具体论述待核实。'),
 'subprime-lending': ('次级贷款指面向**信用评分较低、还款能力较弱**借款人发放的贷款，通常利率更高、条件更严。'
   '2000年代美国次级房贷的扩张，叠加**证券化**（MBS、CDO）与批发融资，'
   '构成2007—2008年全球金融危机的核心链条：'
   '放贷机构因"发起—分销"(originate-to-distribute) 模式而丧失审慎动机，'
   '投资者依赖评级机构对复杂结构化产品的评级，'
    '最终房价下跌触发违约上升、结构化产品价值崩塌、「回购市场挤兑」与金融机构倒闭。'
   '该案例成为"信息不对称（柠檬市场）、激励扭曲与评级失灵"的教科书样本。具体数据待核实。'),
}
for eid, ov in OV.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    d['overview'] = ov
    d['pending_notes'] = (d.get('pending_notes','') + ' 【续作CE】扩写概述。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('扩写', eid, len(ov))
