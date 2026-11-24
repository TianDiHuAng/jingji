# -*- coding: utf-8 -*-
import glob
import json
import re

es = {json.load(open(f, encoding='utf-8'))['id']: json.load(open(f, encoding='utf-8'))
      for f in glob.glob('data/entries/*.json')}
IDS = ['herd-behavior', 'bank-failure', 'collateralized-debt-obligation', 'new-classical',
       'adaptive-expectations', 'resource-curse', 'credit-default-swap',
       'quantitative-tightening', 'risk-premium', 'fear-of-floating',
       'information-asymmetry', 'central-bank-independence', 'global-imbalances',
       'federal-reserve', 'duration-finance']
for eid in IDS:
    d = es.get(eid)
    if not d:
        print('== %s 不存在' % eid)
        continue
    ov = re.sub(r'[；。]?\s*具体[^。]{0,24}待(核实|补充|查)[。]?\s*$', '', d.get('overview') or '').rstrip()
    print('=== %s | %s | %d 字' % (eid, d['title'], len(ov)))
    print(ov)
    print()
