# -*- coding: utf-8 -*-
"""续作CU：新增 Continental Illinois/Penn Square/Franklin National/阿尔巴尼亚金字塔 + 结算风险概念。"""
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
 dict(id='continental-illinois-1984', title='伊利诺伊大陆银行救助(1984)', cat='银行',
  unit='U4 20世纪下半', region='北美', tier='重要',
  ol='美国第七大银行因不良能源贷款与挤兑濒临倒闭，监管首创"太大而不能倒"式全面保护。',
  ov=('伊利诺伊大陆银行(Continental Illinois National Bank and Trust Company) 1910年成立，'
   '鼎盛时期按存款计是美国**第七大**商业银行，资产约 **400亿美元**。'
   '1984年该行陷入危机：其不良能源贷款（大量来自对 Penn Square Bank 的贷款参与，见该条目）'
   '与批发存款的脆弱结构叠加，引发对它的挤兑——在当时，这是美国历史上最大的银行倒闭/救助案之一。'
   '其制度意义在于监管的应对方式：联邦存款保险公司(FDIC) 破例对**所有存款人（含超过保险限额者）**提供保护，'
   '并注入资本、更换管理层，实质上宣告了"**太大而不能倒**"(too big to fail) 的实践先例。'
   '该案例常与 Penn Square、储贷危机（见 savings-loan-1986）串联讨论，'
   '也成为此后"系统性重要机构"监管与处置框架讨论的起点。'
   '值得注意的内部治理问题：该行贷款官员 Lytle 后来承认诈骗该行 **225万美元**、'
   '并为批准高风险贷款收取 **58.5万美元**回扣。具体救助金额与结构待核实。'),
  tl=[
   {'year':1910,'display':'1910年','event':'两家银行合并为 Continental & Commercial National Bank of Chicago（存款1.75亿美元）','sources':['w-en-continental-illinois']},
   {'year':1982,'display':'1982年','event':'Penn Square 倒闭暴露贷款参与损失','sources':['w-en-penn-square']},
   {'year':1984,'display':'1984年','event':'危机爆发，FDIC 全面保护存款人并注资','sources':['w-en-continental-illinois']},
  ],
  causal=[('大额能源贷款参与（含Penn Square）→ 资产质量恶化','w-en-penn-square'),
         ('批发存款为主的结构 + 信心丧失 → 挤兑式资金外流','w-en-continental-illinois'),
         ('FDIC 对所有存款人（含超限额）提供保护 → 形成"太大而不能倒"先例','w-en-continental-illinois')],
  schools=[{'holder':'系统性风险视角','view':'大型银行倒闭的溢出成本超过救助成本，全覆盖保护是不得已','basis':'据监管选择归纳','sources':['w-en-continental-illinois']},
           {'holder':'道德风险视角','view':'全面保护削弱市场约束，为后续更大规模救助埋下伏笔','basis':'据后续危机经验归纳；因果待核实','sources':['w-en-bailout']}],
  kd=[
   {'label':'大陆伊利诺伊资产规模(鼎盛)','value':40,'unit':'十亿美元（约400亿）','year':1984,'comparable_price':False,
    'note':'原文：at its peak the seventh-largest commercial bank in the United States as measured by deposits, with approximately $40 billion in assets；单一来源待核实。','sources':['w-en-continental-illinois']},
   {'label':'贷款官员诈骗金额','value':2.25,'unit':'百万美元（另收回扣58.5万）','year':1982,'comparable_price':False,
    'note':'原文：Lytle later pleaded guilty to a count of defrauding Continental of $2.25 million and receiving $585,000 in kickbacks；单一来源待核实。','sources':['w-en-continental-illinois']},
  ],
  cmp=('与2008年雷曼（被放任倒闭）形成对照：大陆伊利诺伊的"全保"与雷曼的"不救"是危机处置光谱的两端。'
   '与北岩银行(2007)同为批发融资依赖型银行的挤兑样本。具体异同待核实。')),
 dict(id='penn-square-1982', title='Penn Square 银行倒闭(1982)', cat='银行',
  unit='U4 20世纪下半', region='北美', tier='补充',
  ol='俄克拉何马小银行以不审慎能源贷款并转售"贷款参与"，倒闭后拖累多家大银行。',
  ov=('Penn Square Bank 是位于俄克拉何马城的一家小型美国商业银行。'
   '它发放了大量**审慎不足的能源相关贷款**，并将这些贷款转售给其他银行（"贷款参与"）。'
   '这些贷款上的损失使买入方银行陷入严重问题——'
   '**该行常被认为部分导致了芝加哥伊利诺伊大陆银行(Continental Illinois)的崩溃**，后者不得不冲销相关损失。'
   '其扩张速度本身即是警示：**1974至1982年间，该行资产增长超过15倍至5.25亿美元，'
   '存款从2900万美元膨胀到4.5亿美元以上**；而为支撑这一切，它向全美其他银行出售了超过 **10亿美元** 的贷款参与。'
   '1982年该行倒闭。'
   '该案例是"**发起—分销**"(originate-to-distribute) 模式风险的早期样本：'
   '放贷机构因能把贷款卖出去而丧失审慎动机，风险则被传递给对其一无所知的买入方。具体细节待核实。'),
  tl=[
   {'year':1982,'display':'1974—1982年','event':'资产增长超15倍至5.25亿美元，存款由2900万增至4.5亿以上','sources':['w-en-penn-square']},
   {'year':1982,'display':'1982年','event':'银行倒闭，拖累买入贷款参与的多家银行','sources':['w-en-penn-square']},
  ],
  causal=[('能源景气 + 可转售贷款 → 放贷标准放松','w-en-penn-square'),
         ('向其他银行出售超10亿美元贷款参与 → 风险扩散至买入方','w-en-penn-square'),
         ('能源价格回落 → 贷款损失，银行倒闭并拖累大银行','w-en-penn-square')],
  schools=[{'holder':'激励扭曲视角','view':'贷款可转售使发起方丧失审慎动机，是证券化风险的雏形','basis':'据贷款参与模式归纳','sources':['w-en-penn-square']},
           {'holder':'集中度视角','view':'能源行业贷款的高度集中是损失放大的主因','basis':'据贷款结构归纳','sources':['w-en-penn-square']}],
  kd=[
   {'label':'资产规模(1982)','value':525,'unit':'百万美元（增长超15倍）','year':1982,'comparable_price':False,
    'note':'原文：Between 1974 and 1982, the bank\'s assets increased more than 15 times to $525 million；单一来源待核实。','sources':['w-en-penn-square']},
   {'label':'存款规模增长(1974→1982)','value':450,'unit':'百万美元以上（由2900万起）','year':1982,'comparable_price':False,
    'note':'原文：its deposits swelled from $29 million to more than $450 million；单一来源待核实。','sources':['w-en-penn-square']},
   {'label':'出售给其他银行的贷款参与规模','value':1,'unit':'十亿美元以上（超10亿）','year':1982,'comparable_price':False,
    'note':'原文：the sale of over $1 billion in "loan participations" to other banks throughout Ameri[ca]；单一来源待核实。','sources':['w-en-penn-square']},
  ],
  cmp=('与2000年代的次级按揭证券化链条机制同源：把贷款卖出去 → 丧失审慎动机 → 风险由信息劣势方承担。'
   '区别在于1982年的工具是"贷款参与"而非MBS/CDO。具体异同待核实。')),
 dict(id='franklin-national-1974', title='Franklin National 银行倒闭(1974)', cat='银行',
  unit='U4 20世纪下半', region='北美', tier='补充',
  ol='美国第20大银行因外汇投机与欺诈损失倒闭，为当时美国史上最大银行倒闭案。',
  ov=('Franklin National Bank 是位于纽约长岛富兰克林广场的银行，曾是美国**第20大**银行。'
   '它于 **1974年10月8日** 在涉及**米凯莱·辛多纳**(Michele Sindona)——'
   '一位与黑手党有关联的银行家——的复杂情形中倒闭。'
   '关键事实链：辛多纳在外汇市场上遭受巨额亏损，'
   '遂决定**从银行诈取3000万美元**以弥补损失；'
   '**1974年中期**管理层披露巨额亏损，存款人开始大额提款，'
   '迫使该行向美联储借款超过 **10亿美元**。'
   '该行最终倒闭，在当时是美国历史上最大的银行倒闭案（此后被大陆伊利诺伊超越）。'
   '投资人劳伦斯·蒂施(Laurence Tisch) 曾持有 **22%** 股份并任副董事长。'
   '该案例的教训集中在**内控与治理**：单一控制人的外部投机损失可以通过关联交易与欺诈转嫁给银行；'
   '同时它也显示外汇交易风险如何迅速转化为流动性危机。具体细节待核实。'),
  tl=[
   {'year':1974,'display':'1974年中期','event':'披露巨额亏损，存款人大量提款，向美联储借款超10亿美元','sources':['w-en-franklin-national']},
   {'year':1974,'display':'1974年10月8日','event':'银行倒闭（当时美国史上最大银行倒闭案）','sources':['w-en-franklin-national']},
  ],
  causal=[('控股人辛多纳外汇投机巨亏 → 从银行诈取3000万美元弥补','w-en-franklin-national'),
         ('1974年中期披露巨额亏损 → 存款人挤兑','w-en-franklin-national'),
         ('向美联储借款超10亿美元仍不支 → 1974年10月8日倒闭','w-en-franklin-national')],
  schools=[{'holder':'治理视角','view':'单一控制人可借关联交易将私人损失转嫁给银行','basis':'据欺诈与亏损过程归纳','sources':['w-en-franklin-national']},
           {'holder':'市场风险视角','view':'外汇敞口未经对冲，是流动性危机的直接触发','basis':'据外汇亏损归纳','sources':['w-en-franklin-national']}],
  kd=[
   {'label':'辛多纳从银行诈取金额','value':30,'unit':'百万美元（3000万）','year':1974,'comparable_price':False,
    'note':'原文：decided to defraud the bank of $30,000,000 to cover his losses；单一来源待核实。','sources':['w-en-franklin-national']},
   {'label':'向美联储借款规模','value':1,'unit':'十亿美元以上（超10亿）','year':1974,'comparable_price':False,
    'note':'原文：causing the bank to have to borrow over $1 billion from the F[ed]；单一来源待核实。','sources':['w-en-franklin-national']},
  ],
  cmp=('与巴林银行1995年倒闭（见 barings-1995）结构相似：单一交易员的未经授权交易摧毁一家老牌银行；'
   '但Franklin的特殊性在于**控制人本人的欺诈**而非下属违规。具体异同待核实。')),
 dict(id='albania-pyramid-1997', title='阿尔巴尼亚金字塔骗局与1997年动乱', cat='泡沫',
  unit='U4 20世纪下半', region='欧洲', tier='重要',
  ol='金字塔集资规模达12亿美元、近GDP一半，崩盘后引发武装动乱与国家失序。',
  ov=('1997年阿尔巴尼亚的动乱在很大程度上由**多个金字塔集资骗局的失败**触发。'
   '这些骗局的规模相对该国经济达到**空前水平**，使大量阿尔巴尼亚人失去钱财与财产，'
   '最终演变为广泛抗议与武装动乱。'
   '规模数据触目惊心：**骗局负债的面值合计达 12亿美元，接近阿尔巴尼亚当时GDP的一半**。'
   '这一案例的独特之处在于**金融欺诈直接引发国家失序**：'
   '当庞氏结构无法支付"利息"时，储户（许多人卖房、卖地、甚至变卖牲畜参与）的损失'
   '转化为对政府的愤怒——政府此前未有效监管甚至被指默许。'
   '结果是秩序崩溃、武装抢劫军械库、大规模移民外流，直至国际干预与重建。'
   '该案例被广泛用于讨论"转轨经济体金融监管真空"与"庞氏骗局的宏观规模阈值"。'
   '具体骗局数量与破产时序待核实。'),
  tl=[
   {'year':1996,'display':'1990年代中期','event':'金字塔集资快速膨胀，规模达空前水平','sources':['w-en-albania-pyramid-schemes']},
   {'year':1997,'display':'1997年','event':'骗局崩盘（负债12亿美元≈GDP一半），引发武装动乱','sources':['w-en-albania-pyramid-schemes']},
  ],
  causal=[('转轨初期金融监管真空 + 高息承诺 → 金字塔集资迅速膨胀','w-en-albania-pyramid-schemes'),
         ('以新入资金支付旧"利息"（庞氏结构）→ 负债累积至12亿美元≈GDP一半','w-en-albania-pyramid-schemes'),
         ('资金链断裂 → 储户损失惨重、抗议升级为武装动乱与国家失序','w-en-albania-pyramid-schemes')],
  schools=[{'holder':'监管真空视角','view':'转轨期缺乏金融监管与投资者教育是骗局规模化的前提','basis':'据骗局规模与监管状况归纳','sources':['w-en-albania-pyramid-schemes']},
           {'holder':'社会后果视角','view':'当损失波及多数家庭时，金融问题必然政治化','basis':'据动乱过程归纳；因果待核实','sources':['w-en-albania-pyramid-schemes']}],
  kd=[
   {'label':'金字塔骗局负债面值合计','value':1.2,'unit':'十亿美元（12亿），≈GDP一半','year':1997,'comparable_price':False,
    'note':'原文：The face value of the schemes\' liabilities totaled $1.2 billion, nearly half of Albania\'s GDP at the time；单一来源待核实。','sources':['w-en-albania-pyramid-schemes']},
  ],
  cmp=('与2008年马多夫庞氏骗局相比，阿尔巴尼亚案的特点是**规模相对GDP极高**且**直接引发国家动乱**；'
   '马多夫案虽绝对金额更大，但集中于机构与富裕投资者。与苏克阿尔马纳克(1982)同属"非正规金融链条断裂"样本。具体异同待核实。')),
 dict(id='settlement-risk', title='结算风险(Herstatt风险)', cat='制度',
  unit='U6 理论与制度', region='全球', tier='补充',
  ol='交易对手在一方已交付证券或现金后未按约交付的风险，因1974年Herstatt银行倒闭而得名。',
  ov=('结算风险(settlement risk)，又称交付风险或对手方风险，'
   '指**一方已按约交付证券或现金价值后，交易对手（或中介代理）未能交付相应证券或现金的风险**。'
   '该术语涵盖多个因素（时区差异、支付系统运行时间、法律最终性等）。'
   '它也常被称为"**Herstatt风险**"：1974年德国 Herstatt 银行在德国当日营业结束时被关闭，'
   '而与其交易的对手方已在德国时段交付了德国马克，却因美国时段尚未开始而未能收到美元，'
   '由此暴露了**跨境外汇交易中"时间错配"的结算风险**（此背景为通说，具体细节待核实）。'
   '制度后果是**实时全额结算**(RTGS) 系统与"支付对支付"(PVP) 机制的推广，'
   '以及持续联结结算银行(CLS)的建立，用于消除外汇交易的结算本金风险。'
   '在衍生品领域，中央对手方清算(CCP) 也是应对对手方风险的主要制度安排。具体定义边界待核实。'),
  tl=[
   {'year':1974,'display':'1974年','event':'德国 Herstatt 银行倒闭，暴露跨境外汇结算的时间错配风险（通说）','sources':['w-en-settlement-risk']},
  ],
  causal=[('跨境交易双方支付在不同时区完成 → 存在"一方已付、另一方未付"的时间窗','w-en-settlement-risk'),
         ('该时间窗内交易对手违约 → 已交付方承担全额本金损失','w-en-settlement-risk'),
         ('以RTGS、PVP与中央对手方清算压缩该窗口 → 降低结算风险','w-en-settlement-risk')],
  schools=[{'holder':'基础设施视角','view':'结算风险主要靠支付系统与清算机制的设计来消除','basis':'据RTGS/PVP实践归纳','sources':['w-en-settlement-risk']},
           {'holder':'对手方视角','view':'即便有基础设施，交易对手信用仍需资本与保证金约束','basis':'据CCP制度归纳','sources':['w-en-settlement-risk']}],
  kd=[],
  cmp=('与"对手方信用风险"相关但不同：结算风险特指**本金交换过程中的时点风险**，'
   '其暴露是暂时的但金额是全额（而非差额）。具体辨析待核实。')),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': sp['tier'],
        'unit': sp['unit'], 'period': ('理论制度' if sp['unit'].startswith('U6') else sp['unit'].split(' ')[0].replace('U4','20世纪下半')),
        'region': sp['region'], 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': sorted(sp['tl'], key=lambda t:t.get('year',0)),
        'causal_chain': [{'step':s,'sources':[src]} for s,src in sp['causal']],
        'key_data': sp['kd'],
        'schools': sp['schools'],
        'policy_response': [],
        'comparison': sp['cmp'],
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys([s for _st,s in sp['causal']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：据维基全文；单源待核实。【续作CU】'
    }
    if entry['unit'].startswith('U6'):
        entry['period'] = '理论制度'
    json.dump(entry, open('data/entries/'+sp['id']+'.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'], '| period', entry['period'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r107_data.json', encoding='utf-8'))
MAP = {'continental-illinois-1984':'w-en-continental-illinois','penn-square-1982':'w-en-penn-square',
       'franklin-national-1974':'w-en-franklin-national','albania-pyramid-1997':'w-en-albania-pyramid-schemes',
       'settlement-risk':'w-en-settlement-risk'}
KEY = {'continental-illinois-1984':'continental-illinois','penn-square-1982':'penn-square',
       'franklin-national-1974':'franklin-national','albania-pyramid-1997':'albania-pyramid',
       'settlement-risk':'settlement-risk'}
for eid, sid in MAP.items():
    if sid in ex: continue
    v = meta.get(KEY[eid])
    if not v: print('meta缺', KEY[eid]); continue
    sd['sources'].append({'id':sid,'title':v['title'],'author':'Wikipedia contributors','year':'2026',
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+v['title'].replace(' ','_'),'url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia API(full extract)核对(本会话抓取)'})
    ex.add(sid); print('新增来源',sid)
sd['count']=len(sd['sources'])
json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for sp in D:
    if sp['id'] in have: continue
    cov['entries'].append({'id':sp['id'],'level':'L2','tier':sp['tier'],'status':'written',
      'source_count':1,'needs_verification':1,'last_updated':'2026-11-24',
      'unit':sp['unit'],'period':('理论制度' if sp['unit'].startswith('U6') else '20世纪下半'),
      'region':sp['region'],'crisis_type':sp['cat']})
cov['total']=len(cov['entries'])
json.dump(cov, open('coverage.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
