# -*- coding: utf-8 -*-
"""续作EZ：从维基全文中提取政策相关章节，生成候选供人工核验。"""
import glob
import json
import os
import re

OUT = '_research/policy_candidates.json'
POL_HEAD = re.compile(
    r'(policy\s*response|response|rescue|bailout|bail-out|aftermath|measures|'
    r'intervention|reform|resolution|recovery|stabilisation|stabilization)', re.I)

results = {}
for f in sorted(glob.glob('_research/wiki_full/*.txt')):
    eid = os.path.basename(f)[:-4]
    txt = open(f, encoding='utf-8').read()
    # 按 == Heading == 切段
    parts = re.split(r'\n==+\s*(.+?)\s*==+\n', txt)
    # parts[0] 是导言，之后成对出现 (heading, body)
    sections = [('(intro)', parts[0])]
    for i in range(1, len(parts) - 1, 2):
        sections.append((parts[i], parts[i + 1]))

    picks = []
    for head, body in sections:
        if head != '(intro)' and POL_HEAD.search(head):
            para = ' '.join(body.split())
            if len(para) > 80:
                picks.append((head, para[:800]))
    # 导言中也找政策句
    if not picks:
        intro = ' '.join(sections[0][1].split())
        sents = re.split(r'(?<=[.!?])\s+', intro)
        KEY = ['rescued', 'bailout', 'bail-out', 'interven', 'guarantee', 'nationali',
               'recapitali', 'central bank provided', 'government responded', 'policy response']
        hits = [s for s in sents if any(k in s.lower() for k in KEY) and len(s) > 60]
        if hits:
            picks.append(('(intro sentences)', ' '.join(hits[:2])[:800]))
    if picks:
        results[eid] = picks[:2]

json.dump(results, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('有政策候选的案例:', len(results), '/ 20')
for eid, p in results.items():
    print('=== %s ===' % eid)
    for head, body in p:
        print('  [%s] %s' % (head, body[:220]))
