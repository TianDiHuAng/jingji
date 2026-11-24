# -*- coding: utf-8 -*-
"""续作DG：为剩余条目建立最后10组关联。"""
import json, glob

G = {
 # 11 财政政策
 'fiscal-policy': ['fiscal-multiplier', 'automatic-stabilizer', 'budget-balance', 'crowding-out',
                   'austerity', 'fiscal-capacity', 'debt-ceiling'],
 'fiscal-multiplier': ['fiscal-policy', 'automatic-stabilizer', 'aggregate-demand', 'crowding-out'],
 'automatic-stabilizer': ['fiscal-policy', 'fiscal-multiplier', 'budget-balance', 'austerity'],
 'budget-balance': ['fiscal-policy', 'debt-ceiling', 'austerity', 'fiscal-space'],
 'crowding-out': ['fiscal-policy', 'fiscal-multiplier', 'government-debt', 'interest-rate'],
 'austerity': ['fiscal-policy', 'fiscal-multiplier', 'greek-debt-crisis', 'stabilization-program'],
 'fiscal-capacity': ['fiscal-policy', 'fiscal-space', 'informal-economy', 'tax-capacity'],
 'debt-ceiling': ['budget-balance', 'government-debt', 'global-debt', 'sovereign-default'],
 # 12 增长与发展
 'development-economics': ['economic-history', 'industrial-revolution', 'globalization', 'great-divergence',
                           'middle-income-trap', 'lewis-turning-point'],
 'economic-history': ['development-economics', 'industrial-revolution', 'globalization', 'great-divergence'],
 'industrial-revolution': ['economic-history', 'development-economics', 'commercial-revolution', 'creative-destruction'],
 'globalization': ['great-divergence', 'free-trade', 'comparative-advantage', 'global-imbalances'],
 'great-divergence': ['economic-history', 'globalization', 'industrial-revolution', 'development-economics'],
 'middle-income-trap': ['development-economics', 'lewis-turning-point', 'import-substitution', 'growth'],
 'lewis-turning-point': ['development-economics', 'middle-income-trap', 'demographic-dividend', 'labour-market'],
 'demographic-dividend': ['lewis-turning-point', 'development-economics', 'population', 'secular-stagnation'],
 'export-oriented': ['import-substitution', 'development-economics', 'comparative-advantage', 'asian-financial-crisis-1997'],
 'import-substitution': ['export-oriented', 'development-economics', 'latin-american-debt-1975', 'comparative-advantage'],
 'comparative-advantage': ['free-trade', 'mercantilism', 'division-of-labour', 'globalization'],
 'free-trade': ['comparative-advantage', 'mercantilism', 'globalization', 'gatt'],
 'mercantilism': ['comparative-advantage', 'free-trade', 'fiscal-military-state', 'bullion'],
 'division-of-labour': ['comparative-advantage', 'industrial-revolution', 'invisible-hand', 'specialization'],
 # 13 微观与制度基础
 'aggregate-demand': ['aggregate-supply', 'keynesian-economics', 'fiscal-multiplier', 'output-gap'],
 'aggregate-supply': ['aggregate-demand', 'oil-crisis-1973', 'output-gap', 'stagflation'],
 'elasticity': ['aggregate-demand', 'marshall-lerner', 'j-curve', 'tax-incidence'],
 'externality': ['institutional-economics', 'pigouvian-tax', 'market-failure', 'common-pool'],
 'game-theory': ['coordination-games', 'information-asymmetry', 'prisoners-dilemma', 'moral-hazard'],
 'institutional-economics': ['externality', 'property-rights', 'transaction-cost', 'economic-history'],
 'opportunity-cost': ['marginal-utility', 'loanable-funds', 'interest-rate', 'comparative-advantage'],
 'marginal-utility': ['opportunity-cost', 'classical-economics', 'loanable-funds', 'demand'],
 'invisible-hand': ['laissez-faire', 'classical-economics', 'free-trade', 'division-of-labour'],
 'laissez-faire': ['invisible-hand', 'classical-economics', 'free-trade', 'physiocracy'],
 'physiocracy': ['laissez-faire', 'classical-economics', 'invisible-hand', 'agriculture'],
 'political-economy': ['institutional-economics', 'classical-economics', 'public-choice', 'rent-seeking'],
 # 14 银行与机构史
 'bank-of-england': ['lender-of-last-resort', 'overend-gurney', 'central-bank', 'baring-crisis-1890'],
 'bardi-family': ['medici-bank', 'history-of-banking', 'credit-money', 'crisis-late-middle-ages'],
 'medici-bank': ['bardi-family', 'history-of-banking', 'double-entry', 'credit-money'],
 'banking-act-1935': ['glass-steagall', 'emergency-banking-act-1933', 'federal-reserve', 'deposit-insurance'],
 'emergency-banking-act-1933': ['glass-steagall', 'banking-act-1935', 'great-depression', 'bank-holiday'],
 'arthur-andersen': ['enron', 'credit-rating', 'audit-failure', 'information-asymmetry'],
 'dreel': ['drexel', 'enron', 'arthur-andersen'],
 'drexel': ['arthur-andersen', 'savings-loan-1986', 'junk-bond', 'leverage'],
 'barings-1995': ['franklin-national-1974', 'bank-failure', 'rogue-trader', 'derivative'],
 'bcci': ['barings-1995', 'money-laundering', 'bank-failure', 'supervision'],
 'credit-anstalt': ['danatbank-1931', 'european-banking-1931', 'great-depression', 'contagion'],
 'danatbank-1931': ['credit-anstalt', 'european-banking-1931', 'great-depression', 'bank-run'],
 'european-banking-1931': ['credit-anstalt', 'danatbank-1931', 'great-depression', 'gold-standard'],
 'insurance-history': ['history-of-banking', 'lloyds', 'risk-pooling', 'actuarial'],
 # 15 抵押、证券化与信用
 'collateral': ['margin-call', 'fire-sale', 'procyclicality', 'secured-lending'],
 'credit-enhancement': ['securitization', 'credit-rating', 'collateralized-debt-obligation', 'moral-hazard'],
 'credit-rating': ['information-asymmetry', 'credit-enhancement', 'securitization', 'subprime-lending'],
 'credit-risk': ['credit-rating', 'credit-rationing', 'counterparty-risk', 'default'],
 'credit-rationing': ['information-asymmetry', 'adverse-selection', 'credit-risk', 'lemons-market'],
 'off-balance-sheet': ['securitization', 'shadow-banking', 'credit-enhancement', 'disclosure'],
 'margin-finance': ['margin-call', 'leverage', 'fire-sale', 'collateral'],
 'netting': ['otc', 'central-counterparty', 'settlement-risk', 'clearing'],
 'otc': ['netting', 'central-counterparty', 'derivative', 'counterparty-risk'],
 # 16 宏观指标与工具
 'gdp': ['gnp', 'national-income', 'output-gap', 'potential-output'],
 'gnp': ['gdp', 'national-income', 'current-account', 'output-gap'],
 'national-income': ['gdp', 'gnp', 'aggregate-demand', 'keynesian-economics'],
 'output-gap': ['potential-output', 'gdp', 'phillips-curve', 'okuns-law'],
 'potential-output': ['output-gap', 'nairu', 'gdp', 'inflation'],
 'okuns-law': ['output-gap', 'unemployment', 'business-cycle', 'potential-output'],
 'basis-point': ['interest-rate', 'bond', 'arbitrage', 'yield-curve'],
 'bid-ask': ['market-maker', 'liquidity', 'market-risk', 'fire-sale'],
 'pmi': ['business-cycle', 'leading-indicator', 'output-gap', 'recession'],
 'gini': ['poverty-trap', 'inequality', 'development-economics', 'political-economy'],
 'fisher-equation': ['interest-rate', 'inflation', 'monetarism', 'neutral-rate'],
 'menu-cost': ['new-keynesian', 'inflation', 'sticky-prices', 'phillips-curve'],
 'neutrality-of-money': ['monetarism', 'classical-economics', 'money-supply', 'inflation'],
 'loanable-funds': ['interest-rate', 'classical-economics', 'savings', 'investment'],
 'is-lm': ['keynesian-economics', 'monetary-policy', 'fiscal-policy', 'aggregate-demand'],
 'money-market': ['interbank-lending', 'central-bank', 'liquidity', 'short-term-rate'],
 'liquidity': ['money-market', 'fire-sale', 'liquidity-risk', 'market-maker'],
 'liquidity-trap': ['liquidity-preference', 'monetary-policy', 'deflation', 'secular-stagnation'],
 'leverage': ['deleveraging', 'margin-finance', 'procyclicality', 'leverage-cycle'],
 'deleveraging': ['leverage', 'balance-sheet-recession', 'fire-sale', 'debt-deflation'],
 'balance-sheet-recession': ['deleveraging', 'debt-deflation', 'financial-accelerator', 'japan-asset-bubble-1990'],
 'bank-failure': ['bank-run', 'deposit-insurance', 'bank-resolution', 'lender-of-last-resort'],
 'bad-bank': ['bank-failure', 'bank-resolution', 'toxic-assets', 'securitization'],
 'credit-crunch': ['credit-rationing', 'financial-accelerator', 'credit-cycle', 'bank-failure'],
 'financial-disintermediation': ['shadow-banking', 'credit-crunch', 'securitization', 'bank-failure'],
 'devaluation': ['competitive-devaluation', 'currency-crisis', 'fixed-exchange-rate', 'original-sin'],
 'disinflation': ['inflation', 'inflation-targeting', 'stabilization-program', 'sacrifice-ratio'],
 'currency-internationalization': ['reserve-currency', 'de-dollarization', 'exorbitant-privilege', 'capital-account'],
 'exorbitant-privilege': ['reserve-currency', 'triffin-dilemma', 'de-dollarization', 'global-imbalances'],
 'foreign-exchange-reserves': ['fx-intervention', 'fixed-exchange-rate', 'sudden-stop', 'self-insurance'],
 'hot-money': ['sudden-stop', 'capital-flight', 'capital-control', 'carry-trade'],
 'capital-flight': ['capital-control', 'sudden-stop', 'hot-money', 'currency-crisis'],
 'capital-control': ['capital-flight', 'hot-money', 'impossible-trinity', 'capital-account'],
 'carry-trade': ['interest-rate-parity', 'hot-money', 'currency-crisis', 'leverage'],
 'cbdc': ['cryptocurrency', 'payment-system', 'monetary-policy', 'stablecoin'],
 'cryptocurrency': ['cbdc', 'crypto-bubble', 'defi', 'fiat-money'],
 'finance': ['financial-deepening', 'financial-repression', 'financial-inclusion', 'financial-innovation'],
 'financial-deepening': ['financial-repression', 'financial-inclusion', 'financialization', 'development-economics'],
 'financial-inclusion': ['microfinance', 'financial-deepening', 'informal-economy', 'poverty-trap'],
 'financial-innovation': ['securitization', 'financial-deepening', 'shadow-banking', 'cryptocurrency'],
 'microfinance': ['financial-inclusion', 'poverty-trap', 'development-economics', 'informal-economy'],
 'dutch-disease': ['resource-curse', 'commodity-price-index', 'angola-oil-dependence', 'deindustrialization'],
 'resource-curse': ['dutch-disease', 'commodity-price-index', 'nigeria-debt', 'rent-seeking'],
 'long-depression': ['panic-1873', 'deflation', 'kondratiev', 'great-depression'],
 'great-moderation': ['business-cycle', 'monetary-policy', 'inflation-targeting', 'subprime-crisis-2007'],
 'debt-trap-diplomacy': ['odious-debt', 'debt-crisis', 'sovereign-default', 'conditionality'],
 'global-debt': ['global-imbalances', 'government-debt', 'debt-crisis', 'debt-ceiling'],
 'global-imbalances': ['current-account', 'global-debt', 'reserve-currency', 'exorbitant-privilege'],
 'country-risk': ['sovereign-default', 'credit-rating', 'capital-flight', 'hot-money'],
 'market-risk': ['interest-rate-risk', 'liquidity-risk', 'credit-risk', 'var'],
 'basis': ['basis-point'],
}

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
miss, n = set(), 0
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
print('缺失（' + str(len(miss)) + '）:', sorted(miss))
