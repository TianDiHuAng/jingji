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
single = [e['id'] for e in es if len(e.get('sources', [])) == 1]

note = (
    '维基第62轮可用。HR-HU：**继续补单来源条目，并对一处不严谨的处理做了自我修正**。'
    '①用多候选标题再测中文维基，命中 12 项（排除 2 项不完全等价的：'
    '`counterparty-risk`→信用風險、`expectations`→理性预期，二者与条目标题不等义），'
    '为 **10 个**概念补上跨语言第二来源（精算師／貴金屬／去工業化／需求曲線／股息／有效需求／'
    '莫迪利安尼-米勒定理／財產權／分工／有毒资产）。'
    '②**跨语言对照由 39 升至 41 条**；单来源条目 29 → **17**；来源库 730。'
    '③**自我修正**：起初为两个衰退条目补 NBER 并想算作"第二独立来源"，'
    '但随后意识到——维基页面所载的"10／11 个月"**本就引自 NBER**，'
    'NBER 是**原始出处**、维基是转引，二者**不构成相互独立的双源印证**。'
    '已改写 note 明确这一关系，并把该数值仍归为"单源待核实"。'
    '④同时确立一条判断标准：**不以"相关概念页"充作第二来源**——'
    '相关页面可用于补充内容，但不能当作独立印证。'
    '剩余 17 个单来源条目均为 U6 概念条目，其定义为教科书共识而非需双源印证的具体数值，'
    '已统一标 needs_verification。'
    '现状：**' + str(len(es)) + ' 条**（案例 ' + str(len(cases)) + '／概念 ' + str(len(concepts)) + '）、'
    '来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、key_data ' + str(tk) + '、'
    'comparison ' + str(comp) + '、案例政策 ' + str(wp) + '/' + str(len(cases)) + '。十道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作HR-HU', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 12, 'reviewed': 29, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十道检查全绿（跨语言对照 39→41）',
    'spot_check': '10 概念补中文维基；自我修正"NBER≠第二独立来源"',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- **来源：720**（全部 verified 且可达）', '- **来源：%d**（全部 verified 且可达）' % len(srcs))
add = '''- **维基百科第 62 轮可用（round 81）**。**继续补单来源条目，并对一处不严谨的处理做了自我修正**。
- **① 再补 10 个跨语言第二来源**（多候选标题测试命中 12 项，排除 2 项不等义的：`counterparty-risk`→信用風險、`expectations`→理性预期）：

  精算師／貴金屬／去工業化／需求曲線／股息／有效需求／莫迪利安尼-米勒定理／財產權／分工／有毒资产

- **② 效果**：跨语言对照 39 → **41 条**；单来源条目 29 → **17**；来源库 **730**。
- **③ 自我修正**：起初为两个衰退条目补 NBER 并想算作"第二独立来源"，随后意识到——维基所载的"10／11 个月"**本就引自 NBER**，NBER 是**原始出处**、维基是转引，二者**不构成相互独立的双源印证**。已改写 `note` 明确这一关系，并把该数值仍归为"单源待核实"。
- **④ 确立判断标准**：**不以"相关概念页"充作第二来源**——相关页面可用于补充内容，但不能当作独立印证。
- 剩余 17 个单来源条目均为 U6 概念条目，其定义为教科书共识而非需双源印证的具体数值，已统一标 `needs_verification`。
- 现状：**632 条**、来源 **730**、页面 **646**。十道检查全绿。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作HO-HQ｜2026-11-24｜状态：632条；补12个跨语言第二来源，跨语言对照31→39**',
              '**续作HR-HU｜2026-11-24｜状态：632条；再补10个跨语言来源，并自我修正NBER≠第二来源**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 单来源', len(single), '| 来源', len(srcs))
