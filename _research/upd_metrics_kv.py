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
reln = [len(e.get('related', [])) for e in es]

note = (
    "维基第95轮可用。KU-KV：扩写 30 条核心概念（WARNINGS 305 → 275）。"
    "①第一批 16 条（95—96 字 → 411—512 字）：adverse-selection／austerity／behavioral-finance／"
    "bond／classical-economics／core-inflation／fiat-money／hot-money／odious-debt／"
    "representative-money／speculation／capital-structure／collateral／debt-restructuring／"
    "haircut-finance／quantitative-easing。"
    "②第二批 14 条（94—97 字 → 414—567 字）：tragedy-commons／velocity-of-money／volatility／"
    "arbitrage／cryptocurrency／currency-union／division-of-labour／exchange-rate-regime／"
    "exorbitant-privilege／hyperinflation／insider-trading／liquidity-risk／convertible-bond／world-bank。"
    "③**本轮扩写中出现几处特别有价值的「易错点」**："
    "**velocity-of-money** 解释了「为什么量化宽松没引发高通胀」——"
    "M 上升而 V 骤降，且点明「若信心恢复、V 回升，前期积累的货币存量可能迅速转化为通胀」；"
    "**volatility** 指出「风险的度量本身会改变风险」——"
    "低波动率诱发加杠杆、波动率骤升强制减仓；"
    "**liquidity-risk** 把融资流动性与市场流动性拆开，并说明两者如何**互相强化**；"
    "**haircut-finance** 点出「haircut 上调等于在不改变价格的情况下抽走流动性」；"
    "**tragedy-commons** 把系统性风险类比为「金融的公地」，"
    "直接支撑宏观审慎监管的正当性；"
    "**odious-debt** 与 **cryptocurrency** 两处明确守住本库边界——"
    "前者「不对具体国家的债务性质作判断」，后者指出 FTX 的教训是"
    "「同样的金融活动若处在监管边界之外，失败将由客户全额承担」。"
    "④**round 94 的接线检查再次生效**：30 条扩写引入多处「见 xxx」未入 related，"
    "用既定脚本批量修复（补入 21 条、对称化 16 条）。"
    "⑤现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字、related 平均 " + str(round(sum(reln) / len(reln), 1)) +
    " 条；ERRORS 0、WARNINGS " + str(len(short)) + "（R22）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作KU-KV', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 30, 'reviewed': 305, 'fixed': 37,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 275（R22）+ 自测 18/18',
    'spot_check': '扩写 30 条核心概念；批量修复接线',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 95 轮可用（round 114）**。**扩写 30 条核心概念（WARNINGS 305 → 275）**。
- **第一批 16 条**（95—96 字 → 411—512 字）：adverse-selection／austerity／behavioral-finance／bond／classical-economics／core-inflation／fiat-money／hot-money／odious-debt／representative-money／speculation／capital-structure／collateral／debt-restructuring／haircut-finance／quantitative-easing。
- **第二批 14 条**（94—97 字 → 414—567 字）：tragedy-commons／velocity-of-money／volatility／arbitrage／cryptocurrency／currency-union／division-of-labour／exchange-rate-regime／exorbitant-privilege／hyperinflation／insider-trading／liquidity-risk／convertible-bond／world-bank。
- **本轮出现几处特别有价值的「易错点」**：

  | 条目 | 关键判断 |
  |---|---|
  | `velocity-of-money` | 解释「**为什么量化宽松没引发高通胀**」——M 上升而 V 骤降；并点明若信心恢复、V 回升，积累的货币可能迅速转为通胀 |
  | `volatility` | **风险的度量本身会改变风险**——低波动率诱发加杠杆，波动率骤升强制减仓 |
  | `liquidity-risk` | 把**融资流动性**与**市场流动性**拆开，说明两者如何互相强化 |
  | `haircut-finance` | **haircut 上调等于在不改变价格的情况下抽走流动性** |
  | `tragedy-commons` | 把系统性风险类比为「**金融的公地**」，直接支撑宏观审慎监管的正当性 |
  | `odious-debt` | **不对具体国家的债务性质作判断**（守住边界） |
  | `cryptocurrency` | FTX 的教训：**同样的金融活动若处在监管边界之外，失败将由客户全额承担** |

- **round 94 的接线检查再次生效**：30 条扩写引入多处「见 xxx」未入 `related`，用既定脚本批量修复（补入 21 条、对称化 16 条）。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 430 字**；**ERRORS 0**、WARNINGS 275（R22）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作KP-KT｜2026-11-24｜状态：641条；扩写30条机制类核心概念（R22 335→305）**',
              '**续作KU-KV｜2026-11-24｜状态：641条；再扩写30条核心概念（R22 305→275）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| overview 平均', avg)
