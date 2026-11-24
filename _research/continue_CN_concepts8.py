# -*- coding: utf-8 -*-
"""续作CN：新增8条宏观/国际金融概念。"""
import json

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
 dict(id='neutral-rate', title='中性利率(r*)', cat='理论',
  ol='在充分就业/最大产出下、且通胀稳定时使经济保持平衡的实际利率。',
  ov=('中性利率（natural rate of interest，又称 r-star 或 r*）是在**充分就业/最大产出**下、'
   '同时保持（通胀稳定）的实际利率。它是货币政策判断"松紧"的基准：'
   '实际政策利率低于 r* 属宽松，高于 r* 属紧缩。'
   'r* 不可直接观测，只能通过模型估算，估算值随时间与模型差异很大——'
   '这使"政策是否足够宽松"的判断带有相当大的不确定性。'
   '近年发达经济体对 r* 的估计普遍下移，被用于解释长期低利率与"长期停滞"假说。'
   '具体估算方法与数值待核实。'),
  tl=[],
  causal=[('储蓄与投资的结构性因素决定均衡实际利率 → 形成 r*','w-en-neutral-rate'),
         ('实际政策利率相对 r* 的位置 → 决定政策松紧','w-en-neutral-rate'),
         ('r* 不可观测且估算不稳 → 政策判断存在不确定性','w-en-neutral-rate')],
  schools=[('实际因素视角','r* 由储蓄-投资与生产率等实际因素决定','w-en-neutral-rate'),
           ('货币/金融视角','金融周期与危机可长期改变 r*','w-en-fiscal-dominance')],
  srcs=['w-en-neutral-rate','w-en-monetary-policy']),
 dict(id='capital-controls', title='资本管制', cat='制度',
  ol='基于居留身份的、用于调节跨境资本流动的税收、限额或禁令等措施。',
  ov=('资本管制是**基于居留身份**（residency-based）的措施，例如交易税、其他限制或直接的禁令，'
   '一国政府可用以调节资本跨境流动。'
   '常见形式包括：对短期流入征税（如托宾税式）、对流出设限、强制结汇或留存要求、'
   '以及区分居民与非居民的账户管理。'
   '在"不可能三角"框架下，资本管制被视为在保留货币政策独立性的同时维持汇率稳定的一种手段。'
   'IMF 的官方立场在2008年后由"一概反对"转向"在特定情形下可有序使用"（机构观点）。'
   '其效果与副作用（扭曲、规避、治理成本）长期存在争论。具体实践待核实。'),
  tl=[],
  causal=[('跨境资本流动剧烈波动 → 汇率与金融稳定承压','w-en-capital-control'),
         ('以居留身份为基础的税收/限额/禁令 → 抑制特定资本流动','w-en-capital-control'),
         ('代价是扭曲与规避 → 需与宏观审慎、汇率弹性配合','w-en-impossible-trinity')],
  schools=[('三难困境视角','资本管制可换取汇率稳定与货币政策独立性','w-en-impossible-trinity'),
           ('效率视角','管制扭曲配置、催生规避渠道，长期成本高','w-en-capital-flight')],
  srcs=['w-en-capital-control','w-en-impossible-trinity']),
 dict(id='special-drawing-rights', title='特别提款权(SDR)', cat='货币',
  ol='由国际货币基金组织定义与维护的补充性外汇储备资产，是IMF的记账单位。',
  ov=('特别提款权(SDR) 是由国际货币基金组织(IMF) 定义并维护的**补充性外汇储备资产**，'
   'SDR 也是 IMF 的记账单位。'
   'SDR 不是可流通的货币，而是可向其他成员国兑换硬通货的储备索取权，'
   '其价值由一篮子主要货币按权重定值（篮子构成与权重由 IMF 定期审查调整）。'
   'SDR 的用途包括：补充成员国储备、在危机中提供流动性、以及作为IMF贷款的计价单位。'
   '关于 SDR 是否能演进为"超主权储备货币"的讨论长期存在，但进展有限。具体机制与权重待核实。'),
  tl=[
   {'year':1969,'display':'1969年','event':'IMF 设立 SDR（具体细节待核实）','sources':['w-en-special-drawing-rights']},
  ],
  causal=[('全球储备资产供给依赖少数主权货币 → 出现补充性储备资产的需求','w-en-special-drawing-rights'),
         ('IMF 按份额分配 SDR → 补充成员国储备','w-en-special-drawing-rights'),
         ('SDR 不能直接用于市场交易 → 需兑换为硬通货，作用受限','w-en-special-drawing-rights')],
  schools=[('补充储备视角','SDR 可在危机中快速补充全球流动性','w-en-special-drawing-rights'),
           ('超主权货币视角','SDR 有潜力降低对单一主权货币的依赖，但政治阻力大','w-en-triffin-dilemma')],
  srcs=['w-en-special-drawing-rights','w-en-triffin-dilemma']),
 dict(id='bail-in', title='债权人减记(bail-in)', cat='制度',
  ol='让银行股东与债权人（含部分存款人）承担损失、而非由纳税人出资救助的处置方式。',
  ov=('债权人减记(bail-in) 是与"救助"(bailout) 相对的一种银行处置方式：'
   '在机构无法持续经营时，**由股东与债权人（在塞浦路斯案例中包括超过保险限额的存款人）'
   '承担损失或转换为股权**，而不用纳税人的钱注资。'
   '与之相对，bailout 是向本会破产的公司或国家提供财务援助（通常由公共资金承担）。'
   '2008年危机后，bail-in 被写入多数辖区的处置框架（如欧盟的 BRRD、'
   '以及全球的 TLAC/总损失吸收能力要求），目的在于**打破"太大而不能倒"与纳税人兜底**。'
   '塞浦路斯2013年是 bail-in 最著名的实践（超10万欧元存款被征47.5%，见 cypriot-2013）。'
   '争议在于：bail-in 可能引发对其他银行债权人的传染性恐慌。具体机制待核实。'),
  tl=[
   {'year':2013,'display':'2013年3月','event':'塞浦路斯以存款减记(bail-in)换取救助','sources':['w-en-cypriot-financial-crisis']},
  ],
  causal=[('机构无法持续经营且公共资金不宜再兜底 → 转向内部承担损失','w-en-bailout'),
         ('股东与债权人（含超限额存款）减记或转股 → 由市场承担损失','w-en-cypriot-financial-crisis'),
         ('副作用：可能引发对其他银行债权人的传染性恐慌','w-en-contagion')],
  schools=[('市场约束视角','bail-in 恢复"风险自担"、抑制道德风险','w-en-bailout'),
           ('传染视角','bail-in 的可信度不足时反而加速挤兑与资本外逃','w-en-contagion')],
  srcs=['w-en-bailout','w-en-cypriot-financial-crisis']),
 dict(id='j-curve', title='J曲线效应', cat='理论',
  ol='本币贬值后贸易收支先恶化、后改善的J形调整路径。',
  ov=('J曲线（J curve）泛指曲线先下降、再陡升超过起点的J形图；'
   '在国际经济学中，它特指**本币贬值后贸易收支的调整路径**：'
   '贬值初期，由于进出口数量在短期难以调整（合同、产能与习惯），'
   '以本币计的进口成本上升而出口收入增加有限，贸易收支反而**先恶化**；'
   '随着数量逐步调整，收支才**转为改善**，整体呈J形。'
   '其成立条件与马歇尔-勒纳条件相关（见该条目）：若弹性不足，贬值可能长期无效。'
   '该概念常用于评估汇率调整政策的时间维度与耐心要求。具体实证待核实。'),
  tl=[],
  causal=[('本币贬值 → 进口本币成本立即上升，出口数量短期难增','w-en-j-curve'),
         ('贸易收支先恶化（J的下行段）','w-en-j-curve'),
         ('数量逐步调整后改善（J的上行段），前提是弹性条件满足','w-en-marshall-lerner')],
  schools=[('弹性视角','只要满足马歇尔-勒纳条件，贬值最终改善贸易收支','w-en-marshall-lerner'),
           ('短期视角','短期弹性低，贬值可能先带来输入型通胀与收支恶化','w-en-j-curve')],
  srcs=['w-en-j-curve','w-en-marshall-lerner']),
 dict(id='marshall-lerner', title='马歇尔-勒纳条件', cat='理论',
  ol='一国出口与进口需求弹性绝对值之和大于1时，贬值才能改善贸易收支。',
  ov=('马歇尔-勒纳条件(Marshall-Lerner condition) 在**出口与进口需求弹性的绝对值之和大于1**时成立；'
   '若满足该条件，则本币贬值（在数量调整充分后）会改善贸易收支。'
   '反之，若弹性之和小于1（"弹性悲观论"情形），贬值反而可能使贸易收支恶化——'
   '这是J曲线效应产生的理论基础之一。'
   '该条件假设贸易最初平衡、供给弹性充分、且不考虑收入效应，'
   '因此更完整的分析需引入吸收法与一般均衡框架。'
   '实证上，短期弹性往往偏低、长期弹性较高，这解释了J曲线的存在。具体表述待核实。'),
  tl=[],
  causal=[('贬值改变进出口的相对价格 → 数量按弹性调整','w-en-marshall-lerner'),
         ('弹性之和>1 → 数量效应超过价格效应，贸易收支改善','w-en-marshall-lerner'),
         ('弹性之和<1 → 贬值反而恶化收支（J曲线下行段）','w-en-j-curve')],
  schools=[('弹性分析法','以进出口需求弹性判断贬值效果','w-en-marshall-lerner'),
           ('吸收分析法','贬值效果还取决于国内吸收与产出的调整','w-en-balance-of-payments')],
  srcs=['w-en-marshall-lerner','w-en-balance-of-payments']),
 dict(id='interest-parity', title='利率平价', cat='理论',
  ol='投资者比较两国存款利率与远期汇率后不存在无风险套利机会的均衡状态。',
  ov=('利率平价(interest rate parity) 是一种**无套利条件**：在该均衡状态下，'
   '投资者比较两国银行存款的利率时，' 
   '（结合即期与远期汇率后）不存在可获无风险利润的套利机会。'
   '它分为**抛补利率平价**(covered interest parity, CIP) 与**非抛补利率平价**(uncovered, UIP)：'
   '前者用远期合约锁定汇率，后者以预期汇率替代。'
   'CIP 在正常市场中高度成立，但2008年后在主要货币间出现持续偏离（"CIP 之谜"），'
   '被归因于资产负债表约束与监管成本；UIP 的实证表现则长期不佳（"远期溢价之谜"）。'
   '该条件也是判断资本管制与国际套利空间的基础。具体表述与实证待核实。'),
  tl=[],
  causal=[('两国利差 + 即期/远期汇率 → 形成套利空间或均衡','w-en-interest-parity'),
         ('抛补套利使远期汇率偏离被消除（CIP）','w-en-interest-parity'),
         ('资产负债表约束或管制 → CIP 偏离可持续','w-en-capital-control')],
  schools=[('无套利视角','CIP 应近似成立，偏离是摩擦与约束所致','w-en-interest-parity'),
           ('约束视角','杠杆与监管成本使套利资本有限，偏离可长期存在','w-en-capital-control')],
  srcs=['w-en-interest-parity','w-en-capital-control']),
 dict(id='black-market', title='黑市与影子经济', cat='其他',
  ol='在特定法域内具有非法成分、或不符合监管要求的 clandestine 市场与交易。',
  ov=('黑市是一种**隐秘的市场或一系列交易**，其在特定法域内带有某种非法性成分；'
   '也可能不符合（监管）要求。'
   '在宏观经济与国际金融语境中，黑市最常表现为：**外汇黑市**（管制下形成的平行汇率）、'
   '商品黑市（价格管制下的短缺品）与影子经济活动（未纳入统计的产出与就业）。'
   '其经济意义在于：多重汇率与价格管制的普遍存在，会催生平行市场，'
   '使官方统计失真、政策传导受阻，并成为寻租与腐败的温床。'
   '委内瑞拉、黎巴嫩、叙利亚等国的外汇黑市与官方汇率长期并存，即为典型'
   '（见 venezuela-crisis-2013、lebanese-liquidity-2019、syrian-pound-crisis）。具体论述待核实。'),
  tl=[],
  causal=[('价格/汇率管制或高税负 → 交易转入地下','w-en-black-market'),
         ('形成平行汇率与平行价格 → 官方统计与政策传导失真','w-en-black-market'),
         ('寻租与执法成本上升 → 管制本身趋于不可持续','w-en-currency-crisis')],
  schools=[('管制后果视角','黑市是管制的结果，规模可反映管制的严厉与失效程度','w-en-black-market'),
           ('治理视角','需以制度与执法能力而非单纯加码管制来压缩黑市','w-en-capital-control')],
  srcs=['w-en-black-market','w-en-currency-crisis']),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': [],
        'schools': [{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[src]}
                    for h,v,src in sp['schools']],
        'policy_response': [],
        'comparison': '宏观/国际金融概念，与相关理论与案例互补；具体适用待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])),
        'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体细节待核实。【续作CN】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r95_concepts.json', encoding='utf-8'))
MAP = {'neutral-rate':'w-en-neutral-rate','capital-controls':'w-en-capital-control',
       'special-drawing-rights':'w-en-special-drawing-rights','bail-in':'w-en-bailout',
       'j-curve':'w-en-j-curve','marshall-lerner':'w-en-marshall-lerner',
       'interest-parity':'w-en-interest-parity','black-market':'w-en-black-market'}
for eid, sid in MAP.items():
    if sid in ex: continue
    v = meta.get(eid);
    if not v: continue
    sd['sources'].append({'id':sid,'title':v['title'],'author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+v['slug'],'url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia REST API核对(本会话抓取摘要)'})
    ex.add(sid); print('新增来源',sid)
sd['count']=len(sd['sources'])
json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':'重要','status':'written',
      'source_count':len(sp['srcs']),'needs_verification':1,'last_updated':'2026-11-24',
      'unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
