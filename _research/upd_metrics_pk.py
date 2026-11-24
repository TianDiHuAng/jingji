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

note = """维基第152轮可用。PK：为 3 条案例补 policy_response（含更正一处"无来源"错误断言）+ 抓到一次 key_data 覆盖。
①**补 policy_response（156→159）**（据各自专属缓存）：
`danatbank-1931`（德国政府 1931-07-13 银行假日 + 资本管制 + 强制与 Dresdner 合并）、
`argentina-2018`（央行加息至 60% + 2018-05-08 寻求 IMF 贷款）、
`kennedy-slide-1962`（美联储小幅利率操作缓解国债恐慌）。
②**更正错误断言**：`danatbank-1931` 原 overview 称"具体资产负债规模无可靠来源、故不列数值"，但**其专属缓存实有存款 24 亿帝国马克**——已改为据实列出，并补 key_data（存款 2.4 十亿帝国马克）。
③**抓到并修复一次 key_data 覆盖**：给 danatbank 加数据时误用 `d['key_data']=[新行]` **覆盖了原有的"联合担保资本储备=1 十亿马克"行**；靠"key_data 总数应 +1 却仍为 462"发现，已**恢复原行 + 保留新行**（现 463，两行俱在）。教训：改列表字段必先读原值、追加而非替换。
④check 0/0、check_polnum 完全找不到 0、十一道全绿、自测 35/35。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；政策案例 """ + str(pr) + """/209；overview 平均 """ + str(avg) + """ 字。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PK', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 4, 'reviewed': 25, 'fixed': 4,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 35/35',
    'spot_check': '3 条 policy（156→159）+ 更正 danatbank 无来源断言+补存款数据；抓到并恢复 key_data 覆盖',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 152 轮可用（round 172）**。**为 3 条案例补 policy_response（含更正一处「无来源」错误断言）+ 抓到一次 key_data 覆盖**。
- **补 policy_response（156 → 159）**（据各自专属缓存）：`danatbank-1931`（德国政府 1931-07-13 银行假日 + 资本管制 + 强制与 Dresdner 合并）、`argentina-2018`（央行加息至 60% + 2018-05-08 寻求 IMF 贷款）、`kennedy-slide-1962`（美联储小幅利率操作缓解国债恐慌）。
- **更正错误断言**：`danatbank-1931` 原 overview 称「具体资产负债规模无可靠来源、故不列数值」，但**其专属缓存实有存款 24 亿帝国马克**——已改为据实列出，并补 key_data（存款 2.4 十亿帝国马克）。
- **抓到并修复一次 key_data 覆盖**：加数据时误用 `d['key_data']=[新行]` **覆盖了原有「联合担保资本储备 = 1 十亿马克」行**；靠「key_data 总数应 +1 却仍为 462」发现，已**恢复原行 + 保留新行**（现 463）。教训：改列表字段必先读原值、追加而非替换。
- check 0/0、check_polnum 完全找不到 0、十一道全绿、自测 35/35。
- 现状：**641 条**、来源 **740**、页面 **655**；key_data **463**；政策案例 **159/209**；**ERRORS 0、WARNINGS 0**。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | kd', kd, '| policy', pr, '| avg', avg)
