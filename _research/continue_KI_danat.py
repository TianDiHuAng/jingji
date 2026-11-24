# -*- coding: utf-8 -*-
"""续作KI：改写 danatbank-1931 的 overview（用中文译名，英文全称移入括号）。"""
import json

p = 'data/entries/danatbank-1931.json'
d = json.load(open(p, encoding='utf-8'))
old = len(d['overview'])
d['overview'] = (
    '**达纳特银行(Danat-Bank)** 是一家德国大型股份制银行，'
    '由**达姆施塔特银行**（Darmstädter Bank für Handel und Industrie）'
    '与**德意志国民银行**（Nationalbank für Deutschland）于 **1922 年**合并成立。'
    '**1931 年 7 月**，该行倒闭——这是当年德国银行危机的**标志性事件**，'
    '也是欧洲银行危机从奥地利（Creditanstalt 倒下）蔓延至德国的关键一环。'
    '**为什么重要**：它的倒闭表明，'
    '在**金本位**与**固定汇率**的双重约束下，'
    '中央银行无法同时扮演最后贷款人与汇率守护者——'
    '德国帝国银行担心救助会耗尽黄金储备、危及汇率，'
    '因此迟迟未能果断注资，最终酿成全国性的银行挤兑与信贷冻结。'
    '**本库的处理**：该行的具体资产负债规模与救助金额尚无可靠单一来源，'
    '故不列数值，仅记录时间与因果位置；'
    '与 1931 年中欧危机的整体脉络见 creditanstalt 与本单元的相关条目。')
d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作KI】overview 改写为以中文为主（原 %d 字，英文全称过多）。' % old)
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('danatbank-1931: %d → %d 字' % (old, len(d['overview'])))
