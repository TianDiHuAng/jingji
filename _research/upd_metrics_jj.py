# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
from kdclass import counts
c = counts(es)

note = (
    '维基第85轮可用。JG-JJ：**自测从 5 项扩到 11 项，并由自测发现第 9 个工具缺陷：deep_svg 从未被校验**。'
    '①扩展自测覆盖 R1（必填字段）、R7（重复 id）、R8（timeline 乱序）、R9（key_data 非数值）、'
    'R10（SVG 非法元素）、R12（coverage 含不存在条目）。'
    '②**首轮 10/11，R10 未被捕获**——排查发现：'
    'check.py 第 195 行校验的是 svg 字段（588 个条目有），'
    '而 **L3 机制图存在 deep_svg 字段（34 个条目）**，**从未被任何检查覆盖**。'
    '③**修复**：把 R10 扩展为同时校验 `deep_svg`（记为 R10b）。'
    '复核：34 条 deep_svg 的 **XML 全部可解析、元素全部在白名单内**——数据本身是好的，'
    '错的只是"从未有人检查过"。'
    '④过程中又撞上 **CRLF 问题**（round 82/83 的老毛病）：`tools/selftest.py` 是 CRLF 文件，'
    '用 `\\n` 作锚点静默匹配失败。改为读入时归一化为 LF、写回时按原风格还原，并把 CRLF 检测打印出来。'
    '另修正 R7 自测的实现（原方案需备份尚不存在的文件，改为修改现有条目制造重复 id）。'
    '⑤**自测现为 11/11 全部捕获**，涵盖数据规则（R1/R4b/R7/R8/R9/R10/R12/R17/R18/R19）'
    '与页面一致性（文案与导航）。'
    '⑥**这轮的价值在于：不是抽查撞见缺陷，而是自测主动暴露了"某个字段从未被检查"这件事**。'
    '现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '；'
    '印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿 + 自测 11/11**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作JG-JJ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 34, 'reviewed': 622, 'fixed': 3,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿 + 自测 11/11',
    'spot_check': '自测发现 deep_svg 从未被校验（34 条）；R10 已扩展',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 85 轮可用（round 104）**。**自测从 5 项扩到 11 项，并由自测发现第 9 个工具缺陷**。
- 扩展自测覆盖 R1／R7／R8／R9／R10／R12。**首轮 10/11，R10 未被捕获**——排查发现：

  | 字段 | 条目数 | 是否受检 |
  |---|---|---|
  | `svg`（基础图） | 588 | ✅ 受 R10 校验 |
  | **`deep_svg`（L3 机制图）** | **34** | **❌ 从未被任何检查覆盖** |

  `check.py` 第 195 行只校验 `e['svg']`，而 L3 机制图存在 `e['deep_svg']`。

- **修复**：R10 扩展为同时校验 `deep_svg`（R10b）。复核：34 条 deep_svg 的 **XML 全部可解析、元素全部在白名单内**——**数据本身是好的，错的只是“从未有人检查过”**。
- 过程中又撞上 **CRLF 问题**（round 82/83 的老毛病）：`tools/selftest.py` 是 CRLF 文件，用 `\\n` 作锚点**静默匹配失败**。改为读入归一化、写回还原，并打印 CRLF 检测结果。另修正 R7 自测实现（原方案需备份尚不存在的文件）。
- **自测现为 11/11 全部捕获**，涵盖数据规则（R1/R4b/R7/R8/R9/R10/R12/R17/R18/R19）与页面一致性。
- **这轮的价值**：不是抽查撞见缺陷，而是**自测主动暴露了“某个字段从未被检查”**。
- 十一道检查全绿 + 自测 11/11。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作JF｜2026-11-24｜状态：641条；建立检查器自测，发现R4b只检查1个条目**',
              '**续作JG-JJ｜2026-11-24｜状态：641条；自测扩至11项，发现deep_svg从未被校验**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
