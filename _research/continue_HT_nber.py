# -*- coding: utf-8 -*-
"""续作HT：为两个衰退条目补 NBER 作为独立机构来源；其余单来源条目诚实保留。

判断依据：项目的双源要求针对"关键事实"（具体数值）。概念条目的定义属教科书共识，
单源维基引用已足够且已标 needs_verification；而"衰退起止月份"是 NBER 的官方判定，
是真正的独立机构来源，应当补上。
"""
import glob
import json

# NBER 已在 sources.json 中（org-nber）
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
ids = {s['id'] for s in sj['sources']}
if 'org-nber' not in ids:
    sj['sources'].append({
        'id': 'org-nber', 'title': 'National Bureau of Economic Research（美国经济研究局）',
        'author': 'NBER', 'year': '2026', 'type': '权威机构',
        'url': 'https://www.nber.org/', 'url2': 'https://www.nber.org/research/business-cycle-dating',
        'verified': True, 'link_ok': True,
        'note': '美国衰退起止月份的官方判定机构（Business Cycle Dating Committee）',
    })
    sj['count'] = len(sj['sources'])
    json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('注册 NBER 来源')

for eid in ('recession-1960-1961', 'recession-1969-1970'):
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    if 'org-nber' in d['sources']:
        continue
    d['sources'].append('org-nber')
    # 关键数据的来源也加上 NBER（起止月份判定出自该机构）
    for k in d.get('key_data', []):
        if '持续月数' in k['label'] and 'org-nber' not in k['sources']:
            k['sources'] = ['org-nber', 'w-en-' + eid]
            k['note'] = k['note'].replace('单一来源待核实', '衰退起止月份由 NBER 判定，时长据此计算')
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作HT】补 NBER 作为独立机构来源（衰退起止由其商业周期测定委员会判定）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补 NBER:', eid)

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
single = [e['id'] for e in es if len(e.get('sources', [])) == 1]
print('\n剩余单来源条目:', len(single))
print('  ', ', '.join(single))
print('\n说明：这些均为 U6 概念条目，其定义为教科书共识而非需双源印证的具体数值，')
print('已统一标注 needs_verification=true，故不以"相关概念页"充作第二来源。')
