# -*- coding: utf-8 -*-
import urllib.request, ssl, json, urllib.parse, re, time
c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
PAGES = {
 'ems': 'European Monetary System',
 'jamaica-accords': 'Jamaica Accords',
 'nixon-shock': 'Nixon shock',
 'emergency-banking-act-1933': 'Emergency Banking Act of 1933',
 'baring-crisis-1890': 'Baring crisis',
 'spain-2008': '2008–2014 Spanish financial crisis',
 'drexel': 'Drexel Burnham Lambert',
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
json.dump(out, open('_research/r65_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('saved')
