import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'zambia': 'Zambia debt default 2020 sovereign',
 'ghana': 'Ghana debt crisis 2022 default',
 'nigeria': 'Nigerian recession 2016 currency',
 'ethiopia': 'Ethiopia debt distress economy',
 'nz1984': 'New Zealand economic reforms 1984 Rogernomics',
 'aus1890s': 'Australian banking crisis 1893',
 'africa-debt': 'African debt crisis 1980s',
 'latam-stock': 'Latin American stock market crash',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
