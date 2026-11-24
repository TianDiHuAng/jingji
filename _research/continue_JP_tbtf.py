# -*- coding: utf-8 -*-
"""续作JP：深化 too-big-to-fail（据专属维基页全文 36,058 字符）。"""
import json

SID = 'w-en-too-big-to-fail'
p = 'data/entries/too-big-to-fail.json'
d = json.load(open(p, encoding='utf-8'))

d['overview'] = (
    '太大而不能倒(TBTF) 指某些金融机构因**规模、复杂性、互联性与关键功能**过大，'
    '一旦意外进入清算，金融体系与实体经济将承受严重后果，政府因此倾向于救助。'
    '**权威定义**（时任美联储主席伯南克，2010 年）：'
    '"一家太大而不能倒的机构，是指其规模、复杂性、互联性与关键功能达到这样的程度——'
    '若该机构意外进入清算，金融体系其余部分与实体经济将面临严重不利后果。"'
    '他并强调：政府在一场危机中支持这类机构，**并非出于偏袒，也不是特别关照其管理层、'
    '股东或债权人**，而是因为其倒闭的后果无法承受。'
    '**处置工具的演进**（美国经验，说明"救助"并非唯一选项）：'
    '**1950 年以前**，联邦银行监管者对资不抵债机构基本只有两条路——'
    '①**关闭清算**（变卖资产、偿付受保存款人）；②**购买与承接**（促成另一家机构收购其资产、'
    '承担其负债）。**1950 年《联邦存款保险法》**提供了第三种：'
    '③**提供援助**——通过贷款或联邦直接收购资产维持机构，直至其恢复。'
    'TBTF 的**代价**是道德风险（债权人因预期获救而不审慎定价）与不公平竞争'
    '（大机构享有隐性补贴，融资成本更低）。'
    '对策方向是**让处置可信**：提高资本与自救要求、建立有序处置机制（见 bank-resolution）、'
    '并对系统重要性机构分级加码（见 sifi）。')

d['timeline'] = [
    {'year': 1933, 'event': '美国设立联邦存款保险公司(FDIC)，为小额存款提供保险——'
                            '这是"防止挤兑"而非"防止倒闭"的制度（据 Wikipedia Too big to fail 相关系节）'},
    {'year': 1950, 'event': '美国《联邦存款保险法》赋予监管者第三种处置选项：提供援助'
                            '（贷款或直接收购资产），此前只有关闭清算与购买承接两种'
                            '（据 Wikipedia Too big to fail）'},
    {'year': 1984, 'event': '伊利诺伊大陆银行获救助，成为 TBTF 实践的标志性案例'
                            '（据 Wikipedia Too big to fail 相关记述；细节待核实）'},
    {'year': 2010, 'event': '伯南克给出 TBTF 的权威定义，明确其四要素为规模、复杂性、'
                            '互联性与关键功能（据 Wikipedia Too big to fail）'},
]

d['key_data'] = [
    {'label': '伯南克定义中 TBTF 的构成要素个数', 'value': 4,
     'unit': '项（规模／复杂性／互联性／关键功能）', 'year': 2010, 'comparable_price': False,
     'note': '原文：whose size, complexity, interconnectedness, and critical functions；'
             '单一来源待核实。', 'sources': [SID]},
    {'label': '1950 年前美国处置资不抵债银行的选项数', 'value': 2,
     'unit': '种（关闭清算／购买与承接）', 'year': 1950, 'comparable_price': False,
     'note': '原文：U.S. federal bank regulators had essentially two options for resolving an '
             'insolvent institution；单一来源待核实。', 'sources': [SID]},
]

d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作JP】据专属维基页全文（36,058 字符）深化：补伯南克 2010 定义、'
                        '1950 年三种处置方式的演进、四要素；1984 大陆银行案例细节待核实。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('too-big-to-fail 已深化：overview %d 字、timeline %d、key_data %d'
      % (len(d['overview']), len(d['timeline']), len(d['key_data'])))
