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

note = """维基第136轮可用。OT：做"字段交叉"检查——key_data.value 与 note 中"原文"引述数字是否相符（防转写/引述不符）。
①**方法**：对全部 key_data，解析 note 里"原文：…"的引述，提取数字（含拼写数字与 ×/÷ 单位换算），与 value 比对。
②**初筛 59 条**，经修正判据（绝对值/换算因子/拼写数字）后**降至 5 条**，逐一核对：
4 条为假阳性（`half`=50%、`size/complexity/...`=4 个要素、"nineteen"=19 拼写、Count）；
**1 条真问题**：`national-banking-act` 的"第二次法定货币法后发行额=450 百万美元"，**note 引错了句子**（引成了 1862 年法案日期句，实为 1863 年法案"expanded the limit to $450 million"）。
③**修复**：据来源把该 note 改为正确引述（450 系 1863 年法案将上限扩至 $450M，非"第二次法定货币法"本身）；并在 label 语义上标注。
④**结论**：445 条 key_data 中，value 与原文引述数量级/数值一致（除这 1 处引句错）；数据本身可靠，问题仅在"引述贴错句"。
⑤现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；key_data """ + str(kd) + """ 行；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 30/30。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OT', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 1, 'reviewed': kd, 'fixed': 1,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 30/30',
    'spot_check': 'key_data.value vs note原文 交叉核对（445 行）→ 修 national-banking-act 引句错 1 处',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 136 轮可用（round 156）**。**做「字段交叉」检查——key_data.value 与 note 中「原文」引述数字是否相符**。
- **方法**：对全部 key_data，解析 note 里「原文：…」的引述，提取数字（含拼写数字与 ×/÷ 单位换算），与 value 比对。
- **初筛 59 条**，修正判据（绝对值/换算因子/拼写数字）后**降至 5 条**，逐一核对：4 条假阳性（`half`=50%、`size/complexity/…`=4 个要素、「nineteen」=19 拼写、Count）；**1 条真问题**：
  - `national-banking-act` 的「第二次法定货币法后发行额 = 450 百万美元」，**note 引错句子**（引成 1862 年法案日期句，实为 1863 年法案「expanded the limit to $450 million」）。
- **修复**：据来源把该 note 改为正确引述。
- **结论**：445 条 key_data 中 value 与原文引述数量级/数值一致（除这 1 处引句错）；数据本身可靠，问题仅在「引述贴错句」。
- 现状：**641 条**、来源 **742**、页面 **655**；key_data **445** 行；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 30/30。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | kd', kd, '| avg', avg)
