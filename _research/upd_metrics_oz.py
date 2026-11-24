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
ncase_kd = sum(1 for e in es if not e['unit'].startswith('U6') and e.get('key_data'))

note = """维基第141轮可用。OZ：继续为有缓存的案例补 key_data（stock-downturn-2002 / venezuelan-banking-2009），key_data 453→458。
①**网络**：仍 URLError。
②**补 5 条 key_data**（据各自专属缓存）：
`stock-downturn-2002`：道指自 2001-01-01 高点跌 27%、市值损失约 5 万亿美元；
`venezuelan-banking-2009`：2009 年 11—12 月接管 7 家银行、约占总存款 12%、至少逮捕 16 名银行家。
③check_kd 强匹配 342 → **346**；key_data 453 → **458**（案例有数据 """ + str(ncase_kd) + """/209）。
④check_docs 再次成功报出 REPORT 的 key_data 计数需更新（453→458），同步 REPORT/HEALTH。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """ 行；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 32/32。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OZ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 2, 'reviewed': 6, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 32/32',
    'spot_check': 'stock-downturn/venezuelan 补 5 条 key_data（453→458）；check_kd 强匹配 342→346',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 141 轮可用（round 161）**。**继续为有缓存的案例补 key_data（stock-downturn-2002 / venezuelan-banking-2009），key_data 453 → 458**。
- **网络**：仍 URLError。
- **补 5 条 key_data**（据各自专属缓存）：`stock-downturn-2002`（道指自 2001 高点跌 27%、市值损失约 5 万亿美元）；`venezuelan-banking-2009`（2009 年 11—12 月接管 7 家银行、约占存款 12%、至少逮捕 16 名银行家）。
- check_kd 强匹配 342 → **346**；key_data 453 → **458**（案例有数据 """ + str(ncase_kd) + """/209）。
- check_docs 再次成功报出 REPORT 的 key_data 计数需更新（453→458），同步 REPORT/HEALTH。
- 现状：**641 条**、来源 **742**、页面 **655**；key_data **458** 行；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 32/32。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | kd', kd, '| casekd', ncase_kd, '| avg', avg)
