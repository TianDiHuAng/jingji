# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))
pct = cmpn * 100 // len(es)

note = (
    '维基第16轮不可达。EB再补58组概念辨析，覆盖达 ' + str(pct) + '%。重点：'
    '流动性的三种含义（市场/融资/货币，混用会严重误判——2008年正是三者相互强化）、'
    '自我实现预期 vs 基本面驱动（决定用可信承诺还是资本重组）、'
    '货币供给 vs 基础货币（央行可扩基础货币但无法决定广义货币）、'
    '传导机制五渠道（2008年后基础货币暴增而信贷不增＝信贷渠道堵塞）、'
    '货币数量论 vs 费雪恒等式（长期成立短期失效，V会骤降）、'
    '风险加权资产 vs 总资产（可降低RWA而非增加资本，故需杠杆率双轨）、'
    '按市值 vs 历史成本（2023年SVB即"按市价已资不抵债、按摊余成本仍健康"）、'
    'NAIRU的滞后效应（短期失业可转为结构性）、'
    '做市商 vs 套利者（做市商有报价义务，其资产负债表容量决定流动性）、'
    '一级 vs 二级市场（二级流动性决定一级发行成本）。'
    '另发现3个概念不存在（mutual-fund/nasdaq/national-debt）。'
    'comparison覆盖 ' + str(cmpn) + ' 条。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EB', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 58, 'reviewed': 58, 'fixed': 1,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error',
    'spot_check': 'comparison 392→' + str(cmpn) + '条(' + str(pct) + '%)',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EA（34组概念辨析，comparison 392条）',
              '- 当前轮次：续作EB（58组概念辨析，comparison 450条）')
entry = '''- **维基百科第 16 轮不可达**。
- 续作EB：**一次补 58 组概念辨析**，`comparison` 覆盖 **392 → 450 条（76%）**。几组关键的"混用会造成误判"的区分：
  - **"流动性"的三种含义**：市场流动性（能否以合理价格成交）／融资流动性（能否借到钱）／货币流动性（货币供给松紧）。**混用会严重误判**——2008年正是三者相互强化
  - **自我实现的预期 vs 基本面驱动**：前者可信承诺（存款保险）即可低成本化解，后者须资本重组；误判会药不对症
  - **风险加权资产 vs 总资产**：银行可降低 RWA 而非增加资本来改善资本充足率——这正是巴塞尔III同时引入杠杆率的原因
  - **按市值 vs 历史成本**：2023年硅谷银行"按市价已资不抵债、按摊余成本仍显示健康"——后者在挤兑面前一触即溃
  - **做市商 vs 套利者**：做市商有**持续报价义务**，其资产负债表容量决定危机中的流动性
  - **一级 vs 二级市场**：二级市场流动性决定一级市场发行成本
  - **NAIRU 的滞后效应**：短期失业可转为结构性失业——"衰退的伤痕"最持久来源
- 另发现 3 个概念不存在（`mutual-fund`／`nasdaq`／`national-debt`），已记录待补。
- 现状：**总592条，来源695，站点606页**。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EA｜2026-11-24｜状态：592条；comparison 392条（66%）**',
              '**续作EB｜2026-11-24｜状态：592条；comparison 450条（76%）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', cmpn, '/', len(es), '=', pct, '%')
