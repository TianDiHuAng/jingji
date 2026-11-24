# -*- coding: utf-8 -*-
"""续作IY：修复 72 处指向不存在来源的引用。

来源：round 98 批量补 timeline 来源时，部分 id 是按"条目名/id 猜测"构造的，
实际来源 id 拼写不同（如 w-en-british-credit-crisis-of-1772 vs w-en-british-credit-1772）。

修复优先级：
1) 若 bad_id 去掉 'w-en-' 后与现有来源 id 有包含关系 → 用之；
2) 否则若条目自身有新来源 → 用条目主来源；
3) 仍不可解 → 保持并记入 pending_notes（不编造）。
"""
import glob
import json

srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
valid = {s['id'] for s in srcs}
ids = sorted(valid, key=len)


def resolve(bad, eid, entry_srcs):
    core = bad.replace('w-en-', '').replace('w-zh-', '').replace('w-de-', '').replace('w-fr-', '')
    # 1) 包含关系匹配（优先英文维基）
    cands = [i for i in ids if i.startswith('w-en-') and (core in i or i.replace('w-en-', '') in core)]
    if not cands:
        cands = [i for i in ids if core and (core in i or i.replace('w-en-', '') in core)]
    if cands:
        # 取最短（通常最贴近）
        return sorted(cands, key=len)[0], 'fuzzy'
    # 2) 条目主来源
    ok = [s for s in entry_srcs if s in valid]
    if ok:
        return ok[0], 'entry'
    return None, 'none'


fixed_f, fixed_e, unresolved = 0, 0, []
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    ch = False
    for fld in ('timeline', 'schools', 'policy_response', 'key_data'):
        for it in d.get(fld) or []:
            if not isinstance(it, dict):
                continue
            ss = it.get('sources') or []
            new = []
            for s in ss:
                if s in valid:
                    new.append(s)
                    continue
                r, how = resolve(s, d['id'], d.get('sources', []))
                if r:
                    new.append(r)
                    if how == 'fuzzy':
                        fixed_f += 1
                    else:
                        fixed_e += 1
                    ch = True
                else:
                    unresolved.append((d['id'], fld, s))
            # 去重保持顺序
            seen, out = set(), []
            for x in new:
                if x not in seen:
                    seen.add(x)
                    out.append(x)
            if out != ss:
                it['sources'] = out
    if ch:
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

print('模糊匹配修复:', fixed_f)
print('改用条目主来源:', fixed_e)
print('未能解决:', len(unresolved))
for u in unresolved[:8]:
    print('  ', u)

# 复核
srcs2 = {s['id'] for s in json.load(open('data/sources.json', encoding='utf-8'))['sources']}
es = [json.load(open(x, encoding='utf-8')) for x in glob.glob('data/entries/*.json')]
bad = sum(1 for e in es for fld in ('timeline', 'schools', 'policy_response', 'key_data')
          for it in (e.get(fld) or []) if isinstance(it, dict)
          for s in (it.get('sources') or []) if s not in srcs2)
print('剩余无效引用:', bad)
