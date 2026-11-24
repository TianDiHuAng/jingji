# -*- coding: utf-8 -*-
"""续作DD：新增4条(欧洲央行/熔断机制/商品价格指数/市政债券)并修正引用。"""
import json, glob

def svg(t, labels):
    e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：要点</text>"]
    for x, lb in zip([20,270,520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)

D = [
 dict(id='european-central-bank', title='欧洲中央银行(ECB)', cat='制度', region='欧洲',
  ol='欧元体系与欧洲中央银行体系的核心，也是欧盟七个机构之一；在欧债危机中成为关键行动者。',
  ov=('欧洲中央银行(ECB) 是**欧元体系(Eurosystem) 与欧洲中央银行体系(ESCB) 的核心组成部分**，'
   '同时也是**欧盟的七个机构之一**。'
   '其制度特殊性在于：欧元区有统一货币但**没有统一财政**，'
   '因此 ECB 在危机中被迫承担远超常规央行的角色。'
   '在2010—2012年欧债危机中，ECB 的应对（长期再融资操作、证券市场计划、'
   '以及"不惜一切代价"的OMT承诺）被视为稳定市场的关键；'
   '但这些操作也引发争议：是否越过了"禁止货币融资"的界限、'
   '以及货币政策是否被迫承担了本应由财政承担的责任（见 fiscal-dominance）。'
   'ECB 的治理结构（执委会＋各成员国央行行长组成的理事会）也带来决策复杂性与国别利益冲突。'
   '具体工具与法律争议待核实。'),
  tl=[
   {'year':1999,'display':'1999年','event':'欧元启动，ECB 开始运作（年份待核实）','sources':['w-en-european-central-bank']},
   {'year':2012,'display':'2012年','event':'OMT承诺"不惜一切代价"稳定欧元区（细节待核实）','sources':['w-en-eurozone-crisis']},
  ],
  causal=[('统一货币 + 分散财政 → 缺乏跨国财政调整机制','w-en-eurozone-crisis'),
         ('危机中主权利差飙升 → ECB 以非常规工具介入','w-en-european-central-bank'),
         ('介入引发"货币融资"与"财政主导"争议','w-en-fiscal-dominance')],
  schools=[('必要性视角','在财政缺位时，央行介入是防止欧元区解体的唯一现实手段','w-en-european-central-bank'),
           ('纪律视角','非常规操作模糊了货币与财政边界，助长道德风险','w-en-fiscal-dominance')],
  srcs=['w-en-european-central-bank','w-en-eurozone-crisis']),
 dict(id='circuit-breaker', title='熔断机制（交易限制）', cat='制度', region='全球',
  ol='交易所为防股灾实施的价格限制或暂停交易工具，1987年股灾后在美国等市场引入。',
  ov=('熔断机制（trading curb，又称 circuit breaker）是**相关交易所为防范股市崩盘而实施的金融监管工具**。'
   '其形式包括：按价格波动幅度触发**短暂暂停交易**（如美国的三级熔断）、'
   '个股层面的限价区间（limit up/limit down）与收盘集合竞价等。'
   '该机制在 **1987 年黑色星期一**（见 black-monday-1987）之后被广泛引入，'
   '目的是给市场参与者时间消化信息、防止程序化抛售的自我强化。'
   '自设立以来，熔断规则被多次修改——'
   '这本身反映了争议：**熔断可能在暂停后引发更集中的抛售**（"磁吸效应"），'
   '也可能干扰价格发现、损害流动性。'
   '2016年1月中国实施熔断后数日即暂停，即为争议的典型案例。'
   '该机制是"用行政手段打断顺周期放大"的代表性工具。具体规则待核实。'),
  tl=[
   {'year':1987,'display':'1987年后','event':'黑色星期一股灾后，熔断机制在美国等市场引入','sources':['w-en-black-monday-1987']},
  ],
  causal=[('程序化抛售与流动性不足 → 单日暴跌（1987年-22.6%）','w-en-black-monday-1987'),
         ('以价格限制或暂停交易打断抛售 → 给市场消化信息的时间','w-en-trading-curb'),
         ('副作用：磁吸效应与价格发现受损 → 规则反复修改','w-en-trading-curb')],
  schools=[('稳定视角','熔断可阻断恐慌性抛售的自我强化','w-en-trading-curb'),
           ('副作用视角','暂停交易可能集中抛压、干扰价格发现','w-en-black-monday-1987')],
  srcs=['w-en-trading-curb','w-en-black-monday-1987']),
 dict(id='commodity-price-index', title='商品价格指数与商品周期', cat='理论', region='全球',
  ol='以选定商品价格构成的固定权重指数，用于刻画大宗商品的总体价格走势与周期。',
  ov=('商品价格指数(commodity price index) 是**以选定商品价格构成的固定权重指数或加权平均值**，'
   '可基于现货或期货价格，设计目的是**代表广义商品市场**的价格走势。'
   '它在危机分析中的用途有三：'
   '①**判断冲击性质**——商品价格骤变可区分供给侧冲击（如1973年石油禁运）'
   '与需求侧衰退；'
   '②**识别商品周期**——资源出口国的财政与汇率往往随商品周期剧烈波动'
   '（见 dutch-disease、resource-curse）；'
   '③**预警通胀**——商品价格常领先于消费物价。'
   '商品周期的下行对资源依赖型经济体具有系统性影响：'
   '安哥拉、尼日利亚、委内瑞拉、俄罗斯的危机都与商品价格回落直接相关。'
   '具体指数编制与权重待核实。'),
  tl=[],
  causal=[('全球需求与供给冲击 → 商品价格总体波动','w-en-commodity-price-index'),
         ('资源出口国财政与汇率随商品周期放大波动','w-en-dutch-disease'),
         ('价格下行 → 外汇与财政双重恶化，触发危机','w-en-angola-econ')],
  schools=[('周期视角','商品价格具有长周期，资源国需以财政规则对冲','w-en-commodity-price-index'),
           ('结构视角','资源依赖本身（而非价格波动）才是脆弱性根源','w-en-resource-curse')],
  srcs=['w-en-commodity-price-index','w-en-resource-curse']),
 dict(id='municipal-bond', title='市政债券与地方政府债务', cat='制度', region='全球',
  ol='由州或地方政府及其设立的机构发行的债券；地方政府债务危机的重要载体。',
  ov=('市政债券(municipal bond) 是由**州或地方政府、或其设立的机构（如各类管理局与特区）发行的债券**。'
   '在美国，市政债券持有人的利息收入通常享受税收优惠，这使其成为地方政府的主要融资工具。'
   '在危机语境中，市政债券是**地方政府债务危机**的主要载体：'
   '当税基萎缩而支出刚性时，地方政府只能以发债弥补，'
   '最终可能面临再融资中断（如纽约市1975年、见 nyc-fiscal-1975；'
   '波多黎各2014年、见 puerto-rico-debt-2014）。'
   '地方政府的特殊脆弱性在于：'
   '它们**没有货币与汇率工具**、不能像主权国家那样重组外债、'
   '且财政收入对本地经济周期高度敏感。'
   '中国的"地方政府融资平台"债务在功能上类似，但制度与法律框架不同（见 china-realestate-2020）。'
   '具体制度差异待核实。'),
  tl=[
   {'year':1975,'display':'1975年','event':'纽约市财政危机：累积债务140亿美元、被拒于信贷市场之外','sources':['w-en-nyc-fiscal-1975']},
   {'year':2014,'display':'2014年','event':'波多黎各债务危机爆发（见 puerto-rico-debt-2014）','sources':['w-en-puerto-rican-debt-crisis']},
  ],
  causal=[('税基萎缩 + 支出刚性 → 以发债弥补赤字','w-en-municipal-bond'),
         ('债务累积 + 评级下调 → 再融资渠道关闭','w-en-nyc-fiscal-1975'),
         ('无货币工具、不能重组外债 → 需上级政府或专门框架介入','w-en-puerto-rican-debt-crisis')],
  schools=[('财政纪律视角','地方政府应受平衡预算约束，避免以债务掩盖结构赤字','w-en-municipal-bond'),
           ('周期视角','衰退期强制平衡会加剧顺周期紧缩，需中央转移支付','w-en-nyc-fiscal-1975')],
  srcs=['w-en-municipal-bond','w-en-nyc-fiscal-1975']),
]

HAVE = {json.load(open(f, encoding='utf-8'))['title'] for f in glob.glob('data/entries/*.json')}
for sp in D:
    if sp['title'] in HAVE:
        print('跳过重复标题', sp['id'], sp['title']); continue
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': [],
        'schools': [{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[src]}
                    for h,v,src in sp['schools']],
        'policy_response': [], 'comparison': '',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基摘要与标准口径；具体细节待核实。【续作DD】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r114.json', encoding='utf-8'))
MAP = {'european-central-bank':'w-en-european-central-bank','circuit-breaker':'w-en-trading-curb',
       'commodity-price-index':'w-en-commodity-price-index','municipal-bond':'w-en-municipal-bond'}
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
      'unit':'U6 理论与制度','period':'理论制度','region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
