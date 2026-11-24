import urllib.request, ssl, json, time, urllib.parse
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
def search(q):
    u = ('https://en.wikipedia.org/w/api.php?action=query&format=json&formatversion=2&list=search&srsearch='
         + urllib.parse.quote(q) + '&srlimit=2')
    return json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=9, context=c).read())
qs = {
 'nz1987': 'New Zealand sharemarket crash 1987',
 'aus2008': 'Australia financial crisis 2008 stimulus',
 'nz-gfc': 'New Zealand finance company failures 2008',
 'egypt-1930s': 'Egypt economy Great Depression cotton',
 'africa-1980s': 'African economic crisis 1980s structural adjustment',
}
for k, q in qs.items():
    try:
        d = search(q)
        print(k, ':', [r['title'] for r in d['query']['search']])
    except Exception as e:
        print(k, 'FAIL', type(e).__name__)
    time.sleep(0.6)
