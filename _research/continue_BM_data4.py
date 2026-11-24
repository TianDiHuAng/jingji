# -*- coding: utf-8 -*-
"""续作BM：为4个历史案例补关键数据（阿姆斯特丹1763/孟加拉1769/铜恐慌1789/阿伦达尔1886）。"""
import json

DATA = {
 'amsterdam-crisis-1763': [
   ('战时高价回落幅度(1763年初)', -30, '%（战争结束后）', 1763,
    '原文：early 1763, because of the end of the war, the abnormal high war prices plummeted by 30%；单一来源待核实。'),
   ('破产商号数量与债务(1763)', 10, '百万荷兰盾（30多家银行与商号，约1000万盾）', 1763,
    '原文：more than 30 banking and trade firms went bankrupt, with an estimated debt of 10 million Dutch guilders；单一来源待核实。'),
   ('下西里西亚小麦价格跌幅(1763)', -75, '%（腓特烈抛售战时谷物储备后）', 1763,
    '原文：leading in the next months to a 75% drop in the local price of wheat；单一来源待核实。'),
 ],
 'bengal-bubble-1769': [
   ('东印度公司股价(1769)', 284, '英镑/股', 1769,
    '原文：By 1769, the East India Company stock was trading at £284；单一来源待核实。'),
   ('东印度公司股价跌幅(至1784)', -55, '%（跌至£122）', 1784,
    '原文：By 1784, the stock had declined to £122, a fall of 55%；单一来源待核实。'),
 ],
 'copper-panic-1789': [
   ('铜价通胀率(贬损高峰)', 430, '%', 1789,
    '原文：At the height of the debasement, there was a 430% inflation rate for copper and commerce ceased；单一来源待核实。'),
 ],
 'arendal-crash-1886': [
   ('相关债务规模(1886)', 12, '百万挪威克朗（约合2012年60亿克朗）', 1886,
    '原文：The debt ... was finally NOK 12 million, corresponding to the entire wealth of Kristiansand\'s population, or six billion 2012 kroner；单一来源待核实。'),
 ],
}

# 各案例的来源 id（取自其现有 sources）
SRCID = {
 'amsterdam-crisis-1763': 'w-en-amsterdam-crisis-1763',
 'bengal-bubble-1769': 'w-en-bengal-bubble-1769',
 'copper-panic-1789': 'w-en-copper-panic-1789',
 'arendal-crash-1886': 'w-en-arendal-crash-1886',
}

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r76_data.json', encoding='utf-8'))
for eid, sid in SRCID.items():
    if sid in ex:
        continue
    v = meta.get(eid, {})
    t = v.get('title')
    if not t:
        continue
    sd['sources'].append({
        'id': sid, 'title': t, 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科',
        'url': 'https://en.wikipedia.org/wiki/' + t.replace(' ', '_'),
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'Wikipedia API(full extract)核对(本会话抓取全文)'
    })
    ex.add(sid)
    print('新增来源', sid, '|', t)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

for eid, kds in DATA.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    sid = SRCID[eid]
    # 若条目现有来源中已有该页面对应来源，直接复用
    srcs_use = [s for s in d['sources'] if s.startswith('w-en-')][:1] or ([sid] if sid in ex else d['sources'][:1])
    if sid in ex and sid not in d['sources']:
        d['sources'] = [sid] + list(d['sources'])
    have = {k['label'] for k in d.get('key_data', [])}
    added = 0
    for lab, val, unit, yr, note in kds:
        if lab in have:
            continue
        d.setdefault('key_data', []).append({
            'label': lab, 'value': val, 'unit': unit, 'year': yr,
            'comparable_price': False, 'note': note,
            'sources': [sid] if sid in ex else srcs_use})
        added += 1
    d['needs_verification'] = True
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作BM】补关键数据（单源，据维基全文）。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(eid, '补', added, '条')
