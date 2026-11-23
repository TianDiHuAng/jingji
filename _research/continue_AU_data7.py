# -*- coding: utf-8 -*-
"""续作AU：为7个重要级案例补充 key_data。"""
import json

DATA = {
 'crisis-1914': [
   ('外国组合投资抛售规模(1914)', 3, '十亿美元（约30亿）', 1914,
    '原文：the sell-off of about $3 billion ... of foreign portfolio investments；单一来源待核实。'),
   ('英格兰银行贴现率上调(1914-08-01)', 10, '%（7-30自3%升至4%，7-31升8%，8-1升10%）', 1914,
    '原文：raised the bank rate from 3% to 4% on July 30, to 8% on July 31, and then to 10% on August 1；单一来源待核实。'),
 ],
 'crisis-third-century': [
   ('亚历山大城人口降幅(249–262)', -62, '%（塞浦路斯瘟疫）', 262,
    '原文：some cities, such as the city of Alexandria, experienced a 62% decline in population；单一来源待核实。'),
   ('粮价涨幅(半世纪)', 200000, '%', 284,
    '原文：grain prices rose by 200,000% in half a century；单一来源待核实。'),
 ],
 'shanghai-rubber-1910': [
   ('橡胶股票投资总额(1910)', 60, '百万两（6000万两；中国人持70—80%）', 1910,
    '原文：the total of investments was 60 million Tael, in which the Chinese people held the 70%-80% of stocks；单一来源待核实。'),
   ('外国银行规定的抵押贴现率', 80, '%（区间50%—80%，取上限）', 1910,
    '原文：the foreign banks announced to regulate mortgage discount at the level of 50%-80%；单一来源待核实。'),
 ],
 'south-america-2002': [
   ('阿根廷GDP增速(2002)', -10.9, '%（2000年−0.8%、2001年−4.4%、1999年−3.4%）', 2002,
    '原文：GDP continued to decline: 0.8% in 2000, 4.4% in 2001, and 10.9% in 2002；单一来源待核实。'),
 ],
 'stock-crash-1973': [
   ('主要股指名义跌幅(1973–74)', -34, '%（至少）', 1974,
    '原文：having lost at least 34% of their value in nominal terms；单一来源待核实。'),
   ('主要股指实际跌幅(1973–74)', -43, '%（实际值）', 1974,
    '原文：and 43% in real terms；单一来源待核实。'),
   ('美国实际GDP增速(1974)', -2.1, '%（1972年为7.2%）', 1974,
    '原文：the American economy slowed from 7.2% real GDP growth to −2.1% contraction；单一来源待核实。'),
 ],
 'venezuela-crisis-2013': [
   ('人口贫困率(2021)', 95, '%（其中77%为极端贫困）', 2021,
    '原文：95% of the population by 2021 was living in poverty, and 77% lived under extreme poverty；单一来源待核实。'),
   ('外流人口(2024)', 7.7, '百万人（770万；2021年为540万）', 2024,
    '原文：7.7 million had emigrated by 2024；单一来源待核实。'),
 ],
 'silicon-valley-bank': [
   ('挤兑提款额(2023-03-09)', 42, '十亿美元（420亿，次日）', 2023,
    '原文：customers withdrew funds totaling $42 billion by the following day；单一来源待核实。'),
   ('未保险存款占比(2023)', 89, '%（占1720亿美元存款负债）', 2023,
    '原文：About 89 percent of the bank\'s $172 billion in deposit liabilities exceeded the maximum insured by the FDIC；单一来源待核实。'),
 ],
}

SRC = {
 'crisis-1914': 'w-en-financial-crisis-1914',
 'crisis-third-century': 'w-en-crisis-third-century',
 'shanghai-rubber-1910': 'w-en-shanghai-rubber-1910',
 'south-america-2002': 'w-en-south-america-2002',
 'stock-crash-1973': 'w-en-1973-1974-stock-crash',
 'venezuela-crisis-2013': 'w-en-crisis-in-venezuela',
 'silicon-valley-bank': 'w-en-collapse-of-svb',
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r66_data.json', encoding='utf-8'))
for eid, sid in SRC.items():
    if sid in ex:
        continue
    t = meta.get(eid, {}).get('title')
    if not t:
        continue
    sd['sources'].append({
        'id': sid, 'title': t, 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科',
        'url': 'https://en.wikipedia.org/wiki/' + t.replace(' ', '_').replace('–', '%E2%80%93'),
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'Wikipedia API(full extract)核对(本会话抓取全文)'
    })
    ex.add(sid)
    print('新增来源', sid, '|', t)

for eid, kds in DATA.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    sid = SRC[eid]
    if sid in ex and sid not in d['sources']:
        d['sources'] = [sid] + list(d['sources'])
    have = {k.get('label') for k in d.get('key_data', [])}
    added = 0
    for lab, val, unit, yr, note in kds:
        if lab in have:
            continue
        d.setdefault('key_data', []).append({
            'label': lab, 'value': val, 'unit': unit, 'year': yr,
            'comparable_price': False, 'note': note, 'sources': [sid]})
        added += 1
    d['needs_verification'] = True
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作AU】补关键数据（单源）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', added, '条')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
