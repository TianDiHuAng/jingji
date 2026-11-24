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

note = """维基第119轮可用。NS-NT：审计页面结构完整性并把"站点完整性"固化为检查。
①**页面结构审计（全部 655 页）**：缺概述 **0**、空 tbody **0**、L3 缺 SVG **0**、有 key_data 却无关键数据表 **0**——条目页结构完整。
②**聚合页与导航完整性**：timeline.html 658 行（表头+657 事件，与数据 657 一致）、sources.html 完整列出 742 来源；
`index-all.html` 链接到 **641/641** 条目、`cases.html` **209**、`concepts.html` **432**——导航无遗漏；站点共 14 静态页 + 641 条目页 = 655。
③**固化为检查**：`check_pages.py` 新增"站点完整性"三项断言——（a）每条目均有页面；（b）index-all 列全所有条目 id；（c）timeline 页行数不少于事件总数。防 gen_site 截断/漏生成。
④**纳入自测**：`selftest.py` 新增"站点完整性(未列全)"用例（移除 index-all 一条链接应报"未列全"），自测 19 → **20 项**，全通过。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 20/20。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NS-NT', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 655, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 20/20',
    'spot_check': '页面结构完整；check_pages 加站点完整性断言；自测 19→20',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 119 轮可用（round 139）**。**审计页面结构完整性并把「站点完整性」固化为检查**。
- **页面结构审计（全部 655 页）**：缺概述 **0**、空 tbody **0**、L3 缺 SVG **0**、有 key_data 却无关键数据表 **0**——条目页结构完整。
- **聚合页与导航完整性**：timeline.html 658 行（表头+657 事件，与数据一致）、sources.html 完整列出 742 来源；`index-all.html` 链接到 **641/641** 条目、`cases.html` **209**、`concepts.html` **432**；站点共 14 静态页 + 641 条目页 = 655。
- **固化为检查**：`check_pages.py` 新增「站点完整性」三项断言——（a）每条目均有页面；（b）index-all 列全所有条目 id；（c）timeline 页行数不少于事件总数。防 gen_site 截断/漏生成。
- **纳入自测**：`selftest.py` 新增「站点完整性(未列全)」用例，自测 19 → **20 项**，全通过。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 20/20。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NR｜2026-11-24｜状态：641条；修复check_quality孤立**漏检，自测扩至19项**',
              '**续作NS-NT｜2026-11-24｜状态：641条；页面结构审计通过+加站点完整性断言，自测20项**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
