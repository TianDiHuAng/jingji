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
cases = [e for e in es if not e['unit'].startswith('U6')]
pr = sum(1 for e in cases if e.get('policy_response'))

note = """维基第125轮可用。OE：核查 BLOCKERS.md 与 DECISIONS.md，修正多处陈旧/自相矛盾记录。
①**BLOCKERS.md 陈旧三处**（经核实）：
（a）"库缺 2020 新冠股灾一条"→ **`covid-crash-2020` 已建成**，说法错误；
（b）"案例政策覆盖率停在 41%"→ 现为 **146/209（70%）**；
（c）"8 个条目来源为通用概念页（round 50）"→ 8 条**均已补专属来源**，已解决。
已在顶部加"当前阻塞快照（round 145 复核）"，并对三节加【round145 复核：已解决/已改善】标注。真实阻塞仅剩：**维基网络不可用**（3 条缺全文 + 5 条缓存缺口）。
②**DECISIONS.md 关键矛盾**：D08 原文"写 ALL_DONE 于全部完成后"与现行 **AUTONOMOUS"永不写 ALL_DONE、饱和为唯一终态"直接冲突**——已加标注说明后者取代之（"每轮≤40条"仍有效）；D04"100 条目标"已被实际 641 条取代，加注；`url2` 表述中的陈旧"741"改为"来源库"。
③现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；案例政策覆盖 """ + str(pr) + """ 条；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 25/25。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OE', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 2, 'fixed': 4,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 25/25',
    'spot_check': 'BLOCKERS 三处陈旧已核正（2020已建/政策70%/8条已补源）；DECISIONS D08 ALL_DONE矛盾标注',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 125 轮可用（round 145）**。**核查 BLOCKERS.md 与 DECISIONS.md，修正多处陈旧/自相矛盾记录**。
- **BLOCKERS.md 陈旧三处**（经核实）：
  - 「库缺 2020 新冠股灾一条」→ **`covid-crash-2020` 已建成**，说法错误
  - 「案例政策覆盖率停在 41%」→ 现为 **146/209（70%）**
  - 「8 个条目来源为通用概念页（round 50）」→ 8 条**均已补专属来源**，已解决
  - 已在顶部加「当前阻塞快照（round 145 复核）」，并对三节加【已解决/已改善】标注。真实阻塞仅剩**维基网络不可用**（3 条缺全文 + 5 条缓存缺口）。
- **DECISIONS.md 关键矛盾**：D08 原文「写 ALL_DONE 于全部完成后」与现行 **AUTONOMOUS「永不写 ALL_DONE、饱和为唯一终态」直接冲突**——已加标注说明后者取代之；D04「100 条目标」已被实际 641 条取代，加注；`url2` 陈旧数字已改。
- 现状：**641 条**、来源 **742**、页面 **655**；案例政策覆盖 **146** 条；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 25/25。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | pr', pr, '| avg', avg)
