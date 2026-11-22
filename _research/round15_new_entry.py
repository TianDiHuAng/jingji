# -*- coding: utf-8 -*-
"""轮次15 方法2覆盖矩阵：填补20世纪上半×债务空白（道威斯计划1924）。"""
import urllib.request,ssl,json,urllib.parse
c=ssl._create_unverified_context(); h={'User-Agent':'EconCrisisBot/1.0'}
# 核对 Dawes Plan
p={'action':'query','format':'json','formatversion':'2','titles':'Dawes Plan','prop':'info|extracts','explaintext':'1'}
d=json.loads(urllib.request.urlopen(urllib.request.Request('https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode(p),headers=h),timeout=25,context=c).read())
pg=d['query']['pages'][0]
print('pageid',pg.get('pageid'),'touched',pg.get('touched','')[:4],'extract_len',len(pg.get('extract','')))
txt=pg.get('extract','')
open('_research/r15_dawes.txt','w',encoding='utf-8').write(txt)

# 新增来源
sd=json.load(open('data/sources.json',encoding='utf-8'))
sid='w-en-dawes-plan'
if sid not in {x['id'] for x in sd['sources']}:
    sd['sources'].append({'id':sid,'title':pg['title'],'author':'Wikipedia contributors','year':pg.get('touched','')[:4],
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/Dawes_Plan','url2':None,'verified':True,'link_ok':True,
      'note':'Wikipedia API核对(pageid=%s)；轮次15覆盖矩阵稀疏格(20世纪上半×债务)新增' % pg.get('pageid')})
    sd['count']=len(sd['sources'])
    json.dump(sd,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('新增来源',sid)

# 新建条目
cov=json.load(open('coverage.json',encoding='utf-8'))
eid='dawes-plan-1924'
entry={'id':eid,'title':'道威斯计划(1924)','level':'L1','tier':'重要','unit':'U3 20世纪上半',
  'period':'20世纪上半','region':'欧洲','crisis_type':'债务',
  'one_line':'1924年道威斯计划重组德国一战战争赔款支付，缓解魏玛德国赔付危机（轮次15覆盖矩阵新增，骨架）。',
  'overview':'道威斯计划是经覆盖矩阵稀疏格分析（20世纪上半×债务）发现的遗漏，维基页面已核对存在。完整内容待逐条核实来源后补充。',
  'timeline':[],'causal_chain':[],'key_data':[],'schools':[],'policy_response':[],'comparison':'','svg':'',
  'sources':[sid,'w-en-great-depression'],'related':[],'needs_verification':True,'pending_notes':'L1骨架：内容待核实补充。'}
json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
cov['entries'].append({'id':eid,'level':'L1','tier':'重要','status':'written','source_count':2,'needs_verification':1,
  'last_updated':'2026-11-22','unit':'U3 20世纪上半','period':'20世纪上半','region':'欧洲','crisis_type':'债务'})
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新建条目',eid)
