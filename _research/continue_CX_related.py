# -*- coding: utf-8 -*-
"""续作CX：为近期新增条目补充语义 related（并回填对称链接）。"""
import json, glob

REL = {
 'lehman': ['subprime-crisis-2007', 'aig', 'bear-stearns', 'merrill-lynch', 'too-big-to-fail', 'bank-crisis-2023'],
 'archegos-2021': ['ltcm', 'credit-suisse-2023', 'margin-call', 'leverage', 'family-office' ],
 'uk-ldi-crisis-2022': ['margin-call', 'fire-sale', 'procyclicality', 'pension-fund', 'northern-rock'],
 'continental-illinois-1984': ['penn-square-1982', 'too-big-to-fail', 'savings-loan-1986', 'deposit-insurance'],
 'penn-square-1982': ['continental-illinois-1984', 'securitization', 'adverse-selection'],
 'franklin-national-1974': ['barings-1995', 'bank-failure', 'moral-hazard'],
 'albania-pyramid-1997': ['ponzi-scheme', 'bernie-madoff', 'informal-economy'],
 'encilhamento-1890': ['speculative-bubble', 'brazil-hyper-1980', 'baring-crisis-1890', 'redenomination'],
 'haitian-independence-debt': ['sovereign-default', 'debt-crisis', 'fiscal-dominance'],
 'nyc-fiscal-1975': ['puerto-rico-debt-2014', 'australian-banking-1893', 'sovereign-default'],
 'swedish-crisis-1990s': ['finnish-banking-1990', 'norwegian-banking-1988', 'japan-asset-bubble-1990', 'bail-in'],
 'smoot-hawley-1930': ['great-depression', 'beggar-thy-neighbour', 'gold-bloc', 'london-econ-1933'],
 'scissors-crisis-1923': ['soviet-hyper-1917', 'price-revolution', 'middle-income-trap'],
 'london-econ-1933': ['gold-bloc', 'tripartite-1936', 'bretton-woods', 'smoot-hawley-1930'],
 'glass-steagall-1933': ['deposit-insurance', 'banking-act-1935', 'emergency-banking-act-1933', 'shadow-banking'],
 'nira-1933': ['great-depression', 'fiscal-multiplier', 'automatic-stabilizer'],
 'crisis-late-middle-ages': ['bardi-family', 'black-death' ],
 'yemen-currency-divergence': ['currency-substitution', 'currency-crisis', 'syrian-pound-crisis', 'black-market'],
 'syrian-pound-crisis': ['yemen-currency-divergence', 'currency-crisis', 'lebanese-liquidity-2019', 'black-market'],
 'iranian-economic-crisis': ['venezuela-hyper-2016', 'stabilization-program', 'original-sin'],
 'angolan-kwanza-devaluation': ['angola-oil-dependence', 'redenomination', 'dutch-disease'],
 'zambian-kwacha-reform': ['redenomination', 'zimbabwe-hyper-2007', 'hyperinflation'],
 'nz-property-bubble': ['housing-bubble', 'japan-asset-bubble-1990', 'herd-behavior'],
 'cook-islands-currency': ['currency-substitution', 'currency-board', 'legal-tender'],
 'procyclicality': ['financial-accelerator', 'macroprudential', 'credit-cycle'],
 'margin-call': ['fire-sale', 'procyclicality', 'archegos-2021', 'uk-ldi-crisis-2022'],
 'secular-stagnation': ['neutral-rate', 'liquidity-trap', 'debt-deflation'],
 'financialization': ['too-big-to-fail', 'financial-repression', 'shadow-banking'],
 'asset-liability-mismatch': ['original-sin', 'bank-run', 'basel-iii', 'currency-crisis'],
 'settlement-risk': ['systemic-risk', 'financial-contagion', 'herstatt'],
 'bail-in': ['cypriot-2013', 'bailout', 'deposit-insurance', 'too-big-to-fail'],
 'neutral-rate': ['monetary-policy', 'secular-stagnation', 'fiscal-dominance'],
}

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
n_set, miss = 0, set()
for eid, rels in REL.items():
    if eid not in es:
        miss.add(eid); continue
    f = es[eid]
    d = json.load(open(f, encoding='utf-8'))
    valid = [r for r in rels if r in es and r != eid]
    miss |= {r for r in rels if r not in es}
    if valid:
        d['related'] = sorted(set(d.get('related', []) + valid))
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n_set += 1
print('设置 related 的条目:', n_set)
print('不存在的目标 id（已跳过）:', sorted(miss))
