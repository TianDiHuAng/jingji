import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'mexico-bubble': 'Mexican stock market bubble 1990s Bolsa',
 'brazil-bubble': 'Brazil stock market bubble 1971',
 'argentina-bubble': 'Argentina asset price bubble',
 'nigeria-currency': 'Nigerian naira devaluation 2023',
 'egypt-pound': 'Egyptian pound devaluation 2016 2024',
 'ghana-cedi': 'Ghana cedi depreciation crisis 2022',
 'africa-currency': 'African currency crisis devaluation',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
