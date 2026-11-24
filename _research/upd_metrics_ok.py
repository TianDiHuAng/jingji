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

note = """维基第128轮可用。OJ-OK：网络仍不可用；据本地缓存**补 3 条 case 的 policy_response**，并**修一处残留未核实数字**。
①**找候选**：筛出"有专属富缓存、缺 policy_response、缓存含政策词"的 case 24 条；逐条读缓存政策段落，选事实充分者。
②**补 3 条 policy_response**（事实均取自其已引专属来源的本地缓存，未引入外部事实）：
nixon-shock（正文补"90天/10%"精确值后提炼：工资物价冻结+10%进口附加税+取消美元兑金）、
creditanstalt（原 overview 为 stub"待核实补充"，据 w-en-creditanstalt 缓存改写并加"恩德尔救助/否决国有化/1934合并"）、
drexel（补"监管与结局"句并加"SECK/NYSE/纽联储存疑→和解→第11章破产、救助未落实"）。
案例 policy_response 覆盖 146 → **149**。
③**发现并修复残留**：check_polnum 报 `finnish-banking-1990` "20%" 完全找不到——查系 **round 131 只改了 overview 的免责声明、却漏改 policy_response 仍断言"失业率从近零升至近20%"**（来源未载）。已把 policy_response 改为"失业率大幅上升（具体峰值待核实）"。check_polnum 现"完全找不到 0"。
④**教训**：一处"未核实数字"往往在多个字段重复出现——**改一处要全字段搜同款**（overview/one_line/policy_response/…）。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；案例政策 """ + str(pr) + """ 条；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 28/28。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OJ-OK', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 4, 'reviewed': 24, 'fixed': 4,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 28/28',
    'spot_check': '补 3 条 policy_response（政策覆盖 146→149）+ 修 finnish 残留未核实 20%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 128 轮可用（round 148）**。**网络仍不可用；据本地缓存补 3 条 case 的 policy_response，并修一处残留未核实数字**。
- **补 3 条 policy_response**（事实均取自其已引专属来源的本地缓存，未引入外部事实）：
  - `nixon-shock`：正文补「90天/10%」精确值后提炼（工资物价冻结 + 10% 进口附加税 + 取消美元兑金）
  - `creditanstalt`：原 overview 为 stub「待核实补充」，据 `w-en-creditanstalt` 缓存改写并加「恩德尔救助/否决国有化/1934 合并」
  - `drexel`：补「监管与结局」句并加「SEC/NYSE/纽联储存疑→和解→第 11 章破产、救助未落实」
  - 案例 policy_response 覆盖 **146 → 149**
- **发现并修复残留**：`check_polnum` 报 `finnish-banking-1990`「20%」完全找不到——系 **round 131 只改了 overview 的免责声明、却漏改 policy_response 仍断言「失业率从近零升至近20%」**（来源未载）。已改为「失业率大幅上升（具体峰值待核实）」，check_polnum 现「完全找不到 0」。
- **教训**：一处「未核实数字」往往在多个字段重复出现——**改一处要全字段搜同款**。
- 现状：**641 条**、来源 **742**、页面 **655**；案例政策 **149** 条；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 28/28。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | policy', pr, '| avg', avg)
