# -*- coding: utf-8 -*-
"""抓取核心案例页面全文，提取含关键数值的句子，供补充 key_data。"""
import urllib.request, ssl, json, urllib.parse, re, time, sys

c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}

PAGES = {
 'japan-asset-bubble-1990': 'Japanese asset price bubble',
 'argentina-crisis-2001': '1998–2002 Argentine great depression',
 'greek-debt-crisis': 'Greek government-debt crisis',
 'latino': 'Latin American debt crisis',
 'mexican-peso-1994': 'Mexican peso crisis',
 'oil-crisis-1973': '1973 oil crisis',
 'panic-1907': 'Panic of 1907',
}

def full(title):
    p = {'action':'query','format':'json','formatversion':'2','titles':title,
         'prop':'extracts','explaintext':'1','redirects':'1'}
    u = 'https://en.wikipedia.org/w/api.php?' + urllib.parse.urlencode(p)
    d = json.loads(urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c).read())
    pg = d['query']['pages'][0]
    return pg.get('extract', '') or ''

NUM = re.compile(r'(\d[\d,\.]*\s*(?:%|percent|billion|trillion|million|points|florins|livres)|'
                 r'(?:§|\$|US\$|€)\s*\d[\d,\.]*)', re.I)

out = {}
for eid, title in PAGES.items():
    try:
        t = full(title)
        sents = re.split(r'(?<=[.!?])\s+', t)
        hits = [s.strip() for s in sents if NUM.search(s) and 30 < len(s) < 320]
        out[eid] = {'title': title, 'len': len(t), 'hits': hits[:12]}
        print(f'{eid}: len={len(t)} hits={len(hits)}')
    except Exception as e:
        print(f'{eid}: FAIL {type(e).__name__}')
    time.sleep(0.5)

json.dump(out, open('_research/r59_data.json','w',encoding='utf-8'), ensure_ascii=False, indent=2)
print('saved')
