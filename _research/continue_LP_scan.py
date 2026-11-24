# -*- coding: utf-8 -*-
import glob
import json
import os
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
short = [e for e in es if e.get('tier') in ('核心', '重要')
         and len(e.get('overview') or '') < 150 and not e['unit'].startswith('U6')]
print('待处理的案例: %d\n' % len(short))
for e in sorted(short, key=lambda x: len(x['overview'])):
    p = '_research/wiki_full/%s.txt' % e['id']
    n = len(open(p, encoding='utf-8').read()) if os.path.exists(p) else 0
    print('%-26s %3d 字 | 全文 %6d | %s | %s'
          % (e['id'], len(e['overview']), n,
             '有全文' if n else '**无全文**', e['title'][:22]))
