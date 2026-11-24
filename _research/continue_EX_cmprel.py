# -*- coding: utf-8 -*-
"""续作EX：为第二批15个条目补 comparison 与 related。"""
import json
import os

NEW = ['toxic-assets', 'junk-bond', 'payment-system', 'prisoners-dilemma', 'property-rights',
       'transaction-cost', 'savings', 'investment', 'demand', 'population', 'inequality',
       'labour-market', 'specialization', 'tax-incidence', 'buyback']

CMP = {
 'toxic-assets': ('与**不良贷款**的区别在"资产形态"：'
   '有毒资产多指已证券化、市场冻结、无法定价的资产（次级MBS、CDO）；'
   '不良贷款是银行账上逾期或减值的贷款。'
   '这一区分决定处置工具：'
   '不良贷款靠催收、核销或出售；'
   '有毒资产因缺乏市场价格，需要**坏账银行**(bad bank) 或担保定价（如美国TARP的"公私合营投资计划"）。'
   '定价难题是核心——价格过低则银行资不抵债，过高则纳税人承担损失。'),
 'junk-bond': ('与**投资级债券**的区别在信用评级：'
   '垃圾债评级低于投资级（标普BB+及以下），违约概率更高、利差更宽；'
   '投资级债券（BBB-及以上）违约率低。'
   '与**困境债务**(distressed debt) 的区别在"是否已接近违约"：'
   '垃圾债是"高风险但正常付息"，困境债是"已在违约边缘、折价交易"。'
   '这一区分在危机中很关键：'
   '垃圾债利差骤扩是信用周期转向的早期信号，而困境债市场的深度决定了重组的可行路径。'),
 'payment-system': ('与**结算系统**的区别在"层次"：'
   '支付系统是更广的概念（含零售支付、大额支付、卡组织、跨境汇款）；'
   '结算系统特指金融机构之间的最终清算（如Fedwire、TARGET2、CLS）。'
   '这一区分在危机中很重要：'
   '零售支付中断影响公众信心（塞浦路斯2013年的取现限制），'
   '而大额结算系统中断会立即冻结整个金融体系（"管道"失效）——'
   '因此后者被视为系统重要性基础设施，需专门监管（PFMI原则）。'),
 'prisoners-dilemma': ('与**协调博弈**的区别在均衡结构：'
   '囚徒困境有**唯一**纳什均衡，且该均衡对双方都劣（背叛/背叛）；'
   '协调博弈有**多个**均衡，且都是好的（只要预期一致）。'
   '这一区分决定政策思路：'
   '囚徒困境需要**改变激励**（惩罚违约、承诺机制）；'
   '协调博弈只需**改变预期**（存款保险可"挑选"不挤兑的均衡）。'
   '银行挤兑、竞争性贬值、债务减免中的搭便车，分别是这两类结构的实例。'),
 'property-rights': ('与**产权界定**的区别在"权利与执行"：'
   '产权是权利束（使用、收益、转让、排他）；'
   '产权界定是具体分配（谁拥有什么）与执行机制（法院、登记、治安）。'
   '这一区分在发展经济学中极其重要：'
   '仅有名义产权而无有效执行，等于没有产权（de Soto 的"死资本"论点）；'
   '而清晰的产权与低交易成本是市场交易的前提（科斯定理）。'
   '在危机中，产权不清会阻碍债务重组与资产处置（坏账银行的估值难题）。'),
 'transaction-cost': ('与**生产成本**的区别在"交易而非制造"：'
   '生产成本是制造商品的投入（劳动、原料、机器）；'
   '交易成本是**达成与执行交易**的成本（搜寻、议价、监督、履约）。'
   '这一区分是制度经济学的核心：'
   '企业之所以存在，是因为在某些情形下用内部指令替代市场交易更省成本（科斯）；'
   '而金融中介（银行、评级、交易所）本质上也是降低交易成本的制度。'
   '危机中交易成本骤升（信息不对称加剧、信任崩塌），是市场冻结的直接原因。'),
 'savings': ('与**投资**的区别在"主体与用途"：'
   '储蓄是收入中未消费的部分（可持有现金、存款、证券）；'
   '投资在宏观上指**资本形成**（设备、建筑、存货）。'
   '两者在会计上必然相等（储蓄＝投资，通过收入恒等式），但**决策主体不同**：'
   '储蓄由家庭决定，投资由企业决定。'
   '这一区分是凯恩斯"节约悖论"的基础：'
   '所有人同时增加储蓄会压低总需求，反而使储蓄无法实现（收入下降）。'),
 'investment': ('需区分三种含义，混用是常见错误：'
   '①**宏观投资**＝资本形成（机器、建筑、基础设施），增加未来生产能力；'
   '②**金融投资**＝购买金融资产（股票、债券），只是资产所有权的转移，不增加资本存量；'
   '③**外商直接投资**(FDI)＝取得企业控制权的跨境投资（含建厂与并购）。'
   '这一区分很关键：'
   '股市上涨不等于"投资增加"（可能只是估值变化）；'
   '而危机中"投资下滑"通常指宏观资本形成，与金融市场的交易量无关。'),
 'demand': ('与**需求**与**需求量**的区别在"曲线与点"：'
   '需求是整条曲线（各价格下的购买意愿）；'
   '需求量是某一价格下的具体数量。'
   '这一区分在政策讨论中常被忽略：'
   '"抑制需求"（移动曲线，如加税、限购）与"减少需求量"（沿曲线移动，如涨价）是不同的事。'
   '在危机分析中，"需求不足"指整条需求曲线左移（信心崩塌、收入下降），'
   '因此需要财政或货币扩张来移动曲线，而非仅调价。'),
 'population': ('与**劳动人口**的区别在"范围"：'
   '人口是全体居民；'
   '劳动人口是其中处于劳动年龄且参与劳动市场者（劳动参与率×适龄人口）。'
   '这一区分在增长分析中很关键：'
   '人口红利来自**劳动人口占比**高（抚养比低），而非人口总量大；'
   '人口老龄化通过抚养比上升、储蓄下降与财政压力影响增长（见 secular-stagnation）。'
   '危机中，人口结构决定调整的承受力（年轻社会更易消化失业冲击）。'),
 'inequality': ('与**贫困**的区别在"相对与绝对"：'
   '不平等是**相对**分布（差距大小）；'
   '贫困是**绝对**水平（是否低于某条线）。'
   '两者可以反向变动：增长可能同时降低贫困与提高不平等（顶端获益更多）。'
   '与**机会不平等**的区别在"结果与起点"：'
   '前者度量收入/财富分布，后者度量出身对结果的影响程度。'
   '这一区分在危机分析中很重要：'
   '危机后的不平等上升（资产价格反弹而工资停滞）与"机会不平等固化"是不同问题，处方也不同。'),
 'labour-market': ('与**资本市场**的区别在"要素"：'
   '劳动市场配置劳动（工资为价格），资本市场配置资本（利率为价格）。'
   '两者的调整速度差异是宏观分析的关键：'
   '工资调整慢（合约、制度、习惯），资本流动快——'
   '这一不对称使冲击主要通过就业数量而非工资来消化，'
   '因此衰退中失业上升远快于工资下降（这也是菲利普斯曲线存在的微观基础）。'),
 'specialization': ('与**多样化**的区别在"方向"：'
   '专业化使个体/地区专注于特定环节以提高效率；'
   '多样化则分散风险、提供韧性。'
   '这一权衡在危机中很尖锐：'
   '高度专业化的地区（单一产业城市）在遭遇行业冲击时受损更重；'
   '而过度多样化可能牺牲规模经济。'
   '在国际层面，专业化的风险是"比较优势被锁定"与供应链脆弱（2020年后讨论的"去风险"即针对此）。'),
 'tax-incidence': ('与**法定纳税人**的区别在"名义与实质"：'
   '法定纳税人由法律指定；'
   '税负归宿是**经济负担**的实际承担者（取决于供需弹性）。'
   '一般规律是：**弹性小的一方承担更多税负**——'
   '需求缺乏弹性（如必需品）时消费者承担更多；供给缺乏弹性（如土地）时卖方承担更多。'
   '这一区分在政策争论中常被忽略：'
   '对银行征税（如金融交易税）的名义纳税人是机构，实际归宿可能转嫁给客户或股东。'),
 'buyback': ('与**股息**的区别在"形式与灵活性"：'
   '股息是现金分配、通常稳定（下调有负面信号）；'
   '回购是买入自家股票、更灵活（可随时停止，且提升每股收益）。'
   '与**资本支出**的区别在"用途"：'
   '回购把现金返还股东，资本支出投向未来产能。'
   '这一区分在危机前很关键：'
   '2008年前与2021—22年，银行与航空公司大量回购后遭遇冲击、资本不足，'
   '因此受援期间常被限制分红与回购——保存资本最直接的手段是暂停可自由裁量的分配。'),
}

