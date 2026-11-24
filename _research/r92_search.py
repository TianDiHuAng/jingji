import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'mexico-bolsa-bubble': 'Mexican stock market 1990s bubble crash Bolsa',
 'chile-bubble': 'Chile stock market bubble 1990s',
 'colombia-bubble': 'Colombia stock market bubble 1990s',
 'sa-bubble': 'South Africa stock market bubble',
 'nigeria-bubble': 'Nigerian stock market bubble 2008',
 'aus-bubble': 'Australian property bubble',
 'nz-currency': 'New Zealand dollar currency crisis',
 'oceania-debt': 'Pacific island debt crisis',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
