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

note = """维基第132轮可用。OO：补 2 条 policy_response，并**发现并修复另 1 处无源断言（LTRO/扭转操作）**。
①**发现无源**：`stocks-fall-2011` overview 称"欧洲央行推出 LTRO、美联储启动扭转操作"，但**所引来源未载**（来源只载 ECB 买入小国债券、日本 8/4 干预汇市、瑞士央行 8/3 降息）。已删该表述，改为来源可支撑的干预；`find_val "LTRO"` 全库 0 命中。
②**补 policy_response（2 条）**：
stocks-fall-2011（ECB 买入部分小国债券、日本干预汇市、瑞士降息）、
bernie-madoff（SIPC 托管清算，估计直接损失约 180 亿美元、追回约 148 亿美元；SEC 此前多次调查未发现）。案例 policy 153 → **155**。
③check_polnum "完全找不到" = 0；check_body_num 未匹配 81（未新增）；十一道检查全绿。
④现状：""" + str(len(es)) + """ 条、来源 """ + str(len(srcs)) + """、页面 """ + str(pages) + """；案例政策 """ + str(pr) + """ 条；overview 平均 """ + str(avg) + """ 字；ERRORS 0、WARNINGS 0。十一道检查通过 + 自测 28/28。"""

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作OO', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 3, 'reviewed': 4, 'fixed': 3,
    'sources_total': len(srcs),
    'check_result': 'PASS; ERRORS 0；WARNINGS 0 + 自测 28/28',
    'spot_check': '修 stocks-fall-2011 无源 LTRO；补 stocks/bernie policy（153→155）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

add = """- **维基百科第 132 轮可用（round 152）**。**补 2 条 policy_response，并发现并修复另 1 处无源断言（LTRO/扭转操作）**。
- **发现无源**：`stocks-fall-2011` overview 称「欧洲央行推出 LTRO、美联储启动扭转操作」，但**所引来源未载**（来源只载 ECB 买入小国债券、日本 8/4 干预汇市、瑞士央行 8/3 降息）。已删该表述，改为来源可支撑的干预；`find_val "LTRO"` 全库 0 命中。
- **补 policy_response（2 条）**：
  - `stocks-fall-2011`：ECB 买入部分小国债券、日本干预汇市、瑞士降息
  - `bernie-madoff`：SIPC 托管清算，估计直接损失约 180 亿美元、追回约 148 亿美元；SEC 此前多次调查未发现
  - 案例 policy **153 → 155**
- check_polnum「完全找不到」= 0；check_body_num 未匹配 81（未新增）；十一道检查全绿。
- 现状：**641 条**、来源 **742**、页面 **655**；案例政策 **155** 条；**ERRORS 0、WARNINGS 0**。十一道检查通过 + 自测 28/28。

"""

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('\n## 轮次记录\n', '\n' + add + '## 轮次记录\n', 1)
open(p, 'w', encoding='utf-8').write(s)

print('updated | policy', pr, '| avg', avg)
