# -*- coding: utf-8 -*-
"""续作DF：新增7条概念(固定/浮动汇率/转轨经济/柠檬市场/洗钱/货币战/错误投资)。"""
import json, glob

def svg(t, labels):
    e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：概念示意</text>"]
    for x, lb in zip([20,270,520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)

D = [
 dict(id='fixed-exchange-rate', title='固定汇率制度', cat='制度',
  ol='货币当局承诺将本币汇率维持在既定水平（或窄幅区间）的汇率安排。',
  ov=('固定汇率制度（fixed exchange rate system）是货币当局**承诺将本币汇率维持在既定水平或窄幅区间**的安排。'
   '其形式包括硬钉住（货币局、美元化）、传统钉住、水平区间与爬行钉住等。'
   '优点是可提供**名义锚**、抑制通胀预期、降低贸易与投资的汇率不确定性；'
   '代价是**丧失货币政策独立性**（不可能三角），且维持钉住需要充足储备与财政纪律。'
   '危机机制在于：一旦市场认为平价不可持续，投机攻击会耗尽储备，'
   '最终被迫贬值或放弃钉住——1992年英镑（见 black-wednesday-1992）、'
   '1994年墨西哥（见 mexican-peso-1994）、1997年泰铢（见 asian-financial-crisis-1997）'
   '都是同一剧本的不同版本。钉住越"硬"，退出时的痛苦越大。具体分类与案例待核实。'),
  tl=[],
  causal=[('以钉住提供名义锚 → 抑制通胀预期','w-en-fixed-exchange-rate'),
         ('丧失货币政策独立性 + 平价被质疑 → 投机攻击与储备流失','w-en-impossible-trinity'),
         ('被迫贬值或放弃钉住 → 资产负债表效应放大冲击','w-en-original-sin')],
  schools=[('名义锚视角','固定汇率提供可信的物价稳定承诺','w-en-fixed-exchange-rate'),
           ('脆弱性视角','不可持续的平价最终必然崩溃，越晚代价越大','w-en-asian-financial-crisis')],
  srcs=['w-en-fixed-exchange-rate','w-en-impossible-trinity']),
 dict(id='floating-exchange-rate', title='浮动汇率制度', cat='制度',
  ol='汇率由市场供求决定、货币当局不承诺特定水平的汇率安排。',
  ov=('浮动汇率制度（floating exchange rate）是**汇率由市场供求决定**、'
   '货币当局不承诺维持特定水平的安排；介于两者之间的是"管理浮动"。'
   '其核心优势是**保留货币政策独立性**（可自主决定利率）并让汇率吸收外部冲击，'
   '这正是不可能三角中"放弃汇率稳定"的那一极。'
   '代价则包括：汇率波动增加贸易与投资的不确定性；'
   '若存在**货币错配**（借外币），贬值会直接恶化资产负债表'
   '（即"浮动恐惧"现象，见 fear-of-floating）；'
   '以及可能出现的汇率超调与投机性波动。'
   '1973年后主要货币转向浮动（见 bretton-woods、smithsonian-agreement），'
   '但多数新兴市场实际实行的是某种管理浮动。具体分类待核实。'),
  tl=[
   {'year':1973,'display':'1973年','event':'布雷顿森林体系瓦解后主要货币转向浮动','sources':['w-en-floating-exchange-rate']},
  ],
  causal=[('汇率由市场决定 → 货币政策可专注国内目标','w-en-floating-exchange-rate'),
         ('汇率波动吸收外部冲击 → 减少储备消耗','w-en-impossible-trinity'),
         ('若存在货币错配 → 贬值恶化资产负债表（浮动恐惧）','w-en-original-sin')],
  schools=[('吸收冲击视角','浮动使汇率成为缓冲器，保留货币政策空间','w-en-floating-exchange-rate'),
           ('浮动恐惧视角','新兴市场因货币错配而不敢真正浮动','w-en-original-sin')],
  srcs=['w-en-floating-exchange-rate','w-en-impossible-trinity']),
 dict(id='transition-economy', title='转轨经济', cat='其他',
  ol='从计划经济向市场经济转型的经济体；其转型初期的产出下降与制度真空是危机的温床。',
  ov=('转轨经济(transition economy) 指**从计划经济向市场经济转型**的经济体，'
   '主要指1990年代的中东欧与前苏联国家。'
   '其经济特征包括：国有企业大规模私有化、价格与贸易自由化、'
   '金融体系从单一银行制转向商业银行体系、以及国家能力的重构。'
   '转型初期的普遍现象是**产出大幅下降**（"转型性衰退"）、'
   '高通胀甚至恶性通胀（如俄罗斯1992、南斯拉夫1993-94、见 yugoslav-hyper-1992）、'
   '以及**金融监管真空**——后者正是阿尔巴尼亚金字塔骗局（见 albania-pyramid-1997）'
   '与俄罗斯1998年危机（见 russian-1998）的制度背景。'
   '转轨经验催生了大量关于"渐进 vs 休克疗法""制度优先 vs 自由化优先"的争论。'
   '具体路径差异待核实。'),
  tl=[
   {'year':1989,'display':'1989年后','event':'中东欧与前苏联国家启动向市场经济转型','sources':['w-en-transition-economy']},
  ],
  causal=[('价格与贸易自由化 + 私有化 → 原有生产网络解体，产出下降','w-en-transition-economy'),
         ('金融体系重建但监管能力不足 → 监管真空与欺诈滋生','w-en-albania-pyramid-1997'),
         ('财政能力削弱 + 货币扩张 → 高通胀与货币危机','w-en-yugoslav-hyper-1992')],
  schools=[('休克疗法视角','快速全面的自由化可缩短转型期并建立可信度','w-en-transition-economy'),
           ('制度优先视角','缺乏制度基础的自由化会制造真空与掠夺','w-en-ebrd')],
  srcs=['w-en-transition-economy','w-en-ebrd']),
 dict(id='lemons-market', title='柠檬市场（信息不对称与逆向选择）', cat='理论',
  ol='当卖方比买方更了解质量时，低质量商品驱逐高质量商品，市场可能萎缩甚至消失。',
  ov=('"柠檬市场"(the market for lemons) 是阿克洛夫关于**信息不对称与逆向选择**的经典分析：'
   '当**卖方比买方更了解商品质量**时，买方只能按平均质量出价，'
   '于是高质量卖方退出，市场平均质量下降、价格进一步下跌——'
   '最终**低质量商品（"柠檬"）驱逐高质量商品**，市场可能萎缩甚至消失。'
   '该逻辑在金融中有多重映射：'
   '①**信贷配给**——银行无法区分借款人风险时，只能提高利率，'
   '结果把低风险借款人挤出（见 credit-rationing）；'
   '②**证券化**——当发起方比投资者更了解贷款质量时，'
   '结构化产品市场可能因逆向选择而冻结（见 subprime-lending）；'
   '③**银行挤兑**——存款人无法观测银行资产质量，只能先取为快（见 bank-run）。'
   '对策包括信息披露、评级、担保与声誉机制。具体论述待核实。'),
  tl=[],
  causal=[('卖方掌握质量信息、买方不掌握 → 买方只按平均质量出价','w-en-lemons-market'),
         ('高质量卖方退出 → 平均质量与价格进一步下降','w-en-adverse-selection'),
         ('市场萎缩或冻结 → 需以披露、担保与声誉机制缓解','w-en-information-asymmetry')],
  schools=[('信息视角','信息不对称是市场失灵的核心，需制度性披露','w-en-lemons-market'),
           ('市场自愈视角','声誉与担保可内生解决部分不对称问题','w-en-credit-rating')],
  srcs=['w-en-lemons-market','w-en-adverse-selection']),
 dict(id='money-laundering', title='洗钱', cat='其他',
  ol='非法所得通过复杂交易掩饰来源、使其看似合法的过程。',
  ov=('洗钱(money laundering) 是**非法掩饰非法所得来源**、'
   '并把资金转换为看似合法形式的过程（俗称"脏钱"）。'
   '典型环节包括：处置(placement，把现金注入金融体系)、'
   '分层(layering，通过多层交易模糊来源) 与整合(integration，以合法形式取回)。'
   '在金融危机语境中，洗钱的意义有三：'
   '①**银行体系的脆弱点**——反洗钱失效导致的罚款与声誉损失可危及机构生存；'
   '②**与资本管制/多重汇率的互动**——管制越严，地下跨境渠道越活跃（见 black-market）；'
   '③**危机后的监管强化**——FATF 标准与"去风险化"(de-risking) 影响新兴市场的代理行关系。'
   '相关国际标准由 FATF（见 fatf 条目）制定。具体机制与规模估计待核实。'),
  tl=[],
  causal=[('非法所得需掩饰来源 → 通过金融体系分层转移','w-en-money-laundering'),
         ('管制与多重汇率 → 地下跨境渠道扩张','w-en-black-market'),
         ('反洗钱标准强化 → 代理行关系收缩（去风险化）影响新兴市场','w-en-fatf')],
  schools=[('执法视角','强化反洗钱可切断犯罪资金链并提升金融体系完整性','w-en-money-laundering'),
           ('去风险化视角','过度合规使新兴市场失去代理行服务，反而推高非正规渠道','w-en-fatf')],
  srcs=['w-en-money-laundering','w-en-fatf']),
 dict(id='currency-war', title='货币战（竞争性贬值）', cat='货币',
  ol='各国竞相压低本币汇率以获取贸易优势，导致集体受损的"以邻为壑"局面。',
  ov=('货币战(currency war)，又称竞争性贬值(competitive devaluation)，'
   '指各国**竞相压低本币汇率以获取贸易优势**，最终形成**集体受损**的"以邻为壑"局面。'
   '机制是典型的囚徒困境：单国贬值可短期改善贸易收支（若满足马歇尔-勒纳条件），'
   '但对方随即跟进，结果是**各方汇率相对关系不变而全球贸易与信心受损**。'
   '历史案例包括1930年代金本位解体后的竞争性贬值'
   '（见 gold-bloc、tripartite-1936、beggar-thy-neighbour），'
   '以及2010年代关于"汇率操纵"的争论。'
   '该概念与"货币战争"的流行说法不同：学术讨论关注的是政策互动的博弈结构，'
   '而非某一国的阴谋。具体案例与实证待核实。'),
  tl=[],
  causal=[('单国贬值改善贸易收支 → 贸易伙伴受损','w-en-currency-war'),
         ('伙伴跟进贬值 → 相对汇率回到原位，全球贸易收缩','w-en-beggar-thy-neighbour'),
         ('协调（如三方协定）或浮动汇率 → 缓解竞争性贬值压力','w-en-tripartite-1936')],
  schools=[('博弈视角','竞争性贬值是囚徒困境，需国际协调','w-en-currency-war'),
           ('弹性视角','浮动汇率下汇率变动反映基本面，不应简单视为"战争"','w-en-floating-exchange-rate')],
  srcs=['w-en-currency-war','w-en-beggar-thy-neighbour']),
 dict(id='malinvestment', title='错误投资（奥地利学派）', cat='理论',
  ol='在人为压低利率造成的错误价格信号下，资本被配置到不可持续的长期项目。',
  ov=('错误投资(malinvestment) 是奥地利学派商业周期理论的核心概念：'
   '当**央行人为压低利率**、使其低于"自然利率"时，'
   '跨期价格信号被扭曲，企业家会把资本过度配置到**远离消费、回收期过长**的项目上。'
   '这些项目在真实的时间偏好下本不具可行性，因此当利率回升或信贷停止扩张时无法完成，'
   '表现为**危机的"清算"过程**（见 austrian-theory）。'
   '该概念与主流经济学的分歧在于：'
   '主流更强调需求冲击与金融摩擦，而非"利率信号扭曲导致的资本错配"；'
   '但2000年代的低利率与房地产/基建过度投资，使"错误投资"的说法获得部分共鸣。'
   '其难点在于**无法直接观测"正确"的资本结构**，只能事后判断。具体争论待核实。'),
  tl=[],
  causal=[('央行压低利率至自然利率以下 → 跨期价格信号扭曲','w-en-malinvestment'),
         ('资本涌入长期项目 → 资本结构偏离真实时间偏好','w-en-austrian-theory'),
         ('利率回升或信贷停止 → 项目无法完成，危机即清算','w-en-austrian-theory')],
  schools=[('奥地利学派视角','危机是错误投资的必要清算，救助会延长调整','w-en-austrian-theory'),
           ('主流视角','需求与金融摩擦才是主因，"错误投资"难以度量','w-en-keynesian-economics')],
  srcs=['w-en-malinvestment','w-en-austrian-theory']),
]

HAVE = {json.load(open(f, encoding='utf-8'))['title'] for f in glob.glob('data/entries/*.json')}
for sp in D:
    if sp['title'] in HAVE:
        print('跳过重复标题', sp['id'], sp['title']); continue
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': [],
        'schools': [{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[src]}
                    for h,v,src in sp['schools']],
        'policy_response': [], 'comparison': '',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])),
        'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体细节待核实。【续作DF】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r115.json', encoding='utf-8'))
MAP = {'fixed-exchange-rate':'w-en-fixed-exchange-rate','floating-exchange-rate':'w-en-floating-exchange-rate',
       'transition-economy':'w-en-transition-economy','lemons-market':'w-en-lemons-market',
       'money-laundering':'w-en-money-laundering','currency-war':'w-en-currency-war',
       'malinvestment':'w-en-malinvestment'}
for eid, sid in MAP.items():
    if sid in ex: continue
    v = meta.get(eid)
    if not v: print('meta缺', eid); continue
    sd['sources'].append({'id':sid,'title':v['title'],'author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+v['slug'],'url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia REST API核对(本会话抓取摘要)'})
    ex.add(sid); print('新增来源',sid,'|',v['title'])
sd['count']=len(sd['sources'])
json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':'重要','status':'written',
      'source_count':2,'needs_verification':1,'last_updated':'2026-11-24',
      'unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
