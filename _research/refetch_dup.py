# 为缓存与他条目重复的条目改抓更专门的维基页面；已有来源直接用其 URL，缺的新增来源
import json,subprocess,urllib.parse,datetime
M={'asset-liability-mismatch':'w-en-original-sin','austrian-theory':'w-en-austrian-school-of-economics',
'coordination-games':'w-en-coordination-game','marxist-theory':'w-en-marxist-economics','minsky-theory':'w-en-minsky-moment',
'gatt':'w-en-gatt','structural-adjustment':'w-en-structural-adjustment','dutch-stock-crashes':'w-en-financial-history-of-the-dutch-republic',
'esfs':'w-en-esfs','fsb':'w-en-fsb','esrb':'w-en-esrb','greek-hyper-1941':'w-en-greek-hyper-1941','stock-market-crash':'w-en-stock-market-crash',
'bretton-woods':('Bretton Woods system','w-en-bretton-woods-system'),'creative-destruction':('Creative destruction','w-en-creative-destruction'),
'us-video-game-crash-1983':('Video game crash of 1983','w-en-video-game-crash-of-1983'),'keynesian-economics':('Keynesian economics','w-en-keynesian-economics')}
SP='data/sources.json';S=json.load(open(SP,encoding='utf-8'));byid={s['id']:s for s in S['sources']}
for eid,v in M.items():
    if isinstance(v,tuple): title,sid=v
    else: sid=v;title=urllib.parse.unquote(byid[sid]['url'].rsplit('/wiki/',1)[-1]).replace('_',' ')
    api='https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&explaintext=1&redirects=1&titles='+urllib.parse.quote(title)
    r=subprocess.run(['curl','-s','--max-time','40','-x','socks5h://127.0.0.1:10808','-A','jingji-research/1.0',api],capture_output=True)
    try: pg=list(json.loads(r.stdout)['query']['pages'].values())[0];tx=pg.get('extract','')
    except Exception as x: print('FAIL',eid,x);continue
    if len(tx)<500: print('SHORT',eid,title,len(tx));continue
    open(f'_research/wiki_full/{eid}.txt','w',encoding='utf-8').write(f'# {pg["title"]}\n# source {sid}\n'+tx)
    open(f'_research/wiki_full/{eid}.slug','w',encoding='utf-8').write(pg['title'].replace(' ','_'))
    if sid not in byid:
        s={'id':sid,'title':pg['title'],'author':'Wikipedia contributors','year':'2026','type':'权威百科','url':'https://en.wikipedia.org/wiki/'+urllib.parse.quote(pg['title'].replace(' ','_')),'url2':None,'verified':True,'note':f'Wikipedia API 经代理核对（{datetime.date.today()} 抓取全文 {len(tx)} 字符）','link_ok':True}
        S['sources'].append(s);byid[sid]=s
    p=f'data/entries/{eid}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw)
    if sid not in e['sources']: e['sources'].append(sid);s2=json.dumps(e,ensure_ascii=False,indent=2)+'\n';open(p,'w',encoding='utf-8',newline='').write(s2.replace('\n','\r\n') if crlf else s2)
    print('ok',eid,pg['title'],len(tx))
S['count']=len(S['sources']);open(SP,'w',encoding='utf-8').write(json.dumps(S,ensure_ascii=False,indent=2)+'\n');print('sources',S['count'])
