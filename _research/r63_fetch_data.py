# -*- coding: utf-8 -*-
"""抓取第五批案例全文（7个）。"""
import urllib.request, ssl, json, urllib.parse, re, time

c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
PAGES = {
 'showa-crisis-1927': 'Shōwa financial crisis',
 'yugoslav-hyper-1992': 'Hyperinflation in Serbia and Montenegro',
 'norwegian-banking-1988': '1988–1992 Norwegian banking crisis',
 'washington-mutual': 'Washington Mutual',
 'indymac': 'IndyMac',
 'railway-mania': 'Railway Mania',
 'crypto-bubble': 'Cryptocurrency bubble',
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
json.dump(out, open('_research/r63_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('saved')
