# -*- coding: utf-8 -*-
"""续作AS：为7个1930s/新兴市场案例补充 key_data。"""
import json

DATA = {
 'chilean-crisis-1982': [
   ('智利GDP降幅(1982–83)', -14.3, '%', 1983,
    '原文：Chile\'s GDP fell 14.3%, and unemployment rose to 23.7%；单一来源待核实。'),
   ('智利失业率(危机期)', 23.7, '%', 1983,
    '原文：unemployment rose to 23.7%；单一来源待核实。'),
   ('智利外债(1982)', 17, '十亿美元（超170亿）', 1982,
    '原文：By 1982, Chile\'s external debt had risen to over 17 billion dollars；单一来源待核实。'),
 ],
 'brazil-hyper-1980': [
   ('巴西月通胀率峰值(1990年3月)', 81.3, '%（月率；1月71.9%、2月71.7%）', 1990,
    '原文：The monthly inflation rates between January and March 1990 were 71.9%, 71.7% and 81.3%；单一来源待核实。'),
   ('Collor 计划冻结的流动性比例', 80, '%（约）', 1990,
    '原文：The plan effectively froze 80% of all liquidity；单一来源待核实。'),
 ],
 'chinese-hyper-1937': [
   ('进口价格上涨(1938年末)', 72, '%（武汉、广州失守后）', 1938,
    '原文：the fall of Wuhan and Guangzhou in late 1938 caused import prices to rise by 72%；单一来源待核实。'),
   ('1944年进口占1937年水平', 6, '%（仅及6%）', 1944,
    '原文：by 1944, China was only receiving 6% of the total imports it had in 1937；单一来源待核实。'),
 ],
 'soviet-hyper-1917': [
   ('俄国工业总产值(战前)', 6.059, '十亿金卢布（1920年大幅下降）', 1913,
    '原文：by 1920 the total production of Russian industry had fallen from a pre-war level of 6.059 billion gold rubles；单一来源待核实。'),
 ],
 'bankruptcy-ftx': [
   ('FTX 账目窟窿', 8, '十亿美元（80亿，因客户提款激增暴露）', 2022,
    '原文：a spike in customer withdrawals that exposed an $8 billion hole in FTX\'s accounts；单一来源待核实。'),
   ('Bankman-Fried 崩盘前净资产', 16, '十亿美元（160亿，后归零）', 2022,
    '原文：Bankman-Fried\'s net worth, estimated at $16 billion prior to the collapse, was reported as having been wiped out；单一来源待核实。'),
 ],
 'danatbank-1931': [
   ('两家银行联合担保资本与储备', 1, '十亿马克（超10亿）', 1931,
    '原文：Both banks assumed a joint guarantee of capital and reserves of over 1 billion marks；单一来源待核实。'),
 ],
 'european-banking-1931': [
   ('德国股份银行存款中外币占比(1928年中)', 42, '%', 1928,
    '原文：By mid-1928, 42 percent of deposits at joint-stock banks were foreign；单一来源待核实。'),
   ('德国货币供应收缩(1930-06—1931-06)', -17, '%', 1931,
    '原文：contracting by 17 percent from June 1930 to June 1931；单一来源待核实。'),
   ('德国经济产出降幅(1932年低点较1929)', -39, '%', 1932,
    '原文：At its low point in 1932, German economic output had fallen 39 percent from its 1929 level；单一来源待核实。'),
 ],
}

SRC = {
 'chilean-crisis-1982': 'w-en-chilean-crisis-1982',
 'brazil-hyper-1980': 'w-en-hyperinflation-in-brazil',
 'chinese-hyper-1937': 'w-en-chinese-hyperinflation',
 'soviet-hyper-1917': 'w-en-soviet-hyperinflation',
 'bankruptcy-ftx': 'w-en-bankruptcy-of-ftx',
 'danatbank-1931': 'w-en-danat-bank',
 'european-banking-1931': 'w-en-european-banking-crisis-1931',
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r64_data.json', encoding='utf-8'))
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作AS】补关键数据（单源）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', added, '条')

sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))
