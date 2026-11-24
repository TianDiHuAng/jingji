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

note = """维基第124轮可用。OD：核查 BACKLOG.md，**发现多条"真实缺口"其实早已建成**，已重写并加防回归检查。
①**发现陈旧**：BACKLOG 停在"轮次26起点"，头部"核心29全L3/重要59全L2"为旧数；
其"真实缺口"表把 `bank-resolution`／`taper-tantrum`／`leading-indicator`／`self-insurance`／`risk-pooling`／
`secured-lending`／`bank-holiday` 等**7 条其实早已建成**的条目仍列为"缺"——正是 round 77 依过时清单重复建条目的同源风险。
②**核实与重写**：逐条核对 entries，13 条"曾列待建"实已建成；剩余未建（sacrifice-ratio／term-premium／
regulatory-arbitrage／audit-failure／disclosure／rogue-trader／short-term-rate／agriculture）多为**无专属来源/范围过宽**，属来源可得性限制。BACKLOG 已按当前实际重写（网络遗留、概念缺口结论、已建成清单、历史待办留档）。
③**加固 check_docs**：新增守卫——解析 BACKLOG"概念缺口"表，若其中出现**已建成的 id** 则判失败（防依过时清单重复建）。注入测试（塞入 bank-resolution）确认能捕获。
④**纳入自测**：新增"BACKLOG 缺口含已建条目"用例，自测 24 → **25 项**，全通过；同步更新 HEALTH_CHECK。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 25/25。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OD', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 25, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 25/25',
    'spot_check': 'BACKLOG 重写（7 条已建成不再列为缺口）；check_docs 加缺口含已建条目守卫；自测 24→25',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 124 轮可用（round 144）**。**核查 BACKLOG.md，发现多条「真实缺口」其实早已建成**，已重写并加防回归检查。
- **发现陈旧**：BACKLOG 停在「轮次26起点」，且其「真实缺口」表把 `bank-resolution`／`taper-tantrum`／`leading-indicator`／`self-insurance`／`risk-pooling`／`secured-lending`／`bank-holiday` 等**7 条其实早已建成**的条目仍列为「缺」——正是 **round 77 依过时清单重复建条目**的同源风险。
- **核实与重写**：逐条核对 entries，**13 条「曾列待建」实已建成**；剩余未建（sacrifice-ratio／term-premium／regulatory-arbitrage／audit-failure／disclosure／rogue-trader／short-term-rate／agriculture）多为**无专属来源/范围过宽**，属来源可得性限制。BACKLOG 已按当前实际重写。
- **加固 check_docs**：新增守卫——解析 BACKLOG「概念缺口」表，若其中出现**已建成的 id** 则判失败。注入测试（塞入 bank-resolution）确认能捕获。
- **纳入自测**：新增「BACKLOG 缺口含已建条目」用例，自测 24 → **25 项**；同步更新 HEALTH_CHECK。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 25/25。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
