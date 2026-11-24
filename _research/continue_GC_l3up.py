# -*- coding: utf-8 -*-
"""续作GC：把 growth/recession/utility/market-failure 升级为 L3（补 deep_svg/l3_detail/key_data/timeline/policy_response）。"""
import json
import os

SVG_TMPL = ("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 780 300' role='img'>"
            "<text x='20' y='26' class='ttl'>{title}</text>"
            "{boxes}"
            "<text x='20' y='286' class='sub'>{foot}</text></svg>")


def box(x, y, w, h, lbl, sub):
    return ("<g><rect x='%d' y='%d' width='%d' height='%d' rx='6' class='box'/>"
            "<text x='%d' y='%d' class='lbl'>%s</text>"
            "<text x='%d' y='%d' class='sub'>%s</text></g>"
            % (x, y, w, h, x + 9, y + 23, lbl, x + 9, y + 41, sub))


def arrow(x1, y1, x2, y2):
    return "<line x1='%d' y1='%d' x2='%d' y2='%d' class='ar'/>" % (x1, y1, x2, y2)


E = {}

E['growth'] = {
 'level': 'L3',
 'l3_detail': (
   '**增长的三个来源（全文口径）**：①**生产率**（技术进步与效率改善）；②**要素积累**'
   '（资本与劳动的投入增加）；③**人力资本与制度**（教育、健康、产权与政治制度）。'
   '索洛的著名估计认为，技术进步解释了美国长期人均收入增长的约 **80%**，'
   '而资本投资增加只能解释剩余的 **20%**——这一"余值"后来被称为全要素生产率(TFP)。'
   '**创新如何进入消费**：2013 年美国约 **60%** 的消费支出用于 1869 年尚不存在的商品与服务；'
   '20 世纪许多商品的实际价格下降超过 **90%**。'
   '这说明增长的实质不是"生产更多同样的东西"，而是**新产品与新工艺的持续出现**。'
   '**制度的分歧**：关于民主是否促进增长，文献结论并不一致——'
   '有研究认为民主通过产权保护与政策可预期性促进长期投资，'
   '也有研究指出威权体制在特定阶段能更快动员资源。本条目并列呈现，不替读者下结论。'
   '**度量陷阱**：GDP 只计入市场交易，漏掉家务劳动、非正规经济与环境损耗；'
   '跨国比较还受购买力平价与统计能力差异影响。'),
 'key_data': [
   ('技术进步对美国长期人均收入增长的贡献（索洛估计）', 80, '%', 1957,
    '原文：technological progress has accounted for 80 percent of the long-term rise in U.S. per capita income'),
   ('资本投资增加对同一增长的贡献', 20, '%', 1957,
    '原文：with increased investment in capital explaining only the remaining 20 percent'),
   ('2013年消费支出中用于1869年不存在的商品与服务的比例', 60, '%', 2013,
    '原文：about 60% of consumer spending in 2013 went on goods and services that did not exist in 1869'),
   ('20世纪许多商品实际价格的降幅（以上）', 90, '%', 2000,
    '原文：Over the 20th century, the real price of many goods fell by over 90%'),
 ],
 'timeline': [
   {'year': 1776, 'event': '斯密《国富论》讨论分工与市场范围对生产率的作用（据 Wikipedia Economic growth）'},
   {'year': 1956, 'event': '索洛增长模型把技术视为外生、以资本积累解释趋同（据 Wikipedia Economic growth）'},
   {'year': 1980, 'event': '内生增长理论把技术与人力资本内生化（据 Wikipedia Economic growth）'},
 ],
 'policy_response': [{
   'holder': '政策当局（增长政策）',
   'view': ('增长政策的着力点依来源分为三组：**要素积累**（提高储蓄与投资、改善基础设施）、'
            '**人力资本**（教育与健康）、**制度与创新**（产权保护、研发激励、竞争政策）。'
            '全文指出制度质量与政治安排对长期增长的影响仍有争论，'
            '而单纯提高投资率在不改善 TFP 的情况下会遭遇边际收益递减。'),
   'basis': '据 Wikipedia「Economic growth」Determinants 与 Growth theories 章节归纳；具体政策效果待核实',
   'sources': ['w-en-growth'],
 }],
 'deep_svg': SVG_TMPL.format(
   title='经济增长：来源与传导示意',
   boxes=(box(30, 60, 150, 56, '要素积累', '资本·劳动')
          + box(215, 60, 150, 56, '人力资本', '教育·健康')
          + box(400, 60, 150, 56, '技术进步', '创新·效率')
          + box(585, 60, 160, 56, '制度', '产权·竞争')
          + box(215, 190, 350, 60, '全要素生产率(TFP)', '索洛余值≈长期增长的主要来源')),
   foot='框内为增长来源；索洛估计技术进步约占美国长期人均收入增长的80%。来源见本页。'),
}

