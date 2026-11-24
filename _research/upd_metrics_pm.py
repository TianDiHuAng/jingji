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

note = """维基第154轮可用。PM：为 panic-1901 补 key_data（463→464）+ 更正过宽"待核实"；另观察 repo 卫生。
①**补 panic-1901**：该条原 0 条 key_data、且正文称"价格数值待核实来源未载"；但其专属缓存（Panic of 1901 页）确有"Northern Pacific saw a net advance of 16+1⁄2 points"。已补 key_data（净涨 16.5 点）并把正文改为"逼空期间净涨约 16½ 点；其余更具体价位待核实"（170/1000 仍不宣称）。key_data 463 → **464**。
②**repo 卫生观察**（未改动）：`_research` 跟踪 **1459** 文件（wiki_full 571〔check_kd 需保留〕+ continue_*.py 386 + 其他 502，共 22MB）——远多于 data 642/site 656；多为一次性构建脚本，属可选清理项（删除会丢失构建记录，故保留，仅记录）。
③check 0/0；check_body_num 未匹配 81→80；十一道全绿、自测 35/35。
④现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作PM', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': 25, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 35/35',
    'spot_check': 'panic-1901 补 key_data（16½点）+ 更正过宽待核实；key_data 463→464；观察 _research 1459 文件',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 154 轮可用（round 174）**。**为 panic-1901 补 key_data（463 → 464）+ 更正过宽「待核实」；另观察 repo 卫生**。
- **补 panic-1901**：该条原 0 条 key_data、且正文称「价格数值待核实来源未载」；但其专属缓存（Panic of 1901 页）确有「Northern Pacific saw a net advance of 16+1⁄2 points」。已补 key_data（净涨 16.5 点）并把正文改为「逼空期间净涨约 16½ 点；其余更具体价位待核实」（170/1000 仍不宣称）。key_data 463 → **464**。
- **repo 卫生观察**（未改动）：`_research` 跟踪 **1459** 文件（wiki_full 571〔check_kd 需保留〕+ continue_*.py 386 + 其他 502，共 22MB），多为一次性构建脚本，属可选清理项（删除会丢失构建记录，故保留）。
- check 0/0；check_body_num 未匹配 81→80；十一道全绿、自测 35/35。
- 现状：**641 条**、来源 **740**、页面 **655**；key_data **464**；**ERRORS 0、WARNINGS 0**。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | kd', kd, '| avg', avg)
