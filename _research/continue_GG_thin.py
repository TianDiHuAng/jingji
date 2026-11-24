# -*- coding: utf-8 -*-
"""续作GG：为"仅5个区块"的薄弱条目抓取维基全文，供补充时间线与学术分歧。"""
import glob
import json
import os
import re
import ssl
import time
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}
OUT = '_research/wiki_full'
GENERIC = {'Financial_crisis', 'Bank_run', 'Bank', 'Bailout', 'Stock_market_crash',
           'Debt_crisis', 'Currency_crisis', 'Inflation', 'Hyperinflation',
           'Economic_history', 'Economic_bubble', 'Speculative_bubble', 'Recession',
           'Arbitrage', 'Basel_III', 'Quantitative_easing', 'Seigniorage', 'Risk_premium',
           'Yield_curve', 'Leverage_(finance)', 'Corporation', 'Corporate_law', 'Debanking'}

es = {}
for f in os.listdir('data/entries'):
    d = json.load(open('data/entries/' + f, encoding='utf-8'))
    es[d['id']] = d
smap = {x['id']: x for x in json.load(open('data/sources.json', encoding='utf-8'))['sources']}

need = []
for e in es.values():
    if os.path.exists(os.path.join(OUT, e['id'] + '.txt')):
        continue
    # 判据：区块薄弱 = 无 timeline 且无 schools
    if e.get('timeline') or e.get('schools'):
        continue
    best = None
    for sid in e.get('sources', []):
        s = smap.get(sid)
        if not (s and s.get('url', '').startswith('https://en.wikipedia.org/wiki/')):
            continue
        slug = urllib.parse.unquote(s['url'].split('/wiki/')[-1])
        if slug in GENERIC:
            continue
        best = slug
        break
    if best:
        need.append((e['id'], best))

print('待抓:', len(need), flush=True)
ok, fail = 0, []
for eid, slug in need:
    api = ('https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts'
           '&explaintext=1&redirects=1&titles=' + urllib.parse.quote(slug))
    try:
        d = json.loads(urllib.request.urlopen(
            urllib.request.Request(api, headers=HDR), timeout=20, context=CTX).read())
        txt = ''
        for _, pv in d.get('query', {}).get('pages', {}).items():
            txt = pv.get('extract', '')
        if not txt:
            fail.append((eid, 'empty')); continue
        open(os.path.join(OUT, eid + '.txt'), 'w', encoding='utf-8').write(txt)
        open(os.path.join(OUT, eid + '.slug'), 'w', encoding='utf-8').write(slug)
        ok += 1
        time.sleep(0.35)
    except Exception as ex:
        fail.append((eid, type(ex).__name__))
print('成功', ok, '| 失败', len(fail), flush=True)
for x in fail[:8]:
    print('  ', x, flush=True)
