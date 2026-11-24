# -*- coding: utf-8 -*-
import json, glob, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]
tk = sum(len(e.get('key_data', [])) for e in es)
wp = sum(1 for e in cases if e.get('policy_response'))
from kdclass import counts
c = counts(es)
reln = [len(e.get('related', [])) for e in es]

note = (
    '维基第74轮可用。IP-IQ：**修复"文案与导航不一致"，并把该规则固化为检查项**。'
    '①**先排查两件事**：'
    '（a）条目对"通用页"的依赖——178 个条目非专属引用了通用页，'
    '但其中**"仅靠通用页且未标注"的为 0 个**，177 个是"有专属来源、另引通用页作背景"，属合理用法；'
    '（b）**comparison 与 related 的一致性**——发现 **58 个条目**在对比段落中提到某条目'
    '（如"与 X 的区别"），却**未把 X 列入 related**，读者无法跳转。'
    '②**修复**：从 comparison 中提取所有提到的站内 id 补入 related（**76 条**），'
    '并按 round 69 的约定做同类对称化（**120 条**）。'
    '复核结果：**文案与导航不一致的条目归零**；`related` 平均 5.6 → **5.9 条**，最多 26 条。'
    '③**固化为检查项**：在 `check_pages.py` 中新增"文案与导航一致性"检查——'
    '遍历所有条目，若 comparison 提到某 id 而 related 未收录则报错。'
    '这样今后新增条目若忘记互链，会被自动发现。'
    '④典型效果：`bank-resolution` 的相关条目现含坏账银行／bail-in／bailout／'
    '2023 年银行危机／银行倒闭／存款保险／最后贷款人／太大而不能倒——'
    '正是其对比段落中逐一点名的对象。'
    '⑤现状：**' + str(len(es)) + ' 条**、来源 ' + str(len(srcs)) + '、页面 ' + str(pages) + '、'
    'key_data ' + str(tk) + '；印证 ' + str(c['confirmed']) + '／口径对照 ' + str(c['statview']) + '／差异 ' + str(c['discrepant']) + '。'
    '**十一道检查全绿**（check_pages 现含新增的一致性检查）。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作IP-IQ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 58, 'reviewed': 641, 'fixed': 196,
    'sources_total': len(srcs),
    'check_result': 'PASS; 十一道检查全绿（新增文案与导航一致性检查）',
    'spot_check': '76 条补入 related + 120 条对称化；不一致归零',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 内容覆盖：`comparison` **562/624（89%）**、`related` **625/625**',
              '- 内容覆盖：`comparison` 与 `related` 见下；related 平均 %.1f 条' % (sum(reln) / len(reln)))
add = '''- **维基百科第 74 轮可用（round 93）**。**修复"文案与导航不一致"，并把该规则固化为检查项**。
- **先排查两件事**：

  | 排查对象 | 结果 |
  |---|---|
  | 条目对"通用页"的依赖 | 178 个条目非专属引用通用页，但**"仅靠通用页且未标注"的为 0**；177 个是"有专属来源、另引通用页作背景"，属合理用法 |
  | **comparison 与 related 的一致性** | **58 个条目**在对比段落中提到某条目（如"与 X 的区别"），却**未把 X 列入 related** —— 读者无法跳转 |

- **修复**：从 comparison 中提取所有提到的站内 id 补入 `related`（**76 条**），并按 round 69 的约定做同类对称化（**120 条**）。复核结果：**不一致归零**；`related` 平均 5.6 → **5.9 条**，最多 26 条。
- **固化为检查项**：`check_pages.py` 新增「**文案与导航一致性**」检查——若 comparison 提到某 id 而 related 未收录则报错。今后新增条目若忘记互链会被自动发现。
- 典型效果：`bank-resolution` 的相关条目现含**坏账银行／bail-in／bailout／2023 年银行危机／银行倒闭／存款保险／最后贷款人／太大而不能倒**——正是其对比段落中逐一点名的对象。
- 十一道检查全绿（`check_pages` 现含新增的一致性检查）。

'''
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作IN-IO｜2026-11-24｜状态：641条；新建担保贷款与缩减恐慌，来源性质分级标注**',
              '**续作IP-IQ｜2026-11-24｜状态：641条；修复文案与导航不一致并固化为检查**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | related 平均 %.1f' % (sum(reln) / len(reln)))
