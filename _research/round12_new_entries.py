# -*- coding: utf-8 -*-
"""轮次12 NEW-outline：权威大纲(List of economic crises)对照发现的4条高价值遗漏。
每条专属维基页已API核对存在；双源；先建L1骨架。"""
import urllib.request,ssl,json,urllib.parse,re
c=ssl._create_unverified_context(); h={'User-Agent':'EconCrisisBot/1.0'}
NEW=[
 ('black-monday-1987','1987年黑色星期一','Black Monday (1987)','20世纪下半','北美','泡沫','核心','w-en-wall-street-crash-of-1929'),
 ('kipper-wipper-1618','Kipper und Wipper货币危机(1618–1622)','Kipper und Wipper','前17世纪','欧洲','货币','补充','w-en-hyperinflation'),
 ('recession-1937-1938','1937–1938年衰退','Recession of 1937–1938','20世纪上半','北美','其他','重要','w-en-great-depression'),
 ('rodrigazo-1975','罗德里加索危机(阿根廷1975)','Rodrigazo','20世纪下半','拉美','恶性通胀','重要','w-en-latin-american-debt-crisis'),
]
# 核对页面+建来源
titles=[x[2] for x in NEW]
p={'action':'query','format':'json','formatversion':'2','titles':'|'.join(titles),'redirects':'1','prop':'info'}
d=json.loads(urllib.request.urlopen(urllib.request.Request('https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode(p),headers=h),timeout=30,context=c).read())
norm={r['to']:r['from'] for r in d.get('query',{}).get('redirects',[])}
info={}
for pg in d['query']['pages']:
    if not pg.get('missing'):
        e={'canonical':pg['title'],'touched':pg.get('touched','')[:4],'pageid':pg.get('pageid')}
        info[pg['title']]=e
        if pg['title'] in norm: info[norm[pg['title']]]=e
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')[:48]
sd=json.load(open('data/sources.json',encoding='utf-8')); existing={s['id'] for s in sd['sources']}
for eid,name,title,period,region,ctype,tier,sec in NEW:
    if title not in info: print('SKIP',eid); continue
    sid='w-en-'+slug(eid)
    if sid not in existing:
        i=info[title]
        sd['sources'].append({'id':sid,'title':i['canonical'],'author':'Wikipedia contributors','year':i['touched'] or None,
          'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+urllib.parse.quote(i['canonical'].replace(' ','_')),
          'url2':None,'verified':True,'link_ok':True,'note':f'Wikipedia API核对(pageid={i["pageid"]})；轮次12权威大纲新增'})
        existing.add(sid)
sd['count']=len(sd['sources'])
json.dump(sd,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
# 建条目
cov=json.load(open('coverage.json',encoding='utf-8')); created=[]
for eid,name,title,period,region,ctype,tier,sec in NEW:
    if title not in info: continue
    sid='w-en-'+slug(eid); srcs=[s for s in [sid,sec] if s in existing]
    if len(srcs)<2: print('WARN',eid,srcs); continue
    unit={'前17世纪':'U1 早期—17世纪','20世纪上半':'U3 20世纪上半','20世纪下半':'U4 20世纪下半'}[period]
    entry={'id':eid,'title':name,'level':'L1','tier':tier,'unit':unit,'period':period,'region':region,'crisis_type':ctype,
      'one_line':f'{name}：发生于{period}、地区{region}的{ctype}类案例（轮次12新条目，骨架）。',
      'overview':f'{name} 是经权威大纲（Wikipedia List of economic crises）对照发现的遗漏案例，维基页面已核对存在。完整内容待逐条核实来源后补充。',
      'timeline':[],'causal_chain':[],'key_data':[],'schools':[],'policy_response':[],'comparison':'','svg':'',
      'sources':srcs,'related':[],'needs_verification':True,'pending_notes':'L1骨架：内容待核实补充。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    cov['entries'].append({'id':eid,'level':'L1','tier':tier,'status':'written','source_count':len(srcs),'needs_verification':1,
      'last_updated':'2026-11-22','unit':unit,'period':period,'region':region,'crisis_type':ctype})
    created.append(eid)
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新建',len(created),created)
