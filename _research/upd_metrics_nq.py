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

note = """维基第117轮可用。NP-NQ：验证渲染层，发现并修复 3 页残留未渲染 `**`。
①扫描全部 655 个生成页面：`>None<`／`>nan<`／`{}`／"list' object"／`>True<`／`>False<` **均为 0**；
`&lt;` 出现 5 页但属**正常的 `<` 转义**（"β < 1""< 潜在"），非 bug。
②**发现真实渲染问题**：`capital-flight`／`financial-accelerator`／`short-selling` 3 页残留未渲染的 `**`——
根源是这些 overview 中 `**...**` **局部嵌套/奇数配对**（如 `**核心之一是**"…"**。`），
`mdesc` 的非贪婪配对错位后留下孤立 `**`。
③**双重修复**：
（a）**防御性**：`mdesc` 完成成对替换后，若仍有残留 `**` 则**直接剥除**——保证任何页面都不可能显示字面 `**`；
（b）**数据修正**：修正这 3 条 overview 中不平衡的 `**` 标记（如把 `**关键的政策含义**：**修复净值**（…` 改为单一包裹）。
④复查：全部页面 `**` 残留 **归零**；`check_quality` 未渲染粗体 0 项。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 18/18。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NP-NQ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 655, 'fixed': 4,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 18/18（渲染 `**` 残留归零）',
    'spot_check': '渲染层全扫 655 页；修 3 页未渲染 ** + mdesc 防御剥除',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 117 轮可用（round 137）**。**验证渲染层，发现并修复 3 页残留未渲染 `**`**。
- **扫描全部 655 个生成页面**：`>None<`／`>nan<`／`{}`／`list' object`／`>True<`／`>False<` **均为 0**；`&lt;` 出现 5 页但属**正常的 `<` 转义**（「β < 1」「< 潜在」），非 bug。
- **发现真实渲染问题**：`capital-flight`／`financial-accelerator`／`short-selling` 3 页残留未渲染的 `**`——根源是这些 overview 中 `**...**` **局部嵌套/奇数配对**（如 `**核心之一是**"…"**。`），`mdesc` 非贪婪配对错位后留下孤立 `**`。
- **双重修复**：
  - **防御性**：`mdesc` 完成成对替换后，若仍有残留 `**` 则**直接剥除**——保证任何页面都不可能显示字面 `**`
  - **数据修正**：修正这 3 条 overview 中不平衡的 `**` 标记
- **复查**：全部页面 `**` 残留 **归零**；`check_quality` 未渲染粗体 0 项。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NO｜2026-11-24｜状态：641条；3条重要概念补第二派schools（两派628条）**',
              '**续作NP-NQ｜2026-11-24｜状态：641条；渲染层验证，修复3页未渲染**并加防御剥除**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
