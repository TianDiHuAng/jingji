# -*- coding: utf-8 -*-
"""续作AX：新增8条国际货币体系概念(L2)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：概念示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)

D = [
 dict(id='plaza-accord', title='广场协议(1985)', cat='货币',
  ol='1985年9月22日法、西德、日、英、美在纽约广场酒店签署的联合协议，旨在使美元对（其他货币）贬值。',
  ov='广场协议是1985年9月22日在纽约市广场酒店签署的联合协议，签署方为法国、西德、日本、英国与美国，目的是使美元相对于（其他主要货币）贬值。该协议是1980年代国际汇率协调的标志性事件，对日元升值与日本后续资产泡沫有重要影响。具体幅度待核实。',
  tl=[{'year':1985,'display':'1985年9月22日','event':'五国在纽约广场酒店签署广场协议，联合干预使美元贬值（据 Wikipedia Plaza Accord）','sources':['w-en-plaza-accord']}],
  causal=[('1980年代美元大幅升值 → 美国贸易逆差扩大','w-en-plaza-accord'),
          ('五国联合干预 → 美元对日元、马克贬值','w-en-plaza-accord'),
          ('日元急升 → 日本转向宽松政策（与后续泡沫相关）','w-en-japan-asset-bubble-1990')],
  schools=[('协调干预视角','联合干预可在短期显著改变汇率','w-en-plaza-accord'),
           ('结构性视角','汇率调整无法解决根本失衡','w-en-global-imbalances')],
  srcs=['w-en-plaza-accord','w-en-japan-asset-bubble-1990']),
 dict(id='louvre-accord', title='卢浮宫协议(1987)', cat='货币',
  ol='1987年2月22日在巴黎签署的协议，旨在稳定国际货币市场并阻止美元在广场协议后继续下跌。',
  ov='卢浮宫协议是1987年2月22日在巴黎签署的协议，旨在稳定国际货币市场、并阻止美元在1985年广场协议之后的持续下跌。它被视为对广场协议后汇率过度波动的修正尝试。其效果与后续市场反应（如1987年10月股灾）的关系存在讨论。具体内容待核实。',
  tl=[{'year':1987,'display':'1987年2月22日','event':'七国在巴黎签署卢浮宫协议，试图稳定汇率、阻止美元续跌（据 Wikipedia Louvre Accord）','sources':['w-en-louvre-accord']}],
  causal=[('广场协议后美元持续下跌、汇率波动加大','w-en-plaza-accord'),
          ('1987年2月卢浮宫协议 → 设定汇率目标区间以稳定市场','w-en-louvre-accord'),
          ('协调的可持续性受各国政策分歧制约','w-en-competitive-devaluation')],
  schools=[('协调视角','目标区间可稳定预期','w-en-louvre-accord'),
           ('不可持续视角','政策分歧使协调难以持久','w-en-competitive-devaluation')],
  srcs=['w-en-louvre-accord','w-en-plaza-accord']),
 dict(id='de-dollarization', title='去美元化', cat='货币',
  ol='政府、企业与市场参与者减少在储备、贸易计价结算、跨境金融与国内交易中使用美元的努力。',
  ov='去美元化指政府、企业与市场参与者减少在储备、贸易计价与结算、跨境金融以及国内交易中使用美元的努力。其动机多样（政治、制裁风险、汇率稳定等），但美元的网络效应使替代进程缓慢。具体进展待核实。',
  causal=[('对美元依赖的担忧（制裁、汇率传导）→ 寻求替代','w-en-de-dollarization'),
          ('以本币或第三方货币结算、增持非美元储备','w-en-de-dollarization'),
          ('网络效应与惯性 → 进程缓慢（有争议）','w-en-reserve-currency')],
  schools=[('多元化视角','去美元化可降低单一货币依赖风险','w-en-de-dollarization'),
           ('惯性视角','美元的网络外部性使替代极难','w-en-exorbitant-privilege')],
  srcs=['w-en-de-dollarization','w-en-reserve-currency']),
 dict(id='currency-internationalization', title='人民币国际化', cat='货币',
  ol='中国自2000年代末起推动人民币国际化，以减少对美元的依赖。',
  ov='自2000年代末以来，中华人民共和国一直寻求推动其官方货币人民币（RMB/CNY）国际化。该举措旨在减少对美元的依赖，并（提升本币在国际交易中的作用）。其进展受资本账户开放程度与金融市场深度制约。具体举措待核实。',
  causal=[('贸易规模庞大但本币计价比例低 → 推动本币国际化','w-en-currency-internationalization'),
          ('以结算、离岸市场与货币互换推进','w-en-currency-internationalization'),
          ('受资本账户管制与汇率弹性制约','w-en-impossible-trinity')],
  schools=[('国际化视角','本币国际化降低汇率风险与美元依赖','w-en-currency-internationalization'),
           ('三元悖论视角','资本管制与汇率稳定限制国际化步伐','w-en-impossible-trinity')],
  srcs=['w-en-currency-internationalization','w-en-impossible-trinity']),
 dict(id='exorbitant-privilege', title='过高特权', cat='货币',
  ol='美国作为全球安全资产供给者，因其货币充当国际储备货币而获得的利益。',
  ov='"过高特权"一词指美国作为世界安全资产供给者，因其本币充当国际储备货币而获得的利益。这些安全资产主要是政府债务（国债）。该特权包括低成本融资、以本币借债等，但也伴随特里芬式责任。具体论述待核实。',
  causal=[('美元充当储备货币 → 全球对美债等安全资产需求旺盛','w-en-exorbitant-privilege'),
          ('美国获得低成本融资与本币负债优势','w-en-exorbitant-privilege'),
          ('同时承担对外供给流动性之责（特里芬难题）','w-en-triffin-dilemma')],
  schools=[('特权视角','储备货币地位带来显著融资优势','w-en-exorbitant-privilege'),
           ('责任视角','特权伴随对外供给与信心维护的两难','w-en-triffin-dilemma')],
  srcs=['w-en-exorbitant-privilege','w-en-reserve-currency']),
 dict(id='competitive-devaluation', title='货币战争（竞争性贬值）', cat='货币',
  ol='各国通过使本币汇率相对下跌来获取贸易优势的国际状况。',
  ov='货币战争（亦称竞争性贬值）是国际事务中的一种状况：各国试图通过使本国货币汇率相对（他国）下跌来获得贸易优势。此类政策可能引发报复循环、损害国际贸易，是1930年代大萧条恶化的重要因素之一。具体案例待核实。',
  causal=[('出口竞争力压力 → 寻求本币贬值','w-en-competitive-devaluation'),
          ('他国报复性贬值 → 形成贬值竞赛','w-en-competitive-devaluation'),
          ('贸易与资本流动受扰 → 全球经济受损','w-en-beggar-thy-neighbour')],
  schools=[('以邻为壑视角','贬值转嫁调整成本、损害集体福利','w-en-beggar-thy-neighbour'),
           ('协调视角','需国际协调以避免贬值竞赛','w-en-international-monetary-system')],
  srcs=['w-en-competitive-devaluation','w-en-beggar-thy-neighbour']),
 dict(id='beggar-thy-neighbour', title='以邻为壑政策', cat='理论',
  ol='一国试图以恶化他国经济问题的方式来解决自身经济问题的经济政策。',
  ov='在经济学中，以邻为壑政策是一国试图通过那些倾向于恶化其他国家经济问题的手段，来解决自身经济问题的经济政策。典型如竞争性贬值、关税壁垒与资本管制。此类政策在大萧条期间盛行，被认为是危机深化的重要原因。具体论述待核实。',
  causal=[('本国失业与国际收支压力 → 采取保护或贬值措施','w-en-beggar-thy-neighbour'),
          ('他国经济受损 → 报复与连锁反应','w-en-competitive-devaluation'),
          ('全球贸易萎缩 → 集体福利下降','w-en-great-depression')],
  schools=[('集体行动视角','单边自救导致集体受损','w-en-beggar-thy-neighbour'),
           ('协调视角','国际协调可避免负和结果','w-en-international-monetary-system')],
  srcs=['w-en-beggar-thy-neighbour','w-en-great-depression']),
 dict(id='international-monetary-system', title='国际货币体系', cat='货币',
  ol='促进国际贸易、跨境投资与资本在国家间再配置的国际公认规则、惯例与支撑机构的集合。',
  ov='国际货币体系是一套国际公认的规则、惯例与支撑机构，用以促进国际贸易、跨境投资以及资本在国家之间的总体再配置。其历史形态包括金本位、布雷顿森林体系与牙买加体系下的浮动汇率安排。体系设计影响调整负担的分配与危机传播。具体论述待核实。',
  causal=[('各国需共同规则以支持贸易与资本流动 → 形成国际货币体系','w-en-international-monetary-system'),
          ('体系形态（金本位/固定/浮动）决定调整机制','w-en-international-monetary-system'),
          ('体系缺陷或冲击 → 危机与体系变革','w-en-bretton-woods-system')],
  schools=[('规则视角','稳定的规则降低交易成本与不确定性','w-en-international-monetary-system'),
           ('权力视角','体系反映主导国家的利益与货币地位','w-en-exorbitant-privilege')],
  srcs=['w-en-international-monetary-system','w-en-bretton-woods-system']),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp.get('tl', []),
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [],
        'comparison': '国际货币体系概念，与布雷顿森林、牙买加协定等条目互补；具体细节待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据待核实。【续作AX】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r69_ims.json', encoding='utf-8'))
MAP = {'plaza-accord':'w-en-plaza-accord','louvre-accord':'w-en-louvre-accord','de-dollarization':'w-en-de-dollarization',
       'currency-internationalization':'w-en-currency-internationalization','exorbitant-privilege':'w-en-exorbitant-privilege',
       'competitive-devaluation':'w-en-currency-war','beggar-thy-neighbour':'w-en-beggar-thy-neighbour',
       'international-monetary-system':'w-en-international-monetary-system'}
for eid, sid in MAP.items():
    if sid in ex:
        continue
    v = meta.get(eid)
    if not v:
        continue
    sd['sources'].append({
        'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科', 'url': 'https://en.wikipedia.org/wiki/' + v['slug'], 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'Wikipedia REST API核对(本会话抓取摘要)'
    })
    ex.add(sid)
    print('新增来源', sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have:
        continue
    cov['entries'].append({
        'id': sp['id'], 'level': 'L2', 'tier': '重要', 'status': 'written',
        'source_count': len(sp['srcs']), 'needs_verification': 1, 'last_updated': '2026-11-24',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
