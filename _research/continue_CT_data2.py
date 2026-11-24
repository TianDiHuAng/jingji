# -*- coding: utf-8 -*-
"""续作CT：为 gold-reserve-act-1934 与 northern-rock 补关键数据。"""
import json

KD = {
 'gold-reserve-act-1934': ('w-en-gold-reserve-act',
   [('黄金法定价格(法案前)', 20.67, '美元/金衡盎司', 1933,
     '原文：changed the statutory price of gold from $20.67 per troy ounce to $35；单一来源待核实。'),
    ('黄金法定价格(法案后)', 35, '美元/金衡盎司（重估）', 1934,
     '原文：Immediately following passage of the Act, the President revalued the price of gold to $35 per troy ounce；单一来源待核实。'),
    ('美国GNP年均增速(1933–1937)', 8, '%（超过8%）', 1937,
     '原文：Between 1933 and 1937 the GNP in the United States grew at an average rate of over 8 percent；单一来源待核实。'),
    ('美国M1年均增速(1933–1937)', 10, '%', 1937,
     '原文：M1 ... grew at an average rate of 10 percent per year between 1933 and 1937；单一来源待核实。')]),
 'northern-rock': ('w-en-northern-rock',
   [('北岩银行英格兰银行借款峰值', 26.9, '十亿英镑（269亿）', 2007,
     '原文：owing a net balance of only £8.9 billion of the loan which stood at £26.9 billion at the end [of the year]；借款峰值年份待核实。'),
    ('借款余额(2009-03-03)', 8.9, '十亿英镑（89亿，提前偿还）', 2009,
     '原文：As of 3 March 2009, the bank was repaying the loan well ahead of target, owing a net balance of only £8.9 billion；单一来源待核实。')]),
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r105_data.json', encoding='utf-8'))

for eid, (sid, kds) in KD.items():
    if sid not in ex:
        v = meta.get(eid)
        if v:
            sd['sources'].append({'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors',
              'year': '2026', 'type': '权威百科',
              'url': 'https://en.wikipedia.org/wiki/' + v['title'].replace(' ', '_').replace('–','%E2%80%93'),
              'url2': None, 'verified': True, 'link_ok': True,
              'note': 'Wikipedia API(full extract)核对(本会话抓取)'})
            ex.add(sid)
            print('新增来源', sid, '|', v['title'])
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if sid not in d['sources']:
        d['sources'].append(sid)
    have = {k['label'] for k in d.get('key_data', [])}
    for lab, val, unit, yr, note in kds:
        if lab in have:
            continue
        d.setdefault('key_data', []).append({'label': lab, 'value': val, 'unit': unit, 'year': yr,
                                             'comparable_price': False, 'note': note, 'sources': [sid]})
    d['pending_notes'] = d.get('pending_notes', '') + ' 【续作CT】补充关键数据。'
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', len(kds), '条')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
