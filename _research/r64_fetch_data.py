# -*- coding: utf-8 -*-
"""抓取第六批案例全文（7个）。"""
import urllib.request, ssl, json, urllib.parse, re, time

c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
PAGES = {
 'chilean-crisis-1982': 'Crisis of 1982',
 'brazil-hyper-1980': 'Hyperinflation in Brazil',
 'chinese-hyper-1937': 'Chinese hyperinflation',
 'soviet-hyper-1917': 'Hyperinflation in early Soviet Russia',
 'bankruptcy-ftx': 'Bankruptcy of FTX',
 'danatbank-1931': 'Danat-Bank',
 'european-banking-1931': 'European banking crisis of 1931',
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
json.dump(out, open('_research/r64_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('saved')
