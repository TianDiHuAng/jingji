# -*- coding: utf-8 -*-
"""续作BG：用 OWID 世界银行 GDP 总量数据核对 GDP 增速，标注双源一致与差异。"""
import json

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
sid = 'owid-gdp'
if sid not in ex:
    sd['sources'].append({
        'id': sid, 'title': 'GDP, total (World Bank via Our World in Data)',
        'author': 'Our World in Data（数据源：World Bank）', 'year': '2024',
        'type': '统计数据库', 'url': 'https://ourworldindata.org/grapher/gdp-worldbank',
        'url2': None, 'verified': True, 'link_ok': True,
        'note': 'OWID 结构化 CSV(本会话下载并逐年计算增速核对，源自世界银行，非维基，作为第二独立来源)'
    })
    ex.add(sid)
    print('新增统计来源', sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

def add_kd(path, label, val, unit, yr, note, srcs=(sid,)):
    d = json.load(open(path, encoding='utf-8'))
    if sid not in d['sources']:
        d['sources'].append(sid)
    have = {k['label'] for k in d['key_data']}
    if label not in have:
        d['key_data'].append({'label': label, 'value': val, 'unit': unit, 'year': yr,
                              'comparable_price': False, 'note': note, 'sources': list(srcs)})
    # 交叉验证标注
    for k in d['key_data']:
        if k['label'] == label:
            k['note'] = note
    d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BG】GDP增速已用世界银行/OWID数据核对。'
    json.dump(d, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print(path.split('/')[-1], '→', label, val, unit)

# 1) 阿根廷 2002：-10.89% vs -10.9% 完全一致
add_kd('data/entries/south-america-2002.json',
       '阿根廷GDP增速(2002，世界银行/OWID口径)', -10.89, '%（按GDP总量年增率计算；本条目另有−10.9%）', 2002,
       '来源：OWID gdp-worldbank.csv，Argentina 2001→2002 计算得 −10.89%。'
       '**与本条目 −10.9% 几乎完全相同**，构成两个独立来源的强印证。')

# 2) 西班牙 2009：-3.77% vs -3.7%
add_kd('data/entries/spain-2008.json',
       '西班牙GDP增速(2009，世界银行/OWID口径)', -3.77, '%（本条目另有−3.7%）', 2009,
       '来源：OWID gdp-worldbank.csv，Spain 2008→2009 计算得 −3.77%。'
       '**与本条目 −3.7% 一致**，构成双源印证。')

# 3) 俄罗斯 2015：-1.97% vs -3.7% 差异需并列
f = 'data/entries/russian-crisis-2014.json'
d = json.load(open(f, encoding='utf-8'))
if sid not in d['sources']:
    d['sources'].append(sid)
have = {k['label'] for k in d['key_data']}
lab = '俄罗斯GDP增速(2015，世界银行/OWID口径)'
if lab not in have:
    d['key_data'].append({
        'label': lab, 'value': -1.97, 'unit': '%（年增率；本条目另载−3.7%，两源有差异）', 'year': 2015,
        'comparable_price': False,
        'note': '来源：OWID gdp-worldbank.csv，Russia 2014→2015 计算得 −1.97%。'
                '**与本条目所载 −3.7% 存在差异**，可能与数据修订版本、汇率换算或统计口径有关，具体原因待核实。此处并列两源。',
        'sources': [sid]})
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BG】2015年GDP增速已并列两源（−3.7% vs 世行 −1.97%），差异待核实。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('russian-crisis-2014 → 并列两源差异')
