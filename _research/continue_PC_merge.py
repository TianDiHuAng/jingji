# -*- coding: utf-8 -*-
"""续作PC：合并 2 组同 URL 重复来源（递归重映射全部 sources/src 字段），删重复条目，更新 count。
- w-en-capital-adequacy  -> w-en-capital-requirement   (同 https://.../Capital_requirement)
- w-en-bank-holiday      -> w-en-emergency-banking-act-1933 (同 https://.../Emergency_Banking_Act_of_1933)
"""
import glob, json

REMAP = {
 'w-en-capital-adequacy': 'w-en-capital-requirement',
 'w-en-bank-holiday': 'w-en-emergency-banking-act-1933',
}

def remap_obj(o):
    if isinstance(o, dict):
        for k, v in list(o.items()):
            if k in ('sources', 'src'):
                if isinstance(v, list):
                    nv = [REMAP.get(x, x) for x in v]
                    # 去重保序
                    seen = set(); dd = []
                    for x in nv:
                        if x not in seen:
                            seen.add(x); dd.append(x)
                    o[k] = dd
                elif isinstance(v, str):
                    o[k] = REMAP.get(v, v)
            else:
                remap_obj(v)
    elif isinstance(o, list):
        for x in o:
            remap_obj(x)

changed = 0
for f in glob.glob('data/entries/*.json'):
    e = json.load(open(f, encoding='utf-8'))
    before = json.dumps(e, ensure_ascii=False, sort_keys=True)
    remap_obj(e)
    if json.dumps(e, ensure_ascii=False, sort_keys=True) != before:
        json.dump(e, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        changed += 1
print('重映射的条目文件数:', changed)

# 删重复来源
d = json.load(open('data/sources.json', encoding='utf-8'))
keep = [s for s in d['sources'] if s['id'] not in REMAP]
removed = len(d['sources']) - len(keep)
d['sources'] = keep
d['count'] = len(keep)
json.dump(d, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('删除重复来源:', removed, '| 新 count:', d['count'])
