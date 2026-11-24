# -*- coding: utf-8 -*-
"""续作BE：引入 OWID(世界银行/ILO 数据) 作为第二独立来源，验证失业率类数据。"""
import json

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
NEW = {
 'owid-unemployment': ('Unemployment rate (World Bank / ILO via Our World in Data)',
                       'https://ourworldindata.org/grapher/unemployment-rate'),
}
for sid, (title, url) in NEW.items():
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': title, 'author': 'Our World in Data（数据源：World Bank / ILO）',
        'year': '2024', 'type': '统计数据库', 'url': url, 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'OWID 结构化 CSV(本会话下载核对，源自世界银行/ILO，非维基，作为第二独立来源)'
    })
    ex.add(sid)
    print('新增统计来源', sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

# === euro-area-crisis：27% 双源验证 + 精确值 ===
f = 'data/entries/euro-area-crisis.json'
d = json.load(open(f, encoding='utf-8'))
if 'owid-unemployment' not in d['sources']:
    d['sources'].append('owid-unemployment')
for k in d['key_data']:
    if k['label'].startswith('希腊与西班牙失业率峰值'):
        k['sources'] = list(dict.fromkeys(k.get('sources', []) + ['owid-unemployment']))
        k['note'] = (k.get('note', '').rstrip('。') +
                     '｜**双源印证**：OWID/世界银行-ILO 数据为希腊2013年 27.686%、西班牙2013年 26.094%，与维基"高达27%"一致。')
have = {k['label'] for k in d['key_data']}
for lab, val, unit, yr, note in [
  ('希腊失业率(2013，世界银行/ILO)', 27.686, '%', 2013,
   '来源：OWID grapher unemployment-rate.csv，entity=Greece, year=2013 → 27.686（世界银行/ILO 口径）。'),
  ('西班牙失业率(2013，世界银行/ILO)', 26.094, '%', 2013,
   '来源：OWID grapher unemployment-rate.csv，entity=Spain, year=2013 → 26.094（世界银行/ILO 口径）。'),
]:
    if lab in have:
        continue
    d['key_data'].append({'label': lab, 'value': val, 'unit': unit, 'year': yr,
                          'comparable_price': False, 'note': note, 'sources': ['owid-unemployment']})
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BE】失业率已用 OWID/世界银行-ILO 数据双源印证。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('euro-area-crisis 双源验证 + 补2条精确值')
