# -*- coding: utf-8 -*-
"""round 133d：找出 key_data 仅引用"通用页"来源、且 note 含具体数字/专名的行（疑来源错标）。"""
import glob, json, re

GENERIC = {'w-en-debt-crisis', 'w-en-financial-crisis', 'w-en-currency-crisis',
           'w-en-speculative-bubble', 'w-en-bank-run', 'w-en-hyperinflation',
           'w-en-recession', 'w-en-inflation', 'w-en-systemic-risk', 'w-en-too-big-to-fail',
           'w-en-bank-regulation', 'w-en-financial-regulation'}
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
hits = []
for e in es:
    if e['unit'].startswith('U6'):
        continue
    for k in e.get('key_data') or []:
        ss = set(k.get('sources') or [])
        if ss and ss <= GENERIC:
            hits.append((e['id'], k['label'][:30], k['value'], sorted(ss)))
print('=== key_data 仅引通用页来源（疑错标）===')
print('条数:', len(hits))
for h in hits:
    print('  %-28s %-30s v=%-8s %s' % h)
