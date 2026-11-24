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
pr = sum(1 for e in cases if e.get('policy_response'))

note = """维基第130轮可用。OM：把"全字段搜同款"教训沉淀为工具 find_val.py，并用它辅助补 1 条 policy_response。
①**新增 `tools/find_val.py`**：改任何数字前后，一键在 overview/one_line/comparison/policy_response[].view/key_data(label/value/note)/timeline/schools/causal_chain **所有字段**列出该值全部出现位置，避免"只改一处、漏改他处"（round 148 finnish 的 20%、round 149 sterling 的 1.60 都是此坑复发）。
②**用它验证**：`find_val "1.60"`（sterling）与 `"近20%"`（finnish）均 **0 命中**（确已全字段改净）；`"47.5%"` 得 8 处，均在 bail-in/bailout/cypriot-2013，且 cypriot-2013 源确有该值——**合法交叉引用，一致**。
③**补 1 条 policy_response**：`panic-1837`——据 w-en-panic-of-1837 缓存补"杰克逊否决第二合众国银行续照、1836 铸币流通令；范布伦拒绝政府干预"到正文并提炼。案例 policy_response 149 → **150**；check_polnum "完全找不到" = 0。
④README 工具表补 find_val.py。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；案例政策 """ + str(pr) + """ 条；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 28/28。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OM', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 10, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 28/28',
    'spot_check': '新增 find_val.py 全字段同款搜索工具；补 panic-1837 policy（政策 149→150）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 130 轮可用（round 150）**。**把「全字段搜同款」教训沉淀为工具 `find_val.py`，并用它辅助补 1 条 policy_response**。
- **新增 `tools/find_val.py`**：改任何数字前后，一键在 overview／one_line／comparison／policy_response／key_data／timeline／schools／causal_chain **所有字段**列出该值全部出现位置，避免「只改一处、漏改他处」（round 148 finnish 20%、round 149 sterling 1.60 都是此坑复发）。
- **用它验证**：`find_val "1.60"` 与 `"近20%"` 均 **0 命中**（已全字段改净）；`"47.5%"` 得 8 处，均在 bail-in／bailout／cypriot-2013，且 cypriot-2013 源确有该值——**合法交叉引用**。
- **补 1 条 policy_response**：`panic-1837`——据 `w-en-panic-of-1837` 缓存补「杰克逊否决第二合众国银行续照、1836 铸币流通令；范布伦拒绝政府干预」并提炼。案例 policy_response **149 → 150**；check_polnum「完全找不到」= 0。
- README 工具表补 `find_val.py`。
- 现状：**641 条**、来源 **742**、页面 **655**；案例政策 **150** 条；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 28/28。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | policy', pr, '| avg', avg)
