# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))
from collections import Counter
dist = dict(sorted(Counter(len(e.get('schools') or []) for e in es).items()))

note = """维基第116轮可用。NO：为 3 条单观点的重要概念补第二派，两派对照 625→628。
①核验验证页"两源差异并列"（上轮已做，本轮再列 schools/comparison 数字扫描，207 条多为"其他事件年份"的对比引用，属正常，判据噪声大，不再追）。
②**为 3 条单观点的"重要"概念补第二派**（均据其现有来源）：
effective-demand（萨伊定律／古典视角：供给创造需求、不存在持续有效需求不足 vs 凯恩斯有效需求不足）、
inequality（效率／增长权衡与库兹涅茨假说 vs 不平等上升）、
demand（需求定律视角 vs 互补品效应）。
③结果：schools 分布 {0:5, 1:2, 2:628, 4:6}——**两派对照 628 条**；剩 2 条单观点均为案例（federal-reserve-act／sherman-silver-purchase），案例单观点属正常，不强补；5 条 0 schools 为机构类（nasdaq／mutual-fund／dividend／buyback／population），保持留空。
④现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 18/18。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NO', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 10, 'fixed': 3,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 18/18',
    'spot_check': '3 条重要概念补第二派 schools，两派对照 625→628',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 116 轮可用（round 136）**。**为 3 条单观点的重要概念补第二派，两派对照 625 → 628**。
- **为 3 条单观点的「重要」概念补第二派**（均据其现有来源）：

  | 概念 | 第二派 |
  |---|---|
  | `effective-demand` | **萨伊定律／古典视角**（供给创造需求、不存在持续有效需求不足）vs 凯恩斯有效需求不足 |
  | `inequality` | **效率／增长权衡与库兹涅茨假说** vs 不平等上升 |
  | `demand` | 需求定律（价格上升则需求量下降）vs 互补品效应 |

- **结果**：schools 分布 `{0:5, 1:2, 2:628, 4:6}`——**两派对照 628 条**；剩 2 条单观点均为**案例**（`federal-reserve-act`／`sherman-silver-purchase`），案例单观点属正常，不强补；5 条 0 schools 为**机构类**（nasdaq／mutual-fund／dividend／buyback／population），保持留空。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NL-NM｜2026-11-24｜状态：641条；核验两源差异12条（均诚实）+刷新HEALTH_CHECK**',
              '**续作NO｜2026-11-24｜状态：641条；3条重要概念补第二派schools（两派628条）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | schools dist', dist, '| avg', avg)
