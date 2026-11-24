# -*- coding: utf-8 -*-
"""续作JQ：深化 impossible-trinity（据专属维基页全文 10,718 字符）。"""
import json

SID = 'w-en-impossible-trinity'
p = 'data/entries/impossible-trinity.json'
d = json.load(open(p, encoding='utf-8'))

d['overview'] = (
    '不可能三角（又称三难困境，impossible trinity / trilemma）是开放宏观经济学的核心约束：'
    '**固定汇率、资本自由流动、独立货币政策**三者**最多同时实现两个**。'
    '**为什么**——设想世界利率为 5%，若本国央行想把国内利率压到 **2%**，'
    '资本会流出追逐更高回报，本币随即承受**贬值压力**；'
    '要维持固定汇率，央行就必须抛售外汇、回笼本币，国内利率被拉回接近世界水平，'
    '**货币政策自主性因此丧失**。三者之中必须放弃一个。'
    '**地位的变化**：这一思想在 **1980 年代**从"理论上的好奇"变成**开放经济宏观经济学的基础**——'
    '因为许多国家的资本管制相继瓦解，钉住汇率与货币政策自主性之间的冲突变得无法回避。'
    '**与危机的关系（关键）**：固定汇率 + 资本自由流动 + 独立货币政策这一组合'
    '**已知会引发金融危机**。文献常举的例子是'
    '**墨西哥比索危机(1994–1995)**、**1997 亚洲金融危机**与**阿根廷金融崩溃(2001–2002)**；'
    '其中东亚危机（1997–1998）被广泛视为这一政策组合导致的大规模金融危机的典型。'
    '**注意**：该表述指的是"三者同时追求"，而非"三者本身有问题"——'
    '放弃其中一项（如实行资本管制或浮动汇率）即可化解该特定冲突。')

d['timeline'] = [
    {'year': 1963, 'event': '蒙代尔-弗莱明模型为三元悖论提供理论基础'
                            '（据 Wikipedia Impossible trinity 相关记述；具体年份与归属待核实）'},
    {'year': 1980, 'event': '随多国资本管制瓦解，三元悖论从理论好奇变为开放经济宏观经济学的基础'
                            '（据 Wikipedia Impossible trinity）'},
    {'year': 1997, 'event': '亚洲金融危机爆发，被广泛视为"固定汇率+资本自由流动+独立货币政策"'
                            '组合导致的大规模危机典型（据 Wikipedia Impossible trinity）'},
]

d['key_data'] = [
    {'label': '三元悖论中可同时实现的政策目标数（最多）', 'value': 2, 'unit': '项（三者择二）',
     'year': 1980, 'comparable_price': False,
     'note': '原文：a central bank can pursue only two of the above-mentioned three policies simultaneously；'
             '单一来源待核实。', 'sources': [SID]},
    {'label': '教科书中举例的世界利率', 'value': 5, 'unit': '%', 'year': 1980,
     'comparable_price': False,
     'note': '原文：Assume that world interest rate is at 5%；单一来源待核实（示例数值，非史实统计）。',
     'sources': [SID]},
]

d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作JQ】据专属页全文深化：补"为什么"的利率示例、1980 年代地位转变、'
                        '与三场危机的关联；蒙代尔-弗莱明的年份归属待核实。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('impossible-trinity 已深化：overview %d 字、timeline %d、key_data %d'
      % (len(d['overview']), len(d['timeline']), len(d['key_data'])))
