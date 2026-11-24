# -*- coding: utf-8 -*-
"""round 127 全面质量审计（不依赖网络）。"""
import glob
import json
from collections import Counter

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]

print('=== overview 长度分布 ===')
buckets = Counter()
for e in es:
    n = len(e.get('overview') or '')
    if n < 150: buckets['<150'] += 1
    elif n < 250: buckets['150-249'] += 1
    elif n < 400: buckets['250-399'] += 1
    elif n < 600: buckets['400-599'] += 1
    else: buckets['>=600'] += 1
for k in ['<150', '150-249', '250-399', '400-599', '>=600']:
    print('  %-8s %3d' % (k, buckets[k]))

print('\n=== comparison / related 覆盖 ===')
print('  有 comparison:', sum(1 for e in es if e.get('comparison')), '/', len(es))
print('  有 related:', sum(1 for e in es if e.get('related')), '/', len(es))
print('  related 平均:', round(sum(len(e.get('related') or []) for e in es) / len(es), 1))

print('\n=== schools 覆盖 ===')
print('  有 schools:', sum(1 for e in es if e.get('schools')), '/', len(es))
print('  schools 总数:', sum(len(e.get('schools') or []) for e in es))

print('\n=== timeline / key_data ===')
print('  有 timeline:', sum(1 for e in es if e.get('timeline')), '/', len(es))
print('  有 key_data:', sum(1 for e in es if e.get('key_data')), '/', len(es))
print('  案例(key_data 为 0 且 timeline 为 0):',
      sum(1 for e in es if not e['unit'].startswith('U6')
          and not e.get('key_data') and not e.get('timeline')))

print('\n=== 最薄的 10 条（overview 最短） ===')
for e in sorted(es, key=lambda x: len(x.get('overview') or ''))[:10]:
    print('  %-30s %3d 字 | %s' % (e['id'], len(e['overview']), e['title'][:20]))

print('\n=== 案例中 timeline 为空但 tier 重要/核心 ===')
bad = [e for e in es if not e['unit'].startswith('U6') and e.get('tier') in ('核心', '重要')
       and not e.get('timeline')]
print('  条数:', len(bad))
for e in bad[:10]:
    print('   ', e['id'], '|', e['title'][:24])
