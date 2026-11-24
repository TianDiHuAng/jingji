# -*- coding: utf-8 -*-
"""续作GU：恢复误删的 owid-dataset，并修正"未引用来源"的统计口径。

教训（第 5 次工具缺陷）：此前统计"未引用来源"时只看 entries[].sources，
未计入 key_data[].sources——导致把正在被数据行引用的 owid-dataset 判为"未引用"并删除。
"""
import glob
import json
import os

sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
ids = {s['id'] for s in sj['sources']}

RESTORE = [{
    'id': 'owid-dataset',
    'url': 'https://ourworldindata.org/grapher/',
    'type': 'dataset',
    'publisher': 'Our World in Data',
    'note': 'OWID grapher 数据集总入口；具体序列按 slug 逐条引用',
    'verified': True,
}]
for r in RESTORE:
    if r['id'] not in ids:
        sj['sources'].append(r)
        print('恢复来源:', r['id'])
sj['count'] = len(sj['sources'])
json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 正确的引用统计：entries[].sources + key_data[].sources + policy/schools 等
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
used = set()
for e in es:
    used.update(e.get('sources', []))
    for k in e.get('key_data', []):
        used.update(k.get('sources', []))
    for p in e.get('policy_response', []):
        used.update(p.get('sources', []))
    for s in e.get('schools', []):
        if s.get('src'):
            used.add(s['src'])
    for s in e.get('sources_extra', []) if isinstance(e.get('sources_extra'), list) else []:
        used.add(s)

src_ids = {s['id'] for s in sj['sources']}
unused = sorted(src_ids - used)
missing = sorted(used - src_ids)
print('来源库 %d 条 | 被引用的不同来源 %d 条 | 未引用 %d 条' % (len(src_ids), len(src_ids & used), len(unused)))
print('未引用:', ', '.join(unused) if unused else '无')
print('引用了但不存在的来源:', missing if missing else '无')
