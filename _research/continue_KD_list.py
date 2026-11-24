# -*- coding: utf-8 -*-
import glob
import json
import re


def enr(s):
    zh = len(re.findall(r'[\u4e00-\u9fff]', s or ''))
    en = len(re.findall(r'[A-Za-z]', s or ''))
    return en / (zh + en) if (zh + en) else 0


es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
bad = sorted([e for e in es if enr(e.get('overview')) > 0.45], key=lambda x: -enr(x.get('overview')))
print('待修: %d\n' % len(bad))
for e in bad:
    print('=== %s | %s | %.0f%%' % (e['id'], e['title'], enr(e['overview']) * 100))
    print(re.sub(r'^（据 Wikipedia「[^」]*」摘要归纳）', '', e['overview'])[:340])
    print()
