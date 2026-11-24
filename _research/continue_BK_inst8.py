# -*- coding: utf-8 -*-
"""续作BK：新增8条国际金融治理机构(L2)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：架构示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体成立时间与职能见正文。</text></svg>")
    return ''.join(s)

D = [
 dict(id='bis', title='国际清算银行(BIS)', cat='制度',
  ol='由成员国中央银行所有的国际金融机构，主要目标是促进国际货币与金融合作。',
  ov='国际清算银行（BIS）是一家由成员国中央银行所有的国际金融机构。其主要目标是促进国际货币与金融合作（并充当中央银行的银行）。BIS 也是巴塞尔银行监管委员会等标准制定机构的所在地，在全球金融治理中扮演关键角色。具体职能与历史待核实。',
  tl=[{'year':1930,'display':'1930年','event':'BIS 成立（通说；据 Wikipedia BIS，具体日期待核实）','sources':['w-en-bis']}],
  causal=[('各国央行需合作与清算便利 → 设立 BIS','w-en-bis'),
          ('BIS 提供央行合作平台与标准制定场所','w-en-bis'),
          ('巴塞尔资本标准由此产生 → 影响全球银行监管','w-en-basel-accords')],
  schools=[('合作视角','BIS 降低央行间协调成本','w-en-bis'),
           ('标准制定视角','非正式网络促成监管标准扩散','w-en-basel-accords')],
  cmp='与国际货币基金组织（治理与救助）不同，BIS 偏重央行合作与标准制定。具体异同待核实。'),
 dict(id='gatt', title='关税与贸易总协定(GATT)', cat='制度',
  ol='多国间的法律协定，总体目的在通过减少或消除关税等贸易壁垒促进国际贸易。',
  ov='关税与贸易总协定（GATT）是许多国家之间的法律协定，其总体目的是通过减少或消除关税等贸易壁垒来促进国际贸易。它是战后多边贸易体系的基石，后经多轮谈判演化为世界贸易组织（WTO）。具体历史待核实。',
  tl=[{'year':1947,'display':'1947年','event':'GATT 签署（通说；具体日期待核实）','sources':['w-en-gatt']},
      {'year':1995,'display':'1995年1月1日','event':'WTO 成立，接续 GATT 框架','sources':['w-en-wto']}],
  causal=[('1930年代以邻为壑关税战 → 战后寻求贸易自由化规则','w-en-beggar-thy-neighbour'),
          ('GATT 多轮谈判削减关税 → 贸易扩张','w-en-gatt'),
          ('乌拉圭回合 → 升级为 WTO','w-en-wto')],
  schools=[('自由化视角','规则化减关税促进增长','w-en-gatt'),
           ('主权视角','规则约束可能限制政策空间','w-en-beggar-thy-neighbour')],
  cmp='与布雷顿森林体系的货币支柱（IMF）并列，构成战后"货币-贸易"双支柱。具体异同待核实。'),
 dict(id='oecd', title='经济合作与发展组织(OECD)', cat='制度',
  ol='拥有38个成员国的政府间组织，1961年成立，旨在促进经济进步与全球贸易。',
  ov='经济合作与发展组织（OECD）是一个拥有38个成员国的政府间组织。它于1961年成立，旨在促进经济进步与全球贸易。OECD 以政策研究、统计标准与同行评审著称，其数据与研究广泛用于国际比较。具体职能待核实。',
  tl=[{'year':1961,'display':'1961年','event':'OECD 成立，38个成员国（据 Wikipedia OECD）','sources':['w-en-oecd']}],
  causal=[('战后欧洲经济合作需求 → 从 OEEC 演进为 OECD','w-en-oecd'),
          ('提供统计标准与政策同行评审','w-en-oecd'),
          ('影响成员国政策与全球治理议程','w-en-international-monetary-system')],
  schools=[('技术治理视角','以数据与同行评审影响政策','w-en-oecd'),
           ('俱乐部视角','发达国家俱乐部属性限制代表性','w-en-gatt')],
  cmp='与 IMF/世行相比，OECD 不提供救助，侧重研究与政策协调。具体异同待核实。'),
 dict(id='fsb', title='金融稳定理事会(FSB)', cat='制度',
  ol='监测全球金融体系并提出建议的国际机构，2009年G20匹兹堡峰会成立。',
  ov='金融稳定理事会（FSB）是一个监测全球金融体系并提出相关建议的国际机构。它于2009年G20匹兹堡峰会上成立，作为（金融稳定论坛的）后继机构。FSB 负责协调国际监管改革、识别系统性风险，并与标准制定机构合作。具体职能待核实。',
  tl=[{'year':2009,'display':'2009年','event':'G20匹兹堡峰会成立 FSB，接续金融稳定论坛（据 Wikipedia FSB）','sources':['w-en-fsb']}],
  causal=[('2008金融危机暴露监管碎片化 → 需全球协调机构','w-en-global-financial-crisis-2008'),
          ('G20 授权成立 FSB → 协调监管改革','w-en-fsb'),
          ('推动系统重要性机构名单与影子银行监测','w-en-sifi')],
  schools=[('协调视角','FSB 弥合各国监管差异','w-en-fsb'),
           ('执行力视角','FSB 无强制力，依赖成员自愿落实','w-en-basel-iii')],
  cmp='与 BIS（央行合作）分工：FSB 偏重监管政策协调与风险识别。具体异同待核实。'),
 dict(id='esfs', title='欧洲金融监管体系(ESFS)', cat='制度',
  ol='欧盟金融监管框架，自2011年起运作，由欧洲监管局等构成。',
  ov='欧洲金融监管体系（ESFS）是欧盟自2011年起运作的金融监管框架。该系统由欧洲监管局（ESAs）等构成（并与 ESRB 的宏观审慎层面相配合）。它是在2008年危机后为弥补成员国监管分割而建立的。具体架构待核实。',
  tl=[{'year':2011,'display':'2011年起','event':'ESFS 开始运作（据 Wikipedia ESFS）','sources':['w-en-esfs']}],
  causal=[('危机暴露成员国监管分割 → 需欧盟层面协调','w-en-global-financial-crisis-2008'),
          ('建立 ESFS 与三家欧洲监管局 → 统一规则与协调','w-en-esfs'),
          ('与 ESRB 宏观审慎职能配合','w-en-esrb')],
  schools=[('一体化视角','超国家监管协调弥补分割','w-en-esfs'),
           ('主权视角','监管权让渡引发政治阻力','w-en-euro-area-crisis')],
  cmp='与美国的联邦监管体系相比，欧盟为超国家协调且依赖成员国执行。具体异同待核实。'),
 dict(id='esrb', title='欧洲系统性风险委员会(ESRB)', cat='制度',
  ol='2010年12月16日为应对欧元区危机而设立，负责欧盟金融体系的宏观审慎监督。',
  ov='欧洲系统性风险委员会（ESRB）是2010年12月16日为应对欧元区危机而设立的机构。其任务是对（欧盟）金融体系进行宏观审慎监督。ESRB 负责识别系统性风险并向监管者发出警告与建议，本身不具直接监管权。具体职能待核实。',
  tl=[{'year':2010,'display':'2010年12月16日','event':'ESRB 设立，负责宏观审慎监督（据 Wikipedia ESRB）','sources':['w-en-esrb']}],
  causal=[('欧元区危机暴露系统性风险监测缺口','w-en-euro-area-crisis'),
          ('2010-12-16 设立 ESRB → 承担宏观审慎监督','w-en-esrb'),
          ('以警告与建议影响成员国监管','w-en-macroprudential-policy')],
  schools=[('宏观审慎视角','需超越个体机构的系统性视角','w-en-esrb'),
           ('软权力视角','无直接监管权削弱执行力','w-en-macroprudential-policy')],
  cmp='与 FSB 的全球层面相对应，ESRB 是欧盟层面的宏观审慎机构。具体异同待核实。'),
 dict(id='iosco', title='国际证监会组织(IOSCO)', cat='制度',
  ol='各国证券与期货市场监管机构的协会。',
  ov='国际证监会组织（IOSCO）是各国证券与期货市场监管机构组成的协会。其成员通常是一国的主要证券监管机构。IOSCO 制定证券监管原则与标准，促进跨境监管合作与信息共享。具体职能待核实。',
  tl=[{'year':1983,'display':'1983年','event':'IOSCO 成立（通说；具体日期待核实）','sources':['w-en-iosco']}],
  causal=[('跨境证券交易增加 → 需监管协调','w-en-iosco'),
          ('制定监管原则与谅解备忘录 → 促进合作','w-en-iosco'),
          ('与 BIS、FSB 共同构成标准制定网络','w-en-fsb')],
  schools=[('标准制定视角','以原则与同行评审推动趋同','w-en-iosco'),
           ('主权视角','成员国执行差异削弱一致性','w-en-esfs')],
  cmp='与巴塞尔委员会（银行）、IAIS（保险）并列为三大金融标准制定机构。具体异同待核实。'),
 dict(id='fatf', title='金融行动特别工作组(FATF)', cat='制度',
  ol='1989年由G7倡议成立的政府间组织，负责制定反洗钱与反恐融资政策。',
  ov='金融行动特别工作组（FATF，法语名 GAFI）是一个政府间组织，1989年在七国集团（G7）倡议下成立，以制定（反洗钱与反恐融资）政策。FATF 的建议被广泛视为国际反洗钱标准，并通过互评估机制推动落实。具体职能待核实。',
  tl=[{'year':1989,'display':'1989年','event':'G7 倡议成立 FATF（据 Wikipedia FATF）','sources':['w-en-fatf']}],
  causal=[('洗钱与金融犯罪跨境化 → 需国际标准','w-en-fatf'),
          ('FATF 建议 + 互评估 → 推动各国立法','w-en-fatf'),
          ('"不合作辖区"名单 → 形成实质约束力','w-en-fatf')],
  schools=[('标准扩散视角','互评估与名单机制产生强约束','w-en-fatf'),
           ('成本视角','合规负担与"去风险化"副作用受批评','w-en-de-risking')],
  cmp='与 IOSCO/BIS 等标准制定机构相比，FATF 的名单机制约束力更强。具体异同待核实。'),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st, s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：成立时间与职能据维基摘要；具体日期与细节待核实。【续作BK】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r74_inst.json', encoding='utf-8'))
for eid, v in meta.items():
    sid = 'w-en-' + eid
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科', 'url': 'https://en.wikipedia.org/wiki/' + v['slug'], 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'Wikipedia REST API核对(本会话抓取摘要)'
    })
    ex.add(sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have:
        continue
    cov['entries'].append({
        'id': sp['id'], 'level': 'L2', 'tier': '重要', 'status': 'written',
        'source_count': len(sp['causal']), 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
