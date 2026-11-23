# -*- coding: utf-8 -*-
"""续作AM：新增4条(巴尔迪家族银行崩溃/美第奇银行/财政军事国家/财政能力)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

D = [
 dict(id='bardi-family', title='巴尔迪家族银行崩溃(1340s)', cat='银行',
  unit='U1 早期—17世纪', period='早期—17世纪', region='欧洲', tier='重要',
  ol='14世纪佛罗伦萨巴尔迪家族银行因英王爱德华三世拒偿巨额贷款而崩溃，佩鲁齐家族同时倒闭。',
  ov='巴尔迪家族（House of Bardi）是佛罗伦萨一个颇具影响力的家族，创办了实力雄厚的银行公司 Compagnia dei Bardi。14世纪，巴尔迪家族向英格兰国王爱德华三世贷出90万金弗罗林；连同佩鲁齐家族（Peruzzi）借出的60万弗罗林，爱德华三世均未偿还，导致两大家族（银行）双双崩溃。这是中世纪银行业危机的经典案例。具体细节待核实。',
  tl=[
    {'year':1340,'display':'14世纪（约1340年代）','event':'巴尔迪与佩鲁齐家族向英王爱德华三世放贷（据 Wikipedia Bardi family）','sources':['w-en-bardi-family']},
    {'year':1345,'display':'14世纪（约1340年代）','event':'爱德华三世未偿还贷款，两大家族银行崩溃（同上；具体年份待核实）','sources':['w-en-bardi-family']}],
  causal=[('向君主大额放贷（Bardi 90万 + Peruzzi 60万金弗罗林）→ 信用高度集中于单一主权债务人','w-en-bardi-family'),
          ('英王爱德华三世拒付 → 银行资产巨额减值','w-en-bardi-family'),
          ('两大家族银行崩溃 → 佛罗伦萨金融体系受创','w-en-bank-failure')],
  schools=[('主权信用风险视角','对君主的集中放贷缺乏可执行约束','w-en-sovereign-risk'),
           ('集中度视角','单一债务人违约即可摧毁银行','w-en-credit-risk')],
  kd=[{'label':'巴尔迪家族贷予爱德华三世','value':900000,'unit':'金弗罗林（golds florins）','year':1340,'comparable_price':False,
       'note':'原文：lent Edward III of England 900,000 gold florins；单一来源待核实。','sources':['w-en-bardi-family']},
      {'label':'佩鲁齐家族贷予爱德华三世','value':600000,'unit':'金弗罗林','year':1340,'comparable_price':False,
       'note':'原文：600,000 florins borrowed from the Peruzzi family；单一来源待核实。','sources':['w-en-bardi-family']}],
  cmp='与近代主权违约（如西班牙16-17世纪多次破产）机制相同：君主赖账直接摧毁债权人。具体异同待核实。'),
 dict(id='medici-bank', title='美第奇银行(1397–1494)', cat='银行',
  unit='U1 早期—17世纪', period='早期—17世纪', region='欧洲', tier='补充',
  ol='15世纪意大利美第奇家族创办的金融机构，鼎盛期为欧洲最大最受尊敬的银行。',
  ov='美第奇银行是15世纪（1397—1494年）由意大利美第奇家族创办的金融机构。在其鼎盛时期，它是欧洲规模最大、最受尊敬的银行；有估计认为美第奇家族一度是欧洲最富有的家族。该行以跨国分支网络与汇票业务著称，其衰落亦与主权债务人违约相关。具体细节待核实。',
  tl=[
    {'year':1397,'display':'1397年','event':'美第奇银行创立（据 Wikipedia Medici Bank）','sources':['w-en-medici-bank']},
    {'year':1494,'display':'1494年','event':'美第奇银行结束（同上）','sources':['w-en-medici-bank']}],
  causal=[('跨国分支网络 + 汇票业务 → 成为欧洲最大银行','w-en-medici-bank'),
          ('与君主和政治权力深度绑定 → 承受主权违约与政治风险','w-en-medici-bank'),
          ('1494年终结 → 家族银行模式衰落','w-en-bill-of-exchange')],
  schools=[('金融创新视角','分支网络与汇票推动跨境金融','w-en-medici-bank'),
           ('主权风险视角','与君主绑定带来不可控信用风险','w-en-sovereign-risk')],
  cmp='与巴尔迪家族银行同为意大利中世纪-文艺复兴银行业代表，均受主权债务人风险影响。具体异同待核实。'),
 dict(id='fiscal-military-state', title='财政军事国家', cat='制度',
  unit='U6 理论与制度', period='理论制度', region='全球', tier='重要',
  ol='以维持武装力量为经济模式基础的国家，通常在长期或严重冲突时期出现。',
  ov='财政军事国家是一种把经济模式建立在维持武装力量之上的国家，通常出现在长期或严重冲突时期。其特征是为此对公民课以高额税收。该概念用于解释近代欧洲国家能力、公债与税收制度的形成，以及战争与国家建构的关系。具体论述待核实。',
  tl=[],
  causal=[('长期战争压力 → 国家需持续动员资源','w-en-fiscal-military-state'),
          ('建立高税负与公债体系 → 财政能力扩张','w-en-fiscal-military-state'),
          ('财政-军事能力差异 → 影响国际竞争与国家兴衰','w-en-fiscal-capacity')],
  schools=[('国家建构视角','战争需求驱动税收与官僚体系发展','w-en-fiscal-military-state'),
           ('制度视角','财政能力是长期增长与竞争的基础','w-en-institutional-economics')],
  cmp='与重商主义同属近代欧洲国家竞争的经济-政治安排；其公债体系亦为后世主权债市场的前身。具体异同待核实。'),
 dict(id='fiscal-capacity', title='财政能力', cat='制度',
  unit='U6 理论与制度', period='理论制度', region='全球', tier='重要',
  ol='国家在给定行政与财政核算结构下提取收入、以提供公共品并履行职能的能力。',
  ov='财政能力是国家在给定行政与财政核算结构下提取收入、以提供公共品并履行其他职能的能力。在经济学与政治科学中，因税收是（主要手段），财政能力也可称为税收能力、提取能力或征税权力。财政能力是理解国家能力、债务可持续与发展差异的核心变量。具体论述待核实。',
  tl=[],
  causal=[('行政与征管结构决定可提取收入 → 形成财政能力','w-en-fiscal-capacity'),
          ('财政能力充足 → 可提供公共品、承受冲击','w-en-fiscal-space'),
          ('能力薄弱 → 依赖铸币税或外债、易陷入危机','w-en-hyperinflation')],
  schools=[('国家能力视角','财政能力是国家能力的核心维度','w-en-fiscal-capacity'),
           ('发展视角','财政能力差异解释长期发展分化','w-en-institutional-economics')],
  cmp='与财政空间（短期余裕）相比，财政能力更偏结构性与长期；二者共同决定反周期与偿债能力。具体异同待核实。'),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': sp.get('kd', []),
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [{'holder': '政策当局', 'view': '应对措施及效果待核实', 'basis': '需多来源印证',
                             'sources': [sp['causal'][0][1]]}],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st, s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值与细节待核实补充。【续作AM】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r58_early.json', encoding='utf-8'))
for eid, v in meta.items():
    sid = 'w-en-' + eid
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科', 'url': 'https://en.wikipedia.org/wiki/' + v['slug'], 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'Wikipedia REST API核对(本会话抓取摘要)'
    })
    ex.add(sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have:
        continue
    cov['entries'].append({
        'id': sp['id'], 'level': 'L2', 'tier': sp['tier'], 'status': 'written',
        'source_count': len(sp['causal']), 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': sp['unit'], 'period': sp['period'], 'region': sp['region'], 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
