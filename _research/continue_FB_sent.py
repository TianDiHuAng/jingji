# -*- coding: utf-8 -*-
"""续作FB：从维基全文中提取含政策主体机构的句子，输出候选供核验。"""
import glob
import json
import os
import re

ACTORS = [
    'FDIC', 'Federal Reserve', 'the Fed', 'ECB', 'European Central Bank', 'Bank of England',
    'Treasury', 'IMF', 'World Bank', 'government', 'Government', 'regulator',
    'central bank', 'Bank of', 'ministry', 'Ministry', 'Congress', 'Parliament',
    'authorities', 'supervisor', 'Resolution', 'bailout', 'bail-out', 'bail out',
    'nationalized', 'nationalised', 'recapitalized', 'recapitalised', 'injected',
    'guarantee', 'guaranteed', 'emergency', 'rescued', 'rescue package', 'capital injection',
]
# 排除明显是纯描述/背景的句式（弱化噪声）
NOISE = ['is a', 'was a', 'refers to', 'may refer', 'can refer']

out = {}
for f in sorted(glob.glob('_research/wiki_full/*.txt')):
    eid = os.path.basename(f)[:-4]
    txt = open(f, encoding='utf-8').read()
    body = re.sub(r'\n==+.*?==+\n', '\n', txt)      # 去标题行
    body = ' '.join(body.split())
    sents = re.split(r'(?<=[.!?])\s+', body)
    hits = []
    for s in sents:
        if len(s) < 70 or len(s) > 480:
            continue
        low = s.lower()
        if any(n in low for n in NOISE) and len(s) < 140:
            continue
        if sum(1 for a in ACTORS if a in s) >= 1:
            hits.append(s)
    if hits:
        out[eid] = hits[:4]

json.dump(out, open('_research/policy_sentences.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=2)
print('有政策主体句的案例:', len(out), '/', len(glob.glob('_research/wiki_full/*.txt')))
print()
for eid in list(out)[:12]:
    print('===', eid, '===')
    for s in out[eid][:2]:
        print('   •', s[:210])
