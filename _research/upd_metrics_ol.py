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

note = """维基第129轮可用。OL：系统性"全字段搜同款"扫描 body_num 的 81→83 条未匹配，找出并修复 2 处无源数字。
①**审阅 check_body_num 未匹配 83 条**（overview/one_line/comparison 中数字在来源找不到）：绝大多数为**日期/周期区间/示例/交叉引用**的假阴性（如"6月""3—10年""从4.25%升到4.50%举例""标普500""127号文""见cypriot-2013的47.5%"）。
②**发现 2 处真·无源数字**：
（a）`blue-monday-2009` overview 免责声明仍复述"标普 500 于 3 月见底约 676 点"——该数不在本条来源（属另一事件），**违反"不复述未核实数字"**。已删该数值。
（b）`sterling-crisis-1976` overview"一度跌破1.60美元区间"——所引来源**未载该汇率数值**。已改为"具体汇率数值待核实"。
③**"全字段搜同款"当场复发**：改完 sterling 的 overview 后，check_polnum 又报 policy_response 里**同样有 1.60**（我上一轮刚在 finnish 上踩过同一坑）。已一并改 policy_response，并清理替换产生的重复表述。
④**结果**：check_polnum "完全找不到" = 0；check_body_num 未匹配 83 → **81**（真去掉 2 个无源数字）；十一道检查全绿。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 28/28。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OL', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 83, 'fixed': 3,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 28/28',
    'spot_check': 'body_num 81→83 未匹配审阅；修 blue-monday 676 / sterling 1.60（含 policy_response 同款）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 129 轮可用（round 149）**。**系统性「全字段搜同款」扫描 check_body_num 未匹配，找出并修复 2 处无源数字**。
- **审阅 check_body_num 未匹配 83 条**：绝大多数为**日期/周期区间/示例/交叉引用**的假阴性（「6月」「3—10年」「从4.25%升到4.50%举例」「标普500」「127号文」「见 cypriot-2013 的 47.5%」）。
- **发现 2 处真·无源数字**：
  - `blue-monday-2009` overview 免责声明仍复述「标普 500 于 3 月见底约 676 点」——该数不在本条来源（属另一事件），**违反「不复述未核实数字」**，已删。
  - `sterling-crisis-1976` overview「一度跌破 1.60 美元区间」——所引来源**未载该汇率数值**，已改为「具体汇率数值待核实」。
- **「全字段搜同款」当场复发**：改完 sterling 的 overview 后，`check_polnum` 又报 policy_response 里**同样有 1.60**（与上一轮 finnish 同款坑）。已一并修正。
- **结果**：check_polnum「完全找不到」= 0；check_body_num 未匹配 83 → **81**（真去掉 2 个无源数字）；十一道检查全绿。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 28/28。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | avg', avg)
