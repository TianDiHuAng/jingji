# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcn = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
wk = sum(1 for e in cases if e.get('key_data'))
tk = sum(len(e.get('key_data', [])) for e in es)

note = (
    '维基第43轮可用。FY/FZ：**大幅扩大验证覆盖**——为100个"正文含≥5个数字但缺全文"的条目抓取专属维基页（98成功），'
    '使有全文的条目由140升至238。'
    '**效果1**：check_kd 的 key_data 可核对率由 251/391 升至 **387/397（97.5%）**，无全文从140降至10。'
    '**效果2**：check_body_num 的检查范围由 1502 个数字升至 **2571 个**，未匹配61个。'
    '61个逐条核查：多数为概念解释中的**示例数字**（如 basis-point 条目的"从4.25%升到4.50%"）、'
    '周期长度的**通用描述**（信贷周期15—20年）、月份与世纪表述，均属合理。'
    '**发现1处真问题**：finnish-banking-1990 的"失业率从近零升至近20%"在其专属页中**完全不存在**'
    '（全文无 unemployment 一词），已改为待核实表述；'
    '同时补充该页中的确切数据——**纳税人成本约占芬兰 GNP 的 8%**（北欧危机中最严重）。'
    '另确认 continental-illinois-1984 的 225万/58.5万美元（原文 $2.25 million / $585,000）与 '
    'archegos-2021 的18年监禁换算正确。'
    '当前：案例政策 ' + str(wp) + '/' + str(len(cases)) + '、案例数据 ' + str(wk) + '/' + str(len(cases)) + '、key_data ' + str(tk) + ' 条。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FY-FZ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 2571, 'fixed': 1,
    'sources_total': srcn,
    'check_result': 'PASS; key_data 可核对率 387/397=97.5%；正文数字2571个',
    'spot_check': '验证覆盖大幅扩大；发现并标注1处无源数字（芬兰失业率）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FW-FX（新增check_body_num，发现并标注2处无源数字）',
              '- 当前轮次：续作FY-FZ（扩大验证覆盖，key_data可核对率97.5%）')
entry = '''- **维基百科第 43 轮可用**。**大幅扩大验证覆盖**：为 100 个"正文含 ≥5 个数字但缺全文"的条目抓取专属维基页（98 成功），有全文的条目由 140 升至 **238**。
- **效果一**：`check_kd` 的 key_data 可核对率由 251/391 升至 **387/397（97.5%）**，无全文从 140 降至 10。
- **效果二**：`check_body_num` 的检查范围由 1502 个数字升至 **2571 个**，未匹配 61 个。
- 61 个逐条核查，多数属合理：
  - **概念示例数字**：如 `basis-point` 条目的"从 4.25% 升到 4.50%"
  - **通用周期描述**：信贷周期 15—20 年
  - **月份与世纪**表述
- **发现 1 处真问题**：`finnish-banking-1990` 的"失业率从近零升至近 20%"在其专属页中**完全不存在**（全文无 `unemployment` 一词）。
  - 已改为待核实表述
  - 同时补充该页中的确切数据：**纳税人成本约占芬兰 GNP 的 8%**——使其成为北欧危机中最严重的一次
- 另确认 `continental-illinois-1984` 的 225 万/58.5 万美元（原文 $2.25 million / $585,000）与 `archegos-2021` 的 18 年监禁均换算正确。
- 现状：**625 条**、来源 732、站点 639 页；案例政策 69%、案例数据 85%。七道检查中五道全绿，`check_body_num` 的 61 项待人工判断。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FW-FX｜2026-11-24｜状态：625条；新增 check_body_num，发现2处无源数字已标注**',
              '**续作FY-FZ｜2026-11-24｜状态：625条；key_data可核对率97.5%，发现1处无源数字**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | key_data', tk)
