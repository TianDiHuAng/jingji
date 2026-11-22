# -*- coding: utf-8 -*-
"""经济学与金融知识扩充 批次3：6条基础概念(央行独立性/恶性通胀/货币危机/凯恩斯主义/创造性破坏/美联储)。"""
import json
def svg(title,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:22]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：概念示意</text>"]
    for x,t in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(t)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)
D=[
 ('central-bank-independence','央行独立性','制度',
  '中央银行在制定货币政策时不受政府短期政治压力影响的程度。',
  '央行独立性指央行在设定利率等货币政策时保持相对自主、免受政治干预的制度安排。支持者认为其有助于锚定通胀预期、提升政策可信度；亦需相应的问责与透明度。不同国家的制度设计差异较大，待核实。',
  [('赋予央行法定独立授权 → 减少政治周期干扰','w-en-central-bank-independence'),('独立设定货币政策 → 稳定通胀预期','w-en-central-bank-independence'),('配合问责与透明度','w-en-central-bank')],
  [('独立论视角','独立有助于可信度与物价稳定','w-en-central-bank-independence'),('约束论视角','需平衡独立性与民主问责','w-en-central-bank')],
  ['w-en-central-bank-independence','w-en-central-bank']),
 ('hyperinflation','恶性通货膨胀','理论',
  '物价以极高速度持续上涨、货币迅速丧失价值的极端通胀。',
  '恶性通货膨胀指物价在极短时间内成倍飙升、货币职能（计价、交易、储藏）严重受损的极端通胀，通常与财政赤字货币化、战争或制度崩溃相关。学界常用"月度通胀超过50%"等阈值界定。具体阈值与案例待核实。',
  [('财政赤字货币化/供给崩溃 → 货币超发','w-en-hyperinflation'),('通胀预期失控 → 货币流通速度上升、价格加速','w-en-inflation'),('货币失序 → 货币改革或美元化','w-en-hyperinflation')],
  [('货币主义视角','恶性通胀是极端的货币现象','w-en-hyperinflation'),('财政视角','赤字货币化是根本驱动','w-en-inflation')],
  ['w-en-hyperinflation','w-en-inflation']),
 ('currency-crisis','货币危机','货币',
  '一国货币遭遇大规模抛售、急剧贬值或被迫放弃固定汇率的情形。',
  '货币危机指市场对某货币信心崩溃，导致其大幅贬值、外汇储备耗尽或被迫放弃钉住汇率的情形，常与固定汇率高估、资本外逃与投机攻击相关。是新兴市场危机的典型形态。具体机制待核实。',
  [('固定汇率高估+资本外流 → 贬值压力','w-en-currency-crisis'),('投机攻击消耗储备 → 被迫贬值或放弃钉住','w-en-currency-devaluation'),('贬值引发债务与通胀压力','w-en-monetary-policy')],
  [('第一/二代危机模型视角','基本面或预期自我实现导致攻击','w-en-currency-crisis'),('传染视角','危机在区域间传染','w-en-financial-contagion')],
  ['w-en-currency-crisis','w-en-currency-devaluation']),
 ('keynesian-economics','凯恩斯主义','理论',
  '强调总需求、主张政府干预以对抗衰退的宏观经济学流派。',
  '凯恩斯主义源于凯恩斯《就业、利息和货币通论》，认为总需求不足会导致非自愿失业与经济停滞，主张在衰退时以财政与货币政策扩张需求。与古典/新古典学派在政府角色上存在长期争论。具体论述待核实。',
  [('总需求不足 → 非自愿失业与经济低于潜在产出','bk-the-general-theory-of-employment-interest-and-mo'),('财政/货币政策扩张 → 提振总需求','w-en-fiscal-policy'),('乘数效应 → 产出与就业回升','w-en-fiscal-policy')],
  [('凯恩斯视角','市场不能自动出清，需政府干预','bk-the-general-theory-of-employment-interest-and-mo'),('新古典视角','长期趋于均衡，干预效果有限','w-en-monetary-policy')],
  ['bk-the-general-theory-of-employment-interest-and-mo','w-en-fiscal-policy']),
 ('creative-destruction','创造性破坏','理论',
  '熊彼特提出的概念：创新不断淘汰旧产业与旧企业、推动经济演化的过程。',
  '创造性破坏由熊彼特提出，指企业家创新在创造新产业的同时不断摧毁旧结构与既得利益，是资本主义演进的动力。该视角强调创新与企业家精神对长期增长的驱动。具体论述待核实。',
  [('企业家创新 → 新产品/新工艺/新市场','bk-capitalism-socialism-and-democracy'),('新技术替代旧技术 → 旧产业与就业受冲击','bk-capitalism-socialism-and-democracy'),('结构性调整 → 长期生产率提升与经济演化','w-en-recession')],
  [('熊彼特视角','创新与企业家是演化核心动力','bk-capitalism-socialism-and-democracy'),('主流增长视角','强调技术与全要素生产率','w-en-recession')],
  ['bk-capitalism-socialism-and-democracy','w-en-recession']),
 ('federal-reserve','美国联邦储备系统(美联储)','制度',
  '美国的中央银行体系，负责货币政策、金融稳定与银行监管。',
  '美国联邦储备系统（美联储）是美国的中央银行，承担制定货币政策、维护金融稳定、监管银行与提供支付清算等职能，由理事会与12家地区储备银行组成。其独立性、决策框架与历史演变待核实。',
  [('国会授权设立 → 央行体系与地区储备银行','w-en-federal-reserve'),('以货币政策调节利率与货币供给','w-en-monetary-policy'),('危机中行使最后贷款人/流动性支持职能','w-en-lender-of-last-resort')],
  [('独立性视角','相对独立于政治以稳定物价','w-en-central-bank-independence'),('职能视角','兼顾物价稳定、就业与金融稳定','w-en-federal-reserve')],
  ['w-en-federal-reserve','w-en-central-bank']),
]
for eid,title,cat,ol,ov,causal,schools,srcs in D:
    entry={'id':eid,'title':title,'level':'L2','tier':'重要','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':cat,
      'one_line':ol,'overview':ov,'timeline':[],
      'causal_chain':[{'step':st,'sources':[s]} for st,s in causal],'key_data':[],
      'schools':[{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[s]} for h,v,s in schools],
      'policy_response':[],'comparison':'经济学/制度概念条目，与其他概念互补；具体争论待核实。',
      'svg':svg(title,[causal[0][0][:14],causal[1][0][:14],causal[2][0][:14]]),
      'sources':srcs,'related':[],'needs_verification':True,
      'pending_notes':'概念条目：定义/机理据来源与标准口径，具体数据与细节待核实。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('新增',eid)
cov=json.load(open('coverage.json',encoding='utf-8')); have={e['id'] for e in cov['entries']}
for eid,title,cat,ol,ov,causal,schools,srcs in D:
    if eid in have: continue
    cov['entries'].append({'id':eid,'level':'L2','tier':'重要','status':'written','source_count':len(srcs),'needs_verification':1,'last_updated':'2026-11-22','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':cat})
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage total',cov['total'])
