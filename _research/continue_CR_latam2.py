# -*- coding: utf-8 -*-
"""续作CR：新增巴西Encilhamento泡沫(填补拉美×泡沫)与海地独立债务(拉美×19世纪)。"""
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
 dict(id='encilhamento-1890', title='巴西Encilhamento泡沫(1880s末–1890s初)', cat='泡沫',
  region='拉美', tier='重要',
  ol='巴西第一共和国初期的投机泡沫：无限制信贷与货币超发推高公司股票，1891年前后破裂引发制度与金融危机。',
  ov=('Encilhamento 是1880年代末至1890年代初在巴西膨胀起来的经济泡沫，'
   '在巴西第一共和国（1889—1894）初年破裂，并导致**制度危机与金融危机**。'
   '其政策根源是**无限制的信贷供给**：先后两位财政部长——欧鲁普雷图子爵(Viscount of Ouro Preto) 与鲁伊·巴尔博萨(Ruy Barbosa)——'
   '对工业投资采取不受约束的信贷政策，并以**大量货币发行**作为支撑。'
   '在共和初建、奴隶制刚废除（1888）与资本极度稀缺的背景下，'
   '大量新设公司（多为空壳）在里约交易所被狂热追捧，股价脱离任何盈利基础。'
   '1891年前后的信贷收缩与政治动荡使泡沫破裂，公司大批倒闭、银行受损、汇率贬值，'
   '成为巴西此后长期高通胀与货币不稳的历史起点之一（可参看 brazil-hyper-1980）。'
   '该案例是"货币超发+无约束信贷+新设公司投机"组合的早期样本。具体数据待核实。'),
  tl=[
   {'year':1888,'display':'1888年','event':'奴隶制废除，共和运动高涨（背景）','sources':['w-en-encilhamento']},
   {'year':1889,'display':'1889年','event':'巴西第一共和国建立，宽松信贷与货币发行启动','sources':['w-en-encilhamento']},
   {'year':1891,'display':'1891年前后','event':'泡沫破裂，制度与金融危机（具体年份待核实）','sources':['w-en-encilhamento']},
  ],
  causal=[('共和初建 + 资本稀缺 → 以无限制信贷与货币发行推动工业化','w-en-encilhamento'),
         ('空壳公司大量上市 + 交易所狂热 → 股价脱离盈利基础','w-en-encilhamento'),
         ('信贷收缩与政治动荡 → 泡沫破裂、公司倒闭与银行受损','w-en-encilhamento')],
  schools=[{'holder':'货币超发视角','view':'以印钞支撑工业信贷是泡沫的直接成因','basis':'据两位财政部长的政策归纳','sources':['w-en-encilhamento']},
           {'holder':'制度视角','view':'共和初建时监管与公司法的缺位放大了投机','basis':'据泡沫过程归纳；因果待核实','sources':['w-en-encilhamento']}],
  kd=[],
  cmp=('与同期阿根廷1890年巴林危机（见 baring-crisis-1890）同为拉美"伦敦资本—本地投机"链条的一环，'
   '但巴西案例的驱动力更多是**国内货币超发**而非外部借款。具体异同待核实。')),
 dict(id='haitian-independence-debt', title='海地独立债务(1825–)', cat='债务',
  region='拉美', tier='重要',
  ol='1825年法国要求海地支付1.5亿法郎赔偿以换取承认独立，海地为此背负长期债务，实际偿付约1.12亿法郎。',
  ov=('海地独立债务源于 **1825年** 海地与法国达成的一项协议：'
   '法国要求海地支付 **1.5亿法郎** 的赔偿——分 **5年、每年3000万法郎** 支付，'
   '理由是赔偿法国（包括海地奴隶）在海地革命中损失的财产，以此换取外交承认。'
   '海地被迫为第一笔3000万法郎**借入贷款**；**1838年** 法国同意将剩余债务降至 **6000万法郎**、分30年偿付。'
   '有研究估计海地实际支付的赔偿约 **1.12亿法郎**，按通胀调整约相当于 **2022年的5.6亿美元**。'
   '值得注意的对比是：**第一笔年度付款3000万法郎，是海地年（收入）的6倍**——'
   '这意味着偿债压力远超其财政能力，只能靠新借款滚动，形成长期债务依赖。'
   '法方的赔偿计算依据是《黑法典》(Code Noir) 第44与48条（涉及奴隶的财产地位）。'
   '该案例被视为"以债务工具延续殖民榨取"的典型，其长期影响（财政挤压、发展受阻）在近年重获关注。'
   '具体金额与偿债时序待核实。'),
  tl=[
   {'year':1825,'display':'1825年','event':'法国要求1.5亿法郎赔偿（分5年、每年3000万），换取承认独立','sources':['w-en-haitian-independence-debt']},
   {'year':1838,'display':'1838年','event':'法国同意将剩余债务降至6000万法郎、30年偿付','sources':['w-en-haitian-independence-debt']},
  ],
  causal=[('法国以承认独立为条件索取巨额赔偿 → 海地被迫接受1.5亿法郎','w-en-haitian-independence-debt'),
         ('首年付款3000万法郎为年收入的6倍 → 只能借新债偿付，形成债务依赖','w-en-haitian-independence-debt'),
         ('长期偿债挤压财政 → 发展受阻（实际偿付约1.12亿法郎，约合2022年5.6亿美元）','w-en-haitian-independence-debt')],
  schools=[{'holder':'殖民榨取视角','view':'以债务工具延续了对前殖民地的资源抽取','basis':'据赔偿与偿债数据归纳；长期影响评估待核实','sources':['w-en-haitian-independence-debt']},
           {'holder':'财政约束视角','view':'偿债压力挤占公共投资，是长期低发展的机制之一','basis':'据偿债占收入比例归纳','sources':['w-en-haitian-independence-debt']}],
  kd=[
   {'label':'法国要求的赔偿总额(1825)','value':150,'unit':'百万法郎（分5年、每年3000万）','year':1825,'comparable_price':False,
    'note':'原文：France demanding an indemnity of 150 million francs in five annual payments of 30 million；单一来源待核实。','sources':['w-en-haitian-independence-debt']},
   {'label':'减免后剩余债务(1838)','value':60,'unit':'百万法郎（分30年偿付）','year':1838,'comparable_price':False,
    'note':'原文：in 1838 France agreed to reduce the remaining debt to 60 million to be paid over 30 years；单一来源待核实。','sources':['w-en-haitian-independence-debt']},
   {'label':'实际支付的赔偿额(估计)','value':112,'unit':'百万法郎（约合2022年5.6亿美元）','year':1900,'comparable_price':True,
    'note':'原文：They approximated that 112 million francs was actually paid in indemnity, which is equivalent to $560 million in 2022；支付完成年份待核实。','sources':['w-en-haitian-independence-debt']},
   {'label':'首年赔偿付款相当于海地年收入的倍数','value':6,'unit':'倍（3000万法郎）','year':1825,'comparable_price':False,
    'note':'原文：the first annual payment of 30 million francs being six times larger than Haiti\'s yea[rly revenue]；单一来源待核实。','sources':['w-en-haitian-independence-debt']},
  ],
  cmp=('与奥斯曼"公共债务管理局"(1881)、埃及1876年债务危机同属"以财政接管换取债务"的殖民时期模式，'
   '但海地的特殊性在于债务本身源自**独立赔偿**而非发展借款。具体异同待核实。')),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': 'U2 18—19世纪', 'period': '18—19世纪', 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sorted(sp['tl'], key=lambda t:t.get('year',0)),
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': sp['kd'],
        'schools': sp['schools'],
        'policy_response': [],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st,s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基全文；单源待核实。【续作CR】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r102_data.json', encoding='utf-8'))
for sid, key in [('w-en-encilhamento','encilhamento'), ('w-en-haitian-independence-debt','haiti-debt')]:
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
      'unit':'U2 18—19世纪','period':'18—19世纪','region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
