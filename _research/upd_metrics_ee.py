# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))
reln = sum(1 for e in es if e.get('related'))
kdn = sum(len(e.get('key_data', [])) for e in es)
cases = [e for e in es if not e['unit'].startswith('U6')]
pol = sum(1 for e in cases if e.get('policy_response'))

note = (
    '维基第18轮不可达。ED/EE两批共补72条概念辨析，**comparison达成100%全覆盖（' + str(cmpn) + '/' + str(len(es)) + '）**——'
    '全站每个条目（案例与概念）现在都有与其他条目的对照分析。'
    'ED重点：汇票与贴现业务的起源、银行学派vs通货学派（1844年法案在三次危机中被暂停，实践支持灵活性）、'
    '信用货币vs商品货币（弹性vs纪律）、金融加速器vs金融脆弱性（放大机制vs累积机制）、'
    '财政主导vs财政空间（货币是否被迫配合财政）、'
    '马歇尔-勒纳弹性条件、刘易斯拐点与中等收入陷阱的联动、'
    'ALM（主动管理）vs资产负债错配（风险状态）——2023年SVB并非不懂ALM，而是未对利率风险对冲。'
    'EE补最后10条：总供给vs总需求（供给冲击制造滞胀）、bailout vs bail-in（纳税人vs债权人）、'
    '国际收支（流量）vs国际投资头寸（存量）、黑市vs非正规经济（非法vs未监管）。'
    '现状：' + str(cmpn) + '/' + str(len(es)) + ' comparison、' + str(reln) + ' related、'
    + str(kdn) + ' key_data、案例政策覆盖' + str(pol) + '/' + str(len(cases)) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作ED-EE', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 72, 'reviewed': 72, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error',
    'spot_check': '**comparison 100% 全覆盖（' + str(cmpn) + '/' + str(len(es)) + '）**',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作EC（70组概念辨析，comparison 520条）',
              '- 当前轮次：续作ED-EE（comparison达成100%全覆盖）')
entry = '''- **维基百科第 18 轮不可达**。
- 续作ED–EE：两批共补 **72 条**概念辨析，`comparison` 从 87% 推到 **100% 全覆盖（592/592）**——**全站每个条目（案例与概念）现在都有与其他条目的对照分析**。
- 最后补完几组值得一提：
  - **银行学派 vs 通货学派**：1844年英国银行法（十足黄金准备）在 1847、1857、1866 年三次危机中被迫**暂停**——实践支持了银行学派的灵活性主张。这是"规则 vs 相机抉择"最早的实战检验
  - **ALM（主动管理） vs 资产负债错配（风险状态）**：2023年硅谷银行**并非不懂ALM**，而是未对利率风险做对冲——持有至到期账户规避了账面波动，却积累了实际久期风险
  - **金融加速器 vs 金融脆弱性**：前者是"**放大机制**"（净值→融资溢价→投资→净值），后者是"**累积机制**"（对冲→投机→庞氏）。两者叠加构成危机的完整动力学
  - **财政主导 vs 财政空间**：前者是货币**被迫配合**财政（丧失独立性），后者是可用的财政余地。二者的联系是：财政空间耗尽时更易滑向财政主导
  - **国际收支（流量） vs 国际投资头寸（存量）**：经常账户逆差（流量）不一定危险，但对外净负债（存量）高企会使汇率与信心更脆弱
- 当前覆盖：`comparison` **592/592**、`related` 416、`key_data` 357、案例政策 **85/205（41%）**。
- 现状：**总592条，来源695，站点606页**。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作EC｜2026-11-24｜状态：592条；comparison 520条（87%）**',
              '**续作ED-EE｜2026-11-24｜状态：592条；comparison 100% 全覆盖**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', cmpn, '/', len(es), '| related', reln, '| policy', pol, '/', len(cases))
