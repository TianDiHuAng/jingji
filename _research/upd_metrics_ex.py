# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))
reln = sum(1 for e in es if e.get('related'))
cases = [e for e in es if not e['unit'].startswith('U6')]
concepts = [e for e in es if e['unit'].startswith('U6')]

note = (
    '维基第27轮可用。EW/EX第二批补建15个条目：有毒资产、垃圾债、支付系统、囚徒困境、产权、'
    '交易成本、储蓄、投资、需求、人口、不平等、劳动市场、专业化、税负归宿、股票回购。'
    '抓取22个中7个因维基无独立条目（重定向到宽泛条目：disclosure→corporate law、'
    'term-premium→risk premium、bank-resolution→bank run、leverage-ratio→Basel III、'
    'taper-tantrum→QE、inflation-tax→seigniorage、regulatory-arbitrage→arbitrage）**未强建**。'
    '辨析重点：投资需区分宏观资本形成/金融投资/FDI三种含义（混用是常见错误）、'
    '储蓄vs投资的主体不同（凯恩斯"节约悖论"的基础）、'
    '需求vs需求量（曲线与点，政策含义不同）、'
    '不平等vs贫困（相对vs绝对）、税负归宿vs法定纳税人（弹性小者承担更多）、'
    '股票回购vs股息（危机前大量回购导致受援期被限制）。'
    '总条目610→' + str(len(es)) + '（案例' + str(len(cases)) + '/概念' + str(len(concepts)) + '）、'
    '来源712→' + str(src) + '、站点624→639页。comparison与related均' + str(cmpn) + '/' + str(len(es)) + '=100%。三道检查全绿。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EW-EX', 'date': '2026-11-24', 'new_entries': 15, 'upgraded': 15, 'reviewed': 22, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); 三道检查全绿',
    'spot_check': '总条目 610→' + str(len(es)) + '；双 100% 维持',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作ES-EV（**维基恢复**，首批补建18个基础概念）',
              '- 当前轮次：续作EW-EX（第二批补建15个基础概念）')
entry = '''- **维基百科第 27 轮可用**。续作EW–EX：**第二批补建 15 个条目**，总条目 **610 → 625**。
- 抓取 22 个，其中 **7 个因维基无独立条目未强建**（重定向到宽泛条目：`disclosure`→corporate law、`term-premium`→risk premium、`bank-resolution`→bank run、`leverage-ratio`→Basel III、`taper-tantrum`→QE、`inflation-tax`→seigniorage、`regulatory-arbitrage`→arbitrage）。
- 新建 15 个：**有毒资产、垃圾债、支付系统、囚徒困境、产权、交易成本、储蓄、投资、需求、人口、不平等、劳动市场、专业化、税负归宿、股票回购**。
- 几组重要辨析：
  - **投资**需区分三种含义：宏观资本形成／金融投资（只是所有权转移）／FDI（含控制权）。**股市上涨不等于"投资增加"**
  - **储蓄 vs 投资**：会计上必然相等，但决策主体不同（家庭 vs 企业）——这是凯恩斯"节约悖论"的基础
  - **需求 vs 需求量**：曲线与点，"抑制需求"与"减少需求量"是不同的事
  - **不平等 vs 贫困**：相对分布 vs 绝对水平，可以反向变动
  - **税负归宿 vs 法定纳税人**：弹性小的一方承担更多；对银行征税可能转嫁给客户或股东
  - **期货困境 vs 协调博弈**：唯一劣均衡（需改激励）vs 多均衡（只需改预期）
- 当前：**625 条**（案例 205 / 概念 420）、来源 **727**、站点 **639 页**；comparison 与 related 双 **100%**。三道检查全绿。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作ES-EV｜2026-11-24｜状态：维基恢复，610条（+18 基础概念）**',
              '**续作EW-EX｜2026-11-24｜状态：625条（+15 基础概念）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | 条目', len(es), '| 概念', len(concepts), '| 案例', len(cases), '| 来源', src)
