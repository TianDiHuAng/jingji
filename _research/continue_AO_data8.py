# -*- coding: utf-8 -*-
"""续作AO：为8个L3核心案例补充 key_data 与专属来源。"""
import json

DATA = {
 'dotcom-bubble-2000': ('w-en-dot-com-bubble', [
   ('纳斯达克涨幅(1995—2000年3月峰值)', 600, '%', 2000,
    '原文：investments in the Nasdaq Composite ... rose by 600%；单一来源待核实。'),
   ('纳斯达克跌幅(2000年3月峰值—2002年10月)', -78, '%（自峰值）', 2002,
    '原文：only to fall 78% from its peak by October 2002；单一来源待核实。'),
   ('思科股价跌幅', -80, '%（自峰值，约）', 2002,
    '原文：Cisco Systems lost ... 80% of its stock value；单一来源待核实。'),
 ]),
 'euro-area-crisis': ('w-en-eurozone-crisis', [
   ('希腊与西班牙失业率峰值', 27, '%（高达）', 2013,
    '原文：increases in unemployment rates to as high as 27% in Greece and Spain；单一来源待核实。'),
   ('希腊2009年预算赤字/GDP(修正后)', 12.7, '%（原预测6—8%；马斯特里赫特上限3%）', 2009,
    '原文：a revision of the forecast for the 2009 budget deficit from "6–8%" ... to 12.7%；单一来源待核实。'),
 ]),
 'hungarian-hyper-1945': ('w-en-hungarian-pengo', [
   ('价格翻倍所需时间(恶性通胀峰值)', 15, '小时（约）', 1946,
    '原文：it took only about 15 hours for prices to double；单一来源待核实。'),
   ('pengő 贬值90%所需时间', 4, '天（约）', 1946,
    '原文：about four days for the pengő to lose 90% of its prior value；单一来源待核实。'),
   ('资本税(1945年12月)', 75, '%', 1945,
    '原文：such as a 75% capital levy in December 1945；单一来源待核实。'),
 ]),
 'mississippi-bubble-1720': ('w-en-john-law-company', [
   ('公开发行面值总额(1717—1718)', 100, '百万里弗（1亿利弗尔）', 1718,
    '原文：a total 100 million French livres at face value；单一来源待核实。'),
   ('月通胀率(1720年1月)', 23, '%（月率）', 1720,
    '原文：Inflation reached a monthly rate of 23% in January 1720；单一来源待核实。'),
   ('法国国家赔偿公司金额', 514, '百万里弗（5.14亿）', 1720,
    '原文：paid the company an indemnity of 514 million livres；单一来源待核实。'),
 ]),
 'panic-1857': ('w-en-panic-of-1857', [
   ('俄亥俄人寿保险信托负债', 7, '百万美元（700万）', 1857,
    '原文：with liabilities, it is said, of $7,000,000；单一来源待核实。'),
   ('谷物价格(1855)', 2.19, '美元/蒲式耳', 1855,
    '原文：grain prices had skyrocketed to $2.19 a bushel；单一来源待核实。'),
   ('谷物价格(1858)', 0.80, '美元/蒲式耳', 1858,
    '原文：grain prices dropped severely to $0.80 a bushel；单一来源待核实。'),
 ]),
 'panic-1873': ('w-en-panic-of-1873', [
   ('英格兰银行加息至', 9, '%', 1873,
    '原文：the Bank of England raised interest rates to 9 percent；单一来源待核实。'),
   ('英国净资本形成/净国民产出(危机后)', 6.0, '%（自11.5%下降）', 1875,
    '原文：the British ratio of net national capital formation to net national product fell from 11.5% to 6.0%；单一来源待核实。'),
   ('德国净资本形成/净国民产出(危机后)', 15.9, '%（自10.6%上升）', 1875,
    '原文：the German ratio rose from 10.6% to 15.9%；单一来源待核实。'),
 ]),
 'venezuela-hyper-2016': ('w-en-hyperinflation-in-venezuela', [
   ('委内瑞拉通胀率(2014)', 69, '%（年率）', 2014,
    '原文：In 2014, the annual inflation rate reached 69%；单一来源待核实。'),
   ('委内瑞拉通胀率(2016)', 800, '%（年率）', 2016,
    '原文：The rate reached 800% in 2016；单一来源待核实。'),
   ('委内瑞拉通胀率(2018)', 1700000, '%（年率，约170万）', 2018,
    '原文：about 1,700,000% in 2018；单一来源待核实。'),
 ]),
 'zimbabwe-hyper-2007': ('w-en-hyperinflation-in-zimbabwe', [
   ('津巴布韦峰值月通胀(2008年11月中)', 790.6, '十亿%（月环比，约7906亿%）', 2008,
    '原文：Zimbabwe\'s peak month of inflation is estimated at 790.6 billion percent month-on-month；单一来源待核实。'),
   ('津巴布韦通胀率(2019年7月)', 175, '%（年率）', 2019,
    '原文：By mid-July 2019, inflation had increased to 175%；单一来源待核实。'),
 ]),
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
NEW = {
 'w-en-dot-com-bubble': ('Dot-com bubble', 'Dot-com_bubble'),
 'w-en-eurozone-crisis': ('Eurozone crisis', 'Eurozone_crisis'),
 'w-en-hungarian-pengo': ('Hungarian pengő', 'Hungarian_peng%C5%91'),
 'w-en-john-law-company': ("John Law's Company", 'John_Law%27s_Company'),
 'w-en-panic-of-1857': ('Panic of 1857', 'Panic_of_1857'),
 'w-en-panic-of-1873': ('Panic of 1873', 'Panic_of_1873'),
 'w-en-hyperinflation-in-venezuela': ('Hyperinflation in Venezuela', 'Hyperinflation_in_Venezuela'),
 'w-en-hyperinflation-in-zimbabwe': ('Hyperinflation in Zimbabwe', 'Hyperinflation_in_Zimbabwe'),
}
for sid, (title, slug) in NEW.items():
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': title, 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科', 'url': 'https://en.wikipedia.org/wiki/' + slug, 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'Wikipedia API(full extract)核对(本会话抓取全文)'
    })
    ex.add(sid)
    print('新增来源', sid)

for eid, (sid, kds) in DATA.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if sid not in d['sources']:
        d['sources'] = [sid] + [s for s in d['sources']]
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作AO】补关键数据（单源，据专属维基页面全文；跨源核实待完成）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', added, '条 key_data')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
