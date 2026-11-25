# 经 SOCKS 代理(10808)补抓缺失的英文维基全文缓存：取条目首个 w-en-* 来源的页面标题
import json,glob,os,subprocess,urllib.parse,time
S={s['id']:s for s in json.load(open('data/sources.json',encoding='utf-8'))['sources']}
OUT='_research/wiki_full';ok=fail=skip=0;log=[]
for f in sorted(glob.glob('data/entries/*.json')):
    e=json.load(open(f,encoding='utf-8'));p=f'{OUT}/{e["id"]}.txt'
    if os.path.exists(p): continue
    src=[S[x] for x in e.get('sources',[]) if x.startswith('w-en-') and x in S]
    if not src: skip+=1;log.append((e['id'],'无英文维基来源'));continue
    t=urllib.parse.unquote(src[0]['url'].rsplit('/wiki/',1)[-1])
    api='https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts&explaintext=1&redirects=1&titles='+urllib.parse.quote(t)
    r=subprocess.run(['curl','-s','--max-time','40','-x','socks5h://127.0.0.1:10808','-A','jingji-research/1.0',api],capture_output=True)
    try:
        pg=list(json.loads(r.stdout)['query']['pages'].values())[0];tx=pg.get('extract','')
        assert len(tx)>500
        open(p,'w',encoding='utf-8').write(f'# {pg.get("title")}\n# source {src[0]["id"]}\n'+tx);ok+=1
    except Exception as ex: fail+=1;log.append((e['id'],t,str(ex)[:60]))
    time.sleep(0.3)
json.dump(log,open('_research/fetch_missing_log.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('ok',ok,'fail',fail,'skip',skip)
