# -*- coding: utf-8 -*-
"""续作EF：为无related的条目按主题建立关联。"""
import json, glob

G = {
 # 国际金融与汇率
 'purchasing-power-parity': ['interest-rate-parity', 'exchange-rate-regime', 'global-imbalances', 'inflation'],
 'reserve-currency': ['triffin-dilemma', 'exorbitant-privilege', 'de-dollarization', 'currency-internationalization'],
 'sdr': ['reserve-currency', 'imf', 'triffin-dilemma', 'special-drawing-rights'],
 'sterling-area': ['reserve-currency', 'bretton-woods', 'exchange-equalisation', 'gold-standard'],
 'triffin-dilemma': ['reserve-currency', 'bretton-woods', 'exorbitant-privilege', 'dollarization'],
 'world-bank': ['imf', 'development-economics', 'washington-consensus', 'structural-adjustment'],
 'wto': ['gatt', 'free-trade', 'protectionism', 'tariff'],
 'tariff': ['protectionism', 'free-trade', 'smoot-hawley-1930', 'beggar-thy-neighbour'],
 'protectionism': ['tariff', 'free-trade', 'beggar-thy-neighbour', 'smoot-hawley-1930'],
 'competitive-devaluation': ['currency-war', 'devaluation', 'beggar-thy-neighbour', 'gold-standard'],
 # 货币政策
 'quantitative-easing': ['quantitative-tightening', 'yield-curve-control', 'open-market-operation', 'money-creation'],
 'quantitative-tightening': ['quantitative-easing', 'open-market-operation', 'interest-rate', 'taper-tantrum'],
 'repo': ['interbank-lending', 'money-market', 'fire-sale', 'collateral'],
 'reserve-requirement': ['capital-requirement', 'money-multiplier', 'money-creation', 'basel-iii'],
 'taylor-rule': ['monetary-policy', 'time-inconsistency', 'inflation-targeting', 'output-gap'],
 'time-inconsistency': ['taylor-rule', 'central-bank-independence', 'inflation-targeting', 'moral-hazard'],
 'rational-expectations': ['adaptive-expectations', 'lucas-critique', 'new-classical', 'phillips-curve'],
 'real-business-cycle': ['new-classical', 'business-cycle', 'keynesian-economics', 'total-factor-productivity'],
 'says-law': ['keynesian-economics', 'classical-economics', 'aggregate-demand', 'effective-demand'],
 'ricardian-equivalence': ['fiscal-multiplier', 'fiscal-policy', 'government-debt', 'crowding-out'],
 'savings-glut': ['global-imbalances', 'current-account', 'secular-stagnation', 'reserve-currency'],
 'stagflation': ['phillips-curve', 'oil-crisis-1973', 'monetarism', 'aggregate-supply'],
 'sterilization': ['fx-intervention', 'impossible-trinity', 'foreign-exchange-reserves', 'money-supply'],
 'seigniorage': ['inflation', 'hyperinflation', 'fiat-money', 'fiscal-dominance'],
 'redenomination': ['hyperinflation', 'indexation', 'dollarization', 'fiat-money'],
 # 金融工具与结构
 'put-option': ['call-option', 'option', 'black-scholes', 'hedging'],
 'swap': ['derivative', 'otc', 'interest-rate-swap', 'counterparty-risk'],
 'spot-contract': ['futures', 'forward-contract', 'commodity-price-index', 'arbitrage'],
 'rwa': ['capital-requirement', 'basel-iii', 'leverage', 'regulatory-arbitrage'],
 'seniority': ['bail-in', 'debt-restructuring', 'haircut-finance', 'subordination'],
 'tranche': ['securitization', 'collateralized-debt-obligation', 'credit-enhancement', 'credit-rating'],
 'spv': ['securitization', 'off-balance-sheet', 'shadow-banking', 'credit-enhancement'],
 'securitization': ['collateralized-debt-obligation', 'mortgage-backed-security', 'subprime-lending', 'credit-rating'],
 'credit-enhancement': ['securitization', 'credit-rating', 'tranche', 'moral-hazard'],
 # 风险与监管
 'risk-management': ['value-at-risk', 'stress-test', 'risk-premium', 'capital-requirement'],
 'risk-premium': ['interest-rate', 'credit-risk', 'market-risk', 'liquidity'],
 'value-at-risk': ['stress-test', 'risk-management', 'volatility', 'market-risk'],
 'stress-test': ['value-at-risk', 'capital-requirement', 'basel-iii', 'risk-management'],
 'volatility': ['value-at-risk', 'market-risk', 'option', 'risk-management'],
 'systemic-risk': ['macroprudential', 'sifi', 'contagion', 'fire-sale'],
 'sifi': ['systemic-risk', 'too-big-to-fail', 'macroprudential', 'capital-requirement'],
 'prudential-regulation': ['macroprudential', 'capital-requirement', 'basel-iii', 'deposit-insurance'],
 'sarbanes-oxley': ['enron', 'worldcom', 'dodd-frank', 'disclosure'],
 'volcker-rule': ['dodd-frank', 'glass-steagall', 'proprietary-trading', 'too-big-to-fail'],
 'tarp': ['bailout', 'lehman', 'aig', 'subprime-crisis-2007'],
 # 危机史与制度
 'railway-mania': ['panic-1847', 'speculative-bubble', 'dotcom-bubble-2000', 'industrial-revolution'],
 'recession-1920-1921': ['great-depression', 'recession-1937-1938', 'business-cycle', 'deflation'],
 'second-bank': ['first-bank', 'free-banking', 'national-banking-act', 'panic-1819'],
 'sherman-silver-purchase': ['bimetallism', 'silver-standard', 'panic-1893', 'gold-standard'],
 'silver-standard': ['bimetallism', 'gold-standard', 'sherman-silver-purchase', 'panic-1896'],
 'smithsonian-agreement': ['nixon-shock', 'bretton-woods', 'jamaica-accords', 'exchange-rate-regime'],
 'tripartite-1936': ['gold-bloc', 'exchange-equalisation', 'gold-standard', 'london-econ-1933'],
 'roman-currency': ['debasement', 'commodity-money', 'crisis-third-century', 'inflation'],
 'riksbank': ['bank-of-england', 'central-bank', 'history-of-banking', 'fiat-money'],
 'structural-adjustment': ['conditionality', 'imf', 'washington-consensus', 'austerity'],
 'stabilization-program': ['conditionality', 'imf', 'austerity', 'fiscal-multiplier'],
 'washington-consensus': ['structural-adjustment', 'conditionality', 'development-economics', 'imf'],
 'transition-economy': ['structural-adjustment', 'ebrd', 'albania-pyramid-1997', 'russian-1998'],
 # 概念
 'public-choice': ['rent-seeking', 'political-economy', 'externalities', 'welfare-economics'],
 'public-good': ['externality', 'tragedy-commons', 'market-failure', 'deposit-insurance'],
 'tragedy-commons': ['public-good', 'externality', 'moral-hazard', 'rent-seeking'],
 'welfare-economics': ['public-choice', 'externality', 'public-good', 'utility'],
 'usury': ['interest-rate', 'microfinance', 'financial-repression', 'credit-rationing'],
 'unemployment': ['nairu', 'natural-rate-unemployment', 'okuns-law', 'phillips-curve'],
 'total-factor-productivity': ['solow-model', 'development-economics', 'growth', 'industrial-revolution'],
 'solow-model': ['total-factor-productivity', 'development-economics', 'growth', 'convergence'],
 'self-fulfilling': ['coordination-games', 'bank-run', 'diamond-dybvig', 'contagion'],
 'speculation': ['arbitrage', 'speculative-bubble', 'hedging', 'carry-trade'],
 'speculative-attack': ['currency-crisis', 'fixed-exchange-rate', 'self-fulfilling', 'capital-flight'],
 'speculative-bubble': ['herd-behavior', 'credit-cycle', 'minsky-moment', 'tulip-mania-1637'],
 'short-selling': ['market-manipulation', 'speculation', 'hedge-fund', 'liquidity'],
 'supply-side': ['fiscal-policy', 'aggregate-supply', 'stagflation', 'laffer-curve'],
 'wage-price-spiral': ['indexation', 'inflation', 'phillips-curve', 'expectations'],
 'velocity-of-money': ['money-supply', 'quantity-theory-money', 'secular-stagnation', 'liquidity-trap'],
 'token-money': ['representative-money', 'fiat-money', 'commodity-money', 'history-of-money'],
 'representative-money': ['token-money', 'commodity-money', 'gold-standard', 'fiat-money'],
 'stablecoin': ['cryptocurrency', 'cbdc', 'money-creation', 'bank-run'],
 'shadow-banking': ['financial-disintermediation', 'repo', 'securitization', 'macroprudential'],
 'subprime-lending': ['securitization', 'collateralized-debt-obligation', 'credit-rating', 'mortgage-backed-security'],
 'sudden-stop': ['capital-flight', 'currency-crisis', 'original-sin', 'current-account'],
 'stock': ['bond', 'stock-market-crash', 'equity-premium', 'dividend'],
 'stock-exchange': ['stock', 'stock-market-crash', 'market-maker', 'liquidity'],
 'stock-market-crash': ['stock', 'speculative-bubble', 'circuit-breaker', 'black-monday-1987'],
 'sticky-prices': ['new-keynesian', 'menu-cost', 'monetary-transmission', 'phillips-curve'],
 'yield-curve': ['interest-rate', 'yield-curve-control', 'recession', 'term-premium'],
 'yield-curve-control': ['yield-curve', 'quantitative-easing', 'central-bank', 'exchange-rate-regime'],
 'twin-crises': ['currency-crisis', 'bank-crisis-2023', 'sudden-stop', 'original-sin'],
 'twin-deficits': ['current-account', 'budget-balance', 'fiscal-policy', 'global-imbalances'],
 'tobin-tax': ['capital-control', 'hot-money', 'capital-flight', 'speculation'],
 'quantity-theory-money': ['money-supply', 'velocity-of-money', 'fisher-equation', 'monetarism'],
}

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
n, miss, skipped = 0, set(), []
for eid, rels in G.items():
    if eid not in es:
        miss.add('SELF:' + eid); continue
    valid = [r for r in rels if r in es and r != eid]
    miss |= {r for r in rels if r not in es}
    if not valid:
        skipped.append(eid + '(无有效目标)'); continue
    f = es[eid]
    d = json.load(open(f, encoding='utf-8'))
    d['related'] = sorted(set(d.get('related', []) + valid))
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
print('设置 related:', n)
es2 = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
print('有related:', sum(1 for e in es2 if e.get('related')), '/', len(es2))
print('缺失目标:', sorted(miss))
