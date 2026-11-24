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

note = """维基第140轮可用。OY：继续为有缓存的案例补 key_data（showa/merrill），key_data 450→453。
①**网络**：仍 URLError。
②**补 2 条案例 key_data**（据各自专属缓存）：
`showa-crisis-1927`（1927 昭和金融危机：三周银行假日 + 紧急贷款，据 w-en-sh-wa-financial-crisis）、
`merrill-lynch`（2007-11 次贷相关减记 8.4 十亿美元、2025 年等值 12.5 十亿美元，据 w-en-merrill-lynch）。
③**验证 check_docs 修复生效**：key_data 由 450→453，check_docs **成功报出** REPORT 的 `key_data` 450 需更新为 453（上轮加反引号后该项已纳入核对），同步 REPORT/HEALTH。
④check_kd 强匹配 339 → **342**（3 条新增均 strong）；十一道检查全绿。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """ 行；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 32/32。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OY', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 4, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 32/32',
    'spot_check': 'showa/merrill 补 key_data（450→453）；check_kd 强匹配 339→342；验证 check_docs 修复生效',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 140 轮可用（round 160）**。**继续为有缓存的案例补 key_data（showa/merrill），key_data 450 → 453**。
- **网络**：仍 URLError。
- **补 2 条案例 key_data**（据各自专属缓存）：`showa-crisis-1927`（1927 昭和金融危机：三周银行假日 + 紧急贷款）、`merrill-lynch`（2007-11 次贷相关减记 8.4 十亿美元、2025 年等值 12.5 十亿美元）。
- **验证 check_docs 修复生效**：key_data 450→453，check_docs **成功报出** REPORT 的 `key_data` 450 需改为 453（上轮加反引号后该项已纳入核对），同步 REPORT/HEALTH。
- check_kd 强匹配 339 → **342**；十一道检查全绿。
- 现状：**641 条**、来源 **742**、页面 **655**；key_data **453** 行；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 32/32。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | kd', kd, '| avg', avg)
