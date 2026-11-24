# -*- coding: utf-8 -*-
"""续作CF：为「银行危机模板」10条定制因果链与学派观点，消除母版雷同。"""
import json

CAUSAL = {
 'argentina-crisis-2001': [
   ('1991年"可兑换计划"锁定1:1汇率 → 竞争力流失、经常账户与财政赤字累积', 'w-en-argentine-economic-crisis'),
   ('外部融资中断 → 资本外逃与银行挤兑，2001年末存款被限制提取（"Corralito"）', 'w-en-financial-crisis'),
   ('主权违约 + 放弃钉住 → 比索大幅贬值，产出崩溃后于2003年起强劲反弹', 'w-en-argentine-economic-crisis'),
 ],
 'crisis-1914': [
   ('一战爆发使国际债权债务面临清算 → 约30亿美元外国组合投资被抛售', 'w-en-financial-crisis-1914'),
   ('金本位下汇率本应固定，英镑承压引发跨大西洋流动性紧张', 'w-en-financial-crisis-1914'),
   ('交易所关闭、债务延期偿付；英格兰银行贴现率三日内由3%升至10%', 'w-en-financial-crisis-1914'),
 ],
 'great-depression': [
   ('1929年10月股市崩盘 → 财富与信心受创，支出收缩', 'w-en-great-depression'),
   ('1930年秋起银行倒闭潮 → 存款收缩使货币供给至1933年下降近30%', 'fed-great-depression'),
   ('金本位约束下无法扩张 → 通缩与债务负担相互强化，1933年失业率达25%', 'w-en-great-depression'),
 ],
 'panic-1857': [
   ('铁路投资过热与1855年谷物高价（2.19美元/蒲式耳）推动信贷扩张', 'w-en-panic-of-1857'),
   ('俄亥俄人寿保险信托倒闭（负债700万美元）→ 铁路债券与银行信用受疑', 'w-en-panic-of-1857'),
   ('信用收缩跨大西洋传导 → 1858年谷物跌至0.80美元，地价崩跌（1000→10美元）', 'w-en-panic-of-1857'),
 ],
 'panic-1873': [
   ('1850年后罗斯柴尔德与巴林两家发行全球70%债券 → 铁路与主权融资高度集中', 'w-en-panic-of-1873'),
   ('Jay Cooke & Co. 等承销商倒闭 → 铁路债券违约与交易所停市（具体细节待核实）', 'w-en-panic-of-1873'),
   ('英格兰银行加息至9% → 长期萧条；英国净资本形成率11.5%→6.0%，德国反向升至15.9%', 'w-en-panic-of-1873'),
 ],
 'panic-1907': [
   ('1906年起股市持续下挫（1—7月-18%，前九个月-24.4%）→ 抵押品价值缩水', 'w-en-panic-of-1907'),
   ('10月14日联合铜业逼空失败（$39→$52后崩）→ 信托公司遭挤兑', 'w-en-panic-of-1907'),
   ('摩根等人组织私人救市；缺乏最后贷款人成为1913年美联储创设的直接动因', 'w-en-panic-of-1907'),
 ],
 'savings-loan-1986': [
   ('利率自由化后储贷机构以短期高息负债支持长期固定利率房贷 → 期限与利率错配', 'fed-savings-loan'),
   ('监管放松与存款保险下的道德风险 → 1982—1985年资产增长56%（银行24%的两倍）', 'fed-savings-loan'),
   ('地产价格下跌致大面积 insolvency → 关闭1043家（资产5190亿），纳税人成本1238亿', 'w-en-savings-and-loan-crisis'),
 ],
 'subprime-crisis-2007': [
   ('低利率与"发起—分销"模式 → 次级按揭扩张并证券化为MBS/CDO', 'w-en-subprime-mortgage-crisis'),
   ('2006—2007年房价见顶 → 违约上升、结构化产品评级下调、减值连锁', 'w-en-subprime-mortgage-crisis'),
   ('批发融资（回购）挤兑 → 2008年9月雷曼破产，危机全球化', 'w-en-financial-crisis'),
 ],
 'deposit-insurance': [
   ('部分准备金制度下，"先到先得"使挤兑成为自我实现的均衡（Diamond-Dybvig）', 'w-en-bank-run'),
   ('存款保险承诺覆盖限额内存款 → 消除个体挤兑动机', 'w-en-deposit-insurance'),
   ('代价是道德风险 → 需以资本监管与风险差别费率对冲', 'w-en-deposit-insurance'),
 ],
 'lender-of-last-resort': [
   ('系统性冲击下，有偿付能力的机构也面临挤兑与资产贱卖的流动性风险', 'w-en-lender-of-last-resort'),
   ('央行以良好抵押品为担保、按惩罚性利率自由放贷（白芝浩原则）', 'w-en-lender-of-last-resort'),
   ('阻止健康的机构被流动性问题拖垮，但须区分"流动性不足"与"无偿付能力"', 'w-en-lender-of-last-resort'),
 ],
}

