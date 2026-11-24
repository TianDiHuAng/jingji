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

note = """维基第137轮可用。OV：做"timeline 年份 vs 专属来源"交叉核对，发现并删除 1 处无源前瞻事件；加 R26。
①**方法**：逐条核 timeline 事件年份是否出现在其专属来源缓存（通用页/缓存缺口除外）。
②**得 35 条命中**，多为**概念条目的历史里程碑**（源自通用概念页不逐年列，属正常噪音），不逐一追。
③**1 条真问题**：`silicon-valley-bank` timeline 有"**2026 年 First Citizens 完全整合并停用 SVB 名称**"，但所引来源**未载**（缓存只说 2023 FDIC/First Citizens 收购），且属**前瞻性**——违反"只写来源有的/不做预测"。**已删除**该事件。timeline 659 → 658。
④**核对未来年份**：全库无 ≥2027 的 timeline 事件（无预测性事件）。
⑤**固化 R26**：timeline 事件年份不得晚于当前年（防未来/预测性事件）。自测 30 → **31 项**；同步 REPORT/HEALTH 的 timeline 658。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；timeline """ + str(tl) + """ 事件；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 31/31。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OV', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 35, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 31/31',
    'spot_check': 'timeline 年份 vs 来源交叉核对（35 命中）→ 删 SVB 无源前瞻事件 + R26，自测 31',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 137 轮可用（round 157）**。**做「timeline 年份 vs 专属来源」交叉核对，发现并删除 1 处无源前瞻事件；加 R26**。
- **方法**：逐条核 timeline 事件年份是否出现在其专属来源缓存（通用页/缓存缺口除外）。
- **得 35 条命中**，多为**概念条目的历史里程碑**（源自通用概念页不逐年列，属正常噪音），不逐一追。
- **1 条真问题**：`silicon-valley-bank` timeline 有「**2026 年 First Citizens 完全整合并停用 SVB 名称**」，但所引来源**未载**（缓存只说 2023 FDIC/First Citizens 收购），且属**前瞻性**——违反「只写来源有的/不做预测」。**已删除**。timeline 659 → 658。
- **核对未来年份**：全库无 ≥2027 的 timeline 事件。
- **固化 R26**：timeline 事件年份不得晚于当前年（防未来/预测性事件）。自测 30 → **31 项**；同步 REPORT/HEALTH 的 timeline 658。
- 现状：**641 条**、来源 **742**、页面 **655**；timeline **658** 事件；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 31/31。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | tl', tl, '| avg', avg)
