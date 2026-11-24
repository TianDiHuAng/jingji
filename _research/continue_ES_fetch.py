# -*- coding: utf-8 -*-
"""续作ES：维基恢复后，批量抓取 BACKLOG 中缺失概念的摘要。"""
import json
import os
import ssl
import time
import urllib.parse
import urllib.request

OUT = '_research/wiki_batch'
os.makedirs(OUT, exist_ok=True)
CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0 (econ-history research; contact: local)'}

# 待抓取：条目 id -> 维基 slug
TARGETS = {
    'growth': 'Economic_growth',
    'expectations': 'Expectation_(finance)',
    'utility': 'Utility',
    'recession': 'Recession',
    'market-failure': 'Market_failure',
    'rent-seeking': 'Rent-seeking',
    'externality': 'Externality',
    'disclosure': 'Disclosure_(finance)',
    'dividend': 'Dividend',
    'equity-premium': 'Equity_premium_puzzle',
    'term-premium': 'Term_premium',
    'convergence': 'Convergence_(economics)',
    'counterparty-risk': 'Counterparty_risk',
    'effective-demand': 'Effective_demand',
    'proprietary-trading': 'Proprietary_trading',
    'regulatory-arbitrage': 'Regulatory_arbitrage',
    'subordination': 'Subordination_(finance)',
    'taper-tantrum': 'Taper_tantrum',
    'bank-resolution': 'Bank_resolution',
    'leverage-ratio': 'Leverage_ratio',
    'ring-fencing': 'Ring_fencing',
    'inflation-tax': 'Inflation_tax',
    'modigliani-miller': 'Modigliani–Miller_theorem',
    'fractional-reserve': 'Fractional-reserve_banking',
    'eurodollar': 'Eurodollar',
    'mutual-fund': 'Mutual_fund',
    'nasdaq': 'Nasdaq',
    'originate-to-distribute': 'Originate-to-distribute',
    'de-risking': 'De-risking',
}

ok, fail = [], []
for eid, slug in TARGETS.items():
    path = os.path.join(OUT, eid + '.json')
    if os.path.exists(path):
        ok.append((eid, 'cached'))
        continue
    url = 'https://en.wikipedia.org/api/rest_v1/page/summary/' + urllib.parse.quote(slug)
    try:
        raw = urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=15, context=CTX).read()
        d = json.loads(raw)
        if not d.get('extract'):
            fail.append((eid, 'no extract'))
            continue
        json.dump({'id': eid, 'slug': slug, 'title': d.get('title', ''),
                   'extract': d.get('extract', ''),
                   'url': (d.get('content_urls', {}).get('desktop', {}) or {}).get('page', '')},
                  open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        ok.append((eid, len(d.get('extract', ''))))
        time.sleep(0.4)
    except Exception as e:
        fail.append((eid, type(e).__name__))

print('成功 %d 个：' % len(ok))
for x in ok:
    print('  ', x)
print('失败 %d 个：' % len(fail))
for x in fail:
    print('  ', x)
