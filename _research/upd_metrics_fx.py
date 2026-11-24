# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
wk = sum(1 for e in cases if e.get('key_data'))

note = (
    '维基第42轮可用。FW/FX：**新增第7个检查工具 tools/check_body_num.py**，'
    '核对 overview/comparison/one_line 中的数字能否溯源（对照来源全文 + 条目自身 key_data/timeline）。'
    '初版检查 1502 个数字，148 个未匹配；改进后排除年份引用、聚焦真实数值，降至 34 个。'
    '**发现 2 处真问题**：dotcom-bubble-2000 的"高通上涨2619%、12只超1000%、7只超900%"、'
    'panic-1901 的"从170美元涨至1000美元"——**在各自专属维基页中均找不到**，'
    '而这两条本就标着 needs_verification=true。'
    '按项目原则（不编造数字），**不删信息但改为待核实表述**：'
    '明确写出"现行来源页面未载该数值，需补充出处"。'
    '另重抓 dotcom 的专属页（Dot-com_bubble，20202字符），确认 600%/78%/900% 可溯源。'
    'blue-monday-2009 经查维基**无专属条目**（来源仅通用页），已记入 BACKLOG。'
    '至此共 **7 道检查**。当前：案例政策 ' + str(wp) + '/' + str(len(cases)) + '、'
    '案例数据 ' + str(wk) + '/' + str(len(cases)) + '、来源 ' + str(srcn) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FW-FX', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 1502, 'fixed': 2,
    'sources_total': srcn,
    'check_result': 'PASS; 7 道检查全绿（正文数字1502个中34个需人工判断）',
    'spot_check': '发现并标注2处无源数字；新增check_body_num工具',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FV（新增check_sources，来源抽样可达性良好）',
              '- 当前轮次：续作FW-FX（新增check_body_num，发现并标注2处无源数字）')
entry = '''- **维基百科第 42 轮可用**。**新增第 7 个检查工具 `tools/check_body_num.py`**——核对 `overview`／`comparison`／`one_line` 中的数字能否溯源。
- 初版检查 **1502 个数字**，148 个未匹配；改进后排除**年份引用**、聚焦真实数值，降至 34 个。
- **发现 2 处真问题**（本轮最重要的收获）：

  | 条目 | 无法溯源的数字 | 情况 |
  |---|---|---|
  | dotcom-bubble-2000 | 高通上涨 **2619%**、12 只超 1000%、7 只超 900% | 在专属维基页 `Dot-com_bubble` 中**不存在** |
  | panic-1901 | 从 **170 美元**涨至 **1000 美元** | 在 `Panic_of_1901` 中**不存在** |

  这两条本就标着 `needs_verification: true`，但正文里的具体数字未被核实过。
- **处理方式：不删信息，改为待核实表述**。按项目原则（不编造数字），把断言改成——
  > 「具体涨幅数值待核实：现行来源页面未载 2619%、超1000%、超900% 三项，需补充出处」
  
  这样保留了线索，同时明确标注了不确定性。
- 另重抓 `dotcom-bubble-2000` 的专属页（`Dot-com_bubble`，20202 字符），确认 **600%／78%／900%** 可溯源。
- `blue-monday-2009` 经查维基**无专属条目**（来源仅通用页），已记入 BACKLOG。
- **至此共 7 道检查**。现状：**625 条**、来源 732、站点 639 页；案例政策 69%、案例数据 85%。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FV｜2026-11-24｜状态：625条；新增 check_sources，六道检查全绿**',
              '**续作FW-FX｜2026-11-24｜状态：625条；新增 check_body_num，发现2处无源数字已标注**')
open(r, 'w', encoding='utf-8').write(t)
print('updated')
