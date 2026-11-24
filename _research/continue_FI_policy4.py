# -*- coding: utf-8 -*-
"""续作FI：补写4条案例政策应对（日本泡沫/希腊/1825/1819）。"""
import json
import os
import glob

POL = {
 'japan-asset-bubble-1990': (
   '**泡沫期的货币政策（事后被视为成因）**：资产价格加速上涨与短期利率的大幅下降密切相关——'
   '日本银行将官方贴现率由 **5.00%（1986年1月30日）降至 2.50%（1987年2月23日）**，'
   '此后直到 **1989年5月30日** 才调整。'
   '**泡沫破裂后的财政应对**：泡沫后数年日本 GDP 增速急剧下降，'
   '**1993 年**政府决定**大幅增加政府支出**，意在扩大内需、刺激消费以带动经济走出衰退；'
   '但正文指出，增加政府支出的效果**不如政府预期的那么有效**。',
   '据 Wikipedia「Japanese asset price bubble」Monetary policy 与 Government spending 章节；'
   '政策主体：日本银行/日本政府；动作：贴现率下调（成因）、1993年财政扩张（应对）'),

 'greek-debt-crisis': (
   '**财政失衡的形成**：2004—2009 年名义产出增长 **40%**，而中央政府**基本支出增长 87%**、'
   '税收仅增长 **31%**。财政部原计划实施实际支出削减，使 2009—2013 年支出仅增长 **3.8%**，'
   '远低于同期预期通胀 **6.9%**。'
   '**危机后的判断与应对**：2009 年债务因赤字高于预期与偿债成本上升而增加；'
   '希腊政府评估认为**仅靠结构性改革不足**——因为改革见效前债务仍会升至不可持续水平；'
   '因此在结构改革之外，还需**永久性与临时性的紧缩措施**。',
   '据 Wikipedia「Greek government-debt crisis」Government deficit 与 Government debt 章节；'
   '政策主体：希腊政府/财政部；动作：支出削减、结构性改革＋紧缩组合'),

 'panic-1825': (
   '**危机推动的监管改革**：1825 年危机虽动摇公众信心，但最终**强化并集中了市场**而非摧毁它。'
   '当时许多人认为，这次崩溃及随后一系列较轻的危机凸显了**改善监管**的必要。'
   '此后《1855年有限责任法》《1856年公司法》与《1862年公司法》等立法'
   '尝试建立相应的公司制度框架。',
   '据 Wikipedia「Panic of 1825」Regulation 章节；'
   '政策主体：英国议会；动作：有限责任与公司法系列立法'),

 'panic-1819': (
   '**背景性制度缺失**：1811 年第一合众国银行未能续期，使州银行**不再受监管约束**；'
   '"亲信贷"的共和派把自由放任的金融原则与杰斐逊式政治理念结合，将土地投机等同于"粗犷的个人主义"。'
   '**第二合众国银行的设立目标**：其复兴有两大目标——'
   '第一，通过**诱导恢复（银行券与金银的）可兑换性**来逆转战后州银行的通胀做法；'
   '第二，扩大普通人获取银行信贷的机会，促进实业与有序的西进扩张。'
   '该行的监管机制即围绕这两项目标设计。',
   '据 Wikipedia「Panic of 1819」相关章节；'
   '政策主体：美国国会/第二合众国银行；动作：设立国家银行、诱导恢复兑换、调节信贷扩张'),
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FI】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('\n补写 %d | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
