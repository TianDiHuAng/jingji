import urllib.request, ssl, json, urllib.parse, time
c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
PAGES = {'money-laundering': 'Money laundering', 'housing-bubble': 'Housing bubble', 'neoliberalism': 'Neoliberalism'}
def summ(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','exintro':'1','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=20, context=c).read())
    return d['query']['pages'][0].get('extract','') or ''
out={}
for eid,title in PAGES.items():
    try:
        t=summ(title)
        out[eid]={'title':title,'extract':t[:500]}
        print('OK',eid,'|',title,'| len',len(t))
        print('   ',t[:180])
    except Exception as e: print('FAIL',eid,type(e).__name__)
    time.sleep(0.4)
json.dump(out, open('_research/r94_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
