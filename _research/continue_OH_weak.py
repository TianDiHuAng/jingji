# -*- coding: utf-8 -*-
"""round 147：列出 check_kd 的"弱匹配" key_data，供人工判断是否真错。"""
import glob, json, os, sys
sys.path.insert(0, 'tools')
from check_kd import classify

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
weak = []
for e in es:
    p = os.path.join('_research/wiki_full', e['id'] + '.txt')
    if not os.path.exists(p):
        continue
    txt = open(p, encoding='utf-8').read()
    for k in e.get('key_data') or []:
        if classify(k, txt) == 'weak':
            # 展示 note 里的原文引述，判断是否名副其实
            note = (k.get('note') or '')
            weak.append((e['id'], k.get('label','')[:30], k.get('value'), k.get('unit','')[:10], note[:70]))
print('弱匹配 key_data:', len(weak))
for w in weak:
    print('  %-24s %-30s v=%-8s %-10s | %s' % w)
