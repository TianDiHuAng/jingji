# -*- coding: utf-8 -*-
"""续作HU：修正两个衰退条目的来源表述——NBER 是数据的原始出处，不是第二独立来源。

原处理把它们算作"补了第二来源"，但严格说：
维基页面所载的"10个月/11个月"本就引自 NBER 的判定，
因此 NBER 与维基**不是相互独立的两个来源**，而是"原始出处与其转引"。
诚实做法是明确写出这一关系，而不是暗示已获双源印证。
"""
import glob
import json

for eid in ('recession-1960-1961', 'recession-1969-1970'):
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    for k in d.get('key_data', []):
        if '持续月数' in k['label']:
            k['note'] = ('原文：%s（维基页面所载起止月份引自 NBER 商业周期测定委员会的判定，'
                         '故 NBER 为**原始出处**、维基为转引，二者不构成相互独立的双源印证）。'
                         % ('the recession lasted for 10 months' if '1960' in eid
                            else 'the recession lasted for 11 months'))
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作HU】修正：NBER 系数据原始出处（维基转引），'
                            '不构成第二独立来源；该数值仍属单源待核实。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('修正表述:', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
single = [e['id'] for e in es if len(e.get('sources', [])) == 1]
print('\n单来源条目:', len(single), '（含 2 个衰退：其第二来源为原始出处而非独立来源）')
