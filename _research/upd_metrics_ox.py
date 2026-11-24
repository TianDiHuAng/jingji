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
ncases_kd = sum(1 for e in es if not e['unit'].startswith('U6') and e.get('key_data'))

note = """维基第139轮可用。OX：为 1 条重要案例补 5 条 key_data，并发现并修复 check_docs 的 key_data 计数盲区。
①**审计无 key_data 的 26 条案例**：多数为补充/无量化或缓存缺失（核心 `south-sea-bubble-1720` 亦无 key_data 且无缓存，受网络所限）。
②**为 `edict-maximum-prices`（重要，罗马价格敕令301）补 5 条 key_data**（据 w-en-edict-maximum-prices 缓存原文）：argenteus=100第纳里、nummus=25、radiate=4、aureus≥1200、紫染丝一磅限价150000第纳里。key_data 总 445 → **450**。
③**踩坑即修**：新增 key_data 时先报 R9（缺 year/comparable_price），已补 year=301、comparable_price=False。
④**发现 check_docs 盲区**：REPORT 的 "key_data 445 条" **未加反引号**，不匹配 check_docs 的 `` `key_data` `` 判据 → 陈旧不被发现。已把 REPORT 改为 "`key_data` 450 条"（带反引号），使 key_data 计数纳入核对；同步 HEALTH。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """ 行（案例有数据 """ + str(ncases_kd) + """/209）；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 32/32。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OX', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 26, 'fixed': 2,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 32/32',
    'spot_check': 'edict-maximum-prices 补 5 条 key_data（445→450）；修 check_docs 的 key_data 计数盲区',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 139 轮可用（round 159）**。**为 1 条重要案例补 5 条 key_data，并修复 check_docs 的 key_data 计数盲区**。
- **审计无 key_data 的 26 条案例**：多数为补充/无量化或缓存缺失（核心 `south-sea-bubble-1720` 亦无 key_data 且无缓存，受网络所限）。
- **为 `edict-maximum-prices`（重要，罗马价格敕令 301）补 5 条 key_data**（据 `w-en-edict-maximum-prices` 缓存原文）：argenteus=100 第纳里、nummus=25、radiate=4、aureus≥1200、紫染丝一磅限价 150000 第纳里。key_data 总 445 → **450**。
- **踩坑即修**：新增 key_data 先报 R9（缺 year/comparable_price），已补 year=301、comparable_price=False。
- **发现 check_docs 盲区**：REPORT 的「key_data 445 条」**未加反引号**，不匹配 check_docs 的 `` `key_data` `` 判据 → 陈旧不被发现。已把 REPORT 改为「`key_data` 450 条」（带反引号），使 key_data 计数纳入核对。
- 现状：**641 条**、来源 **742**、页面 **655**；key_data **450** 行；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 32/32。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | kd', kd, '| avg', avg)
