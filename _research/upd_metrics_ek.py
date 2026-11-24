# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])

note = (
    '维基第22轮不可达。EJ/EK修复两类HTML语义与可访问性缺陷：'
    '①**标题层次跳级**：条目页分节标题原用 h3，而页面只有 h1——h1 直接跳到 h3，'
    '屏幕阅读器无法正确解析结构。已改为 h2 并同步 CSS（视觉不变），'
    '全站606页现无标题跳级（0处）。'
    '②**覆盖矩阵页结构缺陷**：原 Markdown→HTML 转换对每个表格行生成**独立的 <table>**，'
    '且全部单元格用 <td>、无 <th> 表头——结果矩阵A/B/C 各自散成26个单行表格，'
    '屏幕阅读器与复制粘贴都会错乱。已重写：合并连续行为单一表格、首行用 <th>，'
    '并过滤 Markdown 分隔行（此前被误当作段落输出）。'
    '修复后：6个表格、60个 th、26行；全站缺 th 的表格 0 个。'
    '③可访问性其他项核查通过：lang 属性 100%、SVG 均有 role="img"、viewport 100%。'
    '站点规模：CSS 3.6KB、平均页 6KB、全站 3MB/606页、零 JS。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EJ-EK', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 606, 'fixed': 2,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error',
    'spot_check': '标题层次跳级 0 处；缺 th 的表格 0 个',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EI（单元页导语+字段/性能核查）',
              '- 当前轮次：续作EJ-EK（HTML语义与可访问性修复）')
entry = '''- **维基百科第 22 轮不可达**。继续站点质量工作，修复两类**HTML 语义与可访问性缺陷**：
  1. **标题层次跳级**：条目页分节标题原用 `h3`，而页面只有 `h1`——**h1 直接跳到 h3**，屏幕阅读器无法正确解析文档结构。已改为 `h2` 并同步 CSS（视觉不变）。全站 606 页现**无标题跳级（0 处）**。
  2. **覆盖矩阵页的结构缺陷**：原 Markdown→HTML 转换对**每个表格行生成独立的 `<table>`**，且全部单元格用 `<td>`、**无 `<th>` 表头**——结果矩阵 A/B/C 各自散成 26 个单行表格。已重写：合并连续行为单一表格、首行用 `<th>`，并过滤 Markdown 分隔行（此前被误当作段落 `<p>` 输出）。修复后：**6 个表格、60 个 th、26 行**；全站缺 th 的表格 **0 个**。
- 可访问性其他项核查**通过**：`lang` 属性 100%、SVG 均有 `role="img"`、`viewport` 100%。
- 站点规模：CSS **3.6KB**、平均页 **6KB**、全站 **3MB/606页**、零 JS。
- 现状：**总592条，来源695，站点606页**；comparison 与 related 双 100%。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EI｜2026-11-24｜状态：592条；单元页导语已加，双100%维持**',
              '**续作EJ-EK｜2026-11-24｜状态：592条；HTML语义与可访问性修复完成**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
