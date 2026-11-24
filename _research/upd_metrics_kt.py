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
    "维基第94轮可用。KP-KT：扩写 30 条机制类核心概念（WARNINGS 335 → 305）。"
    "①本轮选择**机制类**而非工具类：跳过 beta（贝塔系数）这类纯统计指标，"
    "优先处理对理解危机有实质作用的条目。"
    "②第一批 15 条（74—92 字 → 363—478 字）：herd-behavior／bank-failure／"
    "collateralized-debt-obligation／new-classical／adaptive-expectations／resource-curse／"
    "credit-default-swap／quantitative-tightening／risk-premium／fear-of-floating／"
    "information-asymmetry／central-bank-independence／global-imbalances／federal-reserve／duration-finance。"
    "③第二批 15 条（82—93 字 → 406—501 字）：initial-public-offering／stock-exchange／"
    "discount-window／fx-intervention／mortgage-backed-security／primary-market／"
    "capital-requirement／country-risk／dollarization／keynesian-economics／market-maker／"
    "market-risk／marginal-utility／bill-of-exchange／kondratiev。"
    "④**扩写的重点不是字数，是补上「机制」与「易错点」**。例："
    "**discount-window** 点明「污名」问题——银行怕被解读为出问题而不敢申请，"
    "使该工具在最需要时反而不被使用；"
    "**market-maker** 指出做市商「没有义务在压力下继续做市」，"
    "于是流动性在最需要的时刻蒸发；"
    "**country-risk** 区分「主权风险」与「国家风险」——"
    "后者包括外汇管制等「债务人有能力但国家让它付不出去」的情形；"
    "**dollarization** 指出它把危机形态从汇率危机转为银行与债务危机，"
    "且失去最后贷款人能力；"
    "**kondratiev** 明确记为「描述性假说而非可操作预测工具」，"
    "并声明本库不据此作周期判断（守住「不作预测」规则）；"
    "**duration-finance** 直接连到 2023 年硅谷银行——长久期债券在加息后的浮亏。"
    "⑤过程中又遇两处引号笔误导致语法错误，按报错定位修正。"
    "⑥**round 94 的接线检查再次生效**：30 条扩写引入 5 处「见 xxx」引用未入 related，"
    "被 check_pages 报出；用 round 94 的扫描逻辑批量修复（补入 15 条 related、对称化 20 条）。"
    "⑦现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) + "（R22 提示）。"
    "十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作KP-KT', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 30, 'reviewed': 345, 'fixed': 35,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 305（R22）+ 自测 18/18',
    'spot_check': '扩写 30 条机制类核心概念；批量修复 5 处未接线',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 94 轮可用（round 113）**。**扩写 30 条机制类核心概念（WARNINGS 335 → 305）**。
- **选择标准**：跳过 `beta`（贝塔系数）这类**纯统计指标**，优先处理对理解危机有实质作用的条目。
- **两批各 15 条**（74—93 字 → 406—501 字）。
- **扩写的重点不是字数，是补上「机制」与「易错点」**：

  | 条目 | 补充的关键判断 |
  |---|---|
  | `discount-window` | **「污名」问题**——银行怕被解读为出问题而不敢申请，使该工具在最需要时反而不被使用 |
  | `market-maker` | 做市商**没有义务在压力下继续做市**，于是流动性在最需要的时刻蒸发 |
  | `country-risk` | 区分「主权风险」与「国家风险」——后者含外汇管制等**「债务人有能力但国家让它付不出去」**的情形 |
  | `dollarization` | 把危机形态从**汇率危机**转为**银行与债务危机**，且失去最后贷款人能力 |
  | `kondratiev` | 明确记为「**描述性假说而非可操作预测工具**」，并声明本库不据此作周期判断（守住「不作预测」规则） |
  | `duration-finance` | 直接连到 2023 年硅谷银行——**长久期债券在加息后的浮亏** |

- **round 94 的接线检查再次生效**：30 条扩写引入 5 处「见 xxx」未入 `related`，被 `check_pages` 报出；用 round 94 的扫描逻辑批量修复（补入 15 条、对称化 20 条）。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 390 字**；**ERRORS 0**、WARNINGS 305（R22 提示）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作KK-KO｜2026-11-24｜状态：641条；清理201条套话，发现335条内容过短（R22）**',
              '**续作KP-KT｜2026-11-24｜状态：641条；扩写30条机制类核心概念（R22 335→305）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| overview 平均', avg)
