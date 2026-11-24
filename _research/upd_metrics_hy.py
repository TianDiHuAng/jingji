# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
comp = sum(1 for e in es if e.get('comparison'))
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))

note = (
    '维基第64轮可用。HX-HY：**修复首页与验证页的口径矛盾**。'
    '①round 82 把验证页的"独立机构印证"由 15 条修正为 **2 条**，但**首页仍显示 15**——'
    '两处判据不一致（首页仍用含 `owid-*` 的旧判据）。'
    '②修正首页 `conf_total` 为**仅 fed-***（与验证页一致），并新增 `stat_total` 卡片显示"统计口径对照"（15 条）。'
    '③首页现有 **10 项统计**：632 条目／34 L3／598 L2／0 L1／730 来源／420 关键数据／'
    '**2 独立机构双源印证**／**15 统计口径对照**／47 多语种维基条目／146/207 案例载有政策。'
    '④技术上遇到 CRLF 行尾导致字符串替换失败，改用**行号定位 + 括号配平**方式定位语句边界后替换。'
    '⑤这是"修正一处后未同步其他处"的典型问题——'
    '**同一指标在两处用不同代码计算，就必然出现矛盾**；理想做法是让两处共用同一函数。'
    '现状：条目 ' + str(len(es)) + '（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HX-HY', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 646, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（首页与验证页口径统一）',
    'spot_check': '首页印证数 15→2 并新增统计口径对照卡片',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
add = '''- **维基百科第 64 轮可用（round 83）**。**修复首页与验证页的口径矛盾**。
- **问题**：round 82 把验证页"独立机构印证"由 15 条修正为 **2 条**，但**首页仍显示 15**——判据不一致（首页用含 `owid-*` 的旧判据）。
- **修正**：
  - 首页 `conf_total` 改为**仅 `fed-*`**（与验证页一致）→ **2**
  - 新增 `stat_total` 卡片「统计口径对照」→ **15**
- **首页现有 10 项统计**：

  | 项 | 值 |
  |---|---|
  | 条目总数 | 632（案例 207／概念 425） |
  | L3 / L2 / L1 | 34 / 598 / 0 |
  | 可用来源 | 730 |
  | 关键数据条数 | 420 |
  | **独立机构双源印证** | **2** |
  | **统计口径对照** | **15** |
  | 多语种维基条目 | 47 |
  | 案例载有政策应对 | 146/207 |

- **技术坑**：`gen_site.py` 是 CRLF 行尾，字符串替换失败 → 改用**行号定位 + 括号配平**定位语句边界。
- **教训**：同一指标在两处用不同代码计算，就必然出现矛盾；理想做法是两处共用同一函数。
- 十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HV-HW｜2026-11-24｜状态：632条；独立印证15→2条，新增统计口径对照15条**',
              '**续作HX-HY｜2026-11-24｜状态：632条；首页与验证页口径已统一（2/15）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
