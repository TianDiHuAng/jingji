# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
tk = sum(len(e.get('key_data', [])) for e in es)
comp = sum(1 for e in es if e.get('comparison'))

note = (
    '维基第55轮可用。HA：**新增第 10 个检查工具 `tools/check_filler.py`**——把"无信息量内容"的判据自动化。'
    '起因：round 73 发现 57 条模板化 comparison，而 CO 轮曾手工清理过 300 条同类内容却**未固化为检查**，'
    '因此后来重新长出。本工具检测四类：'
    '①模板套话（"与同为X类"／"共享相似传导机制"／"差异在时期地区"／"与同类案例共享"）；'
    '②占位数值（unit 含"示意"／"归一化"／"非史料原值"）；'
    '③极短字段（comparison<24／overview<40 字符）；'
    '④跨条目重复句（同一句出现在 ≥3 个条目）。'
    '首次运行发现 5 处：4 条空洞 comparison（仅复述危机类型，如"北欧19世纪银行危机案例；具体异同待核实"）'
    '+ 1 处括号内元信息说明。'
    '**判断**：括号内"（理论概念条目，标准教科书定义…）"标注的是条目性质，有信息量、非填充物，'
    '故调整工具**排除括号内说明**再比对。'
    '清理 4 条空洞 comparison 后，覆盖率 ' + str(comp) + '/' + str(len(es)) + '（' + str(comp * 100 // len(es)) + '%）。'
    '工具现已全绿。至此共 **10 道检查**。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HA', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 625, 'fixed': 4,
    'sources_total': len(srcs),
    'check_result': 'PASS; 10 道检查全绿（新增 check_filler）',
    'spot_check': '新增 check_filler；清理 4 条空洞 comparison；comparison 562/625',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
# 更新顶部检查数与 comparison
s = s.replace('- 内容覆盖：`comparison` **566/625（89%）**', '- 内容覆盖：`comparison` **562/625（89%）**')
s = s.replace('- 内容覆盖：`comparison` **566/625（90%）**', '- 内容覆盖：`comparison` **562/625（89%）**')
s = s.replace('- 检查：**9 道**全绿 —— check.py／check_links.py／check_quality.py／check_kd.py／check_polnum.py',
              '- 检查：**10 道**全绿 —— check.py／check_links.py／check_quality.py／check_kd.py／check_polnum.py')
s = s.replace('  ／check_sources.py／check_body_num.py／check_docs.py',
              '  ／check_sources.py／check_body_num.py／check_docs.py／check_filler.py')
add = '''- **维基百科第 55 轮可用（round 74）**。**新增第 10 个检查工具 `tools/check_filler.py`**——把「无信息量内容」的判据自动化。
- **为什么要建它**：round 73 发现 57 条模板化 `comparison`，而 **CO 轮曾手工清理过 300 条同类内容却未固化为检查**，因此后来重新长出。手工清理只能管一次，检查才能管以后。
- 检测四类：

  | 类型 | 判据 |
  |---|---|
  | 模板套话 | "与同为X类"／"共享相似传导机制"／"差异在时期地区" |
  | 占位数值 | unit 含"示意"／"归一化"／"非史料原值" |
  | 极短字段 | comparison<24／overview<40 字符 |
  | 跨条目重复句 | 同一句出现在 ≥3 个条目 |

- 首次运行发现 **5 处**：4 条空洞 `comparison`（仅复述危机类型，如"北欧19世纪银行危机案例；具体异同待核实"）+ 1 处括号内说明。
- **判断**：括号内"（理论概念条目，标准教科书定义…）"标注的是**条目性质**，有信息量、非填充物 → 调整工具**排除括号内说明**再比对。
- 清理 4 条后，`comparison` 覆盖 **562/625（89%）**。工具现已全绿。
- **至此共 10 道检查**。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作GX-GZ｜2026-11-24｜状态：625条；删除59条无信息量内容，comparison 100%→90%（诚实下降）**',
              '**续作HA｜2026-11-24｜状态：625条；新增 check_filler，共10道检查**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', comp)
