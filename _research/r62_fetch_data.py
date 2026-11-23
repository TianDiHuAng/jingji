# -*- coding: utf-8 -*-
"""抓取第四批案例全文提取数值（19个）。"""
import urllib.request, ssl, json, urllib.parse, re, time

c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}

PAGES = {
 'covid-crash-2020': '2020 stock market crash',
 'china-2015-turbulence': '2015–2016 Chinese stock market turbulence',
 'terra-luna-2022': 'Terra (blockchain)',
 'gamestop-2021': 'GameStop short squeeze',
 'bond-crisis-1994': '1994 bond market crisis',
 'credit-suisse-2023': 'Acquisition of Credit Suisse by UBS',
 'northern-rock': 'Northern Rock',
 'bear-stearns': 'Bear Stearns',
 'enron': 'Enron scandal',
 'worldcom': 'WorldCom scandal',
 'argentina-2018': '2018–present Argentine monetary crisis',
 'turkey-2001': '2001 Turkish economic crisis',
 'egypt-2023': '2023–2024 Egyptian financial crisis',
 'lebanese-liquidity-2019': 'Lebanese liquidity crisis',
 'puerto-rico-debt-2014': 'Puerto Rican government-debt crisis',
 'china-realestate-2020': 'Chinese real estate crisis (2020–present)',
 'china-liquidity-2013': 'Chinese Banking Liquidity Crisis of 2013',
 'oil-price-war-2020': '2020 Russia–Saudi Arabia oil price war',
}

def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    pg = d['query']['pages'][0]
    return pg.get('extract', '') or ''

NUM = re.compile(r'(\d[\d,\.]*\s*(?:%|percent|billion|trillion|million|points|bn)|'
                 r'(?:£|\$|US\$|€|CHF)\s*\d[\d,\.]*)', re.I)

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

json.dump(out, open('_research/r62_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('saved')
