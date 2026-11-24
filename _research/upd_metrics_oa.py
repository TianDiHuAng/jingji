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

note = """维基第122轮可用。OA：核查 coverage.json，修复 6 处字段陈旧，并加 R12b 一致性检查。
①**核查 coverage.json**：id 与条数完全一致（641/641），但**6 处字段与条目不符**：
utility／market-failure／recession／growth 的 level（coverage=L2，条目=L3）——这 4 条早期已升 L3 且确有 deep_svg；
too-big-to-fail（crisis_type 理论 vs 制度）、blue-monday-2009（泡沫 vs 银行，上轮我改的）的 crisis_type。
②**修复**：以 entries 为准同步 coverage.json 的 level/tier/unit/region/crisis_type 字段，6 处全部对齐、剩余不一致 0。
并确认 4 条 L3 均确有 deep_svg（名实相符）。
③**固化为检查**：`check.py` 新增 **R12b**——coverage 的 level/tier/unit/region/crisis_type 须与条目文件一致，否则 warning。已注入测试确认能捕获。
④**纳入自测**：`selftest.py` 新增"R12b coverage字段不一致"用例，自测 22 → **23 项**，全通过；同步更新 HEALTH_CHECK。
⑤这延续了 round 141 的发现：**不在检查清单上的产出物会悄悄陈旧**（上一轮矩阵、本轮 coverage.json）。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 23/23。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OA', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 6, 'reviewed': 641, 'fixed': 7,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 23/23',
    'spot_check': 'coverage.json 6 处字段陈旧已同步；check.py 加 R12b；自测 22→23',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 122 轮可用（round 142）**。**核查 coverage.json，修复 6 处字段陈旧，并加 R12b 一致性检查**。
- **核查 `coverage.json`**：id 与条数完全一致（641/641），但**6 处字段与条目不符**：
  - `utility`／`market-failure`／`recession`／`growth` 的 `level`（coverage=L2，条目=L3）——这 4 条早期已升 L3 且确有 deep_svg
  - `too-big-to-fail`（crisis_type 理论 vs 制度）、`blue-monday-2009`（泡沫 vs 银行，上轮我改的）的 crisis_type
- **修复**：以 entries 为准同步 coverage.json 的 level/tier/unit/region/crisis_type 字段，6 处全部对齐、剩余不一致 0；并确认 4 条 L3 均确有 deep_svg（名实相符）。
- **固化为检查**：`check.py` 新增 **R12b**——coverage 字段须与条目文件一致，否则 warning。已注入测试确认能捕获。
- **纳入自测**：`selftest.py` 新增「R12b coverage字段不一致」用例，自测 22 → **23 项**；同步更新 HEALTH_CHECK。
- 这延续 round 141 的发现：**不在检查清单上的产出物会悄悄陈旧**（上一轮矩阵、本轮 coverage.json）。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 23/23。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NX-NY｜2026-11-24｜状态：641条；修复覆盖矩阵陈旧（592→641）+加矩阵断言（自测22项）**',
              '**续作OA｜2026-11-24｜状态：641条；同步coverage 6处字段陈旧+加R12b检查（自测23项）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
