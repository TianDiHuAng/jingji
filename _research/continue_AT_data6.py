# -*- coding: utf-8 -*-
"""续作AT：为6个制度/危机案例补充 key_data。"""
import json

DATA = {
 'ems': [
   ('汇率蛇波动区间(初始)', 2.25, '%（±2.25%；1993年8月扩大至±15%）', 1979,
    '原文：established a single currency fluctuation band of +/-2.25% ... broadened ... from +/-2.25% to +/-15%；单一来源待核实。'),
   ('德意通胀差(同期对比)', 13, '%（意大利；德国为3%）', 1992,
    '原文：Germany experienced an inflation rate of 3 percent while Italy\'s inflation rate reached 13 percent；单一来源待核实。'),
 ],
 'nixon-shock': [
   ('美元黄金兑换官价(布雷顿森林)', 35, '美元/盎司', 1971,
    '原文：converted to gold at a fixed exchange rate of $35 per ounce；单一来源待核实。'),
   ('美国持有官方黄金储备(1945)', 574, '百万盎司（5.74亿，占全球过半）', 1945,
    '原文：574 million ounces at the end of World War II；单一来源待核实。'),
   ('美国占全球经济产出份额变化', 27, '%（自35%下降）', 1971,
    '原文：share of global economic output dropped from 35% to 27%；单一来源待核实。'),
 ],
 'emergency-banking-act-1933': [
   ('法案通过日期与银行假日间隔', 3, '天（1933-03-09通过，FDR宣布银行假日后3天）', 1933,
    '原文：passed by Congress on March 9, 1933, three days after FDR declared a nationwide bank holiday；单一来源待核实。'),
   ('一周内回流银行的现金', 1, '十亿美元（10亿）', 1933,
    '原文：Americans returned $1 billion to bank vaults in the following week；单一来源待核实。'),
   ('道指单日上涨(1933-03-15)', 8.26, '点（收于62.10）', 1933,
    '原文：gaining 8.26 points to close at 62.10；单一来源待核实。'),
 ],
 'baring-crisis-1890': [
   ('阿根廷实际GDP降幅(1890–1891)', -11, '%', 1891,
    '原文：its real GDP falling by 11 percent between 1890 and 1891；单一来源待核实。'),
 ],
 'spain-2008': [
   ('西班牙申请的外部救助规模', 100, '十亿欧元（1000亿）', 2012,
    '原文：had to apply for a €100 billion rescue；单一来源待核实。'),
   ('私人部门信贷年均增速(1997–2007)', 17, '%（约）', 2007,
    '原文：Credit to the non-financial private sector grew at an average annual rate of about 17%；单一来源待核实。'),
   ('西班牙GDP增速(2009)', -3.7, '%', 2009,
    '原文：The economy contracted 3.7% in 2009 and again in 2010 by 0.1%；单一来源待核实。'),
 ],
 'drexel': [
   ('德崇证券净利润(1986财年)', 545.5, '百万美元（5.455亿，当时华尔街最高）', 1986,
    '原文：netting $545.5 million, which represented the most profitable year ever for a Wall Street firm at the time；单一来源待核实。'),
   ('米尔肯薪酬(1986)', 295, '百万美元（2.95亿，当时史上最高薪酬）', 1986,
    '原文：Milken ... was paid $295 million, the highest salary that an employee in the modern history of the world had ever received；单一来源待核实。'),
 ],
}

SRC = {
 'ems': 'w-en-european-monetary-system',
 'nixon-shock': 'w-en-nixon-shock',
 'emergency-banking-act-1933': 'w-en-emergency-banking-act-1933',
 'baring-crisis-1890': 'w-en-baring-crisis',
 'spain-2008': 'w-en-spain-2008',
 'drexel': 'w-en-drexel-burnham-lambert',
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r65_data.json', encoding='utf-8'))
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作AT】补关键数据（单源）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', added, '条')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
