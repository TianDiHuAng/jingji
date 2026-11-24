# -*- coding: utf-8 -*-
"""续作IB：新建 capital-adequacy（资本充足率）与 liquidity-coverage-ratio（流动性覆盖率）。"""
import glob
import json

NEW = {
 'capital-adequacy': {
   'title': '资本充足率',
   'tier': '重要',
   'one_line': '银行自有资本相对风险加权资产的比率要求，是审慎监管的核心工具。',
   'overview': (
     '资本充足率要求指银行必须持有的**自有资本**相对于**风险加权资产**的最低比率，'
     '是当代银行审慎监管框架的核心。其功能是让**股东而非存款人或纳税人**承担损失的第一道缓冲：'
     '资本越厚，银行吸收亏损而不至倒闭的能力越强。'
     '监管资本按质量分层：**一级资本(Tier 1)** 以普通股与留存收益为主（能在持续经营中吸收损失），'
     '**二级资本(Tier 2)** 包括次级债等（主要在清算时吸收损失）。'
     '**巴塞尔协议**体系将此国际标准化：Basel I（1988）确立 8% 的最低资本要求，'
     'Basel II（2004）引入内部评级与三大支柱，'
     'Basel III（2010 年后）大幅提高核心一级资本要求并新增杠杆率与流动性指标。'
     '**根本局限**在于风险权重由模型或规则确定：'
     '若权重低估真实风险（如次贷危机前对按揭证券的权重），资本充足率可以**看起来达标而实际脆弱**。'),
   'timeline': [
     {'year': 1988, 'event': '巴塞尔委员会发布 Basel I，确立 8% 的最低资本充足率（据 Wikipedia Capital requirement）'},
     {'year': 2004, 'event': 'Basel II 引入内部评级法与三大支柱框架（据 Wikipedia Capital requirement）'},
     {'year': 2010, 'event': 'Basel III 大幅提高核心一级资本要求并新增杠杆率与流动性指标（据 Wikipedia Capital requirement）'},
   ],
   'schools': [
     {'holder': '缓冲视角',
      'view': '资本是吸收损失的缓冲，要求越严则银行越能承受冲击；'
              '危机后各国普遍提高核心一级资本要求即基于此（据 Wikipedia Capital requirement）',
      'sources': ['w-en-capital-adequacy']},
     {'holder': '成本与规避视角',
      'view': '更高的资本要求抬高融资成本、可能抑制信贷；'
              '且银行会通过**调整风险权重模型**或把资产移出表外来规避，'
              '使名义充足率改善而实际风险未减（据 Wikipedia Capital requirement）',
      'sources': ['w-en-capital-adequacy']},
   ],
   'key_data': [
     ('Basel I 确立的最低资本充足率', 8, '%（资本/风险加权资产）', 1988,
      '原文：the 8% minimum capital requirement established under Basel I'),
   ],
   'comparison': (
     '与**杠杆率**的区别：资本充足率的分母是**风险加权**资产（可被模型调低），'
     '杠杆率的分母是**未加权**的总暴露（无法通过权重规避）——'
     '后者正是为了约束前者的计量操纵而引入。'
     '与**流动性比率**的区别：资本是"能吸收多少损失"，流动性是"能撑多久的现金流出"，'
     '两者不可互相替代——危机中常见"资本充足但流动性枯竭"的银行。'),
   'related': ['basel-accords', 'basel-iii', 'leverage-ratio', 'liquidity-coverage-ratio',
               'macroprudential', 'bank-regulation'],
   'src': 'w-en-capital-adequacy',
 },
 'liquidity-coverage-ratio': {
   'title': '流动性覆盖率(LCR)',
   'tier': '重要',
   'one_line': '要求银行持有足够高质量流动资产，覆盖压力情景下30天净现金流出的监管指标。',
   'overview': (
     '流动性覆盖率(LCR) 是 **Basel III** 引入的流动性监管指标，'
     '要求银行持有足够的**高质量流动资产(HQLA)**，以覆盖**压力情景下 30 天的净现金流出**。'
     '其结构是一个简单比值：分子为 HQLA 的价值，分母为压力情景下的净现金流出总额。'
     '引入这一指标的直接理由是：2008 年危机中**一些资本充足的银行仍因流动性管理不善而陷入困境**——'
     '资本指标衡量的是"能吸收多少损失"，而流动性衡量的是"能撑多久"。'
     'Basel III 同时引入的另一个流动性指标是**净稳定资金比率(NSFR)**，关注一年期的结构性资金匹配；'
     'LCR 关注短期的压力承受力，两者一短一长。'
     '**局限**在于"高质量"与"压力情景"的定义由监管设定：'
     '若被认定为 HQLA 的资产在真实压力下同样难以变现（如某些主权债），该指标会高估韧性。'),
   'timeline': [
     {'year': 2010, 'event': 'Basel III 框架发布，首次引入 LCR 与 NSFR 两项流动性要求（据 Wikipedia Basel III）'},
     {'year': 2013, 'event': 'LCR 按原定时间表开始分阶段实施（据 Wikipedia Basel III）'},
   ],
   'schools': [
     {'holder': '流动性独立于资本',
      'view': '资本充足不能保证流动性安全——危机中多家资本达标的银行因短期融资断档而倒闭，'
              '故需单独设立流动性指标（据 Wikipedia Basel III）',
      'sources': ['w-en-liquidity-coverage-ratio']},
     {'holder': '资产可替代性质疑',
      'view': 'HQLA 的界定依赖"压力下仍可变现"的假设；'
              '若被认定的高流动性资产在系统性压力中同时失去流动性，指标会低估真实风险'
              '（据 Wikipedia Basel III 相关讨论；具体批评出处待核实）',
      'sources': ['w-en-liquidity-coverage-ratio']},
   ],
   'key_data': [
     ('LCR 覆盖的压力情景期限', 30, '天', 2010,
      '原文：to cover its total net cash outflows over 30 days under a stressed scenario'),
   ],
   'comparison': (
     '与**资本充足率**的区别：前者管"损失吸收能力"，后者管"短期现金流韧性"；'
     '一家银行可以资本充足而 LCR 不达标（资产长期、负债短期）。'
     '与**净稳定资金比率(NSFR)** 的区别：LCR 看 30 天的压力，NSFR 看一年期的结构性匹配。'
     '与**存款准备金**的区别：准备金要求针对存款负债设固定比率，LCR 针对**压力情景下的净流出**，'
     '是风险敏感的。'),
   'related': ['basel-iii', 'basel-accords', 'capital-adequacy', 'leverage-ratio',
               'bank-run', 'lender-of-last-resort'],
   'src': 'w-en-liquidity-coverage-ratio',
 },
}

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
ids = {e['id'] for e in es}
titles = {e['title'] for e in es}
for eid in list(NEW):
    if eid in ids or NEW[eid]['title'] in titles:
        print('跳过（已存在）:', eid)
        NEW.pop(eid)

