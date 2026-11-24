# -*- coding: utf-8 -*-
"""抽样验证 sources.json 中 verified=true 的来源可达性。

用途：定期确认"标注已验证"的来源没有批量失效。
说明：403/405/429（反爬、方法不允许、限流）视为可达；
      503/超时多属服务端瞬时问题，可重试；404 需人工确认是否路径变更。

用法：python -X utf8 tools/check_sources.py [样本数]
退出码：0 = 抽样全部可达；1 = 存在需关注的失败
"""
import json
import os
import random
import ssl
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CTX = ssl._create_unverified_context()
HDR = {'User-Agent': 'EconCrisisBot/1.0 (link check)'}
SOFT = (403, 405, 429)      # 视为可达
RETRY = (500, 502, 503, 504)  # 重试一次


def probe(url):
    for attempt in (1, 2):
        try:
            r = urllib.request.urlopen(urllib.request.Request(url, headers=HDR), timeout=15, context=CTX)
            return 'OK', r.status
        except urllib.error.HTTPError as e:
            if e.code in SOFT:
                return 'OK', e.code
            if e.code in RETRY and attempt == 1:
                time.sleep(2); continue
            return 'FAIL', e.code
        except Exception as e:
            if attempt == 1:
                time.sleep(2); continue
            return 'FAIL', type(e).__name__
    return 'FAIL', 'retries exhausted'


def main():
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 30
    src = json.load(open(os.path.join(ROOT, 'data', 'sources.json'), encoding='utf-8'))['sources']
    pool = [s for s in src if s.get('verified') and s.get('url', '').startswith('http')]
    random.seed(60)
    sample = random.sample(pool, min(n, len(pool)))
    ok, fail = 0, []
    for s in sample:
        st, code = probe(s['url'])
        if st == 'OK':
            ok += 1
        else:
            fail.append((s['id'], code, s['url'][:74]))
    print('抽样 %d 个来源 | 可达 %d | 失败 %d' % (len(sample), ok, len(fail)))
    for f in fail:
        print('  %-42s %-16s %s' % (f[0][:42], str(f[1]), f[2]))
    if fail:
        print('\n结果：存在需关注的失败')
        return 1
    print('\n结果：抽样全部可达')
    return 0


if __name__ == '__main__':
    sys.exit(main())
