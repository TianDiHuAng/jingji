# -*- coding: utf-8 -*-
"""续作H：2条L1→L2（Kipper und Wipper / 1840s美国州违约）。"""
import json
def svg(t,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x,lb in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)
D={
 'kipper-wipper-1618':{'sid':'w-en-kipper-wipper-1618','tl':[
   (1618,'30年战争初期','神圣罗马帝国各城邦为筹措军费大量降低铸币成色（据 Wikipedia Kipper und Wipper）'),
   (1620,'约1620—1623年','贬值最严重时期；德意志王国出现饥荒（同上）'),
   (1623,'1623年后','当局试图抑制通胀，宣布劣币非法并退出流通（同上）')],
  'causal':['30年战争爆发 → 军费激增','各城邦大量降低铸币成色以筹收入 → 货币贬值、通胀','约1620-23年贬值最烈并伴饥荒；其后当局禁劣币、回收'],
  'schools':[('财政/铸币贬值视角','战争财政压力导致系统性货币贬值'),('货币纪律视角','劣币驱逐良币、需以禁令与回收恢复信用')],
  'cmp':'与罗马第三世纪危机同属战争财政引发的货币贬值；具体异同待核实。'},
 'us-state-defaults-1840s':{'sid':'w-en-us-state-defaults-1840s','tl':[
   (1837,'1837年','恐慌收紧信贷，英格兰银行收缩放贷（据 Wikipedia U.S. state defaults in the 1840s）'),
   (1841,'1841年','26个美国州中19个及3个领地中的2个已发行债券、负有州债（同上）'),
   (1840,'1840年代','阿肯色、伊利诺伊、印第安纳、路易斯安那、马里兰、密歇根、密西西比、宾夕法尼亚、佛罗里达等州违约；4州最终拒付全部或部分债务，3州大规模重组（同上）')],
  'causal':['1834-39通胀期结束 + 1837恐慌 → 英格兰银行收紧对美信贷','多州已大量举债(1841年19/26州) → 偿付困难','多州违约；4州拒付、3州重组'],
  'schools':[('外部信贷视角','英国信贷收缩触发州债偿付危机'),('财政纪律视角','州级过度举债与项目失败导致违约')],
  'kd':[('1841年已发债州数','19','个(美国26州中)',1841,'原文：By 1841, nineteen of the twenty-six U.S. states ... had issued bonds；单一来源待核实。'),
        ('最终拒付州数','4','个(全部或部分债务)',1845,'原文：Four states ultimately repudiated all or part of their debts；单一来源待核实。')],
  'cmp':'与1837恐慌直接相连，是美国州级主权违约的经典案例；具体异同待核实。'},
}
for eid,sp in D.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'; sid=sp['sid']
    have={t.get('display') for t in d.get('timeline',[])}
    for y,disp,ev in sp['tl']:
        if disp not in have: d.setdefault('timeline',[]).append({'year':y,'display':disp,'event':ev,'sources':[sid]})
    d['timeline'].sort(key=lambda t:t.get('year',0))
    d['causal_chain']=[{'step':st,'sources':[sid]} for st in sp['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基摘要归纳；具体表述待核实','sources':[sid]} for h,v in sp['schools']]
    hk={k.get('label') for k in d.get('key_data',[])}
    for kd in sp.get('kd',[]):
        if kd[0] not in hk: d.setdefault('key_data',[]).append({'label':kd[0],'value':kd[1],'unit':kd[2],'year':kd[3],'comparable_price':False,'note':kd[4],'sources':[sid]})
    d['policy_response']=[{'holder':'政策当局','view':'应对措施及效果待核实','basis':'需多来源印证','sources':[d['sources'][0]]}]
    d['comparison']=sp['cmp']
    if not d.get('svg'): d['svg']=svg(d['title'],[sp['tl'][0][2][:12],'传导','后果'])
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【续作H】升L2(据REST摘要)。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'->L2')
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in D: e['level']='L2'; e['last_updated']='2026-11-23'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('done')
