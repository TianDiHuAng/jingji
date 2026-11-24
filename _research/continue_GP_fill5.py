# -*- coding: utf-8 -*-
"""续作GP：为最后 5 个薄弱条目补充 timeline/schools/key_data。"""
import json
import os

ADD = {
 'property-rights': {
   'timeline': [
     {'year': 1689, 'event': '洛克《政府论二篇》提出最有影响的自然权利产权论述之一'
                             '（据 Wikipedia Property rights (economics)）'},
     {'year': 2013, 'event': '一项研究发现更好的产权保护可影响多项发展结果，包括自然资源管理'
                             '（据 Wikipedia Property rights (economics)）'},
   ],
   'schools': [
     ('洛克式劳动理论', '产权源于对自己劳动成果的自然权利（据 Wikipedia Property rights (economics)）',
      'w-en-property-rights'),
     ('发展与契约视角', '产权界定与执行影响投资激励；但不完全契约意味着产权无法穷尽所有情形，'
                        '剩余控制权的配置本身成为关键（据 Wikipedia Property rights (economics)）',
      'w-en-property-rights'),
   ],
 },
 'specialization': {
   'timeline': [
     {'year': 1714, 'event': '曼德维尔在《蜜蜂的寓言》第二卷讨论分工'
                             '（据 Wikipedia Division of labour）'},
     {'year': 1776, 'event': '斯密《国富论》开篇以扣针工厂说明分工提高生产率'
                             '（据 Wikipedia Division of labour）'},
   ],
 },
 'mutual-fund': {
   'timeline': [
     {'year': 1774, 'event': '为应对 1772—73 年金融危机，阿姆斯特丹商人 van Ketwich 设立信托 '
                             'Eendragt Maakt Magt（"团结就是力量"），被视为共同基金雏形'
                             '（据 Wikipedia Mutual fund History）'},
   ],
   'key_data': [
     ('全球开放式共同基金资产（2023年底）', 69, '万亿美元', 2023,
      '原文：At the end of 2023, open-end mutual fund assets worldwide were $69.0 trillion'),
   ],
 },
 'nasdaq': {
   'key_data': [
     ('纳斯达克上市公司数（2024年底）', 4075, '家', 2024,
      '原文：As of December 31, 2024, 4,075 companies listed securities on Nasdaq'),
   ],
 },
 'labour-market': {
   'timeline': [
     {'year': 2010, 'event': '1990—2010 年间的重要研究进展是动态搜寻—匹配—议价框架的发展'
                             '（据 Wikipedia Labour economics）'},
   ],
   'schools': [
     ('搜寻匹配视角', '劳动市场并非无摩擦的拍卖市场：岗位与工人需要相互搜寻、匹配并议价，'
                      '因此摩擦性失业是常态而非异常（据 Wikipedia Labour economics）',
      'w-en-labour-market'),
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
        d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作GP】补充 %s。' % '/'.join(added))
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n += 1
        print('%s: +%s' % (eid, '/'.join(added)))

import glob
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
thin = [e['id'] for e in es if not (e.get('timeline') or e.get('schools'))]
print('\n共更新 %d | 仍缺 timeline/schools: %d %s' % (n, len(thin), thin))
