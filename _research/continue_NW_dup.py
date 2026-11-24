# -*- coding: utf-8 -*-
"""round 140c：找 overview 高度相似的条目对（防复制粘贴/重复内容）。"""
import glob, json
from itertools import combinations

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
# 用字符 3-gram 的 Jaccard 近似
def shingles(s, k=6):
    s = ''.join(ch for ch in s if not ch.isspace())
    return set(s[i:i+k] for i in range(len(s)-k+1))

data = [(e['id'], shingles((e.get('overview') or '')), len(e.get('overview') or '')) for e in es]
data = [d for d in data if d[2] >= 80]
pairs = []
for (i1, s1, n1), (i2, s2, n2) in combinations(data, 2):
    if not s1 or not s2:
        continue
    inter = len(s1 & s2); uni = len(s1 | s2)
    if uni and inter / uni >= 0.55:
        pairs.append((round(inter/uni, 2), i1, i2, n1, n2))
pairs.sort(reverse=True)
print('overview 相似度>=0.55 的条目对:', len(pairs))
for p in pairs[:20]:
    print('  jaccard=%.2f  %-26s ~ %-26s (%d/%d字)' % p)
