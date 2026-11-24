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
short = [(e['id'], len(e.get('overview') or ''), e['tier']) for e in es
         if e.get('tier') in ('核心', '重要') and len(e.get('overview') or '') < 150]

note = (
    "维基第93轮可用。KK-KO：清理「待核实」套话 201 条，并由此发现内容单薄的系统性掩盖。"
    "①清理：564 个条目的 overview 以「具体XX待核实」结尾（占 88%），"
    "这不是纯套话（诚实声明），但它是无信息量的模板化尾巴，且让每条概述结尾雷同。"
    "已移除 **201 条**（其内容并入 pending_notes），"
    "另 **358 条因移除后不足 150 字而保留**——避免把内容不足掩盖成「已清理」。"
    "②由此发现第 10 个系统性问题：那些「待核实」的尾巴一直在掩盖内容单薄。"
    "358 条中 **326 条是概念/理论类**，多为「通货膨胀」「失业」「系统性风险」这类基础概念（66—90 字）。"
    "③加入 R22（核心/重要条目 overview 应 ≥150 字）作为 warning：实际捕获 **335 条**"
    "（3 核心 + 332 重要）。"
    "④本轮扩写最核心的 10 条（80—91 字 → 380—488 字）："
    "leverage／inflation／deflation／systemic-risk／currency-crisis／"
    "creative-destruction／fiscal-policy／unemployment／opportunity-cost／balance-of-payments，"
    "每一条都补上了机制细节与「与危机的具体关联」。"
    "例如 systemic-risk 点明「个体审慎的加总未必等于系统稳健」这一合成谬误；"
    "balance-of-payments 指出「赤字好坏取决于融资结构，1997 年亚洲危机前赤字并不高，"
    "但短期外币外债占比高」；deflation 区分「好的通缩」（生产率推动）与"
    "「坏的通缩」（需求崩溃）。"
    "⑤**R22 保留为 warning 而非 error**：335 条不可能也不应一次性拉齐——"
    "「贝塔系数」「久期」这类工具性概念，简短定义即是完整，强行注水反而降低质量。"
    "真正需要扩写的是其中约三分之一的机制类核心概念，已列入 BACKLOG 分批处理。"
    "⑥现状：" + str(len(es)) + " 条、来源 " + str(len(srcs)) + "、页面 " + str(pages) +
    "；**ERRORS 0**、WARNINGS " + str(len(short)) + "（均为 R22 提示）。"
    "十一道检查通过 + 自测 18/18。"
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作KK-KO', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 10, 'reviewed': 641, 'fixed': 211,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 335 均为 R22 提示 + 自测 18/18',
    'spot_check': '清理 201 条套话；扩写 10 条核心概念；新增 R22',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# BACKLOG
bl = 'BACKLOG.md'
b = open(bl, encoding='utf-8').read()
add_bl = "\n## 待办：R22 内容过短（335 条，round 112 记录）\n\n"
add_bl += "**性质**：tier 为「核心」或「重要」，但 overview < 150 字。已扩写 10 条，余 **325 条**。\n\n"
add_bl += "**判断原则**：不是所有都要拉长。\n"
add_bl += "- **机制类核心概念**（如 systemic-risk／currency-crisis／moral-hazard 一类）→ **应扩写**，补机制与危机关联\n"
add_bl += "- **工具性概念**（如 beta／duration／IPO／basis-point）→ **简短即完整**，强行注水反而降低质量\n\n"
add_bl += "**最短的 20 条**（优先处理）：\n\n"
for s in sorted(short, key=lambda x: x[1])[:20]:
    add_bl += "- `%s`（%d 字，%s）\n" % (s[0], s[1], s[2])
add_bl += "\n**修法**：读 `_research/wiki_full/<id>.txt`（若无则先抓），扩写 overview 并补「与金融危机的关系」；改完跑 `check.py` 确认 WARNINGS 下降。\n"
if 'R22 内容过短' not in b:
    b = b.rstrip() + '\n' + add_bl
    open(bl, 'w', encoding='utf-8').write(b)
    print('BACKLOG 已记录')

add = """- **维基百科第 93 轮可用（round 112）**。**清理「待核实」套话 201 条，并由此发现内容单薄的系统性掩盖**。
- **清理**：**564 个条目**（88%）的 overview 以「具体XX待核实」结尾。这不是纯套话（诚实声明），但它是**无信息量的模板化尾巴**，且让每条概述结尾雷同。已移除 **201 条**（内容并入 `pending_notes`），另 **358 条因移除后不足 150 字而保留**——避免把内容不足掩盖成「已清理」。
- **由此发现第 10 个系统性问题**：那些「待核实」的尾巴**一直在掩盖内容单薄**。358 条中 **326 条是概念/理论类**，多为「通货膨胀」「失业」「系统性风险」这类基础概念（66—90 字）。
- **加入 R22**（核心/重要条目 overview 应 ≥150 字）作为 warning：捕获 **335 条**（3 核心 + 332 重要）。
- **本轮扩写最核心的 10 条**（80—91 字 → 380—488 字）：

  | 条目 | 补充的关键判断 |
  |---|---|
  | `systemic-risk` | **个体审慎的加总未必等于系统稳健**（合成谬误） |
  | `balance-of-payments` | 赤字好坏**取决于融资结构**——1997 年亚洲危机前赤字并不高，但短期外币外债占比高 |
  | `deflation` | 区分**「好的通缩」**（生产率推动）与**「坏的通缩」**（需求崩溃） |
  | `creative-destruction` | 危机中的破坏**未必伴随创造**——信贷瘫痪时新企业同样得不到融资 |
  | `opportunity-cost` | **救助的机会成本**常被忽略；监管的机会成本正是政策辩论的实质 |

- **R22 保留为 warning 而非 error**：335 条不可能也不应一次性拉齐——「贝塔系数」「久期」这类**工具性概念，简短定义即是完整**，强行注水反而降低质量。真正需扩写的是其中约三分之一的**机制类核心概念**，已列入 `BACKLOG.md` 分批处理。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0**、WARNINGS 335（均 R22 提示）。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作KD-KI｜2026-11-24｜状态：641条；R21归零，38条英文正文全部改写为中文**',
              '**续作KK-KO｜2026-11-24｜状态：641条；清理201条套话，发现335条内容过短（R22）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | R22 条数', len(short))
