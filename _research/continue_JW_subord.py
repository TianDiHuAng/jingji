# -*- coding: utf-8 -*-
import json
import re
import ssl
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}
api = ('https://en.wikipedia.org/w/api.php?action=query&format=json'
       '&prop=extracts&explaintext=1&redirects=1&titles=' + urllib.parse.quote('Subordination (finance)'))
d = json.loads(urllib.request.urlopen(urllib.request.Request(api, headers=HDR),
                                      timeout=20, context=CTX).read())
txt = ''
title = ''
for _, pv in d.get('query', {}).get('pages', {}).items():
    txt = pv.get('extract', '') or ''
    title = pv.get('title', '')
print('页面:', title, '| 长度:', len(txt))
if len(txt) > 400:
    open('_research/wiki_full/subordination.txt', 'w', encoding='utf-8').write(txt)
    print('章节:', re.findall(r'\n==+\s*(.+?)\s*==+\n', txt)[:8])
    print('正文:', ' '.join(txt[:900].split()))
else:
    print('内容过短，正文如下：')
    print(txt[:600])
