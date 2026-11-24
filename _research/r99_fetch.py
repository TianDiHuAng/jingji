import urllib.request, ssl, json, urllib.parse, re, time
c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    return d['query']['pages'][0].get('extract','') or ''
t = full('Crisis of the late Middle Ages')
print('len', len(t))
print(t[:1200])
NUM = re.compile(r'[^.]{0,130}?(\d[\d,\.]*\s*(?:%|percent|million)|(?:£|\$)\s*\d[\d,\.]*)[^.]{0,130}\.', re.I)
sents = re.split(r'(?<=[.!?])\s+', t)
hits = [s.strip() for s in sents if NUM.search(s) and 40 < len(s) < 320]
print('\n--- hits', len(hits))
for s in hits[:8]: print('  -', s[:170])
json.dump({'crisis-late-middle-ages':{'title':'Crisis of the late Middle Ages','extract':t[:1500],'hits':hits[:10]}},
          open('_research/r99_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
