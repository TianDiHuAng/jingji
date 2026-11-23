# -*- coding: utf-8 -*-
"""续作：6条概念L1→L2（据已有来源,标准口径,网络无关）。"""
import json
def svg(t,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(t)}：概念示意</text>"]
    for x,lb in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)
D={
 'animal-spirits':{'cat':'理论',
  'causal':[('不确定性 → 信心与预期波动','bk-the-general-theory-of-employment-interest-and-mo'),('动物精神驱动投资与消费 → 总需求波动','w-en-business-cycle'),('信心逆转 → 繁荣转衰退','w-en-financial-crisis')],
  'schools':[('凯恩斯主义视角','心理与预期是投资波动的重要来源','bk-the-general-theory-of-employment-interest-and-mo'),('行为经济学视角','情绪与认知偏差影响金融决策','w-en-business-cycle')]},
 'moral-hazard':{'cat':'理论',
  'causal':[('存在保险/救助预期 → 一方承担风险的后果部分由他人承担','w-en-moral-hazard'),('受保护方改变行为、承担更多风险','w-en-moral-hazard'),('系统性风险上升(如存款保险与救助的道德风险)','w-en-deposit-insurance')],
  'schools':[('道德风险视角','保护会诱使过度冒险，需激励相容设计','w-en-moral-hazard'),('制度设计视角','以资本要求/监管缓释道德风险','w-en-deposit-insurance')]},
 'too-big-to-fail':{'cat':'制度',
  'causal':[('机构规模大、关联性强 → 倒闭会引发系统性风险','w-en-too-big-to-fail'),('政府倾向救助 → 隐性担保','w-en-too-big-to-fail'),('诱发道德风险与不公平竞争','w-en-systemic-risk')],
  'schools':[('系统性风险视角','大机构倒闭外溢巨大，故被救助','w-en-too-big-to-fail'),('道德风险视角','隐性担保鼓励冒险，需处置框架','w-en-moral-hazard')]},
 'impossible-trinity':{'cat':'货币',
  'causal':[('固定汇率+资本自由流动+独立货币政策三者不可兼得','w-en-currency-crisis'),('须放弃其一(如牺牲汇率稳定或资本管制)','w-en-monetary-policy'),('制度选择影响货币危机风险','w-en-currency-crisis')],
  'schools':[('三元悖论视角','三目标最多取其二','w-en-currency-crisis'),('政策选择视角','按国情权衡汇率与资本账户','w-en-monetary-policy')]},
 'banking-school':{'cat':'理论',
  'causal':[('19世纪英国关于银行券发行与货币供给的争论','w-en-currency-school'),('银行学派主张按"真实票据"灵活发行、反对僵化规则','w-en-currency-school'),('与通货学派对立，影响后世央行理论','w-en-central-bank')],
  'schools':[('银行学派','货币供给应随贸易需要灵活调整','w-en-currency-school'),('通货学派','应严格限制发行以稳定物价','w-en-central-bank')]},
 'coordination-games':{'cat':'理论',
  'causal':[('经济主体的选择相互依赖 → 多重均衡可能','w-en-coordination-game'),('预期与协调失灵 → 挤兑/恐慌等坏均衡','w-en-coordination-game'),('政策/制度可促成好均衡','w-en-financial-crisis')],
  'schools':[('协调博弈视角','危机可理解为协调失败的坏均衡','w-en-coordination-game'),('宏观/政策视角','政策协调可引导至好均衡','w-en-financial-crisis')]},
}
for eid,sp in D.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'; d['crisis_type']=sp['cat'] if eid not in ('impossible-trinity',) else d.get('crisis_type','货币')
    d['causal_chain']=[{'step':s,'sources':[src]} for s,src in sp['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据来源/标准口径归纳；具体表述待核实','sources':[src]} for h,v,src in sp['schools']]
    if not d.get('policy_response'): d['policy_response']=[{'holder':'政策当局','view':'应对/制度设计及效果待核实','basis':'需多来源印证','sources':[d['sources'][0]]}]
    if not d.get('comparison'): d['comparison']='经济学/金融概念，与其他概念互补；具体争论待核实。'
    if not d.get('svg'): d['svg']=svg(d['title'],[sp['causal'][0][0][:12],sp['causal'][1][0][:12],sp['causal'][2][0][:12]])
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【续作】升L2。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'->L2')
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in D: e['level']='L2'; e['last_updated']='2026-11-23'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('done')
