# -*- coding: utf-8 -*-
"""轮次4：为理论条目补来源 —— 新增核对过的百科页 + 给6条低来源条目补第二条来源。"""
import urllib.request, ssl, json, urllib.parse

c=ssl._create_unverified_context(); h={'User-Agent':'EconCrisisBot/1.0'}
NEW = {
 'Herd behavior':'羊群行为',
 'Coordination game':'协调博弈',
 'Minsky moment':'明斯基时刻',
 'Hyman Minsky':'海曼·明斯基',
 'Currency school':'通货学派（银行学派争论）',
}
# 核对存在性 + 取最后修改年
titles=list(NEW.keys())
p={'action':'query','format':'json','formatversion':'2','titles':'|'.join(titles),'redirects':'1','prop':'info'}
req=urllib.request.Request('https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode(p),headers=h)
d=json.loads(urllib.request.urlopen(req,timeout=30,context=c).read())
norm={r['to']:r['from'] for r in d.get('query',{}).get('redirects',[])}
info={}
for pg in d['query']['pages']:
    if not pg.get('missing'):
        entry={'canonical':pg['title'],'touched':pg.get('touched','')[:4],'pageid':pg.get('pageid')}
        info[pg['title']]=entry
        if pg['title'] in norm:  # 用原始查询标题亦可访问
            info[norm[pg['title']]]=entry

srcdata=json.load(open('data/sources.json',encoding='utf-8'))
existing={s['id'] for s in srcdata['sources']}
added=[]
import re
def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')[:48]
for title, zh in NEW.items():
    canonical = info.get(title,{}).get('canonical')
    if not canonical:
        print('SKIP (missing)',title); continue
    sid='w-en-'+slug(title)
    if sid in existing: continue
    i=info[title]
    srcdata['sources'].append({
      'id':sid,'title':i['canonical'],'author':'Wikipedia contributors','year':i['touched'] or None,
      'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+urllib.parse.quote(i['canonical'].replace(' ','_')),
      'url2':None,'verified':True,'link_ok':True,
      'note':f'Wikipedia API 核对：页面存在（pageid={i["pageid"]}）；中文主题：{zh}（轮次4新增）'})
    added.append(sid); existing.add(sid)
srcdata['count']=len(srcdata['sources'])
json.dump(srcdata,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新增来源',len(added),added)

# 给6条理论补第二条来源（优先本条主题对应的百科页）
ADD = {
 'austrian-theory':'w-en-austrian-school-of-economics',
 'marxist-theory':'w-en-marxist-economics',
 'contagion':'w-en-financial-contagion',
 'banking-school':'w-en-currency-school',
 'coordination-games':'w-en-coordination-game',
 'minsky-theory':'w-en-minsky-moment',
}
for eid, sid in ADD.items():
    f='data/entries/'+eid+'.json'
    d=json.load(open(f,encoding='utf-8'))
    if sid in d['sources']: continue
    if sid not in existing:
        print('WARN sid not in sources',sid); continue
    d['sources'].append(sid)
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','')+f' 【轮次4补源】新增来源 {sid}，具体适用待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('补源',eid,'->',sid)
