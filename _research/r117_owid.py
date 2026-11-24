import urllib.request, ssl, csv, io, json
c = ssl._create_unverified_context()
h = {'User-Agent': 'EconCrisisBot/1.0'}
SLUGS = {'unemployment': 'unemployment-rate', 'inflation': 'inflation-of-consumer-prices',
         'gdp': 'gdp-worldbank', 'growth': 'real-gdp-growth'}
out = {}
for k, slug in SLUGS.items():
    u = f'https://ourworldindata.org/grapher/{slug}.csv?v=1&csvType=full&useColumnShortNames=true'
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=25, context=c)
        txt = r.read().decode('utf-8', 'replace')
        rows = list(csv.DictReader(io.StringIO(txt)))
        out[k] = {'n': len(rows), 'cols': list(rows[0].keys())[:6]}
        print(f'{k}: {len(rows)} rows | cols={list(rows[0].keys())[:5]}')
        open(f'_research/owid_{k}.csv', 'w', encoding='utf-8').write(txt)
    except Exception as e:
        print(f'{k}: FAIL {type(e).__name__}')
json.dump(out, open('_research/owid_meta.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