SCHOOLS = {
 'argentina-crisis-2001': [
   {'holder':'汇率制度视角','view':'货币局制度在竞争力持续流失下不可维持，退出必然伴随挤兑与违约','basis':'据危机时序归纳；具体因果待核实','sources':['w-en-argentine-economic-crisis']},
   {'holder':'债务重组视角','view':'大规模减记虽带来短期剧痛，却是恢复增长的必经步骤','basis':'据危机后复苏数据归纳；因果待核实','sources':['w-en-argentine-economic-crisis']},
 ],
 'crisis-1914': [
   {'holder':'全球化脆弱性视角','view':'高度一体化的资本流动在战争冲击下反而放大了清算压力','basis':'据事件规模归纳','sources':['w-en-financial-crisis-1914']},
   {'holder':'最后贷款人视角','view':'贴现率的急剧上调与交易所关闭是防止黄金外流的必要手段','basis':'据政策操作归纳；效果评价待核实','sources':['w-en-financial-crisis-1914']},
 ],
 'great-depression': [
   {'holder':'货币主义解释','view':'美联储未能阻止货币供给收缩，把普通衰退变成了大萧条','basis':'据美联储历史与货币数据归纳；学界仍有争论','sources':['fed-great-depression']},
   {'holder':'金本位解释','view':'坚持金本位束缚了货币政策，越早退出的国家复苏越快','basis':'据各国退出时点与复苏对比归纳；因果待核实','sources':['w-en-gold-standard']},
 ],
 'panic-1857': [
   {'holder':'铁路投资周期视角','view':'基础设施投资的过度扩张是危机根源','basis':'据铁路债券与农产品价格数据归纳','sources':['w-en-panic-of-1857']},
   {'holder':'全球传导视角','view':'电报与蒸汽船使危机首次实现跨大西洋同步传导','basis':'据危机波及范围归纳；具体机制待核实','sources':['w-en-panic-of-1857']},
 ],
 'panic-1873': [
   {'holder':'长期萧条视角','view':'1873年后是长达二十余年的价格与增长低迷期','basis':'据资本形成与产出数据归纳；学界对"长期萧条"定性有争论','sources':['w-en-panic-of-1873']},
   {'holder':'国别分化视角','view':'同一冲击下英国资本形成率下降而德国上升，说明产业结构决定后果','basis':'据两国比率对比归纳','sources':['w-en-panic-of-1873']},
 ],
 'panic-1907': [
   {'holder':'制度缺失视角','view':'缺乏最后贷款人使局部逼空升级为系统性恐慌','basis':'据事件与美联储创设史归纳','sources':['w-en-panic-of-1907']},
   {'holder':'私人救助视角','view':'摩根等人的私人协调在短期内替代了公共机构','basis':'据救市过程归纳；规模与效果待核实','sources':['w-en-panic-of-1907']},
 ],
 'savings-loan-1986': [
   {'holder':'监管失灵视角','view':'存款保险+放松管制+宽限会计处理共同制造了道德风险','basis':'据美联储历史与行业数据归纳','sources':['fed-savings-loan']},
   {'holder':'利率风险视角','view':'核心问题是期限错配，而非单纯的欺诈与投机','basis':'据资产负债结构变化归纳','sources':['w-en-savings-and-loan-crisis']},
 ],
 'subprime-crisis-2007': [
   {'holder':'证券化链条视角','view':'"发起—分销"使放贷者丧失审慎动机，风险被评级与模型掩盖','basis':'据危机机制归纳；具体份额待核实','sources':['w-en-subprime-mortgage-crisis']},
   {'holder':'资产负债表视角','view':'批发融资的挤兑（回购市场）是危机从次级债扩散为系统性危机的关键','basis':'据2008年机构倒闭过程归纳','sources':['w-en-financial-crisis']},
 ],
 'deposit-insurance': [
   {'holder':'消除挤兑视角','view':'限额保险即可消除协调失败，无需覆盖全部存款','basis':'据Diamond-Dybvig框架归纳','sources':['w-en-bank-run']},
   {'holder':'道德风险视角','view':'保险削弱市场约束，需监管与差别费率配套','basis':'据制度设计争论归纳','sources':['w-en-deposit-insurance']},
 ],
 'lender-of-last-resort': [
   {'holder':'白芝浩原则','view':'自由放贷、惩罚性利率、良好抵押品，且只针对市场整体','basis':'据《伦巴第街》传统归纳','sources':['w-en-lender-of-last-resort']},
   {'holder':'边界模糊视角','view':'流动性不足与无偿付能力在危机中难以区分，实践中救助范围不断扩大','basis':'据2008/2023年案例归纳；争议待核实','sources':['w-en-lender-of-last-resort']},
 ],
}

n=0
for eid, chain in CAUSAL.items():
    f='data/entries/'+eid+'.json'
    d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':s,'sources':[src]} for s,src in chain]
    if eid in SCHOOLS:
        d['schools']=SCHOOLS[eid]
    d['pending_notes']=d.get('pending_notes','')+' 【续作CF】因果链与学派观点已按本条目史实定制，替换通用母版。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    n+=1
    print('定制',eid)
print('共',n,'条')
