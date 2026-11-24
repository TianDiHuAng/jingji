# -*- coding: utf-8 -*-
"""续作EV：为18个新建条目补 comparison 与 related。"""
import json

NEW = ['growth', 'recession', 'utility', 'market-failure', 'rent-seeking', 'expectations',
       'effective-demand', 'convergence', 'modigliani-miller', 'equity-premium',
       'counterparty-risk', 'fractional-reserve', 'subordination', 'proprietary-trading',
       'mutual-fund', 'nasdaq', 'eurodollar', 'dividend']

CMP = {
 'growth': ('与**发展**的区别在"量"与"结构"：增长指产出规模的扩大（可用人均实际GDP增长率度量），'
   '发展还包括结构转型、健康、教育与制度改善（见 development-economics）。'
   '与**商业周期**的区别在时间尺度：增长是长期趋势，周期是围绕趋势的短期波动。'
   '二者的混淆会导致政策误判——把周期的短期反弹当作增长提速，或把趋势放缓当作周期衰退。'),
 'recession': ('与**萧条**的区别在程度与持续性：衰退是产出与就业的显著下降，'
   '萧条是更严重、更持久的下滑（如大萧条、阿根廷1998—2002"大萧条"）。'
   '与**增长放缓**的区别在广度：衰退要求多个指标（产出、就业、收入、销售）**共同**下降，'
   '单一指标下滑不足以判定。这一区分很关键：'
   '"连续两季负增长"只是通俗标准，NBER 用多指标事后判定——'
   '因为仅看GDP会漏掉就业与收入的持续恶化。'),
 'utility': ('与**价值**的区别在"主观与客观"：效用是个人对某种状态的**主观满足**排序，'
   '价值（劳动价值论）被视为商品内在属性。'
   '与**福利**的区别在层次：效用是个体层面的度量，福利是社会层面的加总（需价值判断）。'
   '这一区分在危机政策中很实际：'
   '"救助银行提高了社会福利"这类主张，必须说明如何加权不同群体的效用——'
   '而这本身是规范判断，不是实证结论。'),
 'market-failure': ('与**政府失灵**的区别在"失灵主体"：市场失灵指自由市场配置未达帕累托效率'
   '（外部性、公共品、信息不对称、垄断、协调失败）；'
   '政府失灵指干预本身因激励扭曲（寻租、信息不足、政治周期）而未能改善（见 public-choice）。'
   '两者必须一起看：'
   '论证监管必要性时，只指出市场失灵不够，还须证明干预的收益大于政府失灵的成本——'
   '这是2008年后"监管改革"争论的核心框架。'),
 'rent-seeking': ('与**寻租**相近但需与**利润**区分：利润来自创造新价值（生产、创新、效率改进），'
   '寻租来自**重新分配**既有价值（游说关税、牌照限制、补贴争取）。'
   '与**腐败**的区别在合法性：寻租多通过**合法**的政治影响实现（游说、旋转门），'
   '腐败涉及非法交易。'
   '在金融危机中，寻租的典型形态是"太大而不能倒"带来的隐性补贴——'
   '机构通过规模获得保护，而非通过效率。'),
 'expectations': ('与**理性预期**的区别在"是否用尽信息"：'
   '一般意义上的预期是"对最可能发生之结果的信念"，可能符合也可能偏离现实；'
   '理性预期假设主体**用尽所有可得信息**（含政策规则）形成预期，'
   '因此不会系统性犯错。'
   '这一区分决定政策空间：'
   '若公众预期是适应性（外推过去），政策可短期"欺骗"公众；'
   '若是理性的，被预期的政策无效（政策无效性命题）。'),
 'effective-demand': ('与**名义需求**的区别在"是否受约束"：'
   '有效需求是购买者在**其他市场受到约束**时实际出现的需求；'
   '名义需求是只受价格与偏好约束、不受其他市场配给限制的需求。'
   '这一区分源自凯恩斯对"需求不足"的论证：'
   '当劳动市场或信贷市场存在配给时，家庭的支出计划无法实现，'
   '总需求低于潜在水平——因此扩张政策可提高产出而不只是推高物价。'),
 'convergence': ('与**分化**的区别在方向：收敛假说主张贫穷经济体人均收入增长更快、'
   '从而缩小与富国的差距；分化则是差距扩大（见 great-divergence）。'
   '需区分两种收敛：'
   '**绝对收敛**（所有经济体趋向同一水平）在现实中很少成立；'
   '**条件收敛**（各自趋向自身稳态）得到较多实证支持。'
   '这一区分解释了为何"开放就能追上"的简单主张失败——'
   '收敛取决于储蓄率、人力资本与制度等条件。'),
 'modigliani-miller': ('与**权衡理论**的区别在"是否考虑摩擦"：'
   'MM定理在无税收、无破产成本的理想世界中证明资本结构无关；'
   '权衡理论引入税盾收益与财务困境成本，得出"存在最优负债率"。'
   '与**优序融资理论**的区别在信息假设：'
   '后者从信息不对称出发，认为企业优先内部资金、其次债务、最后股权。'
   'MM定理的价值不在其假设的现实性，而在它**定义了必须引入哪些摩擦**才能解释现实。'),
 'equity-premium': ('与**风险溢价**的区别在"总量与谜题"：'
   '风险溢价是承担风险所要求的额外回报（一般概念）；'
   '股权溢价之谜是**特定的实证异常**——历史股权溢价远高于标准模型（基于风险厌恶系数）所能解释的水平。'
   '可能的解释包括：短视损失厌恶、罕见灾难风险、习惯形成、'
   '以及幸存者偏差（美国样本的特殊性）。'
   '该谜题的重要性在于：若模型无法解释风险定价，则资产价格中的"泡沫"判断就缺乏基准。'),
 'counterparty-risk': ('与**市场风险**的区别在"违约与价格"：'
   '对手方风险是交易对手不履约（不交割、不支付）的风险；'
   '市场风险是价格波动导致的损失。'
   '与**结算风险**的关系是"同义"（结算风险亦称交割风险或对手方风险），'
   '但严格说结算风险特指**时区错配**造成的本金暴露（Herstatt 风险）。'
   '这一风险在危机中会集中爆发：'
   '当一家机构违约，其所有对手方同时受损——'
   '这正是中央对手方(CCP)与净额结算存在的理由，也是它们成为系统重要性节点的原因。'),
 'fractional-reserve': ('与**全额准备金银行**的区别在"能否创造货币"：'
   '部分准备金制度下银行只保留存款的一小部分作准备、其余贷出，'
   '这个过程**创造了存款货币**（货币乘数）；'
   '全额准备金（狭义银行）要求准备金100%覆盖存款，银行不能创造货币。'
   '这一区分是货币理论的核心分歧：'
   '主张狭义银行者认为可消除挤兑与道德风险；'
   '反对者认为会消灭信贷中介功能、迫使融资转向影子银行。'
   '与之配套的制度是存款保险与最后贷款人——两者都是对挤兑风险的回应。'),
 'subordination': ('与**担保**的区别在"顺序与特定资产"：'
   '次级化决定同一发行人不同债务的**清偿顺序**（优先债先于次级债、次级债先于股权）；'
   '担保则以**特定资产**作为偿付来源。'
   '这一区分在 bail-in 设计中至关重要：'
   '处置时必须按法定顺序承担损失（先股东、再次级债、最后优先债与存款），'
   '否则会破坏市场纪律与定价基础——'
   '塞浦路斯2013年对超10万欧元存款的减记之所以争议巨大，正因它打破了既定的清偿顺序预期。'),
 'proprietary-trading': ('与**做市**的区别在"目的与客户"：'
   '自营交易以公司自有资金为自己获利；'
   '做市则是为客户提供流动性、赚取买卖价差（虽有库存风险，但目的是服务客户）。'
   '与**代客交易**的区别在风险归属：'
   '自营风险归公司，代客风险归客户。'
   '这一区分是沃尔克规则的核心：'
   '该规则禁止银行从事自营交易（因有存款保险与央行支持作后盾），'
   '但允许做市与承销——边界模糊正是执行困难的原因。'),
 'mutual-fund': ('与**对冲基金**的区别在监管与投资者：'
   '共同基金面向**公众**、受严格披露与流动性约束（每日可赎回）；'
   '对冲基金面向合格投资者、策略自由（做空、杠杆）、通常有锁定期。'
   '与**ETF**的区别在交易方式：'
   '共同基金按每日净值申赎，ETF 在交易所实时交易。'
   '这一差别在危机中放大风险：'
   '共同基金的"每日可赎回"承诺使其在极端行情下面临**被迫抛售**（2020年3月债券基金），'
   '而对冲基金的锁定期反而限制了挤兑。'),
 'nasdaq': ('与**纽交所**的区别在交易结构：'
   '纳斯达克的传统是**做市商报价驱动**（多个做市商竞争报价），电子化程度高、'
   '适合成长型与科技公司；'
   '纽交所传统上是指令驱动加专家制度，上市门槛与品牌溢价更高。'
   '这一结构差异在2000年互联网泡沫与2010年闪崩中都有体现：'
   '做市商退出会导致流动性瞬间消失。'
   '纳斯达克亦以"交易所自身是上市公司"闻名——'
   '这种双重身份使其治理与监管边界成为讨论对象。'),
 'eurodollar': ('与**离岸人民币**等离岸货币市场同属"境外本币"现象：'
   '欧洲美元是存放于美国境外的美元存款，'
   '不受美国国内准备金要求与存款保险约束（这是其最初的成本优势）。'
   '与**外汇储备**的区别在持有主体与目的：'
   '欧洲美元由银行体系持有并用于同业融资，'
   '外汇储备由央行持有用于干预与偿付。'
   '其系统性意义在于：'
   '欧洲美元市场是**无最后贷款人**的美元体系——'
   '2008年该市场冻结时，美联储不得不通过央行互换额度向全球提供美元。'),
 'dividend': ('与**股票回购**的区别在"分配形式"：'
   '股息是现金分配且通常稳定（向下调整有负面信号），'
   '回购是买入自家股票（减少股本、提升每股收益），更灵活但受股价影响。'
   '与**利息**的区别在"是否强制"：'
   '股息由董事会酌情决定（普通股），利息是合同义务（否则违约）。'
   '这一区分在危机中很重要：'
   '银行在受援期间常被限制分红与回购，'
   '目的正是防止资本外流——把"可自由裁量"的分配暂停，是保存资本最直接的手段。'),
}

