import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'dubai': 'Dubai debt crisis 2009 Dubai World Nakheel',
 'saudi': 'Saudi Arabia economic crisis oil price 2014',
 'korea1997': 'South Korean financial crisis 1997 IMF',
 'indonesia1997': 'Indonesian financial crisis 1997',
 'thailand1997': 'Thai financial crisis 1997',
 'iran': 'Iran economy sanctions crisis',
 'iraq': 'Iraq economy crisis',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
