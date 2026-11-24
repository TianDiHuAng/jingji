# -*- coding: utf-8 -*-
"""续作DC：按主题为更多条目组建立关联（加密/中国/中东/非洲/南亚/欧债/大泡沫史/公司丑闻）。"""
import json, glob

GROUPS = {
 # 加密与数字金融
 'crypto-bubble': ['defi', 'terra-luna-2022', 'bankruptcy-ftx', 'speculative-bubble', 'stablecoin'],
 'defi': ['crypto-bubble', 'terra-luna-2022', 'bankruptcy-ftx', 'shadow-banking'],
 'terra-luna-2022': ['crypto-bubble', 'bankruptcy-ftx', 'defi', 'bank-run'],
 'bankruptcy-ftx': ['crypto-bubble', 'terra-luna-2022', 'bernie-madoff', 'ponzi-scheme'],
 # 公司丑闻与欺诈
 'enron': ['worldcom', 'bernie-madoff', 'ponzi-scheme', 'credit-rating', 'shadow-banking'],
 'worldcom': ['enron', 'bernie-madoff', 'speculative-bubble'],
 'bernie-madoff': ['enron', 'worldcom', 'ponzi-scheme', 'bankruptcy-ftx'],
 'ponzi-scheme': ['bernie-madoff', 'albania-pyramid-1997', 'bankruptcy-ftx'],
 # 中国
 'china-2015-turbulence': ['china-liquidity-2013', 'china-realestate-2020', 'chinese-stock-bubble-2007', 'capital-flight'],
 'china-liquidity-2013': ['china-2015-turbulence', 'china-realestate-2020', 'shadow-banking'],
 'china-realestate-2020': ['china-2015-turbulence', 'hainan-property-bubble-1992', 'housing-bubble', 'local-government-debt'],
 'chinese-stock-bubble-2007': ['china-2015-turbulence', 'china-realestate-2020', 'speculative-bubble'],
 'hainan-property-bubble-1992': ['china-realestate-2020', 'housing-bubble', 'taiwan-bubble'],
 'henan-2022': ['china-liquidity-2013', 'deposit-insurance', 'bank-run'],
 # 中东
 'dubai-debt-2009': ['egypt-2023', 'lebanese-liquidity-2019', 'sovereign-wealth-fund'],
 'egypt-2023': ['dubai-debt-2009', 'lebanese-liquidity-2019', 'sri-lanka-crisis-2019', 'stabilization-program'],
 'lebanese-liquidity-2019': ['syrian-pound-crisis', 'egypt-2023', 'bank-run', 'currency-crisis'],
 'syrian-crisis-2011': ['syrian-pound-crisis', 'yemen-currency-divergence', 'lebanese-liquidity-2019'],
 'syrian-pound-crisis': ['yemen-currency-divergence', 'lebanese-liquidity-2019', 'syrian-crisis-2011', 'currency-crisis'],
 'turkey-2001': ['turkish-crisis-2018', 'argentina-2018', 'original-sin', 'stabilization-program'],
 'turkish-crisis-2018': ['turkey-2001', 'argentina-2018', 'original-sin', 'currency-crisis'],
 'yemen-currency-divergence': ['syrian-pound-crisis', 'lebanese-liquidity-2019', 'dollarization', 'black-market'],
 'iranian-economic-crisis': ['venezuela-hyper-2016', 'turkish-crisis-2018', 'stabilization-program'],
 # 非洲
 'angola-oil-dependence': ['angolan-kwanza-devaluation', 'nigeria-debt', 'dutch-disease', 'resource-curse'],
 'angolan-kwanza-devaluation': ['angola-oil-dependence', 'zambian-kwacha-reform', 'redenomination'],
 'ghana-banking-2017': ['nigeria-debt', 'zambian-kwacha-reform', 'bank-failure'],
 'nigeria-debt': ['angola-oil-dependence', 'southafrica-debt', 'ghana-banking-2017', 'dutch-disease'],
 'southafrica-debt': ['nigeria-debt', 'egypt-2023', 'sovereign-default'],
 'zambian-kwacha-reform': ['zimbabwe-hyper-2007', 'angolan-kwanza-devaluation', 'redenomination'],
 'zimbabwe-hyper-2007': ['zambian-kwacha-reform', 'venezuela-hyper-2016', 'hyperinflation'],
 'cameroon-crisis-1987': ['nigeria-debt', 'latin-american-debt-1975', 'debt-crisis'],
 # 南亚
 'sri-lanka-crisis-2019': ['pakistan-crisis-2021', 'egypt-2023', 'sovereign-default', 'stabilization-program'],
 'pakistan-crisis-2021': ['sri-lanka-crisis-2019', 'egypt-2023', 'stabilization-program'],
 'indian-1991': ['sri-lanka-crisis-2019', 'pakistan-crisis-2021', 'stabilization-program'],
 # 欧债危机
 'euro-area-crisis': ['greek-debt-crisis', 'irish-banking-2008', 'spain-2008', 'cypriot-2013', 'european-central-bank'],
 'greek-debt-crisis': ['euro-area-crisis', 'cypriot-2013', 'spain-2008', 'stabilization-program'],
 'irish-banking-2008': ['euro-area-crisis', 'spain-2008', 'icelandic-crisis-2008', 'bank-guarantee'],
 'spain-2008': ['euro-area-crisis', 'irish-banking-2008', 'housing-bubble'],
 'icelandic-crisis-2008': ['irish-banking-2008', 'cypriot-2013', 'euro-area-crisis'],
 'cypriot-2013': ['greek-debt-crisis', 'icelandic-crisis-2008', 'bail-in', 'deposit-insurance'],
 # 大泡沫史
 'tulip-mania': ['south-sea-bubble-1720', 'mississippi-bubble-1720', 'speculative-bubble'],
 'south-sea-bubble-1720': ['mississippi-bubble-1720', 'tulip-mania', 'speculative-bubble'],
 'mississippi-bubble-1720': ['south-sea-bubble-1720', 'tulip-mania', 'speculative-bubble', 'bimetallism'],
 'wall-street-1929': ['great-depression', 'black-monday-1987', 'speculative-bubble'],
 'black-monday-1987': ['wall-street-1929', 'dotcom-bubble-2000', 'circuit-breaker'],
 'dotcom-bubble-2000': ['black-monday-1987', 'subprime-crisis-2007', 'speculative-bubble', 'crypto-bubble'],
 'japan-asset-bubble-1990': ['taiwan-bubble', 'housing-bubble', 'balance-sheet-recession'],
 'taiwan-bubble': ['japan-asset-bubble-1990', 'hainan-property-bubble-1992', 'speculative-bubble'],
 # 巴西/拉美
 'brazil-2014': ['argentina-2018', 'venezuela-crisis-2013', 'commodity-price-cycle'],
 'argentina-2018': ['brazil-2014', 'turkey-2001', 'argentina-crisis-2001', 'currency-crisis'],
 'venezuela-crisis-2013': ['venezuela-hyper-2016', 'venezuela-energy-2010', 'hyperinflation'],
 'venezuela-hyper-2016': ['venezuela-crisis-2013', 'zimbabwe-hyper-2007', 'hyperinflation', 'redenomination'],
 'venezuela-energy-2010': ['venezuela-crisis-2013', 'oil-price-war-2020', 'resource-curse'],
 'venezuelan-banking-2009': ['venezuela-crisis-2013', 'bank-run', 'deposit-insurance'],
 # 俄罗斯
 'russian-crisis-2014': ['great-recession-russia', 'russian-1998', 'oil-crisis-1973'],
 'great-recession-russia': ['russian-crisis-2014', 'russian-1998', 'bank-crisis-2023'],
 'russian-1998': ['russian-crisis-2014', 'ltcm', 'sovereign-default'],
}

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
miss, n = set(), 0
for eid, rels in GROUPS.items():
    if eid not in es:
        miss.add(eid); continue
    valid = [r for r in rels if r in es and r != eid]
    miss |= {r for r in rels if r not in es}
    if not valid: continue
    f = es[eid]
    d = json.load(open(f, encoding='utf-8'))
    d['related'] = sorted(set(d.get('related', []) + valid))
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
print('设置 related 条目:', n)
print('缺失目标 id:', sorted(miss))
