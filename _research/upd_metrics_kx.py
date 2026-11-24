# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts

c = counts(es)
short = [e for e in es if e.get('tier') in ('核心', '重要') and len(e.get('overview') or '') < 150]
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))

note = (
    "维基第96轮可用。KW-KX：扩写 30 条（WARNINGS 275 → 245）。"
    "①第一批 17 条：token-money／double-entry／history-of-money／economic-history／iosco／"
    "kitchin-cycle／money-market／put-option／real-business-cycle／usury／bid-ask／"
    "current-account／de-dollarization／depression-economics／economic-recession／"
    "minsky-moment／monetary-policy。"
    "②第二批 13 条：monetary-transmission／option／prudential-regulation／welfare-economics／"
    "financial-inclusion／fiscal-dominance／free-trade／futures／gatt／legal-tender／"
    "leverage-cycle／loanable-funds／beta（连纯工具指标也一并补齐）。"
    "③**几处值得单列的判断**："
    "**double-entry** 指出危机中的会计根源几乎从不是「算错」，"
    "而是「**该记的没记进去**」（表外、估值假设、合并范围）；"
    "**bid-ask** 强调价差扩大可在**价格几乎不变**时发生——"
    "它衡量的不是「资产值多少」而是「**现在还能不能交易**」；"
    "**minsky-moment** 明确澄清明斯基**未给出「何时」的公式**，"
    "该概念是描述机制的、不是择时信号；"
    "**beta** 点出危机中「**所有相关性都变成 1**」，使基于 β 的对冲同时失效；"
    "**loanable-funds** 指出可贷资金是「流量」框架而现代银行是「内生货币」，"
    "因此「储蓄池决定可贷资金」在有银行体系的经济中并不成立；"
    "**financial-inclusion** 把「包容与稳定的张力」讲清——"
    "问题不在「穷人获得信贷」，而在**掠夺性条款与审慎标准的放弃**；"
    "**kitchin／kondratiev 两类周期**均注明统计基础有争议、本库不据周期位置作预测。"
    "④**round 94 的接线检查再次生效**，用既定脚本批量修复并对称化 34 条。"
    "⑤现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) +
    "（R22）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作KW-KX', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 30, 'reviewed': 275, 'fixed': 30,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 245（R22）+ 自测 18/18',
    'spot_check': '扩写 30 条（含 beta）；批量修复接线并对称化 34 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 96 轮可用（round 115）**。**扩写 30 条（WARNINGS 275 → 245）**。
- **第一批 17 条**：token-money／double-entry／history-of-money／economic-history／iosco／kitchin-cycle／money-market／put-option／real-business-cycle／usury／bid-ask／current-account／de-dollarization／depression-economics／economic-recession／minsky-moment／monetary-policy。
- **第二批 13 条**：monetary-transmission／option／prudential-regulation／welfare-economics／financial-inclusion／fiscal-dominance／free-trade／futures／gatt／legal-tender／leverage-cycle／loanable-funds／**beta**（连纯工具指标也一并补齐）。
- **几处值得单列的判断**：

  | 条目 | 关键判断 |
  |---|---|
  | `double-entry` | 危机的会计根源几乎从不是「算错」，而是「**该记的没记进去**」（表外、估值假设、合并范围） |
  | `bid-ask` | 价差扩大可在**价格几乎不变**时发生——它衡量的不是「资产值多少」而是「**现在还能不能交易**」 |
  | `minsky-moment` | 明斯基**未给出「何时」的公式**；该概念是描述机制的、**不是择时信号** |
  | `beta` | 危机中「**所有相关性都变成 1**」，使基于 β 的对冲同时失效 |
  | `loanable-funds` | 可贷资金是「流量」框架，而现代银行是「**内生货币**」——「储蓄池决定可贷资金」在有银行体系的经济中并不成立 |
  | `financial-inclusion` | 问题不在「穷人获得信贷」，而在**掠夺性条款与审慎标准的放弃** |
  | `kitchin`／`kondratiev` | 两类周期均注明**统计基础有争议，本库不据周期位置作预测** |

- **round 94 的接线检查再次生效**，用既定脚本批量修复并对称化 34 条。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 470 字**；**ERRORS 0**、WARNINGS 245（R22）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作KU-KV｜2026-11-24｜状态：641条；再扩写30条核心概念（R22 305→275）**',
              '**续作KW-KX｜2026-11-24｜状态：641条；再扩写30条（R22 275→245）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| avg', avg)
