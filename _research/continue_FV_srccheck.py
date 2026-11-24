# -*- coding: utf-8 -*-
"""续作FV：抽样验证 sources.json 中 verified=true 的来源是否真可达。"""
import json
import random
import ssl
import urllib.error
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0 (link check)'}

src = json.load(open('data/sources.json', encoding='utf-8'))['sources']
pool = [s for s in src if s.get('verified') and s.get('url', '').startswith('http')]
random.seed(60)
sample = random.sample(pool, min(30, len(pool)))

ok, fail = 0, []
for s in sample:
    url = s['url']
    try:
        req = urllib.request.Request(url, headers=HDR, method='HEAD')
        r = urllib.request.urlopen(req, timeout=12, context=CTX)
        ok += 1
    except urllib.error.HTTPError as e:
        if e.code in (403, 405, 429):      # 反爬或方法不允许，不代表不存在
            ok += 1
        else:
            fail.append((s['id'], e.code, url[:70]))
    except Exception as e:
        fail.append((s['id'], type(e).__name__, url[:70]))

print('抽样 %d 个来源 | 可达 %d | 失败 %d' % (len(sample), ok, len(fail)))
for f in fail:
    print('  %-42s %-14s %s' % (f[0][:42], str(f[1]), f[2]))
