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
from collections import Counter
tl = dict(Counter((e['tier'], e['level']) for e in es))

note = """维基第127轮可用。OH-OI：网络仍不可用；完成两项内容核查并把层级达标固化为 R23。
①**网络复测**：en/zh wikipedia 均 URLError 超时，仍不可用——3 条缺全文 + 5 条缓存缺口无法在本轮解决。
②**key_data 弱匹配核查**：check_kd 的 44 条"弱匹配"逐条阅读——**note 均含与数值一致的原文引述**，系格式差（如 900,000 逗号、单位词未入关键词表）造成的假阴性，**内容准确、无实错**。
③**层级达标核查**：tier×level 交叉表 **完全一致**——核心 34 全 L3、重要 502 全 L2、补充 105 全 L2，**0 违规**。
④**固化为检查**：`check.py` 新增 **R23**——核心须 L3、重要须 L2/L3，否则 error。注入测试（核心改 L2）确认能捕获。
⑤**纳入自测**：新增"R23 核心未达L3"用例，自测 27 → **28 项**，全通过；同步更新 HEALTH_CHECK（R1–R23、自测 28）。
⑥现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 28/28。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OH-OI', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 0, 'reviewed': 44, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 28/28',
    'spot_check': '44 弱匹配 key_data 均假阴性；层级达标 0 违规；加 R23；自测 27→28',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 127 轮可用（round 147）**。**网络仍不可用；完成两项内容核查并把层级达标固化为 R23**。
- **网络复测**：en／zh wikipedia 均 URLError 超时，仍不可用——3 条缺全文 + 5 条缓存缺口无法在本轮解决。
- **key_data 弱匹配核查**：`check_kd` 的 44 条「弱匹配」逐条阅读——**note 均含与数值一致的原文引述**，系格式差（如 900,000 逗号、单位词未入关键词表）造成的假阴性，**内容准确、无实错**。
- **层级达标核查**：tier×level 交叉表 **完全一致**——核心 34 全 L3、重要 502 全 L2、补充 105 全 L2，**0 违规**。
- **固化为检查**：`check.py` 新增 **R23**——核心须 L3、重要须 L2/L3，否则 error。注入测试确认能捕获。
- **纳入自测**：新增「R23 核心未达L3」用例，自测 27 → **28 项**；同步更新 HEALTH_CHECK（R1–R23、自测 28）。
- 现状：**641 条**、来源 **742**、页面 **655**；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 28/28。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | tier×level', tl, '| avg', avg)
