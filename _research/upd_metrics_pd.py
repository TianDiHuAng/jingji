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

note = """维基第145轮可用。PD：多项一致性核查（均干净）+ 固化 R29（案例 period 与 unit 对应）。
①**网络**：仍 URLError。
②**核查均干净**：one_line／comparison **跨条目完全相同 = 0**；来源库 740 中 **724 被引用、16 未引用**（为书籍/机构参考资源，GAP_REPORT 已声明保留，不动）；**案例 unit 与 period 完全对应**（432 条"不符"均为 U6 概念用"理论制度"作 period 标签，非错）。
③**固化 R29**：案例 period 须与 unit 对应（U1–U5；U6 不适用），防时期字段漂移。自测 33 → **34 项**。
④十一道检查全绿。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 34/34。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PD', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 641, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 34/34',
    'spot_check': '多项一致性核查干净；加 R29（案例 period↔unit），自测 34',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 145 轮可用（round 165）**。**多项一致性核查（均干净）+ 固化 R29（案例 period 与 unit 对应）**。
- **网络**：仍 URLError。
- **核查均干净**：one_line／comparison **跨条目完全相同 = 0**；来源库 740 中 **724 被引用、16 未引用**（为书籍/机构参考资源，GAP_REPORT 已声明保留，不动）；**案例 unit 与 period 完全对应**（432 条「不符」均为 U6 概念用「理论制度」作 period 标签，非错）。
- **固化 R29**：案例 period 须与 unit 对应（U1–U5；U6 不适用），防时期字段漂移。自测 33 → **34 项**。
- 现状：**641 条**、来源 **740**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 34/34。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
