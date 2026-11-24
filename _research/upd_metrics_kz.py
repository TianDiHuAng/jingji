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
    "维基第97轮可用。KY-KZ：扩写 29 条（WARNINGS 245 → 216）。"
    "①第一批 14 条：pmi／potential-output／poverty-trap／twin-deficits／bank-regulation／"
    "call-option／commodity-money／currency-board／financial-repression／game-theory／"
    "interest-rate／risk-management／sovereign-risk／sterilization。"
    "②第二批 15 条：automatic-stabilizer／bad-bank／budget-balance／crowding-out／"
    "forward-guidance／mercantilism／money-multiplier／self-fulfilling／credit-rationing／"
    "financial-disintermediation／forward-contract／market-manipulation／new-keynesian／"
    "open-market-operation／commercial-revolution。"
    "③**本轮几处关键判断**："
    "**potential-output** 指出危机会降低潜在产出本身，"
    "因此**危机后的产出缺口可能被高估**（分母已下移）；"
    "**money-multiplier** 强调乘数「不是常数而是结果」，"
    "危机中乘数与流通速度同时下降，"
    "这解释了为何「基础货币大增而通胀未现」；"
    "**credit-rationing** 用斯蒂格利茨-韦斯逻辑说明"
    "「加息会先赶走低风险借款人、银行预期收益反而下降」，"
    "故银行宁可配给而不加息；"
    "**self-fulfilling** 指出若危机是自我实现的，"
    "则**改变预期**（存款保险、最后贷款人、暂停兑换）即可阻止危机——"
    "但也提醒「基本面确实恶化的危机靠喊话无法解决」；"
    "**sovereign-risk** 点出主权债务与私人债务的三个根本差别"
    "（无破产程序、「不愿」与「不能」难分、资产难扣押）；"
    "**currency-board** 指出它把货币危机转化为银行与债务危机，"
    "且无法充当最后贷款人；"
    "**bad-bank** 的经验结论是「分拆＋政府担保」的折中优于直接定价。"
    "④过程中出现两处字符串未闭合的语法错误，"
    "用 ast.parse 定位并修正——比逐个读报错更快。"
    "⑤**round 94 的接线检查再次生效**，用既定脚本批量修复并对称化 30 条。"
    "⑥现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) +
    "（R22）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作KY-KZ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 29, 'reviewed': 245, 'fixed': 29,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 216（R22）+ 自测 18/18',
    'spot_check': '扩写 29 条；批量修复接线并对称化 30 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 97 轮可用（round 116）**。**扩写 29 条（WARNINGS 245 → 216）**。
- **第一批 14 条**：pmi／potential-output／poverty-trap／twin-deficits／bank-regulation／call-option／commodity-money／currency-board／financial-repression／game-theory／interest-rate／risk-management／sovereign-risk／sterilization。
- **第二批 15 条**：automatic-stabilizer／bad-bank／budget-balance／crowding-out／forward-guidance／mercantilism／money-multiplier／self-fulfilling／credit-rationing／financial-disintermediation／forward-contract／market-manipulation／new-keynesian／open-market-operation／commercial-revolution。
- **本轮几处关键判断**：

  | 条目 | 判断 |
  |---|---|
  | `potential-output` | 危机会**降低潜在产出本身**，因此危机后的「产出缺口」可能被**高估**（分母已下移） |
  | `money-multiplier` | 乘数「**不是常数而是结果**」；危机中乘数与流通速度同时下降，解释了「基础货币大增而通胀未现」 |
  | `credit-rationing` | 加息会**先赶走低风险借款人**、银行预期收益反而下降，故宁可配给而不加息 |
  | `self-fulfilling` | 若危机是自我实现的，**改变预期**即可阻止——但「基本面确实恶化的危机靠喊话无法解决」 |
  | `sovereign-risk` | 主权债务与私人债务的三个根本差别：**无破产程序**、「不愿」与「不能」难分、资产难扣押 |
  | `currency-board` | 把**货币危机**转化为**银行与债务危机**，且无法充当最后贷款人 |
  | `bad-bank` | 经验结论：「**分拆＋政府担保**」的折中优于直接定价 |

- 过程中出现两处**字符串未闭合**的语法错误，用 `ast.parse` 定位并修正——比逐个读报错更快。
- **round 94 的接线检查再次生效**，用既定脚本批量修复并对称化 **30 条**。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 500 字**；**ERRORS 0**、WARNINGS 216（R22）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作KW-KX｜2026-11-24｜状态：641条；再扩写30条（R22 275→245）**',
              '**续作KY-KZ｜2026-11-24｜状态：641条；再扩写29条（R22 245→216）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| avg', avg)
