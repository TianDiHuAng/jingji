import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'p1793': 'Panic of 1793 United States',
 'latam-1820s': 'Latin American debt crisis 1820s default London bonds',
 'argentina-1890': 'Argentina 1890 crisis Baring',
 'brazil-1890s': 'Brazil Encilhamento bubble 1890',
 'chile-1878': 'Chile economic crisis 1878 nitrate',
 'japan-meiji': 'Matsukata deflation Japan 1880s',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
