# -*- coding: utf-8 -*-
"""续作BH：用 OWID 实际GDP增速数据核对巴西/德国数据。"""
import json

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
sid = 'owid-real-gdp'
if sid not in ex:
    sd['sources'].append({
        'id': sid, 'title': 'Real GDP growth (World Bank via Our World in Data)',
        'author': 'Our World in Data（数据源：World Bank）', 'year': '2024',
        'type': '统计数据库', 'url': 'https://ourworldindata.org/grapher/real-gdp-growth',
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'OWID 结构化 CSV(本会话下载核对，实际GDP增速口径，源自世界银行，非维基，作为第二独立来源)'
    })
    ex.add(sid)
    print('新增统计来源', sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

# === 1) 巴西：两源完全一致 ===
f = 'data/entries/brazil-2014.json'
d = json.load(open(f, encoding='utf-8'))
if sid not in d['sources']:
    d['sources'].append(sid)
have = {k['label'] for k in d['key_data']}
for lab, val, yr, note in [
  ('巴西实际GDP增速(2015，世界银行/OWID口径)', -3.546, 2015,
   '来源：OWID real-gdp-growth.csv，Brazil 2015 → −3.546%。**与本条目 −3.5% 完全一致**，双源印证。'),
  ('巴西实际GDP增速(2016，世界银行/OWID口径)', -3.276, 2016,
   '来源：OWID real-gdp-growth.csv，Brazil 2016 → −3.276%。**与本条目 −3.3% 一致**，双源印证。'),
]:
    if lab in have:
        continue
    d['key_data'].append({'label': lab, 'value': val, 'unit': '%（实际GDP年增率）', 'year': yr,
                          'comparable_price': False, 'note': note, 'sources': [sid]})
# 给原两条加印证标注
for k in d['key_data']:
    if k['label'] in ('巴西GDP增速(2015)', '巴西GDP增速(2016)'):
        k['note'] = k.get('note', '').rstrip('。') + '｜**已由世界银行/OWID 数据印证**（两源数值一致）。'
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BH】2015/2016实际GDP增速已获世界银行/OWID双源印证。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('brazil-2014 双源印证')

# === 2) 德国：2023接近、2024差异显著 ===
f = 'data/entries/german-crisis-2022.json'
d = json.load(open(f, encoding='utf-8'))
if sid not in d['sources']:
    d['sources'].append(sid)
have = {k['label'] for k in d['key_data']}
for lab, val, yr, note in [
  ('德国实际GDP增速(2023，世界银行/OWID口径)', -1.017, 2023,
   '来源：OWID real-gdp-growth.csv，Germany 2023 → −1.017%。与本条目 −0.9% 接近（差异约0.1个百分点，或因修订版本不同）。'),
  ('德国实际GDP增速(2024，世界银行/OWID口径)', 0.007, 2024,
   '来源：OWID real-gdp-growth.csv，Germany 2024 → +0.007%（近乎零增长）。**与本条目所载 −0.5% 差异显著**；'
   '可能源于统计机构初值/修订值差异或口径不同，具体待核实。此处并列两源，不替读者判断。'),
]:
    if lab in have:
        continue
    d['key_data'].append({'label': lab, 'value': val, 'unit': '%（实际GDP年增率）', 'year': yr,
                          'comparable_price': False, 'note': note, 'sources': [sid]})
d['pending_notes'] = (d.get('pending_notes', '') +
                      ' 【续作BH】2024年增速已并列两源（−0.5% vs 世行 +0.007%），差异显著；2023年两源接近。')
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('german-crisis-2022 并列两源（2024差异显著）')
