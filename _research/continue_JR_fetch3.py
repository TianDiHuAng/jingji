# -*- coding: utf-8 -*-
import json
import re
import ssl
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}
M = [('moral-hazard', 'Moral hazard'),
     ('animal-spirits', 'Animal spirits (Keynes)'),
     ('debt-trap-diplomacy', 'Debt-trap diplomacy')]
for eid, title in M:
    api = ('https://en.wikipedia.org/w/api.php?action=query&format=json'
           '&prop=extracts&explaintext=1&redirects=1&titles=' + urllib.parse.quote(title))
    try:
        d = json.loads(urllib.request.urlopen(
            urllib.request.Request(api, headers=HDR), timeout=20, context=CTX).read())
        txt = ''
        for _, pv in d.get('query', {}).get('pages', {}).items():
            txt = pv.get('extract', '') or ''
        if len(txt) > 500:
            open('_research/wiki_full/%s.txt' % eid, 'w', encoding='utf-8').write(txt)
            open('_research/wiki_full/%s.slug' % eid, 'w', encoding='utf-8').write(title.replace(' ', '_'))
            print('%-22s %6d | %s' % (eid, len(txt), re.findall(r'\n==+\s*(.+?)\s*==+\n', txt)[:5]))
        else:
            print('%-22s 过短 %d' % (eid, len(txt)))
    except Exception as ex:
        print('%-22s ERR %s' % (eid, type(ex).__name__))
