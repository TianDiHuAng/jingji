# -*- coding: utf-8 -*-
"""续作FH：修正抓取逻辑——优先选与条目 id 匹配的维基来源，重抓误用通用页的案例。"""
import json
import os
import ssl
import time
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}
OUT = '_research/wiki_full'
GENERIC = {'Financial_crisis', 'Bank_run', 'Bank', 'Bailout', 'Stock_market_crash'}

es = {}
for f in os.listdir('data/entries'):
    d = json.load(open('data/entries/' + f, encoding='utf-8'))
    es[d['id']] = d
smap = {x['id']: x for x in json.load(open('data/sources.json', encoding='utf-8'))['sources']}


def pick_url(e):
    """优先选 slug 与条目 id 有词重叠的维基来源，跳过通用页。"""
    cands = []
    for sid in e.get('sources', []):
        s = smap.get(sid)
        if not (s and s.get('url', '').startswith('https://en.wikipedia.org/wiki/')):
            continue
        slug = urllib.parse.unquote(s['url'].split('/wiki/')[-1])
        cands.append((slug, sid))
    if not cands:
        return None, 'no wiki'
    # 打分：slug 词与 id 词重叠数
    idtoks = set(e['id'].replace('-', ' ').split())
    best, bestscore = None, -1
    for slug, sid in cands:
        if slug in GENERIC:
            continue
        stoks = set(slug.lower().replace('_', ' ').replace('-', ' ').split())
        score = len(idtoks & stoks)
        if score > bestscore:
            best, bestscore = (slug, sid), score
    if not best:
        return None, 'only generic'
    return best, None


todo = []
for d in es.values():
    if d['unit'].startswith('U6') or d.get('policy_response'):
        continue
    url, why = pick_url(d)
    if not url:
        continue
    slug = url[0]
    # 若已抓的文件不是这个 slug 对应的内容，重抓
    meta_p = os.path.join(OUT, d['id'] + '.slug')
    old = open(meta_p).read().strip() if os.path.exists(meta_p) else ''
    if old == slug:
        continue
    todo.append((d, slug))

print('需重抓/新抓:', len(todo), flush=True)
ok, fail = 0, []
for e, slug in todo[:45]:
    eid = e['id']
    page = urllib.parse.unquote(slug).replace('_', ' ')
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
            fail.append((eid, slug, 'empty'))
            continue
        open(os.path.join(OUT, eid + '.txt'), 'w', encoding='utf-8').write(txt)
        open(os.path.join(OUT, eid + '.slug'), 'w', encoding='utf-8').write(slug)
        ok += 1
        time.sleep(0.4)
    except Exception as ex:
        fail.append((eid, slug, type(ex).__name__))

print('成功', ok, '| 失败', len(fail), flush=True)
for x in fail[:10]:
    print('  ', x, flush=True)