REL = {
 'toxic-assets': ['bad-bank', 'subprime-lending', 'collateralized-debt-obligation', 'tarp'],
 'junk-bond': ['credit-rating', 'credit-risk', 'bond', 'credit-cycle'],
 'payment-system': ['settlement-risk', 'netting', 'money-market', 'central-counterparty'],
 'prisoners-dilemma': ['coordination-games', 'bank-run', 'game-theory', 'competitive-devaluation'],
 'property-rights': ['transaction-cost', 'market-failure', 'public-good', 'institutional-economics'],
 'transaction-cost': ['property-rights', 'institutional-economics', 'market-failure', 'lemons-market'],
 'savings': ['investment', 'loanable-funds', 'savings-glut', 'secular-stagnation'],
 'investment': ['savings', 'capital-structure', 'total-factor-productivity', 'business-cycle'],
 'demand': ['aggregate-demand', 'supply-side', 'elasticity', 'effective-demand'],
 'population': ['labour-market', 'secular-stagnation', 'growth', 'lewis-turning-point'],
 'inequality': ['gini', 'labour-market', 'tax-incidence', 'welfare-economics'],
 'labour-market': ['unemployment', 'nairu', 'natural-rate-unemployment', 'inequality'],
 'specialization': ['transaction-cost', 'free-trade', 'comparative-advantage', 'industrial-revolution'],
 'tax-incidence': ['elasticity', 'fiscal-policy', 'laffer-curve', 'inequality'],
 'buyback': ['dividend', 'stock', 'capital-requirement', 'glass-steagall'],
}

for eid in NEW:
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('缺文件', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if CMP.get(eid):
        d['comparison'] = CMP[eid]
    if REL.get(eid):
        d['related'] = REL[eid]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作EX】已补comparison与related。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('已处理', len(NEW))
