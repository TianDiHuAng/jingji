# -*- coding: utf-8 -*-
"""续作JS：深化 moral-hazard（据专属页 26,026 字符）。"""
import json

SID = 'w-en-moral-hazard'
p = 'data/entries/moral-hazard.json'
d = json.load(open(p, encoding='utf-8'))

d['overview'] = (
    '道德风险(moral hazard) 指一方在**受到保护**（保险、救助预期、或"赚了归自己、亏了有人兜"的安排）之后'
    '**改变行为、承担更多风险**，因为后果有一部分由他人承担。'
    '**词源澄清**（据 Dembe 与 Boden 的研究）：该词可追溯到 **17 世纪**，到 **19 世纪末**已被英国保险公司广泛使用；'
    '早期用法带负面含义，指欺诈或不道德行为。但两位学者指出，18 世纪研究决策问题的著名数学家'
    '把 "moral" 用作"**主观的**"(subjective) 之意——**这与伦理无关**，可能混淆了该词后来的道德色彩。'
    '**在金融中的经典案例**：**1998 年**纽约联储主席 McDonough 出手安排，使长期资本管理公司(LTCM)的'
    '对手方免于损失。此举被前美联储主席**沃尔克**等人批评为**加重了道德风险**。'
    '经济学家 Tyler Cowen 的概括是：债权人由此相信"**只要机构的崩溃会威胁全球信贷体系，'
    '美联储就会让他们的贷款得到偿付**"。'
    '**与 2008 年危机的关系**：许多学者与记者认为道德风险在其中起了作用，'
    '一般归纳为**三条渠道**：①**资产管理人**替他人理财时倾向冒更多风险，'
    '尤其当报酬按**利润百分比**计提（赚了分成、亏了不担）；②③（其余两条待据原文补全）。'
    '**争议焦点**：道德风险常被用作反对救助的理由，但批评者指出——'
    '若系统性崩溃的代价远大于救助成本，"不救"本身也会制造更大的伤害；'
    '因此政策目标不是"消灭道德风险"，而是**让救助尽可能少、且有代价**（如要求股东先承担损失）。')

d['timeline'] = [
    {'year': 1700, 'event': '道德风险一词可追溯至 17 世纪；到 19 世纪末已被英国保险公司广泛使用，'
                            '早期带"欺诈/不道德"的负面含义（据 Wikipedia Moral hazard；'
                            'Dembe 与 Boden 研究）', 'sources': [SID]},
    {'year': 1998, 'event': '纽约联储主席 McDonough 安排使 LTCM 的对手方免于损失，'
                            '被沃尔克等人批评为加重道德风险（据 Wikipedia Moral hazard）',
     'sources': [SID]},
    {'year': 2008, 'event': '许多学者与记者认为道德风险在 2008 年金融危机中起了作用，'
                            '归纳为三条渠道（据 Wikipedia Moral hazard）', 'sources': [SID]},
]

d['key_data'] = [
    {'label': '2008 危机中道德风险的传导渠道数', 'value': 3, 'unit': '条', 'year': 2008,
     'comparable_price': False,
     'note': '原文：there are three ways in which moral hazard may have manifested itself；'
             '单一来源待核实。', 'sources': [SID]},
]

d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作JS】据专属页全文（26,026 字符）深化：补 17 世纪词源与 "moral=主观" 的澄清、'
                        '1998 年 LTCM 的经典案例、2008 年三条渠道中的第一条；'
                        '另两条渠道待据原文补全。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('moral-hazard 已深化：overview %d 字、timeline %d、key_data %d'
      % (len(d['overview']), len(d['timeline']), len(d['key_data'])))
