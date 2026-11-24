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
cases = [e for e in es if not e['unit'].startswith('U6')]
cc = sum(1 for e in cases if e.get('causal_chain'))

note = """维基第138轮可用。OW：区块覆盖度审计，补齐 4 条案例的 causal_chain；加 R27。
①**网络**：仍 URLError 不可用。
②**单元页核对**：unit-u1..u6 列出的条目数与数据完全一致（10/37/34/50/78/432），无误。
③**覆盖度审计**：案例 209 条 overview/one_line/timeline/comparison/related 全覆盖；key_data 183、policy 156、causal_chain 205、deep_svg 24。
④**补齐 4 条 causal_chain**（据各自正文机制与已引来源，不引入新事实）：bank-holiday、recession-1960-1961、recession-1969-1970、taper-tantrum——**案例 causal_chain 覆盖 205 → 209（全覆盖）**。
⑤**固化 R27**：核心/重要案例须有 causal_chain，否则 warning。自测 31 → **32 项**。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；案例 causal_chain """ + str(cc) + """/209；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 32/32。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OW', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 4, 'reviewed': 641, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 32/32',
    'spot_check': '补 4 条 causal_chain（205→209 全覆盖）+ R27，自测 32；单元页计数核对全一致',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 138 轮可用（round 158）**。**区块覆盖度审计，补齐 4 条案例的 causal_chain；加 R27**。
- **网络**：仍 URLError 不可用。
- **单元页核对**：unit-u1..u6 列出的条目数与数据完全一致（10/37/34/50/78/432），无误。
- **覆盖度审计**：案例 209 条 overview／one_line／timeline／comparison／related 全覆盖；key_data 183、policy 156、causal_chain 205、deep_svg 24。
- **补齐 4 条 causal_chain**（据各自正文机制与已引来源，不引入新事实）：`bank-holiday`、`recession-1960-1961`、`recession-1969-1970`、`taper-tantrum`——**案例 causal_chain 覆盖 205 → 209（全覆盖）**。
- **固化 R27**：核心/重要案例须有 causal_chain，否则 warning。自测 31 → **32 项**。
- 现状：**641 条**、来源 **742**、页面 **655**；案例 causal_chain **209/209**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 32/32。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | cc', cc, '| avg', avg)
