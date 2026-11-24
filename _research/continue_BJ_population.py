# -*- coding: utf-8 -*-
"""续作BJ：用 OWID 人口数据核对移民/人口流失类数据，如实并列口径差异。"""
import json

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
sid = 'owid-population'
if sid not in ex:
    sd['sources'].append({
        'id': sid, 'title': 'Population (World Bank / UN via Our World in Data)',
        'author': 'Our World in Data（数据源：World Bank / UN）', 'year': '2024',
        'type': '统计数据库', 'url': 'https://ourworldindata.org/grapher/population',
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'OWID 结构化 CSV(本会话下载核对，源自世界银行/联合国，非维基，作为第二独立来源)'
    })
    ex.add(sid)
    print('新增统计来源', sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

# === 委内瑞拉：常住人口 vs 累计移民，口径不同 ===
f = 'data/entries/venezuela-crisis-2013.json'
d = json.load(open(f, encoding='utf-8'))
if sid not in d['sources']:
    d['sources'].append(sid)
have = {k['label'] for k in d['key_data']}
add = [
 ('委内瑞拉常住人口(2018，世行/UN口径)', 29.81, '百万人（29,807,591）', 2018,
  '来源：OWID population.csv，Venezuela 2018 → 29,807,591（世界银行/联合国口径）。', [sid]),
 ('委内瑞拉常住人口(2021，世行/UN口径)', 28.24, '百万人（28,237,830；较2018减少约157万，−5.3%）', 2021,
  '来源：OWID population.csv，Venezuela 2021 → 28,237,830。'
  '**与本条目"2021年20%（540万）已离开"并不矛盾但口径不同**：本条为常住人口存量净变化（−157万），'
  '而"540万"通常指累计出境人数（含短期离境、未变更常住登记等）。两者不可直接等同，具体口径待核实。', [sid]),
]
for lab, val, unit, yr, note, srcs in add:
    if lab in have:
        continue
    d['key_data'].append({'label': lab, 'value': val, 'unit': unit, 'year': yr,
                          'comparable_price': False, 'note': note, 'sources': srcs})
# 给原有移民数据加口径说明
for k in d['key_data']:
    if '外流人口' in k['label'] or '离开' in k['label']:
        if '口径' not in k.get('note', ''):
            k['note'] = k.get('note', '').rstrip('。') + '｜注：此为**累计出境/移民统计**，与常住人口存量变化（见世行口径条目）口径不同，不宜直接比较。'
d['pending_notes'] = (d.get('pending_notes', '') +
                      ' 【续作BJ】人口外流数据已并列两套口径：累计移民数（维基）与常住人口净变化（世行/UN）；二者含义不同，已分别注明。')
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('venezuela-crisis-2013 → 并列两套人口口径')

# === 希腊：人口变化（与危机相关）===
f = 'data/entries/greek-debt-crisis.json'
d = json.load(open(f, encoding='utf-8'))
if sid not in d['sources']:
    d['sources'].append(sid)
have = {k['label'] for k in d['key_data']}
for lab, val, unit, yr, note in [
 ('希腊人口(2009，世行/UN口径)', 11.11, '百万人（11,108,067）', 2009,
  '来源：OWID population.csv，Greece 2009 → 11,108,067（世界银行/联合国口径）。'),
 ('希腊人口(2017，世行/UN口径)', 10.75, '百万人（10,753,532；较2009减少约35万，−3.2%）', 2017,
  '来源：OWID population.csv，Greece 2017 → 10,753,532。危机期间人口净减少，与移民外流和低生育率相符（具体归因待核实）。'),
]:
    if lab in have:
        continue
    d['key_data'].append({'label': lab, 'value': val, 'unit': unit, 'year': yr,
                          'comparable_price': False, 'note': note, 'sources': [sid]})
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BJ】补充世行/UN口径人口数据。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('greek-debt-crisis → 补人口数据')
