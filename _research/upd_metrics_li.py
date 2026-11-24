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
    "维基第101轮可用。LH-LI：扩写 21 条（WARNINGS 136 → 115）。"
    "①第一批 12 条：public-choice／reserve-currency／reserve-requirement／short-selling／"
    "time-inconsistency／wto／yield-curve／capital-flight／credit-risk／demographic-dividend／"
    "import-substitution／netting。"
    "②第二批 9 条：optimum-currency-area／says-law／tobin-tax／aggregate-supply／"
    "derivative／esrb／nairu／sarbanes-oxley／credit-rating。"
    "③**本轮几处关键判断**："
    "**time-inconsistency** 讲清了「为什么监管要提前设计」——"
    "事前最优是「绝不救助」，但事后必然救助，"
    "因此承诺不可信，**解决办法不是更坚定的承诺，而是改变事后的激励结构**；"
    "**credit-rating** 指出「评级依赖」是核心问题——"
    "当规则直接引用评级，评级就从「一种意见」变成「具有法律效力的开关」，"
    "降级触发被动抛售，形成 cliff effect；"
    "**sarbanes-oxley** 纠正一个常见误解——"
    "**它并未阻止 2008 年危机**，因为危机主体是不受该法约束的金融机构的风险承担；"
    "教训是「**针对上一次丑闻的改革，未必能防住下一次危机的形态**」；"
    "**yield-curve** 与 **nairu** 两处均明确「记录机制与历史证据，不据其作预测」，"
    "其中 nairu 坦承「该概念是有用的组织框架，但不是可靠的数值目标」；"
    "**netting** 区分三种层次，并指出终止净额在雷曼破产中的关键作用；"
    "**esrb** 点出宏观审慎的普遍困境——**成功是不可见的（没有发生的危机），成本是可见的**。"
    "④沿用三引号 + 保存前换行规范化，两批语法与渲染均一次通过。"
    "⑤**round 94 的接线检查再次生效**，批量修复并对称化 29 条。"
    "⑥现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) +
    "（R22）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作LH-LI', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 21, 'reviewed': 136, 'fixed': 21,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 115（R22）+ 自测 18/18',
    'spot_check': '扩写 21 条；对称化 29 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 101 轮可用（round 120）**。**扩写 21 条（WARNINGS 136 → 115）**。
- **第一批 12 条**：public-choice／reserve-currency／reserve-requirement／short-selling／time-inconsistency／wto／yield-curve／capital-flight／credit-risk／demographic-dividend／import-substitution／netting。
- **第二批 9 条**：optimum-currency-area／says-law／tobin-tax／aggregate-supply／derivative／esrb／nairu／sarbanes-oxley／credit-rating。
- **本轮几处关键判断**：

  | 条目 | 判断 |
  |---|---|
  | `time-inconsistency` | 讲清「**为什么监管要提前设计**」——事前最优是「绝不救助」，但事后必然救助，故承诺不可信；**解决办法不是更坚定的承诺，而是改变事后的激励结构** |
  | `credit-rating` | 「评级依赖」是核心问题——当规则直接引用评级，评级就从「一种意见」变成「**具有法律效力的开关**」，降级触发被动抛售（cliff effect） |
  | `sarbanes-oxley` | 纠正常见误解——**它并未阻止 2008 年危机**，因为危机主体是不受该法约束的金融机构的风险承担；教训是「**针对上一次丑闻的改革，未必能防住下一次危机的形态**」 |
  | `nairu` | 坦承「该概念是**有用的组织框架，但不是可靠的数值目标**」 |
  | `esrb` | 点出宏观审慎的普遍困境——**成功是不可见的（没有发生的危机），成本是可见的** |
  | `netting` | 区分三种层次，并指出**终止净额**在雷曼破产中的关键作用 |

- 沿用三引号 + 保存前换行规范化，两批**语法与渲染均一次通过**。
- **round 94 的接线检查再次生效**，批量修复并对称化 **29 条**。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 680 字**；**ERRORS 0**、WARNINGS 115（R22）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作LF-LG｜2026-11-24｜状态：641条；扩写24条（R22 161→136）**',
              '**续作LH-LI｜2026-11-24｜状态：641条；扩写21条（R22 136→115）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| avg', avg)
