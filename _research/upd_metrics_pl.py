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
cases = [e for e in es if not e['unit'].startswith('U6')]
pr = sum(1 for e in cases if e.get('policy_response'))

note = """维基第153轮可用。PL：继续宽扫补 policy_response（159→161）。
①**补 2 条 policy_response**（直接提炼正文，未引入新事实）：
`bank-holiday`（1933 各州银行假日 + 《紧急银行救济法》授权 12 家联储发行额外货币 + 择优复业 + FDIC）、
`blue-monday-2009`（英政府把 RBS 持股提高至 70% / 国有化传闻）。
②政策案例 159 → **161/209**；check_polnum 完全找不到 0；check 0/0；十一道全绿、自测 35/35。
③**各字段改动均核对总量**（policy 161、key_data 463 均符合预期，无覆盖）。
④现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；政策案例 """ + str(pr) + """/209；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PL', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 25, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 35/35',
    'spot_check': '补 2 条 policy_response（159→161）：bank-holiday / blue-monday-2009',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 153 轮可用（round 173）**。**继续宽扫补 policy_response（159 → 161）**。
- **补 2 条 policy_response**（直接提炼正文，未引入新事实）：`bank-holiday`（1933 各州银行假日 + 《紧急银行救济法》授权 12 家联储发行额外货币 + 择优复业 + FDIC）、`blue-monday-2009`（英政府把 RBS 持股提高至 70% / 国有化传闻）。
- 政策案例 159 → **161/209**；check_polnum 完全找不到 0；check 0/0；十一道全绿、自测 35/35。
- 各字段改动均核对总量（policy 161、key_data 463 均符合预期，无覆盖）。
- 现状：**641 条**、来源 **740**、页面 **655**；key_data **463**；政策案例 **161/209**；**ERRORS 0、WARNINGS 0**。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | policy', pr, '| kd', kd, '| avg', avg)
