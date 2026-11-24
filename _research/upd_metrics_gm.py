# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)

note = (
    '维基第48轮可用。**本轮主要处理一起自己造成的事故**：'
    'round 66 用正则替换 PROGRESS.md 顶部状态区块时，误删 **979 行**历史记录。'
    '原因：PROGRESS.md 是**追加型**文档——40 多轮的记录都堆在"## 当前状态"区块内部'
    '（用 `- ` 列表项而非 `## ` 标题分隔），因此"到下一个 `## `"的非贪婪匹配吞掉了全部历史。'
    '处理：①先 `git show 4805ede` 取回未受损版本（997 行）；'
    '②按**行号区间**重建文档结构为 当前状态（自动生成）／历史记录（轮次 1—65，981 行）／'
    '轮次记录／状态文件，现 1012 行、**41 条轮次记录全部保留**；'
    '③教训记入 DECISIONS.md：修改追加型文档须用行号区间替换或先备份，'
    '删除超过 10 行须先 `git diff --stat` 确认影响范围。'
    '④SATURATION.json 经查仍标 saturated=true（135 条时设定），未改动——'
    '因其为历史判定的存档，而 PROGRESS.md 顶部已明确当前非饱和。'
    '当前：' + str(len(es)) + ' 条、来源 ' + str(srcn) + '、案例政策 ' + str(wp) + '/' + str(len(cases)) + '、key_data ' + str(tk) + ' 条。九道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作GL-GM', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 1, 'fixed': 1,
    'sources_total': srcn,
    'check_result': 'PASS; 九道检查全绿；PROGRESS.md 已恢复（1012行）',
    'spot_check': '修复误删979行历史记录的事故',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 在历史记录区块末尾追加本轮记录
p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
mark = '## 轮次记录'
add = '''- **维基百科第 48 轮可用（round 67）**。**本轮主要处理一起自己造成的事故**。
- **事故**：round 66 用正则 `## 当前状态.*?(?=\\n## )` 替换 PROGRESS.md 顶部状态区块，**误删 979 行**历史记录。
- **原因**：PROGRESS.md 是**追加型**文档——40 多轮记录都堆在"当前状态"区块内部（用 `- ` 列表项而非 `## ` 标题分隔），因此"到下一个 `## `"的非贪婪匹配吞掉了全部历史。
- **处理**：
  1. `git show 4805ede` 取回未受损版本（997 行）
  2. 按**行号区间**重建结构：当前状态（自动生成）／历史记录（轮次 1—65，981 行）／轮次记录／状态文件
  3. 现 **1012 行**、**41 条轮次记录全部保留**
  4. 教训记入 `DECISIONS.md`：修改追加型文档须用行号区间替换或先备份；删除超 10 行须先 `git diff --stat` 确认
- `SATURATION.json` 经查仍标 `saturated=true`（135 条时设定），**未改动**——其为历史判定的存档，而 PROGRESS.md 顶部已明确当前非饱和。
- 九道检查全绿。

'''
s = s.replace(mark, mark, 1)
# 插到历史记录末尾（即 "## 轮次记录" 之前）
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)
print('PROGRESS.md 已追加本轮记录')

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GK｜2026-11-24｜状态：625条；新增 check_docs，修复滞后40轮的文档状态**',
              '**续作GL-GM｜2026-11-24｜状态：625条；已修复误删979行历史记录的事故**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
