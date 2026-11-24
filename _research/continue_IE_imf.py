# -*- coding: utf-8 -*-
"""续作IE：注册 IMF 官方术语表为来源，并用它补 sdr 条目。

意义：这是项目首次使用**国际机构一手文献**（而非维基百科或其转引）作为来源，
突破了"无专属维基页面即无法建条目"的限制。
"""
import glob
import json

SP = 'data/sources.json'
sj = json.load(open(SP, encoding='utf-8'))
SID = 'org-imf-glossary'
if SID not in {s['id'] for s in sj['sources']}:
    sj['sources'].append({
        'id': SID,
        'title': 'IMF Glossary（国际货币基金组织术语表）',
        'author': 'International Monetary Fund',
        'year': '2026',
        'type': '权威机构',
        'url': 'https://www.imf.org/en/About/Glossary',
        'url2': None,
        'verified': True,
        'link_ok': True,
        'note': 'IMF 官方术语表；含监督、全球失衡、储备、SDR 等条目的一手定义。'
                '注意：部分段落为较早快照（如提及"下次审查2011年"），引用时须核对时点',
    })
    sj['count'] = len(sj['sources'])
    json.dump(sj, open(SP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('注册来源:', SID)

p = 'data/entries/sdr.json'
d = json.load(open(p, encoding='utf-8'))

if SID not in d['sources']:
    d['sources'].append(SID)

# 概述：把"待核实"的篮子构成按 IMF 官方补上
d['overview'] = d['overview'].replace(
    '具体机制与权重待核实。',
    '据 IMF 术语表：SDR 篮子目前由**人民币、欧元、日元、英镑与美元**五种货币构成；'
    '最近一次审查于 **2015 年 11 月**完成，新权重于 **2016 年 10 月 1 日**生效；'
    'SDR 利率是篮子货币市场短期利率的**每周加权平均**，并设有 **0.050%** 的下限。'
    '具体权重数值与后续审查结果待核实。')

# key_data（仅取 IMF 明确给出的数值型事实）
have = {k['label'] for k in d.get('key_data', [])}
new_kd = [
    ('SDR 篮子货币数', 5, '种（人民币／欧元／日元／英镑／美元）', 2016,
     '来源：IMF Glossary — SDR 篮子目前由人民币、欧元、日元、英镑与美元构成'),
    ('SDR 利率下限', 0.050, '%', 2016,
     '来源：IMF Glossary — SDR 利率为篮子市场短期利率的每周加权平均，subject to a 0.050 percent floor'),
]
for lb, v, u, y, nt in new_kd:
    if lb in have:
        continue
    d.setdefault('key_data', []).append({
        'label': lb, 'value': v, 'unit': u, 'year': y, 'comparable_price': False,
        'note': nt + '；单一机构来源，待第二来源核实。', 'sources': [SID],
    })

# timeline 补官方时点
tl_years = {t['year'] for t in d.get('timeline', [])}
for y, ev in ((2015, 'IMF 完成 SDR 篮子最近一次审查（据 IMF Glossary）'),
              (2016, '新权重与调整后的篮子于 10 月 1 日生效（据 IMF Glossary）')):
    if y not in tl_years:
        d.setdefault('timeline', []).append({'year': y, 'event': ev})

d['timeline'] = sorted(d['timeline'], key=lambda x: x['year'])
d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作IE】补 IMF 官方术语表来源；篮子构成／审查时点／利率下限据 IMF 一手文献。')
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('sdr 已更新：来源 %d、key_data %d、timeline %d'
      % (len(d['sources']), len(d['key_data']), len(d['timeline'])))
