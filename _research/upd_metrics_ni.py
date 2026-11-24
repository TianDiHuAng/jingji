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

note = """维基第113轮可用。ND-NI：继续内容抽查，发现并修复"来源错标"与"缓存缺口"两类结构性问题。
①one_line 日期/数字 vs 来源：24 条数字疑点全为**单位换算假阴性**（亿/万↔billion/million）；日期检查 0 命中（说明 blue-monday 那类日期错已不存在）。
②one_line 年份 vs 来源：9 条疑点，逐一核对——多为区间/短缓存，其中 russian 的"1540"是金额被误当年份（假阳性）。
③**发现"缓存缺口"6 条**：dutch-stock-crashes／panic-1896／panic-1910／us-video-game-crash-1983／yemen-currency-divergence（另 recession 为概念条目属正常）——其 `wiki_full` 缓存存的是**通用页**（Currency crisis／Economic bubble／Bank run）而非专属来源页。**但条目内容经人工阅读核对准确、引用正确**，只是本地无法逐数核对。已在各 pending_notes 注明，并写入 BACKLOG（网络恢复后补抓专属页）。
④**修复 kipper-wipper-1618 日期不一致**：标题原"1618–1622"、概述"约1618—1623"、来源记"1619–1623"彼此冲突；统一为"约1618–1623"并注明来源年份（Kindleberger 记 1619–1623、最严重贬损 1620–1623）。
⑤**修复 cameroon-crisis-1987 来源错标**：key_data 的 18%／$150m 与 timeline 原误标通用来源 `w-en-debt-crisis`，实则见于专属页 `w-en-cameroonian-economic-crisis`，已改正；1994 年 CFA 贬值 50% 不在所引来源中，改为"大幅贬值（幅度待核实）"。
⑥**系统修复 14 处 key_data 来源错标**：扫描全库"仅引通用页来源"的 key_data，逐一验证数字确在专属页缓存中，将其来源改为条目的专属来源（涉及 brexit／china-liquidity／souk-al-manakh／panic-1866／panic-1884／uk-secondary-banking-1973 等）。**0 条遗留**。
⑦现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 18/18。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作ND-NI', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 16, 'reviewed': 641, 'fixed': 17,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 18/18',
    'spot_check': '修 14 处 key_data 来源错标 + cameroon + kipper 日期；记录 6 条缓存缺口',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 113 轮可用（round 133）**。**继续内容抽查，发现并修复「来源错标」与「缓存缺口」两类结构性问题**。
- **one_line 日期/数字 vs 来源**：24 条数字疑点全为**单位换算假阴性**（亿/万↔billion/million）；日期检查 **0 命中**（说明 blue-monday 那类日期错已不存在）。
- **one_line 年份 vs 来源**：9 条疑点多为区间/短缓存，其中 russian 的「1540」是金额被误当年份（假阳性）。
- **发现「缓存缺口」6 条**：`dutch-stock-crashes`／`panic-1896`／`panic-1910`／`us-video-game-crash-1983`／`yemen-currency-divergence`（另 `recession` 为概念条目属正常）——其 `wiki_full` 缓存存的是**通用页**而非专属来源页。**但条目内容经人工阅读核对准确、引用正确**，只是本地无法逐数核对。已写入 `BACKLOG.md`（网络恢复后补抓专属页）。
- **修复 `kipper-wipper-1618` 日期不一致**：标题「1618–1622」、概述「约1618—1623」、来源记「1619–1623」彼此冲突；统一为「约1618–1623」并注明来源年份。
- **修复 `cameroon-crisis-1987` 来源错标**：key_data 的 18%／$150m 与 timeline 原误标通用来源 `w-en-debt-crisis`，实则见于专属页 `w-en-cameroonian-economic-crisis`，已改正；1994 年 CFA 贬值 50% 不在所引来源中，改为「大幅贬值（幅度待核实）」。
- **系统修复 14 处 key_data 来源错标**：扫描全库「仅引通用页来源」的 key_data，逐一验证数字确在专属页缓存中，将其来源改为条目的专属来源（涉及 `brexit-crash-2016`／`china-liquidity-2013`／`souk-al-manakh-1982`／`panic-1866`／`panic-1884`／`uk-secondary-banking-1973` 等）。**0 条遗留**。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NB-NC｜2026-11-24｜状态：641条；修正blue-monday-2009事件张冠李戴+无来源数字**',
              '**续作ND-NI｜2026-11-24｜状态：641条；修14处key_data来源错标+记录6条缓存缺口**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