META = {
 'w-en-capital-adequacy': ('Capital requirement', 'https://en.wikipedia.org/wiki/Capital_requirement'),
 'w-en-liquidity-coverage-ratio': ('Basel III', 'https://en.wikipedia.org/wiki/Basel_III'),
}
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
have = {s['id'] for s in sj['sources']}
for sid, (t, u) in META.items():
    if sid not in have:
        sj['sources'].append({'id': sid, 'title': t, 'author': 'Wikipedia contributors', 'year': '2026',
                              'type': '权威百科', 'url': u, 'url2': None, 'verified': True,
                              'link_ok': True, 'note': 'Wikipedia API 核对（本会话抓取全文）'})
        print('注册来源:', sid)
sj['count'] = len(sj['sources'])
json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

n = 0
for eid, v in NEW.items():
    d = {
        'id': eid, 'title': v['title'], 'level': 'L2', 'tier': v['tier'],
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': '制度',
        'one_line': v['one_line'], 'overview': v['overview'],
        'timeline': v['timeline'], 'causal_chain': [], 'schools': v['schools'],
        'key_data': [{'label': lb, 'value': val, 'unit': u, 'year': y, 'comparable_price': False,
                      'note': nt + '；单一来源待核实。', 'sources': [v['src']]}
                     for lb, val, u, y, nt in v['key_data']],
        'comparison': v['comparison'],
        'related': [r for r in v['related'] if r in ids or r in NEW],
        'sources': [v['src']], 'needs_verification': True,
        'pending_notes': '【续作IB】据维基全文新建；监管细则与各国实施差异待核实。',
    }
    d['related'] = [r for r in d['related'] if r in ids or r in NEW]
    json.dump(d, open('data/entries/%s.json' % eid, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('新建:', eid)

cov = json.load(open('coverage.json', encoding='utf-8'))
covids = {e['id'] for e in cov['entries']}
for eid, v in NEW.items():
    if eid not in covids:
        cov['entries'].append({'id': eid, 'level': 'L2', 'tier': v['tier'], 'status': 'written',
                               'source_count': 1, 'needs_verification': 1, 'last_updated': '2026-11-24',
                               'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球',
                               'crisis_type': '制度'})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('新建 %d 条 | coverage total: %d' % (n, cov['total']))
