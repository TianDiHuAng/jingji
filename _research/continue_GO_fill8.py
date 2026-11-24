# -*- coding: utf-8 -*-
"""续作GO：为 8 个薄弱条目补充 timeline/schools/key_data（取自维基全文）。"""
import json
import os

ADD = {
 'equity-premium': {
   'timeline': [
     {'year': 1985, 'event': 'Mehra 与 Prescott 发表《The Equity Premium: A Puzzle》，'
                             '正式提出股权溢价之谜（据 Wikipedia Equity premium puzzle）'},
   ],
   'schools': [
     ('谜题本身', '历史股权溢价约 **5%—8%**，相对标准模型所隐含的风险厌恶水平而言**高得难以置信**；'
                  '"谜题"指的正是这一差距缺乏解释（据 Wikipedia Equity premium puzzle）', 'w-en-equity-premium'),
     ('罕见灾难假说', '若投资者对极低概率的巨大灾难赋予足够权重，则高溢价可在理性框架内被解释'
                      '（据 Wikipedia Equity premium puzzle Rare events hypothesis）', 'w-en-equity-premium'),
   ],
   'key_data': [
     ('历史股权溢价区间（下界）', 5, '%', 1985, '原文：the 5% to 8% premium is considered to be an implausibly high difference'),
     ('历史股权溢价区间（上界）', 8, '%', 1985, '原文：the 5% to 8% premium'),
   ],
 },
 'fractional-reserve': {
   'timeline': [
     {'year': 1668, 'event': '瑞典央行(Riksbank)成立，为世界第一家中央银行'
                             '（据 Wikipedia Fractional-reserve banking）'},
   ],
   'schools': [
     ('挤兑的脆弱性', '当储户希望提取的金额超过银行持有的准备金时，银行会陷入短缺——'
                      '这是部分准备金制度的内在脆弱点（据 Wikipedia Fractional-reserve banking）',
      'w-en-fractional-reserve'),
   ],
 },
 'inequality': {
   'key_data': [
     ('乐施会2026年报告：亿万富翁人数', 3000, '人', 2026,
      '原文：the number of billionaires has increased to 3,000'),
     ('乐施会2026年报告：亿万富翁财富总额', 18.3, '万亿美元', 2026,
      '原文：their wealth has increased to 18.3 trillion, breaking records'),
   ],
   'schools': [
     ('国内不平等的上升', '过去 30 年**多数国家内部**的不平等显著上升，尤其在发达国家'
                          '（据 Wikipedia Economic inequality）', 'w-en-inequality'),
   ],
 },
 'investment': {
   'timeline': [
     {'year': -1700, 'event': '投资行为可追溯至约公元前 1700 年的《汉谟拉比法典》'
                              '（据 Wikipedia Investment）'},
   ],
 },
 'eurodollar': {
   'timeline': [
     {'year': 1949, 'event': '一种说法认为第一个欧洲美元账户 1949 年设于法国、为当时的中国所设'
                             '（据 Wikipedia Eurodollar History）'},
   ],
 },
 'modigliani-miller': {
   'schools': [
     ('定理的基准含义', '在无税收、无破产成本等假设下，企业价值与资本结构**无关**——'
                        '这为讨论"现实中哪些摩擦使其相关"提供了基准（据 Wikipedia Modigliani–Miller theorem）',
      'w-en-modigliani-miller'),
   ],
 },
 'payment-system': {
   'schools': [
     ('系统重要性', '支付与结算系统是金融体系的"管道"：其稳定性直接决定交易能否完成，'
                    '因此被视为需专门监管的基础设施（据 Wikipedia Payment system）', 'w-en-payment-system'),
   ],
 },
 'proprietary-trading': {
   'schools': [
     ('与做市的边界', '自营交易以自有资金为自己获利；做市则为客户提供流动性并赚取价差。'
                      '沃尔克规则禁止前者、允许后者，边界模糊正是执行难点'
                      '（据 Wikipedia Proprietary trading；具体条文待核实）', 'w-en-proprietary-trading'),
   ],
 },
}

n = 0
for eid, upd in ADD.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    added = []
    if upd.get('timeline') and not d.get('timeline'):
        d['timeline'] = upd['timeline']; added.append('timeline')
    if upd.get('schools') and not d.get('schools'):
        d['schools'] = [{'holder': h, 'view': v, 'src': s} for h, v, s in upd['schools']]
        added.append('schools')
    if upd.get('key_data') and not d.get('key_data'):
        sid = next((s for s in d['sources'] if s.startswith('w-en')), d['sources'][0])
        d['key_data'] = [{
            'label': label, 'value': value, 'unit': unit, 'year': year,
            'comparable_price': False,
            'note': note + '；单一来源待核实。', 'sources': [sid],
        } for label, value, unit, year, note in upd['key_data']]
        added.append('key_data')
    if added:
        d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作GO】补充 %s。' % '/'.join(added))
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n += 1
        print('%s: +%s' % (eid, '/'.join(added)))
print('\n共更新 %d 个条目' % n)
