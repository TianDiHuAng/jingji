import urllib.request, ssl, json, time, os
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
cands = [
 ('bank-resolution', 'Bank_resolution'),
 ('toxic-assets', 'Toxic_asset'),
 ('junk-bond', 'High-yield_debt'),
 ('sacrifice-ratio', 'Sacrifice_ratio'),
 ('prisoners-dilemma', 'Prisoner%27s_dilemma'),
 ('property-rights', 'Property_rights_(economics)'),
 ('transaction-cost', 'Transaction_cost'),
 ('rent-seeking', 'Rent-seeking'),
 ('market-failure', 'Market_failure'),
 ('payment-system', 'Payment_system'),
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
            print('OK', eid, '|', d.get('title')[:40])
    except Exception as e:
        print('FAIL', eid, type(e).__name__)
    time.sleep(0.35)
json.dump(out, open('_research/r116.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('抓到', len(out))
