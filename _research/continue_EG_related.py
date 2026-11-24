# -*- coding: utf-8 -*-
"""续作EG：为剩余88条建立关联，目标related全覆盖。"""
import json, glob

G = {
 'creditanstalt': ['danatbank-1931', 'european-banking-1931', 'gold-standard', 'contagion'],
 'currency-war': ['competitive-devaluation', 'beggar-thy-neighbour', 'devaluation', 'gold-bloc'],
 'depression-economics': ['keynesian-economics', 'liquidity-trap', 'debt-deflation', 'secular-stagnation'],
 'dodd-frank': ['glass-steagall', 'volcker-rule', 'sarbanes-oxley', 'macroprudential'],
 'durable-goods': ['business-cycle', 'output-gap', 'recession-1937-1938', 'aggregate-demand'],
 'economic-recession': ['business-cycle', 'output-gap', 'unemployment', 'great-depression'],
 'edict-maximum-prices': ['crisis-third-century', 'debasement', 'inflation', 'price-revolution'],
 'ems': ['exchange-rate-regime', 'black-wednesday-1992', 'european-central-bank', 'impossible-trinity'],
 'esfs': ['esrb', 'macroprudential', 'euro-area-crisis', 'european-central-bank'],
 'esrb': ['esfs', 'macroprudential', 'systemic-risk', 'european-central-bank'],
 'european-central-bank': ['esrb', 'euro-area-crisis', 'fiscal-dominance', 'exchange-rate-regime'],
 'exchange-equalisation': ['sterling-crisis-1976', 'fx-intervention', 'foreign-exchange-reserves', 'tripartite-1936'],
 'family-office': ['archegos-2021', 'hedge-fund', 'margin-call', 'disclosure'],
 'fannie-mae': ['freddie-mac', 'mortgage-backed-security', 'subprime-crisis-2007', 'securitization'],
 'federal-reserve-act': ['national-banking-act', 'federal-reserve', 'panic-1907', 'lender-of-last-resort'],
 'federal-reserve': ['federal-reserve-act', 'lender-of-last-resort', 'monetary-policy', 'discount-window'],
 'financial-crisis': ['bank-failure', 'currency-crisis', 'debt-crisis', 'contagion'],
 'financial-repression': ['financial-deepening', 'capital-control', 'inflation', 'debt-overhang'],
 'fire-sale': ['margin-call', 'liquidity-risk', 'financial-accelerator', 'procyclicality'],
 'fiscal-military-state': ['government-debt', 'seigniorage', 'mercantilism', 'history-of-banking'],
 'fixed-exchange-rate': ['floating-exchange-rate', 'impossible-trinity', 'currency-crisis', 'currency-board'],
 'floating-exchange-rate': ['fixed-exchange-rate', 'impossible-trinity', 'fear-of-floating', 'exchange-rate-regime'],
 'forward-guidance': ['monetary-policy', 'central-bank-independence', 'inflation-targeting', 'rational-expectations'],
 'freddie-mac': ['fannie-mae', 'mortgage-backed-security', 'subprime-crisis-2007', 'securitization'],
 'free-banking': ['national-banking-act', 'second-bank', 'banking-school', 'bank-run'],
 'gamestop-2021': ['short-selling', 'hedge-fund', 'market-manipulation', 'speculative-bubble'],
 'glass-steagall': ['dodd-frank', 'volcker-rule', 'deposit-insurance', 'banking-act-1935'],
 'gold-bloc': ['gold-standard', 'tripartite-1936', 'exchange-equalisation', 'great-depression'],
 'gold-reserve-act-1934': ['gold-standard', 'gold-bloc', 'federal-reserve', 'devaluation'],
 'hedging': ['speculation', 'diversification', 'derivative', 'risk-management'],
 'history-of-banking': ['history-of-money', 'bardi-family', 'medici-bank', 'riksbank'],
 'housing-bubble': ['nz-property-bubble', 'japan-asset-bubble-1990', 'subprime-crisis-2007', 'credit-cycle'],
 'iais': ['iosco', 'esrb', 'prudential-regulation', 'insurance-history'],
 'indymac': ['washington-mutual', 'subprime-crisis-2007', 'bank-run', 'fdic-insurance'],
 'informal-economy': ['black-market', 'shadow-banking', 'microfinance', 'financial-inclusion'],
 'initial-public-offering': ['primary-market', 'secondary-market', 'stock-exchange', 'disclosure'],
 'interest-rate-parity': ['purchasing-power-parity', 'carry-trade', 'exchange-rate-regime', 'capital-control'],
 'interest-rate-swap': ['swap', 'ldi-strategy', 'interest-rate-risk', 'derivative'],
 'interest-rate': ['interest-rate-parity', 'yield-curve', 'monetary-policy', 'neutral-rate'],
 'iosco': ['iais', 'esrb', 'securities-regulation', 'disclosure'],
 'j-curve': ['marshall-lerner', 'balance-of-payments', 'exchange-rate-regime', 'devaluation'],
 'jamaica-accords': ['smithsonian-agreement', 'nixon-shock', 'bretton-woods', 'exchange-rate-regime'],
 'joint-stock': ['history-of-banking', 'secondary-market', 'initial-public-offering', 'limited-liability'],
 'laffer-curve': ['fiscal-policy', 'supply-side', 'tax-capacity', 'budget-balance'],
 'ldi-strategy': ['pension-fund', 'interest-rate-swap', 'uk-ldi-crisis-2022', 'margin-call'],
 'lemons-market': ['information-asymmetry', 'adverse-selection', 'credit-rationing', 'disclosure'],
 'louvre-accord': ['plaza-accord', 'exchange-rate-regime', 'gold-standard', 'tripartite-1936'],
 'malinvestment': ['austrian-theory', 'credit-cycle', 'capital-structure', 'business-cycle'],
 'marshall-lerner': ['j-curve', 'balance-of-payments', 'elasticity', 'devaluation'],
 'marshall-plan': ['world-bank', 'bretton-woods', 'exchange-rate-regime', 'development-economics'],
 'merrill-lynch': ['lehman', 'bear-stearns', 'bank-of-america', 'subprime-crisis-2007'],
 'mmt': ['fiscal-dominance', 'monetary-policy', 'inflation', 'government-debt'],
 'money-laundering': ['black-market', 'informal-economy', 'fatf', 'capital-control'],
 'municipal-bond': ['puerto-rico-debt-2014', 'nyc-fiscal-1975', 'government-debt', 'sovereign-default'],
 'national-banking-act': ['free-banking', 'federal-reserve-act', 'second-bank', 'panic-1873'],
 'natural-rate-unemployment': ['nairu', 'phillips-curve', 'unemployment', 'output-gap'],
 'nixon-shock': ['bretton-woods', 'smithsonian-agreement', 'jamaica-accords', 'gold-standard'],
 'nz-1984-reform': ['nz-finance-collapse', 'financial-liberalization', 'financial-repression', 'washington-consensus'],
 'nz-finance-collapse': ['nz-1984-reform', 'shadow-banking', 'deposit-insurance', 'rhode-island-banking-1990'],
 'oil-price-war-2020': ['oil-crisis-1973', 'oil-crisis-1979', 'commodity-price-index', 'covid-crash-2020'],
 'original-sin': ['currency-mismatch', 'asset-liability-mismatch', 'sudden-stop', 'fear-of-floating'],
 'pension-fund': ['ldi-strategy', 'uk-ldi-crisis-2022', 'sovereign-wealth-fund', 'insurance-history'],
 'plaza-accord': ['louvre-accord', 'exchange-rate-regime', 'japan-asset-bubble-1990', 'tripartite-1936'],
 'poverty-trap': ['middle-income-trap', 'microfinance', 'development-economics', 'growth-inequality'],
 'ppi': ['cpi', 'commodity-price-index', 'inflation', 'monetary-transmission'],
 'price-revolution': ['commodity-money', 'inflation', 'edict-maximum-prices', 'mercantilism'],
 'primary-market': ['secondary-market', 'initial-public-offering', 'stock-exchange', 'liquidity'],
 'principal-agent': ['moral-hazard', 'information-asymmetry', 'corporate-governance', 'enron'],
 'secondary-market': ['primary-market', 'stock-exchange', 'liquidity', 'market-maker'],
 'sovereign-risk': ['sovereign-default', 'country-risk', 'credit-rating', 'debt-crisis'],
 'sovereign-wealth-fund': ['foreign-exchange-reserves', 'pension-fund', 'resource-curse', 'norway-gpfg'],
 'washington-consensus': ['structural-adjustment', 'development-economics', 'world-bank', 'imf'],
 'washington-mutual': ['indymac', 'subprime-crisis-2007', 'bank-run', 'securitization'],
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
