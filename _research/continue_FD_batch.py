# -*- coding: utf-8 -*-
"""续作FD：批量抓取剩余案例的维基全文（每次最多40个）。"""
import json
import os
import ssl
import time
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}
OUT = '_research/wiki_full'
os.makedirs(OUT, exist_ok=True)

es = {}
for f in os.listdir('data/entries'):
    d = json.load(open('data/entries/' + f, encoding='utf-8'))
    es[d['id']] = d
smap = {x['id']: x for x in json.load(open('data/sources.json', encoding='utf-8'))['sources']}

todo = [d for d in es.values() if not d['unit'].startswith('U6') and not d.get('policy_response')]
todo = [d for d in todo if not os.path.exists(os.path.join(OUT, d['id'] + '.txt'))]
print('剩余待抓:', len(todo), flush=True)

ok, fail = 0, []
for e in todo[:40]:
    eid = e['id']
    url = None
    for sid in e.get('sources', []):
        s = smap.get(sid)
        if s and s.get('url', '').startswith('https://en.wikipedia.org/wiki/'):
            url = s['url']
            break
    if not url:
        fail.append((eid, 'no wiki url'))
        continue
    page = urllib.parse.unquote(url.split('/wiki/')[-1]).replace('_', ' ')
    api = ('https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts'
           '&explaintext=1&redirects=1&titles=' + urllib.parse.quote(page))
    try:
        raw = urllib.request.urlopen(urllib.request.Request(api, headers=HDR),
                                     timeout=20, context=CTX).read()
        d = json.loads(raw)
        txt = ''
        for _, pv in d.get('query', {}).get('pages', {}).items():
            txt = pv.get('extract', '')
        if not txt:
            fail.append((eid, 'empty'))
            continue
        open(os.path.join(OUT, eid + '.txt'), 'w', encoding='utf-8').write(txt)
        ok += 1
        time.sleep(0.4)
    except Exception as ex:
        fail.append((eid, type(ex).__name__))

print('成功', ok, '| 失败', len(fail), flush=True)
print(fail, flush=True)
