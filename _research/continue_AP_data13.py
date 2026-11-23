# -*- coding: utf-8 -*-
"""续作AP：为13个重要级案例补充 key_data（据本次抓取全文，单源标注）。"""
import json

DATA = {
 'black-wednesday-1992': [
   ('英国基准利率上调(1992-09-16)', 12, '%（自10%上调）', 1992,
    '原文：announced an increase in the base interest rate, from an already high 10%, to 12%；单一来源待核实。'),
   ('英镑加入ERM的中心汇率(1990-10-08)', 2.95, '德国马克/英镑', 1990,
    '原文：Thatcher entered the pound into the ERM at DM 2.95 to £1；单一来源待核实。'),
 ],
 'russian-1998': [
   ('GKO 国债利率(1998年6月)', 150, '%', 1998,
    '原文：Kiriyenko hiked GKO interest rates to 150%；单一来源待核实。'),
   ('车臣战争花费与赤字', 5.5, '十亿美元（战费；预算赤字近GDP10%）', 1996,
    '原文：the war in Chechnya cost Russia $5.5 billion, causing budget deficits close to 10% of their GDP；单一来源待核实。'),
 ],
 'savings-loan-1986': [
   ('被关闭储贷机构数', 1043, '家（持有5190亿美元资产）', 1995,
    '原文：The two agencies closed 1,043 banks that held $519 billion in assets；单一来源待核实。'),
   ('纳税人总成本(至1999年底)', 123.8, '十亿美元（另加储贷业291亿损失）', 1999,
    '原文：The total cost of taxpayers by the end of 1999 was $123.8 billion；单一来源待核实。'),
 ],
 'icelandic-crisis-2008': [
   ('冰岛外债/GDP(2008年二季度)', 7, '倍（外债9.553万亿克朗≈500亿欧元，>7倍）', 2008,
    '原文：external debt was 9.553 trillion Icelandic krónur (€50 billion), more than 7 times the GDP of Iceland in 2007；单一来源待核实。'),
   ('三大银行资产/GDP', 11, '倍（14.437万亿克朗，>11倍）', 2008,
    '原文：The assets of the three banks totaled 14.437 trillion krónur ... equal to more than 11 times the national GDP；单一来源待核实。'),
 ],
 'cypriot-2013': [
   ('超10万欧元存款被征收比例', 47.5, '%', 2013,
    '原文：47.5% of all bank deposits above €100,000 were seized；单一来源待核实。'),
   ('商业地产价值跌幅', -30, '%（约）', 2013,
    '原文：Commercial property values declined by approximately 30%；单一来源待核实。'),
 ],
 'russian-crisis-2014': [
   ('俄罗斯GDP增速(2015)', -3.7, '%', 2015,
    '原文：Russian GDP contracted 3.7% in 2015；单一来源待核实。'),
   ('央行政策利率(2014年12月)', 17, '%（自8月8%上调）', 2014,
    '原文：sharply increased interest rates from 8% in August to 17% in December；单一来源待核实。'),
   ('资本外流(2014)', 154, '十亿美元（1540亿）', 2014,
    '原文：Capital outflows of $154B；单一来源待核实。'),
 ],
 'sri-lanka-crisis-2019': [
   ('外汇储备(2022年3月)', 1.9, '十亿美元（19亿）', 2022,
    '原文：the remaining foreign exchange reserves of US$1.9 billion as of March 2022；单一来源待核实。'),
   ('2022年到期偿还总额', 8.6, '十亿美元（86亿）', 2022,
    '原文：Sri Lanka had a total of $8.6 billion in repayments due in 2022；单一来源待核实。'),
 ],
 'oil-crisis-1979': [
   ('全球石油供应降幅', -4, '%（约）', 1979,
    '原文：the global oil supply only decreased by approximately four percent；单一来源待核实。'),
   ('原油均价(1979-04-05)', 15.85, '美元/桶', 1979,
    '原文：the average price of crude oil was US$15.85 per barrel；单一来源待核实。'),
 ],
 'recession-1920-1921': [
   ('衰退持续时长', 18, '个月（1920年1月—1921年7月，NBER）', 1921,
    '原文：The recession lasted from January 1920 to July 1921, or 18 months, according to NBER；单一来源待核实。'),
 ],
 'recession-1937-1938': [
   ('衰退持续时长', 13, '个月', 1938,
    '原文：lasting for 13 months through most of 1938；单一来源待核实。'),
   ('工业生产降幅', -30, '%（近30%）', 1938,
    '原文：Industrial production declined almost 30 percent；单一来源待核实。'),
   ('失业率(1938年6月)', 19.0, '%（自1937年5月14.3%上升）', 1938,
    '原文：Unemployment jumped from 14.3% in May 1937 to 19.0% in June 1938；单一来源待核实。'),
 ],
 'panic-1792': [
   ('银行股认购凭证(scrip)价格峰值', 280, '美元（面值认购25美元起）', 1792,
    '原文：prices for scrips increased dramatically ... reaching $280 in New York；单一来源待核实。'),
 ],
 'black-friday-1869': [
   ('政府释放黄金规模(1869年9月)', 4, '百万美元（400万）', 1869,
    '原文：ordering the release of $4 million in government gold on September；单一来源待核实。'),
 ],
}

# 案例 id -> 专属来源 id
SRC = {
 'black-wednesday-1992': 'w-en-black-wednesday',
 'russian-1998': 'w-en-1998-russian-financial-crisis',
 'savings-loan-1986': 'w-en-savings-and-loan-crisis',
 'icelandic-crisis-2008': 'w-en-icelandic-financial-crisis-2008',
 'cypriot-2013': 'w-en-cypriot-financial-crisis',
 'russian-crisis-2014': 'w-en-russian-financial-crisis-2014',
 'sri-lanka-crisis-2019': 'w-en-sri-lankan-economic-crisis',
 'oil-crisis-1979': 'w-en-1979-oil-crisis',
 'recession-1920-1921': 'w-en-recession-1920-1921',
 'recession-1937-1938': 'w-en-recession-1937-1938',
 'panic-1792': 'w-en-panic-of-1792',
 'black-friday-1869': 'w-en-black-friday-1869',
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r61_data.json', encoding='utf-8'))
for eid, sid in SRC.items():
    if sid in ex:
        continue
    # 用抓取到的真实标题与 slug 反查
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作AP】补关键数据（单源）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', added, '条')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
