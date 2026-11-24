# -*- coding: utf-8 -*-
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
nos = [e for e in es if not (e.get('schools') or [])]
print('无 schools 的条目: %d\n' % len(nos))
for e in sorted(nos, key=lambda x: len(x['overview'])):
    print('=== %s | %s | %s | %d 字' % (e['id'], e['title'], e['unit'][:8], len(e['overview'])))
    print('    sources:', e['sources'])
    print('    ' + e['overview'][:180].replace('\n', ' '))
    print('    timeline %d | key_data %d | comparison %s'
          % (len(e.get('timeline') or []), len(e.get('key_data') or []),
             '有' if e.get('comparison') else '无'))
    print()
