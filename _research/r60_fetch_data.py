# -*- coding: utf-8 -*-
"""抓取第二批核心案例页面全文，提取数值句。"""
import urllib.request, ssl, json, urllib.parse, re, time

c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}

PAGES = {
 'dotcom-bubble-2000': 'Dot-com bubble',
 'euro-area-crisis': 'Eurozone crisis',
 'hungarian-hyper-1945': 'Hungarian pengő',
 'mississippi-bubble-1720': "John Law's Company",
 'panic-1857': 'Panic of 1857',
 'panic-1873': 'Panic of 1873',
 'venezuela-hyper-2016': 'Hyperinflation in Venezuela',
 'zimbabwe-hyper-2007': 'Hyperinflation in Zimbabwe',
}

def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    pg = d['query']['pages'][0]
    return pg.get('extract', '') or ''

NUM = re.compile(r'(\d[\d,\.]*\s*(?:%|percent|billion|trillion|million|points|pengo|pengő)|'
                 r'(?:§|\$|US\$|€)\s*\d[\d,\.]*)', re.I)

out = {}
for eid, title in PAGES.items():
    try:
        t = full(title)
        sents = re.split(r'(?<=[.!?])\s+', t)
        hits = [s.strip() for s in sents if NUM.search(s) and 30 < len(s) < 300]
        out[eid] = {'title': title, 'len': len(t), 'hits': hits[:12]}
        print(f'{eid}: len={len(t)} hits={len(hits)}')
    except Exception as e:
        print(f'{eid}: FAIL {type(e).__name__}')
    time.sleep(0.5)

json.dump(out, open('_research/r60_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('saved')
