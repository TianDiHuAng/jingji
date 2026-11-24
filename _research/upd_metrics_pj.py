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
kd = sum(len(e.get('key_data') or []) for e in es)

note = """维基第151轮可用。PJ：枚举字段取值核查（全部干净）+ 固化 R30。
①**枚举字段核查**：region（8 值）、crisis_type（8 值）、tier（3）、level（L2/L3）、unit/period（各 6）——**取值全部规范，无拼写错/近义重复**；unit×crisis_type 交叉合理（案例 U1–U5 无一标"理论"，U6 概念标制度177/理论152 及各领域类型）。
②**固化 R30**：枚举字段（region/crisis_type/tier/level/unit/period）取值须在允许集合内，否则 error。自测 34 → **35 项**。
③十一道检查全绿。
④现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 35/35。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PJ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 641, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 35/35',
    'spot_check': '枚举字段全部规范；加 R30 枚举合法性，自测 35',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 151 轮可用（round 171）**。**枚举字段取值核查（全部干净）+ 固化 R30**。
- **枚举字段核查**：region（8 值）、crisis_type（8 值）、tier（3）、level（L2/L3）、unit/period（各 6）——**取值全部规范，无拼写错/近义重复**；unit×crisis_type 交叉合理（案例 U1–U5 无一标「理论」，U6 概念标制度 177／理论 152 及各领域类型）。
- **固化 R30**：枚举字段取值须在允许集合内，否则 error。自测 34 → **35 项**。
- 十一道检查全绿。
- 现状：**641 条**、来源 **740**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 35/35。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
