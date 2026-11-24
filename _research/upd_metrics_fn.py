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
    '维基第34、35轮可用。FN：案例政策覆盖 67%→' + str(pct) + '%（' + str(wp) + '/' + str(len(cases)) + '）。'
    '方法：输出剩余67个案例的**全部章节名**人工逐个判断（不用正则，因前三次正则均漏关键词），'
    '再读取命中章节原文后撰写4条：'
    '美林2008（未对冲CDO损失、交易对手对其偿付能力失去信心、部分银行考虑若雷曼倒闭即停止与美林交易、'
    '最终由美国银行收购——属市场化处置而非政府注资）、'
    '匈牙利1946（pengő 1927.1.1取代korona、1946.7.31被forint取代；末期发行10²⁰面额、10²¹印而未发）、'
    '乌克兰2008（央行10月对提前取款实施暂停令、12月不良率10.3%、11月工业产出-28.6%、IMF 2009.4预测萎缩8%）、'
    '三方协议1936（非正式临时协议、承诺避免竞争性贬值、法国贬值换取协议、比利时瑞士荷兰跟进）。'
    '剩余' + str(len(rest)) + '个案例按类型：' + str(dict(Counter(e['crisis_type'] for e in rest))) + '。'
    '这些案例的维基页面经全部章节人工检视后，确认不含"当局做了什么"的独立记载'
    '（多为纯市场事件、纯统计记录或理论讨论）。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作FN', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 4, 'reviewed': 67, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '案例政策覆盖 67%→' + str(pct) + '%',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作FL-FM（修复8个来源不足条目，案例政策67%）',
              '- 当前轮次：续作FN（人工扫描全部章节后补4条，案例政策69%）')
entry = '''- **维基百科第 34、35 轮可用**。案例政策覆盖 **67% → 69%（142/205）**。
- **方法改进**：因前三次正则均漏关键词，本轮改为**输出剩余 67 个案例的全部章节名，人工逐个判断**，再读取命中章节原文撰写。
- 补写 4 条：

  | 案例 | 政策／处置 |
  |---|---|
  | 美林 2008 | 未对冲 CDO 损失 + 交易对手信心崩塌；部分银行考虑**若雷曼倒闭即停止与美林交易**；最终由美国银行收购（**市场化处置，非政府注资**） |
  | 匈牙利 1946 | pengő 1927.1.1 取代 korona、**1946.7.31 被 forint 取代**；末期发行 **10²⁰** 面额，**10²¹ 印而未发** |
  | 乌克兰 2008 | 央行 10 月对提前取款实施**暂停令**；12 月不良率 **10.3%**；11 月工业产出 **-28.6%**；IMF 2009.4 预测萎缩 8% |
  | 三方协议 1936 | **非正式、临时**协议；承诺避免竞争性贬值；**法国贬值**换取协议；比利时、瑞士、荷兰跟进 |
- 剩余 63 个案例，经**全部章节人工检视**确认不含"当局做了什么"的独立记载——多为纯市场事件、纯统计记录或理论讨论。
- 三道检查全绿。现状：**625 条**、来源 732、站点 639 页。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作FL-FM｜2026-11-24｜状态：625条；8个来源不足条目已修复，案例政策67%**',
              '**续作FN｜2026-11-24｜状态：625条；案例政策69%**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 案例政策', wp, '/', len(cases), '=', pct, '%')
print('剩余按类型:', dict(Counter(e['crisis_type'] for e in rest)))
