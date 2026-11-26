# 为 6 个缓存放错页面的条目抓取专题页，新增来源并替换缓存
import json,subprocess,urllib.parse,datetime
M={'steel-crisis-1973':('Steel crisis','w-en-steel-crisis'),
   'panic-1796':('Panic of 1796–1797','w-en-panic-of-1796-1797'),
   'panic-1910':('Panic of 1910–11','w-en-panic-of-1910-11'),
   'venezuela-energy-2010':('Energy crisis in Venezuela','w-en-energy-crisis-in-venezuela'),
   'israel-bank-1983':('1983 Israel bank stock crisis','w-en-1983-israel-bank-stock-crisis'),
   'crisis-33ce':('Financial crisis of 33','w-en-financial-crisis-of-33')}
SP='data/sources.json';S=json.load(open(SP,encoding='utf-8'));have={s['id'] for s in S['sources']}
for eid,(title,sid) in M.items():
    api='https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&explaintext=1&redirects=1&titles='+urllib.parse.quote(title)
    r=subprocess.run(['curl','-s','--max-time','40','-x','socks5h://127.0.0.1:10808','-A','jingji-research/1.0',api],capture_output=True)
    pg=list(json.loads(r.stdout)['query']['pages'].values())[0];tx=pg.get('extract','')
    if len(tx)<500: print('FAIL',eid,len(tx));continue
    open(f'_research/wiki_full/{eid}.txt','w',encoding='utf-8').write(f'# {pg["title"]}\n# source {sid}\n'+tx)
    url='https://en.wikipedia.org/wiki/'+urllib.parse.quote(pg['title'].replace(' ','_'))
    if sid not in have:
        S['sources'].append({'id':sid,'title':pg['title'],'author':'Wikipedia contributors','year':'2026','type':'权威百科','url':url,'url2':None,'verified':True,'note':f'Wikipedia API 经代理核对（{datetime.date.today()} 抓取全文 {len(tx)} 字符）','link_ok':True});have.add(sid)
    p=f'data/entries/{eid}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw)
    if sid not in e['sources']: e['sources'].insert(0,sid)
    s=json.dumps(e,ensure_ascii=False,indent=2)+'\n';open(p,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s)
    print('ok',eid,pg['title'],len(tx))
S['count']=len(S['sources']);open(SP,'w',encoding='utf-8').write(json.dumps(S,ensure_ascii=False,indent=2)+'\n');print('sources',S['count'])