E['recession'] = {
 'level': 'L3',
 'l3_detail': (
   '**判定标准（多套并行）**：全文列出三个维度的门槛——'
   '**深度**（实际国民总收入下降 1.5%、非农就业下降 15%、失业率上升两点至至少 6%）；'
   '**扩散**（非农就业在超过 **75%** 的行业中下降，跨度六个月以上）；'
   '以及 OECD 的定义（至少两年期间累计产出缺口达到阈值）。'
   '**"两季负增长"只是通俗说法**，并非任一官方标准。'
   '**衰退 vs 萧条**：严重（GDP 下降 **10%**）或持久（三至四年）的衰退被称为萧条，'
   '但全文指出两者的成因与处方可能不同，界线并非纯量化。'
   '**两种特殊形态**：**资产负债表衰退**（私人部门集体偿债导致需求长期不足，'
   '货币政策失效）与**流动性陷阱**（利率触零后货币扩张无法刺激支出）。'
   '**悖论**：节约悖论（个体增储反而使总储蓄下降）与去杠杆悖论（集体去杠杆推高负债率）。'
   '**预测**：收益率曲线倒挂、PMI 与初请失业金等指标被用作先行信号，但准确率有限。'),
 'key_data': [
   ('衰退的深度门槛：实际国民总收入降幅', 1.5, '%', 0,
    '原文：A 1.5% decline in real gross national income'),
   ('衰退的深度门槛：非农就业降幅', 15, '%', 0,
    '原文：a 15% decline in non-agricultural employment'),
   ('衰退的扩散门槛：非农就业下降的行业占比（以上）', 75, '%', 0,
    '原文：A decline in non-agricultural employment in more than 75% of industries'),
   ('被界定为"萧条"的GDP降幅门槛', 10, '%', 0,
    '原文：A severe (GDP down by 10%) or prolonged (three or four years) recession is referred to as an economic depression'),
 ],
 'timeline': [
   {'year': 1945, 'event': '美国开始以 NBER 的多指标方法事后判定衰退起止（据 Wikipedia Recession）'},
   {'year': 1975, 'event': '奥肯法则被用于估计产出缺口与失业的关系（据 Wikipedia Recession）'},
   {'year': 2008, 'event': '资产负债表衰退与流动性陷阱在危机后被广泛讨论（据 Wikipedia Recession）'},
 ],
 'policy_response': [{
   'holder': '政策当局（逆周期政策）',
   'view': ('应对工具分为货币与财政两类：**货币政策**通过降息与流动性工具刺激需求，'
            '但在**流动性陷阱**与**资产负债表衰退**中效果受限；'
            '**财政政策**通过支出与减税直接支撑需求，乘数在经济闲置时更大。'
            '全文同时指出"节约悖论"与"去杠杆悖论"——'
            '个体理性的紧缩在总量上可能自我挫败，因此政策需对冲私人部门的同步收缩。'),
   'basis': '据 Wikipedia「Recession」Balance sheet recession／Liquidity trap／Paradoxes 章节归纳；具体效果待核实',
   'sources': ['w-en-recession'],
 }],
 'deep_svg': SVG_TMPL.format(
   title='衰退：冲击—放大—政策对冲示意',
   boxes=(box(30, 60, 150, 56, '初始冲击', '需求/供给/金融')
          + box(215, 60, 150, 56, '放大机制', '资产负债表·预期')
          + box(400, 60, 150, 56, '产出与就业', '收缩')
          + box(585, 60, 160, 56, '政策对冲', '货币+财政')
          + box(215, 190, 350, 60, '自我强化回路', '收入↓→支出↓→收入↓')),
   foot='框内为传导环节；判定门槛见 key_data。来源见本页。'),
}

E['utility'] = {
 'level': 'L3',
 'l3_detail': (
   '**两种含义**：全文指出 utility 至少有两义——'
   '**规范性含义**（某种状态本身的合意程度，与福利相关）与'
   '**描述性含义**（对偏好排序的数值表示，即"效用函数"）。'
   '现代经济学多取后者：效用不必可比人际、只需能排序。'
   '**边际效用递减**：同一种商品每多消费一单位带来的效用增量递减，'
   '这解释了需求曲线向下倾斜，也构成"水与钻石悖论"的解法。'
   '**期望效用**：在不确定性下，决策依据是各结果效用的概率加权（期望效用理论）。'
   '**行为经济学的修正**：前景理论指出人们对**损失**的敏感度高于同等收益，'
   '且概率权重非线性——这解释了为何期望效用理论在某些选择上系统性偏离实际行为。'
   '**政策含义**：任何"提高社会福利"的主张都必须说明如何加权不同个体的效用，'
   '而这本身是**规范判断**，不是实证结论。'),
 'key_data': [
   ('效用概念的现代用法数（至少）', 2, '种含义', 2000,
    '原文：the term has been used with at least two meanings'),
 ],
 'timeline': [
   {'year': 1789, 'event': '边沁提出功利主义，把效用与社会福利相联系（据 Wikipedia Utility）'},
   {'year': 1871, 'event': '边际革命：杰文斯、门格尔与瓦尔拉斯确立边际效用递减（据 Wikipedia Utility）'},
   {'year': 1944, 'event': '冯·诺依曼与摩根斯坦建立期望效用理论（据 Wikipedia Utility）'},
 ],
 'policy_response': [{
   'holder': '政策分析（福利评价）',
   'view': ('效用概念在政策中的用途是**评价**而非**指导**：'
            '成本收益分析以效用（或支付意愿）为尺度比较不同方案；'
            '但由于效用的人际可比性存疑，"社会总效用最大化"必须辅以分配判断。'
            '行为经济学的修正则提示：以显示偏好推断福利时，需考虑偏差与信息不足。'),
   'basis': '据 Wikipedia「Utility」相关章节归纳；具体应用争议待核实',
   'sources': ['w-en-utility'],
 }],
 'deep_svg': SVG_TMPL.format(
   title='效用：从偏好到福利评价示意',
   boxes=(box(30, 60, 150, 56, '偏好', '可排序')
          + box(215, 60, 150, 56, '效用表示', '序数/基数')
          + box(400, 60, 150, 56, '期望效用', '不确定性下')
          + box(585, 60, 160, 56, '社会福利', '需分配判断')
          + box(215, 190, 350, 60, '行为修正', '损失厌恶·概率权重非线性')),
   foot='框内为概念层次；效用的人际可比性是福利评价的关键争议。来源见本页。'),
}

