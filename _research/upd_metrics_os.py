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
tl = sum(len(e.get('timeline') or []) for e in es)
from collections import Counter
uc = Counter(e['unit'] for e in es)

note = """维基第135轮可用。OR-OS：核查 timeline 年份，发现并修 **2 处单元误分类** + 补齐 1 条 timeline。
①**方法**：对每条目检查 timeline 年份是否落在其单元时期范围内；"全部年份都超出"是单元误分类的强信号。
②**发现 2 处单元错**：`railway-mania`（铁路狂热 1845-47，原标 U3 20世纪上半 → 改 **U2 18—19世纪**）、
`cook-islands-currency`（核心事件 1989-1995，原标 U5 21世纪 → 改 **U4 20世纪下半**）。
其余"部分超范围"多为创立年/后续背景（如 aig 1919 创立），属正常。
③**补齐**：`creditanstalt` timeline 原仅 1855 创立，补 **1931 危机 / 1934 合并**（据 w-en-creditanstalt 缓存）。timeline 事件 657 → 659。
④**同步**：coverage.json、COVERAGE_MATRIX（U2 37/U3 34/U4 50/U5 78）、scope.md 时期列；check_docs 及时抓到 REPORT/HEALTH 的 timeline 657→659 需更新（守卫生效）。
⑤**固化 R25**：条目所有 timeline 年份都超出其单元时期范围则 warning（防单元误分类再现）。自测 29 → **30 项**。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；timeline """ + str(tl) + """ 事件；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 30/30。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OR-OS', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 641, 'fixed': 4,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 30/30',
    'spot_check': '修 2 处单元误分类（railway/cook-islands）+ creditanstalt timeline + R25，自测 30',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 135 轮可用（round 155）**。**核查 timeline 年份，发现并修 2 处单元误分类 + 补齐 1 条 timeline**。
- **方法**：检查每条目 timeline 年份是否落在其单元时期范围内；「全部年份都超出」是单元误分类的强信号。
- **发现 2 处单元错**：`railway-mania`（铁路狂热 1845-47，原标 U3 20世纪上半 → **U2 18—19世纪**）、`cook-islands-currency`（核心事件 1989-1995，原标 U5 21世纪 → **U4 20世纪下半**）。其余「部分超范围」多为创立年/后续背景（如 aig 1919 创立），属正常。
- **补齐**：`creditanstalt` timeline 原仅 1855 创立，补 **1931 危机 / 1934 合并**（据 `w-en-creditanstalt` 缓存）。timeline 事件 657 → 659。
- **同步**：coverage.json、COVERAGE_MATRIX（U2 37/U3 34/U4 50/U5 78）、scope.md 时期列；check_docs 及时抓到 REPORT/HEALTH 的 timeline 657→659 需更新（守卫生效）。
- **固化 R25**：条目所有 timeline 年份都超出其单元时期范围则 warning。自测 29 → **30 项**。
- 现状：**641 条**、来源 **742**、页面 **655**；timeline **659** 事件；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 30/30。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | tl', tl, '| units', dict(uc), '| avg', avg)
