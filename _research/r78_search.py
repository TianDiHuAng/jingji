import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'nigeria-naira': 'Nigerian naira devaluation 2016 currency crisis',
 'zambia-default': 'Zambia sovereign default 2020 bonds',
 'southafrica-debt': 'South African debt crisis economy 1985',
 'angola': 'Angola economic crisis oil 2015',
 'kenya': 'Kenyan banking crisis 1980s',
 'nigeria-2016': 'Economy of Nigeria recession',
 'nz-rogernomics': 'Rogernomics New Zealand 1984',
 'fiji': 'Fiji economy crisis',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
