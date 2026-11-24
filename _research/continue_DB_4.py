# -*- coding: utf-8 -*-
"""续作DB：补建4个被引用但缺失的条目(first-bank/indexation/interest-rate-risk/overend-gurney)。"""
import json, glob

def svg(t, labels):
    e = lambda s: str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：要点</text>"]
    for x, lb in zip([20,270,520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

D = [
 dict(id='first-bank', title='美国第一合众国银行', cat='制度', region='北美',
  unit='U2 18—19世纪', per='18—19世纪', tier='补充',
  ol='1791年2月25日由美国国会特许、期限二十年的国家银行，美国中央银行的第一次尝试。',
  ov=('"合众国银行总裁、董事与公司"（通称**第一合众国银行**）是一家国家银行，'
   '由**美国国会于 1791 年 2 月 25 日**特许，**期限为二十年**。'
   '它是美国建立中央银行职能的第一次尝试：兼具商业银行业务与代理国库、'
   '约束州银行纸币发行的准中央银行角色，其章程设计参照了汉密尔顿的金融方案。'
   '该行从一开始就陷入宪法与政治争论（联邦权力 vs 州权、金融集中 vs 民主问责），'
   '二十年期满后未获续期。'
   '此后美国经历了近二十年的"无国家银行"时期，'
   '直到 1816 年设立第二合众国银行（见 second-bank）。'
   '该线索与第二合众国银行、自由银行时代、国民银行法、联邦储备法共同构成'
   '美国"长期缺乏中央银行 → 危机频发"的制度史。具体条款与争论细节待核实。'),
  tl=[
   {'year':1791,'display':'1791年2月25日','event':'国会特许第一合众国银行，期限二十年','sources':['w-en-first-bank']},
   {'year':1811,'display':'1811年','event':'二十年期满后未获续期（年份据特许期推算待核实）','sources':['w-en-first-bank']},
   {'year':1816,'display':'1816年','event':'第二合众国银行获联邦特许','sources':['w-en-second-bank']},
  ],
  causal=[('联邦需统一货币与代理国库 → 设立国家银行','w-en-first-bank'),
         ('兼营商业银行业务 + 准央行职能 → 引发权力集中与合宪性争论','w-en-second-bank'),
         ('期满未续 → 进入无国家银行时期，州银行与纸币失序','w-en-free-banking')],
  schools=[('汉密尔顿视角','国家银行是统一信用与经济现代化的必要工具','w-en-first-bank'),
           ('杰斐逊视角','集中的金融权力威胁民主与州权','w-en-second-bank')],
  srcs=['w-en-first-bank','w-en-second-bank']),
 dict(id='overend-gurney', title='Overend, Gurney 倒闭(1866)', cat='银行', region='欧洲',
  unit='U2 18—19世纪', per='18—19世纪', tier='重要',
  ol='伦敦"银行的银行"1866年倒闭，欠债约1100万英镑（≈2025年11.32亿），直接触发1866年恐慌。',
  ov=('Overend, Gurney and Company 是一家伦敦的**批发贴现银行**，被称为"**银行的银行**"(the bankers\' bank)。'
   '该行于 **1866 年** 倒闭，**欠债约 1100 万英镑——相当于 2025 年的 11.32 亿英镑**。'
   '其倒闭**直接触发了银行恐慌**（见 panic-1866）。'
   '该事件的重要性有三层：'
   '①**规模与关联性**——它作为批发贴现银行，是众多银行流动性的来源，'
   '其倒闭使"关联度"而非"规模"成为系统性风险的核心；'
   '②**有限责任与治理**——该行在倒闭前不久才转为有限责任公司，'
   '财务不透明与治理失误（包括对单一行业的过度敞口）被广泛批评；'
   '③**最后贷款人的确立**——恐慌中的流动性枯竭使英格兰银行在事后明确承担最后贷款人角色，'
   '白芝浩的《伦巴第街》(1873) 即以此类经验为基础写成（见 lender-of-last-resort）。'
   '该案例是"批发融资银行＋高关联度"型危机的早期原型。具体细节待核实。'),
  tl=[
   {'year':1866,'display':'1866年','event':'Overend, Gurney 倒闭，欠债约1100万英镑（≈2025年11.32亿），触发银行恐慌','sources':['w-en-overend-gurney']},
   {'year':1873,'display':'1873年','event':'白芝浩《伦巴第街》出版，系统阐述最后贷款人原则（年份待核实）','sources':['w-en-lender-of-last-resort']},
  ],
  causal=[('批发贴现银行成为众多银行的流动性来源 → 高关联度','w-en-overend-gurney'),
         ('财务不透明 + 治理失误 → 1866年倒闭（欠债约1100万英镑）','w-en-overend-gurney'),
         ('流动性枯竭引发恐慌 → 英格兰银行明确最后贷款人角色','w-en-lender-of-last-resort')],
  schools=[('关联度视角','系统性风险来自关联度而非单体规模','w-en-overend-gurney'),
           ('最后贷款人视角','恐慌中需央行以良好抵押品自由放贷以止住挤兑','w-en-lender-of-last-resort')],
  srcs=['w-en-overend-gurney','w-en-lender-of-last-resort']),
 dict(id='indexation', title='指数化', cat='制度', region='全球',
  unit='U6 理论与制度', per='理论制度', tier='补充',
  ol='以价格指数调整收入支付以维持购买力的技术；解除该安排称"去指数化"。',
  ov=('指数化(indexation) 是一种**以价格指数调整收入支付、从而在高通胀后维持公众购买力**的技术；'
   '而**去指数化(deindexation)** 则是解除这一安排的过程。'
   '它常被用于使工资、养老金、债券利息与租约等随物价调整。'
   '在危机语境中，指数化具有**两面性**：'
   '①**缓冲作用**——在高通胀中保护实际收入与债务关系的可预期性；'
   '②**惯性作用**——一旦工资与价格普遍挂钩，通胀便获得自我延续的动能（"通胀惯性"），'
   '使反通胀的成本大幅上升。巴西1980—1990年代的恶性通胀（见 brazil-hyper-1980）'
   '即被视为指数化惯性的典型案例，其终结（1994年雷亚尔计划）需要同时切断指数化与财政赤字。'
   '因此稳定化方案（见 stabilization-program）常把"去指数化"作为核心步骤之一。具体机制待核实。'),
  tl=[],
  causal=[('高通胀侵蚀实际收入 → 以价格指数调整工资/利息/养老金','w-en-indexation'),
         ('普遍挂钩 → 通胀具备惯性，自我延续','w-en-hyperinflation-in-brazil'),
         ('反通胀需同时"去指数化"与调整财政 → 否则紧缩成本极高','w-en-stabilization-policy')],
  schools=[('保护视角','指数化在高通胀中维持购买力与契约公平','w-en-indexation'),
           ('惯性视角','普遍指数化使通胀难以自行消退，是稳定化的主要障碍','w-en-hyperinflation-in-brazil')],
  srcs=['w-en-indexation','w-en-hyperinflation-in-brazil']),
 dict(id='interest-rate-risk', title='利率风险', cat='理论', region='全球',
  unit='U6 理论与制度', per='理论制度', tier='补充',
  ol='利率波动导致金融损失的潜在风险；对债券、银行与保险公司的作用机制各不相同。',
  ov=('利率风险(interest rate risk) 指**因利率波动而遭受潜在财务损失**的风险。'
   '该风险对不同主体的作用方式不同：'
   '对**债券**持有人，利率上升使既有债券价格下跌（久期越长、跌幅越大）；'
   '对**银行**，利率上升可能压缩净息差、并使持有的固定利率资产市值下跌'
   '（硅谷银行2023年倒闭的核心即在于此，见 silicon-valley-bank）；'
   '对**保险公司与养老金**，利率变动同时影响资产与负债的现值，久期错配会放大缺口'
   '（英国LDI危机2022即为此机制，见 uk-ldi-crisis-2022）。'
   '在低利率长期持续后，机构往往积累了大量长久期固定利率资产与隐性杠杆，'
   '此时利率快速上行会把"账面浮亏"转化为"实际偿付危机"——'
   '这正是2022—2023年多起银行与养老金事件的共同脉络。具体度量方法待核实。'),
  tl=[],
  causal=[('低利率期积累长久期固定利率资产 → 久期错配','w-en-interest-rate-risk'),
         ('利率快速上行 → 资产市值下跌、浮亏扩大','w-en-silicon-valley-bank'),
         ('浮亏触及偿付或抵押要求 → 被迫抛售/挤兑（LDI与SVB）','w-en-uk-ldi')],
  schools=[('资产负债表视角','利率风险以市值为口径衡量，浮亏即真实损失','w-en-silicon-valley-bank'),
           ('银行账簿视角','持有至到期资产可按摊余成本计量，浮亏不立即体现（争议）','w-en-interest-rate-risk')],
  srcs=['w-en-interest-rate-risk','w-en-silicon-valley-bank']),
]

HAVE = {json.load(open(f, encoding='utf-8'))['title'] for f in glob.glob('data/entries/*.json')}
for sp in D:
    if sp['title'] in HAVE:
        print('跳过重复标题', sp['id'], sp['title']); continue
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': sp['per'], 'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sp['tl'],
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': [],
        'schools': [{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[src]}
                    for h,v,src in sp['schools']],
        'policy_response': [], 'comparison': '',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基摘要与标准口径；单源待核实。【续作DB】'
    }
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'], '|', sp['per'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r113.json', encoding='utf-8'))
MAP = {'first-bank':'w-en-first-bank','overend-gurney':'w-en-overend-gurney',
       'indexation':'w-en-indexation','interest-rate-risk':'w-en-interest-rate-risk'}
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
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':sp['tier'],'status':'written',
      'source_count':2,'needs_verification':1,'last_updated':'2026-11-24',
      'unit':sp['unit'],'period':sp['per'],'region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
