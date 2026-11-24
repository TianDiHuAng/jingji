# -*- coding: utf-8 -*-
"""续作CW：新增5条金融稳定类概念。"""
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
 dict(id='procyclicality', title='顺周期性与逆周期变量', cat='理论',
  ol='与GDP周期同向（正向）或反向（负向）变动的变量；金融体系常被指具有顺周期性。',
  ov=('顺周期与逆周期变量是相对于商业周期波动的两类变量：'
   '**顺周期变量**与 GDP 的波动**正相关**，**逆周期变量**则与之**负相关**。'
   '该概念在金融监管中的意义在于：许多金融变量（信贷、杠杆、资产价格、抵押品价值）本身具有**顺周期性**——'
   '景气时放大扩张、下行时放大收缩，从而把冲击放大（与"金融加速器"机制相通）。'
   '由此产生**逆周期政策工具**的需求，例如逆周期资本缓冲(countercyclical capital buffer)、'
   '贷款价值比(LTV)上限与动态拨备，目的是让监管要求随周期反向变动，抵消顺周期放大效应。'
   '具体度量与政策设计待核实。'),
  tl=[],
  causal=[('信贷、杠杆与抵押品价值随景气同向变动 → 顺周期放大','w-en-procyclicality'),
         ('下行时抵押品贬值 → 追加抵押与信贷收缩 → 进一步下行','w-en-fire-sale'),
         ('以逆周期资本缓冲等工具反向调节 → 削弱放大效应','w-en-macroprudential')],
  schools=[('放大机制视角','金融体系的顺周期性是危机深度的关键放大器','w-en-financial-accelerator'),
           ('监管设计视角','以逆周期工具（CCyB/LTV）对冲，但时机判断困难','w-en-macroprudential')],
  srcs=['w-en-procyclicality','w-en-macroprudential']),
 dict(id='margin-call', title='保证金与追加保证金', cat='制度',
  ol='交易方需缴纳的抵押品；价格不利变动时被要求追加，可触发强制平仓与螺旋式抛售。',
  ov=('在金融中，保证金(margin) 是金融工具持有者需向交易对手缴纳的**抵押品**，'
   '用以覆盖该持有者对对手方造成的部分或全部信用风险。'
   '**追加保证金**(margin call) 是在抵押品价值不足以覆盖敞口时，'
   '对手方要求补足抵押品的通知；若无法补足，头寸将被**强制平仓**。'
   '这一机制在危机中具有强烈的**顺周期放大**效应：'
   '价格下跌 → 抵押品贬值 → 追加保证金 → 被迫卖出 → 价格进一步下跌（"**保证金螺旋**"）。'
   'Archegos(2021) 与英国 LDI 危机(2022) 都是保证金机制放大冲击的直接案例。'
   '监管上，初始保证金与变动保证金要求（如对非集中清算衍生品）旨在抑制过度杠杆，'
   '但在压力情形下也可能加速抛售。具体规则待核实。'),
  tl=[],
  causal=[('杠杆头寸以抵押品担保 → 抵押品价值随价格波动','w-en-margin-call'),
         ('价格不利变动 → 抵押品不足 → 追加保证金通知','w-en-margin-call'),
         ('无法补足 → 强制平仓 → 价格进一步下跌（保证金螺旋）','w-en-fire-sale')],
  schools=[('风险控制视角','保证金是控制对手方风险的基本工具','w-en-margin-call'),
           ('顺周期视角','压力时追加保证金加速抛售，放大系统性冲击','w-en-procyclicality')],
  srcs=['w-en-margin-call','w-en-fire-sale']),
 dict(id='secular-stagnation', title='长期停滞', cat='理论',
  ol='市场经济长期增长近乎停滞的状态；用于解释发达经济体长期低利率、低通胀与低增长并存。',
  ov=('在经济学中，长期停滞(secular stagnation) 指市场经济处于**增长可忽略或几乎为零**的状态。'
   '此处"secular"意为**长期**，以区别于周期性波动。'
   '该概念被用于解释2008年后发达经济体的组合症状：'
   '**低增长、低通胀、低均衡利率（r* 下移）并存**，使常规货币政策空间受限（见 neutral-rate、'
   'liquidity-trap 条目）。'
   '主要解释包括：需求长期不足（人口老龄化、不平等上升、投资需求疲弱）、'
   '技术进步对就业与投资的净效应、以及债务积压后的去杠杆。'
   '批评者认为观测到的低增长更多是统计与周期因素，或归因于政策选择而非"长期停滞"的必然性。'
   '该概念对"低利率是常态还是异常"的判断有直接影响。具体争论待核实。'),
  tl=[],
  causal=[('人口与投资需求长期偏弱 → 均衡实际利率(r*)下移','w-en-secular-stagnation'),
         ('政策利率易触及下限 → 常规货币政策空间受限','w-en-liquidity-trap'),
         ('低增长、低通胀、低利率并存 → 形成"长期停滞"症状组合','w-en-neutral-rate')],
  schools=[('需求不足视角','储蓄过剩与投资需求疲弱使经济长期低于潜在产出','w-en-secular-stagnation'),
           ('政策与统计视角','低增长更多源于政策选择与度量问题，非必然停滞','w-en-neutral-rate')],
  srcs=['w-en-secular-stagnation','w-en-neutral-rate']),
 dict(id='financialization', title='金融化', cat='其他',
  ol='1980年以来金融资本主义的发展：债务权益比上升、金融部门比重扩大、企业行为受金融逻辑主导。',
  ov=('金融化(financialization) 是一个常被用来描述**1980年至今金融资本主义发展**的术语——'
   '这一时期**债务对权益比率上升**，金融部门在经济中的比重扩大，'
   '非金融企业的行为也更多受金融逻辑（股东价值、股价、财务工程）主导。'
   '其表现包括：金融业占GDP与利润份额上升、家庭债务扩张、'
   '企业把更多现金流用于回购与分红而非投资、以及"以交易而非生产"获利模式的扩散。'
   '与危机的关系是双向的：金融化被认为提高了系统性风险与不平等，'
   '而危机后的救助又可能强化"太大而不能倒"与金融部门的政治影响力。'
   '该概念也存在争议——批评者认为它过于笼统、难以量化，且与"金融深化"的正面效应难以区分。'
   '具体度量与因果待核实。'),
  tl=[],
  causal=[('放松管制与股东价值导向 → 金融动机渗透非金融企业','w-en-financialization'),
         ('债务权益比上升 + 金融部门份额扩大 → 系统杠杆与关联度上升','w-en-financialization'),
         ('危机后救助强化大型金融机构地位 → 金融化趋势延续（争议）','w-en-too-big-to-fail')],
  schools=[('批判视角','金融化抬高风险与不平等，挤压实体投资','w-en-financialization'),
           ('质疑视角','概念过于笼统，与金融深化的正面作用难以区分','w-en-financial-repression')],
  srcs=['w-en-financialization','w-en-financial-repression']),
 dict(id='asset-liability-mismatch', title='资产负债错配（含货币错配）', cat='理论',
  ol='机构资产与负债的期限、币种或利率特征不匹配，是银行与主权危机的共同根源之一。',
  ov=('资产负债错配(asset–liability mismatch) 指一家机构的**资产与负债在金融条件上不相匹配**。'
   '常见的错配类型包括：'
   '**期限错配**（短借长贷，如银行以活期存款支持长期贷款）、'
   '**币种错配/货币错配**（借外币、收本币，汇率贬值即放大债务负担，即"原罪"问题，'
   '见 original-sin）、以及**利率错配**（浮动利率负债对应固定利率资产）。'
   '错配是银行业务的本质特征（也是其盈利来源），但过度错配会把小幅冲击放大为偿付危机：'
   '期限错配导致挤兑风险，货币错配使贬值直接恶化资产负债表的负债端。'
   '监管以流动性覆盖率、净稳定资金比率与外汇敞口限额等工具约束错配程度。'
   '具体分类与度量待核实。'),
  tl=[],
  causal=[('短借长贷或借外币/放本币 → 资产负债在期限与币种上不匹配','w-en-alm'),
         ('冲击（挤兑或贬值）→ 负债端骤增或资产端无法变现','w-en-original-sin'),
         ('以流动性比率与外汇敞口限额约束 → 降低错配放大效应','w-en-basel-iii')],
  schools=[('银行本质视角','期限转换是银行的核心功能，错配无法消除只能管理','w-en-bank-run'),
           ('新兴市场视角','货币错配是新兴市场危机的结构性根源（原罪）','w-en-original-sin')],
  srcs=['w-en-alm','w-en-original-sin']),
]

HAVE_TITLES = {json.load(open(f, encoding='utf-8'))['title'] for f in glob.glob('data/entries/*.json')}
for sp in D:
    if sp['title'] in HAVE_TITLES:
        print('跳过重复标题', sp['id'], sp['title'])
        continue
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': [],
        'schools': [{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[src]}
                    for h,v,src in sp['schools']],
        'policy_response': [],
        'comparison': '',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])),
        'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体细节待核实。【续作CW】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r110_concepts.json', encoding='utf-8'))
MAP = {'procyclicality':'w-en-procyclicality','margin-call':'w-en-margin-call',
       'secular-stagnation':'w-en-secular-stagnation','financialization':'w-en-financialization',
       'asset-liability-mismatch':'w-en-alm'}
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
added = 0
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':'重要','status':'written',
      'source_count':2,'needs_verification':1,'last_updated':'2026-11-24',
      'unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':sp['cat']})
    added += 1
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'], '| 新增', added)
