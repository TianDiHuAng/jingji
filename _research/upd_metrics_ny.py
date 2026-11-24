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

note = """维基第121轮可用。NX-NY：核验覆盖矩阵，**发现并修复一个陈旧聚合页**（matrix.html 显示 592 条，实际 641）。
①**核验 matrix.html**：解析三张矩阵发现——矩阵 A/B/C 合计均为 **592**，而实际条目 **641**、案例 209（矩阵仅 205），
且 U3/U4/U5 期计数（34/47/78）与实际（35/49/79）均不符——**matrix.html 数据陈旧**。
②**根因**：`matrix.html` 由 `gen_site.py` 读取静态文件 `COVERAGE_MATRIX.md` 渲染，而该 md 从未随条目增长更新（停在 592 条）。
③**修复**：用当前 641 条数据**重生成 `COVERAGE_MATRIX.md`**（矩阵 A/B/C + 空白清单），gen_site 重新渲染后合计 **641**、各期 10/36/35/49/79/432 与实际完全一致；空白格子 9 个。
④**固化为检查**：`check_pages.py` 新增"覆盖矩阵合计须等于条目总数"断言（解析 matrix.html 三张表的合计行），防 COVERAGE_MATRIX.md 再次陈旧。已注入测试（改 641→999）确认能捕获。
⑤**纳入自测**：`selftest.py` 新增"矩阵合计校验"用例，自测 21 → **22 项**，全通过；同步更新 HEALTH_CHECK。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 22/22。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NX-NY', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 655, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 22/22',
    'spot_check': '修复 matrix.html 陈旧（592→641）；check_pages 加矩阵合计断言；自测 21→22',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 121 轮可用（round 141）**。**核验覆盖矩阵，发现并修复一个陈旧聚合页**（matrix.html 显示 592 条，实际 641）。
- **核验 matrix.html**：三张矩阵合计均为 **592**，而实际条目 **641**、案例 209（矩阵仅 205），且 U3/U4/U5 期计数（34/47/78）与实际（35/49/79）均不符——**数据陈旧**。
- **根因**：`matrix.html` 由 `gen_site.py` 读取静态文件 `COVERAGE_MATRIX.md` 渲染，而该 md **从未随条目增长更新**（停在 592 条）。
- **修复**：用当前 641 条数据**重生成 `COVERAGE_MATRIX.md`**（矩阵 A/B/C + 空白清单），重新渲染后合计 **641**、各期 10/36/35/49/79/432 与实际完全一致；空白格子 9 个。
- **固化为检查**：`check_pages.py` 新增「覆盖矩阵合计须等于条目总数」断言（解析三张表的合计行），防 `COVERAGE_MATRIX.md` 再次陈旧。已注入测试（改 641→999）确认能捕获。
- **纳入自测**：`selftest.py` 新增「矩阵合计校验」用例，自测 21 → **22 项**；同步更新 HEALTH_CHECK。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 22/22。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NU-NW｜2026-11-24｜状态：641条；SVG/重复审计通过，check_filler加整段重复检测（自测21项）**',
              '**续作NX-NY｜2026-11-24｜状态：641条；修复覆盖矩阵陈旧（592→641）+加矩阵断言（自测22项）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
