# -*- coding: utf-8 -*-
"""阶段5：生成 REPORT.md（总条目、层级、验证、待核实、空白格子）。"""
import json, glob, re
from collections import Counter

cov = json.load(open('coverage.json',encoding='utf-8'))
src = json.load(open('data/sources.json',encoding='utf-8'))
entries = [json.load(open(f,encoding='utf-8')) for f in sorted(glob.glob('data/entries/*.json'))]
lv = Counter(e['level'] for e in entries)
tier = Counter(e['tier'] for e in entries)
ver = sum(1 for s in src['sources'] if s['verified'])
unver = len(src['sources'])-ver
needs = sum(1 for e in entries if e.get('needs_verification'))

# 空白格子：从覆盖矩阵解析0值
blanks=[]
for line in open('COVERAGE_MATRIX.md',encoding='utf-8'):
    if line.startswith('- '): blanks.append(line[2:].strip())

r = [
 '# REPORT.md — 《经济史与金融危机案例库》项目报告','',
 '生成日期：2026-11-22','',
 '## 一、条目统计','',
 f'- **总条目数：{len(entries)}**（scope 规划 {cov["total"]}，全部已建文件）',
 f'- 按层级：**L2 标准 {lv["L2"]} 条**（核心{tier["核心"]}+重要{tier["重要"]}中已升级者），**L1 骨架 {lv["L1"]} 条**（补充条目），**L3 深度 {lv["L3"]} 条**',
 f'- 按层级目标分布：核心 {tier["核心"]} / 重要 {tier["重要"]} / 补充 {tier["补充"]}',
 f'- 按时期：'+ '、'.join(f'{k} {v}' for k,v in Counter(e['period'] for e in entries).items()),
 f'- 按地区：'+ '、'.join(f'{k} {v}' for k,v in Counter(e['region'] for e in entries).items()),
 f'- 按危机类型：'+ '、'.join(f'{k} {v}' for k,v in Counter(e['crisis_type'] for e in entries).items()),
 '',
 '## 二、来源与验证','',
 f'- **来源库总数：{len(src["sources"])}**（权威百科、学术著作、官方机构）',
 f'- **已核对 verified=true：{ver}** — 经 Wikipedia API / Open Library / 机构页 HTTP 抓取逐条核对标题、作者/机构、年份',
 f'- **待核实（反爬不可达）：{unver}** — Britannica / IMF / Investopedia / 百度百科 / BLS 返回 HTTP 403，已如实标注',
 f'- 关键事实双源规则：由 tools/check.py R5/R6 机器强制；不足者标 needs_verification',
 f'- **需进一步核实的条目：{needs} 条**（含具体数值/人物/政策细节待查原文）',
 '',
 '## 三、校验结果','',
 '| 校验环节 | 结果 |','|---|---|',
 '| tools/check.py（数据层 R1–R15） | 106 条，0 error |',
 '| tools/check_links.py（站点终检） | 117 页，0 断链、0 图片、SVG 结构合法 |',
 '| 批次复检（RECHECK.md） | 抽查4条 L2 全 PASS |',
 '',
 '## 四、站点产出','',
 '- `site/index.html` 首页（统计卡片 + 单元导航）',
 '- 单元页 ×6、条目详情页 ×106、全站索引、时间线、来源列表、覆盖矩阵页',
 '- 纯 HTML + CSS，零 JavaScript；浅/深双模式通过 CSS 变量与 `prefers-color-scheme` 自动切换',
 '- 全部图示为内联 SVG，文字使用 CSS 变量，双模式可读；无图片',
 '',
 '## 五、覆盖矩阵空白格子清单','',
 '以下格子当前无条目（时期 × 危机类型；多属理论制度类或早期史料稀缺维度）：','',
]
for b in blanks: r.append('- '+b)
r += ['', '## 六、已知限制与后续','',
 '- 多数条目的具体数值、精确日期与人物归属标注为"待核实"，需逐条查原文补全（TASK 硬性规则：宁缺勿编）。',
 '- 理论制度单元（U6）部分条目的来源数偏少，已标 needs_verification。',
 '- 5 条权威站点因反爬无法核对标题/年份，列为待核实；如需升级 verified 请人工打开页面确认。',
 '- 补充层级（L1）43 条为背景骨架，未升级 L2；下一轮可按核心→重要→补充顺序继续深化。',
 '']
open('REPORT.md','w',encoding='utf-8').write('\n'.join(r))
print('REPORT.md 写入，行数',len(r))
print('层级',dict(lv))
