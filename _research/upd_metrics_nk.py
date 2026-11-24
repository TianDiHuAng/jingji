# -*- coding: utf-8 -*-
import glob
import json
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'tools'))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
srcs = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pages = len(glob.glob('site/*.html'))
avg = round(sum(len(e.get('overview') or '') for e in es) / len(es))
from kdclass import counts
c = counts(es)

note = """维基第114轮可用。NJ-NK：内容审计 + 根治 check_kd 的"单位换算"缺陷。
①审计"案例 sources 全为通用页"：**0 条**——每个案例都至少有一个专属来源，结构稳健。
②审计 crisis_type 与标题一致性：9 条疑似不符，逐一核对**均合理**（法规/制度类如"国民银行法"标"制度"、"银行股灾"标"泡沫"，皆正确）。
③**根治 check_kd 的单位换算缺陷**（这个缺陷在 round 106/129/132/133 反复造成假阴性）：
（a）新增 `derived_by_unit()`：把"亿"按 billion(value/10)/million(value×100)、"万"按 million(value/100)/thousand(value×10) 推导等值数字，从而匹配来源中以 billion/million/thousand 表述的同一数值；
（b）补齐 `UNIT_PAT` 中缺失的**裸「亿」「万」**键（原只有'亿美元''百万'等复合键，导致'万挪威克朗''亿元'等无提示词）。
④效果：check_kd 强匹配 336 → **339**、弱匹配 46 → 44；单元测试（12亿↔$1.2 billion、750亿↔$75 billion、1200万↔12 million、6000万两↔60 million）全部 strong。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 18/18。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作NJ-NK', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 641, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 18/18（check_kd 强匹配 336→339）',
    'spot_check': '审计：0 条案例全通用来源、crisis_type 均合理；根治 check_kd 单位换算',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 114 轮可用（round 134）**。**内容审计 + 根治 check_kd 的「单位换算」缺陷**。
- **审计「案例 sources 全为通用页」**：**0 条**——每个案例都至少有一个专属来源，结构稳健。
- **审计 crisis_type 与标题一致性**：9 条疑似不符，逐一核对**均合理**（法规/制度类如「国民银行法」标「制度」、「银行股灾」标「泡沫」，皆正确）。
- **根治 check_kd 的单位换算缺陷**（此缺陷在 round 106／129／132／133 反复造成假阴性）：
  - 新增 `derived_by_unit()`：把「亿」按 billion(value/10)/million(value×100)、「万」按 million(value/100)/thousand(value×10) 推导等值数字
  - 补齐 `UNIT_PAT` 中缺失的**裸「亿」「万」**键（原只有「亿美元」「百万」等复合键，导致「万挪威克朗」「亿元」等无提示词）
- **效果**：check_kd 强匹配 **336 → 339**、弱匹配 46 → 44；单元测试（12亿↔$1.2 billion、750亿↔$75 billion、1200万↔12 million、6000万两↔60 million）全部 strong。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 18/18。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作ND-NI｜2026-11-24｜状态：641条；修14处key_data来源错标+记录6条缓存缺口**',
              '**续作NJ-NK｜2026-11-24｜状态：641条；审计通过 + 根治check_kd单位换算缺陷**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | avg', avg)
