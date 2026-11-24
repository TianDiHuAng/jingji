# -*- coding: utf-8 -*-
import json
import re
import ssl
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}
M = [('south-sea-bubble-1720', ['South Sea Bubble', 'South Sea Company']),
     ('bear-stearns', ['Bear Stearns']),
     ('bcci', ['Bank of Credit and Commerce International', 'BCCI'])]
for eid, titles in M:
    print('===', eid)
    for title in titles:
        api = ('https://en.wikipedia.org/w/api.php?action=query&format=json'
               '&prop=extracts&explaintext=1&redirects=1&titles=' + urllib.parse.quote(title))
        try:
            d = json.loads(urllib.request.urlopen(
                urllib.request.Request(api, headers=HDR), timeout=20, context=CTX).read())
            txt = ''
            pt = ''
            for _, pv in d.get('query', {}).get('pages', {}).items():
                txt = pv.get('extract', '') or ''
                pt = pv.get('title', '')
            print('  %-40s %s %d' % (title, pt[:30], len(txt)))
            if len(txt) > 1500:
                open('_research/wiki_full/%s.txt' % eid, 'w', encoding='utf-8').write(txt)
                open('_research/wiki_full/%s.slug' % eid, 'w', encoding='utf-8').write(title.replace(' ', '_'))
                print('    -> 已保存')
                break
        except Exception as ex:
            print('  %-40s ERR %s' % (title, type(ex).__name__))
