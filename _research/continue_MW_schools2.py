# -*- coding: utf-8 -*-
"""续作MW：为 6 条单 schools 条目补第二派观点（真实争论，据现有来源）。"""
import json

ADD = {
 'fractional-reserve': (
   '信贷中介功能视角',
   '部分准备金是银行实现"期限转换"、支撑信贷与经济活动的必要机制；'
   '其脆弱性应通过**存款保险、资本与流动性要求、最后贷款人**来缓释，而非废除——'
   '这与主张"100% 准备金"的奥地利学派观点相对立（据 Wikipedia Fractional-reserve banking）',
   'w-en-fractional-reserve'),
 'modigliani-miller': (
   '权衡理论视角',
   '现实中存在**税盾（利息抵税）与破产成本**，二者随杠杆此消彼长，'
   '因此**存在最优资本结构**——这恰是 MM 定理标出"理想条件"后被用来解释现实偏离的方向'
   '（据 Wikipedia Modigliani–Miller theorem）',
   'w-en-modigliani-miller'),
 'labour-market': (
   '竞争性市场视角',
   '若无摩擦，工资由**劳动的边际生产率**决定、劳动市场趋于出清；'
   '该视角把失业更多归因于工资刚性与制度约束，而非搜寻摩擦'
   '（据 Wikipedia Labour economics）',
   'w-en-labour-market'),
 'counterparty-risk': (
   '市场自律视角',
   '交易双方可通过**抵押品、交易限额、双边净额协议与信用评估**自行管理结算敞口，'
   '监管与中央对手方并非唯一手段；强制集中清算也会带来新的集中风险'
   '（据 Wikipedia Settlement risk）',
   'w-en-settlement-risk'),
 'payment-system': (
   '效率与竞争视角',
   '支付系统的技术演进降低了交易成本、促进了竞争与金融普惠；'
   '监管需在**稳定性与创新**之间平衡，过度审慎可能抑制效率改进'
   '（据 Wikipedia Payment system）',
   'w-en-payment-system'),
 'proprietary-trading': (
   '风险承担／效益视角',
   '自营交易为公司提供利润来源，并在一定程度上为市场**提供流动性**；'
   '限制自营的批评者认为，全面禁止可能损失这些收益、并可能将业务推向监管更松的领域'
   '（据 Wikipedia Proprietary trading 及沃尔克规则的相关争论）',
   'w-en-proprietary-trading'),
}

for eid, (holder, view, sid) in ADD.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    holders = {s.get('holder') for s in d.get('schools') or []}
    if holder in holders:
        continue
    d.setdefault('schools', []).append({'holder': holder, 'view': view, 'sources': [sid]})
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作MW】补 schools 第二派观点（据现有来源）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('%-24s schools += 1 (共 %d)' % (eid, len(d['schools'])))
