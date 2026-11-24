# -*- coding: utf-8 -*-
"""续作CJ：新增安哥拉宽扎贬值、赞比亚克瓦查改革(非洲×货币)与新西兰房地产泡沫(大洋洲×泡沫)。"""
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
 dict(id='angolan-kwanza-devaluation', title='安哥拉宽扎贬值与货币更替', cat='货币',
  unit='U5 21世纪', period='21世纪', region='非洲', tier='补充',
  ol='安哥拉宽扎自独立以来经历多次更替与大幅贬值，2023年5—6月对美元贬值近40%至825宽扎。',
  ov=('安哥拉宽扎(Kz) 在安哥拉独立后引入，平价替代了此前的埃斯库多，并细分为100 lwei。'
   '该货币此后经历多次更替与大幅贬值：'
   '**2023年5月至6月，宽扎对美元贬值近40%，创下825宽扎兑1美元的历史低点**。'
   '安哥拉作为高度依赖石油出口的经济体（2017年石油占出口价值90%以上），'
   '油价与产量波动直接决定外汇收入，进而决定汇率压力（见 angola-oil-dependence）。'
   '历史上安哥拉曾多次更换货币单位（kwanza→new kwanza→kwanza reajustado→现行宽扎），'
   '这与长期通胀与计价单位过小有关（参见 redenomination）。具体更替年份待核实。'),
  tl=[
    {'year':1977,'display':'1977年','event':'第一次宽扎(AOK)引入，平价替代埃斯库多','sources':['w-en-angolan-kwanza']},
    {'year':2023,'display':'2023年5—6月','event':'宽扎对美元贬值近40%，创825宽扎/美元低点','sources':['w-en-angolan-kwanza']},
  ],
  causal=[('石油出口收入波动 → 外汇供给与财政同步恶化','w-en-angolan-econ'),
         ('汇率承压 → 宽扎大幅贬值（2023年5—6月近40%）','w-en-angolan-kwanza'),
         ('长期通胀与计价单位过小 → 多次更替货币单位','w-en-angolan-kwanza')],
  schools=[{'holder':'资源依赖视角','view':'石油单一依赖使汇率成为油价冲击的传导器','basis':'据出口结构归纳','sources':['w-en-angola-econ']},
           {'holder':'货币更替视角','view':'更换货币单位不能替代宏观稳定，否则通胀在新单位下延续','basis':'据多次更替史归纳；因果待核实','sources':['w-en-redenomination']}],
  kd=[
    {'label':'宽扎单月贬值幅度(2023年5—6月)','value':-40,'unit':'%（近40%）','year':2023,'comparable_price':False,
     'note':'原文：The currency suffered a devaluation of nearly 40% against the US dollar between May and June 2023；单一来源待核实。','sources':['w-en-angolan-kwanza']},
    {'label':'宽扎汇率低点(2023)','value':825,'unit':'宽扎/美元（纪录低点）','year':2023,'comparable_price':False,
     'note':'原文：to a record low of 825 kwanzas to the US dollar；单一来源待核实。','sources':['w-en-angolan-kwanza']},
  ],
  cmp='与尼日利亚、委内瑞拉等石油依赖经济体同型：油价冲击→外汇短缺→贬值。具体异同待核实。'),
 dict(id='zambian-kwacha-reform', title='赞比亚克瓦查重定面值(2013)', cat='货币',
  unit='U5 21世纪', period='21世纪', region='非洲', tier='补充',
  ol='赞比亚2013年以重定面值更换克瓦查，收回3.7万亿旧钞（占流通95.3%）。',
  ov=('赞比亚克瓦查(ZMW) 是赞比亚的官方货币，由赞比亚银行发行，细分为100 ngwee。'
   '2013年，赞比亚实施货币重定面值：**到2013年6月26日，赞比亚银行已收回3.7万亿旧克瓦查纸币，'
   '约占流通中纸币的95.3%**；相关改革使克瓦查的金标准降低 **7.8%**。'
   '重定面值是通胀后计价单位过小的应对（参见 redenomination 条目），本身不改变对外汇率，'
   '但需要配套的财政与货币纪律才能维持币值。'
   '2025年3月31日，赞比亚银行又推出"Heritage Series"新版系列（六种纸币与六种硬币）。具体细节待核实。'),
  tl=[
    {'year':2013,'display':'2013年6月26日','event':'赞比亚银行已收回3.7万亿旧克瓦查纸币（占流通95.3%）','sources':['w-en-zambian-kwacha']},
    {'year':2025,'display':'2025年3月31日','event':'发行"Heritage Series"新版纸币与硬币','sources':['w-en-zambian-kwacha']},
  ],
  causal=[('长期通胀使旧克瓦查计价单位过小 → 需重定面值','w-en-redenomination'),
         ('以新币替换旧币 → 至2013年6月收回3.7万亿旧钞（占流通95.3%）','w-en-zambian-kwacha'),
         ('改革使克瓦查金标准降低7.8% → 若无纪律配套，贬值压力延续','w-en-zambian-kwacha')],
  schools=[{'holder':'技术视角','view':'重定面值仅为计价单位调整，属象征性','basis':'据定义与该案例归纳','sources':['w-en-redenomination']},
           {'holder':'配套视角','view':'需与财政货币纪律结合才能稳定币值','basis':'据多国经验归纳；因果待核实','sources':['w-en-zambian-kwacha']}],
  kd=[
    {'label':'收回旧钞规模(至2013-06-26)','value':3.7,'unit':'万亿克瓦查（占流通95.3%）','year':2013,'comparable_price':False,
     'note':'原文：the Bank of Zambia managed to withdraw 3.7 trillion Kwacha in old banknotes, accumulating to about 95.3% of the circulating banknotes；单一来源待核实。','sources':['w-en-zambian-kwacha']},
    {'label':'改革后克瓦查金标准下调','value':-7.8,'unit':'%','year':2013,'comparable_price':False,
     'note':'原文：These reforms resulted in a reduction of the kwacha\'s gold standard by 7.8%；单一来源待核实。','sources':['w-en-zambian-kwacha']},
  ],
  cmp='与津巴布韦、安哥拉等多次更替货币的非洲经济体同类；赞比亚案例的特殊性在于回收率数据较为完整。具体异同待核实。'),
 dict(id='nz-property-bubble', title='新西兰房地产泡沫(1990s–)', cat='泡沫',
  unit='U5 21世纪', period='21世纪', region='大洋洲', tier='重要',
  ol='新西兰房价自1990年代初以来远超收入增长，2002—2008年实际涨80%，住房自有率由74%降至65%。',
  ov=('新西兰的房地产泡沫是该国重大的经济与社会议题。'
   '自1990年代初以来，新西兰房价上涨速度远超收入，使公共住房供给方压力上升、'
   '能通过私人市场获得住房的家庭减少。'
   '规模上：**2002至2008年间，全国房价实际上涨80%**；部分区域出现过约 **9%** 的（回调）幅度——尽管是从极高水平回落。'
   '社会后果显著：**1986至2013年，住房自有率由74%降至65%**，'
   '并被认为加剧了收入不平等（新西兰现为发达国家中不平等程度较高者之一）。'
   '政策与制度的角色受关注：有分析认为1970年代某法案使1977—2018年间人口每增长1%推高房价约2%，'
   '而此前仅约0.5%。'
   '此外，1987年股灾中 NZSE 指数自峰值下跌约 **60%**，恢复所需时间也长于多数发达市场。具体数据待核实。'),
  tl=[
    {'year':1987,'display':'1987年','event':'NZSE 指数自峰值下跌约60%（黑色星期一）','sources':['w-en-new-zealand-property-bubble']},
    {'year':2008,'display':'2002—2008年','event':'全国房价实际上涨80%','sources':['w-en-new-zealand-property-bubble']},
    {'year':2013,'display':'1986—2013年','event':'住房自有率由74%降至65%','sources':['w-en-new-zealand-property-bubble']},
  ],
  causal=[('长期低利率、移民流入与土地/规划约束 → 住房供给弹性不足','w-en-new-zealand-property-bubble'),
         ('信贷扩张推动房价远超收入（2002—2008实际+80%）→ 住房自有率下降（74%→65%）','w-en-new-zealand-property-bubble'),
         ('财富与债务集中于房地产 → 加剧不平等并放大金融体系对房价的敏感度','w-en-new-zealand-property-bubble')],
  schools=[{'holder':'供给约束视角','view':'规划与土地供给限制是房价长期偏高的主因','basis':'据人口与房价弹性测算归纳；因果待核实','sources':['w-en-new-zealand-property-bubble']},
           {'holder':'信贷与利率视角','view':'低利率与信贷扩张放大了需求端','basis':'据房价与信贷周期归纳','sources':['w-en-new-zealand-property-bubble']}],
  kd=[
    {'label':'新西兰房价实际上涨(2002—2008)','value':80,'unit':'%（实际值）','year':2008,'comparable_price':True,
     'note':'原文：Nationwide, property prices increased 80% in real terms between 2002 and 2008；单一来源待核实。','sources':['w-en-new-zealand-property-bubble']},
    {'label':'住房自有率(1986)','value':74,'unit':'%','year':1986,'comparable_price':False,
     'note':'原文：Between 1986 and 2013, home ownership dropped from 74% to 65%；单一来源待核实。','sources':['w-en-new-zealand-property-bubble']},
    {'label':'住房自有率(2013)','value':65,'unit':'%','year':2013,'comparable_price':False,
     'note':'原文：home ownership dropped from 74% to 65%；单一来源待核实。','sources':['w-en-new-zealand-property-bubble']},
    {'label':'NZSE指数自峰值跌幅(1987)','value':-60,'unit':'%（约）','year':1987,'comparable_price':False,
     'note':'原文：The NZSE dropped around 60% from its peak；单一来源待核实。','sources':['w-en-new-zealand-property-bubble']},
  ],
  cmp=('与澳大利亚、加拿大等移民型经济体房价长期偏高相似；但新西兰的住房自有率下降与不平等恶化证据更完整。'
   '与日本1990年泡沫不同，新西兰房价未曾出现同等量级的崩跌。具体异同待核实。')),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sorted(sp['tl'], key=lambda t:t.get('year',0)),
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': sp['kd'], 'schools': sp['schools'],
        'policy_response': [{'holder':'政策当局','view':'应对措施与效果待核实','basis':'需多来源印证',
                            'sources':[sp['causal'][0][1]]}],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st,s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基全文；单源待核实。【续作CJ】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r89_data.json', encoding='utf-8'))
for sid, key in [('w-en-angolan-kwanza','angolan-kwanza'), ('w-en-zambian-kwacha','zambian-kwacha'),
                 ('w-en-new-zealand-property-bubble','nz-property-bubble')]:
    if sid in ex: continue
    v = meta.get(key, {}); t = v.get('title')
    if not t: continue
    sd['sources'].append({'id':sid,'title':t,'author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+t.replace(' ','_'),'url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia API(full extract)核对(本会话抓取)'})
    ex.add(sid); print('新增来源', sid, '|', t)
sd['count']=len(sd['sources'])
json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':sp['tier'],'status':'written',
      'source_count':len(sp['causal']),'needs_verification':1,'last_updated':'2026-11-24',
      'unit':sp['unit'],'period':sp['period'],'region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
