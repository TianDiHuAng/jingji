# -*- coding: utf-8 -*-
"""续作HI：处理重复——externalities→externality、var→value-at-risk。

BACKLOG 清单（round 37 编制）已过时：它列出 externalities 与 var 为缺口，
但站内已有 externality 与 value-at-risk（id 不同）。这是"未先检索自己的库"的又一次复发。
合并方式：把新建条目中的 timeline／对比／关联并入已有条目，删除重复文件。
"""
import glob
import json
import os

PAIRS = [('externalities', 'externality'), ('var', 'value-at-risk')]

for new_id, keep_id in PAIRS:
    np = 'data/entries/%s.json' % new_id
    kp = 'data/entries/%s.json' % keep_id
    if not os.path.exists(np):
        print('无', new_id); continue
    n = json.load(open(np, encoding='utf-8'))
    k = json.load(open(kp, encoding='utf-8'))

    # 并入 timeline（已有为空则采用新的）
    if n.get('timeline') and not k.get('timeline'):
        k['timeline'] = n['timeline']
        print('%s: 并入 timeline %d 条' % (keep_id, len(k['timeline'])))
    # 并入 sources
    for s in n.get('sources', []):
        if s not in k['sources']:
            k['sources'].append(s)
            print('%s: 并入来源 %s' % (keep_id, s))
    # 并入 related
    for r in n.get('related', []):
        if r not in n.get('related', []):
            continue
        if r not in k.get('related', []) and r not in (new_id, keep_id):
            k.setdefault('related', []).append(r)
    # 若已有 overview 较短，用新的替换
    if len(k.get('overview', '')) < len(n.get('overview', '')):
        k['overview'] = n['overview']
        print('%s: 采用更完整的 overview（%d 字）' % (keep_id, len(k['overview'])))
    if len(k.get('comparison', '')) < len(n.get('comparison', '')):
        k['comparison'] = n['comparison']
        print('%s: 采用更完整的 comparison' % keep_id)
    if not k.get('schools') and n.get('schools'):
        k['schools'] = n['schools']
    k['pending_notes'] = (k.get('pending_notes', '')
                          + ' 【续作HI】并入 %s 的内容（重复条目，已删除）。' % new_id)
    json.dump(k, open(kp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    # 全站 related 重定向
    for f in glob.glob('data/entries/*.json'):
        d = json.load(open(f, encoding='utf-8'))
        rel = d.get('related', [])
        if new_id in rel:
            d['related'] = sorted({keep_id if r == new_id else r for r in rel} - {new_id})
            json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

    os.remove(np)
    print('已删除:', new_id)

# 更新 coverage
cov = json.load(open('coverage.json', encoding='utf-8'))
cov['entries'] = [e for e in cov['entries'] if e['id'] not in ('externalities', 'var')]
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total:', cov['total'])
