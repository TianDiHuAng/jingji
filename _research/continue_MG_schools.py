# -*- coding: utf-8 -*-
"""续作MG：为 11 条确有学术分歧的概念补 schools（两派观点）。

依据：各条目自身的 wiki_full 全文与标准理论分歧。
不新增无据的具体数字/日期；观点均标注到该条目已有来源。
"""
import json

S = {
 'market-failure': [
   ('新古典干预视角',
    '市场在公共品、外部性、信息不对称与竞争不足处无法达到帕累托效率，'
    '因此需要政府纠正；金融监管的正当性即建立在此（据 Wikipedia Market failure）',
    'w-en-market-failure'),
   ('公共选择／奥地利视角',
    '所谓"市场失灵"常被用作扩大政府干预的理由，'
    '但政府同样面临信息与激励问题，干预可能带来更严重的失灵；'
    '该视角强调"失灵"往往是干预自身造成的（据 Wikipedia Market failure 的相关批评）',
    'w-en-market-failure'),
 ],
 'utility': [
   ('规范视角（目标函数）',
    '效用指我们希望最大化的目标，近似于边沁、密尔的功利主义概念，'
    '具有伦理与"善"的内涵（据 Wikipedia Utility）',
    'w-en-utility'),
   ('描述视角（偏好表示）',
    '效用仅表示可被观测的选择偏好可被某函数排序，不必包含"幸福"或"善"；'
    '在此视角下效用是序数的，人与人之间不可比较（据 Wikipedia Utility）',
    'w-en-utility'),
 ],
 'recession': [
   ('量化门槛视角',
    '衰退可由产出、就业、收入与销售等多项指标同时下降来识别，'
    '设法给出可操作的门槛（如连续两季负增长）（据 Wikipedia Recession）',
    'w-en-recession'),
   ('机构判定视角',
    '并不存在唯一的量化门槛，不同机构采用不同判据，'
    '因此同一时期是否算"衰退"可能有分歧；重要的是说明所用口径'
    '（据 Wikipedia Recession 关于定义之争的讨论）',
    'w-en-recession'),
 ],
 'growth': [
   ('增长优先视角',
    '经济增长提高物质生活水平，是减贫与公共福利改善的主要来源，'
    '因此应作为政策核心目标（据 Wikipedia Economic growth）',
    'w-en-growth'),
   ('限度／代价视角',
    '增长伴随资源消耗、环境代价与分配问题，'
    '且"增长"不等于"福祉"；该视角主张关注增长的构成与可持续性，'
    '甚至主张"去增长"（据 Wikipedia Economic growth 中的批评讨论）',
    'w-en-growth'),
 ],
 'prisoners-dilemma': [
   ('一次性博弈视角',
    '在单次博弈中，背叛对每个主体单独而言都是理性的，'
    '因此合作型结果不是均衡——这正是困境之所在（据 Wikipedia Prisoner\'s dilemma）',
    'w-en-prisoners-dilemma'),
   ('重复博弈视角',
    '若博弈反复进行、参与者有耐心，合作可以成为均衡'
    '（如"以牙还牙"策略），因此制度设计（重复互动、声誉、惩罚）'
    '能改变结果（据 Wikipedia Prisoner\'s dilemma 关于重复博弈的讨论）',
    'w-en-prisoners-dilemma'),
 ],
 'convergence': [
   ('无条件收敛视角',
    '资本边际报酬递减意味穷国增长应快于富国，'
    '因此差距会随时间缩小（据 Wikipedia Convergence (economics)）',
    'w-en-convergence'),
   ('条件收敛视角',
    '收敛只在"条件相似"的国家组内成立；'
    '全球范围内的无条件收敛证据薄弱，穷国与富国的差距在 20 世纪大部分时间扩大'
    '（据 Wikipedia Convergence (economics)）',
    'w-en-convergence'),
 ],
 'specialization': [
   ('效率视角',
    '分工提高熟练度、节省转换时间并便于发明机器，'
    '是生产率提升与国家贸易收益的来源（据 Wikipedia Division of labour）',
    'w-en-division-of-labour'),
   ('脆弱性视角',
    '专业化提高相互依赖：环节中断会沿链条传导，'
    '且知识碎片化使个体难以判断整体风险；'
    '金融体系的"发起—分销"分工即为典型（据 Wikipedia Division of labour 及相关讨论）',
    'w-en-division-of-labour'),
 ],
 'investment': [
   ('经济学视角（实物资本）',
    '投资指实物资本的增加（厂房、设备、住宅、存货），'
    '是 GDP 的组成部分，能提高经济体的生产能力（据 Wikipedia Investment）',
    'w-en-investment'),
   ('金融视角（资产购买）',
    '投资指购买金融资产（股票、债券）；'
    '一方的购买只是另一方的融资，并不直接增加资本存量——'
    '混淆两者是常见的分析错误（据 Wikipedia Investment）',
    'w-en-investment'),
 ],
 'toxic-assets': [
   ('"无法定价"视角',
    '"有毒"的实质不是资产一文不值，而是市场停止交易、模型失去可信度，'
    '因而无法定价；这使机构间无法判断彼此的偿付能力（据 Wikipedia Toxic asset）',
    'w-en-toxic-assets'),
   ('"价格下跌"视角',
    '有毒资产指价值大幅下跌、且不再存在有效市场的资产；'
    '由于资产与负债相抵并常带杠杆，价格下跌对持有人可能相当危险'
    '（据 Wikipedia Toxic asset）',
    'w-en-toxic-assets'),
 ],
 'eurodollar': [
   ('效率视角',
    '欧洲美元市场使美元流动性可在美国境外创造，'
    '提高了国际融资效率、降低了跨境交易成本（据 Wikipedia Eurodollar）',
    'w-en-eurodollar'),
   ('监管／风险视角',
    '它构成一个不受美国国内监管直接约束的美元市场，'
    '规模庞大且跨境自由流动；危机中的美元短缺难以由单一央行单独解决，'
    '需央行货币互换（据 Wikipedia Eurodollar）',
    'w-en-eurodollar'),
 ],
 'expectations': [
   ('适应性预期视角',
    '人们依据过去实际发生的情况外推未来、按预测误差逐步修正，'
    '因此预期调整滞后、变量呈现惯性（据 Wikipedia Expectation (philosophy)）',
    'w-en-expectations'),
   ('理性预期视角',
    '人们利用全部可得信息、按正确的经济模型推断，'
    '因此不犯系统性错误；政策规则改变时预期会立即调整'
    '（据 Wikipedia Expectation (philosophy) 及相关理论）',
    'w-en-expectations'),
 ],
}

n = 0
for eid, views in S.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    if d.get('schools'):
        continue
    d['schools'] = [{'holder': h, 'view': v, 'sources': [s]} for h, v, s in views]
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作MG】补 schools（两派观点，据本条目已有来源）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('%-20s schools=2' % eid)
print('共补', n, '条')
