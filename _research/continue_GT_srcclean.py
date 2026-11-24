# -*- coding: utf-8 -*-
"""续作GT：为明确相关的书籍与机构来源补引用；删除确实无用的个别来源。"""
import json
import os
import glob

# 书籍/机构 -> 条目（只补内容确实依赖者）
FIX = {
 'wall-street-1929': ['bk-the-great-crash-1929', 'bk-the-crash-of-1929'],
 'great-depression': ['bk-the-great-depression', 'org-fed-essay-greatdep'],
 'subprime-crisis-2007': ['bk-the-big-short'],
 'marxist-theory': ['bk-das-kapital'],
 'black-wednesday-1992': ['bk-black-wednesday'],
 'business-cycle': ['org-nber'],
 'central-bank': ['org-fed-history', 'org-bis'],
 'european-central-bank': ['org-ecb'],
 'debt-crisis': ['bk-sovereign-debt-and-the-financial-crisis'],
 'industrial-organization': ['bk-the-theory-of-industrial-organization'],
}

n = 0
for eid, sids in FIX.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    srcs = d.setdefault('sources', [])
    added = [s for s in sids if s not in srcs]
    if added:
        srcs.extend(added)
        d['pending_notes'] = (d.get('pending_notes', '')
                              + ' 【续作GT】补充背景文献/机构来源 %s。' % '、'.join(added))
        json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n += 1
        print('%-24s += %s' % (eid, ','.join(added)))

# 删除确实无用的来源（消歧义页与无对应条目的通用页）
DROP = ['w-en-venezuelan-economic-crisis', 'w-zh-001', 'org-georgetown', 'owid-dataset']
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
before = len(sj['sources'])
sj['sources'] = [s for s in sj['sources'] if s['id'] not in DROP]
sj['count'] = len(sj['sources'])
json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('\n删除无用来源 %d 个：%s' % (before - sj['count'], ', '.join(DROP)))

# 复核
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src_ids = {s['id'] for s in sj['sources']}
used = set()
missing = []
for e in es:
    for s in e.get('sources', []):
        used.add(s)
        if s not in src_ids:
            missing.append((e['id'], s))
unused = [s for s in src_ids if s not in used]
print('补入 %d 个条目 | 剩余未引用 %d 个 | 引用了不存在的来源 %d 处' % (n, len(unused), len(missing)))
if unused:
    print('  ', ', '.join(sorted(unused)))
if missing:
    print('  缺失:', missing[:6])
