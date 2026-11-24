# -*- coding: utf-8 -*-
"""续作FO：从维基全文中提取带单位的数字候选，供人工筛选为 key_data。"""
import glob
import json
import os
import re

# 条目 -> 全文路径
es = {}
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    es[d['id']] = d

targets = [e for e in es.values() if not e['unit'].startswith('U6') and not e.get('key_data')]

# 数字模式：百分比、金额、人数、指数
PAT = re.compile(
    r'((?:US\$|\$|£|€|RMB|₴|₦|Z\$)?\s?\d[\d,.]*\s?'
    r'(?:billion|million|trillion|percent|%|points|tonnes|marks|tael|dollars|pounds|euros|'
    r'francs|roubles|rubles|lira|pengő|kwacha|rial|pula|units|people|banks|employees|'
    r'basis points))', re.I)

out = {}
for e in targets:
    p = '_research/wiki_full/%s.txt' % e['id']
    if not os.path.exists(p):
        continue
    t = open(p, encoding='utf-8').read()
    body = ' '.join(t.split())
    sents = re.split(r'(?<=[.!?])\s+', body)
    cands = []
    for s in sents:
        if len(s) < 50 or len(s) > 420:
            continue
        ms = PAT.findall(s)
        if not ms:
            continue
        # 至少含一个百分比或金额
        if not re.search(r'%|percent|billion|million|trillion', s, re.I):
            continue
        cands.append((ms[:2], s[:260]))
    if cands:
        out[e['id']] = cands[:5]

json.dump(out, open('_research/kd_candidates.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('有数字候选的条目:', len(out), '/', len(targets))
for eid in list(out)[:8]:
    print('===', eid, '===')
    for ms, s in out[eid][:2]:
        print('   ', ms, '|', s[:170])
