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
con = [e for e in short if e['unit'].startswith('U6')]
cas = [e for e in short if not e['unit'].startswith('U6')]
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))

note = (
    "维基第104轮可用。LN-LO：扩写 27 条概念（WARNINGS 59 → 32）。"
    "**至此，27 条过短概念全部完成，剩余 32 条全部是案例。**"
    "①第一批 14 条：mundell-fleming／total-factor-productivity／fiscal-capacity／liquidity／"
    "fannie-mae／interest-rate-swap／solow-model／natural-rate-unemployment／credit-cycle／"
    "black-scholes／marshall-plan／twin-crises／carry-trade／cbdc。"
    "②第二批 13 条：neutrality-of-money／post-keynesian／repo／money-supply／securitization／"
    "wage-price-spiral／debt-ceiling／bailout／okuns-law／ldi-strategy／taylor-rule／"
    "triffin-dilemma／phillips-curve。"
    "③**本轮几处关键判断**："
    "**ldi-strategy** 点出 2022 年英国 LDI 危机的核心教训——"
    "「久期匹配若通过高杠杆实现，就把一个利率风险问题转化成了流动性风险问题，而后者要危险得多」；"
    "**bailout** 明确区分「救助（用公共资金）」与「减记（把损失强制分配给股东与债权人）」，"
    "核心分野是「谁承担损失」而非「机构是否存活」，"
    "并以塞浦路斯 2013 年为例说明 bail-in 触及存款时的巨大争议；"
    "**securitization** 与 **repo** 两处呼应同一机制——"
    "「风险是否真正转移到更有能力承担者手中，还是只是变得不可见」；"
    "**phillips-curve** 把三次理论修正（原始经验规律／长期垂直／理性预期抵消）"
    "串成一条线，并指出「它的每次失效都是宏观经济学重大转向的起点」；"
    "**twin-crises** 指出双危机的政策困境——"
    "「保卫汇率会压垮银行，救银行会耗尽储备」；"
    "**debt-ceiling** 指出它是「主权风险的非典型来源」——"
    "不是偿债能力不足，而是政治程序可能导致技术性违约。"
    "④沿用三引号 + 保存前换行规范化，两批语法与渲染均一次通过。"
    "⑤**round 94 的接线检查再次生效**，批量修复接线。"
    "⑥现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) +
    "（全部为案例）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作LN-LO', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 27, 'reviewed': 59, 'fixed': 27,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 32（全部为案例）+ 自测 18/18',
    'spot_check': '扩写 27 条概念，概念类全部完成；剩余 32 条均为案例',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 104 轮可用（round 124）**。**扩写 27 条概念（WARNINGS 59 → 32）**。**至此 27 条过短概念全部完成，剩余 32 条全部是案例。**
- **第一批 14 条**：mundell-fleming／total-factor-productivity／fiscal-capacity／liquidity／fannie-mae／interest-rate-swap／solow-model／natural-rate-unemployment／credit-cycle／black-scholes／marshall-plan／twin-crises／carry-trade／cbdc。
- **第二批 13 条**：neutrality-of-money／post-keynesian／repo／money-supply／securitization／wage-price-spiral／debt-ceiling／bailout／okuns-law／ldi-strategy／taylor-rule／triffin-dilemma／phillips-curve。
- **本轮几处关键判断**：

  | 条目 | 判断 |
  |---|---|
  | `ldi-strategy` | 2022 年英国 LDI 危机的教训——「**久期匹配若通过高杠杆实现，就把一个利率风险问题转化成了流动性风险问题，而后者要危险得多**」 |
  | `bailout` | 明确区分「救助（公共资金）」与「减记（损失强制分配给股东与债权人）」——核心分野是「**谁承担损失**」而非「机构是否存活」；塞浦路斯 2013 触及存款引发巨大争议 |
  | `phillips-curve` | 把三次理论修正（原始经验规律／长期垂直／理性预期抵消）串成一条线——「**它的每次失效都是宏观经济学重大转向的起点**」 |
  | `twin-crises` | 双危机的政策困境——「**保卫汇率会压垮银行，救银行会耗尽储备**」 |
  | `debt-ceiling` | 「**主权风险的非典型来源**」——不是偿债能力不足，而是政治程序可能导致技术性违约 |

- 沿用三引号 + 保存前换行规范化，两批**语法与渲染均一次通过**。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 860 字**；**ERRORS 0**、WARNINGS **32（全部为案例）**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作LL-LM｜2026-11-24｜状态：641条；扩写26条概念（R22 85→59）**',
              '**续作LN-LO｜2026-11-24｜状态：641条；扩写27条概念，概念类全部完成（R22 59→32）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22', len(short), '| 概念', len(con), '| 案例', len(cas), '| avg', avg)
