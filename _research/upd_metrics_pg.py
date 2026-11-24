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

note = """维基第148轮可用。PG：确认出网为白名单式（补记 BLOCKERS）+ 完整质量快照。
①**网络**：进一步探测确认出网为**白名单式**——仅 github.com／baidu 等少数可达，维基/archive/google/duckduckgo 均阻断；DNS 对 8.8.8.8 的查询亦被透明污染（返回 Twitter/Facebook IP），直连 archive.org 真实 IP 亦 Reset/超时。**无本地手段取回维基全文**，3+5 条待网络解除。已补记 BLOCKERS。
②**完整质量快照（内容溯源三项）**：
check_kd：可核对 451，强匹配 **350（78%）**、弱 50、未匹配 51（多为 OWID/单位/概念）；
check_polnum：强 **443**、弱 141、**完全找不到 0**；
check_body_num：强 **984**、弱 427、未匹配 81（多为日期/举例/交叉引用）。
③未匹配/弱匹配均为已归类的"非错误"类（格式/单位/OWID/跨事件引用），此前多轮抽查已确认。
④十一道检查全绿、自测 34/34。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PG', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 0, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 34/34',
    'spot_check': '出网白名单结论补记 BLOCKERS；质量快照 kd强350/polnum强443(找不到0)/body强984',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 148 轮可用（round 168）**。**确认出网为白名单式（补记 BLOCKERS）+ 完整质量快照**。
- **网络**：进一步探测确认出网为**白名单式**——仅 github.com／baidu 等少数可达，维基/archive/google/duckduckgo 均阻断；DNS 对 8.8.8.8 的查询亦被透明污染（返回 Twitter/Facebook IP），直连 archive.org 真实 IP 亦 Reset/超时。**无本地手段取回维基全文**，3+5 条待网络解除。已补记 BLOCKERS。
- **完整质量快照（内容溯源三项）**：
  - check_kd：可核对 451，强匹配 **350（78%）**、弱 50、未匹配 51（多为 OWID/单位/概念）
  - check_polnum：强 **443**、弱 141、**完全找不到 0**
  - check_body_num：强 **984**、弱 427、未匹配 81（多为日期/举例/交叉引用）
- 未匹配/弱匹配均为已归类的「非错误」类，此前多轮抽查已确认。
- 十一道检查全绿、自测 34/34。
- 现状：**641 条**、来源 **740**、页面 **655**；**ERRORS 0、WARNINGS 0**。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
