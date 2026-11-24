# -*- coding: utf-8 -*-
"""续作EH：补完最后16条related，达成全覆盖。"""
import json, glob

G = {
 'alm': ['asset-liability-mismatch', 'interest-rate-risk', 'maturity-transformation', 'bank-run'],
 'assignat-1790s': ['continental-currency-1775', 'hyperinflation', 'fiat-money', 'edict-maximum-prices'],
 'bailout': ['bail-in', 'tarp', 'too-big-to-fail', 'moral-hazard'],
 'beggar-thy-neighbour': ['competitive-devaluation', 'currency-war', 'tariff', 'smoot-hawley-1930'],
 'black-market': ['informal-economy', 'money-laundering', 'capital-control', 'currency-crisis'],
 'bond-crisis-1994': ['interest-rate-risk', 'bond', 'monetary-policy', 'yield-curve'],
 'call-option': ['put-option', 'option', 'black-scholes', 'hedging'],
 'capital-structure': ['leverage', 'capital-requirement', 'debt-overhang', 'modigliani-miller'],
 'central-bank-independence': ['time-inconsistency', 'inflation-targeting', 'fiscal-dominance', 'monetary-policy'],
 'central-counterparty': ['netting', 'otc', 'systemic-risk', 'counterparty-risk'],
 'circuit-breaker': ['black-monday-1987', 'mini-crash-1997', 'market-maker', 'liquidity'],
 'commercial-revolution': ['industrial-revolution', 'joint-stock', 'double-entry', 'history-of-banking'],
 'commodity-price-index': ['oil-crisis-1973', 'dutch-disease', 'cpi', 'inflation'],
 'continental-currency-1775': ['assignat-1790s', 'hyperinflation', 'fiat-money', 'seigniorage'],
 'convertible-bond': ['bond', 'option', 'capital-structure', 'credit-rating'],
 'creative-destruction': ['business-cycle', 'industrial-revolution', 'recession', 'austrian-theory'],
}

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
n, miss = 0, set()
for eid, rels in G.items():
    if eid not in es:
        miss.add('SELF:' + eid); continue
    valid = [r for r in rels if r in es and r != eid]
    miss |= {r for r in rels if r not in es}
    if not valid: continue
    f = es[eid]
    d = json.load(open(f, encoding='utf-8'))
    d['related'] = sorted(set(d.get('related', []) + valid))
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
print('设置 related:', n)
es2 = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
rest = [e['id'] for e in es2 if not e.get('related')]
print('有related:', sum(1 for e in es2 if e.get('related')), '/', len(es2))
print('仍无related:', rest)
print('缺失目标:', sorted(miss))
