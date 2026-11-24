# -*- coding: utf-8 -*-
"""续作CI：新增也门货币分裂案例(中东×货币)与"货币重定面值"概念。"""
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
 dict(id='yemen-currency-divergence', title='也门货币分裂与里亚尔贬值(2015–)', cat='货币',
  unit='U5 21世纪', period='21世纪', region='中东', tier='重要',
  ol='也门内战导致里亚尔在南北分裂为两套体系，持续印钞使南部币值大幅下跌。',
  ov=('也门里亚尔(YER)是也门的官方货币，技术上分为100费尔。由于持续的政治不稳定，里亚尔的价值已大幅下跌。'
   '也门内战还导致**货币分裂**：在南部（主要由阿联酋支持的分裂势力控制，与国际承认、沙特支持的政府并行），'
   '**持续的印钞使货币价值暴跌**；而北部（胡塞控制区）则出现不同的货币安排与汇率。'
   '一国之内同时存在两套货币当局与双重汇率，使支付、清算与物价呈现区域分化，'
   '这是内战型经济中"货币主权分裂"的典型样本。'
   '具体汇率水平、通胀数据与分裂时点待核实（本条目暂无可靠的单源数值，故 key_data 暂缺）。'),
  tl=[
    {'year':2014,'display':'2014年起','event':'也门内战爆发，政治不稳定致里亚尔持续贬值','sources':['w-en-yemeni-rial']},
    {'year':2016,'display':'2010年代中期起','event':'南部持续印钞使币值暴跌，南北货币安排分化（细节待核实）','sources':['w-en-yemeni-rial']},
  ],
  causal=[('内战导致税收与外汇收入瓦解 → 财政只能靠印钞融资','w-en-yemeni-rial'),
         ('南部持续印钞 → 里亚尔币值暴跌','w-en-yemeni-rial'),
         ('南北分裂的货币当局 → 一国两套货币与多重汇率，支付与物价区域化','w-en-yemeni-rial')],
  schools=[{'holder':'国家能力视角','view':'货币统一依附于政治统一，内战必然导致货币分裂','basis':'据也门案例归纳；一般化待核实','sources':['w-en-yemeni-rial']},
           {'holder':'印钞融资视角','view':'缺乏税收能力时印钞成为唯一财源，币值下跌是必然结果','basis':'据货币危机通行逻辑归纳','sources':['w-en-yemeni-rial']}],
  kd=[],
  cmp=('与津巴布韦2009年美元化、南斯拉夫1990s货币崩溃相比，也门的特殊性在于**一国之内并存两套货币安排**；'
   '与黎巴嫩的多重汇率并存亦有相似处（见 lebanese-liquidity-2019）。具体异同待核实。')),
 dict(id='redenomination', title='货币重定面值(redenomination)', cat='货币',
  unit='U6 理论与制度', period='理论制度', region='全球', tier='补充',
  ol='改变流通中纸币与硬币面值的过程，常因通胀使货币单位过小而发生。',
  ov=('在货币经济学中，货币重定面值(redenomination) 是改变流通中纸币与硬币面值的过程。'
   '它可能因**通胀已使货币单位过小**、流通中只剩大面额而发生——此时货币名称可能改变，'
   '或在原名前加"新"字等限定词。重定面值也可能出于其他原因，例如转换为新货币（如欧元）或十进制化。'
   '就其本身而言，重定面值被视为**象征性**措施：它并不影响一国相对其他货币的汇率，'
   '但可能对公众心理产生（影响）。'
   '经济学上，若因通胀而重定面值，换算比率通常远大于1，且多为10的正整数次幂（如100、1000或100万）。'
   '该工具本身不能替代财政与货币纪律——若无根本调整，通胀会在新面值下继续。具体案例待核实。'),
  tl=[],
  causal=[('恶性通胀使货币单位过小 → 流通中只剩大面额','w-en-redenomination'),
         ('按10的整数次幂换算面值（如1/1000）→ 旧币换新币','w-en-redenomination'),
         ('重定面值本身不影响汇率 → 若不解决财政与货币根源，通胀延续','w-en-hyperinflation')],
  schools=[{'holder':'技术视角','view':'重定面值只是计价单位的数学调整，属象征性','basis':'据定义归纳','sources':['w-en-redenomination']},
           {'holder':'可信度视角','view':'若与稳定化政策配套，重定面值可传递决心、重建信心','basis':'据多国经验归纳；效果待核实','sources':['w-en-hyperinflation']}],
  kd=[],
  cmp=('与贬值(devaluation) 不同：后者改变对外汇率，重定面值只改变计价单位；'
   '与货币改革(currency reform) 相比，后者通常伴随旧币兑换限制或减记。具体异同待核实。')),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': sp['kd'], 'schools': sp['schools'],
        'policy_response': [{'holder':'政策当局','view':'应对措施与效果待核实','basis':'需多来源印证',
                            'sources':[sp['causal'][0][1]]}],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st,s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基摘要（也门页数据有限，key_data暂缺）；具体数据待核实。【续作CI】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r87_data.json', encoding='utf-8'))
for sid, key in [('w-en-yemeni-rial','yemeni-rial'), ('w-en-redenomination','redenomination')]:
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
