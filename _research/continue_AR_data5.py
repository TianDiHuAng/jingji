# -*- coding: utf-8 -*-
"""续作AR：为5个案例补充 key_data（南斯拉夫恶性通胀/华盛顿互惠/IndyMac/铁路狂热/加密泡沫）。"""
import json

DATA = {
 'yugoslav-hyper-1992': [
   ('月通胀率峰值(1994年1月)', 313000000, '%（月率，3.13亿%）', 1994,
    '原文：Inflation peaked at a monthly rate of 313 million percent in January 1994；单一来源待核实。'),
   ('日通胀率(峰值期)', 62, '%（日均；时均2.03%）', 1994,
    '原文：Daily inflation was 62%, with an inflation rate of 2.03% per hour；单一来源待核实。'),
   ('恶性通胀持续时长', 22, '个月（史上第三严重）', 1994,
    '原文：the third-worst hyperinflation in world economic history, lasting 22 months；单一来源待核实。'),
 ],
 'washington-mutual': [
   ('9天挤兑提款额', 16.7, '十亿美元（167亿，占存款9%）', 2008,
    '原文：the withdrawal of US$16.7 billion in deposits during a 9-day bank run；单一来源待核实。'),
   ('FDIC 出售给摩根大通的对价', 1.9, '十亿美元（19亿）', 2008,
    '原文：The FDIC sold the banking subsidiaries ... to JPMorgan Chase for $1.9 billion；单一来源待核实。'),
   ('控股公司资产(2007年报)', 327.9, '十亿美元（3279亿）', 2007,
    '原文：the holding company held assets valued at $327.9 billion；单一来源待核实。'),
 ],
 'indymac': [
   ('房贷发放额(2006)', 90, '十亿美元（超900亿）', 2006,
    '原文：During 2006, IndyMac originated over $90 billion of mortgages；单一来源待核实。'),
   ('风险资本比率(评级下调后推算)', 9.27, '%（总风险资本率；"资本充足"下限10%）', 2008,
    '原文：the bank\'s capital ratio would have been 9.27% total risk-based；单一来源待核实。'),
 ],
 'railway-mania': [
   ('认购定金比例', 10, '%（可仅付10%定金购买股份）', 1845,
    '原文：Shares were promoted and could be purchased for a 10% deposit；单一来源待核实。'),
 ],
 'crypto-bubble': [
   ('比特币价格峰值(2013年11月)', 1127.45, '美元', 2013,
    '原文：In November 2013, Bitcoin\'s price rose to US$1,127.45；单一来源待核实。'),
   ('比特币价格(2011年6月)', 29.58, '美元（同年11月跌至2.14）', 2011,
    '原文：In June 2011, Bitcoin\'s price again rose, to US$29.58. The price then fell to US$2.14 that November；单一来源待核实。'),
 ],
}

SRC = {
 'yugoslav-hyper-1992': 'w-en-yugoslav-hyperinflation',
 'washington-mutual': 'w-en-washington-mutual',
 'indymac': 'w-en-indymac',
 'railway-mania': 'w-en-railway-mania',
 'crypto-bubble': 'w-en-crypto-bubble',
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r63_data.json', encoding='utf-8'))
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作AR】补关键数据（单源）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', added, '条')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
