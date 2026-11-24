# -*- coding: utf-8 -*-
"""续作IG：细化独立撰写 vs 统计汇总的判据（修正引号问题）。"""
P = 'tools/gen_site.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

if 'INDEP_DOC_IDS' in s:
    print('已存在，跳过')
else:
    anchor = "OFFICIAL_PREFIX = ('fed-', 'owid-')"
    lines = [
        "OFFICIAL_PREFIX = ('fed-', 'owid-')",
        "# 机构独立撰写的文献（独立撰写链条，非汇总各国统计）",
        "INDEP_DOC_IDS = {'org-imf-glossary', 'org-bis', 'org-fsb', 'org-nber',",
        "                 'org-fed-history', 'org-fed-essay-1907', 'org-fed-essay-greatdep',",
        "                 'org-ecb'}",
        "# 汇总各国官方统计的数据源（与维基数字常同源）",
        "STAT_DATA_IDS = {'owid-dataset', 'owid-inflation', 'owid-gdp', 'owid-real-gdp',",
        "                 'owid-unemployment', 'owid-population', 'org-imf-data',",
        "                 'org-worldbank', 'org-fred', 'org-bea', 'org-ourworldindata'}",
    ]
    add = '\n'.join(lines)
    if anchor in s:
        s = s.replace(anchor, add, 1)
        print('1) 已插入白名单')

old2 = "        elif any(str(x).startswith('fed-') for x in srcs) and any(w in note for w in _confkw):"
new2 = ("        elif (any(str(x).startswith('fed-') for x in srcs)\n"
        "              or any(str(x) in INDEP_DOC_IDS for x in srcs)) \\\n"
        "             and any(w in note for w in _confkw):")
if old2 in s:
    s = s.replace(old2, new2, 1)
    print('2) confirmed 判据已修正')

old3 = "        elif any(str(x).startswith(('owid-', 'org-')) for x in srcs) and any(w in note for w in _confkw):"
new3 = ("        elif (any(str(x).startswith('owid-') for x in srcs)\n"
        "              or any(str(x) in STAT_DATA_IDS for x in srcs)) \\\n"
        "             and any(w in note for w in _confkw):")
if old3 in s:
    s = s.replace(old3, new3, 1)
    print('3) statview 判据已修正')

with open(P, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print('写入完成')
