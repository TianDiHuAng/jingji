# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts
c = counts(es)

note = (
    '维基第86轮可用。JK-JL：**自测从 11 项扩到 17 项，覆盖全部主要检查器**。'
    '①新增覆盖：`check_filler`（3 种模板套话 + 占位数值）、'
    '`check_links`（站内断链）、`check_quality`（缺 h1 结构）。'
    '②**结果 17/17 全部捕获**——这轮**没有发现新缺陷**，与前两轮不同：'
    'round 103 发现 R4b 变量作用域 bug、round 104 发现 deep_svg 从未被校验，'
    '而本轮所有新纳入自测的规则**都确实有效**。'
    '③这一点本身有信息量：**此前的缺陷集中在"我新写的规则"上**'
    '（R4b 与 R10b 都是当轮刚加、未经验证的），'
    '而 `check_filler`／`check_links`／`check_quality` 这些**经过多轮实战检验的工具是可靠的**。'
    '④**自测清单（17 项）**：'
    'R1 必填／R4b 嵌套来源／R7 重复 id／R8 timeline 乱序／R9 key_data 非数值／'
    'R10+10b SVG 非法元素／R12 coverage 越界／R17 来源 type／R18 link_ok／R19 内容字段缺来源／'
    '文案与导航一致性／check_filler 套话×3／check_filler 占位值／'
    'check_links 断链／check_quality 缺 h1。'
    '⑤自测的 `backup/restore` 机制经检查确认工作正常——运行后无残留 `.bak_jf` 文件，'
    '数据与页面均恢复原状。'
    '⑥**方法论意义**：从 round 100 起，四轮的主题从"改内容"转向"验证工具"，'
    '累计发现 **9 个工具缺陷**（7 个靠抽查偶然发现，2 个靠自测主动发现）。'
    '现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿 + 自测 17/17**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JK-JL', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 3, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿 + 自测 17/17',
    'spot_check': '自测覆盖全部主要检查器；本轮未发现新缺陷',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 86 轮可用（round 105）**。**自测从 11 项扩到 17 项，覆盖全部主要检查器**。
- 新增覆盖：`check_filler`（3 种模板套话 + 占位数值）、`check_links`（站内断链）、`check_quality`（缺 h1 结构）。
- **结果 17/17 全部捕获——本轮没有发现新缺陷**，与前两轮不同（103 发现 R4b 变量作用域 bug、104 发现 deep_svg 从未被校验）。
- **这一点本身有信息量**：

  | 缺陷来源 | 规律 |
  |---|---|
  | round 103 R4b、104 R10b | **都是当轮刚加、未经验证的规则** |
  | `check_filler`／`check_links`／`check_quality` | **经多轮实战检验，可靠** |

- **自测清单（17 项）**：R1／R4b／R7／R8／R9／R10+10b／R12／R17／R18／R19／文案与导航一致性／check_filler 套话×3／check_filler 占位值／check_links 断链／check_quality 缺 h1。
- 自测的 `backup/restore` 机制经检查确认工作正常——运行后**无残留 `.bak_jf` 文件**，数据与页面均恢复原状。
- **方法论意义**：从 round 100 起四轮主题从“改内容”转向“验证工具”，累计发现 **9 个工具缺陷**（7 个靠抽查偶然发现，**2 个靠自测主动发现**）。
- 十一道检查全绿 + 自测 17/17。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JG-JJ｜2026-11-24｜状态：641条；自测扩至11项，发现deep_svg从未被校验**',
              '**续作JK-JL｜2026-11-24｜状态：641条；自测扩至17项，覆盖全部主要检查器**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
