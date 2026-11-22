# -*- coding: utf-8 -*-
"""轮次14 方法4读者问题清单发现：2条标志性遗漏（TASK点名的1997亚洲金融危机 + 核心概念银行挤兑）。"""
import json
NEW=[
 ('asian-financial-crisis-1997','1997亚洲金融危机','20世纪下半','亚洲','货币','核心',
  ['w-en-asian-financial-crisis','w-zh-006','bk-the-asian-financial-crisis'],'U4 20世纪下半'),
 ('bank-run','银行挤兑','理论制度','全球','银行','核心',
  ['w-en-bank-run','w-en-systemic-risk'],'U6 理论与制度'),
]
sd=json.load(open('data/sources.json',encoding='utf-8'))
existing={s['id'] for s in sd['sources']}
cov=json.load(open('coverage.json',encoding='utf-8')); created=[]
for eid,name,period,region,ctype,tier,srcs,unit in NEW:
    srcs=[s for s in srcs if s in existing]
    if len(srcs)<2: print('WARN',eid,srcs); continue
    entry={'id':eid,'title':name,'level':'L1','tier':tier,'unit':unit,'period':period,'region':region,'crisis_type':ctype,
      'one_line':f'{name}：{period}、{region}的{ctype}类核心案例/概念（轮次14读者问题清单发现的遗漏）。',
      'overview':f'{name} 是读者问题清单核对发现的标志性遗漏（来源库已有核对来源）。完整内容待逐条核实后补充。',
      'timeline':[],'causal_chain':[],'key_data':[],'schools':[],'policy_response':[],'comparison':'','svg':'',
      'sources':srcs,'related':[],'needs_verification':True,'pending_notes':'L1骨架：内容待核实补充。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    cov['entries'].append({'id':eid,'level':'L1','tier':tier,'status':'written','source_count':len(srcs),'needs_verification':1,
      'last_updated':'2026-11-22','unit':unit,'period':period,'region':region,'crisis_type':ctype})
    created.append(eid)
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新建',len(created),created)
