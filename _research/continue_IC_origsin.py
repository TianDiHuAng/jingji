# -*- coding: utf-8 -*-
"""续作IC：为 original-sin 补 timeline／key_data 并扩充概述（据其专属维基页全文）。"""
import json

p = 'data/entries/original-sin.json'
d = json.load(open(p, encoding='utf-8'))
SID = 'w-en-original-sin'

d['overview'] = (
    '原罪(Original sin) 是经济学文献中的术语，由 Eichengreen 与 Hausmann 于 **1999 年**提出'
    '（后与 Panizza 合作扩展），指"**多数国家无法以本国货币在海外借款**"的情形。'
    '其后果是**货币错配**：这些国家的对外负债以外币计价，而资产与收入多为本币，'
    '因此本币贬值会直接恶化其资产负债表——净值下降、偿债负担上升，'
    '进而可能引发违约或银行危机。'
    '文献给出**三个衡量指标(OSIN1／OSIN2／OSIN3)**，均定义为"1 减去本币计价证券占相关总量的比例"，'
    '取值 **0—1**，越接近 1 表示原罪越严重：'
    'OSIN1 只看国际债券，OSIN2 纳入银行贷款与互换（覆盖更广但精度较低），'
    'OSIN3 以中间指数刻画互换的影响。'
    '实证研究指出原罪的**六个决定因素**：'
    '①发展水平；②货币可信度；③债务负担水平；④汇率制度；⑤收益率曲线斜率；⑥投资者基础规模。')

d['timeline'] = [
    {'year': 1999, 'event': 'Eichengreen 与 Hausmann 提出"原罪"概念，'
                            '并以本币银行借款与国际债券份额构建衡measured指标'
                            '（据 Wikipedia Original sin (economics)）'},
    {'year': 2001, 'event': '与 Panizza 合作扩展，形成 OSIN1／OSIN2／OSIN3 三个指标'
                            '（据 Wikipedia Original sin (economics)）'},
    {'year': 2003, 'event': '后续研究转向"原罪的赎免"——哪些国家、通过何种路径摆脱了原罪'
                            '（据 Wikipedia Original sin (economics)）'},
]

d['key_data'] = [
    {'label': '原罪指标(OSIN)的取值范围上界', 'value': 1, 'unit': '（0—1，越接近1越严重）',
     'year': 1999, 'comparable_price': False,
     'note': '原文：Original sin measures range between 0 and 1；单一来源待核实。', 'sources': [SID]},
    {'label': '原罪指标的个数（文献定义）', 'value': 3, 'unit': '个（OSIN1／OSIN2／OSIN3）',
     'year': 2001, 'comparable_price': False,
     'note': '原文：There are three different measures of original sin in economics literature；单一来源待核实。',
     'sources': [SID]},
    {'label': '实证研究指出的决定因素个数', 'value': 6, 'unit': '项', 'year': 2003,
     'comparable_price': False,
     'note': '原文：(i) the level of development, (ii) monetary credibility, (iii) level of debt burden, '
             '(iv) the exchange rate regime, (v) slope of the yield curve, and (vi) size of the investor base'
             '；单一来源待核实。', 'sources': [SID]},
]

d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作IC】据专属维基页全文补充 timeline／key_data／六个决定因素；'
                        '同年份与指标定义待第二来源核实。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('original-sin 已补充：timeline %d 条、key_data %d 条' % (len(d['timeline']), len(d['key_data'])))
