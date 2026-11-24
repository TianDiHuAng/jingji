# -*- coding: utf-8 -*-
"""续作BD：继续用美联储历史站交叉验证/补充数据。"""
import json

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
NEW = {
 'fed-stock-crash-1987': ('Stock Market Crash of 1987', 'https://www.federalreservehistory.org/essays/stock-market-crash-of-1987'),
 'fed-savings-loan': ('Savings and Loan Crisis', 'https://www.federalreservehistory.org/essays/savings-and-loan-crisis'),
 'fed-subprime': ('Subprime Mortgage Crisis', 'https://www.federalreservehistory.org/essays/subprime-mortgage-crisis'),
 'fed-asian-crisis': ('Asian Financial Crisis', 'https://www.federalreservehistory.org/essays/asian-financial-crisis'),
}
for sid, (title, url) in NEW.items():
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': title, 'author': 'Federal Reserve History (美国联邦储备系统历史站)',
        'year': 'n.d.', 'type': '官方机构', 'url': url, 'url2': None,
        'verified': True, 'link_ok': True,
        'note': '官方机构页面(本会话抓取核对，非维基，作为第二独立来源)'
    })
    ex.add(sid)
    print('新增官方来源', sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

# === 1) black-monday-1987：22.6% 双源完全一致 ===
f = 'data/entries/black-monday-1987.json'
d = json.load(open(f, encoding='utf-8'))
if 'fed-stock-crash-1987' not in d['sources']:
    d['sources'].append('fed-stock-crash-1987')
for k in d['key_data']:
    if k['label'].startswith('道指单日跌幅'):
        k['sources'] = list(dict.fromkeys(k.get('sources', []) + ['fed-stock-crash-1987']))
        k['note'] = (k.get('note', '').rstrip('。') +
                     '｜**双源完全一致**：美联储历史站记载"DJIA dropped 22.6 percent"（单日最大跌幅），与维基来源数值相同，两个独立来源印证。')
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BD】道指22.6%已获美联储历史站双源印证。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('black-monday-1987 标注双源一致')

# === 2) savings-loan-1986：补资产增速 ===
f = 'data/entries/savings-loan-1986.json'
d = json.load(open(f, encoding='utf-8'))
if 'fed-savings-loan' not in d['sources']:
    d['sources'].append('fed-savings-loan')
have = {k['label'] for k in d['key_data']}
lab = '储贷业资产增速(1982–1985)'
if lab not in have:
    d['key_data'].append({
        'label': lab, 'value': 56, 'unit': '%（同期银行24%，两倍多）', 'year': 1985,
        'comparable_price': False,
        'note': '原文：From 1982 to 1985, thrift industry assets grew 56 percent, more than twice the 24 percent rate observed at banks（美联储历史）。',
        'sources': ['fed-savings-loan']})
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BD】资产增速数据来自美联储历史站。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('savings-loan-1986 补1条')

# === 3) subprime-crisis-2007：补FHA份额 ===
f = 'data/entries/subprime-crisis-2007.json'
d = json.load(open(f, encoding='utf-8'))
if 'fed-subprime' not in d['sources']:
    d['sources'].append('fed-subprime')
have = {k['label'] for k in d['key_data']}
lab = 'FHA占新发按揭份额变化'
if lab not in have:
    d['key_data'].append({
        'label': lab, 'value': 40, 'unit': '%（危机后超40%；危机前不足10%）', 'year': 2010,
        'comparable_price': False,
        'note': '原文：Because FHA loans allow for low down payments, the agency\'s share of newly issued mortgages jumped from under 10 percent to over 40 percent（美联储历史）。',
        'sources': ['fed-subprime']})
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BD】FHA份额数据来自美联储历史站。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('subprime-crisis-2007 补1条')

# === 4) asian-financial-crisis-1997：补GDP增速背景 ===
f = 'data/entries/asian-financial-crisis-1997.json'
d = json.load(open(f, encoding='utf-8'))
if 'fed-asian-crisis' not in d['sources']:
    d['sources'].append('fed-asian-crisis')
have = {k['label'] for k in d['key_data']}
lab = '亚洲经济体危机前GDP增速'
if lab not in have:
    d['key_data'].append({
        'label': lab, 'value': 5, 'unit': '%（超过5%，常接近更高）', 'year': 1996,
        'comparable_price': False,
        'note': '原文：supporting GDP growth rates exceeding 5 percent and often approachin[g...]（美联储历史）。',
        'sources': ['fed-asian-crisis']})
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BD】危机前增速背景来自美联储历史站。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('asian-financial-crisis-1997 补1条')
