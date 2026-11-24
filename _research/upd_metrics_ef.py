# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))
reln = sum(1 for e in es if e.get('related'))
kdn = sum(len(e.get('key_data', [])) for e in es)
pct = reln * 100 // len(es)

note = (
    '维基第19轮不可达。EF为90条条目按六个主题建立关联（国际金融与汇率、货币政策、'
    '金融工具与结构、风险与监管、危机史与制度、基础概念），related覆盖 416→' + str(reln) + '条（' + str(pct) + '%）。'
    '过程中又发现19个基础概念缺失：convergence/counterparty-risk/disclosure/dividend/effective-demand/'
    'equity-premium/expectations/externalities/growth/market-failure/proprietary-trading/recession/'
    'regulatory-arbitrage/rent-seeking/subordination/taper-tantrum/term-premium/utility/special-drawing-rights，'
    '**多为经济学最基础的概念**（增长、预期、效用、衰退、市场失灵、寻租），'
    '再次印证此前判断：本站概念覆盖偏向"金融专门术语"，而基础经济学地基不完整。已记入BACKLOG。'
    '当前：comparison ' + str(cmpn) + '/' + str(len(es)) + '、related ' + str(reln) + '/' + str(len(es)) + '、key_data ' + str(kdn) + '。'
)

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作EF', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 90, 'reviewed': 90, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (' + str(len(es)) + '); check_links 606页 0 error',
    'spot_check': 'related 416→' + str(reln) + '条(' + str(pct) + '%)',
    'note': note,
})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作ED-EE（comparison达成100%全覆盖）',
              '- 当前轮次：续作EF（related覆盖达85%）')
entry = '''- **维基百科第 19 轮不可达**。
- 续作EF：**为 90 条条目按六个主题建立关联**（国际金融与汇率、货币政策、金融工具与结构、风险与监管、危机史与制度、基础概念），`related` 覆盖 **416 → 504 条（85%）**。
- **又发现 19 个基础概念缺失**：`convergence`／`counterparty-risk`／`disclosure`／`dividend`／`effective-demand`／`equity-premium`／`expectations`／`externalities`／`growth`／`market-failure`／`proprietary-trading`／`recession`／`regulatory-arbitrage`／`rent-seeking`／`subordination`／`taper-tantrum`／`term-premium`／`utility`／`special-drawing-rights`。
  - 其中 `growth`（增长）、`expectations`（预期）、`utility`（效用）、`recession`（衰退）、`market-failure`（市场失灵）、`rent-seeking`（寻租）**都是经济学最基础的概念**。
  - 这再次印证此前判断：本站概念覆盖偏向"金融专门术语"（巴塞尔III、CDO、LDI…），而**基础经济学的地基并不完整**。已记入 `BACKLOG.md`。
- 当前覆盖：`comparison` **592/592（100%）**、`related` **504/592（85%）**、`key_data` 357、案例政策 85/205（41%）。
- 现状：**总592条，来源695，站点606页**。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作ED-EE｜2026-11-24｜状态：592条；comparison 100% 全覆盖**',
              '**续作EF｜2026-11-24｜状态：592条；related 85%（comparison 100%）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | related', reln, '/', len(es), '=', pct, '%')
