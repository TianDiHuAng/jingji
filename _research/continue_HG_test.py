# -*- coding: utf-8 -*-
"""续作HG：为 12 个待建概念测维基页面并抓取摘要/全文。"""
import json
import os
import ssl
import time
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}
OUT = '_research/wiki_full'

CAND = {
 'externalities': [('Externality', 'Externality')],
 'var': [('Value_at_risk', 'Value at risk')],
 'sacrifice-ratio': [('Sacrifice_ratio', 'Sacrifice ratio')],
 'regulatory-arbitrage': [('Regulatory_arbitrage', 'Regulatory arbitrage')],
 'taper-tantrum': [('Taper_tantrum', 'Taper tantrum'), ('2013_taper_tantrum', '2013 taper tantrum')],
 'term-premium': [('Term_premium', 'Term premium')],
 'pigouvian-tax': [('Pigouvian_tax', 'Pigouvian tax')],
 'disclosure': [('Disclosure_(finance)', 'Disclosure (finance)')],
 'leading-indicator': [('Leading_indicator', 'Leading indicator')],
 'bank-resolution': [('Bank_resolution', 'Bank resolution')],
 'common-pool': [('Common-pool_resource', 'Common-pool resource')],
 'bank-holiday': [('Bank_holiday', 'Bank holiday')],
}

ok, fail = 0, []
for eid, cands in CAND.items():
    got = False
    for slug, title in cands:
        if os.path.exists(os.path.join(OUT, eid + '.txt')):
            ok += 1
            got = True
            break
        api = ('https://en.wikipedia.org/w/api.php?action=query&format=json&prop=extracts'
               '&explaintext=1&redirects=1&titles=' + urllib.parse.quote(title))
        try:
            d = json.loads(urllib.request.urlopen(
                urllib.request.Request(api, headers=HDR), timeout=20, context=CTX).read())
            txt = ''
            real = ''
            for _, pv in d.get('query', {}).get('pages', {}).items():
                txt = pv.get('extract', '') or ''
                real = pv.get('title', '')
            if len(txt) > 500:
                open(os.path.join(OUT, eid + '.txt'), 'w', encoding='utf-8').write(txt)
                open(os.path.join(OUT, eid + '.slug'), 'w', encoding='utf-8').write(slug)
                print('%-24s OK  %-28s %d字符' % (eid, real[:28], len(txt)))
                ok += 1
                got = True
                break
            else:
                print('%-24s --  %-28s %d字符（过短）' % (eid, real[:28], len(txt)))
        except Exception as ex:
            print('%-24s ERR %-28s %s' % (eid, slug[:28], type(ex).__name__))
        time.sleep(0.3)
    if not got:
        fail.append(eid)

print('\n成功 %d | 失败 %d: %s' % (ok, len(fail), ', '.join(fail)))
