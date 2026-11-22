# -*- coding: utf-8 -*-
"""缺口发现：深度缺口 + 悬空引用 + 覆盖矩阵稀疏 + 待核实分布。"""
import json, glob, re
from collections import Counter, defaultdict

entries = {}
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f,encoding='utf-8'))
    entries[d['id']] = d
cov = json.load(open('coverage.json',encoding='utf-8'))
scope_ids = {e['id'] for e in cov['entries']}

report = ['# 缺口发现报告（轮次3）','']

# --- 方法1：深度缺口（核心条目未达L3）---
core = [d for d in entries.values() if d['tier']=='核心']
core_l2 = [d['id'] for d in core if d['level']=='L2']
report.append('## 方法1：深度缺口')
report.append(f'- 核心条目 {len(core)} 条，其中仍为 L2 的 {len(core_l2)} 条 → 升级L3候选')
report.append('- 候选：'+', '.join(sorted(core_l2)))
report.append('')

# --- 方法2：悬空引用（related 指向不存在的条目）---
dangling=[]
for d in entries.values():
    for r in d.get('related',[]):
        if r not in entries:
            dangling.append((d['id'],r))
report.append('## 方法2：悬空引用')
report.append(f'- related 指向不存在条目：{len(dangling)} 处')
for a,b in dangling[:15]: report.append(f'  - {a} → {b}')
report.append('')

# --- 方法3：覆盖矩阵稀疏（每格子条目数）---
grid=defaultdict(int)
for d in entries.values():
    grid[(d.get('period',''),d.get('crisis_type',''))]+=1
sparse=[(k,v) for k,v in grid.items() if v<=1]
report.append('## 方法3：覆盖矩阵稀疏格子（≤1条）')
for (p,t),v in sorted(sparse): report.append(f'  - {p} × {t}: {v}')
report.append('')

# --- 方法4：待核实分布 ---
needs=[d for d in entries.values() if d.get('needs_verification')]
report.append('## 方法4：待核实分布')
report.append(f'- needs_verification=true：{len(needs)}/{len(entries)}')
report.append(f'- 其中 L2：{sum(1 for d in needs if d["level"]=="L2")}，L1：{sum(1 for d in needs if d["level"]=="L1")}')
report.append('')

# --- 方法5：来源数偏少的条目（<2）---
lowsrc=[(d['id'],len(d.get('sources',[]))) for d in entries.values() if len(d.get('sources',[]))<2]
report.append('## 方法5：来源数<2的条目')
report.append(f'- 共 {len(lowsrc)} 条' + ('：'+', '.join(x[0] for x in lowsrc[:20]) if lowsrc else ''))
report.append('')

open('GAP_REPORT.md','w',encoding='utf-8').write('\n'.join(report))
print('\n'.join(report[:30]))
