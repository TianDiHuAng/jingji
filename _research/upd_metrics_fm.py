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
    '维基第33轮可用。FL/FM：案例政策覆盖 65%→' + str(pct) + '%（' + str(wp) + '/' + str(len(cases)) + '）。'
    '**①修复round 50记录的8个来源不足条目**：为它们找到并补充专属史实来源——'
    'Danish_state_bankruptcy_of_1813（专属条目）、British_credit_crisis_of_1772–1773（专属）、'
    'Panic_of_1896（专属）、Shanghai_rubber_stock_market_crisis（专属）、'
    'Subprime_mortgage_crisis（专属）、Panic_of_1837、Fourth_Anglo-Dutch_War、'
    'Dutch_East_India_Company、Economy_of_Yemen、Yemeni_civil_war_(2014–present)；'
    '新增5个来源（727→732）、10条条目-来源关联。至此这8条不再仅依赖"债务危机/货币危机"通用页。'
    '**②重抓4个仍用通用页的条目**（british-credit-1772/danish-bankruptcy-1813/'
    'us-state-defaults-1840s/dutch-collapse-1780），重新提取政策章节。'
    '**③再补4条政策应对**：丹麦1813（1813.1.5宣布破产并设Rigsbank，两大目标为稳定经济与建立统一货币体系，'
    '1818年设私营Nationalbank向企业提供信贷、恢复白银为核心货币）、'
    '津巴布韦（重定值至高达百万亿面额，最终方案是采用外币为官方货币——关键不在选哪种币而在统一到单一货币，美元最有可信度）、'
    '安然（2001.10.16宣布重述1997—2000财报：利润减6.13亿美元占23%、负债增6.28亿，SEC调查促成萨班斯法）、'
    '华盛顿互惠（接管后分行售予摩根大通，2009年内全部改冠名Chase或关闭）。'
    '剩余' + str(len(rest)) + '个案例按类型：' + str(dict(Counter(e['crisis_type'] for e in rest))) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FL-FM', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 12, 'reviewed': 71, 'fixed': 8,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '修复8个来源不足条目；案例政策覆盖 65%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FJ-FK（第三次工具缺陷修正，案例政策65%）',
              '- 当前轮次：续作FL-FM（修复8个来源不足条目，案例政策67%）')
entry = '''- **维基百科第 33 轮可用**。案例政策覆盖 **65% → 67%（138/205）**。
- **修复 round 50 记录的 8 个来源不足条目**——为它们找到专属史实来源：

  | 条目 | 新增专属来源 |
  |---|---|
  | `danish-bankruptcy-1813` | Danish_state_bankruptcy_of_1813（**专属条目**） |
  | `british-credit-1772` | British_credit_crisis_of_1772–1773（**专属**） |
  | `panic-1896` | Panic_of_1896（**专属**） |
  | `panic-1910` | Shanghai_rubber_stock_market_crisis（**专属**） |
  | `subprime-crisis-2007` | Subprime_mortgage_crisis（**专属**） |
  | `us-state-defaults-1840s` | Panic_of_1837 |
  | `dutch-collapse-1780` | Fourth_Anglo-Dutch_War / Dutch_East_India_Company |
  | `yemen-currency-divergence` | Economy_of_Yemen / Yemeni_civil_war(2014–) |

  新增 **5 个来源**（727→732）、**10 条**关联。这 8 条不再仅依赖"债务危机／货币危机"通用页。
- 重抓 4 个仍用通用页的条目后，**再补 4 条政策应对**：
  - **丹麦 1813**：1813.1.5 宣布破产并设 **Rigsbank**，两大目标为**稳定经济**与**建立统一货币体系**；1818 年设**私营 Nationalbank** 向企业提供信贷、**恢复白银**为核心货币
  - **津巴布韦**：重定值至高达**百万亿**面额；最终方案是**采用外币为官方货币**——关键不在选哪种币，而在**统一到单一货币**，美元最有可信度
  - **安然**：2001.10.16 宣布重述 1997—2000 财报，利润减 **6.13 亿美元（占 23%）**、负债增 6.28 亿；SEC 调查促成萨班斯法
  - **华盛顿互惠**：接管后分行售予摩根大通，2009 年内全部改冠名 Chase 或关闭
- 三道检查全绿。现状：**625 条**、来源 **732**、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FJ-FK｜2026-11-24｜状态：625条；案例政策覆盖65%**',
              '**续作FL-FM｜2026-11-24｜状态：625条；8个来源不足条目已修复，案例政策67%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 案例政策', wp, '/', len(cases), '=', pct, '% | 来源', src)
