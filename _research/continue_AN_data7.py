# -*- coding: utf-8 -*-
"""续作AN：为7个L3核心案例补充 key_data 与专属来源（据本次抓取的页面全文，单源标注待核实）。"""
import json

# 案例 id -> (专属来源id, [key_data...])
DATA = {
 'japan-asset-bubble-1990': ('w-en-japanese-asset-price-bubble', [
   ('日本官方贴现率(1987年2月)', 2.5, '%（降至）', 1987,
    '原文：slashed the official discount rate to as low as 2.5% by February 1987；单一来源待核实。'),
   ('东京商业区地价涨幅(较1985)', 122, '%（约）', 1987,
    '原文：jumped approximately 122% (compared to 1985)；单一来源待核实。'),
   ('东京住宅区地价涨幅(较1985)', 45, '%', 1987,
    '原文：recorded an increase of 45% (compared to 1985)；单一来源待核实。'),
 ]),
 'argentina-crisis-2001': ('w-en-argentine-economic-crisis', [
   ('阿根廷年均月通胀(1975–1988)', 10, '%（月均，约合年220%）', 1980,
    '原文：inflation, which had already averaged 10% per month (220% per year) from 1975 to 1988；单一来源待核实。'),
   ('预算赤字/GDP', 15, '%（占GDP）', 1983,
    '原文：Budget deficits jumped to 15% of GDP；单一来源待核实。'),
   ('国家接管的私人债务', 15, '十亿美元（>150亿美元）', 1982,
    '原文：state takeover of over $15 billion in private debts；单一来源待核实。'),
 ]),
 'latin-american-debt-1975': ('w-en-latin-american-debt-crisis', [
   ('拉美外债(1975)', 75, '十亿美元（750亿）', 1975,
    '原文：from US$75 billion in 1975；单一来源待核实。'),
   ('拉美外债(1983)', 315, '十亿美元（>3150亿，约占区域GDP50%）', 1983,
    '原文：to more than $315 billion in 1983, or 50 percent of the region GDP；单一来源待核实。'),
   ('偿债额(1982)', 66, '十亿美元（660亿；1975年为120亿）', 1982,
    '原文：reaching $66 billion in 1982, up from $12 billion in 1975；单一来源待核实。'),
 ]),
 'greek-debt-crisis': ('w-en-greek-government-debt-crisis', [
   ('希腊政府债务(2009)', 300, '十亿欧元（3000亿）', 2009,
    '原文：Between 2009–2017, the Greek government debt rose from €300bn to €318bn；单一来源待核实。'),
   ('希腊债务/GDP(2009)', 127, '%（占GDP）', 2009,
    '原文：the Greek debt-to-GDP ratio rose up from 127% to 179%；单一来源待核实。'),
   ('希腊债务/GDP(2017)', 179, '%（占GDP）', 2017,
    '原文：rose up from 127% to 179%, due to the severe GDP drop；单一来源待核实。'),
 ]),
 'mexican-peso-1994': ('w-en-mexican-peso-crisis', [
   ('墨西哥通胀(危机期)', 52, '%（约）', 1995,
    '原文：The Mexican economy experienced inflation of around 52%；单一来源待核实。'),
   ('美国组织的救助规模', 50, '十亿美元（500亿，1995年1月）', 1995,
    '原文：The United States organized a $50 billion bailout for Mexico in January 1995；单一来源待核实。'),
   ('比索贬值幅度(1994-12-20宣布)', 15, '%（13%—15%，取上限）', 1994,
    '原文：announced the Mexican central bank devaluation of the peso between 13% and 15%；单一来源待核实。'),
 ]),
 'oil-crisis-1973': ('w-en-1973-oil-crisis', [
   ('油价涨幅(至1974年3月)', 300, '%（近300%；3美元/桶→近12美元/桶）', 1974,
    '原文：the price of oil had risen by nearly 300%: from US$3/barrel to nearly US$12/barrel；单一来源待核实。'),
   ('美国产量占全球(1973)', 16, '%', 1973,
    '原文：In 1973, US production had declined to 16% of global output；单一来源待核实。'),
 ]),
 'panic-1907': ('w-en-panic-of-1907', [
   ('美股跌幅(1906年1—7月)', 18, '%', 1906,
    '原文：From their peak in January, stock prices declined 18% by July 1906；单一来源待核实。'),
   ('美股总市值损失(1906-09—1907-03)', 7.7, '%', 1907,
    '原文：Between September 1906 and March 1907, the stock market slid, losing 7.7% of its capitalization；单一来源待核实。'),
   ('美股跌幅(1907-03-09—26)', 9.8, '%', 1907,
    '原文：Between March 9 and 26, stocks fell a further 9.8%；单一来源待核实。'),
 ]),
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}

# 补缺失来源
if 'w-en-argentine-economic-crisis' not in ex:
    sd['sources'].append({
        'id': 'w-en-argentine-economic-crisis', 'title': '1998–2002 Argentine great depression',
        'author': 'Wikipedia contributors', 'year': '2026', 'type': '权威百科',
        'url': 'https://en.wikipedia.org/wiki/1998%E2%80%932002_Argentine_great_depression',
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'Wikipedia API(full extract)核对(本会话抓取全文)'
    })
    ex.add('w-en-argentine-economic-crisis')
    print('新增来源 w-en-argentine-economic-crisis')

for eid, (sid, kds) in DATA.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if sid not in d['sources']:
        d['sources'] = [sid] + [s for s in d['sources']]
    have = {k.get('label') for k in d.get('key_data', [])}
    for lab, val, unit, yr, note in kds:
        if lab in have:
            continue
        d.setdefault('key_data', []).append({
            'label': lab, 'value': val, 'unit': unit, 'year': yr,
            'comparable_price': False, 'note': note, 'sources': [sid]})
    d['needs_verification'] = True
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作AN】补关键数据（单源，据专属维基页面全文；跨源核实待完成）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', len(kds), '条 key_data')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
