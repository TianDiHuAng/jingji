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

note = """维基第143轮可用。PB：随机抽 4 条有缓存案例做整体内容核对（全部准确），并为 oil-price-war-2020 补 2 条 key_data。
①**网络**：仍 URLError。
②**随机抽查 4 条**（recession-1937-1938／spain-2008／oil-price-war-2020／sherman-silver-purchase）：概述关键数字逐一与缓存核对——**全部准确**（"30 percent""8 March" 等只是我的 grep 格式差异：日为"8 March"、数为"30 percent"）。4 条均已有较完善 key_data。
③**为 oil-price-war-2020 补 2 条 key_data**（据 w-en-oil-price-war-2020 缓存）：战前油价自 2020 年初因需求下降跌 **30%**；布伦特原油 2020-03-09 单日跌 **30%**（海湾战争以来最大）。key_data 460 → **462**；check_kd 强匹配 348 → **350**。
④check_docs 报出 key_data 460→462 需同步，已更新 REPORT/HEALTH。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """ 行；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 32/32。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PB', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 4, 'fixed': 0,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 32/32',
    'spot_check': '随机 4 条整体核对全准确；oil-price-war 补 2 条 key_data（460→462）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 143 轮可用（round 163）**。**随机抽 4 条有缓存案例做整体内容核对（全部准确），并为 oil-price-war-2020 补 2 条 key_data**。
- **网络**：仍 URLError。
- **随机抽查 4 条**（recession-1937-1938／spain-2008／oil-price-war-2020／sherman-silver-purchase）：概述关键数字逐一与缓存核对——**全部准确**（「30 percent」「8 March」等只是我的 grep 格式差异）。4 条均已有较完善 key_data。
- **为 oil-price-war-2020 补 2 条 key_data**（据 `w-en-oil-price-war-2020` 缓存）：战前油价自 2020 年初因需求下降跌 **30%**；布伦特原油 2020-03-09 单日跌 **30%**（海湾战争以来最大）。key_data 460 → **462**；check_kd 强匹配 348 → **350**。
- check_docs 报出 key_data 460→462 需同步，已更新 REPORT/HEALTH。
- 现状：**641 条**、来源 **742**、页面 **655**；key_data **462** 行；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 32/32。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | kd', kd, '| avg', avg)
