# -*- coding: utf-8 -*-
"""续作NI：修复 key_data 来源错标——把仅引"通用页"的行改引条目的专属来源。

判据：该行数字确实出现在条目的 wiki_full 缓存（专属页）中，且条目 sources 中存在非通用来源。
"""
import glob, json, os, re

GENERIC = {'w-en-debt-crisis', 'w-en-financial-crisis', 'w-en-currency-crisis',
           'w-en-speculative-bubble', 'w-en-bank-run', 'w-en-hyperinflation',
           'w-en-recession', 'w-en-inflation', 'w-en-systemic-risk', 'w-en-too-big-to-fail',
           'w-en-bank-regulation', 'w-en-financial-regulation'}
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]

def variants(v):
    out = set(); s = str(v).replace(',', '')
    out.add(str(v)); out.add(s)
    try:
        f = float(s)
        if f == int(f):
            out.add(str(int(f))); out.add('{:,}'.format(int(f)))
        else:
            out.add('%.1f' % f); out.add('%.2f' % f)
    except ValueError:
        pass
    return out

changed = 0
left = []
byid = {e['id']: e for e in es}
for e in es:
    if e['unit'].startswith('U6'):
        continue
    p = os.path.join('_research/wiki_full', e['id'] + '.txt')
    cache = open(p, encoding='utf-8').read() if os.path.exists(p) else ''
    dedicated = [s for s in (e.get('sources') or []) if s not in GENERIC]
    if not dedicated:
        continue
    ch = False
    for k in e.get('key_data') or []:
        ss = set(k.get('sources') or [])
        if ss and ss <= GENERIC:
            in_cache = any(v and v in cache for v in variants(k['value']))
            if in_cache:
                k['sources'] = [dedicated[0]]
                changed += 1; ch = True
            else:
                left.append((e['id'], k['label'][:24], k['value'], sorted(ss)))
    if ch:
        e['pending_notes'] = (e.get('pending_notes', '')
            + ' 【续作NI｜round133】部分 key_data 原误标通用来源，已按"数字确在专属页缓存中"改引专属来源 %s。' % dedicated[0])
        json.dump(e, open('data/entries/%s.json' % e['id'], 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('已改来源归属的行:', changed)
print('数字不在缓存、保留待查的行:', len(left))
for x in left:
    print('  ', x)
