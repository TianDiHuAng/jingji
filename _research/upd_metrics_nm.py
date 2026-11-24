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

note = """维基第115轮可用。NL-NM：核验"两源差异并列"区块 + 刷新陈旧体检报告。
①**核验验证页"两源差异并列"12 条**：逐一检查——german-crisis-2022（-0.5% vs OWID 0.007%）、russian-crisis-2014（-3.7% vs -1.97%）、venezuela-hyper-2016（69% vs 62.17%；254.95% vs 800%）、zimbabwe（255.31% vs 175%）、argentina-2018（30% vs 34.28%）、subprime（13万亿 vs 约11万亿）等——**全部真实并列两组冲突数值或明确标注口径不同（如委内瑞拉累计出境 vs 常住人口存量）**。验证页内核诚实可靠。
②**发现并刷新陈旧文档**：`HEALTH_CHECK.md` 停留在 round 80（条目 632/来源 720/comparison 569），已 55 轮未更新。按 **round 135 实际状态**重写：641 条（案例 209/概念 432）、来源 742、页面 655、key_data 445、timeline 657、schools 1279、comparison 641/641、单来源 26 条、check.py 已 R1–R22+R4b、自测 18/18；并如实记录 3 条缺全文 + 6 条缓存缺口两项遗留。
③现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 18/18。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NL-NM', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 12, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 18/18',
    'spot_check': '核验两源差异 12 条（全部诚实）；刷新 HEALTH_CHECK.md',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 115 轮可用（round 135）**。**核验「两源差异并列」区块 + 刷新陈旧体检报告**。
- **核验验证页「两源差异并列」12 条**：逐一检查——german-crisis-2022（-0.5% vs OWID 0.007%）、russian-crisis-2014（-3.7% vs -1.97%）、venezuela-hyper-2016（69% vs 62.17%；254.95% vs 800%）、zimbabwe（255.31% vs 175%）、argentina-2018（30% vs 34.28%）、subprime（13 万亿 vs 约 11 万亿）等——**全部真实并列两组冲突数值或明确标注口径不同**。验证页内核诚实可靠。
- **发现并刷新陈旧文档**：`HEALTH_CHECK.md` 停留在 **round 80**（条目 632／来源 720／comparison 569），已 55 轮未更新。按 **round 135** 实际状态重写：641 条（案例 209／概念 432）、来源 742、页面 655、key_data 445、timeline 657、schools 1279、comparison 641/641、单来源 26 条、check.py 已 R1–R22+R4b、自测 18/18；并如实记录 3 条缺全文 + 6 条缓存缺口两项遗留。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作NJ-NK｜2026-11-24｜状态：641条；审计通过 + 根治check_kd单位换算缺陷**',
              '**续作NL-NM｜2026-11-24｜状态：641条；核验两源差异12条（均诚实）+刷新HEALTH_CHECK**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
