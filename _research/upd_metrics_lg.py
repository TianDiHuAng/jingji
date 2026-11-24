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
nl = sum(1 for e in es if '\n' in (e.get('overview') or ''))

note = (
    "维基第100轮可用（round 119）。LF-LG：扩写 24 条（WARNINGS 161 → 136）。"
    "①第一批 15 条：foreign-exchange-reserves／savings-glut／beggar-thy-neighbour／"
    "conditionality／credit-money／deleveraging／insurance-history／laissez-faire／"
    "monetarism／quantity-theory-money／rwa／secondary-market／spv／capm／"
    "central-counterparty／financial-innovation。"
    "②第二批 9 条：esfs／fiscal-military-state／helicopter-money／imf／"
    "institutional-economics／juglar-cycle／liquidity-preference／margin-finance／paris-club。"
    "③**方法闭环**：沿用三引号写法（语法一次通过），"
    "并在脚本内**保存前做换行规范化**"
    "（`re.sub(r'\\s*\\n\\s*', '', ov)`）——"
    "这是 round 118 那个渲染 bug 的根治办法："
    "既保留三引号的书写便利，又不把换行带进数据。"
    "**check_quality 两批均一次通过。**"
    "④**本轮几处关键判断**："
    "**rwa** 讲清了「风险加权资产为何是危机的核心问题」——"
    "权重由规则或模型决定，因此可以被「优化」；"
    "**central-counterparty** 指出它把「双边信用风险」转换成了「集中与操作风险」，"
    "风险没有消失而是换了形态，「清算所太大而不能倒」成为新的政策难题；"
    "**spv** 的教训是「法律形式上的隔离，不等于经济实质上的隔离」——"
    "只要声誉与融资渠道相连，风险终会回流；"
    "**financial-innovation** 提出评价标准："
    "**它是否真正转移了风险，还是仅仅转移了风险的可见性**；"
    "**margin-finance** 点明「用自有资金承受下跌」与「被强制平仓」的区别——"
    "后者把账面损失变成永久损失；"
    "**juglar／kondratiev／kitchin** 三类周期均注明统计基础有争议、本库不据周期位置作预测。"
    "⑤**round 94 的接线检查再次生效**，批量修复并对称化 37 条。"
    "⑥现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；含换行 " + str(nl) +
    "；ERRORS 0、WARNINGS " + str(len(short)) + "（R22）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作LF-LG', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 24, 'reviewed': 161, 'fixed': 25,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 136（R22）+ 自测 18/18',
    'spot_check': '扩写 24 条；三引号 + 保存前规范化，check_quality 两批一次通过',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 100 轮可用（round 119）**。**扩写 24 条（WARNINGS 161 → 136）**。
- **第一批 15 条**：foreign-exchange-reserves／savings-glut／beggar-thy-neighbour／conditionality／credit-money／deleveraging／insurance-history／laissez-faire／monetarism／quantity-theory-money／rwa／secondary-market／spv／capm／central-counterparty／financial-innovation。
- **第二批 9 条**：esfs／fiscal-military-state／helicopter-money／imf／institutional-economics／juglar-cycle／liquidity-preference／margin-finance／paris-club。
- **方法闭环**：沿用三引号写法（语法一次通过），并在脚本内**保存前做换行规范化**——这是 round 118 渲染 bug 的根治办法：**既保留三引号的书写便利，又不把换行带进数据**。`check_quality` 两批均一次通过。
- **本轮几处关键判断**：

  | 条目 | 判断 |
  |---|---|
  | `rwa` | 讲清「风险加权资产为何是危机的核心问题」——**权重由规则或模型决定，因此可以被「优化」** |
  | `central-counterparty` | 它把「双边信用风险」转换成「**集中与操作风险**」——风险没消失而是换了形态，「清算所太大而不能倒」成为新难题 |
  | `spv` | **法律形式上的隔离 ≠ 经济实质上的隔离**——只要声誉与融资渠道相连，风险终会回流 |
  | `financial-innovation` | 评价标准：**它是否真正转移了风险，还是仅仅转移了风险的可见性** |
  | `margin-finance` | 「用自有资金承受下跌」与「被强制平仓」的区别——**后者把账面损失变成永久损失** |
  | `juglar`／`kondratiev`／`kitchin` | 三类周期均注明**统计基础有争议、本库不据周期位置作预测** |

- **round 94 的接线检查再次生效**，批量修复并对称化 **37 条**。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 620 字**；含换行 **0**；**ERRORS 0**、WARNINGS 136（R22）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作LC-LE｜2026-11-24｜状态：641条；扩写27条（R22 188→161），修复换行渲染bug**',
              '**续作LF-LG｜2026-11-24｜状态：641条；扩写24条（R22 161→136）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| avg', avg)
