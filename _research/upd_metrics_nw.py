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
svg = sum(1 for e in es if e.get('deep_svg'))

note = """维基第120轮可用。NU-NW：审计 SVG 与重复内容，并把"整段重复"纳入 check_filler。
①**SVG 机制图审计（34 条 L3）**：全部有 viewBox（780×300 共 31 条、780×280 共 3 条），**元素坐标无一越出 viewBox**（不会被裁剪）——图形渲染合规。（首版脚本误用双引号正则，未匹配单引号属性而全报"no viewBox"，已修正。）
②**overview 重复检测**：用 6-gram Jaccard 比对全部 overview，**相似度≥0.55 的条目对为 0**——无复制粘贴。
③**固化为检查**：`check_filler.py` 新增"整段 overview 高度相似（Jaccard≥0.55）"检测，防未来复制粘贴。
④**纳入自测**：`selftest.py` 新增"check_filler 整段重复"用例（把一条 overview 复制到另一条应报"高度相似"），自测 20 → **21 项**，全通过；并同步更新 `HEALTH_CHECK.md` 的自测数。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；L3 机制图 """ + str(svg) + """ 张；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 21/21。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NU-NW', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 641, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 21/21',
    'spot_check': 'SVG 无越界、overview 无重复；check_filler 加整段重复检测，自测 20→21',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 120 轮可用（round 140）**。**审计 SVG 与重复内容，并把「整段重复」纳入 check_filler**。
- **SVG 机制图审计（34 条 L3）**：全部有 viewBox（780×300 ×31、780×280 ×3），**元素坐标无一越出 viewBox**（不会被裁剪），图形渲染合规。（首版脚本误用双引号正则、未匹配单引号属性而全报「no viewBox」，已修正——**又一个「检查器本身有 bug」的实例**。）
- **overview 重复检测**：6-gram Jaccard 比对全部 overview，**相似度≥0.55 的条目对为 0**——无复制粘贴。
- **固化为检查**：`check_filler.py` 新增「整段 overview 高度相似（Jaccard≥0.55）」检测。
- **纳入自测**：`selftest.py` 新增「check_filler 整段重复」用例，自测 20 → **21 项**；同步更新 `HEALTH_CHECK.md`。
- 现状：**641 条**、来源 **742**、页面 **655**；L3 机制图 **34 张**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 21/21。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NS-NT｜2026-11-24｜状态：641条；页面结构审计通过+加站点完整性断言，自测20项**',
              '**续作NU-NW｜2026-11-24｜状态：641条；SVG/重复审计通过，check_filler加整段重复检测（自测21项）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | svg', svg, '| avg', avg)
