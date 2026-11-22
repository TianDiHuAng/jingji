# -*- coding: utf-8 -*-
"""经济学与金融知识扩充 批次1：经济学概念(7) + 金融工具(2)，重要级L2，据库内verified来源。"""
import json

def svg(title,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:22]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：概念示意</text>"]
    xs=[20,270,520]
    for x,t in zip(xs,labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(t)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准经济学口径。</text></svg>")
    return ''.join(s)

# (id,title,cat,one_line,overview,causal[(step,src)],schools[(holder,view,src)],srcs)
D=[
 ('inflation','通货膨胀','理论',
  '物价总水平持续上涨、货币购买力下降的现象。',
  '通货膨胀指经济中商品与服务的总体价格水平持续上升。按成因常分为需求拉动型与成本推动型；温和通胀被认为与经济增长相容，恶性通胀则破坏货币职能。具体度量（CPI等）与各经济体数据待核实。',
  [('总需求扩张或成本上升 → 物价上行压力','w-en-inflation'),('预期与工资-价格螺旋 → 通胀自我延续','w-en-inflation'),('货币政策收紧/锚定预期 → 通胀回落','w-en-monetary-policy')],
  [('货币主义视角','通胀是货币现象，货币供给增速决定物价长期走势','w-en-inflation'),('成本推动/结构视角','供给冲击与成本变化亦可推动物价','w-en-monetary-policy')],
  ['w-en-inflation','w-en-monetary-policy']),
 ('unemployment','失业','理论',
  '有劳动意愿与能力者未能找到工作的状态。',
  '失业指在现行工资下愿意工作却找不到工作的人口。经济学区分摩擦性、结构性、周期性失业；失业率是重要宏观指标。自然失业率与周期性波动的关系存在理论分歧。具体统计口径待核实。',
  [('总需求不足 → 周期性失业上升','w-en-unemployment'),('结构与技能错配 → 结构性失业','w-en-unemployment'),('政策（财政/货币）刺激 → 就业回升','w-en-fiscal-policy')],
  [('凯恩斯主义视角','总需求不足导致非自愿失业，需政策干预','w-en-fiscal-policy'),('古典/自然率视角','长期趋于自然失业率，政策影响有限','w-en-unemployment')],
  ['w-en-unemployment','w-en-business-cycle']),
 ('monetary-policy','货币政策','制度',
  '中央银行调节货币供给与利率以实现物价稳定等目标的政策。',
  '货币政策是央行通过利率、准备金、公开市场操作等工具调节货币与信贷条件的政策。目标通常包括物价稳定、充分就业与金融稳定；政策传导存在时滞。不同央行的目标框架（如通胀目标制）各异，具体待核实。',
  [('央行调整政策利率 → 市场利率与信贷条件变化','w-en-monetary-policy'),('总需求与汇率、资产价格随之调整','w-en-monetary-policy'),('最终影响通胀与产出','w-en-inflation')],
  [('规则vs相机抉择','政策应遵循规则还是灵活相机抉择存在长期争论','w-en-monetary-policy'),('通胀目标制视角','以锚定通胀预期为核心','w-en-inflation')],
  ['w-en-monetary-policy','w-en-central-bank']),
 ('fiscal-policy','财政政策','制度',
  '政府通过税收与支出调节总需求与经济活动的政策。',
  '财政政策指政府运用税收、公共支出与债务管理影响经济的政策。扩张性财政（增支减税）可刺激需求，紧缩性则相反；其效果受乘数、挤出效应与债务可持续性影响。具体乘数与财政规则待核实。',
  [('政府增减支出/税收 → 总需求变动','w-en-fiscal-policy'),('乘数效应传导至产出与就业','w-en-fiscal-policy'),('债务与利率的可持续性约束','w-en-debt-crisis')],
  [('凯恩斯视角','财政乘数显著，衰退期应扩张','w-en-fiscal-policy'),('李嘉图等价视角','理性预期下财政刺激效果有限','w-en-monetary-policy')],
  ['w-en-fiscal-policy','w-en-monetary-policy']),
 ('quantitative-easing','量化宽松','制度',
  '央行大规模购买资产以注入流动性、压低长期利率的非常规货币政策。',
  '量化宽松(QE)是政策利率接近零下限时的非常规工具：央行购买国债等资产，扩大资产负债表以注入流动性、压低长期利率并支持需求。其效果与副作用（资产价格、退出难度）存在争议。具体规模与操作待核实。',
  [('政策利率触零下限 → 常规工具失效','w-en-quantitative-easing'),('央行购买资产 → 流动性与长期利率下降','w-en-quantitative-easing'),('支持需求/资产价格；退出需谨慎','w-en-quantitative-tightening')],
  [('支持方视角','QE在危机中有效稳定市场与需求','w-en-quantitative-easing'),('质疑方视角','可能推高资产泡沫、加大退出难度','w-en-speculative-bubble')],
  ['w-en-quantitative-easing','w-en-monetary-policy']),
 ('quantitative-tightening','量化紧缩','制度',
  '央行缩减资产负债表、回收流动性的过程（量化宽松的反向）。',
  '量化紧缩(QT)是央行通过停止再投资或主动出售资产来收缩资产负债表、回收流动性的过程，是QE的退出。可能抬升长期利率、收紧金融条件，进程与节奏对市场影响存在争议。具体操作待核实。',
  [('结束资产再投资/出售资产 → 资产负债表收缩','w-en-quantitative-tightening'),('流动性与长期利率上行 → 金融条件收紧','w-en-quantitative-tightening'),('对增长与资产价格形成压力','w-en-monetary-policy')],
  [('稳健退出视角','缓慢可预期地缩表以减小冲击','w-en-quantitative-tightening'),('担忧视角','过快紧缩可能引发市场动荡','w-en-financial-crisis')],
  ['w-en-quantitative-tightening','w-en-monetary-policy']),
 ('real-business-cycle','真实经济周期理论','理论',
  '将经济周期主要归因于技术冲击等实际因素的新古典宏观理论。',
  '真实经济周期理论(RBC)认为经济波动主要源于技术等实际（供给）冲击，而非货币因素；在理性预期与市场出清的框架下，波动被视为对冲击的有效反应。该理论与凯恩斯主义在周期成因上存在根本分歧。',
  [('技术/生产率冲击 → 相对价格与产出变化','w-en-real-business-cycle-theory'),('理性主体跨期替代劳动与消费','w-en-real-business-cycle-theory'),('产出与就业随之波动','w-en-business-cycle')],
  [('RBC视角','波动主要来自实际冲击，市场大体出清','w-en-real-business-cycle-theory'),('凯恩斯视角','强调需求侧因素与市场不完全','w-en-fiscal-policy')],
  ['w-en-real-business-cycle-theory','w-en-business-cycle']),
 ('mortgage-backed-security','抵押贷款支持证券(MBS)','制度',
  '以一组住房抵押贷款的未来现金流为支撑发行的证券。',
  '抵押贷款支持证券(MBS)将众多住房抵押贷款打包、以其本息现金流为偿付来源发行给投资者，实现风险分散与流动性转换。次级MBS在2008年危机中扮演核心角色。其结构化与评级问题待核实。',
  [('银行发放房贷 → 打包成资产池','w-en-mortgage-backed-security'),('以池内现金流为支撑发行证券给投资者','w-en-mortgage-backed-security'),('房价下跌/违约上升 → 证券价值受损、风险传染','w-en-subprime-mortgage-crisis')],
  [('金融创新/分散风险视角','MBS分散风险、增加住房融资','w-en-mortgage-backed-security'),('风险放大视角','层层证券化与信息不对称放大系统性风险','w-en-systemic-risk')],
  ['w-en-mortgage-backed-security','w-en-subprime-mortgage-crisis']),
 ('credit-default-swap','信用违约互换(CDS)','制度',
  '一种转移信用风险的金融衍生合约：买方支付保费，在标的违约时获赔。',
  '信用违约互换(CDS)是信用风险转移工具：保护买方定期支付费用，若标的债务违约则由卖方赔付。它可用于对冲或投机，其集中与对手方风险在2008年危机中受关注。具体条款与规模待核实。',
  [('债权人购买CDS → 将违约风险转移给卖方','w-en-credit-default-swap'),('支付保费获得违约保护','w-en-credit-default-swap'),('违约时卖方赔付；集中持仓放大对手方风险','w-en-systemic-risk')],
  [('风险管理视角','CDS便于对冲与价格发现','w-en-credit-default-swap'),('系统性风险视角','不透明与高杠杆可能放大传染','w-en-systemic-risk')],
  ['w-en-credit-default-swap','w-en-systemic-risk']),
]
for eid,title,cat,ol,ov,causal,schools,srcs in D:
    entry={'id':eid,'title':title,'level':'L2','tier':'重要','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':cat,
      'one_line':ol,'overview':ov,'timeline':[],
      'causal_chain':[{'step':st,'sources':[s]} for st,s in causal],
      'key_data':[],
      'schools':[{'holder':h,'view':v,'basis':'据维基原题/标准经济学口径归纳；具体表述待核实','sources':[s]} for h,v,s in schools],
      'policy_response':[],'comparison':f'经济学/金融概念条目，与其他概念互补；具体适用与争论待核实。',
      'svg':svg(title,[causal[0][0][:14],causal[1][0][:14],causal[2][0][:14]]),
      'sources':srcs,'related':[],'needs_verification':True,
      'pending_notes':'概念条目：定义/机理据标准口径与维基来源，具体数据与学派细节待核实补充。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('新增',eid)

# coverage
cov=json.load(open('coverage.json',encoding='utf-8'))
have={e['id'] for e in cov['entries']}
for eid,title,cat,ol,ov,causal,schools,srcs in D:
    if eid in have: continue
    cov['entries'].append({'id':eid,'level':'L2','tier':'重要','status':'written','source_count':len(srcs),'needs_verification':1,'last_updated':'2026-11-22','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':cat})
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage total',cov['total'])
