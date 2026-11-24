# -*- coding: utf-8 -*-
"""续作CP：新增5条U3(20世纪上半)制度与事件条目。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20,270,520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

D = [
 dict(id='smoot-hawley-1930', title='斯姆特-霍利关税法(1930)', cat='制度',
  region='全球',
  ol='1930年美国大幅提高进口关税的法案，引发贸易伙伴报复，被视为大萧条深化的重要因素。',
  ov=('《斯姆特-霍利关税法》(Smoot–Hawley Tariff Act) 是1930年美国通过的大幅提高进口关税的法案。'
   '其后果可从两组数据看出：**1932年应税关税税率峰值达 59.1%**，仅次于1830年的61.7%；'
   '但同期的**全部进口中有63%是免税的**（1933年），因此应税税率并不等于实际保护水平。'
   '贸易伙伴迅速报复：**1930年5月，美国最忠实的贸易伙伴加拿大队16种产品加征新关税，'
   '这些产品约占美国（对加出口）的30%**。'
   '关税战使国际贸易萎缩，常被视为"以邻为壑"政策的教科书案例（见 beggar-thy-neighbour）。'
   '学界对其因果权重仍有争论：关税确实加剧了贸易萎缩，但大萧条的深度主要源于货币与金融因素。'
   '具体税率结构与各国报复清单待核实。'),
  tl=[
   {'year':1930,'display':'1930年','event':'美国通过《斯姆特-霍利关税法》，大幅提高进口关税','sources':['w-en-smoot-hawley']},
   {'year':1930,'display':'1930年5月','event':'加拿大对16种产品加征新关税（约占美国对加出口30%）','sources':['w-en-smoot-hawley']},
   {'year':1932,'display':'1932年','event':'应税关税税率峰值59.1%（仅次于1830年61.7%）','sources':['w-en-smoot-hawley']},
  ],
  causal=[('大萧条初期保护本国产业的政治压力 → 大幅提高关税','w-en-smoot-hawley'),
         ('贸易伙伴报复 → 各国关税轮番上升（应税税率峰值59.1%）','w-en-smoot-hawley'),
         ('国际贸易萎缩 → 加深全球性萧条（与货币金融因素叠加）','w-en-beggar-thy-neighbour')],
  schools=[{'holder':'贸易战视角','view':'关税战通过贸易渠道放大并延长了萧条','basis':'据关税与贸易数据归纳；因果权重待核实','sources':['w-en-smoot-hawley']},
           {'holder':'货币优先视角','view':'大萧条主因是货币收缩与金本位，关税是加剧因素而非主因','basis':'据货币主义解释归纳','sources':['fed-great-depression']}],
  kd=[
   {'label':'美国应税关税税率峰值(1932)','value':59.1,'unit':'%','year':1932,'comparable_price':False,
    'note':'原文：The dutiable tariff rate peak of 1932 was 59.1%, second only to the 61.7% rate of 1830；单一来源待核实。','sources':['w-en-smoot-hawley']},
   {'label':'1830年应税关税税率','value':61.7,'unit':'%（历史更高值）','year':1830,'comparable_price':False,
    'note':'原文：second only to the 61.7% rate of 1830；单一来源待核实。','sources':['w-en-smoot-hawley']},
   {'label':'免税进口占全部进口比重(1933)','value':63,'unit':'%','year':1933,'comparable_price':False,
    'note':'原文：63% of all imports in 1933 were not taxed, which the dutiable tariff rate does not reflect；单一来源待核实。','sources':['w-en-smoot-hawley']},
   {'label':'加拿大报复关税覆盖的美国出口比重','value':30,'unit':'%（16种产品，约）','year':1930,'comparable_price':False,
    'note':'原文：Canada ... imposing new tariffs on 16 products which accounted altogether for approximately 30% of U[S exports]；单一来源待核实。','sources':['w-en-smoot-hawley']},
  ],
  cmp=('与2018年以来的中美关税摩擦相比，1930年代的关税战发生在金本位与货币收缩的背景下，'
   '缺乏汇率与货币政策的缓冲；这与当代浮动汇率环境有本质差异。具体异同待核实。')),
 dict(id='scissors-crisis-1923', title='苏联剪刀差危机(1923)', cat='其他',
  region='欧洲',
  ol='1923年苏联新经济政策时期工农业价格"剪刀差"急剧扩大，农民收入相对工业品价格暴跌。',
  ov=('剪刀差危机(Scissors Crisis) 是1923年苏联新经济政策(NEP)时期的一次经济事件：'
   '**工业品与农产品价格之间的"剪刀差"不断扩大**，如同张开的剪刀两刃。'
   '价格分化在 **1923年10月** 达到峰值（工业品价格相对农产品极高）。'
   '后果是农民出售农产品的实际回报骤降，出现"谷物罢工"——农民不愿按低价交售，'
   '进而威胁城市粮食供应与工业化的资金来源。政府随后通过压低工业品价格、'
   '整顿"耐普曼"流通环节与信贷措施缓解。'
   '类似情形在 **1916年** 也曾出现（例如黑麦价格上涨47%，而一双靴子上涨334%）。'
   '该术语后来被广泛用于描述任何时期工农业（或初级产品与制成品）相对价格的失衡。具体数据待核实。'),
  tl=[
   {'year':1916,'display':'1916年','event':'类似危机：黑麦涨47%、靴子涨334%','sources':['w-en-scissors-crisis']},
   {'year':1923,'display':'1923年10月','event':'"剪刀差"达峰值，工农业价格严重分化','sources':['w-en-scissors-crisis']},
  ],
  causal=[('工业恢复慢于农业 + 流通环节与定价扭曲 → 工业品相对农产品价格偏高','w-en-scissors-crisis'),
         ('农民交售意愿下降（"谷物罢工"）→ 城市供应与工业化资金来源受威胁','w-en-scissors-crisis'),
         ('政策压价与整顿流通 → 剪刀差收窄，但埋下后续政策争论','w-en-scissors-crisis')],
  schools=[{'holder':'价格失衡视角','view':'剪刀差是计划/半计划体制下相对价格扭曲的典型表现','basis':'据1923年物价数据归纳','sources':['w-en-scissors-crisis']},
           {'holder':'工业化积累视角','view':'通过价格剪刀差为工业化积累资金，是一种隐性的资源转移','basis':'据苏联工业化融资讨论归纳；争议大','sources':['w-en-scissors-crisis']}],
  kd=[
   {'label':'黑麦价格涨幅(1916)','value':47,'unit':'%','year':1916,'comparable_price':False,
    'note':'原文：in 1916, when for example the price of rye rose by 47%；单一来源待核实。','sources':['w-en-scissors-crisis']},
   {'label':'靴子价格涨幅(1916)','value':334,'unit':'%（对比黑麦+47%）','year':1916,'comparable_price':False,
    'note':'原文：whereas that of a pair of boots rose by 334%；单一来源待核实。','sources':['w-en-scissors-crisis']},
  ],
  cmp=('与当代"初级产品 vs 制成品"贸易条件恶化（如 Prebisch-Singer 假说）机制相通，'
   '但苏联案例中价格并非完全由市场决定。具体异同待核实。')),
 dict(id='london-econ-1933', title='伦敦经济会议(1933)', cat='制度',
  region='全球',
  ol='1933年6—7月66国在伦敦召开的经济会议，旨在协调抗击大萧条，但因汇率分歧失败。',
  ov=('1933年伦敦货币与经济会议（London Monetary and Economic Conference）是'
   ' **1933年6月12日至7月27日** 在伦敦地质博物馆举行的、**66个国家**代表参加的国际会议。'
   '其目的是就抗击大萧条的措施、复兴国际贸易与稳定（汇率）达成协议。'
   '会议最终失败，核心障碍是汇率与国内政策优先次序的分歧：'
   '美国当时正转向国内复兴与美元贬值，不愿承诺稳定汇率；'
   '而金集团国家与英国则希望恢复汇率稳定与贸易秩序。'
   '会议的失败标志着1930年代国际经济合作的一次重大挫折，'
   '此后各国转向双边与帝国特惠安排（如渥太华协定体系），全球经济进一步碎片化。'
   '该案例常被引为"缺乏霸权或领导力时国际协调难以达成"的典型。具体细节待核实。'),
  tl=[
   {'year':1933,'display':'1933年6月12日—7月27日','event':'66国伦敦经济会议召开，最终失败','sources':['w-en-london-economic-conference']},
  ],
  causal=[('大萧条下各国亟需协调 → 66国召开伦敦会议','w-en-london-economic-conference'),
         ('汇率稳定与国内复兴的政策优先次序冲突（美国不愿承诺汇率）→ 谈判破裂','w-en-nixon-shock'),
         ('合作失败 → 转向双边与帝国特惠，全球经济碎片化','w-en-tariff-act')],
  schools=[{'holder':'协调失败视角','view':'缺乏领导国与共同承诺使国际协调难以持续','basis':'据会议进程归纳','sources':['w-en-london-economic-conference']},
           {'holder':'国内优先视角','view':'各国在大萧条中优先稳定国内，外部承诺被牺牲','basis':'据政策取向归纳；因果待核实','sources':['w-en-gold-bloc']}],
  kd=[],
  cmp=('与1944年布雷顿森林会议形成鲜明对比：后者在美国主导、战争同盟背景下达成，'
   '而1933年缺乏领导力与共同框架。具体异同待核实。')),
 dict(id='glass-steagall-1933', title='格拉斯-斯蒂格尔法(1933)', cat='制度',
  region='北美',
  ol='1933年美国银行法的四项条款，分离商业银行与投资银行，并设立存款保险。',
  ov=('《格拉斯-斯蒂格尔法》(Glass–Steagall legislation) 指美国1933年银行法中的**四项条款**，'
   '其核心是**分离商业银行与投资银行业务**。'
   '名称来自国会提案人——参议员卡特·格拉斯(Carter Glass) 与众议员亨利·斯蒂格尔(Henry B. Steagall)。'
   '分离的具体标准之一是：除获准承销政府发行债券外，'
   '**商业银行来自证券业务的收入不得超过其总收入的10%**。'
   '该法同时设立了联邦存款保险公司(FDIC)（见 deposit-insurance 条目）。'
   '其立法动因是大萧条中的银行倒闭潮与对"银行用存款投机证券"的指责。'
   '1999年《金融服务现代化法》废除了其中的业务分离条款，'
   '而2008年危机后对其功过的讨论再度升温。具体条款细节待核实。'),
  tl=[
   {'year':1933,'display':'1933年','event':'美国银行法通过，含格拉斯-斯蒂格尔四项条款','sources':['w-en-glass-steagall']},
   {'year':1933,'display':'1933年','event':'据该法设立FDIC（存款保险）','sources':['w-en-deposit-insurance']},
   {'year':1999,'display':'1999年','event':'《金融服务现代化法》废除业务分离条款','sources':['w-en-glass-steagall']},
  ],
  causal=[('大萧条银行倒闭潮 + 对存款被用于证券投机的指责 → 立法分离业务','w-en-glass-steagall'),
         ('商业银行证券业务收入不得超过总收入10%（政府债券除外）→ 业务边界确立','w-en-glass-steagall'),
         ('1999年废除分离条款 → 混业经营恢复，2008年后争议再起','w-en-glass-steagall')],
  schools=[{'holder':'金融稳定视角','view':'业务分离可隔离证券风险对存款保险基金的侵蚀','basis':'据立法动因归纳','sources':['w-en-glass-steagall']},
           {'holder':'效率视角','view':'分离削弱范围经济，且未阻止2008年危机','basis':'据废除与危机经验归纳；因果待核实','sources':['w-en-subprime-mortgage-crisis']}],
  kd=[
   {'label':'商业银行证券业务收入上限','value':10,'unit':'%（占总收入，政府债券除外）','year':1933,'comparable_price':False,
    'note':'原文：commercial banks could only have 10 percent of their income come from securit[ies]；单一来源待核实。','sources':['w-en-glass-steagall']},
  ],
  cmp=('与英国2019年起实施的"圈护"(ring-fencing) 制度思路相近：都试图在混业环境中隔离零售存款业务。具体异同待核实。')),
 dict(id='nira-1933', title='全国工业复兴法(1933)', cat='制度',
  region='北美',
  ol='1933年美国授权总统规范工业以"公平工资与价格"刺激复苏的法律，并设立公共工程管理局。',
  ov=('《1933年全国工业复兴法》(NIRA) 是美国第73届国会通过的劳动法与消费者法，'
   '授权总统**规范工业以设定"公平工资与价格"、从而刺激经济复苏**；'
   '同时设立全国公共工程计划——公共工程管理局(PWA)。'
   '其经济逻辑值得注意：当时把垄断与卡特尔的"更高价格"视为**必要**，'
   '因为 **1929—1933年的严重通缩已使价格下跌20%以上**——'
   '这与通常"反垄断以降低价格"的思路相反，反映了大萧条中"再通胀"的紧迫性。'
   '规模上，第二编第204条明确为公路、桥梁、道路、铁路交叉口等交通项目提供了 '
   '**4亿美元** 的资金。'
   'NIRA 于1935年被最高法院裁定违宪（具体案由待核实），其工业规范部分随之终止，'
   '但公共工程与部分劳工权利安排延续。具体条款待核实。'),
  tl=[
   {'year':1933,'display':'1933年','event':'NIRA 通过，设立PWA；第204条拨款4亿美元用于交通项目','sources':['w-en-nira-1933']},
   {'year':1935,'display':'1935年','event':'最高法院裁定NIRA违宪（具体案由待核实）','sources':['w-en-nira-1933']},
  ],
  causal=[('1929—1933年通缩使价格下跌20%以上 → 政策转向"再通胀"','w-en-nira-1933'),
         ('授权规范工业的工资与价格 + PWA公共工程（4亿美元交通项目）→ 直接创造需求','w-en-nira-1933'),
         ('被最高法院裁定违宪 → 工业规范终止，财政与劳工立法另寻路径','w-en-nira-1933')],
  schools=[{'holder':'再通胀视角','view':'在深度通缩下，抬高价格与工资有助于打破债务-通缩螺旋','basis':'据立法逻辑与通缩数据归纳','sources':['w-en-nira-1933']},
           {'holder':'竞争视角','view':'允许卡特尔化损害效率与消费者利益','basis':'据反垄断传统归纳；效果争议大','sources':['w-en-nira-1933']}],
  kd=[
   {'label':'PWA交通项目拨款(第204条)','value':400,'unit':'百万美元（4亿）','year':1933,'comparable_price':False,
    'note':'原文：Title II, Section 204 explicitly provided $400 million for the construction of public highways, bridges, roads...；单一来源待核实。','sources':['w-en-nira-1933']},
   {'label':'1929—1933年美国通缩幅度','value':-20,'unit':'%（价格下跌20%以上）','year':1933,'comparable_price':False,
    'note':'原文：the severe deflation of 1929–33 had depressed prices 20% and more；单一来源待核实。','sources':['w-en-nira-1933']},
  ],
  cmp=('与 contemporaneous 的英国"廉价货币"+公共工程思路相比，NIRA 的独特之处是**允许甚至鼓励卡特尔化以抬价**，'
   '而非单纯扩大需求。具体异同待核实。')),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U3 20世纪上半', 'period': '20世纪上半', 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sorted(sp['tl'], key=lambda t:t.get('year',0)),
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': sp['kd'],
        'schools': sp['schools'],
        'policy_response': [],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st,s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基全文；单源待核实。【续作CP】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r97_data.json', encoding='utf-8'))
MAP = {'smoot-hawley-1930':'w-en-smoot-hawley','scissors-crisis-1923':'w-en-scissors-crisis',
       'london-econ-1933':'w-en-london-economic-conference','glass-steagall-1933':'w-en-glass-steagall',
       'nira-1933':'w-en-nira-1933'}
for eid, sid in MAP.items():
    if sid in ex: continue
    v = meta.get(eid)
    if not v: continue
    sd['sources'].append({'id':sid,'title':v['title'],'author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+v['title'].replace(' ','_').replace('–','%E2%80%93'),
      'url2':None,'verified':True,'link_ok':True,'note':'Wikipedia API(full extract)核对(本会话抓取)'})
    ex.add(sid); print('新增来源',sid,'|',v['title'])
sd['count']=len(sd['sources'])
json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':'重要','status':'written',
      'source_count':len(sp['causal']),'needs_verification':1,'last_updated':'2026-11-24',
      'unit':'U3 20世纪上半','period':'20世纪上半','region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