REL = {
 'growth': ['development-economics', 'total-factor-productivity', 'solow-model', 'business-cycle'],
 'recession': ['business-cycle', 'output-gap', 'unemployment', 'great-depression'],
 'utility': ['welfare-economics', 'marginal-utility', 'behavioral-finance', 'public-choice'],
 'market-failure': ['externality', 'public-good', 'information-asymmetry', 'public-choice'],
 'rent-seeking': ['public-choice', 'regulatory-arbitrage', 'too-big-to-fail', 'political-economy'],
 'expectations': ['rational-expectations', 'adaptive-expectations', 'phillips-curve', 'lucas-critique'],
 'effective-demand': ['aggregate-demand', 'keynesian-economics', 'says-law', 'liquidity-trap'],
 'convergence': ['solow-model', 'development-economics', 'total-factor-productivity', 'great-divergence'],
 'modigliani-miller': ['capital-structure', 'leverage', 'capital-requirement', 'debt-overhang'],
 'equity-premium': ['risk-premium', 'equity-premium', 'volatility', 'behavioral-finance'],
 'counterparty-risk': ['settlement-risk', 'netting', 'central-counterparty', 'credit-risk'],
 'fractional-reserve': ['money-creation', 'money-multiplier', 'bank-run', 'deposit-insurance'],
 'subordination': ['bail-in', 'seniority', 'debt-restructuring', 'haircut-finance'],
 'proprietary-trading': ['volcker-rule', 'glass-steagall-1933', 'hedge-fund', 'too-big-to-fail'],
 'mutual-fund': ['hedge-fund', 'etf', 'pension-fund', 'fire-sale'],
 'nasdaq': ['stock-exchange', 'market-maker', 'dotcom-bubble-2000', 'circuit-breaker'],
 'eurodollar': ['foreign-exchange-reserves', 'money-market', 'swap', 'triffin-dilemma'],
 'dividend': ['stock', 'bond', 'capital-requirement', 'buyback'],
}

for eid in NEW:
    p = 'data/entries/%s.json' % eid
    import os
    if not os.path.exists(p):
        print('缺文件', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if CMP.get(eid):
        d['comparison'] = CMP[eid]
    if REL.get(eid):
        d['related'] = REL[eid]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作EV】已补comparison与related。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('已处理', len(NEW), '个条目')
