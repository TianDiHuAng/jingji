import urllib.request, ssl, json, urllib.parse
c = ssl._create_unverified_context(); h = {'User-Agent':'EconCrisisBot/1.0'}
p = {'action':'query','format':'json','formatversion':'2','titles':'Late Middle Ages',
     'prop':'extracts','exintro':'1','explaintext':'1','redirects':'1'}
u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=20, context=c).read())
t = d['query']['pages'][0].get('extract','') or ''
print('len', len(t)); print(t[:300])
sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
if 'w-en-late-middle-ages' not in ex:
    sd['sources'].append({'id':'w-en-late-middle-ages','title':'Late Middle Ages',
      'author':'Wikipedia contributors','year':'2026','type':'权威百科',
      'url':'https://en.wikipedia.org/wiki/Late_Middle_Ages','url2':None,
      'verified':True,'link_ok':True,'note':'Wikipedia API(extract intro)核对(本会话抓取)'})
    sd['count']=len(sd['sources'])
    json.dump(sd, open('data/sources.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增 w-en-late-middle-ages')
f='data/entries/crisis-late-middle-ages.json'; e=json.load(open(f,encoding='utf-8'))
if 'w-en-late-middle-ages' not in e['sources']:
    e['sources'].append('w-en-late-middle-ages')
    e['pending_notes']=e.get('pending_notes','')+' 【续作CQ】补第二参考来源。'
    json.dump(e,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('补第二来源')
