import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'nz-debt': 'New Zealand government debt crisis 1984',
 'aus-debt': 'Australian government debt 1980s',
 'iran-infl': 'Iranian rial hyperinflation 2020s',
 'syria-infl': 'Syrian pound collapse inflation',
 'lebanon-hyper': 'Lebanese hyperinflation 2020',
 'venezuela': 'Venezuelan bolivar hyperinflation',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
