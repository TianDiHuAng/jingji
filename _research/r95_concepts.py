import urllib.request, ssl, json, time, os
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
cands = [
 ('neutral-rate', 'Natural_rate_of_interest'),
 ('policy-rate', 'Policy_rate'),
 ('bank-resolution', 'Bank_resolution'),
 ('bail-in', 'Bail-in'),
 ('tlac', 'Total_loss-absorbing_capacity'),
 ('leverage-ratio', 'Leverage_ratio'),
 ('liquidity-coverage-ratio', 'Liquidity_coverage_ratio'),
 ('capital-controls', 'Capital_control'),
 ('special-drawing-rights', 'Special_drawing_rights'),
 ('currency-substitution', 'Currency_substitution'),
 ('shadow-economy', 'Shadow_economy'),
 ('j-curve', 'J_curve'),
 ('marshall-lerner', 'Marshall%E2%80%93Lerner_condition'),
 ('interest-parity', 'Interest_rate_parity'),
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
    time.sleep(0.4)
json.dump(out, open('_research/r95_concepts.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('抓到', len(out))
