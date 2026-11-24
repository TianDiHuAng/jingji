import urllib.request, ssl, json, time, os
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 EconCrisisBot/1.0'}
cands = [
 ('bis', 'Bank_for_International_Settlements'),
 ('gatt', 'General_Agreement_on_Tariffs_and_Trade'),
 ('oecd', 'OECD'),
 ('fsb', 'Financial_Stability_Board'),
 ('esfs', 'European_System_of_Financial_Supervision'),
 ('esrb', 'European_Systemic_Risk_Board'),
 ('iosco', 'International_Organization_of_Securities_Commissions'),
 ('fatf', 'Financial_Action_Task_Force'),
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
json.dump(out, open('_research/r74_inst.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('抓到', len(out))
