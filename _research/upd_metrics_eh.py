# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))
reln = sum(1 for e in es if e.get('related'))
kdn = sum(len(e.get('key_data', [])) for e in es)
cases = [e for e in es if not e['unit'].startswith('U6')]
pol = sum(1 for e in cases if e.get('policy_response'))

note = (
    '维基第20轮不可达。EG/EH两批共为89条条目建立关联，**related达成100%全覆盖（' + str(reln) + '/' + str(len(es)) + '）**。'
    '至此**全站每个条目都同时具有 comparison（与其他条目的对照分析）与 related（语义关联）**，'
    '知识网络的两个维度均已关闭缺口。'
    'EG按主题建关联（制度机构/理论概念/案例），EH补完最后16条（ALM/指券/救助/以邻为壑/黑市/'
    '债券危机1994/看涨期权/资本结构/央行独立性/中央对手方/熔断/商业革命/商品价格指数/大陆币/可转债/创造性破坏）。'
    '过程中又发现3个缺失：recession（衰退，基础概念）、modigliani-miller（资本结构定理）、counterparty-risk（对手方风险）。'
    '当前：comparison ' + str(cmpn) + '/592（100%）、related ' + str(reln) + '/592（100%）、'
    'key_data ' + str(kdn) + '、案例政策 ' + str(pol) + '/' + str(len(cases)) + '（41%，已达来源上限）。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EG-EH', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 89, 'reviewed': 89, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error',
    'spot_check': '**related 100% 全覆盖（' + str(reln) + '/' + str(len(es)) + '）**',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EF（related覆盖达85%）',
              '- 当前轮次：续作EG-EH（related达成100%全覆盖）')
entry = '''- **维基百科第 20 轮不可达**。
- 续作EG–EH：两批共为 89 条条目建立关联，`related` 从 85% 推到 **100% 全覆盖（592/592）**。
- **至此知识网络的两个维度均已关闭缺口**：全站每个条目都同时具有
  - `comparison`（与其他条目的对照分析）——**592/592**
  - `related`（语义关联）——**592/592**
- 最后补完的 16 条包括：ALM、指券、救助(bailout)、以邻为壑、黑市、1994债券危机、看涨期权、资本结构、央行独立性、中央对手方、熔断机制、商业革命、商品价格指数、大陆币、可转债、创造性破坏。
- **又发现 3 个缺失概念**：`recession`（衰退，仍是基础概念）、`modigliani-miller`（资本结构定理）、`counterparty-risk`（对手方风险）。
- 当前三维度覆盖：`comparison` **100%**、`related` **100%**、案例政策 **41%（已达来源上限）**。
- 现状：**总592条，来源695，站点606页**。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EF｜2026-11-24｜状态：592条；related 85%（comparison 100%）**',
              '**续作EG-EH｜2026-11-24｜状态：592条；comparison 与 related 双100%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', cmpn, '| related', reln, '| policy', pol, '/', len(cases))
