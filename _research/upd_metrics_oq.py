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

note = """维基第134轮可用。OQ：网络仍不可用；修 related 孤岛并加 R24。
①**网络复测**：en wikipedia 仍 URLError，本会话持续不可用。
②**related 一致性复核**：发现 **3 条条目无任何 related 入链**（`cook-islands-currency`／`haitian-independence-debt`／`recession-1960-1961`）。注意：另有 366 处"单向 related"多为**枢纽概念被广泛引用**（如 bank-run 被数百条指向），**全对称会让枢纽 related 爆炸，不宜强行对称**；仅对这 3 条各补一条反向链接（currency-board／sovereign-default／recession）。修后 **related 孤岛 = 0**。
③**固化为检查 R24**：每条目应至少被一条 related 引用，否则 warning（防孤岛再现）。注入测试（移除 currency-board→cook-islands-currency）确认能捕获。
④**纳入自测**：新增"R24 related孤岛"用例，自测 28 → **29 项**；同步更新 HEALTH_CHECK（R1–R24、自测 29）。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 29/29。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OQ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 4, 'reviewed': 641, 'fixed': 4,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 29/29',
    'spot_check': '修 3 条 related 孤岛；加 R24；自测 28→29',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 134 轮可用（round 154）**。**网络仍不可用；修 related 孤岛并加 R24**。
- **网络复测**：en wikipedia 仍 URLError，本会话持续不可用。
- **related 一致性复核**：发现 **3 条条目无任何 related 入链**（`cook-islands-currency`／`haitian-independence-debt`／`recession-1960-1961`）。注意：另 366 处「单向 related」多为**枢纽概念被广泛引用**（如 bank-run 被数百条指向），**全对称会让枢纽 related 爆炸，不宜强行对称**；仅对这 3 条各补一条反向链接（currency-board／sovereign-default／recession）。修后 **related 孤岛 = 0**。
- **固化为检查 R24**：每条目应至少被一条 related 引用，否则 warning。注入测试确认能捕获。
- **纳入自测**：新增「R24 related孤岛」用例，自测 28 → **29 项**；同步更新 HEALTH_CHECK（R1–R24、自测 29）。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 29/29。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
