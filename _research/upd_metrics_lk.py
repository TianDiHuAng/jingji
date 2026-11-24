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
    "维基第102轮可用。LJ-LK：扩写 30 条概念（WARNINGS 115 → 85）。"
    "①第一批 15 条：disinflation／fatf／gini／inflation-targeting／mark-to-market／"
    "public-good／sudden-stop／tarp／hedging／history-of-banking／middle-income-trap／"
    "ponzi-scheme／bimetallism／financial-fragility／long-depression。"
    "②第二批 15 条：fiscal-multiplier／fsb／globalization／national-income／stress-test／"
    "tranche／comparative-advantage／international-monetary-system／washington-consensus／"
    "basel-accords／basel-iii／financial-crisis／fiscal-space／lewis-turning-point／ppi。"
    "③**本轮几处关键判断**："
    "**ponzi-scheme** 明确区分「庞氏骗局（欺诈）」与「明斯基的庞氏融资（脆弱性结构）」——"
    "两者形式相似（都依赖持续流入）但性质不同，「"
    "不该把所有高杠杆结构都称为庞氏」；"
    "**tranche** 指出分层的实质是「把同一资产池的风险在投资者之间重新分配」，"
    "而它对相关性的依赖在危机中失效——"
    "「分层能切分风险，但不能降低系统性风险」；"
    "**mark-to-market** 并列了两派（批评者称放大下跌 vs 支持者称问题在价格本身失真），"
    "并点出关键一句「**掩盖损失并不会消除损失**」；"
    "**public-good** 把金融稳定与危机中的流动性明确为公共品，"
    "直接解释「最后贷款人」的正当性；"
    "**national-income** 指出 GDP 不反映杠杆与资产泡沫——"
    "「这正是危机前宏观数据看起来很好的原因」；"
    "**financial-fragility** 提醒「脆弱性不等于即将出事」，"
    "把它当作危机将至的信号是对该概念的误用。"
    "④沿用三引号 + 保存前换行规范化，两批语法与渲染均一次通过。"
    "⑤**round 94 的接线检查再次生效**，批量修复并对称化 59 条。"
    "⑥现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) +
    "（其中概念 " + str(len(con)) + "／案例 " + str(len(cas)) + "）。"
    "十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作LJ-LK', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 30, 'reviewed': 115, 'fixed': 30,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 85（R22）+ 自测 18/18',
    'spot_check': '扩写 30 条概念；对称化 59 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 102 轮可用（round 121）**。**扩写 30 条概念（WARNINGS 115 → 85）**。
- **第一批 15 条**：disinflation／fatf／gini／inflation-targeting／mark-to-market／public-good／sudden-stop／tarp／hedging／history-of-banking／middle-income-trap／ponzi-scheme／bimetallism／financial-fragility／long-depression。
- **第二批 15 条**：fiscal-multiplier／fsb／globalization／national-income／stress-test／tranche／comparative-advantage／international-monetary-system／washington-consensus／basel-accords／basel-iii／financial-crisis／fiscal-space／lewis-turning-point／ppi。
- **本轮几处关键判断**：

  | 条目 | 判断 |
  |---|---|
  | `ponzi-scheme` | 明确区分「**庞氏骗局（欺诈）**」与「**明斯基的庞氏融资（脆弱性结构）**」——两者形式相似但性质不同，「不该把所有高杠杆结构都称为庞氏」 |
  | `tranche` | 分层的实质是「把同一资产池的风险在投资者之间重新分配」；**分层能切分风险，但不能降低系统性风险** |
  | `mark-to-market` | 并列两派，并点出关键一句「**掩盖损失并不会消除损失**」 |
  | `public-good` | 把**金融稳定与危机中的流动性**明确为公共品，直接解释「最后贷款人」的正当性 |
  | `national-income` | GDP 不反映杠杆与资产泡沫——「**这正是危机前宏观数据看起来很好的原因**」 |
  | `financial-fragility` | 提醒「**脆弱性不等于即将出事**」，把它当作危机将至的信号是误用 |

- 沿用三引号 + 保存前换行规范化，两批**语法与渲染均一次通过**。
- **round 94 的接线检查再次生效**，批量修复并对称化 **59 条**。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 750 字**；**ERRORS 0**、WARNINGS 85（概念 55／案例 30）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作LH-LI｜2026-11-24｜状态：641条；扩写21条（R22 136→115）**',
              '**续作LJ-LK｜2026-11-24｜状态：641条；扩写30条概念（R22 115→85）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| 概念', len(con), '| 案例', len(cas), '| avg', avg)
