# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cases = [e for e in es if not e['unit'].startswith('U6')]
wk = sum(1 for e in cases if e.get('key_data'))
tk = sum(len(e.get('key_data', [])) for e in es)
pct = wk * 100 // len(cases)

note = (
    '维基第37轮可用。FQ：先用修正后的来源选择逻辑抓取20个缺失案例的**专属维基页全文**，'
    '再从全文中提取"数字+单位"候选并**人工筛选**，为10个条目补充17条 key_data。'
    '案例数据覆盖 79%→' + str(pct) + '%（' + str(wk) + '/' + str(len(cases)) + '）、全站 key_data 374→' + str(tk) + '条。'
    '新增数据：1935年银行法下98.5%存款在5000美元保险限额以内；喀麦隆1987—88年度预算削减18%、IMF援助1.5亿美元；'
    '加纳Capital/UT Bank无法回收债务110亿塞地、对Capital Bank流动性支持6.2亿塞地；'
    '缅甸私营银行占储蓄比重由10%（1994）升至66%（2003）；'
    'Overend, Gurney倒闭时欠债约1100万英镑（合2025年11.32亿英镑）；1866年危机后失业率8%；'
    '罗得岛州政府为偿付储户发行6.97亿美元债券；Souk al-Manakh市值数月内从50亿升至1000亿美元、'
    '约6000名投资者的未结支票总值相当于940亿美元；'
    '英格兰银行在"救生艇行动"中损失约1亿英镑、1973年10月利率升至13%；'
    '2010年闪崩由41亿美元单笔交易触发、道指盘中跌超1000点。'
    '每条保留英文原文于 note 并标注"单一来源待核实"；value 均为数值。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FQ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 10, 'reviewed': 43, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': 'key_data 374→' + str(tk) + '条；案例数据覆盖 79%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FO-FP（补17条key_data，案例数据覆盖79%）',
              '- 当前轮次：续作FQ（再补17条key_data，案例数据覆盖83%）')
entry = '''- **维基百科第 37 轮可用**。案例数据覆盖 **79% → 83%（172/205）**，全站 `key_data` **374 → 391 条**。
- 先抓 20 个缺失案例的**专属**维基页全文，再提取数字候选并人工筛选，为 10 个条目补充 17 条数据。几条值得看：

  | 条目 | 数据 |
  |---|---|
  | 1935 年银行法 | **98.5%** 的存款在 5000 美元保险限额以内 |
  | 喀麦隆 1987 | 预算削减 **18%**；IMF 援助 **1.5 亿美元** |
  | 加纳 2017 | 两家银行无法回收债务 **110 亿塞地**；流动性支持 **6.2 亿塞地** |
  | 缅甸 2003 | 私营银行占储蓄比重 **10%（1994）→ 66%（2003）** |
  | Overend, Gurney 1866 | 欠债约 **1100 万英镑**（合 2025 年 **11.32 亿英镑**） |
  | **Souk al-Manakh 1982** | 市值数月内 **50 亿 → 1000 亿美元**；约 6000 名投资者的未结支票总值 **940 亿美元** |
  | 英国二级银行 1973 | 英央行"救生艇行动"损失 **1 亿英镑**；利率升至 **13%** |
  | 闪崩 2010 | **41 亿美元**单笔交易触发，道指盘中跌超 **1000 点** |

- 三条特别有信息量的：
  - **98.5%**：1935 年把保险限额设为 5000 美元，覆盖了绝大多数存款人——**限额设计基于分布而非拍脑袋**
  - **10% → 66%**：缅甸私营银行在 9 年内从边缘变成储蓄主体，而其不受存款保险保护——**这正是 2003 年挤兑的结构基础**
  - **940 亿美元空头支票**：Souk al-Manakh 是一次「无现金结算」的投机市场，崩盘时暴露的不是亏损而是**根本不存在的钱**
- 三道检查全绿。现状：**625 条**、来源 732、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FO-FP｜2026-11-24｜状态：625条；案例数据覆盖79%**',
              '**续作FQ｜2026-11-24｜状态：625条；案例数据覆盖83%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | key_data', tk, '| 案例数据覆盖', wk, '/', len(cases), '=', pct, '%')
