# -*- coding: utf-8 -*-
"""续作BF：用 OWID/世界银行通胀数据交叉核对，如实记录口径差异（争议并列，不替读者下结论）。"""
import json

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
sid = 'owid-inflation'
if sid not in ex:
    sd['sources'].append({
        'id': sid, 'title': 'Inflation of consumer prices (World Bank via Our World in Data)',
        'author': 'Our World in Data（数据源：World Bank）', 'year': '2024',
        'type': '统计数据库', 'url': 'https://ourworldindata.org/grapher/inflation-of-consumer-prices',
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'OWID 结构化 CSV(本会话下载核对，源自世界银行，非维基，作为第二独立来源)'
    })
    ex.add(sid)
    print('新增统计来源', sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

# === 委内瑞拉：如实记录两源显著差异 ===
f = 'data/entries/venezuela-hyper-2016.json'
d = json.load(open(f, encoding='utf-8'))
if sid not in d['sources']:
    d['sources'].append(sid)
have = {k['label'] for k in d['key_data']}
add = [
 ('委内瑞拉通胀率(2014，世界银行/OWID口径)', 62.17, '%（年率；维基条目另载69%，两源有差异）', 2014,
  '来源：OWID inflation-of-consumer-prices.csv，entity=Venezuela, year=2014 → 62.169（世界银行口径）。'
  '**与维基所载69%存在差异**，可能与口径（年均/年末）或修订有关，具体差异原因待核实。', [sid]),
 ('委内瑞拉通胀率(2016，世界银行/OWID口径)', 254.95, '%（年率；维基条目另载800%，两源差异显著）', 2016,
  '来源：OWID ... year=2016 → 254.949（世界银行口径）。**与维基所载800%差异显著**。'
  '委内瑞拉自2015年后长期停发完整官方统计，各方估算分歧很大；此处并列两源，不替读者判断何者为准。', [sid]),
]
for lab, val, unit, yr, note, srcs in add:
    if lab in have:
        continue
    d['key_data'].append({'label': lab, 'value': val, 'unit': unit, 'year': yr,
                          'comparable_price': False, 'note': note, 'sources': srcs})
d['pending_notes'] = (d.get('pending_notes', '') +
                      ' 【续作BF】委内瑞拉通胀已并列"维基估算"与"世界银行/OWID"两组数值，二者差异显著；官方统计长期中断，具体数值以何者为准待核实。')
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('venezuela-hyper-2016 并列两源（含差异说明）')

# === 津巴布韦：同样并列 ===
f = 'data/entries/zimbabwe-hyper-2007.json'
d = json.load(open(f, encoding='utf-8'))
if sid not in d['sources']:
    d['sources'].append(sid)
have = {k['label'] for k in d['key_data']}
lab = '津巴布韦通胀率(2019，世界银行/OWID口径)'
if lab not in have:
    d['key_data'].append({
        'label': lab, 'value': 255.31, 'unit': '%（年率；维基条目另载175%，两源有差异）', 'year': 2019,
        'comparable_price': False,
        'note': '来源：OWID ... entity=Zimbabwe, year=2019 → 255.305（世界银行口径）。**与维基所载175%存在差异**，'
                '可能与统计口径与时点不同有关，具体待核实。此处并列两源。',
        'sources': [sid]})
d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作BF】2019年通胀已并列两组数值（175% vs 255.3%），差异待核实。')
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('zimbabwe-hyper-2007 并列两源')

# === 阿根廷：两源接近，可视为印证 ===
f = 'data/entries/argentina-2018.json'
d = json.load(open(f, encoding='utf-8'))
if sid not in d['sources']:
    d['sources'].append(sid)
have = {k['label'] for k in d['key_data']}
lab = '阿根廷通胀率(2018，世界银行/OWID口径)'
if lab not in have:
    d['key_data'].append({
        'label': lab, 'value': 34.28, 'unit': '%（年率；维基条目载"超过30%"）', 'year': 2018,
        'comparable_price': False,
        'note': '来源：OWID ... entity=Argentina, year=2018 → 34.277（世界银行口径）。**与维基"超过30%"一致**，构成双源印证。',
        'sources': [sid]})
d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作BF】2018年通胀已由世界银行/OWID数据印证（34.3% vs "超过30%"）。')
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('argentina-2018 双源印证')
