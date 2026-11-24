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

note = """维基第118轮可用。NR：把 round 137 的渲染扫描固化为永久检查——修复 check_quality 的"孤立 **"漏检。
①**发现检查盲区**：round 137 手工扫描发现 3 页残留**，但 check_quality 当时报 0 problem——因其判据为正则 `\\*\\*[^*]+\\*\\*`（只抓**成对**的 **x**），
而残留的是**孤立**的单个 **（如"…指标**，但…"），不被匹配。
②**修复 check_quality**：改为"页面中任意出现 `**` 即报错"（正确渲染的 HTML 不应含任何字面 **）。已注入测试确认能捕获孤立 **，当前站 0 problem。
③**纳入自测**：`selftest.py` 新增"check_quality 孤立**"用例，自测由 18 → **19 项**，全部通过。
④这延续了既定模式：**发现→修复→加检查→加自测**，使同类问题不可复发。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 19/19。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NR', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 655, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 19/19',
    'spot_check': '修复 check_quality 孤立**漏检 + 自测新增用例（18→19）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 118 轮可用（round 138）**。**把 round 137 的渲染扫描固化为永久检查——修复 check_quality 的「孤立 `**`」漏检**。
- **发现检查盲区**：round 137 手工扫描发现 3 页残留 `**`，但 `check_quality` 当时报 0 problem——因其判据为正则 `\\*\\*[^*]+\\*\\*`（只抓**成对**的 `**x**`），而残留的是**孤立**的单个 `**`（如「…指标**，但…」），不被匹配。
- **修复 check_quality**：改为「页面中任意出现 `**` 即报错」（正确渲染的 HTML 不应含任何字面 `**`）。已注入测试确认能捕获孤立 `**`，当前站 0 problem。
- **纳入自测**：`selftest.py` 新增「check_quality 孤立**」用例，自测由 18 → **19 项**，全部通过。
- 这延续了既定模式：**发现→修复→加检查→加自测**，使同类问题不可复发。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 19/19。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NP-NQ｜2026-11-24｜状态：641条；渲染层验证，修复3页未渲染**并加防御剥除**',
              '**续作NR｜2026-11-24｜状态：641条；修复check_quality孤立**漏检，自测扩至19项**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
