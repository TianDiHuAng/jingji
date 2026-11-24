# -*- coding: utf-8 -*-
import glob
import json

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
short = [(e['id'], len(e.get('overview') or ''), e['tier']) for e in es
         if e.get('tier') in ('核心', '重要') and len(e.get('overview') or '') < 150]
print('R22 实际条数: %d' % len(short))
print('按 tier:', {t: sum(1 for s in short if s[2] == t) for t in ('核心', '重要')})
print('\n最短 15 条:')
for s in sorted(short, key=lambda x: x[1])[:15]:
    print('  %-30s %3d 字 | %s' % (s[0], s[1], s[2]))
