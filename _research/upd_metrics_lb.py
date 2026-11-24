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
    "维基第98轮可用。LA-LB：扩写 28 条（WARNINGS 216 → 188）。"
    "①第一批 14 条：jamaica-accords／physiocracy／political-economy／price-revolution／"
    "silver-standard／alm／capital-account／competitive-devaluation／credit-enhancement／"
    "development-economics／diversification／elasticity／ems／hedge-fund。"
    "②第二批 14 条：seniority／tariff／basis-point／fire-sale／interbank-lending／"
    "joint-stock／menu-cost／oecd／smithsonian-agreement／speculative-attack／stablecoin／"
    "debt-overhang／endogenous-money／fisher-equation。"
    "③**本轮几处关键判断**："
    "**credit-enhancement** 点破「增级只能重新分配风险、不能消灭风险」，"
    "且外部担保依赖担保方自身偿付能力——2008 年 monoline 被降级后"
    "担保反而把风险传导回被担保证券；"
    "**fire-sale** 提出「贱卖外部性」——卖出者自己承担的价格损失有一部分强加给同行，"
    "这正是宏观审慎监管的理由；"
    "**interbank-lending** 说明同业市场为何是最灵敏的体温计："
    "**无抵押品保护、完全依赖对交易对手的信任**，一旦怀疑即瞬间关闭；"
    "**debt-overhang** 指出它与「资产替代」方向相反——"
    "濒临违约时倾向赌博、已经资不抵债时倾向躺平，两者可同时存在；"
    "**endogenous-money** 纠正教科书顺序「贷款创造存款而非存款创造贷款」，"
    "并解释为何央行控制的是利率而非货币数量；"
    "**fisher-equation** 提醒名义利率高不等于政策紧——"
    "1970 年代与 2021—22 年都出现过实际利率为负的「金融抑制」。"
    "④**教训（过程层面）**：本轮出现 4 处字符串未闭合的语法错误，"
    "全部由 `ast.parse` 定位修正；这已是连续两轮出现同类失误，"
    "原因是长文写作时跨行拼接遗漏引号。"
    "⑤**round 94 的接线检查再次生效**，批量修复并对称化 35 条。"
    "⑥现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) +
    "（R22）。十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作LA-LB', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 28, 'reviewed': 216, 'fixed': 28,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 188（R22）+ 自测 18/18',
    'spot_check': '扩写 28 条；批量修复接线并对称化 35 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 98 轮可用（round 117）**。**扩写 28 条（WARNINGS 216 → 188）**。
- **第一批 14 条**：jamaica-accords／physiocracy／political-economy／price-revolution／silver-standard／alm／capital-account／competitive-devaluation／credit-enhancement／development-economics／diversification／elasticity／ems／hedge-fund。
- **第二批 14 条**：seniority／tariff／basis-point／fire-sale／interbank-lending／joint-stock／menu-cost／oecd／smithsonian-agreement／speculative-attack／stablecoin／debt-overhang／endogenous-money／fisher-equation。
- **本轮几处关键判断**：

  | 条目 | 判断 |
  |---|---|
  | `credit-enhancement` | **增级只能重新分配风险、不能消灭风险**；外部担保依赖担保方自身偿付能力——2008 年 monoline 被降级后，担保反而把风险传导回被担保证券 |
  | `fire-sale` | 提出「**贱卖外部性**」——卖出者自己承担的价格损失有一部分强加给同行 |
  | `interbank-lending` | 同业市场为何是最灵敏的体温计：**无抵押品保护、完全依赖对交易对手的信任** |
  | `debt-overhang` | 与「资产替代」方向**相反**——濒临违约时倾向赌博、已资不抵债时倾向躺平，两者可同时存在 |
  | `endogenous-money` | 纠正教科书顺序：**贷款创造存款，而非存款创造贷款**；故央行控制的是利率而非货币数量 |
  | `fisher-equation` | 名义利率高**不等于**政策紧——1970 年代与 2021—22 年都出现过实际利率为负的「金融抑制」 |

- **过程教训**：本轮出现 **4 处字符串未闭合**的语法错误，全部由 `ast.parse` 定位修正；这已是连续两轮出现同类失误，原因是长文写作时跨行拼接遗漏引号。
- **round 94 的接线检查再次生效**，批量修复并对称化 **35 条**。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 530 字**；**ERRORS 0**、WARNINGS 188（R22）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作KY-KZ｜2026-11-24｜状态：641条；再扩写29条（R22 245→216）**',
              '**续作LA-LB｜2026-11-24｜状态：641条；再扩写28条（R22 216→188）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 剩余', len(short), '| avg', avg)
