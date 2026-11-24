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

note = """维基第131轮可用。ON：继续据本地缓存补 policy_response，并用 find_val 抓到一处重复。
①**补 3 条 policy_response**（事实取自各自已引来源缓存）：
nigeria-debt（2006 年巴黎俱乐部：约 120 亿美元现金回购 + 约 180 亿美元减免，首个全额清偿巴黎俱乐部债务的非洲国家）、
angola-oil-dependence（1987 自由化、1998 改革、2000 IMF 职员监督计划 SMP、世界银行协助私有化）、
ems（ERM 波动区间/ECU/德国马克为锚/Delors 计划三阶段）。案例 policy 150 → **153**。
②**find_val 抓到重复**：追加 nigeria 政策段后发现 overview 本已含"2006 年巴黎俱乐部 120 亿回购"——`find_val "120 亿美元"` 显示两处重复。已删重复段、保留单一表述（180 亿减免仅留在 policy_response，源中有 $18bn 支撑），并把年份对齐为 2006。
③check_polnum "完全找不到" = 0；十一道检查全绿。
④现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；案例政策 """ + str(pr) + """ 条；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 28/28。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作ON', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 5, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 28/28',
    'spot_check': '补 3 条 policy_response（150→153）；find_val 抓到 nigeria 重复并去重',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 131 轮可用（round 151）**。**继续据本地缓存补 policy_response，并用 find_val 抓到一处重复**。
- **补 3 条 policy_response**（事实取自各自已引来源缓存）：
  - `nigeria-debt`：2006 年巴黎俱乐部——约 120 亿美元现金回购 + 约 180 亿美元减免，首个全额清偿巴黎俱乐部债务的非洲国家
  - `angola-oil-dependence`：1987 自由化、1998 改革、2000 IMF 职员监督计划(SMP)、世界银行协助私有化
  - `ems`：ERM 波动区间／ECU／德国马克为锚／Delors 计划三阶段
  - 案例 policy **150 → 153**
- **find_val 抓到重复**：追加 nigeria 政策段后发现 overview 本已含「2006 年巴黎俱乐部 120 亿回购」——`find_val "120 亿美元"` 显示两处重复，已删重复段、年份对齐 2006（180 亿减免仅留 policy_response，源中有 $18bn 支撑）。
- check_polnum「完全找不到」= 0；十一道检查全绿。
- 现状：**641 条**、来源 **742**、页面 **655**；案例政策 **153** 条；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 28/28。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | policy', pr, '| avg', avg)
