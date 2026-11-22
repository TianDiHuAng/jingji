# -*- coding: utf-8 -*-
"""经济学与金融知识扩充 批次2：金融概念/工具(9)，重要级L2，据库内verified来源。"""
import json
def svg(title,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:22]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：概念示意</text>"]
    for x,t in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(t)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准金融口径。</text></svg>")
    return ''.join(s)
D=[
 ('collateralized-debt-obligation','债务抵押债券(CDO)','制度',
  '将多类债务(如MBS、贷款)分层打包、按优先级分配现金流的结构化证券。',
  '债务抵押债券(CDO)把多种债务资产汇入资产池，按优先级/次级等分层发行，不同层级承担不同违约风险与收益。次级CDO在2008年放大了次贷风险。其分层与评级问题待核实。',
  [('汇集多类债务资产 → 形成资产池','w-en-collateralized-debt-obligation'),('按优先级分层发行、分配现金流','w-en-collateralized-debt-obligation'),('底层违约上升 → 次级层先受损、风险传导','w-en-subprime-mortgage-crisis')],
  [('结构化/分散视角','分层满足不同风险偏好、理论分散风险','w-en-collateralized-debt-obligation'),('复杂性/信息不对称视角','模型与评级失准放大系统性风险','w-en-systemic-risk')],
  ['w-en-collateralized-debt-obligation','w-en-subprime-mortgage-crisis']),
 ('subprime-lending','次级贷款','制度',
  '向信用记录较弱借款人发放的高利率、较高风险贷款。',
  '次级贷款指向信用评分较低、还款能力较弱的借款人发放的贷款，利率较高。2000年代美国次级房贷扩张、叠加证券化，构成2008年危机的核心。具体标准与规模待核实。',
  [('向低信用借款人放贷 → 高利率、高违约风险','w-en-subprime-lending'),('贷款经证券化打包出售 → 风险扩散至投资者','w-en-mortgage-backed-security'),('房价下跌/利率重设 → 违约潮与危机','w-en-subprime-mortgage-crisis')],
  [('普惠/创新视角','扩大住房融资可得性','w-en-subprime-lending'),('风险/监管视角','放松标准与证券化放大系统性风险','w-en-systemic-risk')],
  ['w-en-subprime-lending','w-en-subprime-mortgage-crisis']),
 ('sovereign-default','主权违约','债务',
  '一国政府未能按期偿付其主权债务本息。',
  '主权违约指政府无法或不愿履行债务偿付义务，可能表现为拒付、重组或贬值偿还。与私人债务不同，主权债缺乏超国家强制执行机制，重组常通过谈判进行。案例与机制待核实。',
  [('财政赤字与外债累积 → 偿付能力受质疑','w-en-debt-crisis'),('融资成本上升/收入下降 → 违约暴露','w-en-sovereign-default'),('违约或重组 → 债权人损失与传染','w-en-financial-contagion')],
  [('偿付能力视角','根本源于财政与外部失衡','w-en-debt-crisis'),('偿付意愿/制度视角','强调政治意愿与债权人协调','w-en-sovereign-default')],
  ['w-en-sovereign-default','w-en-debt-crisis']),
 ('credit-crunch','信贷紧缩','银行',
  '银行因资本受损或风险上升而大幅收紧放贷的情形。',
  '信贷紧缩指银行因资本充足率下降、不良上升或不确定性而急剧收缩信贷供给，导致企业与家庭融资困难，加剧实体经济的下行。常在金融危机后出现。具体度量待核实。',
  [('危机致银行资本受损/风险厌恶上升','w-en-credit-crunch'),('银行收紧放贷标准、信贷供给下降','w-en-credit-crunch'),('企业投资与消费受抑 → 经济下行','w-en-recession')],
  [('金融加速器视角','信贷紧缩与资产价格下跌相互强化','w-en-credit-crunch'),('政策视角','央行/政府需注入流动性缓解','w-en-lender-of-last-resort')],
  ['w-en-credit-crunch','w-en-recession']),
 ('bank-failure','银行倒闭','银行',
  '银行因资不抵债或流动性枯竭而无法持续经营、被关闭或接管。',
  '银行倒闭指银行无法偿付存款人或满足监管资本要求而停业、被接管或清算。因银行高杠杆与期限转换特性，单家倒闭可能引发挤兑与传染。存款保险与处置机制旨在降低冲击。案例待核实。',
  [('资产损失/挤兑 → 银行偿付能力恶化','w-en-bank-run'),('监管接管或清算 → 银行倒闭','w-en-bank-failure'),('信心传染 → 其他银行承压','w-en-financial-contagion')],
  [('微观审慎视角','源于单家银行的风险管理失败','w-en-bank-failure'),('系统性视角','银行关联与挤兑致连锁失败','w-en-systemic-risk')],
  ['w-en-bank-failure','w-en-bank-run']),
 ('systemic-risk','系统性风险','银行',
  '金融体系中因机构关联与共同暴露而导致整体不稳定的风险。',
  '系统性风险指金融体系整体（而非单个机构）发生失灵的风险，源于机构间的关联、共同暴露与信心传染，可能造成广泛的金融与经济损害。是宏观审慎监管的核心关注。具体度量待核实。',
  [('机构关联/共同暴露 → 局部冲击扩散','w-en-systemic-risk'),('信心传染与去杠杆 → 系统性压力','w-en-financial-contagion'),('系统性危机 → 广泛经济损害','w-en-financial-crisis')],
  [('关联性视角','“太大而不能倒”与网络关联放大风险','w-en-too-big-to-fail'),('宏观审慎视角','需逆周期资本等工具防范','w-en-systemic-risk')],
  ['w-en-systemic-risk','w-en-financial-contagion']),
 ('speculative-bubble','投机泡沫','泡沫',
  '资产价格显著偏离基本面、由投机预期驱动的上涨后崩盘现象。',
  '投机泡沫指资产价格因投机性买盘与乐观预期而远超其基本面价值，最终破裂回落的现象。成因涉及信贷扩张、羊群行为与预期自我强化。泡沫的识别与界定存在争议。案例众多。',
  [('信贷可得+乐观叙事 → 资产价格上涨','w-en-speculative-bubble'),('价格上涨自我强化 → 更多投机入场','w-en-speculative-bubble'),('信心逆转 → 价格崩盘','w-en-financial-crisis')],
  [('非理性泡沫视角','群体投机使价格脱离基本面','w-en-speculative-bubble'),('有效市场视角','价格多数可由基本面解释、泡沫难判定','w-en-financial-crisis')],
  ['w-en-speculative-bubble','w-en-financial-crisis']),
 ('debt-crisis','债务危机','债务',
  '债务人（国家、企业或家庭）债务负担过重、难以偿付而引发的危机。',
  '债务危机指债务累积超出偿付能力、在冲击下暴露违约风险而引发的危机，可发生于主权、银行、企业或家庭部门。常与通缩、货币贬值或重组相伴。机制与案例待核实。',
  [('举债扩张+偿付假设 → 债务累积','w-en-debt-crisis'),('利率上升/收入下降 → 偿付困难暴露','w-en-sovereign-default'),('违约或去杠杆 → 收缩与传染','w-en-financial-contagion')],
  [('债务周期视角','过度负债与通缩相互强化','w-en-debt-crisis'),('资产负债表视角','去杠杆引发衰退','w-en-recession')],
  ['w-en-debt-crisis','w-en-sovereign-default']),
 ('initial-public-offering','首次公开募股(IPO)','制度',
  '企业首次向公众发行股票并在证券交易所上市的融资过程。',
  '首次公开募股(IPO)是企业首次向公众发行股票、在交易所挂牌上市的过程，为企业融资并为早期投资者提供退出渠道。IPO定价、抑价与市场时机是研究主题。具体机制待核实。',
  [('企业决定上市 → 承销与路演定价','w-en-initial-public-offering'),('向公众发行新股、挂牌交易','w-en-initial-public-offering'),('融资与股权分散；估值受市场情绪影响','w-en-speculative-bubble')],
  [('融资成长视角','IPO为企业提供成长资本与流动性','w-en-initial-public-offering'),('市场情绪视角','IPO热潮常与估值泡沫相伴','w-en-speculative-bubble')],
  ['w-en-initial-public-offering','w-en-speculative-bubble']),
]
for eid,title,cat,ol,ov,causal,schools,srcs in D:
    entry={'id':eid,'title':title,'level':'L2','tier':'重要','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':cat,
      'one_line':ol,'overview':ov,'timeline':[],
      'causal_chain':[{'step':st,'sources':[s]} for st,s in causal],'key_data':[],
      'schools':[{'holder':h,'view':v,'basis':'据维基原题/标准金融口径归纳；具体表述待核实','sources':[s]} for h,v,s in schools],
      'policy_response':[],'comparison':'金融概念条目，与其他概念互补；具体适用待核实。',
      'svg':svg(title,[causal[0][0][:14],causal[1][0][:14],causal[2][0][:14]]),
      'sources':srcs,'related':[],'needs_verification':True,
      'pending_notes':'概念条目：定义/机理据标准口径与维基来源，具体数据与细节待核实。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('新增',eid)
cov=json.load(open('coverage.json',encoding='utf-8')); have={e['id'] for e in cov['entries']}
for eid,title,cat,ol,ov,causal,schools,srcs in D:
    if eid in have: continue
    cov['entries'].append({'id':eid,'level':'L2','tier':'重要','status':'written','source_count':len(srcs),'needs_verification':1,'last_updated':'2026-11-22','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':cat})
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage total',cov['total'])
