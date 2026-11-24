# -*- coding: utf-8 -*-
"""round 129f：审计验证页五分类的真实性。
跨语言对照：条目须同时有 w-en-* 与 w-zh-* 来源；
统计口径对照：须有统计类来源；
独立机构印证：须有 fed-*/机构独立文献来源。"""
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = {s['id']: s for s in json.load(open('data/sources.json', encoding='utf-8'))['sources']}

def is_en(s): return str(s).startswith('w-en-')
def is_zh(s): return str(s).startswith('w-zh-')

# 跨语言对照：key_data 的 sources 中同时有 en 与 zh
cross = 0
cross_bad = []
for e in es:
    for k in e.get('key_data') or []:
        ss = k.get('sources') or []
        if any(is_en(x) for x in ss) and any(is_zh(x) for x in ss):
            cross += 1
            if not (any(is_en(x) for x in ss) and any(is_zh(x) for x in ss)):
                cross_bad.append(e['id'])
print('跨语言对照（en+zh 同在 key_data）:', cross, '| 检查矛盾:', len(cross_bad))

# 统计口径对照：是否有 owid/worldbank 等
STAT = ('owid-', 'org-worldbank', 'org-imf-data', 'org-fred', 'org-bea', 'org-ourworldindata')
stat = 0
for e in es:
    for k in e.get('key_data') or []:
        if any(str(x).startswith(STAT) for x in (k.get('sources') or [])):
            stat += 1
print('统计口径对照（含 OWID/世行等来源的 key_data）:', stat)

# 独立机构印证：fed-* 或 org-* 独立文献
IND = ('fed-', 'org-fed-history', 'org-fed-essay-1907', 'org-fed-essay-greatdep',
       'org-imf-glossary', 'org-bis', 'org-fsb', 'org-ecb')
ind = 0
for e in es:
    for k in e.get('key_data') or []:
        if any(str(x).startswith(IND) for x in (k.get('sources') or [])):
            ind += 1
print('独立机构印证（含 fed-/独立机构文献）:', ind)

# 来源类型分布
from collections import Counter
print('\n来源总量:', len(srcs))
print('类型:', dict(Counter(s.get('type') for s in srcs.values())))
# 语言前缀分布
pref = Counter()
for sid in srcs:
    if sid.startswith('w-en-'): pref['w-en'] += 1
    elif sid.startswith('w-zh-'): pref['w-zh'] += 1
    elif sid.startswith('w-'): pref['w-其他'] += 1
    elif sid.startswith('org-'): pref['org'] += 1
    elif sid.startswith('bk-'): pref['bk'] += 1
    else: pref['其他'] += 1
print('前缀:', dict(pref))
