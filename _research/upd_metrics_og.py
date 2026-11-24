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

note = """维基第126轮可用。OF-OG：完成文档系统全覆盖，修正 README/SATURATION/scope 等陈旧，并加两项守卫。
①**README.md 严重陈旧**（读者首见）：仍写"106 案例/180 来源/check.py R1–R15/PROGRESS 含 ALL_DONE/106 条目 L1-L2"——已完整重写（641 条/742 来源/13 工具/R1–R22+R4b/R12b/25→27 自测/复现命令）。
②**SATURATION.json 误报饱和（关键）**：顶部 `saturated:true / maintenance_mode:true / zero_gap_streak:3`——这是机器可读的"已完成"宣称，与"网络阻塞、仍在维护、永不写 ALL_DONE、饱和尚未达到"**直接冲突**。已重置为 false/0/false 并注明原委；历史 rounds 数组保留。
③**scope.md 陈旧**：头部"106 条"与 600 行清单不符，且**缺 48 条后期新增概念**、含 1 条重复陈旧行（glass-steagall）。已改头部计数、**补录 48 条附录**、删除重复行——现 scope 覆盖 **641/641**。
④**HEALTH_CHECK_F.md** 加"历史快照"标注（原 round 11 一次性记录）。
⑤**新增两项 check_docs 守卫**：（a）scope.md 须覆盖全部条目；（b）SATURATION.json 不得误报 saturated=true。均注入测试确认可捕获。
⑥**自测 25 → 27**（新增 scope 未覆盖、SATURATION 误报两用例）。十一道检查全绿。
⑦现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 27/27。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OF-OG', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 7, 'fixed': 4,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 27/27',
    'spot_check': 'README 重写；SATURATION 误报饱和已重置；scope 补录 48 条覆盖 641；加 2 守卫；自测 25→27',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 126 轮可用（round 146）**。**完成文档系统全覆盖，修正 README／SATURATION／scope 等陈旧，并加两项守卫**。
- **README.md 严重陈旧**（读者首见）：仍写「106 案例／180 来源／check.py R1–R15／PROGRESS 含 ALL_DONE／106 条目 L1-L2」——已完整重写（641 条／742 来源／13 工具／R1–R22+R4b/R12b／自测 27／复现命令）。
- **SATURATION.json 误报饱和（关键）**：顶部 `saturated:true / maintenance_mode:true / zero_gap_streak:3`——这是机器可读的「已完成」宣称，与「网络阻塞、仍在维护、永不写 ALL_DONE、饱和尚未达到」**直接冲突**。已重置为 false/0/false 并注明原委。
- **scope.md 陈旧**：头部「106 条」与 600 行清单不符，且**缺 48 条后期新增概念**、含 1 条重复陈旧行（`glass-steagall`）。已改计数、**补录 48 条附录**、删除重复行——现 scope 覆盖 **641/641**。
- **HEALTH_CHECK_F.md** 加「历史快照」标注（原 round 11 一次性记录）。
- **新增两项 check_docs 守卫**：（a）scope.md 须覆盖全部条目；（b）SATURATION.json 不得误报 `saturated=true`。均注入测试确认可捕获。
- **自测 25 → 27**。十一道检查全绿。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 27/27。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
