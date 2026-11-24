# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])

note = (
    '维基第23轮不可达。EL-EO修复同页多SVG的重复id与重复属性问题，过程经历三次迭代：'
    '①发现：28页有重复 id="arrowhead"——原 fix_svg 给每个含箭头的 SVG 注入同名 marker 定义，'
    '而条目页有2个SVG（机制图+L3深度图），导致 id 重复（HTML 要求 id 唯一）。'
    '②第一版改为"单页只注入一次"，但造成第二个 SVG 依赖跨SVG引用 marker（浏览器兼容风险）。'
    '③第二版改为每SVG唯一id + 内联 marker-end 引用，但替换逻辑对已有 style 属性的元素'
    '**新增**了一个 style（duplicate attribute），且自闭合标签 <x/> 的处理把 / 放错位置，'
    '导致 check_links 的 SVG XML 解析在 581 页失败。'
    '④最终版：已有 style 则把 marker-end 合并进去；自闭合标签在 /> 之前插入。'
    '结果：重复id 0/606、重复style 0、SVG XML 解析 0 错误、check.py 0 error。'
    '教训：生成逻辑的修改必须由检查脚本验证——若无 check_links 的 SVG XML 解析检查，'
    '这类"页面能显示但结构非法"的问题不会暴露。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EL-EO', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 606, 'fixed': 3,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error（含SVG XML解析）',
    'spot_check': '重复id 0/606；重复style 0；SVG XML解析0错误',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EJ-EK（HTML语义与可访问性修复）',
              '- 当前轮次：续作EL-EO（SVG重复id与重复属性修复，三次迭代）')
entry = '''- **维基百科第 23 轮不可达**。修复同页多 SVG 的**重复 id 与重复属性**问题。这一过程经历了三次迭代，本身就值得记：
  1. **发现**：28 页有重复 `id="arrowhead"`——原 `fix_svg` 给每个含箭头的 SVG 注入**同名** marker 定义，而条目页有两个 SVG（机制图 + L3 深度图），id 必然重复（HTML 要求 id 唯一）。
  2. **第一版**改为"单页只注入一次"——但造成第二个 SVG 依赖**跨 SVG 引用** marker，有浏览器兼容风险。
  3. **第二版**改为每 SVG 唯一 id + 内联 `marker-end` 引用，但替换逻辑对**已有 `style` 属性**的元素又新增了一个 `style`（duplicate attribute），且自闭合标签 `<x/>` 的处理把 `/` 放错位置——导致 `check_links` 的 **SVG XML 解析在 581 页失败**。
  4. **最终版**：已有 `style` 则把 `marker-end` **合并进去**；自闭合标签在 `/>` **之前**插入。
- 结果：**重复 id 0/606、重复 style 0、SVG XML 解析 0 错误**、check.py 0 error。
- **教训**：生成逻辑的修改必须由检查脚本验证。若无 `check_links` 的 SVG XML 解析检查，这类"页面能显示但结构非法"的问题不会暴露——这正是 round 40 提到的"check.py 只查数据合规、不查 HTML 语义"的延续。
- 现状：**总592条，来源695，站点606页**；comparison 与 related 双 100%。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EJ-EK｜2026-11-24｜状态：592条；HTML语义与可访问性修复完成**',
              '**续作EL-EO｜2026-11-24｜状态：592条；SVG重复id清零（三次迭代）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
