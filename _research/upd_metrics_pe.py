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

note = """维基第146轮可用。PE：渲染与"验证页诚实性"核查，均通过（无数据改动）。
①**网络**：仍 URLError。
②**渲染核查**：抽查 site/lehman.html —— 12 个章节（概述/时间线/触发机制/关键数据/各方解释/政策/比较/一图示意/L3深度说明/L3深度图/待核实/来源）齐全，style.css 挂载、内联 SVG 与来源外链均在，title 规范。最终产物渲染正常。
③**验证页诚实性审计**：`gen_site` 分类逻辑严谨——"独立机构印证"须有 `fed-*` 或机构独立文献 + "印证"关键词，且排除"不构成独立/系转引"；"统计口径对照""跨语言对照"均带诚实免责声明（明示不构成独立互证）。实际 **2 条独立机构印证**经核实均为真·独立：`black-monday-1987`（fed-stock-crash-1987）、`wall-street-1929`（fed-stock-crash-1929）——均有美联储历史站独立文献佐证，非仅维基。
④本轮无数据改动；十一道检查全绿、自测 34/34。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 34/34。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PE', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 2, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 34/34',
    'spot_check': '渲染核查(lehman 页 12 章节完整)+验证页诚实性审计(2 条独立印证真实)，无数据改动',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 146 轮可用（round 166）**。**渲染与「验证页诚实性」核查，均通过（无数据改动）**。
- **网络**：仍 URLError。
- **渲染核查**：抽查 `site/lehman.html`——12 个章节（概述/时间线/触发机制/关键数据/各方解释/政策/比较/一图示意/L3 深度说明/L3 深度图/待核实/来源）齐全，style.css 挂载、内联 SVG 与来源外链均在，title 规范。最终产物渲染正常。
- **验证页诚实性审计**：`gen_site` 分类逻辑严谨——「独立机构印证」须有 `fed-*` 或机构独立文献 + 「印证」关键词，且排除「不构成独立/系转引」；「统计口径对照」「跨语言对照」均带诚实免责声明。实际 **2 条独立机构印证**经核实均为真·独立：`black-monday-1987`、`wall-street-1929`——均有美联储历史站独立文献佐证，非仅维基。
- 本轮无数据改动；十一道检查全绿、自测 34/34。
- 现状：**641 条**、来源 **740**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 34/34。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
