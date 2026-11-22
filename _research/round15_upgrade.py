# -*- coding: utf-8 -*-
"""轮次15：dawes-plan-1924 升L2（维基原文实证数值）。"""
import json
f='data/entries/dawes-plan-1924.json'; d=json.load(open(f,encoding='utf-8'))
d['level']='L2'
d['timeline']=[
 {'year':1923,'display':'1923年1月','event':'德国被宣布赔款违约，法比军队占领鲁尔（据 Wikipedia Dawes Plan）','sources':['w-en-dawes-plan']},
 {'year':1924,'display':'1924年8月29日','event':'德国国会通过道威斯计划（同上）','sources':['w-en-dawes-plan']},
 {'year':1924,'display':'1924年9月1日','event':'道威斯计划正式生效，终结外交危机（同上）','sources':['w-en-dawes-plan']},
 {'year':1925,'display':'1925年8月25日','event':'鲁尔占领结束（同上）','sources':['w-en-dawes-plan']},
 {'year':1929,'display':'1929年','event':'道威斯计划被杨格计划取代（同上）','sources':['w-en-dawes-plan']},
]
d['key_data']=[
 {'label':'1929年前德国获贷款','value':29,'unit':'十亿帝国马克（德国，截至1929年世界经济危机前累计贷款）','year':1929,'comparable_price':False,
  'note':'原文：By the start of the world economic crisis in 1929, Germany had received 29 billion Reichsmarks in loans；单一来源待核实。','sources':['w-en-dawes-plan']},
]
d['causal_chain']=[
 {'step':'一战后赔款负担 → 德国1923年违约','sources':['w-en-dawes-plan']},
 {'step':'法比占领鲁尔 → 外交与经济危机','sources':['w-en-dawes-plan']},
 {'step':'道威斯计划(贷款+赔款重组) → 危机缓解、经济短暂稳定','sources':['w-en-dawes-plan']},
]
d['schools']=[
 {'holder':'赔款制度视角','view':'危机源于一战后赔款安排的可持续性缺陷','basis':'维基 Dawes Plan 背景叙述','sources':['w-en-dawes-plan']},
]
d['policy_response']=[{'holder':'协约国与德国','view':'以道威斯计划重组赔款并引入美国贷款；效果存在争议（依赖短期贷款，1929后中断）','basis':'需多来源印证','sources':['w-en-dawes-plan']}]
d['comparison']='与魏玛恶性通胀(1921-23)同属一战后德国经济危机链条；道威斯计划是赔款层面的制度应对，恶性通胀是货币层面的后果。具体异同待核实。'
d['svg']="<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'><text x='20' y='28' class='ttl'>道威斯计划：赔款危机应对机制</text><g><rect x='20' y='55' width='210' height='52' rx='6' class='box'/><text x='29' y='78' class='lbl'>赔款违约+鲁尔占领</text><text x='29' y='96' class='sub'>1923 危机触发</text></g><line x1='230' y1='81' x2='265' y2='81' class='ar'/><g><rect x='270' y='55' width='210' height='52' rx='6' class='box'/><text x='279' y='78' class='lbl'>道威斯计划重组</text><text x='279' y='96' class='sub'>贷款+赔款安排</text></g><line x1='480' y1='81' x2='515' y2='81' class='ar'/><g><rect x='520' y='55' width='220' height='52' rx='6' class='box'/><text x='529' y='78' class='lbl'>危机缓解(1924-29)</text><text x='529' y='96' class='sub'>1929被杨格计划取代</text></g><text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>"
d['needs_verification']=True
d['pending_notes']='L1骨架升级L2：timeline/数值经维基原文实证，均单一来源待核实。'
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id']=='dawes-plan-1924': e['level']='L2'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('dawes-plan → L2')
