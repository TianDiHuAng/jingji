# -*- coding: utf-8 -*-
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
nocmp = [e for e in es if not e.get('comparison')]
nosch = [e for e in es if not e.get('schools')]
print('缺 comparison: %d' % len(nocmp))
for e in sorted(nocmp, key=lambda x: len(x.get('overview') or ''))[:25]:
    print('  %-30s %4d 字 | %s | %s' % (e['id'], len(e.get('overview') or ''), e['tier'], e['title'][:20]))
print('\n缺 schools: %d' % len(nosch))
for e in nosch:
    print('  %-30s %4d 字 | %s | %s' % (e['id'], len(e.get('overview') or ''), e['tier'], e['title'][:22]))
