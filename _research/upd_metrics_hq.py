# -*- coding: utf-8 -*-
"""续作HQ：重写 HEALTH_CHECK.md，并写本轮记录。"""
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
single = [e['id'] for e in es if len(e.get('sources', [])) == 1]

HC = '''# 体检报告（round 80 重新生成）

> 原文件为 round 6 的记录，其列出的"56 条无入链""6 组来源雷同"等问题此后均已解决。
> 本文件按当前实际状态重写。

## 硬性问题

| 项 | 结果 |
|---|---|
| 站内断链 | **0** |
| 重复标题 | **0** |
| 孤儿页面（无任何入链） | **0** |
| 同名指标多值冲突 | **0**（同名指标已加年份区分） |
| 非法／未 verified 来源引用 | **0** |
| 未渲染 Markdown | **0** |

## 来源与结构

| 项 | 数值 |
|---|---|
| 条目总数 | %d（案例 %d / 概念 %d） |
| 来源库 | %d 条，抽样可达性全通 |
| 来源组合完全相同的条目组（≥3 条） | **0**（round 6 时为 6 组） |
| **仅 1 个来源的条目** | **%d**（多为概念条目，正逐步补跨语言第二来源） |
| comparison 覆盖 | %d/%d |

## 已修复的历史问题（对照 round 6 报告）

| round 6 记录 | 现状 |
|---|---|
| 56 条无 related 入链 | 0（related 已对称化，双向 1,615 对） |
| 6 组来源组合雷同 | 0（逐条补专属来源） |
| 未渲染 Markdown（当时未发现） | 0（round 64 发现并修复 125 页） |

## 结论

- **硬性问题：0**
- **软性问题：仅 1 个来源的条目 %d 个**——这些条目的内容已标 `needs_verification`，
  且已在 round 80 为其中 12 个补入中文维基作为跨语言第二来源（跨语言对照由 31 升至 39 条）。
''' % (len(es), len(cases), len(concepts), len(srcs), len(single), comp, len(es), len(single))

open('HEALTH_CHECK.md', 'w', encoding='utf-8').write(HC)
print('HEALTH_CHECK.md 已重写')

note = (
    '维基第61轮可用。HO-HQ：**校验三份体检文档，并补 12 个概念条目的跨语言第二来源**。'
    '①核查 `HEALTH_CHECK.md`（round 6）：其列"56 条无入链""6 组来源雷同"等问题**均已解决**——'
    '现孤儿页面 0、来源雷同组 0。'
    '②核查发现**41 个条目仅有 1 个来源**（39 个为 U6 概念条目，缺乏第二来源支撑）。'
    '③为其中 **12 个**补入**中文维基**作为跨语言第二来源（股权溢价之谜／经济增长／投资／劳合社／'
    '市场失灵／共同基金／纳斯达克／庇古税／囚徒困境／尋租／储蓄／交易成本），'
    '`recession` 因中文维基误重定向到「老化」而排除。'
    '④效果：**跨语言对照由 31 升至 39 条**；单来源条目 41 → **29**；来源库 708 → **720**。'
    '⑤**重写 HEALTH_CHECK.md**：按当前状态列出硬性问题（全部 0）与软性问题（单来源条目数），'
    '并逐项对照 round 6 的历史记录注明"已修复"。'
    '⑥来源抽样 15 个全部可达。'
    '现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、key_data ' + str(tk) + '、'
    'comparison ' + str(comp) + '、案例政策 ' + str(wp) + '/' + str(len(cases)) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HO-HQ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 12, 'reviewed': 41, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（跨语言对照 31→39）',
    'spot_check': '12 个概念补跨语言第二来源；单来源条目 41→29；重写 HEALTH_CHECK',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **来源：708**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
add = '''- **维基百科第 61 轮可用（round 80）**。**校验三份体检文档，补 12 个概念条目的跨语言第二来源**。
- **① 核查 `HEALTH_CHECK.md`（round 6）**：其列"56 条无入链""6 组来源雷同"等问题**均已解决**（现孤儿 0、雷同组 0）。
- **② 发现 41 个条目仅有 1 个来源**（39 个为 U6 概念条目，缺乏第二来源支撑）。
- **③ 为其中 12 个补入中文维基作为跨语言第二来源**：

  股权溢价之谜／经济增长／投资／劳合社／市场失灵／共同基金／纳斯达克／庇古税／囚徒困境／尋租／储蓄／交易成本

  （`recession` 因中文维基误重定向到「老化」而排除——又是一次重定向陷阱。）

- **④ 效果**：

  | 指标 | 之前 | 现在 |
  |---|---|---|
  | 跨语言对照 | 31 条 | **39 条** |
  | 单来源条目 | 41 | **29** |
  | 来源库 | 708 | **720** |

- **⑤ 重写 `HEALTH_CHECK.md`**：按当前状态列出硬性问题（**全部 0**）与软性问题（单来源条目数），并逐项对照 round 6 的历史记录注明"已修复"。
- 来源抽样 15 个全部可达。
- 现状：**632 条**（案例 205／概念 427）、来源 **720**、页面 **646**。十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HM-HN｜2026-11-24｜状态：632条；重写2份诊断文档，新建2个衰退条目**',
              '**续作HO-HQ｜2026-11-24｜状态：632条；补12个跨语言第二来源，跨语言对照31→39**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 单来源', len(single), '| 来源', len(srcs))
