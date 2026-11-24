# -*- coding: utf-8 -*-
"""续作IU：实测 link_ok 为 None 的 34 个来源，回填可达性结果。"""
import json
import ssl
import time
import urllib.error
import urllib.request

CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'Mozilla/5.0 (compatible; EconCrisisBot/1.0)'}
SP = 'data/sources.json'
sj = json.load(open(SP, encoding='utf-8'))
none_lk = [s for s in sj['sources'] if s.get('link_ok') is None]
print('待测:', len(none_lk), flush=True)

ok, fail = 0, []
for s in none_lk:
    u = s['url']
    st = None
    for attempt in (1, 2):
        try:
            r = urllib.request.urlopen(urllib.request.Request(u, headers=HDR), timeout=15, context=CTX)
            st = ('ok', r.status)
            break
        except urllib.error.HTTPError as e:
            if e.code in (403, 405, 429):
                st = ('ok', e.code)
                break
            if attempt == 1:
                time.sleep(2); continue
            st = ('fail', e.code)
        except Exception as ex:
            if attempt == 1:
                time.sleep(2); continue
            st = ('fail', type(ex).__name__)
    if st and st[0] == 'ok':
        s['link_ok'] = True
        ok += 1
    else:
        s['link_ok'] = False
        fail.append((s['id'], st[1] if st else '?', u[:60]))
    time.sleep(0.2)

json.dump(sj, open(SP, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('可达 %d | 不可达 %d' % (ok, len(fail)), flush=True)
for f in fail:
    print('   ', f, flush=True)
