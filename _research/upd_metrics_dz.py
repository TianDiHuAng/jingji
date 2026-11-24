# -*- coding: utf-8 -*-
import json, glob

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
src = len(json.load(open('data/sources.json', encoding='utf-8'))['sources'])
cmpn = sum(1 for e in es if e.get('comparison'))

mm = json.load(open('METRICS.json', encoding='utf-8'))
mm['metrics'].append({
    'round': '续作DZ', 'date': '2026-11-24', 'new_entries': 0, 'upgraded': 24, 'reviewed': 24, 'fixed': 0,
    'sources_total': src,
    'check_result': 'PASS (%d); check_links 606页 0 error' % len(es),
    'spot_check': 'comparison 334→%d条(%d%%)' % (cmpn, cmpn * 100 // len(es)),
    'note': ('维基第14轮不可达。DZ再补24组概念辨析，重点：格雷欣法则的准确表述（不是"劣币驱逐良币"，'
             '而是当法定比价与实际价值不一致时，人们会贮藏或熔化良币、用劣币支付——真正起作用的是价格管制）、'
             '财政vs货币政策（工具与滞后）、GDP vs GNP（地理边界vs国民身份）、IMF vs世界银行（管失衡vs管发展）、'
             '多德-弗兰克vs格拉斯-斯蒂格尔（监管强化vs业务分离）、直升机货币vs QE（直接转移vs金融体系注入）、'
             '期货vs远期（中央清算vs对手方风险）、衰退vs萧条（无严格量化界线）、'
             '流动性风险vs偿付能力（危机处置的分水岭）、利率互换vs货币互换（同币种vs跨币种）。'
             'comparison覆盖%d条。') % cmpn})
json.dump(mm, open('METRICS.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

p = 'PROGRESS.md'
s = open(p, encoding='utf-8').read()
s = s.replace('- 当前轮次：续作DY（32组概念辨析，comparison 334条）',
              '- 当前轮次：续作DZ（24组概念辨析，comparison 358条）')
entry = '''- **维基百科第 14 轮不可达**。
- 续作DZ：再为 24 组概念写对照辨析，`comparison` 覆盖 **334 → 358 条（60%）**。其中几组值得单独记：
  - **格雷欣法则的准确表述**：不是"劣币驱逐良币"，而是"当**法定比价与实际价值不一致**时，人们把价值高的货币贮藏或熔化、用价值低的支付"——真正起作用的是**价格管制**，而非劣币本身有力量
  - **流动性风险 vs 偿付能力风险**：危机处置的**分水岭**——前者用最后贷款人（抵押融资），后者用资本重组/处置；现实中二者难以分辨，正是白芝浩原则在执行上的困难
  - **多德-弗兰克 vs 格拉斯-斯蒂格尔**：监管强化（复杂、依赖执行）vs 业务分离（简单、刚性）；转变原因是现代金融已高度混业，"切分"难以执行
  - **直升机货币 vs QE**：直接向公众/财政转移 vs 通过金融体系注入流动性；2020年现金发放与 MMT 讨论使这条界线再次模糊
  - **衰退 vs 萧条**：没有严格量化界线——"两季负增长"只是通俗标准，NBER 用多指标事后判定
- 现状：**总592条，来源695，站点606页**。QA全清。
'''
s = s.replace('## 轮次记录', entry + '\n## 轮次记录')
open(p, 'w', encoding='utf-8').write(s)

r = 'REPORT.md'
t = open(r, encoding='utf-8').read()
t = t.replace('**续作DY｜2026-11-24｜状态：592条；comparison 334条（56%）**',
              '**续作DZ｜2026-11-24｜状态：592条；comparison 358条（60%）**')
open(r, 'w', encoding='utf-8').write(t)
print('updated | comparison', cmpn, '/', len(es))
