import urllib.request, ssl, json, time, os
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
cands = [
 ('fixed-exchange-rate', 'Fixed_exchange_rate_system'),
 ('floating-exchange-rate', 'Floating_exchange_rate'),
 ('counterparty-risk', 'Counterparty_risk'),
 ('transition-economy', 'Transition_economy'),
 ('lemons-market', 'The_Market_for_Lemons'),
 ('money-laundering', 'Money_laundering'),
 ('currency-war', 'Currency_war'),
 ('malinvestment', 'Malinvestment'),
]
out = {}
for eid, slug in cands:
    if os.path.exists('data/entries/' + eid + '.json'):
        print('SKIP', eid); continue
    try:
        d = json.loads(urllib.request.urlopen(urllib.request.Request(
            'https://en.wikipedia.org/api/rest_v1/page/summary/' + slug, headers=h), timeout=8, context=c).read())
        if d.get('extract'):
            out[eid] = {'title': d.get('title'), 'extract': d['extract'], 'slug': slug}
            print('OK', eid, '|', d.get('title')[:44])
    except Exception as e:
        print('FAIL', eid, type(e).__name__)
    time.sleep(0.4)
json.dump(out, open('_research/r115.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('抓到', len(out))
