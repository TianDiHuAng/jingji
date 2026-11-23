# -*- coding: utf-8 -*-
"""续作AQ：为17个重要级案例补充 key_data（据抓取全文，单源标注）。"""
import json

DATA = {
 'covid-crash-2020': [
   ('全球股市单日最大跌幅(2020-03-16)', -13, '%（12—13%，"黑色星期一II"）', 2020,
    '原文：the largest drop was on 16 March, nicknamed "Black Monday II" of 12–13%；单一来源待核实。'),
   ('10年期美债收益率(低位)', 1.54, '%', 2020,
    '原文：the yields on 10-year and 30-year U.S. Treasury securities fell to 1.54% and 1.99%；单一来源待核实。'),
 ],
 'china-2015-turbulence': [
   ('上证三周跌幅(至2015-07-09)', -30, '%（1400家公司停牌，过半上市）', 2015,
    '原文：the Shanghai stock market had fallen 30 percent over three weeks as 1,400 companies ... filed for a trading halt；单一来源待核实。'),
   ('上证单日跌幅(2015-08-24)', -8.48, '%（2007年以来最大）', 2015,
    '原文：the Shanghai index fell again by 8.48 percent on 24 August, marking the largest fall since 2007；单一来源待核实。'),
 ],
 'terra-luna-2022': [
   ('Anchor Protocol 提供的收益率', 19.45, '%', 2022,
    '原文：Investors who deposited UST in the Anchor Protocol were receiving a 19.45% yield；单一来源待核实。'),
   ('LFG 崩盘前持有的比特币储备价值', 2.4, '十亿美元（80,394枚BTC，约$2.4bn）', 2022,
    '原文：LFG held reserves of 80,394 bitcoin worth approximately $2.4 billion；单一来源待核实。'),
 ],
 'bond-crisis-1994': [
   ('全球债券市值损失', 1.5, '万亿美元（$1.5 trillion）', 1994,
    '原文：About $1.5 trillion in lost market value across the globe；单一来源待核实。'),
   ('美联储首次加息(1994)', 3.25, '%（联邦基金利率目标，自3%上调）', 1994,
    '原文：raise its federal funds rate target from 3% to 3.25%；单一来源待核实。'),
 ],
 'credit-suisse-2023': [
   ('瑞银收购瑞信对价', 3, '十亿瑞郎（CHF 3bn ≈ US$3.2bn）', 2023,
    '原文：agreed to buy Credit Suisse for CHF 3 billion (US$3.2 billion)；单一来源待核实。'),
   ('被减记至零的AT1债券', 16, '十亿瑞郎（CHF 16bn ≈ US$17.2bn）', 2023,
    '原文：CHF 16 billion (US$17.2 billion) of Additional Tier 1 (AT1) bonds were written down to zero；单一来源待核实。'),
 ],
 'bear-stearns': [
   ('衍生品名义合约规模(2007)', 13.4, '万亿美元（其中上市期货1.85万亿）', 2007,
    '原文：notional contract amounts of approximately $13.40 trillion in derivative financial instruments；单一来源待核实。'),
   ('第3层资产 vs 净权益(2007财年末)', 28, '十亿美元（level 3 资产>280亿；净权益仅111亿）', 2007,
    '原文：carrying more than $28 billion in level 3 assets ... versus a net equity position of only $11.1 billion；单一来源待核实。'),
 ],
 'enron': [
   ('安然资产规模(破产时)', 63.4, '十亿美元（当时美国最大企业破产）', 2001,
    '原文：Enron\'s $63.4 billion in assets made it the largest corporate bankruptcy in U.S.；单一来源待核实。'),
   ('股东诉讼索赔与获赔', 40, '十亿美元（索赔；最终部分获赔72亿）', 2002,
    '原文：Shareholders filed a $40 billion lawsuit, for which they were eventually partially compensated $7.2 billion；单一来源待核实。'),
 ],
 'worldcom': [
   ('世通虚增资产规模', 11, '十亿美元（超110亿，当时美国史上最大会计欺诈）', 2002,
    '原文：WorldCom had overstated its assets by over $11 billion；单一来源待核实。'),
   ('内部审计发现的虚假分录', 3.8, '十亿美元（超38亿）', 2002,
    '原文：identified over $3.8 billion in fraudulent balance sheet entries；单一来源待核实。'),
 ],
 'argentina-2018': [
   ('阿根廷年通胀率(危机期)', 30, '%（超过30%）', 2018,
    '原文：the annual inflation rate was over 30 percent；单一来源待核实。'),
   ('政府预算赤字', -8, '%（占GDP，赤字8%）', 2018,
    '原文：The government budget balance had an 8% deficit；单一来源待核实。'),
 ],
 'turkey-2001': [
   ('外资撤离规模', 70, '十亿美元（700亿）', 2001,
    '原文：they withdrew $70 billion worth of capital from the country；单一来源待核实。'),
   ('IMF 提供的贷款(2000年11月)', 11.4, '十亿美元（114亿）', 2000,
    '原文：In November 2000, the IMF provided Turkey with $11.4 billion in loans；单一来源待核实。'),
 ],
 'egypt-2023': [
   ('与阿联酋的Ras el-Hekma开发协议', 35, '十亿美元（另加IMF等220亿支持）', 2024,
    '原文：A $35 billion deal with the United Arab Emirates ... along with $22 billion in support from the IMF；单一来源待核实。'),
   ('贸易逆差峰值(2014–2015)', 39.1, '十亿美元（391亿）', 2015,
    '原文：recording a peak trade deficit in 2014–2015 at US$39.1 billion；单一来源待核实。'),
 ],
 'lebanese-liquidity-2019': [
   ('本币贬值幅度(2023-01—2024-03)', -98, '%（超98%）', 2024,
    '原文：The currency was devalued by over 98% between January 2023 and March 2024；单一来源待核实。'),
   ('年通胀率(2023)', 221.3, '%', 2023,
    '原文：with an annual inflation rate of 221.3% in 2023；单一来源待核实。'),
 ],
 'puerto-rico-debt-2014': [
   ('波多黎各债券债务(2018年报告)', 74, '十亿美元（740亿）', 2018,
    '原文：the Commonwealth had $74 billion in bond debt；单一来源待核实。'),
   ('国民总收入变动(2007—2017)', -14, '%', 2017,
    '原文：Puerto Rico\'s gross national income declined by 14 percent；单一来源待核实。'),
 ],
 'china-realestate-2020': [
   ('恒大负债规模', 2, '万亿元人民币（约3100亿美元）', 2021,
    '原文：were owed 2 trillion RMB (310 billion USD) by Evergrande；单一来源待核实。'),
   ('恒大土地储备可容纳人口(2020)', 1000, '万人', 2020,
    '原文：Evergrande\'s land reserves alone were large enough to house 10 million people in 2020；单一来源待核实。'),
 ],
 'oil-price-war-2020': [
   ('油价季度跌幅(2020Q1)', -65, '%', 2020,
    '原文：facilitated a 65% quarterly fall in the price of oil；单一来源待核实。'),
   ('美国油价跌幅(2020年3月头几周)', -34, '%', 2020,
    '原文：US oil prices fell by 34%, crude oil fell by 26%, and Brent oil fell by 24%；单一来源待核实。'),
 ],
 'gamestop-2021': [
   ('做空比例(2021年1月)', 140, '%（占流通股）', 2021,
    '原文：Approximately 140 percent of GameStop\'s public float had been sold short；单一来源待核实。'),
   ('股价峰值(2021-01-28盘前)', 500, '美元/股（拆股调整后125美元，近30倍）', 2021,
    '原文：stock price to reach a pre-market value of over US$500 per share ($125 split-adjusted), nearly 30 ti...；单一来源待核实。'),
 ],
}

SRC = {
 'covid-crash-2020': 'w-en-2020-stock-market-crash',
 'china-2015-turbulence': 'w-en-china-2015-turbulence',
 'terra-luna-2022': 'w-en-terra-luna-2022',
 'bond-crisis-1994': 'w-en-bond-crisis-1994',
 'credit-suisse-2023': 'w-en-credit-suisse-2023',
 'bear-stearns': 'w-en-bear-stearns',
 'enron': 'w-en-enron',
 'worldcom': 'w-en-worldcom',
 'argentina-2018': 'w-en-argentina-2018',
 'turkey-2001': 'w-en-turkey-2001',
 'egypt-2023': 'w-en-egypt-2023',
 'lebanese-liquidity-2019': 'w-en-lebanese-liquidity-crisis',
 'puerto-rico-debt-2014': 'w-en-puerto-rican-debt-crisis',
 'china-realestate-2020': 'w-en-china-realestate-2020',
 'oil-price-war-2020': 'w-en-oil-price-war-2020',
 'gamestop-2021': 'w-en-gamestop-2021',
 'northern-rock': 'w-en-northern-rock',
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r62_data.json', encoding='utf-8'))
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作AQ】补关键数据（单源）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', added, '条')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
