import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'ldi': '2022 United Kingdom gilt crisis liability-driven investment',
 'archegos': 'Archegos Capital Management collapse 2021',
 'mmf': '2020 money market fund crisis March',
 'gamestop': 'GameStop short squeeze 2021',
 'evergrande': 'Evergrande debt crisis 2021',
 'credit-suisse': 'Credit Suisse collapse 2023 UBS',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
