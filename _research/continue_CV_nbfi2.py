# -*- coding: utf-8 -*-
"""续作CV：新增Archegos爆仓(2021)与英国LDI危机(2022)——两类非银行金融机构危机。"""
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
 dict(id='archegos-2021', title='Archegos 爆仓(2021)', cat='银行',
  region='北美', tier='重要',
  ol='家族办公室以总收益互换隐藏高杠杆集中持仓，2021年3月保证金违约引发多家投行巨额损失。',
  ov=('Archegos Capital Management 是一家有限合伙形式的**家族办公室**，管理 Bill Hwang 的个人资产，'
   '一度管理超过 **360亿美元**。**2024年11月，Hwang 因联邦欺诈与敲诈勒索指控被判处18年监禁**。'
   '崩盘过程：**2021年3月26日**，Archegos 对多家全球投资银行的追加保证金通知违约，'
   '包括瑞信(Credit Suisse)、野村(Nomura) 等。'
   '其**衍生品合约"在交易恶化时使公司暴露于严重损失"**；'
   '据《华尔街日报》报道，**Hwang 在10天内损失了80亿美元**。'
   '强制平仓冲击了市场：据报道，这笔抛售被认为是 **ViacomCBS 股价暴跌27%** 的原因，Discovery 也出现类似跌幅。'
   '背景：Hwang 原属"老虎幼崽"基金 Tiger Asia Management，2013年设立 Archegos 家族办公室，'
   '**2020年管理规模为100亿美元**；Tiger Asia 曾于2012年对中资银行股票内幕交易认罪并支付 **4400万美元** 罚金。'
   '该案例的关键教训在于**披露与杠杆的不透明**：通过总收益互换(TRS)，'
   '家族办公室能在不触发大额持仓披露的情况下，对多家银行同时维持巨额集中敞口——'
   '每家银行只看到自己那一部分，无人看到全貌。具体规模与时序待核实。'),
  tl=[
   {'year':2012,'display':'2012年','event':'Tiger Asia 就中资银行股票内幕交易认罪，罚金4400万美元','sources':['w-en-archegos']},
   {'year':2013,'display':'2013年','event':'Hwang 设立 Archegos 家族办公室','sources':['w-en-archegos']},
   {'year':2021,'display':'2021年3月26日','event':'对多家投行追加保证金违约；10天内损失80亿美元','sources':['w-en-archegos']},
   {'year':2024,'display':'2024年11月','event':'Hwang 因欺诈与敲诈勒索被判18年监禁','sources':['w-en-archegos']},
  ],
  causal=[('以总收益互换(TRS)建立跨多家银行的大额集中敞口 → 各银行只见局部、无人见全貌','w-en-archegos'),
         ('标的股价下跌触发追加保证金 → 2021年3月26日违约','w-en-archegos'),
         ('银行强制平仓 → 相关股票暴跌（ViacomCBS -27%），投行承担巨额损失','w-en-archegos')],
  schools=[{'holder':'披露缺口视角','view':'衍生品敞口不透明使风险在多家机构间叠加而无人可见','basis':'据TRS安排与损失分布归纳','sources':['w-en-archegos']},
           {'holder':'杠杆视角','view':'家族办公室缺乏资本与流动性约束，可承受极高杠杆','basis':'据10天损失80亿归纳；因果待核实','sources':['w-en-archegos']}],
  kd=[
   {'label':'Archegos 管理资产峰值','value':36,'unit':'十亿美元（超360亿）','year':2021,'comparable_price':False,
    'note':'原文：at one time managing over $36 billion in assets；单一来源待核实。','sources':['w-en-archegos']},
   {'label':'Hwang 10天内损失','value':8,'unit':'十亿美元（80亿）','year':2021,'comparable_price':False,
    'note':'原文：The Wall Street Journal reported that Hwang lost $8 billion in 10 days；单一来源待核实。','sources':['w-en-archegos']},
   {'label':'管理规模(2020)','value':10,'unit':'十亿美元（100亿）','year':2020,'comparable_price':False,
    'note':'原文：Hwang created the Archegos family office in 2013, with $10 billion under management as of 2020；单一来源待核实。','sources':['w-en-archegos']},
   {'label':'Hwang 刑期','value':18,'unit':'年（2024年11月判决）','year':2024,'comparable_price':False,
    'note':'原文：In November 2024, Hwang was sentenced to 18 years in prison on federal charges of fraud and racketeering；单一来源待核实。','sources':['w-en-archegos']},
   {'label':'ViacomCBS 因强制平仓的跌幅','value':-27,'unit':'%','year':2021,'comparable_price':False,
    'note':'原文：reported to be the cause of a 27% plunge in share price of ViacomCBS；单一来源待核实。','sources':['w-en-archegos']},
  ],
  cmp=('与LTCM(1998，见 ltcm)同属"高杠杆＋不透明＋多家银行对手方"的组合，但规模来源不同：'
   'LTCM 是基金＋模型失效，Archegos 是家族办公室＋衍生品隐藏持仓。'
   '2023年瑞信之倒闭与其在Archegos与Greensill上的损失直接相关。具体异同待核实。')),
 dict(id='uk-ldi-crisis-2022', title='英国LDI危机(2022)', cat='制度',
  region='欧洲', tier='重要',
  ol='养老金LDI策略的利率对冲在国债收益率飙升时触发追加抵押，被迫抛售金边债形成自我强化下跌。',
  ov=('2022年英国"迷你预算"后，国债（金边债）收益率飙升，触发了以**负债驱动投资**(LDI) 为核心的养老金体系危机。'
   'LDI 是一种**资产负债管理方法**：围绕已知负债的规模、时点与风险特征来设计资产组合，'
   '被固定收益养老金计划与保险公司用于降低融资波动、确保到期有现金支付；'
   '其技术包括**现金流匹配与久期匹配**，并常使用利率互换等衍生品加杠杆对冲。'
   '危机机制是**抵押品螺旋**：收益率上升 → 互换头寸亏损 → 需追加抵押品 → 只能抛售金边债 → 价格进一步下跌、收益率再升。'
   '英格兰银行介入临时购债，据其演讲披露最终在操作中买入 **193亿英镑** 金边债。'
   '后续基于逐笔交易数据的研究发现：LDI 基金的被迫抛售在峰值造成约 **7%—10%** 的价格折价；'
   '池化(pooled)LDI 基金额外卖出了约 **13个百分点** 的金边债持仓，折价在10月底前收窄。'
   '该案例是"**非银行金融机构＋杠杆＋抵押品**"型危机的教科书样本，'
   '也说明养老金的"安全资产"策略在利率急变时可成为系统性风险源。具体数据待核实。'),
  tl=[
   {'year':2022,'display':'2022年9—10月','event':'"迷你预算"后金边债收益率飙升，LDI触发追加抵押与被迫抛售','sources':['w-en-ldi']},
   {'year':2022,'display':'2022年10月','event':'英格兰银行临时购债，累计买入193亿英镑金边债；折价在10月底前收窄','sources':['w-en-ldi']},
  ],
  causal=[('LDI 以利率互换等衍生品对冲久期 → 隐含杠杆','w-en-ldi'),
         ('国债收益率飙升 → 互换亏损、追加抵押 → 被迫抛售金边债','w-en-ldi'),
         ('抛售压低价格、推高收益率 → 自我强化的抵押品螺旋（峰值折价7%—10%）','w-en-ldi')],
  schools=[{'holder':'抵押品螺旋视角','view':'杠杆化对冲在利率急变时产生顺周期抛售，是危机核心','basis':'据折价与抛售数据归纳','sources':['w-en-ldi']},
           {'holder':'监管缺口视角','view':'养老金此前未被作为系统性风险来源监管，杠杆与流动性错配未被充分覆盖','basis':'据事后研究归纳；因果待核实','sources':['w-en-ldi']}],
  kd=[
   {'label':'英格兰银行临时购债规模','value':19.3,'unit':'十亿英镑（193亿）','year':2022,'comparable_price':False,
    'note':'原文：A Bank of England speech reported that the Bank ultimately bought £19.3 billion of gilts during the operation；单一来源待核实。','sources':['w-en-ldi']},
   {'label':'LDI抛售造成的价格折价(峰值，下界)','value':7,'unit':'%（7%—10%区间下界）','year':2022,'comparable_price':False,
    'note':'原文：forced sales by LDI funds created price discounts on the order of 7% to 10% at the peak；单一来源待核实。','sources':['w-en-ldi']},
   {'label':'LDI抛售造成的价格折价(峰值，上界)','value':10,'unit':'%（区间上界）','year':2022,'comparable_price':False,
    'note':'原文：on the order of 7% to 10% at the peak；单一来源待核实。','sources':['w-en-ldi']},
   {'label':'池化LDI基金额外卖出的金边债持仓','value':13,'unit':'百分点（约）','year':2022,'comparable_price':False,
    'note':'原文：pooled funds sold roughly 13 percentage points more of their gilt holdings；单一来源待核实。','sources':['w-en-ldi']},
  ],
  cmp=('与2020年3月美国国债市场动荡、2023年硅谷银行（持有至到期债券的利率风险）机制同源：'
   '**利率急变 → 抵押品/资产价格下跌 → 被迫抛售 → 进一步下跌**。'
   '区别在于本次主体是养老金而非银行，且杠杆通过衍生品而非存款融资实现。具体异同待核实。')),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': 'U5 21世纪', 'period': '21世纪', 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sorted(sp['tl'], key=lambda t:t.get('year',0)),
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': sp['kd'],
        'schools': sp['schools'],
        'policy_response': [],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st,s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基全文；单源待核实。【续作CV】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r109_data.json', encoding='utf-8'))
for sid, key in [('w-en-archegos','archegos'), ('w-en-ldi','ldi')]:
    if sid in ex: continue
    v = meta.get(key)
    if not v: continue
    sd['sources'].append({'id':sid,'title':v['title'],'author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+v['title'].replace(' ','_'),'url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia API(full extract)核对(本会话抓取)'})
    ex.add(sid); print('新增来源',sid,'|',v['title'])
sd['count']=len(sd['sources'])
json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':sp['tier'],'status':'written',
      'source_count':1,'needs_verification':1,'last_updated':'2026-11-24',
      'unit':'U5 21世纪','period':'21世纪','region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
