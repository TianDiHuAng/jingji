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

note = """维基第144轮可用。PC：数据卫生扫描干净；来源库结构审计发现并合并 2 组同 URL 重复来源；加 R28。
①**网络**：仍 URLError。
②**数据卫生扫描（全 641 条）**：重复 key_data label **0**、重复 schools holder **0**、重复 timeline 事件 **0**、空字段 **0**——数据内部一致。
③**来源库结构审计**：count 742=实际、无重复 id、无缺字段、verified/link_ok 全 true、type 均合法；**发现 2 组同 URL 重复来源**（同一维基页登记了两个 id）：
`w-en-capital-adequacy`→`w-en-capital-requirement`（同 Capital_requirement）、`w-en-bank-holiday`→`w-en-emergency-banking-act-1933`（同 EBRA）。
④**合并**：递归重映射 entries 全部 sources/src 字段、去重、删重复来源，**来源库 742 → 740**；无残留引用、无重复 URL、check 0/0。
⑤**固化 R28**：来源 URL 不得重复。自测 32 → **33 项**；同步 REPORT/HEALTH（来源 740、R1–R28、自测 33）。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 33/33。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PC', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 4, 'reviewed': 641, 'fixed': 3,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 33/33',
    'spot_check': '数据卫生干净；合并 2 组重复 URL 来源（742→740）+ R28，自测 33',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 144 轮可用（round 164）**。**数据卫生扫描干净；来源库结构审计发现并合并 2 组同 URL 重复来源；加 R28**。
- **网络**：仍 URLError。
- **数据卫生扫描（全 641 条）**：重复 key_data label **0**、重复 schools holder **0**、重复 timeline 事件 **0**、空字段 **0**。
- **来源库结构审计**：count 742=实际、无重复 id、无缺字段、verified/link_ok 全 true、type 均合法；**发现 2 组同 URL 重复来源**（同一维基页登记了两个 id）：`w-en-capital-adequacy`→`w-en-capital-requirement`（Capital_requirement）、`w-en-bank-holiday`→`w-en-emergency-banking-act-1933`（EBRA）。
- **合并**：递归重映射 entries 全部 sources/src 字段、去重、删重复来源，**来源库 742 → 740**；无残留引用、无重复 URL、check 0/0。
- **固化 R28**：来源 URL 不得重复。自测 32 → **33 项**；同步 REPORT/HEALTH（来源 740、R1–R28、自测 33）。
- 现状：**641 条**、来源 **740**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 33/33。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | sources', len(srcs), '| avg', avg)
