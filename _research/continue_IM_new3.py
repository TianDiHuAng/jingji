# -*- coding: utf-8 -*-
"""续作IM：新建 bank-holiday（1933年美国银行假日）、risk-pooling、self-insurance。"""
import glob
import json

NEW = {
 'bank-holiday': {
   'title': '1933年美国银行假日',
   'unit': 'U3 20世纪上半', 'period': '20世纪上半', 'region': '北美',
   'crisis_type': '银行', 'tier': '重要', 'src': 'w-en-bank-holiday',
   'one_line': '1933年美国全国性银行停业与《紧急银行救济法》，用"关门整顿+重新发钞"止住挤兑。',
   'overview': (
     '1933 年美国银行假日是大萧条期间**以行政手段中止全国银行营业**、再择优选优复业的处置。'
     '起因是挤兑的连锁扩散：**1933 年 2 月 14 日**起，受大萧条打击尤重的密歇根州率先宣布'
     '**八天**银行假日；对其他银行倒闭的恐惧从一个州蔓延到另一个州，储户争相提取存款；'
     '**数周内**其余各州相继宣布本州银行假日，试图遏制挤兑。'
     '**1933 年 3 月 9 日**，国会通过《紧急银行救济法》(Emergency Banking Relief Act)，'
     '该法是 1917 年《与敌国贸易法》的修正案，'
     '**授权十二家联邦储备银行以"良好资产"为担保发行额外货币**，'
     '使获准复业的银行能满足一切合法提款需求。'
     '**3 月 13 日**银行复业，储户反而排队把藏起来的现金存回银行——'
     '**两周内**美国人存回了停业前合法提取的**超过一半**的通货。'
     '**3 月 15 日**华尔街复市，道琼斯工业平均指数当日上涨 **8.26 点**。'
     '同年晚些时候通过的《1933 年银行法》提供了长期回应（含设立联邦存款保险公司 FDIC）。'),
   'timeline': [
     {'year': 1933, 'event': '2月14日密歇根州率先宣布八天银行假日，挤兑恐慌向其他州蔓延'
                             '（据 Wikipedia Emergency Banking Act of 1933）'},
     {'year': 1933, 'event': '3月9日国会通过《紧急银行救济法》，授权联邦储备银行以良好资产发行额外货币'
                             '（据 Wikipedia Emergency Banking Act of 1933）'},
     {'year': 1933, 'event': '3月13日银行复业，储户排队存回现金；3月15日华尔街复市，道指涨8.26点'
                             '（据 Wikipedia Emergency Banking Act of 1933）'},
     {'year': 1933, 'event': '同年《1933年银行法》通过，设立联邦存款保险公司(FDIC)'
                             '（据 Wikipedia Emergency Banking Act of 1933）'},
   ],
   'schools': [
     {'holder': '"关门整顿"视角',
      'view': '停业给当局争取了核查银行偿付能力的时间，并以"资产担保发钞"消除复业银行的流动性疑虑——'
              '挤兑因此停止，存款回流',
      'sources': ['w-en-bank-holiday']},
     {'holder': '"信心与信号"视角',
      'view': '止住挤兑的关键不只是资金，而是**公开的择优复业名单**这一信号：'
              '被批准复业的银行获得隐性认证，未被批准者则被市场淘汰',
      'sources': ['w-en-bank-holiday']},
   ],
   'key_data': [
     {'label': '密歇根州银行假日天数', 'value': 8, 'unit': '天', 'year': 1933,
      'comparable_price': False,
      'note': '原文：Michigan ... declared an eight-day bank holiday；单一来源待核实。',
      'sources': ['w-en-bank-holiday']},
     {'label': '华尔街复市当日道指涨幅', 'value': 8.26, 'unit': '点', 'year': 1933,
      'comparable_price': False,
      'note': '原文：the Dow Jones Industrial Average, gaining 8.26 point；单一来源待核实。',
      'sources': ['w-en-bank-holiday']},
     {'label': '复业两周内回流存款占停业前提取额的比例（超过）', 'value': 50, 'unit': '%', 'year': 1933,
      'comparable_price': False,
      'note': '原文：Within two weeks, Americans had redeposited more than half of the currency '
              'that they had legally withdrawn before the bank suspension；单一来源待核实。',
      'sources': ['w-en-bank-holiday']},
   ],
   'comparison': (
     '与现代**处置制度**（见 bank-resolution）的区别：1933 年的做法是'
     '**全国性临时停业 + 择优复业**，没有区分"系统重要性"与"非系统重要性"，也没有自救债券；'
     '现代处置强调按机构分级、由股东与债权人承担损失。'
     '与**存款保险**的关系：银行假日是**应急止血**，FDIC 是**长期制度**——'
     '两者在同一年先后出现，正好构成"先救火、再防火"的完整序列。'),
   'related': ['crisis-33ce', 'great-depression', 'bank-run', 'deposit-insurance',
               'bank-resolution', 'panic-1930'],
 },
 'risk-pooling': {
   'title': '风险池（风险汇聚）',
   'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球',
   'crisis_type': '制度', 'tier': '补充', 'src': 'w-en-risk-pooling',
   'one_line': '把大量独立风险汇聚到一个池中，以分散单个主体难以承受的巨灾损失。',
   'overview': (
     '风险池(risk pool) 是一种风险管理形式，主要由保险公司采用：'
     '多家保险公司共同组成一个池，为参与方提供对**洪水、地震等巨灾风险**的保护。'
     '其原理是**大数定律**——单个主体难以承受的极端损失，'
     '由大量相互独立的暴露单位共同分担后变得可以承受。'
     '风险池的**前提假设**是各成员的风险**相互独立**：'
     '若风险高度相关（如同一地区的所有成员同时遭遇同一场地震），'
     '池化就失效——这与金融危机的传染机制是同一个数学问题。'
     '除保险外，风险池也用于**供应链管理**与**政府**（如州级巨灾池、失业保险池）。'),
   'timeline': [
     {'year': 1752, 'event': '本杰明·富兰克林创立费城房屋火灾保险公司，'
                             '为美国最早的互助式风险汇聚实践之一（据 Wikipedia Risk pool；具体年份待核实）'},
   ],
   'schools': [
     {'holder': '分散化视角',
      'view': '把大量独立风险汇聚可显著降低单个主体的尾部暴露，是保险业存在的基本理由'
              '（据 Wikipedia Risk pool）',
      'sources': ['w-en-risk-pooling']},
     {'holder': '相关性风险视角',
      'view': '池化的有效性依赖风险独立性；当风险高度相关（巨灾、系统性事件）时，'
              '池化不能分散而只是**集中**了风险，反而可能放大脆弱性'
              '（本库据通行讨论归纳；具体出处待核实）',
      'sources': ['w-en-risk-pooling']},
   ],
   'key_data': [],
   'comparison': (
     '与**分散化投资**的区别：后者靠持有多种资产降低非系统性风险，'
     '前者靠成员间分担损失。两者都依赖"相关性低"这一前提。'
     '与**再保险**的区别：风险池是**同层成员之间**的分担，'
     '再保险是**向上转移**给更大的承担者。'
     '与**存款保险**的类比：存款保险基金本质上是一个风险池，'
     '其脆弱点同样在于"危机时所有成员同时出险"。'),
   'related': ['deposit-insurance', 'counterparty-risk', 'moral-hazard', 'actuarial',
               'insurance-history', 'systemic-risk'],
 },
 'self-insurance': {
   'title': '自我保险',
   'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球',
   'crisis_type': '制度', 'tier': '补充', 'src': 'w-en-self-insurance',
   'one_line': '不购买第三方保险而自行承担风险，通常以专门准备金或资本缓冲的形式留存。',
   'overview': (
     '自我保险(self-insurance) 是一种风险管理方法：'
     '对某类风险负有责任的组织**不购买第三方保险**，而选择**自行承担**该风险。'
     '审慎运用时，采用者会为潜在损失**预留专门的准备金或资本缓冲**，'
     '使自己在损失发生时仍能履约——因此它并不等于"不设防"，'
     '而是把"向外部付费转移风险"换成"内部留存资金吸收风险"。'
     '其**适用条件**是：损失规模可估、发生频率可控、且自身资本足以承受最坏情形。'
     '在金融领域，银行用**资本缓冲**吸收预期内的贷款损失、'
     '大型企业用**专属保险公司(captive insurer)**处理自身风险，都属自我保险的形态。'
     '其**风险**在于误判自身承受能力：若把"低概率高损失"的风险当作可自我保险，'
     '一次极端事件就可能击穿全部准备金。'),
   'timeline': [
     {'year': 1970, 'event': '大型企业开始普遍设立专属保险公司(captive insurer)处理自身风险'
                             '（据 Wikipedia Self-insurance；具体年份待核实）'},
   ],
   'schools': [
     {'holder': '成本效率视角',
      'view': '当损失频率与规模可估、且自身资本充裕时，自我保险可省去保险公司的费用与利润加成'
              '（据 Wikipedia Self-insurance）',
      'sources': ['w-en-self-insurance']},
     {'holder': '尾部风险视角',
      'view': '自我保险对**肥尾**风险不适用——最需要保险的恰是极端事件，'
              '而自我保险在此时往往同时面临资本枯竭。'
              '（本库据通行讨论归纳；具体出处待核实）',
      'sources': ['w-en-self-insurance']},
   ],
   'key_data': [],
   'comparison': (
     '与**购买保险**的区别：保险把风险转移给第三方（支付保费换取确定性），'
     '自我保险在内部留存资金（省下保费但承担波动）。'
     '与**资本缓冲**的关系：银行资本在功能上就是对其资产风险的自我保险。'
     '与**存款保险**的区别：后者是行业共同出资的强制安排，非个体自主选择。'),
   'related': ['deposit-insurance', 'risk-pooling', 'capital-adequacy', 'moral-hazard',
               'insurance-history'],
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
 'w-en-bank-holiday': ('Emergency Banking Act of 1933', 'https://en.wikipedia.org/wiki/Emergency_Banking_Act_of_1933'),
 'w-en-risk-pooling': ('Risk pool', 'https://en.wikipedia.org/wiki/Risk_pool'),
 'w-en-self-insurance': ('Self-insurance', 'https://en.wikipedia.org/wiki/Self-insurance'),
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
        'unit': v['unit'], 'period': v['period'], 'region': v['region'],
        'crisis_type': v['crisis_type'],
        'one_line': v['one_line'], 'overview': v['overview'],
        'timeline': v['timeline'], 'causal_chain': [], 'schools': v['schools'],
        'key_data': v['key_data'], 'comparison': v['comparison'],
        'related': [r for r in v['related'] if r in ids or r in NEW],
        'sources': [v['src']], 'needs_verification': True,
        'pending_notes': '【续作IM】据维基专属页全文新建；细节与年份待第二来源核实。',
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
                               'unit': v['unit'], 'period': v['period'], 'region': v['region'],
                               'crisis_type': v['crisis_type']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('新建 %d 条 | coverage total: %d' % (n, cov['total']))
