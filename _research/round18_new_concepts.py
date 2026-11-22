# -*- coding: utf-8 -*-
"""轮次18 网络无关扩充：用库内既有 verified 来源新增3个核心金融概念条目（L1骨架）。"""
import json
NEW=[
 ('moral-hazard','道德风险','一种现象：一方在受保护（如保险、救助预期）后改变行为、承担更多风险，因为后果部分由他人承担。是存款保险与"太大而不能倒"救助的核心争议概念。',
  ['w-en-moral-hazard','w-en-deposit-insurance'],['deposit-insurance','too-big-to-fail']),
 ('too-big-to-fail','太大而不能倒','指某些金融机构规模与关联性过大，一旦倒闭会引发系统性风险，政府因此倾向于救助；其代价是可能诱发道德风险与不公平竞争。',
  ['w-en-too-big-to-fail','w-en-systemic-risk'],['moral-hazard','bank-run']),
 ('impossible-trinity','不可能三角（三难困境）','国际金融中的政策约束：固定汇率、资本自由流动与独立货币政策三者不可同时实现，最多取其二。用于解释货币危机与汇率制度选择。',
  ['w-en-currency-crisis','w-en-monetary-policy'],['bretton-woods','black-wednesday-1992']),
]
cov=json.load(open('coverage.json',encoding='utf-8'))
existing={e['id'] for e in cov['entries']}
for eid,name,ov,srcs,rels in NEW:
    if eid in existing: print('exists',eid); continue
    entry={'id':eid,'title':name,'level':'L1','tier':'补充','unit':'U6 理论与制度',
      'period':'理论制度','region':'全球','crisis_type':'理论','one_line':ov,
      'overview':ov+'（理论概念条目，标准教科书定义；具体论述出处与案例适用待核实。）',
      'timeline':[],'causal_chain':[],'key_data':[],'schools':[],'policy_response':[],'comparison':'','svg':'',
      'sources':srcs,'related':rels,'needs_verification':True,
      'pending_notes':'理论概念：定义出处与在具体危机中的适用待核实补充。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    cov['entries'].append({'id':eid,'level':'L1','tier':'补充','status':'written','source_count':len(srcs),'needs_verification':1,'last_updated':'2026-11-22','unit':'U6 理论与制度','period':'理论制度','region':'全球','crisis_type':'理论'})
    print('新增',eid)
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
