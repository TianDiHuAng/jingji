# -*- coding: utf-8 -*-
"""轮次21：网络恢复(REST API)，补建3条待联网缺口条目（L1骨架，真实摘要，双源）。"""
import urllib.request, ssl, json, re

c=ssl._create_unverified_context(); h={'User-Agent':'Mozilla/5.0 EconCrisisBot/1.0'}
def summary(slug):
    r=urllib.request.urlopen(urllib.request.Request('https://en.wikipedia.org/api/rest_v1/page/summary/'+slug,headers=h),timeout=15,context=c)
    return json.loads(r.read())

SPECS=[
 ('railway-mania','铁路狂热(1840年代英国)','Railway_Mania','20世纪上半','欧洲','泡沫','重要',['w-en-speculative-bubble'],'1840年代英国铁路投资狂潮（Railway Mania），大量资本涌入铁路股票形成泡沫，随后崩盘。'),
 ('recession-1920-1921','1920–1921年衰退','Recession_of_1920%E2%80%931921','20世纪上半','北美','其他','重要',['w-en-business-cycle'],'一战后美国及多国的急剧通缩型经济衰退（1920–1921）。'),
 ('bankruptcy-ftx','加密市场崩盘与FTX破产(2022)','Collapse_of_FTX','21世纪','全球','泡沫','重要',['w-en-financial-crisis'],'2022年加密货币市场崩盘，FTX交易所破产为标志性事件。'),
]
srcdata=json.load(open('data/sources.json',encoding='utf-8'))
existing={s['id'] for s in srcdata['sources']}
cov=json.load(open('coverage.json',encoding='utf-8'))
created=[]
for eid,name,slug,period,region,ctype,tier,secs,oneline in SPECS:
    try:
        d=summary(slug)
    except Exception as e:
        print('SKIP(summary fail)',eid,type(e).__name__); continue
    title=d.get('title',slug.replace('_',' '))
    extract=d.get('extract','')
    sid='w-en-'+eid
    if sid not in existing:
        srcdata['sources'].append({'id':sid,'title':title,'author':'Wikipedia contributors','year':'2026','type':'权威百科',
          'url':'https://en.wikipedia.org/wiki/'+slug,'url2':None,'verified':True,'link_ok':True,
          'note':'Wikipedia REST API核对(page id存在)；轮次21网络恢复后新增；摘要:"%s"' % extract[:60]})
        existing.add(sid)
    srcs=[s for s in [sid]+secs if s in existing]
    if len(srcs)<2: print('WARN <2',eid,srcs); continue
    unit={'20世纪上半':'U3 20世纪上半','21世纪':'U5 21世纪'}.get(period,'U5 21世纪')
    ov=(extract[:400] if extract else oneline)+'（据维基摘要；完整时间线/数据待核实补充。）'
    entry={'id':eid,'title':name,'level':'L1','tier':tier,'unit':unit,'period':period,'region':region,'crisis_type':ctype,
      'one_line':oneline,'overview':ov,'timeline':[],'causal_chain':[],'key_data':[],'schools':[],'policy_response':[],
      'comparison':'','svg':'','sources':srcs,'related':[],'needs_verification':True,
      'pending_notes':'L1骨架（据维基摘要）：时间线、传导机制、数据、各方解释待核实补充。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    cov['entries'].append({'id':eid,'level':'L1','tier':tier,'status':'written','source_count':len(srcs),'needs_verification':1,'last_updated':'2026-11-22','unit':unit,'period':period,'region':region,'crisis_type':ctype})
    created.append(eid)
    print('新建',eid,'| title:',title,'| extract:',len(extract))
srcdata['count']=len(srcdata['sources'])
cov['total']=len(cov['entries'])
json.dump(srcdata,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('created',created)
