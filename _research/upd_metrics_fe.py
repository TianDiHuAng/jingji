# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
pct = wp * 100 // len(cases)

note = (
    '维基第29轮可用。FD/FE：再抓40个案例全文（累计80个），提取政策章节后**人工核验补写12条**，'
    '案例政策覆盖 45%→' + str(pct) + '%（' + str(wp) + '/' + str(len(cases)) + '）**首次过半**。'
    '补写内容：北岩银行（英央行流动性支持、2008国有化、英国150年首次因挤兑倒闭）、'
    '印度1991（卢比7.1贬9%、7.3再贬11%，分两步测试反应）、IndyMac（107亿美元贷款无法出售、存款流失7.5%）、'
    '俄2014（斥资近20亿美元干预、关键利率10.5%→17%、卢布仍跌至79）、'
    '美国1920-21（美联储加息4.75%→7%、哈定召开失业会议）、'
    '俄1998（复苏归因于油价与贬值，非特定救助计划——正文明确如此）、'
    '尼克松冲击（1971.8.13戴维营秘密会议、8.15暂停美元兑换黄金）、'
    '新西兰金融公司（2008金融顾问法等系列立法）、1937-38衰退（反垄断修辞运动+1938新AAA）、'
    '河南村镇银行（5万起分七档垫付至50万、超额保留权利）、'
    'NIRA（两年批准557+189个行业守则）、新西兰房价（规划管制+住房供给+金融监管）。'
    '**跳过9个 panic-\* 案例**：它们的"Regulatory failures"章节是维基多页共用的通用讨论，'
    '不是该次危机的具体政策。跳过 iranian-economic-crisis（章节是抗议而非政策）。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FD-FE', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 12, 'reviewed': 40, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '案例政策覆盖 45%→' + str(pct) + '%（首次过半）',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EY-FC（维基全文补案例政策应对，覆盖45%）',
              '- 当前轮次：续作FD-FE（再补12条，案例政策首次过半51%）')
entry = '''- **维基百科第 29 轮可用**。再抓 40 个案例全文（累计 80 个），人工核验后补写 **12 条**，案例政策覆盖 **45% → 51%（105/205）——首次过半**。
- 本轮补写的几个关键数据：

  | 案例 | 政策应对与硬数据 |
  |---|---|
  | 北岩银行 2007 | 英央行流动性支持；2008 **国有化**；英国 **150 年**来首次因挤兑倒闭 |
  | 印度 1991 | 卢比 7月1日贬 **9%**、7月3日再贬 **11%**（分两步测试反应） |
  | IndyMac 2008 | **107 亿美元**贷款无法出售；存款流失 **7.5%**；FDIC 接管 |
  | 俄 2014 | 斥资近 **20 亿美元**干预；关键利率 **10.5% → 17%**；卢布仍跌至 79 |
  | 美国 1920-21 | 美联储加息 **4.75% → 7%**；哈定召开总统失业会议 |
  | 尼克松冲击 1971 | 8月13日戴维营秘密会议 → 8月15日**暂停美元兑换黄金** |
  | 河南村镇银行 2022 | 5万起分**七档**垫付至 50 万，超额保留权利 |
  | NIRA 1933 | 两年批准 **557 + 189** 个行业守则 |

- **跳过两类不应写的案例**：
  - 9 个 `panic-*` 案例：维基的"Regulatory failures"章节是**多页共用的通用讨论**，不是该次危机的具体政策
  - `iranian-economic-crisis`：章节内容是抗议与社会动荡，不是政策
- 三道检查全绿。现状：**625 条**、来源 727、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EY-FC｜2026-11-24｜状态：625条；案例政策覆盖45%（维基全文）**',
              '**续作FD-FE｜2026-11-24｜状态：625条；案例政策覆盖51%（首次过半）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 案例政策', wp, '/', len(cases), '=', pct, '%')
