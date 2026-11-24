# -*- coding: utf-8 -*-
"""round 134：找出 sources 全部为通用页的案例条目（可能缺专属来源）。"""
import glob, json

GENERIC = {'w-en-debt-crisis', 'w-en-financial-crisis', 'w-en-currency-crisis',
           'w-en-speculative-bubble', 'w-en-bank-run', 'w-en-hyperinflation',
           'w-en-recession', 'w-en-inflation', 'w-en-systemic-risk', 'w-en-too-big-to-fail',
           'w-en-bank-regulation', 'w-en-financial-regulation', 'w-en-economic-history',
           'w-en-bubble', 'w-en-great-depression', 'w-en-deflation'}
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
onlyg = [e for e in cases if e.get('sources') and set(e['sources']) <= GENERIC]
print('案例中 sources 全为通用页: %d' % len(onlyg))
for e in sorted(onlyg, key=lambda x: x['tier']):
    print('  %-30s %-4s src=%s | %s' % (e['id'], e['tier'], e['sources'], e['title'][:18]))
