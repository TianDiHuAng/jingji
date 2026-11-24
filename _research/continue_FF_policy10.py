# -*- coding: utf-8 -*-
"""续作FF：第三批补写10条案例政策应对（人工核验撰写）。"""
import json
import os

POL = {
 'shanghai-rubber-1910': (
   '**地方政府救援（借款维持市面）**：1910年7月21日正元、兆康、谦余三家华资银行倒闭，随后五家停业。'
   '上海道台蔡乃煌与上海商会主席周金箴赴宁波，向两江总督张人骏、江苏巡抚程德全报告，'
   '张再上报中枢。**7月27日清廷批准向外国银行借款**；'
   '**8月4日**蔡乃煌与 **9 家外国银行**签订"维持上海市面借款"合约，'
   '由上海政府借入 **350 万两**。',
   '据 Wikipedia「Shanghai rubber stock market crisis」相关章节；'
   '政策主体：清政府/上海道台；动作：批准并签订对外借款以维持市面'),

 'smithsonian-agreement': (
   '**史密森协议（1971年12月）**：各国货币对美元设定约 **2.25% 的交易区间**；'
   '各方同意以**特别提款权(SDR)** 平衡世界金融体系的方案；'
   '美国**取消进口附加税**。'
   '但黄金市场的美元价格持续对官方汇率施压——'
   '**1973年2月14日**美元再贬值 **10%** 后，日本与欧洲经济合作组织国家转向**浮动汇率**，'
   '此后十年间多数工业化国家相继浮动。',
   '据 Wikipedia「Smithsonian Agreement」相关章节；'
   '政策主体：十国集团/美国；动作：汇率重估与区间设定、取消进口附加税'),

 'silicon-valley-bank': (
   '**官方表态**：2023年3月11日拜登与加州州长纽森讨论该行倒闭；'
   '**3月13日**开市前发表电视讲话，表达对银行体系韧性的信心，'
   '承诺政府将确保存款可用、但**不以纳税人资金奖励投资者**，'
   '并承诺**追究银行高管责任**、推动相关规则改革。'
   '**争论**：包括 Garry Tan、David Sacks 在内的 **599 名风险投资人**'
   '与对冲基金经理 Bill Ackman 等呼吁政府干预以保护未保险存款人；'
   '部分国会议员主张让存款人全额受偿，另一些则持相反立场。'
   '（正文同时记录了 FDIC 的接管与存款保险处置。）',
   '据 Wikipedia「Silicon Valley Bank」Official responses 与 Debate over government intervention 章节；'
   '政策主体：总统/FDIC/国会；动作：承诺存款可用、追究高管责任、公开争论'),

 'spain-2008': (
   '**2012年银行纾困**：**2012年6月9日**欧元集团召开紧急会议讨论向西班牙银行业注资；'
   'IMF 估计西班牙银行的资本需求约为 **400 亿欧元**；'
   '欧元集团宣布拟向西班牙政府的"有序银行重组基金"(FROB) 提供**最多 1000 亿欧元**，'
   '再由西班牙政府按需拨付给银行。',
   '据 Wikipedia 相关条目 2012 financial bailout 章节；'
   '政策主体：欧元集团/西班牙政府；动作：向 FROB 提供最高1000亿欧元纾困额度'),

 'turkey-2001': (
   '**稳定化努力**：**2000年11月** IMF 向土耳其提供 **114 亿美元**贷款；'
   '土耳其并出售大量国有企业以平衡预算——'
   '例如土耳其航空在报纸上刊登广告，为其 **51% 股权**征集报价。'
   '到 2000 年，土耳其已出现大规模失业、药品短缺、信贷紧缩、'
   '为对抗通胀而压低生产以及税负上升。',
   '据 Wikipedia「2001 Turkish economic crisis」Stabilization efforts 章节；'
   '政策主体：土耳其政府/IMF；动作：IMF贷款、国企私有化'),

 'yugoslav-hyper-1992': (
   '**稳定化方案的三次尝试**：南斯拉夫社会主义联邦共和国时期的恶性通胀以**非正统稳定方案**治理；'
   '南斯拉夫联盟共和国(FRY) 成立后改行**正统方案**。'
   '两者在短期都相对成功、但在长期均告失败并导致方案崩溃。'
   '**1994年初**又推出"货币重建计划"(Monetary Reconstruction Program)。',
   '据 Wikipedia 相关条目 Stabilization program 章节；'
   '政策主体：南斯拉夫当局；动作：非正统/正统稳定方案、货币重建计划'),

 'worldcom': (
   '**立法反应**：《萨班斯-奥克斯利法》正是在包括世通与安然在内的多起商业丑闻之后通过的。'
   '世通更名为 MCI，于 **2006年1月**被 Verizon Communications 收购。',
   '据 Wikipedia「WorldCom」Aftermath 章节；'
   '政策主体：美国国会；动作：通过萨班斯-奥克斯利法（会计与审计监管改革）'),

 'swedish-crisis-1990s': (
   '**救助与处置并行（含同期芬兰经验）**：正文记载，'
   '1992年为稳定金融部门、防止信贷紧缩，政府向银行提供 **71 亿马克卡（约 12 亿欧元）**'
   '的初始零息可转换贷款，多数银行（SKOP 除外）其后偿还；'
   '并设立国有的**政府担保基金**(Valtion vakuusrahasto) 支持储蓄银行。'
   '瑞典方面的应对见本条目概述：Nordbanken 与 Götabanken 获财政支持并被国有化，'
   '成本达 **640 亿克朗**。',
   '据 Wikipedia 相关条目 Government intervention and aftermath 章节（该段为芬兰经验）'
   '及本条目概述（瑞典数据）；政策主体：瑞典/芬兰政府；动作：可转换贷款、担保基金、国有化'),

 'defi': (
   '**监管纳入**：**2021年10月**，金融行动特别工作组(FATF) 将 DeFi 纳入针对加密服务提供者的指引，'
   '意在对此类资产实施监管；FATF 期待各国自行判定 DeFi 的参与者是否可被视为虚拟资产提供者，'
   '从而适用相关义务。',
   '据 Wikipedia「Decentralized finance」Regulation 章节；'
   '政策主体：FATF/各国监管机构；动作：将DeFi纳入反洗钱指引范围'),

 'gamestop-2021': (
   '**监管指引**：**2021年2月8日**，美国证券交易委员会(SEC) 发布一份**样本函**，'
   '为在"极端价格波动"期间寻求融资的公司提供指引——'
   '要求公司在信息披露中列明相关风险，并鼓励其……（具体建议内容待核实）。',
   '据 Wikipedia「GameStop short squeeze」Regulation 章节；'
   '政策主体：SEC；动作：发布披露指引样本函'),
}

n = 0
for eid, (view, basis) in POL.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if d.get('policy_response'):
        print('已有', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
                             'basis': basis + '；效果评价待核实',
                             'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FF】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1

import glob
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('补写 %d 条 | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
