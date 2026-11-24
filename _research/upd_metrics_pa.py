# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))
kd = sum(len(e.get('key_data') or []) for e in es)
ncase_kd = sum(1 for e in es if not e['unit'].startswith('U6') and e.get('key_data'))

note = """维基第142轮可用。PA：为 creditanstalt 补 2 条 key_data（占银行业总资产27%/GDP16%），key_data 458→460。
①**网络**：仍 URLError。
②**补 2 条 key_data**（据 w-en-creditanstalt 缓存，1931 年）：该行占奥地利银行业总资产 **27%**、相当于奥地利 GDP **16%**。key_data 458 → **460**；check_kd 强匹配 346 → **348**。
③check_docs 报出 REPORT 的 key_data 计数需更新（458→460），已同步 REPORT/HEALTH。
④现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """ 行（案例有数据 """ + str(ncase_kd) + """/209）；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 32/32。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PA', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 8, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 32/32',
    'spot_check': 'creditanstalt 补 2 条 key_data（458→460）；check_kd 强匹配 346→348',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 142 轮可用（round 162）**。**为 creditanstalt 补 2 条 key_data（占银行业总资产 27% / GDP 16%），key_data 458 → 460**。
- **网络**：仍 URLError。
- **补 2 条 key_data**（据 `w-en-creditanstalt` 缓存，1931 年）：该行占奥地利银行业总资产 **27%**、相当于奥地利 GDP **16%**。key_data 458 → **460**；check_kd 强匹配 346 → **348**。
- check_docs 报出 REPORT 的 key_data 计数需更新（458→460），已同步 REPORT/HEALTH。
- 现状：**641 条**、来源 **742**、页面 **655**；key_data **460** 行；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 32/32。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | kd', kd, '| casekd', ncase_kd, '| avg', avg)
