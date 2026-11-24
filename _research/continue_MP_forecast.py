# -*- coding: utf-8 -*-
"""round 129c：检查预测性语言与投资建议（项目铁律：不作预测、不给投资建议）。"""
import glob
import json
import re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]

# 预测性短语（谨慎：很多是"预期"作为经济学概念名，需人工判断）
PATS = ['将会发生', '预计未来', '可能会在', '下一轮', '未来将', '即将到来',
        '将会引发', '大概率', '建议买入', '建议卖出', '值得投资', '推荐投资',
        '可以预测', '将会出现', '势必']
hits = []
for e in es:
    for fld in ('overview', 'comparison', 'one_line'):
        t = e.get(fld) or ''
        for p in PATS:
            if p in t:
                i = t.find(p)
                hits.append((e['id'], fld, p, t[max(0, i - 25):i + 25].replace('\n', ' ')))
print('=== 预测性/投资建议短语命中 ===')
print('条数:', len(hits))
for h in hits[:30]:
    print('  %-24s %-11s 「%s」 … %s' % (h[0], h[1], h[2], h[3]))

# 单来源条目统计
print('\n=== 单来源条目（needs_verification 应为 True）===')
single = [e for e in es if len(e.get('sources') or []) == 1]
print('单来源条目数:', len(single))
badflag = [e['id'] for e in single if not e.get('needs_verification')]
print('其中 needs_verification != True 的:', len(badflag), badflag[:10])
