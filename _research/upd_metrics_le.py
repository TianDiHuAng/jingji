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
    "维基第99轮可用。LC-LE：扩写 27 条（WARNINGS 188 → 161），"
    "并在过程中发现并修复一个**渲染 bug**。"
    "①第一批 14 条：crypto-bubble／durable-goods／export-oriented／invisible-hand／"
    "macroprudential／microfinance／otc／protectionism／ricardian-equivalence／swap／"
    "balance-sheet-recession／financial-accelerator／financial-deepening／government-debt。"
    "②第二批 13 条：liquidity-trap／mmt／money-creation／off-balance-sheet／"
    "rational-expectations／spot-contract／sticky-prices／stock-market-crash／stock／"
    "supply-side／convexity／currency-internationalization／debt-deflation。"
    "③**方法改进**：上轮连续 4 处字符串未闭合，本轮改用**三引号字符串**写整段，"
    "两批**语法均一次通过**——拼接问题解决。"
    "④**但三引号引入了新的 bug**：它保留了段内换行（\\n），"
    "而 `mdesc()` 的粗体正则 `\\*\\*(.+?)\\*\\*` **默认不跨行匹配**，"
    "导致跨行的 `**...**` 无法渲染，页面上残留 `**`。"
    "**check_quality 立即抓到 13 项「未渲染粗体」**——这正是该检查存在的意义。"
    "⑤**修复两处**："
    "（a）数据层——把 overview／comparison／one_line／timeline／schools／policy_response 中的换行"
    "规范化掉（共 27 条），因为中文段落本不需要硬换行；"
    "（b）渲染层——给 mdesc 的粗体正则加 `re.S` 作为防御，跨行也能渲染。"
    "修复后 check_quality 归零。"
    "⑥**本轮的元教训**："
    "**修一个问题的方法，可能就是下个问题的来源**——"
    "为避免拼接遗漏引号而改用三引号，"
    "却引进了换行导致渲染失败。"
    "幸运的是检查体系接住了它——这说明**检查的价值不在于预防所有错误，"
    "而在于让错误在发布前暴露**。"
    "⑦现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；含换行的 overview: " + str(nl) +
    "；ERRORS 0、WARNINGS " + str(len(short)) + "（R22）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作LC-LE', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 27, 'reviewed': 188, 'fixed': 28,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 161（R22）+ 自测 18/18',
    'spot_check': '扩写 27 条；修复三引号引入的换行渲染 bug',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 99 轮可用（round 118）**。**扩写 27 条（WARNINGS 188 → 161），并发现修复一个渲染 bug**。
- **第一批 14 条**：crypto-bubble／durable-goods／export-oriented／invisible-hand／macroprudential／microfinance／otc／protectionism／ricardian-equivalence／swap／balance-sheet-recession／financial-accelerator／financial-deepening／government-debt。
- **第二批 13 条**：liquidity-trap／mmt／money-creation／off-balance-sheet／rational-expectations／spot-contract／sticky-prices／stock-market-crash／stock／supply-side／convexity／currency-internationalization／debt-deflation。
- **方法改进**：上轮连续 4 处字符串未闭合，本轮改用**三引号字符串**写整段，两批**语法均一次通过**。
- **但三引号引入了新的 bug**：

  | 环节 | 问题 |
  |---|---|
  | 三引号 | 保留了段内换行（`\\n`） |
  | `mdesc()` 粗体正则 | `\\*\\*(.+?)\\*\\*` **默认不跨行匹配** |
  | 结果 | 跨行的 `**...**` 无法渲染，页面残留 `**` |

  **`check_quality` 立即抓到 13 项「未渲染粗体」**——这正是该检查存在的意义。

- **修复两处**：
  - **数据层**：把 overview／comparison／one_line／timeline／schools／policy_response 中的换行规范化（**27 条**），中文段落本不需要硬换行
  - **渲染层**：给 `mdesc` 的粗体正则加 `re.S` 作为防御
  - 修复后 `check_quality` 归零
- **本轮的元教训**：

  > **修一个问题的方法，可能就是下个问题的来源**——为避免拼接遗漏引号而改用三引号，却引进了换行导致渲染失败。

  幸运的是检查体系接住了它——**检查的价值不在于预防所有错误，而在于让错误在发布前暴露**。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 570 字**；含换行的 overview **0**；**ERRORS 0**、WARNINGS 161（R22）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作LA-LB｜2026-11-24｜状态：641条；再扩写28条（R22 216→188）**',
              '**续作LC-LE｜2026-11-24｜状态：641条；扩写27条（R22 188→161），修复换行渲染bug**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| avg', avg, '| 含换行', nl)
