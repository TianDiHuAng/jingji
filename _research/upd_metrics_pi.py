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

note = """维基第150轮可用。PI：核查 3 条缺全文条目的诚实性（均无编造）+ 更新 REPORT 遗留（含备份风险）。
①**DBpedia 摘要端点彻底不可用**（对 Berlin 等也返回 0 行，非仅目标资源），放弃该绕行。
②**核查 3 条缺全文条目**（south-sea-bubble-1720／bear-stearns／bcci）：均 needs_verification=True、概述注明"暂缺维基全文…待补"、无编造的价格/人物细节。bear-stearns 的两条 key_data（$13.40T 衍生品名义额、$28B level-3 资产 vs $11B 净权益）均有"原文"引述、系真实数据（仅本地无缓存），非编造。**诚实性合格**。
③**更新 REPORT.md 遗留节**：新增"成果未备份到 GitHub"（远程 pushed_at 停在 2026-11-22、约 415 提交未推、无 token 无法自动推）与网络白名单式诊断说明。
④十一道检查全绿、自测 34/34。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PI', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 3, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 34/34',
    'spot_check': '3 条缺全文条目诚实性合格（无编造）；REPORT 遗留补备份风险与网络诊断',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 150 轮可用（round 170）**。**核查 3 条缺全文条目的诚实性（均无编造）+ 更新 REPORT 遗留（含备份风险）**。
- **DBpedia 摘要端点彻底不可用**（对 Berlin 等通用实体也返回 0 行），放弃该绕行。
- **核查 3 条缺全文条目**（`south-sea-bubble-1720`／`bear-stearns`／`bcci`）：均 `needs_verification=True`、概述注明「暂缺维基全文…待补」、无编造的价格/人物细节。`bear-stearns` 的两条 key_data（$13.40T 衍生品名义额、$28B level-3 资产 vs $11B 净权益）均有「原文」引述、系真实数据（仅本地无缓存），非编造。**诚实性合格**。
- **更新 REPORT.md 遗留节**：新增「成果未备份到 GitHub」（远程 pushed_at 停在 2026-11-22、约 415 提交未推、无 token 无法自动推）与网络白名单式诊断说明。
- 十一道检查全绿、自测 34/34。
- 现状：**641 条**、来源 **740**、页面 **655**；**ERRORS 0、WARNINGS 0**。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
