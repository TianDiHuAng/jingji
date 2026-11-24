# -*- coding: utf-8 -*-
"""round 131：列出 check_kd 未匹配的 key_data，附上下文供人工评估。"""
import glob
import json
import os
import re
import sys

sys.path.insert(0, 'tools')
from check_kd import classify, variants  # 复用判据

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
FULL = '_research/wiki_full'

unmatched = []
for e in es:
    p = os.path.join(FULL, e['id'] + '.txt')
    if not os.path.exists(p):
        continue
    txt = open(p, encoding='utf-8').read()
    for k in e.get('key_data') or []:
        r = classify(k, txt)
        if r is None:  # 未匹配
            unmatched.append((e['id'], k))

print('未匹配 key_data: %d\n' % len(unmatched))
for eid, k in unmatched:
    txt = open(os.path.join(FULL, eid + '.txt'), encoding='utf-8').read()
    # 展示 note 前 90 字 + value
    note = (k.get('note') or '')[:90].replace('\n', ' ')
    print('%-24s v=%-10s unit=%-6s' % (eid, k.get('value'), k.get('unit')))
    print('    label:', (k.get('label') or '')[:50])
    print('    note :', note)
    print()
