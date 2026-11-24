# -*- coding: utf-8 -*-
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
bad = [e for e in es if e['unit'].startswith('U6')
       and not (e.get('timeline') or []) and not (e.get('key_data') or [])]
print('U6 概念中既无 timeline 也无 key_data 的条目:', len(bad))
for e in sorted(bad, key=lambda x: len(x['overview'])):
    print('  %-32s %4d 字 | schools %d | %s'
          % (e['id'], len(e['overview']), len(e.get('schools') or []), e['title'][:24]))
print()
# 无 schools 的条目
nos = [e for e in es if not (e.get('schools') or [])]
print('全库无 schools 的条目:', len(nos))
for e in sorted(nos, key=lambda x: len(x['overview']))[:8]:
    print('  %-32s %4d 字 | %s' % (e['id'], len(e['overview']), e['title'][:26]))
