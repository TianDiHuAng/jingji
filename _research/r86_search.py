import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'naira': 'Nigerian naira devaluation history currency',
 'cedi': 'Ghana cedi redenomination 2007',
 'iran': 'Iranian rial inflation currency crisis',
 'sudan': 'Sudan hyperinflation currency',
 'yemen': 'Yemen currency crisis rial',
 'mexico-bolsa': 'Mexican bolsa bubble 1990s 1994',
 'brazil-bolsa': 'Bovespa bubble 1990s',
 'oceania-cur': 'Pacific islands currency crisis',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
