import urllib.request, ssl, json, time, os
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
cands = [
 ('paris-club', 'Paris_Club'),
 ('london-club', 'London_Club_(debt)'),
 ('iais', 'International_Association_of_Insurance_Supervisors'),
 ('aiib', 'Asian_Infrastructure_Investment_Bank'),
 ('adb', 'Asian_Development_Bank'),
 ('ebrd', 'European_Bank_for_Reconstruction_and_Development'),
 ('idb', 'Inter-American_Development_Bank'),
 ('afdb', 'African_Development_Bank'),
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
            print('OK', eid, '|', d.get('title')[:42])
    except Exception as e:
        print('FAIL', eid, type(e).__name__)
    time.sleep(0.4)
json.dump(out, open('_research/r75_inst2.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('抓到', len(out))
