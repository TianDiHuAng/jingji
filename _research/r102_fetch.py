import urllib.request, ssl, json, urllib.parse, re, time
c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
PAGES = {'encilhamento': 'Encilhamento', 'haiti-debt': 'Haitian independence debt'}
def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    return d['query']['pages'][0].get('extract','') or ''
NUM = re.compile(r'[^.]{0,130}?(\d[\d,\.]*\s*(?:%|percent|billion|million)|(?:US\$|\$|£|francs)\s*\d[\d,\.]*)[^.]{0,130}\.', re.I)
out = {}
for eid, title in PAGES.items():
    try:
        t = full(title)
        sents = re.split(r'(?<=[.!?])\s+', t)
        hits = [s.strip() for s in sents if NUM.search(s) and 40 < len(s) < 320]
        out[eid] = {'title': title, 'len': len(t), 'hits': hits[:10], 'extract': t[:800]}
        print(f'{eid}: len={len(t)} hits={len(hits)}')
    except Exception as e:
        print(f'{eid}: FAIL {type(e).__name__}')
    time.sleep(0.4)
json.dump(out, open('_research/r102_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
for k, v in out.items():
    print('==='+k+'===')
    print('摘要:', v.get('extract','')[:420])
    for s in v['hits'][:5]: print('  -', s[:170])
