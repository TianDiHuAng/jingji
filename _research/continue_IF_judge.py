# -*- coding: utf-8 -*-
"""续作IF：细化"独立撰写"与"统计汇总"的判据。

原判据简单按前缀：fed-* → 独立；owid-*/org-* → 统计汇总。
问题：org-imf-glossary（IMF 官方术语表）、org-bis、org-fsb、org-nber 是**机构独立撰写的文献**，
     不是"汇总各国官方统计"；把它们归入"统计口径对照"是错的。

新判据：
  独立撰写 = fed-* 或  白名单中的机构文献 id
  统计汇总 = owid-* 或  白名单中的数据类 id
"""
P = 'tools/gen_site.py'
with open(P, 'r', encoding='utf-8', newline='') as f:
    s = f.read()

# 定义两组 id（放在 OFFICIAL_PREFIX 附近）
if 'INDEP_DOC_IDS' not in s:
    anchor = "OFFICIAL_PREFIX = ('fed-', 'owid-')"
    add = (
        "OFFICIAL_PREFIX = ('fed-', 'owid-')\n"
        "# 机构独立撰写的文献（可视为独立撰写链条，非"汇总各国统计"）\n"
        "INDEP_DOC_IDS = {'org-imf-glossary', 'org-bis', 'org-fsb', 'org-nber',\n"
        "                 'org-fed-history', 'org-fed-essay-1907', 'org-fed-essay-greatdep',\n"
        "                 'org-ecb'}\n"
        "# 汇总各国官方统计的数据源（与维基数字常同源）\n"
        "STAT_DATA_IDS = {'owid-dataset', 'owid-inflation', 'owid-gdp', 'owid-real-gdp',\n"
        "                 'owid-unemployment', 'owid-population', 'org-imf-data',\n"
        "                 'org-worldbank', 'org-fred', 'org-bea', 'org-ourworldindata'}\n"
    )
    if anchor in s:
        s = s.replace(anchor, add, 1)
        print('1) 已插入两组 id 白名单')

# 修正分类条件
old2 = "        elif any(str(x).startswith('fed-') for x in srcs) and any(w in note for w in _confkw):"
new2 = ("        elif (any(str(x).startswith('fed-') for x in srcs)\n"
        "              or any(str(x) in INDEP_DOC_IDS for x in srcs)) \\\n"
        "             and any(w in note for w in _confkw):")
if old2 in s:
    s = s.replace(old2, new2, 1)
    print('2) 已修正 confirmed 判据')

old3 = "        elif any(str(x).startswith(('owid-', 'org-')) for x in srcs) and any(w in note for w in _confkw):"
new3 = ("        elif (any(str(x).startswith('owid-') for x in srcs)\n"
        "              or any(str(x) in STAT_DATA_IDS for x in srcs)) \\\n"
        "             and any(w in note for w in _confkw):")
if old3 in s:
    s = s.replace(old3, new3, 1)
    print('3) 已修正 statview 判据')

with open(P, 'w', encoding='utf-8', newline='') as f:
    f.write(s)
print('写入完成')