E['market-failure'] = {
 'level': 'L3',
 'l3_detail': (
   '**定义与来源**：市场失灵指自由市场对商品与服务的配置**未达到帕累托效率**，'
   '常导致经济价值的净损失。全文指出该概念在**新古典经济学**中形成，'
   '早期分析集中于**外部性**与**公共品**，后扩展到信息不对称、垄断与协调失败。'
   '**主要类型**：①外部性（成本或收益未计入价格）；②公共品（非竞争、非排他，供给不足）；'
   '③信息不对称（逆向选择与道德风险）；④市场势力（垄断与买方垄断）；'
   '⑤协调失败（多重均衡，如银行挤兑）；⑥宏观波动与系统性风险。'
   '**与政府失灵的对偶**：指出市场失灵并不自动证明干预正当——'
   '干预本身可能因激励扭曲（寻租、信息不足、政治周期）而更糟。'
   '**金融领域的应用**：金融稳定兼具公共品与公共池属性，'
   '过度冒险的成本由全体承担而收益归个体，这构成审慎监管的理论基础。'),
 'key_data': [],
 'timeline': [
   {'year': 1776, 'event': '斯密提出"看不见的手"，为市场配置效率提供早期论证（据 Wikipedia Market failure）'},
   {'year': 1920, 'event': '庇古系统分析外部性，提出征税/补贴的矫正思路（据 Wikipedia Market failure）'},
   {'year': 1954, 'event': '萨缪尔森给出公共品的正式定义（据 Wikipedia Market failure）'},
   {'year': 1970, 'event': '阿克洛夫"柠檬市场"揭示信息不对称导致的市场萎缩（据 Wikipedia Market failure）'},
 ],
 'policy_response': [{
   'holder': '政策当局（矫正性干预）',
   'view': ('针对不同类型，工具不同：外部性用**庇古税/补贴**或**科斯式产权界定**；'
            '公共品用**公共供给或政府采购**；信息不对称用**强制披露与准入审查**；'
            '市场势力用**反垄断**；协调失败用**可信承诺**（如存款保险"挑选"好均衡）。'
            '全文强调判断标准：干预的收益须**大于**政府失灵的成本，'
            '而这需要逐案评估而非按类型套用。'),
   'basis': '据 Wikipedia「Market failure」相关章节归纳；具体政策效果待核实',
   'sources': ['w-en-market-failure'],
 }],
 'deep_svg': SVG_TMPL.format(
   title='市场失灵：类型与矫正工具示意',
   boxes=(box(24, 60, 138, 56, '外部性', '庇古税·产权')
          + box(178, 60, 138, 56, '公共品', '公共供给')
          + box(332, 60, 138, 56, '信息不对称', '披露·准入')
          + box(486, 60, 138, 56, '市场势力', '反垄断')
          + box(640, 60, 130, 56, '协调失败', '可信承诺')
          + box(178, 190, 420, 60, '判断标准', '干预收益 > 政府失灵成本')),
   foot='框内为失灵类型与对应工具；右下方为决策判据。来源见本页。'),
}

n = 0
for eid, upd in E.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    d['level'] = 'L3'
    for k in ('l3_detail', 'deep_svg', 'timeline', 'policy_response', 'key_data'):
        if upd.get(k):
            d[k] = upd[k]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作GC】升级为L3（补 deep_svg/l3_detail/key_data/timeline/policy_response）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('升级 L3:', eid)

import glob
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
l3 = [e for e in es if e.get('level') == 'L3']
full = sum(1 for e in l3 if all(e.get(x) for x in ('deep_svg','l3_detail','key_data','timeline','policy_response')))
core = [e for e in es if e.get('tier') == '核心']
core_l3 = sum(1 for e in core if e.get('level') == 'L3')
print('\nL3 共 %d（五项全备 %d）| 核心 %d 条中 L3 %d 条' % (len(l3), full, len(core), core_l3))
