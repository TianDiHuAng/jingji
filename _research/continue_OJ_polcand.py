# -*- coding: utf-8 -*-
"""round 148：找有丰富专属缓存、缺 policy_response、且缓存含政策词的 case。"""
import glob, json, os, re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
GENERIC_HEAD = ('a currency crisis', 'an economic bubble', 'a financial crisis is', 'a bank run',
                'a speculative bubble', 'in economics, a recession', 'hyperinflation is')
POL = re.compile(r'(bail.?out|rescue|recapitali|nationali|central bank|government|interven|'
                 r'liquidity support|regulat|reform|lender of last resort|deposit insurance|'
                 r'reserve requirement|stress test|guarantee)', re.I)
cands = []
for e in es:
    if e['unit'].startswith('U6'):
        continue
    if e.get('policy_response'):
        continue
    p = os.path.join('_research/wiki_full', e['id'] + '.txt')
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8').read()
    if t[:200].lower().strip().startswith(GENERIC_HEAD):
        continue
    if len(t) < 8000:
        continue
    hits = len(POL.findall(t))
    if hits >= 8:
        cands.append((e['id'], len(t), hits, len(e.get('key_data') or []), (e.get('causal_chain') and 'Y' or '-')))
cands.sort(key=lambda x: -x[2])
print('候选(有专属富缓存/缺policy/含政策词≥8):', len(cands))
for c in cands[:25]:
    print('  %-28s cache=%d 政策词=%d key_data=%d causal=%s' % c)
