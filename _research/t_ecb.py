import urllib.request, ssl
c = ssl._create_unverified_context()
h = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'}
tests = [
 ('ECB-debt', 'https://data-api.ecb.europa.eu/service/data/GOV_10DD_EDPT1/D.GR.L.S13.GD.T?format=csvdata&startPeriod=2009&endPeriod=2017'),
 ('ECB-root', 'https://data-api.ecb.europa.eu/service/'),
 ('BIS-root', 'https://stats.bis.org/api/v1/data/'),
]
for n, u in tests:
    try:
        r = urllib.request.urlopen(urllib.request.Request(u, headers=h), timeout=15, context=c)
        d = r.read()
        print(n, 'OK', r.status, len(d))
        print('  ', d[:180])
    except Exception as e:
        print(n, 'FAIL', type(e).__name__)
