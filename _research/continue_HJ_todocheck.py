# -*- coding: utf-8 -*-
"""续作HJ：用模糊匹配校验 BACKLOG 待建概念清单的真实缺口。

起因：round 77 依据过时清单建了 externalities／var，而站内已有 externality／value-at-risk。
判据：不只比对 id，还比对标题与 id 的词元重合，避免"同义不同名"被误判为缺失。
"""
import glob
import json
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
ids = {e['id'] for e in es}
titles = {e['id']: e['title'] for e in es}

TODO = {
 'bank-resolution': '银行处置',
 'sacrifice-ratio': '牺牲率',
 'disclosure': '信息披露',
 'agriculture': '农业',
 'tax-capacity': '税收能力',
 'short-term-rate': '短期利率',
 'secured-lending': '担保贷款',
 'self-insurance': '自我保险',
 'risk-pooling': '风险汇聚',
 'actuarial': '精算',
 'leading-indicator': '领先指标',
 'deindustrialization': '去工业化',
 'supervision': '监管',
 'rogue-trader': '流氓交易员',
 'audit-failure': '审计失败',
 'bank-holiday': '银行假日',
 'bullion': '金银块',
 'lloyds': '劳合社',
 'term-premium': '期限溢价',
 'regulatory-arbitrage': '监管套利',
 'taper-tantrum': '缩减恐慌',
}


def toks(s):
    return {t for t in re.split(r'[^a-z0-9]+', s.lower()) if len(t) > 2}


print('%-26s %-8s %s' % ('待建概念', '状态', '匹配到的现有条目'))
print('-' * 78)
real_gap = []
for eid, zh in TODO.items():
    if eid in ids:
        print('%-26s %-8s 已存在（同名）' % (eid, '✓'))
        continue
    # 词元匹配
    tt = toks(eid)
    cands = []
    for i in ids:
        it = toks(i)
        if tt & it and len(tt & it) >= max(1, len(tt) // 2):
            cands.append(i)
    # 标题匹配
    for i, t in titles.items():
        if zh and zh in t:
            cands.append(i)
    cands = sorted(set(cands))
    if cands:
        print('%-26s %-8s %s' % (eid, '⚠ 已有', ', '.join(cands[:4])))
    else:
        print('%-26s %-8s —' % (eid, '缺口'))
        real_gap.append((eid, zh))

print('\n真实缺口: %d 个' % len(real_gap))
for g in real_gap:
    print('  %-26s %s' % g)
