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

note = """维基第133轮可用。OP：补 1 条 policy_response（british-credit-1772），并确认本地可支撑的政策候选已近穷尽。
①**补 british-credit-1772**：据 w-en-british-credit-1772 缓存补"1773 年 1 月 10 日英格兰银行出面救助、允许提取金银"到正文并加 policy_response（案例 policy 155 → **156**，占 209 的 75%）。
②**排查**：对无 policy 的 case 按"强救助措辞（bailout/rescue/recapitali/nationaliz）"扫描，**仅 brexit-crash-2016 命中 3 处**，但其缓存无明确 BoE 措施，不勉强；**其余无 policy 案例的缓存多不含明确政策应对**（专属来源未缓存或来源本身无政策段）。
③**结论**：在"仅用本地缓存、不联网"的约束下，case 的 policy_response 覆盖已接近可得上限；进一步补全需网络恢复（补抓专属来源全文）。
④check_polnum "完全找不到" = 0；十一道检查全绿。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；案例政策 """ + str(pr) + """/209；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 28/28。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OP', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 12, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 28/28',
    'spot_check': '补 british-credit-1772 policy（155→156）；确认本地政策候选近穷尽',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 133 轮可用（round 153）**。**补 1 条 policy_response（british-credit-1772），并确认本地可支撑的政策候选已近穷尽**。
- **补 `british-credit-1772`**：据 `w-en-british-credit-1772` 缓存补「1773 年 1 月 10 日英格兰银行出面救助、允许提取金银」到正文并加 policy_response（案例 policy **155 → 156**，占 209 的 **75%**）。
- **排查**：对无 policy 的 case 按「强救助措辞（bailout/rescue/recapitali/nationaliz）」扫描，**仅 `brexit-crash-2016` 命中 3 处**，但其缓存无明确 BoE 措施，不勉强；**其余无 policy 案例的缓存多不含明确政策应对**。
- **结论**：在「仅用本地缓存、不联网」约束下，case 的 policy_response 覆盖已接近可得上限；进一步补全需网络恢复。
- check_polnum「完全找不到」= 0；十一道检查全绿。
- 现状：**641 条**、来源 **742**、页面 **655**；案例政策 **156/209**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 28/28。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | policy', pr, '| avg', avg)
