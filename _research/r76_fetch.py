import urllib.request, ssl, json, urllib.parse, re, time
c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
PAGES = {
 'amsterdam-crisis-1763': 'Amsterdam banking crisis of 1763',
 'british-credit-1772': 'British credit crisis of 1772',
 'bengal-bubble-1769': 'Bengal Bubble of 1769',
 'copper-panic-1789': 'Copper Panic of 1789',
 'australian-banking-1893': 'Australian banking crisis of 1893',
 'arendal-crash-1886': 'Arendal crash',
 'paris-bourse-1882': 'Paris Bourse crash of 1882',
 'us-state-defaults-1840s': 'Default (finance)',
}
def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    return d['query']['pages'][0].get('extract','') or ''
NUM = re.compile(r'(\d[\d,\.]*\s*(?:%|percent|billion|trillion|million|livres|pounds|gulden|florins)|(?:£|\$|US\$|€)\s*\d[\d,\.]*)', re.I)
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
json.dump(out, open('_research/r76_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
