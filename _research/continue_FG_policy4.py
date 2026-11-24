# -*- coding: utf-8 -*-
"""续作FG：补写4条案例政策应对 + 记录剩余案例的来源限制。"""
import json
import os
import glob

POL = {
 'venezuela-hyper-2016': (
   '**政策转向（放弃管制）**：在 2019 年国际制裁加剧之后，马杜罗政府**放弃了查韦斯时期'
   '自 2003 年起实施的价格与货币管制**，其结果是经济从持续下滑中出现反弹。'
   '**非正式美元化**：据咨询机构 Econalítica 的调查，2019 年 9 月委内瑞拉约 **54%** 的交易以美元进行，'
   '马拉开波更高达 **86%**；几乎所有电器销售、以及约半数的服装、汽车零配件与食品销售已美元化。',
   '据 Wikipedia「Venezuelan hyperinflation」Informal dollarization 章节；'
   '政策主体：委内瑞拉政府/央行；动作：放弃价格与货币管制（被动接受美元化）'),

 'syrian-pound-crisis': (
   '**战后货币改革**：2024 年底阿萨德政权倒台后，领导过渡政府的总统 Ahmed al-Sharaa 表示，'
   '拟在货币稳定后以新货币取代叙利亚镑。'
   '**2025年8月**宣布将对货币进行重估——**去掉两个零**并于 12 月发行新钞；'
   '10 月当局再次确认该计划但把日期推迟至 **2026 年**。'
   '**2025年12月29日**，叙利亚央行与总统共同公布了新版叙利亚镑的面额。',
   '据 Wikipedia 相关条目 Post-Assad reforms 章节；'
   '政策主体：叙利亚过渡政府/央行；动作：货币重估（去两个零）、发行新钞'),

 'uruguay-2002': (
   '**美元化作为长期制度安排**：乌拉圭经济的美元化是长期特征，'
   '根源在于 1950 年代起的慢性通胀与对本币信心的下降；'
   '**1962 年当局授权美元存款**，此后美元存款在通胀期间成为首选的保值手段。'
   '研究者把乌拉圭的高度美元化归因于"市场不完整"，包括某些市场（如长期本币信贷）的缺失。'
   '（正文对本币与外币资产的替代机制有进一步讨论。）',
   '据 Wikipedia「2002 Uruguay banking crisis」Dollarization 章节；'
   '说明：此处记载的是长期制度性选择（1962年授权美元存款），而非2002年当年的应急措施'),

 'second-bank': (
   '**制度职能（监管机制）**：1816 年经国会特许设立的第二合众国银行的首要监管任务，'
   '是**抑制州或私人放贷机构无节制地扩张纸币（银行券）**——这对这些机构而言极为有利可图。'
   '该行由此主持了信用的"民主化"过程，促成了面向农场主、小商人等的大量且有利可图的银行贷款发放。',
   '据 Wikipedia「Second Bank of the United States」Regulatory mechanisms 章节；'
   '政策主体：美国国会特许的国家银行；动作：以监管职能抑制纸币无序扩张'),
}

n = 0
for eid, (view, basis) in POL.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if d.get('policy_response'):
        print('已有', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
                             'basis': basis + '；效果评价待核实',
                             'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FG】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
rest = [e for e in cases if not e.get('policy_response')]
print()
print('补写 %d | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
print('剩余无政策案例:', len(rest))
from collections import Counter
print('剩余按类型:', dict(Counter(e['crisis_type'] for e in rest)))
