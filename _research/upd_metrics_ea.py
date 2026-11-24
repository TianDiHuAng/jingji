# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EA', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 34, 'reviewed': 34, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (%d); check_links 606页 0 error' % len(es),
    'spot_check': 'comparison 358→%d条(%d%%)' % (cmpn, cmpn * 100 // len(es)),
    'note': ('维基第15轮不可达。EA再补34组概念辨析，重点：货币主义vs凯恩斯主义（规则vs相机抉择、滞胀的冲击）、'
             'NAIRU vs自然失业率（操作定义vs理论概念，把它当常数会误判）、'
             '菲利普斯曲线vs自然率假说（短期替代成立、长期预期调整后只留更高通胀）、'
             '庞氏vs金字塔（中心化vs层级化）、后凯恩斯vs新凯恩斯（主流内外之别）、'
             '贫困陷阱vs中等收入陷阱（收入水平与机制不同、处方不同）、'
             '委托-代理vs道德风险（结构vs后果）、微观审慎vs宏观审慎（单家机构vs体系整体）、'
             '回购vs同业拆借（有担保vs无担保，2008年回购市场挤兑）、'
             '李嘉图等价vs财政乘数（债务预期影响当期行为、高债务国乘数更小）、'
             '储蓄过剩vs全球失衡（解释与被解释、与"美元特权"解释竞争）、'
             '萨伊定律vs凯恩斯（供给创造需求vs流动性偏好）、'
             'VaR vs压力测试（常态尾部vs极端情景，2008年VaR系统性低估）、'
             '收益率曲线vs YCC（市场现象vs政策操作）。comparison覆盖%d条。') % cmpn})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作DZ（24组概念辨析，comparison 358条）',
              '- 当前轮次：续作EA（34组概念辨析，comparison 392条）')
entry = '''- **维基百科第 15 轮不可达**。
- 续作EA：再为 34 组概念写对照辨析，`comparison` 覆盖 **358 → 392 条（66%）**。重点：
  - **货币主义 vs 凯恩斯主义**：规则 vs 相机抉择；1970年代滞胀打击前者共识、2008年后零利率又让财政政策回归——这一往复说明争论未决
  - **NAIRU vs 自然失业率**：操作定义 vs 理论概念；**把它当固定常数会误判**（1970s与2010s都犯过）
  - **菲利普斯曲线 vs 自然率假说**：替代关系只在短期成立；长期预期调整后只留下更高通胀——这正是滞胀的机制
  - **微观审慎 vs 宏观审慎**：单家机构稳健 vs 体系整体稳健；2008年证明"每家都合规"仍可能集体崩塌
  - **回购 vs 同业拆借**：有担保 vs 无担保；2008年回购市场因抵押品价值不明而"挤兑"
  - **储蓄过剩 vs 全球失衡**：解释与被解释；与"美元特权"解释**相互竞争**，政策含义相反
  - **VaR vs 压力测试**：常态尾部 vs 极端情景；2008年 VaR 系统性低估（相关性上升、流动性消失）
  - **收益率曲线 vs YCC**：市场现象（倒挂预示衰退） vs 政策操作（钉住特定期限收益率）
- 现状：**总592条，来源695，站点606页**。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作DZ｜2026-11-24｜状态：592条；comparison 358条（60%）**',
              '**续作EA｜2026-11-24｜状态：592条；comparison 392条（66%）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', cmpn, '/', len(es))
