# -*- coding: utf-8 -*-
"""续作JV：深化 global-debt（据专属页 8,940 字符）。"""
import json

SID = 'w-en-global-debt'
p = 'data/entries/global-debt.json'
d = json.load(open(p, encoding='utf-8'))

d['overview'] = (
    '全球债务指全球范围内所有部门——**政府、企业与家庭**——所欠货币的总量。'
    '它是观察全球杠杆水平与金融脆弱性的**总量指标**。'
    '**三个必须区分的口径**（据维基条目对统计表的说明）：'
    '①**公共债务占 GDP**：政府及其机构的**内外债总额**占该国 GDP 的比例；'
    '②**私人债务占 GDP**：公民与私营企业的内外债总额占 GDP 的比例；'
    '③**外债**：公共与私人债务人对**外国银行及其他外国债权人**的负债总额（以十亿美元计）。'
    '三者不可混用——同一国家的"债务水平"在三种口径下可以相差悬殊。'
    '**一个常被忽略的事实**：世界的债务总量**大于流通中的货币总量**。'
    '据该条目的统计，**总债务与货币供应量之比**从日本、瑞士的 **1.7** 到丹麦、冰岛的 **4.7**，'
    '**世界总计为 1.8**。'
    '经济学家更常看**债务与 GDP 之比**：从拉脱维亚的 **1.5** 到卢森堡的 **5.0**，'
    '**世界总计为 3.5**（据国际金融协会 IIF）。'
    '**风险的构成比总量更重要**：公共与私人、国内与跨境的结构差异，'
    '决定了同样的总量在冲击下会以何种方式破裂'
    '（如外币外债占比高者，本币贬值即直接恶化资产负债表）。')

d['timeline'] = [
    {'year': 2015, 'event': '国际金融协会(IIF)等机构开始系统发布全球债务总量监测，'
                            '"债务/GDP"成为常用观察口径（据 Wikipedia Global debt 所引统计；'
                            '起始年份待核实）', 'sources': [SID]},
]

d['key_data'] = [
    {'label': '世界总债务与货币供应量之比', 'value': 1.8, 'unit': '倍', 'year': 2018,
     'comparable_price': False,
     'note': '原文：The ratio for the world total is 1.8, according to the above table；'
             '年份为条目表格快照，待核实。', 'sources': [SID]},
    {'label': '世界总债务与GDP之比', 'value': 3.5, 'unit': '倍', 'year': 2018,
     'comparable_price': False,
     'note': '原文：The world total is 3.5, according to the Institute of International Finance；'
             '年份待核实。', 'sources': [SID]},
    {'label': '总债务/货币供应比的最高国家值（丹麦、冰岛）', 'value': 4.7, 'unit': '倍', 'year': 2018,
     'comparable_price': False,
     'note': '原文：The ratio of total debt to money supply ranges from 1.7 in Japan and '
             'Switzerland to 4.7 in Denmark and Iceland；年份待核实。', 'sources': [SID]},
]

d['comparison'] = (
    '与**外债**的区别：外债只计对**外国债权人**的负债，全球债务则含国内债权债务；'
    '同一笔国内债务在两者中只出现一次与零次的差别。'
    '与**政府债务**的区别：政府债务只是全球债务的一个部门。'
    '与**杠杆率**的关系：杠杆率通常以"债务/资产"或"债务/资本"衡量，'
    '而全球债务统计多用"债务/GDP"——分母不同，结论也不同。'
    '与**国际投资头寸(IIP)** 的区别：IIP 是**存量资产负债表**（资产减负债=净头寸），'
    '全球债务只统计负债一方。')

d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作JV】据专属页全文（8,940 字符）深化：补三种口径的区分、'
                        '"债务多于货币"的事实与债务/GDP 世界总计 3.5（IIF）；'
                        '各数值的统计年份待核实。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('global-debt 已深化：overview %d 字、timeline %d、key_data %d'
      % (len(d['overview']), len(d['timeline']), len(d['key_data'])))
