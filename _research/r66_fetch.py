# -*- coding: utf-8 -*-
import urllib.request, ssl, json, urllib.parse, re, time
c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
PAGES = {
 'crisis-1914': 'Financial crisis of 1914',
 'crisis-third-century': 'Crisis of the Third Century',
 'panic-1825': 'Panic of 1825',
 'shanghai-rubber-1910': 'Shanghai rubber stock market crisis',
 'south-america-2002': 'South American economic crisis of 2002',
 'stock-crash-1973': '1973–1974 stock market crash',
 'venezuela-crisis-2013': 'Crisis in Venezuela',
 'silicon-valley-bank': 'Collapse of Silicon Valley Bank',
 'brexit-crash-2016': '2015–2016 stock market selloff',
}
def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    return d['query']['pages'][0].get('extract','') or ''
NUM = re.compile(r'(\d[\d,\.]*\s*(?:%|percent|billion|trillion|million|points|bn)|(?:£|\$|US\$|€|DM)\s*\d[\d,\.]*)', re.I)
out = {}
for eid, title in PAGES.items():
    try:
        t = full(title)
        sents = re.split(r'(?<=[.!?])\s+', t)
        hits = [s.strip() for s in sents if NUM.search(s) and 30 < len(s) < 300]
        out[eid] = {'title': title, 'len': len(t), 'hits': hits[:8]}
        print(f'{eid}: len={len(t)} hits={len(hits)}')
    except Exception as e:
        print(f'{eid}: FAIL {type(e).__name__}')
    time.sleep(0.4)
json.dump(out, open('_research/r66_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('saved')
