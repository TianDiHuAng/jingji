import urllib.request, ssl, json, urllib.parse, re, time
c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
PAGES = {
 'gold-reserve-act-1934': 'Gold Reserve Act',
 'jamaica-accords': 'Jamaica Accords',
 'northern-rock': 'Northern Rock',
 'norwegian-banking-1988': '1988–1992 Norwegian banking crisis',
 'showa-crisis-1927': 'Shōwa financial crisis',
 'panic-1825': 'Panic of 1825',
 'tripartite-1936': 'Tripartite Agreement of 1936',
 'gold-bloc': 'Gold bloc',
}
def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    return d['query']['pages'][0].get('extract','') or ''
NUM = re.compile(r'[^.]{0,130}?(\d[\d,\.]*\s*(?:%|percent|billion|million|points)|(?:US\$|\$|£|NOK|kr)\s*\d[\d,\.]*)[^.]{0,130}\.', re.I)
out = {}
for eid, title in PAGES.items():
    try:
        t = full(title)
        sents = re.split(r'(?<=[.!?])\s+', t)
        hits = [s.strip() for s in sents if NUM.search(s) and 35 < len(s) < 320]
        out[eid] = {'title': title, 'len': len(t), 'hits': hits[:8]}
        print(f'{eid}: len={len(t)} hits={len(hits)}')
    except Exception as e:
        print(f'{eid}: FAIL {type(e).__name__}')
    time.sleep(0.4)
json.dump(out, open('_research/r105_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
for k, v in out.items():
    if not v['hits']: continue
    print('==='+k+'===')
    for s in v['hits'][:4]: print('  -', s[:165])
