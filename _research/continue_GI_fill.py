# -*- coding: utf-8 -*-
"""续作GI：为薄弱条目补充 timeline / schools / key_data（均取自维基全文）。"""
import json
import os
import glob

ADD = {
 'counterparty-risk': {
   'timeline': [
     {'year': 1974, 'event': '赫斯塔特银行(Herstatt)被德国监管机构吊销牌照，'
                             '因时区错配导致对手方在马克已付、美元未收时暴露损失（据 Wikipedia Settlement risk）'},
     {'year': 1990, 'event': '德崇证券(Drexel)关闭未引发同类问题——英格兰银行设立专门安排确保支付完成'
                             '（据 Wikipedia Settlement risk）'},
   ],
   'schools': [
     ('监管视角', '结算风险源于流程而非当事人意愿——即便双方同意，结算环节本身也可能中断交易，'
                  '因此需中央对手方与净额结算等机制（据 Wikipedia Settlement risk）', 'w-en-counterparty-risk'),
   ],
   'key_data': [
     ('赫斯塔特银行牌照被吊销的日期', 1974, '年6月26日', 1974,
      '原文：On 26 June 1974, the bank\'s license was withdrawn by German regulators at the end of the banking day'),
   ],
 },
 'dividend': {
   'timeline': [
     {'year': 1602, 'event': '荷兰东印度公司(VOC)成立，此后近两百年间支付约占股价 18% 的年度股息'
                             '（据 Wikipedia Dividend）'},
     {'year': 1902, 'event': '加拿大 Burland v Earle 与英国 Bond v Barrow 判例确立"不干预"原则'
                             '（据 Wikipedia Dividend）'},
   ],
   'key_data': [
     ('荷兰东印度公司年度股息占股价比例（约，1602—1800）', 18, '%', 1602,
      '原文：The VOC paid annual dividends worth around 18 percent of the value of its shares for almost 200 years'),
   ],
 },
 'convergence': {
   'timeline': [
     {'year': 1970, 'event': 'Sachs 与 Warner 以 111 国 1970—1989 年数据检验开放与增长的关系'
                             '（据 Wikipedia Convergence (economics)）'},
     {'year': 1992, 'event': 'Barro 与 Sala-i-Martin 区分绝对收敛与条件收敛（据 Wikipedia Convergence (economics)）'},
   ],
   'key_data': [
     ('Sachs-Warner 研究中工业化国家人均年增速', 2.3, '%', 1989,
      '原文：the industrialized countries had a growth of 2.3% per year per capita'),
   ],
 },
 'buyback': {
   'timeline': [
     {'year': 1934, 'event': '美国《证券交易法》第 9(a)(2) 与 10(b) 条成为反操纵的法律基础'
                             '（据 Wikipedia Share repurchase）'},
     {'year': 1981, 'event': '此前所有要约回购均采用固定价格要约；此后引入荷兰式拍卖等方式'
                             '（据 Wikipedia Share repurchase）'},
   ],
 },
 'savings': {
   'schools': [
     ('凯恩斯视角', '储蓄是漏出：个体增储在总量上压低需求，可能使储蓄目标无法实现（节约悖论）'
                    '（据 Wikipedia Saving 与凯恩斯主义通行表述；具体出处待核实）', 'w-en-savings'),
     ('新古典视角', '储蓄是可贷资金的供给，通过利率与投资自动均衡（据 Wikipedia Saving；具体出处待核实）',
      'w-en-savings'),
   ],
 },
 'demand': {
   'schools': [
     ('互补品效应', '完全互补品表现为单一商品；互补品价格上升会使另一商品的需求量下降'
                    '（据 Wikipedia Demand）', 'w-en-demand'),
   ],
 },
 'effective-demand': {
   'schools': [
     ('与名义需求的区别', '有效需求是购买者在其他市场受到约束时实际出现的需求；'
                          '名义需求则不受其他市场配给限制（据 Wikipedia Effective demand）', 'w-en-effective-demand'),
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
        d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作GI】补充 %s。' % '/'.join(added))
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n += 1
        print('%s: +%s' % (eid, '/'.join(added)))

print('\n共更新 %d 个条目' % n)
