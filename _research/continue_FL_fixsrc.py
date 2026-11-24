# -*- coding: utf-8 -*-
"""续作FL：为8个来源不足的条目补充专属史实来源。"""
import json
import ssl
import time
import urllib.parse
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0'}

# 条目 id -> [(slug, 说明)]
ADD = {
 'us-state-defaults-1840s': [('Panic_of_1837', '1837年恐慌与州债违约的背景')],
 'danish-bankruptcy-1813': [('Danish_state_bankruptcy_of_1813', '丹麦1813年国家破产（专属条目）')],
 'dutch-collapse-1780': [('Fourth_Anglo-Dutch_War', '第四次英荷战争'),
                         ('Dutch_East_India_Company', '荷兰东印度公司')],
 'british-credit-1772': [('Crisis_of_1772', '1772—1773年英国信用危机（专属条目）')],
 'panic-1896': [('Panic_of_1896', '1896年恐慌（专属条目）')],
 'yemen-currency-divergence': [('Economy_of_Yemen', '也门经济'),
                               ('Yemeni_Civil_War_(2014–present)', '也门内战（2014—）')],
 'panic-1910': [('Shanghai_rubber_stock_market_crisis', '上海橡皮股票风潮（专属条目）')],
 'subprime-crisis-2007': [('Subprime_mortgage_crisis', '次贷危机（专属条目）')],
}

src = json.load(open('data/sources.json', encoding='utf-8'))
have = {x['id']: x for x in src['sources']}
added_src, linked = 0, 0

for eid, items in ADD.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    for slug, note in items:
        sid = 'w-en-' + slug.lower().replace('_', '-').replace('–', '-')
        sid = sid.replace('(', '').replace(')', '').replace('—', '-')
        if sid not in have:
            url = 'https://en.wikipedia.org/api/rest_v1/page/summary/' + urllib.parse.quote(slug, safe='')
            try:
                r = json.loads(urllib.request.urlopen(
                    urllib.request.Request(url, headers=HDR), timeout=15, context=CTX).read())
                if not r.get('extract'):
                    print('  跳过(无摘要)', slug); continue
                rec = {
                    'id': sid, 'title': r.get('title') or slug,
                    'author': 'Wikipedia contributors', 'year': '2026', 'type': '权威百科',
                    'url': (r.get('content_urls', {}).get('desktop', {}) or {}).get('page')
                           or ('https://en.wikipedia.org/wiki/' + slug),
                    'url2': None, 'verified': True,
                    'note': 'REST summary API 核对：页面存在并返回摘要（%d 字符）。%s'
                            % (len(r['extract']), note),
                }
                src['sources'].append(rec)
                have[sid] = rec
                added_src += 1
                print('  + 新来源', sid, '=', rec['title'][:40])
                time.sleep(0.3)
            except Exception as e:
                print('  失败', slug, type(e).__name__); continue
        if sid not in d['sources']:
            d['sources'].append(sid)
            linked += 1
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作FL】已补充专属史实来源（此前仅有通用概念页）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

src['count'] = len(src['sources'])
json.dump(src, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print()
print('新增来源 %d 个 | 条目-来源关联 %d 条 | 来源总数 %d' % (added_src, linked, src['count']))
