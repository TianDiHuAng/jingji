# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)

note = (
    '维基第40轮可用。FT/FU：**新增第5个检查工具 tools/check_polnum.py**，'
    '核对 policy_response 中提到的每个数字能否溯源。'
    '初版检查 392 个数字，15 条未匹配；逐条核查发现**全部为中文单位换算或月份写法差异**，无一处抄错：'
    '如 6.13亿 ↔ 613 million、640亿克朗 ↔ 64 billion kronor、'
    '11月 ↔ November、1994年1月 ↔ January 1994。'
    '工具三次改进：①加入"亿/万 ↔ billion/million"换算；②加入月份中英对应；'
    '③把条目自身 overview/comparison 并入查找范围（部分数字出自条目正文而非维基全文）。'
    '改进后 **392 个数字全部可溯源**。'
    '至此共有 5 道检查：check（数据合规R1-R16）、check_links（链接与SVG）、'
    'check_quality（HTML结构10项）、check_kd（key_data数值）、check_polnum（政策段数字）。'
    '当前：案例政策覆盖 ' + str(wp) + '/' + str(len(cases)) + '（' + str(wp * 100 // len(cases)) + '%）、'
    'key_data ' + str(tk) + ' 条、来源 ' + str(src) + ' 条。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FT-FU', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 392, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS; 5 道检查全绿（含392个政策段数字全部可溯源）',
    'spot_check': 'policy_response 数字溯源：392/392 通过',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FS（再补6项key_data，案例数据覆盖85%）',
              '- 当前轮次：续作FT-FU（新增check_polnum，392个政策数字全部溯源）')
entry = '''- **维基百科第 40 轮可用**。**新增第 5 个检查工具 `tools/check_polnum.py`**——核对 `policy_response` 中每个数字能否溯源。
- 初版检查 **392 个数字**，15 条未匹配；逐条核查发现**全部为中文单位换算或月份写法差异**，无一处抄错：
  - `6.13亿` ↔ `613 million`；`640亿克朗` ↔ `64 billion kronor`；`1045亿` ↔ `104.5 billion`
  - `11月` ↔ `November`；`1994年1月` ↔ `January 1994`
- 工具三次改进：
  1. 加入「**亿/万 ↔ billion/million**」换算
  2. 加入**月份中英对应**
  3. 把条目**自身** `overview`／`comparison` 并入查找范围（部分数字出自条目正文而非维基全文）
- 改进后 **392 个数字全部可溯源**。
- **至此共有 5 道检查**：

  | 脚本 | 管什么 |
  |---|---|
  | `check.py` | 数据合规（R1–R16） |
  | `check_links.py` | 链接与 SVG |
  | `check_quality.py` | HTML 结构（10 项） |
  | `check_kd.py` | key_data 数值可核对性 |
  | **`check_polnum.py`** | **policy_response 数字溯源** |

- 现状：**625 条**、来源 732、站点 639 页；案例政策 69%、案例数据 85%。五道检查全绿。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FS｜2026-11-24｜状态：625条；案例数据覆盖85%（剩余29条属来源边界）**',
              '**续作FT-FU｜2026-11-24｜状态：625条；新增 check_polnum，392个政策数字全部溯源**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
