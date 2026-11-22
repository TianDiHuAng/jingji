# -*- coding: utf-8 -*-
"""轮次13：中文权威大纲(Category:泡沫經濟)发现3条遗漏，双源新建。"""
import urllib.request,ssl,json,urllib.parse,re
c=ssl._create_unverified_context(); h={'User-Agent':'EconCrisisBot/1.0'}
NEW=[
 ('hainan-property-bubble-1992','1992–1993年海南房地产泡沫','1992年—1993年海南房地产泡沫','20世纪下半','亚洲','泡沫','重要','w-en-chinese-stock-bubble-of-2007'),
 ('taiwan-bubble','台湾泡沫经济','台灣泡沫經濟','20世纪下半','亚洲','泡沫','补充','w-en-japanese-asset-price-bubble'),
 ('us-video-game-crash-1983','1983年美国游戏业大萧条','1983年美国游戏业大萧条','20世纪下半','北美','泡沫','补充','w-en-speculative-bubble'),
]
titles=[x[2] for x in NEW]
p={'action':'query','format':'json','formatversion':'2','titles':'|'.join(titles),'redirects':'1','prop':'info'}
d=json.loads(urllib.request.urlopen(urllib.request.Request('https://zh.wikipedia.org/w/api.php?'+urllib.parse.urlencode(p),headers=h),timeout=30,context=c).read())
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
    sid='w-zh-'+slug(eid)
    if sid not in existing:
        i=info[title]
        sd['sources'].append({'id':sid,'title':i['canonical'],'author':'维基百科贡献者','year':i['touched'] or None,
          'type':'权威百科','url':'https://zh.wikipedia.org/wiki/'+urllib.parse.quote(i['canonical'].replace(' ','_')),
          'url2':None,'verified':True,'link_ok':True,'note':f'中文维基API核对(pageid={i["pageid"]})；轮次13中文权威大纲新增'})
        existing.add(sid)
sd['count']=len(sd['sources'])
json.dump(sd,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
cov=json.load(open('coverage.json',encoding='utf-8')); created=[]
for eid,name,title,period,region,ctype,tier,sec in NEW:
    if title not in info: continue
    sid='w-zh-'+slug(eid); srcs=[s for s in [sid,sec] if s in existing]
    if len(srcs)<2: print('WARN',eid,srcs); continue
    entry={'id':eid,'title':name,'level':'L1','tier':tier,'unit':'U4 20世纪下半','period':period,'region':region,'crisis_type':ctype,
      'one_line':f'{name}：发生于{period}、地区{region}的{ctype}类案例（轮次13新条目，骨架）。',
      'overview':f'{name} 是经中文权威大纲（Wikipedia 泡沫经济分类）对照发现的遗漏案例，维基页面已核对存在。完整内容待逐条核实来源后补充。',
      'timeline':[],'causal_chain':[],'key_data':[],'schools':[],'policy_response':[],'comparison':'','svg':'',
      'sources':srcs,'related':[],'needs_verification':True,'pending_notes':'L1骨架：内容待核实补充。'}
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    cov['entries'].append({'id':eid,'level':'L1','tier':tier,'status':'written','source_count':len(srcs),'needs_verification':1,
      'last_updated':'2026-11-22','unit':'U4 20世纪下半','period':period,'region':region,'crisis_type':ctype})
    created.append(eid)
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新建',len(created),created)
