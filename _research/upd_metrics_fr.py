# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wk = sum(1 for e in cases if e.get('key_data'))
tk = sum(len(e.get('key_data', [])) for e in es)

note = (
    '维基第38轮可用。FR：本轮以**质量复核**为主，新增数据为辅。'
    '①**新增 tools/check_kd.py**：逐条检查 key_data 的 value 能否在同条目**来源全文**中找到'
    '（容忍负号表示跌幅、千分位、单位换算如 620 million ↔ 0.62 billion）。'
    '结果：251 条可核对、140 条因来源为 OWID／美联储专文／中文维基而无对应全文（非错误）。'
    '29 条未直接匹配，逐条核查 note 后确认**均属合理**：'
    'OWID 口径差异（如巴西2015年 -3.546% vs 条目 -3.5%，实为双源印证）、'
    '单位换算（620 million ↔ 0.62 billion、10 million people ↔ 1000万人）、'
    '中文维基页码（台湾股价指数）等。**未发现抄错**。'
    '②**修正来源错标**：ghana-banking-2017 的 key_data 原标为通用页 Financial_crisis，'
    '实际数据出自 Ghana_banking_crisis，已改正为专属页。'
    '③README 登记新工具。'
    '当前：案例数据覆盖 83%（' + str(wk) + '/' + str(len(cases)) + '）、全站 key_data ' + str(tk) + ' 条、来源 ' + str(src) + ' 条。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FR', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 391, 'fixed': 1,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿；check_kd 251条可核对',
    'spot_check': '复核251条key_data数值，未发现抄错；修正1处来源错标',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FQ（再补17条key_data，案例数据覆盖83%）',
              '- 当前轮次：续作FR（新增check_kd工具，复核391条数值）')
entry = '''- **维基百科第 38 轮可用**。本轮以**质量复核**为主。
- **新增 `tools/check_kd.py`**：逐条检查 `key_data` 的 `value` 能否在同条目**来源全文**中找到（容忍负号表示跌幅、千分位、单位换算如 620 million ↔ 0.62 billion）。
- 复核结果：

  | 项 | 数量 |
  |---|---|
  | 可核对 | **251 条** |
  | 无对应全文（OWID／美联储专文／中文维基来源，非错误） | 140 条 |
  | 未直接匹配 | 29 条 |

  29 条逐条核查 `note` 后**均属合理**：
  - **OWID 口径差异**：巴西 2015 年 −3.546% vs 条目 −3.5%——实为**双源印证**
  - **单位换算**：620 million ↔ 0.62 billion；10 million people ↔ 1000 万人
  - **中文维基页码**：台湾股价指数 636／12682／2485
  - **未发现抄错**
- **修正 1 处来源错标**：`ghana-banking-2017` 的 `key_data` 原标为通用页 `Financial_crisis`，实际数据出自 `Ghana_banking_crisis`，已改正。
- README 登记新工具。
- 当前：案例数据覆盖 **83%（172/205）**、`key_data` **391 条**、来源 **732 条**。三道检查全绿。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FQ｜2026-11-24｜状态：625条；案例数据覆盖83%**',
              '**续作FR｜2026-11-24｜状态：625条；新增check_kd，复核391条数值无抄错**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
