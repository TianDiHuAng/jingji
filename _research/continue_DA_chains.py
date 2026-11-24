# -*- coding: utf-8 -*-
"""续作DA：为19世纪美国恐慌序列与北欧/拉美危机组建立真正的链式关联。"""
import json, glob

# 恐慌序列：链接前一个、后一个，以及相关的制度条目
CHAIN = {
 'panic-1792': ['panic-1796', 'panic-1819', 'first-bank', 'speculative-bubble'],
 'panic-1796': ['panic-1792', 'panic-1819', 'amsterdam-crisis-1763'],
 'panic-1819': ['panic-1796', 'panic-1825', 'second-bank', 'deflation'],
 'panic-1825': ['panic-1819', 'panic-1837', 'speculative-bubble', 'baring-crisis-1890'],
 'panic-1837': ['panic-1825', 'panic-1847', 'free-banking', 'second-bank'],
 'panic-1847': ['panic-1837', 'panic-1857', 'railway-mania', 'panic-1866'],
 'panic-1857': ['panic-1847', 'panic-1866', 'free-banking', 'globalization'],
 'panic-1866': ['panic-1857', 'panic-1873', 'bill-of-exchange', 'overend-gurney'],
 'panic-1873': ['panic-1866', 'panic-1884', 'long-depression', 'national-banking-act'],
 'panic-1884': ['panic-1873', 'panic-1893', 'national-banking-act'],
 'panic-1893': ['panic-1884', 'panic-1896', 'sherman-silver-purchase', 'national-banking-act'],
 'panic-1896': ['panic-1893', 'panic-1901', 'bimetallism', 'sherman-silver-purchase'],
 'panic-1901': ['panic-1896', 'panic-1907', 'speculative-bubble'],
 'panic-1907': ['panic-1901', 'panic-1910', 'lender-of-last-resort', 'federal-reserve-act'],
 'panic-1910': ['panic-1907', 'crisis-1914', 'shanghai-rubber-1910'],
}

GROUPS = {
 # 北欧银行危机群
 'finnish-banking-1990': ['swedish-crisis-1990s', 'norwegian-banking-1988', 'japan-asset-bubble-1990', 'bailout'],
 'swedish-crisis-1990s': ['finnish-banking-1990', 'norwegian-banking-1988', 'japan-asset-bubble-1990', 'bail-in'],
 'norwegian-banking-1988': ['finnish-banking-1990', 'swedish-crisis-1990s', 'oil-crisis-1979'],
 # 拉美债务群
 'latin-american-debt-1975': ['chilean-crisis-1982', 'mexican-peso-1994', 'argentina-crisis-2001', 'debt-crisis'],
 'chilean-crisis-1982': ['latin-american-debt-1975', 'mexican-peso-1994', 'sudden-stop', 'original-sin'],
 'mexican-peso-1994': ['latin-american-debt-1975', 'chilean-crisis-1982', 'asian-financial-crisis-1997', 'sudden-stop'],
 'argentina-crisis-2001': ['mexican-peso-1994', 'uruguay-2002', 'argentina-2018', 'sovereign-default'],
 'uruguay-2002': ['argentina-crisis-2001', 'south-america-2002', 'contagion'],
 # 亚洲危机群
 'asian-financial-crisis-1997': ['mexican-peso-1994', 'russian-1998', 'ltcm', 'sudden-stop', 'original-sin'],
 'indian-1991': ['asian-financial-crisis-1997', 'sri-lanka-crisis-2019', 'stabilization-program'],
 'showa-crisis-1927': ['great-depression', 'japan-asset-bubble-1990', 'bank-run'],
 # 恶性通胀群
 'weimar-hyper-1921': ['hungarian-hyper-1945', 'soviet-hyper-1917', 'greek-hyper-1941', 'hyperinflation', 'redenomination'],
 'hungarian-hyper-1945': ['weimar-hyper-1921', 'yugoslav-hyper-1992', 'hyperinflation', 'redenomination'],
 'yugoslav-hyper-1992': ['hungarian-hyper-1945', 'zimbabwe-hyper-2007', 'hyperinflation', 'redenomination'],
 'zimbabwe-hyper-2007': ['yugoslav-hyper-1992', 'venezuela-hyper-2016', 'hyperinflation', 'dollarization'],
 'venezuela-hyper-2016': ['zimbabwe-hyper-2007', 'brazil-hyper-1980', 'hyperinflation', 'redenomination'],
 'brazil-hyper-1980': ['venezuela-hyper-2016', 'argentina-crisis-2001', 'indexation', 'redenomination'],
 'soviet-hyper-1917': ['weimar-hyper-1921', 'chinese-hyper-1937', 'scissors-crisis-1923'],
 # 2008 序列
 'bear-stearns': ['lehman', 'subprime-crisis-2007', 'northern-rock', 'too-big-to-fail'],
 'lehman': ['bear-stearns', 'aig', 'merrill-lynch', 'washington-mutual', 'too-big-to-fail'],
 'aig': ['lehman', 'subprime-crisis-2007', 'too-big-to-fail', 'credit-default-swap'],
 'northern-rock': ['lehman', 'uk-ldi-crisis-2022', 'bank-run', 'deposit-insurance'],
 # 2023 序列
 'silicon-valley-bank': ['signature-bank', 'first-republic', 'credit-suisse-2023', 'bank-crisis-2023', 'interest-rate-risk'],
 'signature-bank': ['silicon-valley-bank', 'first-republic', 'bank-crisis-2023'],
 'first-republic': ['silicon-valley-bank', 'signature-bank', 'bank-crisis-2023'],
 'credit-suisse-2023': ['silicon-valley-bank', 'archegos-2021', 'bank-crisis-2023', 'too-big-to-fail'],
}

es = {json.load(open(f, encoding='utf-8'))['id']: f for f in glob.glob('data/entries/*.json')}
miss = set()
n = 0
for mapping in (CHAIN, GROUPS):
    for eid, rels in mapping.items():
        if eid not in es:
            miss.add(eid); continue
        valid = [r for r in rels if r in es and r != eid]
        miss |= {r for r in rels if r not in es}
        if not valid: continue
        f = es[eid]
        d = json.load(open(f, encoding='utf-8'))
        d['related'] = sorted(set(valid))
        d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DA】related已按危机序列/同组语义重建。')
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        n += 1
print('重建 related 条目:', n)
print('不存在的目标 id:', sorted(miss))
