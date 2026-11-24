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
    "维基第103轮可用。LL-LM：扩写 26 条概念（WARNINGS 85 → 59）。"
    "①第一批 14 条：industrial-revolution／bis／cpi／dodd-frank／lucas-critique／"
    "principal-agent／purchasing-power-parity／greshams-law／is-lm／laffer-curve／"
    "yield-curve-control／aggregate-demand／dutch-disease／efficient-market。"
    "②第二批 12 条：etf／maturity-transformation／seigniorage／sovereign-wealth-fund／"
    "debasement／volcker-rule／output-gap／great-moderation／plaza-accord／louvre-accord／"
    "great-divergence／gnp。"
    "③**本轮几处关键判断**："
    "**great-moderation** 给出危机前认知失误的标准解释——"
    "「波动被转移了，而非消除：风险从产出与通胀转移到了金融体系的杠杆与资产负债表，"
    "而这些不在当时的政策指标里」；"
    "**is-lm** 与 **lucas-critique** 两处都指向同一件事——"
    "主流宏观模型**没有金融中介、忽略预期与监管的结构变化**，"
    "这正是 2008 年后被批评之处；"
    "**volcker-rule** 记录了一个具体的制度衰退——"
    "2019—2020 年美国对其实施实质性放松，是「危机后改革会随时间被侵蚀」的例证；"
    "**debasement** 归纳出一条跨越时代的线索——"
    "「从降低金属成色，到超额印钞，到现代的各种金融抑制手段，"
    "经济实质是同一个：以隐蔽的方式重新分配财富」；"
    "**greshams-law** 明确了它的适用条件（必须有法定比价），"
    "并指出它在单一法定货币体系中**不适用**，但常被误用；"
    "**plaza-accord** 对「广场协议→日本泡沫」这条因果链保持了谨慎——"
    "「不能把日本的经验简单归因于一份协议」。"
    "④沿用三引号 + 保存前换行规范化，两批语法与渲染均一次通过。"
    "⑤**round 94 的接线检查再次生效**，批量修复并对称化 40 条。"
    "⑥现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；overview 平均 " + str(avg) + " 字；ERRORS 0、WARNINGS " + str(len(short)) +
    "（概念 " + str(len(con)) + "／案例 " + str(len(cas)) + "）。"
    "十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作LL-LM', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 26, 'reviewed': 85, 'fixed': 26,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 59（R22）+ 自测 18/18',
    'spot_check': '扩写 26 条概念；对称化 40 条',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 103 轮可用（round 122）**。**扩写 26 条概念（WARNINGS 85 → 59）**。
- **第一批 14 条**：industrial-revolution／bis／cpi／dodd-frank／lucas-critique／principal-agent／purchasing-power-parity／greshams-law／is-lm／laffer-curve／yield-curve-control／aggregate-demand／dutch-disease／efficient-market。
- **第二批 12 条**：etf／maturity-transformation／seigniorage／sovereign-wealth-fund／debasement／volcker-rule／output-gap／great-moderation／plaza-accord／louvre-accord／great-divergence／gnp。
- **本轮几处关键判断**：

  | 条目 | 判断 |
  |---|---|
  | `great-moderation` | **波动被转移了，而非消除**——风险从产出与通胀转移到金融体系的杠杆与资产负债表，而这些**不在当时的政策指标里** |
  | `is-lm` / `lucas-critique` | 都指向同一件事——主流宏观模型**没有金融中介、忽略预期与结构变化**，这正是 2008 年后被批评之处 |
  | `volcker-rule` | 记录一个具体的制度衰退——2019—2020 年美国对其实施实质性放松，是「**危机后改革会随时间被侵蚀**」的例证 |
  | `debasement` | 归纳一条跨越时代的线索——**从降低金属成色到超额印钞到现代金融抑制，经济实质是同一个：以隐蔽方式重新分配财富** |
  | `greshams-law` | 明确适用条件（**必须有法定比价**），并指出它在单一法定货币体系中**不适用**，但常被误用 |
  | `plaza-accord` | 对「广场协议→日本泡沫」保持谨慎——「**不能把日本的经验简单归因于一份协议**」 |

- 沿用三引号 + 保存前换行规范化，两批**语法与渲染均一次通过**。
- **round 94 的接线检查再次生效**，批量修复并对称化 **40 条**。
- 现状：**641 条**、来源 **742**、页面 **655**；overview 平均 **约 810 字**；**ERRORS 0**、WARNINGS 59。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作LJ-LK｜2026-11-24｜状态：641条；扩写30条概念（R22 115→85）**',
              '**续作LL-LM｜2026-11-24｜状态：641条；扩写26条概念（R22 85→59）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22', len(short), '| 概念', len(con), '| 案例', len(cas), '| avg', avg)
