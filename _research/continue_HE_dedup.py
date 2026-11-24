# -*- coding: utf-8 -*-
"""续作HE：合并 sources.json 中指向同一 URL 的重复来源。

策略：每组保留"被引用次数更多"的 id（并列时保留 id 较短者），
把全站引用（sources／key_data／policy_response／schools）重定向后删除多余条目。
"""
import glob
import json
from collections import Counter, defaultdict

SP = 'data/sources.json'
sj = json.load(open(SP, encoding='utf-8'))
srcs = sj['sources']

# 统计引用
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
use = Counter()


def bump(sid, n=1):
    if sid:
        use[sid] += n


for e in es:
    for s in e.get('sources', []) or []:
        bump(s)
    for k in e.get('key_data', []) or []:
        for s in k.get('sources', []) or []:
            bump(s)
    for p in e.get('policy_response', []) or []:
        for s in p.get('sources', []) or []:
            bump(s)
    for sc in e.get('schools', []) or []:
        bump(sc.get('src'))

# 按 URL 分组
groups = defaultdict(list)
for s in srcs:
    groups[s['url'].rstrip('/').lower()].append(s['id'])

redirect = {}
for url, ids in groups.items():
    if len(ids) < 2:
        continue
    # 保留：引用多者优先，并列取 id 短者
    keep = sorted(ids, key=lambda i: (-use[i], len(i), i))[0]
    for i in ids:
        if i != keep:
            redirect[i] = keep

print('待合并来源: %d 个 → 归并为 %d 个保留 id' % (len(redirect), len(set(redirect.values()))))
for old, new in list(redirect.items())[:8]:
    print('  %-40s → %s (refs %d→%d)' % (old, new, use[old], use[new]))

# 重定向全站引用
n_ent = 0
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    changed = False

    def remap(lst):
        out, seen = [], set()
        for x in lst:
            y = redirect.get(x, x)
            if y not in seen:
                seen.add(y)
                out.append(y)
        return out

    if d.get('sources'):
        new = remap(d['sources'])
        if new != d['sources']:
            d['sources'] = new
            changed = True
    for k in d.get('key_data', []) or []:
        if k.get('sources'):
            new = remap(k['sources'])
            if new != k['sources']:
                k['sources'] = new
                changed = True
    for p in d.get('policy_response', []) or []:
        if p.get('sources'):
            new = remap(p['sources'])
            if new != p['sources']:
                p['sources'] = new
                changed = True
    for sc in d.get('schools', []) or []:
        if sc.get('src'):
            y = redirect.get(sc['src'], sc['src'])
            if y != sc['src']:
                sc['src'] = y
                changed = True
    if changed:
        n_ent += 1
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('重定向涉及的条目: %d' % n_ent)

# 删除被合并的来源
before = len(sj['sources'])
sj['sources'] = [s for s in sj['sources'] if s['id'] not in redirect]
sj['count'] = len(sj['sources'])
json.dump(sj, open(SP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源库: %d → %d' % (before, sj['count']))
