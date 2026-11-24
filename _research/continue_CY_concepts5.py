# -*- coding: utf-8 -*-
"""续作CY：新增5条概念(housing-bubble/informal-economy/family-office/pension-fund/stabilization-program)。"""
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
 dict(id='housing-bubble', title='房地产泡沫', cat='泡沫',
  ol='在地方或全球房地产市场周期性出现的资产泡沫，通常跟随土地价格与信贷扩张。',
  ov=('房地产泡沫（real-estate bubble 或 property bubble）是在**地方或全球房地产市场周期性出现**的一类经济泡沫，'
   '通常伴随着土地价格与信贷的扩张。'
   '其共同机制与一般资产泡沫一致：信贷可得性上升 → 房价上涨 → 抵押品价值上升 → 进一步放宽信贷 → 房价再涨；'
   '而房地产的特殊性在于**杠杆高、供给调整慢、且与银行体系深度绑定**，'
   '因此破裂时的破坏力远超股票泡沫——2007—08年全球危机即由美国房价下跌触发。'
   '识别指标包括房价收入比、房价租金比、信贷/GDP 缺口与建筑投资占比，但均存在局限。'
   '经典案例：日本1990（见 japan-asset-bubble-1990）、西班牙2008、爱尔兰2008、'
   '新西兰1990s以来（见 nz-property-bubble）、中国2020年以来（见 china-realestate-2020）。具体论述待核实。'),
  tl=[],
  causal=[('低利率与信贷扩张 → 住房需求与房价上升','w-en-real-estate-bubble'),
         ('抵押品升值 → 进一步放宽信贷（顺周期）','w-en-financial-accelerator'),
         ('利率上行或预期逆转 → 价格下跌，通过银行体系放大冲击','w-en-subprime-crisis')],
  schools=[('信贷视角','泡沫由信贷扩张驱动，货币条件变化是关键','w-en-real-estate-bubble'),
           ('供给视角','土地与规划约束使供给弹性低，价格对需求冲击更敏感','w-en-new-zealand-property-bubble')],
  srcs=['w-en-real-estate-bubble','w-en-financial-accelerator']),
 dict(id='informal-economy', title='非正规经济', cat='其他',
  ol='任何经济中既不被征税也不被政府监测的部分。',
  ov=('非正规经济(informal economy) 是任何经济中**既不被征税、也不被政府以任何形式监测**的那部分。'
   '尽管非正规部门在许多经济体中都占相当大的比重，但它长期游离于官方统计与监管之外。'
   '在危机语境中，非正规经济有三重意义：'
   '①**统计失真**——官方GDP、就业与通胀数据可能系统性低估实际活动，'
   '使政策制定者对经济状况判断失误；'
   '②**传导渠道**——非正规信贷（如民间标会、地下钱庄）在正规金融收缩时膨胀，'
   '也成为风险积累的暗池（见 black-market）；'
   '③**政策盲区**——税收能力薄弱限制了财政应对危机的空间。'
   '该概念对理解新兴市场与转轨经济的危机机制尤为重要。具体度量方法待核实。'),
  tl=[],
  causal=[('正规部门税负与管制较重 → 活动转入非正规部门','w-en-informal-economy'),
         ('官方统计未覆盖 → 政策判断与危机应对依据失真','w-en-informal-economy'),
         ('非正规信贷扩张 → 风险在监管视野外积累','w-en-black-market')],
  schools=[('结构视角','非正规部门是管制与税负的产物，规模反映制度质量','w-en-informal-economy'),
           ('金融稳定视角','非正规信贷链条断裂时缺乏最后贷款人与处置机制','w-en-black-market')],
  srcs=['w-en-informal-economy','w-en-black-market']),
 dict(id='family-office', title='家族办公室', cat='制度',
  ol='为富裕家族管理投资与财富的私人持股公司，监管与披露要求通常低于基金。',
  ov=('家族办公室(family office)，或单一家族办公室(SFO)，是为富裕家族管理**投资与财富**的私人持股公司。'
   '与共同基金或对冲基金不同，家族办公室通常只服务一个家族，'
   '因此在多数辖区享有**更宽松的注册、披露与资本要求**。'
   '这种制度安排的风险含义在 Archegos 事件中暴露得很清楚（见 archegos-2021）：'
   '家族办公室可以通过**总收益互换**等衍生品在多家银行同时建立巨额集中敞口，'
   '而每家银行只看到自己那一部分，**无人掌握整体杠杆**；'
   '同时它不受基金那样的杠杆与投资者披露约束。'
   '监管讨论的焦点是：是否应把大型家族办公室纳入系统性风险监测，'
   '以及银行对单一交易对手的敞口限制是否足以覆盖衍生品名义敞口。具体规则待核实。'),
  tl=[],
  causal=[('单一家族服务 + 门槛较低 → 披露与资本约束宽松','w-en-family-office'),
         ('以衍生品建立跨行敞口 → 各银行只见局部、整体杠杆不透明','w-en-archegos'),
         ('标的价格不利变动 → 集中敞口同时触发多家银行追保','w-en-margin-call')],
  schools=[('监管缺口视角','大型家族办公室应纳入系统性风险监测','w-en-archegos'),
           ('对手方管理视角','银行应自行以敞口限额与保证金覆盖风险，无需专门监管','w-en-margin-call')],
  srcs=['w-en-family-office','w-en-archegos']),
 dict(id='pension-fund', title='养老基金', cat='制度',
  ol='提供退休收入的基金或计划；其资产负债久期错配与对冲策略可成为系统性风险源。',
  ov=('养老基金(pension fund) 是任何**提供退休收入**的计划、基金或安排（部分国家称 superannuation fund）。'
   '按筹资方式可分为**确定给付(DB)**与**确定缴费(DC)**两类：'
   'DB 计划承诺固定待遇，投资风险由雇主/计划承担；DC 计划则由个人承担投资风险。'
   'DB 计划因负债久期很长，普遍采用**负债驱动投资(LDI)** 等久期匹配策略，'
   '并借助利率互换等衍生品加杠杆对冲——这使其在利率急变时可能被迫抛售资产，'
   '成为系统性风险的来源（见 uk-ldi-crisis-2022）。'
   '此外，老龄化与低利率环境使 DB 计划的融资缺口长期承压，'
   '而 DC 化趋势把风险转移给家庭部门。具体制度差异待核实。'),
  tl=[
   {'year':2022,'display':'2022年','event':'英国LDI策略在国债收益率飙升时触发抵押品螺旋','sources':['w-en-ldi']},
  ],
  causal=[('DB 计划负债久期长 → 以久期匹配与衍生品对冲','w-en-pension-fund'),
         ('对冲需缴纳抵押品 → 利率急变时需追加','w-en-margin-call'),
         ('被迫抛售长期债券 → 收益率再升（抵押品螺旋）','w-en-ldi')],
  schools=[('负债管理视角','LDI 是对冲利率风险的必要工具','w-en-ldi'),
           ('系统性风险视角','杠杆化对冲在压力下放大市场波动，需监管覆盖','w-en-pension-fund')],
  srcs=['w-en-pension-fund','w-en-ldi']),
 dict(id='stabilization-program', title='稳定化政策', cat='制度',
  ol='为稳定金融体系或经济而推出的一揽子措施，可针对需求管理或国际收支调整。',
  ov=('在宏观经济学中，稳定化政策(stabilization policy) 是为**稳定金融体系或经济**而引入的一揽子或一组措施。'
   '该词可用于两类政策：'
   '①**需求管理型**——财政与货币政策用于平抑产出与通胀的波动（见 fiscal-multiplier、'
   'automatic-stabilizer）；'
   '②**国际收支/危机型**——在货币或债务危机中，以汇率调整、财政紧缩、'
   '货币改革与外部融资组合恢复对外平衡，通常伴随 IMF 的条件性贷款（见 imf-programs 类讨论）。'
   '后者的典型配方包括：贬值、紧缩财政、提高利率、重组债务与结构性改革，'
   '其社会代价与效果长期存在激烈争论——紧缩可能压低需求从而推高债务率（见 greek-debt-crisis），'
   '而延迟调整又可能耗尽储备（见 sri-lanka-crisis-2019）。具体配方与效果待核实。'),
  tl=[],
  causal=[('内外失衡（通胀、赤字、储备流失）→ 需要一揽子调整','w-en-stabilization-policy'),
         ('汇率调整 + 财政紧缩 + 货币改革 + 外部融资 → 恢复对外平衡','w-en-imf'),
         ('紧缩压低需求 → 产出与就业代价，效果存在争论','w-en-greek-government-debt-crisis')],
  schools=[('正统配方视角','及早、可信、全面的调整可缩短危机并恢复市场信心','w-en-stabilization-policy'),
           ('代价视角','紧缩本身压低需求，可能自我挫败并加重分配后果','w-en-greek-government-debt-crisis')],
  srcs=['w-en-stabilization-policy','w-en-imf']),
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
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体细节待核实。【续作CY】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r111_concepts.json', encoding='utf-8'))
MAP = {'housing-bubble':'w-en-real-estate-bubble','informal-economy':'w-en-informal-economy',
       'family-office':'w-en-family-office','pension-fund':'w-en-pension-fund',
       'stabilization-program':'w-en-stabilization-policy'}
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
