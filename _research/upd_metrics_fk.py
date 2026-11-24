# -*- coding: utf-8 -*-
import json, glob
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
rest = [e for e in cases if not e.get('policy_response')]
pct = wp * 100 // len(cases)

note = (
    '维基第32轮可用。FJ/FK：案例政策覆盖 60%→' + str(pct) + '%（' + str(wp) + '/' + str(len(cases)) + '）。'
    '**本轮最大收获是第三次发现工具缺陷**：提取政策章节的正则漏了 recapitalization／disposition／'
    'receivership／forbearance／PBOC Reaction 等关键词，导致 savings-loan-1986、signature-bank、'
    'china-liquidity-2013 等本有明确政策的条目被误判为"无政策"。'
    '改为**输出全部章节名人工判断**后，立刻又找到6条：'
    '储贷危机（FSLIC处置成本1985年74亿+1986年91亿美元、准备金降至不足20亿、1988年资不抵债508家、FIRREA+RTC）、'
    '签名银行（2023.3.19 FDIC将部分资产负债售予NYCB、40家分行并入Flagstar、600亿贷款留接管含110亿租金管制公寓）、'
    '2013中国钱荒（央行**拒绝**注入流动性，被解读为转向"有质量增长"的政策变化）、'
    '苏联1917（1921春转向NEP、实物税替代强制征购）、'
    '1857恐慌（布坎南撤回20美元以下银行券）、'
    '1893恐慌（克利夫兰经Morgan-Belmont辛迪加向摩根与罗斯柴尔德借6500万美元黄金）。'
    '另补5条：魏玛1923（地租马克以黄金计价债券为锚、Rentenbank、1923.10.13-15法令）、'
    '土耳其2018（削支100亿美元、通胀11.9%、里拉4.0→7.0）、1929股灾（Pecora委员会→格拉斯-斯蒂格尔法）、'
    '1930恐慌（美联储学习承担最后贷款人）、1907恐慌（无央行的制度脆弱性→1913联邦储备法）。'
    '**另发现数据质量问题并记入BLOCKERS**：8个条目的来源全部是通用概念页'
    '（us-state-defaults-1840s/danish-bankruptcy-1813/dutch-collapse-1780/british-credit-1772/'
    'panic-1896/yemen-currency-divergence/panic-1910/subprime-crisis-2007），'
    '具体史实无法由"债务危机/货币危机"通用条目支撑。'
    '剩余' + str(len(rest)) + '个案例按类型：' + str(dict(Counter(e['crisis_type'] for e in rest))) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FJ-FK', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 11, 'reviewed': 77, 'fixed': 1,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '案例政策覆盖 60%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FG-FI（修正抓取逻辑后补8条，案例政策60%）',
              '- 当前轮次：续作FJ-FK（第三次工具缺陷修正，案例政策65%）')
entry = '''- **维基百科第 32 轮可用**。案例政策覆盖 **60% → 65%（134/205）**。
- **第三次发现工具缺陷**：提取政策章节的正则漏了 `recapitalization`／`disposition`／`receivership`／`forbearance`／`PBOC Reaction` 等关键词——导致 `savings-loan-1986`、`signature-bank`、`china-liquidity-2013` 等**本有明确政策**的条目被误判为"无政策"。
- 改为**输出全部章节名人工判断**，立刻又找到 6 条：

  | 案例 | 政策应对 |
  |---|---|
  | 储贷危机 1986 | FSLIC 处置成本 1985年 **74亿** + 1986年 **91亿美元**；1988年资不抵债 **508家**；**FIRREA + RTC** |
  | 签名银行 2023 | FDIC 将部分资产负债售予 NYCB、40家分行并入 Flagstar；**600亿**贷款留接管 |
  | **2013 中国钱荒** | 央行**拒绝**注入流动性——被解读为从"快速增长"转向"有质量增长"的政策变化 |
  | 苏联 1917 | 1921春转向 **NEP**，实物税替代强制征购 |
  | 1857 恐慌 | 布坎南撤回 **20 美元以下**银行券 |
  | 1893 恐慌 | 克利夫兰经 **Morgan-Belmont 辛迪加**借入 **6500 万美元**黄金 |

- 另补 5 条：魏玛 1923（地租马克以黄金计价债券为锚、**1923.10.13—15** 法令）、土耳其 2018（削支 100 亿美元）、1929 股灾（Pecora 委员会→格拉斯-斯蒂格尔法）、1930 恐慌（美联储学习承担最后贷款人）、1907 恐慌（→1913 联邦储备法）。
- **另发现数据质量问题（已记入 BLOCKERS）**：8 个条目的来源全部是**通用概念页**（`Debt_crisis`／`Currency_crisis`／`Bank_run`／`Financial_crisis`），具体史实无法由通用条目支撑——`us-state-defaults-1840s`、`danish-bankruptcy-1813`、`dutch-collapse-1780`、`british-credit-1772`、`panic-1896`、`yemen-currency-divergence`、`panic-1910`、`subprime-crisis-2007`。
- 三道检查全绿。现状：**625 条**、来源 727、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FG-FI｜2026-11-24｜状态：625条；案例政策覆盖60%**',
              '**续作FJ-FK｜2026-11-24｜状态：625条；案例政策覆盖65%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 案例政策', wp, '/', len(cases), '=', pct, '%')
