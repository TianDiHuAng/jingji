# -*- coding: utf-8 -*-
"""续作EY：抓取缺 policy_response 的案例的维基全文（用于人工核验后撰写政策段）。"""
import json
import os
import ssl
import time
import urllib.parse
import urllib.request

OUT = '_research/wiki_full'
os.makedirs(OUT, exist_ok=True)
CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}

es = {}
for f in os.listdir('data/entries'):
    d = json.load(open('data/entries/' + f, encoding='utf-8'))
    es[d['id']] = d

src = json.load(open('data/sources.json', encoding='utf-8'))
smap = {x['id']: x for x in src['sources']}

cases = [d for d in es.values() if not d['unit'].startswith('U6') and not d.get('policy_response')]
print('待处理案例:', len(cases))

BATCH = cases[:20]
ok, fail = [], []
for e in BATCH:
    eid = e['id']
    p = os.path.join(OUT, eid + '.txt')
    if os.path.exists(p):
        ok.append(eid); continue
    # 取第一个维基来源的 url
    url = None
    for sid in e.get('sources', []):
        s = smap.get(sid)
        if s and s.get('url', '').startswith('https://en.wikipedia.org/wiki/'):
            url = s['url']
            break
    if not url:
        fail.append((eid, 'no wiki url')); continue
    page = urllib.parse.unquote(url.split('/wiki/')[-1]).replace('_', ' ')
    api = ('https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts'
           '&explaintext=1&redirects=1&titles=' + urllib.parse.quote(page))
    try:
        raw = urllib.request.urlopen(urllib.request.Request(api, headers=HDR), timeout=20, context=CTX).read()
        d = json.loads(raw)
        pages = d.get('query', {}).get('pages', {})
        txt = ''
        for _, pv in pages.items():
            txt = pv.get('extract', '')
        if not txt:
            fail.append((eid, 'empty')); continue
        open(p, 'w', encoding='utf-8').write(txt)
        ok.append((eid, len(txt)))
        time.sleep(0.5)
    except Exception as ex:
        fail.append((eid, type(ex).__name__))

print('成功:', len(ok))
for x in ok: print('  ', x)
print('失败:', len(fail))
for x in fail: print('  ', x)
