# -*- coding: utf-8 -*-
"""续作CK：新增伊朗经济危机(中东×恶性通胀)与叙利亚镑贬值。"""
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
 dict(id='iranian-economic-crisis', title='伊朗经济危机与高通胀(2018–)', cat='恶性通胀',
  unit='U5 21世纪', period='21世纪', region='中东', tier='重要',
  ol='制裁、石油依赖与汇率贬值叠加，伊朗年通胀达88.6%—200%，为半个世纪以来全球最高。',
  ov=('伊朗经济危机是制裁、石油依赖与宏观管理失衡叠加的结果。'
   '伊朗财政高度依赖油气：例如 **2009财年，油气部门占政府预算的60%**。'
   '制裁压缩石油出口与外汇收入后，里亚尔大幅贬值、进口成本飙升，通胀迅速攀升——'
   '据伊朗统计组织报告，年通胀率达 **88.6%至200%**，为**半个世纪以来全球最高**。'
   '民生冲击显著：基本商品价格涨幅高达 **400%**（例如鸡蛋由每枚70,000里亚尔涨至200,000，约三倍）；'
   '实际最低工资降至每月不足 **100美元**，家庭食品支出占比常达 **70%**；'
   '2024年劳工与社会福利部报告称 **57%** 的人口存在营养不良。'
   '**口径提示**：上述为年通胀率。是否达到 Cagan 式恶性通胀的严格标准（月率>50%、年率约>13,000%）尚有争议，'
   '本条目按"高通胀/接近恶性通胀"处理，具体界定待核实。'),
  tl=[
    {'year':2009,'display':'2009财年','event':'油气部门占政府预算60%','sources':['w-en-iranian-economic-crisis']},
    {'year':2018,'display':'2018年起','event':'制裁强化，里亚尔贬值、通胀攀升（细节待核实）','sources':['w-en-iranian-economic-crisis']},
    {'year':2024,'display':'2024年','event':'57%人口营养不良；基本商品涨幅达400%','sources':['w-en-iranian-economic-crisis']},
  ],
  causal=[('制裁压缩石油出口与外汇收入 → 里亚尔贬值、进口成本上升','w-en-iranian-economic-crisis'),
         ('油气占预算60%的财政结构 → 收入冲击直接转为赤字与货币扩张','w-en-iranian-economic-crisis'),
         ('年通胀88.6%—200%、基本商品涨400% → 实际工资与营养状况恶化','w-en-iranian-economic-crisis')],
  schools=[{'holder':'制裁-汇率视角','view':'外部制裁通过汇率与进口成本传导为通胀','basis':'据通胀与汇率数据归纳','sources':['w-en-iranian-economic-crisis']},
           {'holder':'财政结构视角','view':'石油依赖使财政对油价与出口冲击极度敏感','basis':'据油气占预算60%归纳','sources':['w-en-iranian-economic-crisis']}],
  kd=[
    {'label':'伊朗年通胀率(下限)','value':88.6,'unit':'%','year':2023,'comparable_price':False,
     'note':'原文：Iran\'s Statistics Organization reported an annual inflation rate between 88.6% and 200%；单一来源待核实。','sources':['w-en-iranian-economic-crisis']},
    {'label':'伊朗年通胀率(上限)','value':200,'unit':'%（半个世纪以来全球最高）','year':2023,'comparable_price':False,
     'note':'原文：between 88.6% and 200%—the highest recorded globally in half a century；单一来源待核实。','sources':['w-en-iranian-economic-crisis']},
    {'label':'油气占政府预算比重(2009财年)','value':60,'unit':'%','year':2009,'comparable_price':False,
     'note':'原文：During the 2009 fiscal year ... the oil and gas sector accounted for 60% of the government\'s budget；单一来源待核实。','sources':['w-en-iranian-economic-crisis']},
    {'label':'基本商品价格涨幅','value':400,'unit':'%（高达；鸡蛋由70,000涨至200,000里亚尔/枚）','year':2024,'comparable_price':False,
     'note':'原文：Basic goods saw price increases of up to 400%; the cost of eggs ... tripled from 70,000 to 200,000 rials each；单一来源待核实。','sources':['w-en-iranian-economic-crisis']},
    {'label':'营养不良人口比例(2024)','value':57,'unit':'%','year':2024,'comparable_price':False,
     'note':'原文：In 2024, the Ministry ... reported that 57% of the population suffered from malnourishment；单一来源待核实。','sources':['w-en-iranian-economic-crisis']},
  ],
  cmp=('与委内瑞拉、津巴布韦等恶性通胀相比，伊朗的通胀尚未进入"月率>50%"的极端区间，'
   '但持续时间长、制裁为外生约束，性质更接近"长期高通胀+货币贬值"。具体界定待核实。')),
 dict(id='syrian-pound-crisis', title='叙利亚镑贬值与汇率分裂(2011–)', cat='货币',
  unit='U5 21世纪', period='21世纪', region='中东', tier='补充',
  ol='叙利亚镑自2011年战争爆发后大幅贬值，官方与市场汇率分化，2017年已达515镑/美元。',
  ov=('叙利亚镑(SYP) 是叙利亚的官方货币，由叙利亚中央银行发行，名义上分为100皮阿斯特，目前仅发行纸币。'
   '历史上其汇率长期稳定：1947年之前与（某货币挂钩）；对美元汇率 LS 2.19148 = US$1 的平价一直维持到 **1961年**。'
   '2000年代初常见汇率约为 LS 50 = US$1；2005年12月5日商业叙利亚银行报价为 LS 48.4 = US$1。'
   '2011年3月内战爆发前为 LS 47 = US$1，到 **2017年7月已贬至 LS 515 = US$1**。'
   '战时经济下官方汇率与黑市汇率严重分化，外汇短缺、制裁与产出崩溃使货币持续承压。'
   '2025年前后叙利亚政权更迭后，货币安排与汇率统一问题成为重建议题之一（细节待核实）。'),
  tl=[
    {'year':1961,'display':'至1961年','event':'对美元平价 LS 2.19148 = US$1 维持至此','sources':['w-en-syrian-pound']},
    {'year':2005,'display':'2005年12月5日','event':'商业叙利亚银行卖出价 LS 48.4 = US$1','sources':['w-en-syrian-pound']},
    {'year':2011,'display':'2011年3月','event':'内战爆发前 LS 47 = US$1','sources':['w-en-syrian-pound']},
    {'year':2017,'display':'2017年7月','event':'贬至 LS 515 = US$1','sources':['w-en-syrian-pound']},
  ],
  causal=[('内战爆发 → 产出崩溃、外汇收入锐减与制裁','w-en-syrian-pound'),
         ('外汇短缺 + 财政货币化 → 里亚尔（镑）持续贬值','w-en-syrian-pound'),
         ('官方与黑市汇率分化 → 多重汇率、支付与物价区域化','w-en-yemeni-rial')],
  schools=[{'holder':'战争经济视角','view':'汇率贬值是产出崩溃与外汇短缺的直接反映','basis':'据汇率数据归纳','sources':['w-en-syrian-pound']},
           {'holder':'多重汇率视角','view':'官方与市场汇率分化本身会扭曲资源配置并滋生寻租','basis':'据多重汇率通行分析归纳','sources':['w-en-yemeni-rial']}],
  kd=[
    {'label':'叙利亚镑汇率(2011-03)','value':47,'unit':'镑/美元','year':2011,'comparable_price':False,
     'note':'原文：It was LS 47 = US$1 in March 2011 and LS 515 in July 2017；单一来源待核实。','sources':['w-en-syrian-pound']},
    {'label':'叙利亚镑汇率(2017-07)','value':515,'unit':'镑/美元','year':2017,'comparable_price':False,
     'note':'原文：LS 515 in July 2017；单一来源待核实。','sources':['w-en-syrian-pound']},
    {'label':'叙利亚镑汇率(2005-12-05)','value':48.4,'unit':'镑/美元（商业叙利亚银行卖出价）','year':2005,'comparable_price':False,
     'note':'原文：On 5 December 2005, the selling rate quoted by the Commercial Bank of Syria was LS 48.4 = US$1；单一来源待核实。','sources':['w-en-syrian-pound']},
  ],
  cmp='与也门里亚尔(内战致货币分裂)、黎巴嫩镑(多重汇率)同属"战时/危机中的多重汇率"样本。具体异同待核实。'),
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
        'pending_notes': 'L2：据维基全文；单源待核实。伊朗条目已注明"是否构成严格恶性通胀待核实"。【续作CK】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r91_data.json', encoding='utf-8'))
for sid, key in [('w-en-iranian-economic-crisis','iranian-crisis'), ('w-en-syrian-pound','syrian-pound')]:
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
