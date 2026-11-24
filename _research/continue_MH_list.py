# -*- coding: utf-8 -*-
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
nocmp = [e for e in es if not e.get('comparison')]
print('缺 comparison: %d\n' % len(nocmp))
for e in nocmp:
    print('=== %s | %s | %s' % (e['id'], e['tier'], e['title']))
    print('    one_line:', e.get('one_line'))
    print('    related:', e.get('related'))
