# -*- coding: utf-8 -*-
"""抓取第三批案例全文提取数值（14个）。"""
import urllib.request, ssl, json, urllib.parse, re, time

c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}

PAGES = {
 'black-wednesday-1992': 'Black Wednesday',
 'russian-1998': '1998 Russian financial crisis',
 'savings-loan-1986': 'Savings and loan crisis',
 'icelandic-crisis-2008': '2008–2011 Icelandic financial crisis',
 'cypriot-2013': '2012–2013 Cypriot financial crisis',
 'russian-crisis-2014': 'Russian financial crisis (2014–2016)',
 'sri-lanka-crisis-2019': 'Sri Lankan economic crisis (2019–2024)',
 'lebanese-liquidity-2019': 'Lebanese liquidity crisis',
 'oil-crisis-1979': '1979 oil crisis',
 'recession-1920-1921': 'Recession of 1920–1921',
 'recession-1937-1938': 'Recession of 1937–1938',
 'panic-1792': 'Panic of 1792',
 'baring-crisis-1890': 'Baring crisis',
 'black-friday-1869': 'Black Friday (1869)',
}

def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    pg = d['query']['pages'][0]
    return pg.get('extract', '') or ''

NUM = re.compile(r'(\d[\d,\.]*\s*(?:%|percent|billion|trillion|million|points|billion|bn|m)|'
                 r'(?:£|\$|US\$|€)\s*\d[\d,\.]*)', re.I)

out = {}
for eid, title in PAGES.items():
    try:
        t = full(title)
        sents = re.split(r'(?<=[.!?])\s+', t)
        hits = [s.strip() for s in sents if NUM.search(s) and 30 < len(s) < 300]
        out[eid] = {'title': title, 'len': len(t), 'hits': hits[:10]}
        print(f'{eid}: len={len(t)} hits={len(hits)}')
    except Exception as e:
        print(f'{eid}: FAIL {type(e).__name__}')
    time.sleep(0.4)

json.dump(out, open('_research/r61_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('saved')
