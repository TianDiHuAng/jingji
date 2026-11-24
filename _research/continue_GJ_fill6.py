# -*- coding: utf-8 -*-
"""续作GJ：为 6 个薄弱条目补充 timeline/schools/key_data/policy_response。"""
import json
import os

ADD = {
 'toxic-assets': {
   'timeline': [
     {'year': 2006, 'event': '该词至少早在 2006 年已有限使用；可能由 Countrywide Financial 创始人 '
                             'Angelo Mozilo 在当年春季的邮件中首创或推广（经 SEC 文件披露）'
                             '（据 Wikipedia Toxic asset）'},
     {'year': 2009, 'event': '3月23日美国财长盖特纳宣布"公私合营投资计划"(PPIP) 以购买银行的有毒资产'
                             '（据 Wikipedia Toxic asset）'},
   ],
   'key_data': [
     ('PPIP 宣布当日美股主要指数涨幅（以上）', 6, '%', 2009,
      '原文：The major stock market indexes in the United States rallied on the day of the announcement, rising by over six percent'),
   ],
   'policy_response': [{
     'holder': '美国财政部（2009）',
     'view': ('2009年3月23日财长盖特纳宣布**公私合营投资计划(PPIP)** 以从银行购买有毒资产。'
              '宣布当日美国主要股指上涨**超过 6%**，银行股领涨。'
              '该计划的核心难题是**定价**：价格过低会使银行资不抵债，过高则由纳税人承担损失。'),
     'basis': '据 Wikipedia「Toxic asset」Geithner attempt at bail-out 章节；效果评价待核实',
     'sources': ['w-en-toxic-assets'],
   }],
 },
 'rent-seeking': {
   'timeline': [
     {'year': 1817, 'event': '李嘉图在"地租"的狭义上使用 rent 一词（据 Wikipedia Rent-seeking）'},
     {'year': 1967, 'event': '塔洛克发表论文，使寻租成为经济学与政治学的持续研究对象'
                             '（据 Wikipedia Rent-seeking）'},
     {'year': 1980, 'event': '学界开始批评寻租理论——质疑"浪费资源"概念的模糊性与假设的可靠性'
                             '（据 Wikipedia Rent-seeking）'},
   ],
   'schools': [
     ('塔洛克悖论', '寻租者为获得政治好处所付出的成本**远低于**该好处对其的价值——'
                    '这一"低成本高收益"的落差本身构成一个待解释的悖论（据 Wikipedia Rent-seeking）',
      'w-en-rent-seeking'),
     ('批评者（1980年代）', '批评者认为寻租理论把"生产率"定义为纯物理属性，'
                            '忽略了围绕财产权的权利安排；且"浪费资源"的界定存在模糊性'
                            '（据 Wikipedia Rent-seeking Criticism of theories）', 'w-en-rent-seeking'),
   ],
 },
 'transaction-cost': {
   'timeline': [
     {'year': 1931, 'event': '制度经济学家 John R. Commons 提出以"交易"而非商品或个人作为经济理论的基础'
                             '（据 Wikipedia Transaction cost）'},
     {'year': 1996, 'event': '威廉姆森在《治理机制》中系统列出交易成本经济学与新古典微观经济学的分歧'
                             '（据 Wikipedia Transaction cost）'},
   ],
   'schools': [
     ('交易成本经济学（威廉姆森）', '拒绝"工具理性"假设及其对行为的预测含义，'
                                    '认为有限理性与机会主义使治理结构（市场/企业/混合）成为关键变量'
                                    '（据 Wikipedia Transaction cost）', 'w-en-transaction-cost'),
     ('新古典微观经济学', '以工具理性与完全信息为基准，把交易本身视为无摩擦，'
                          '因此不把治理结构作为分析对象（据 Wikipedia Transaction cost）', 'w-en-transaction-cost'),
   ],
 },
 'tax-incidence': {
   'schools': [
     ('弹性决定归宿（一般规则）', '需求曲线越**陡**、供给曲线越**平**，消费者承担的税负越多；反之则生产者承担更多'
                                  '（据 Wikipedia Tax incidence）', 'w-en-tax-incidence'),
     ('供给无弹性、需求有弹性', '生产者无论价格如何都生产相同数量，消费者对价格高度敏感——'
                                '此时税负主要落在**生产者**身上（据 Wikipedia Tax incidence）', 'w-en-tax-incidence'),
   ],
 },
 'junk-bond': {
   'schools': [
     ('违约风险视角', '高收益债的低评级反映更高的违约可能，投资者因此要求更高的收益率作为补偿'
                      '（据 Wikipedia High-yield debt）', 'w-en-junk-bond'),
     ('再打包视角', '高收益债可被打包成 **CDO**，使其优先级分层的评级**高于原始债务**，'
                    '从而满足养老金等机构投资者的最低评级要求——这扩大了风险的市场分布'
                    '（据 Wikipedia High-yield debt）', 'w-en-junk-bond'),
   ],
 },
 'prisoners-dilemma': {
   'timeline': [
     {'year': 1950, 'event': '囚徒困境由梅里尔·弗勒德与梅尔文·德雷希尔提出，后由塔克形式化'
                             '（据 Wikipedia Prisoner\'s dilemma）'},
     {'year': 1984, 'event': '阿克塞尔罗德在《合作的演化》中报告重复囚徒困境锦标赛，'
                             '"针锋相对"(tit-for-tat) 表现突出（据 Wikipedia Prisoner\'s dilemma）'},
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
    if upd.get('policy_response') and not d.get('policy_response'):
        d['policy_response'] = upd['policy_response']
        added.append('policy_response')
    if added:
        d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作GJ】补充 %s。' % '/'.join(added))
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n += 1
        print('%s: +%s' % (eid, '/'.join(added)))
print('\n共更新 %d 个条目' % n)
