# -*- coding: utf-8 -*-
"""续作HS：为 10 个概念条目补中文维基第二来源（排除不完全等价的 2 项）。"""
import glob
import json

ZH = {
 'actuarial': ('精算師', 'https://zh.wikipedia.org/wiki/%E7%B2%BE%E7%AE%97%E5%B8%AB'),
 'bullion': ('貴金屬', 'https://zh.wikipedia.org/wiki/%E8%B2%B4%E9%87%91%E5%B1%AC'),
 'deindustrialization': ('去工業化', 'https://zh.wikipedia.org/wiki/%E5%8E%BB%E5%B7%A5%E6%A5%AD%E5%8C%96'),
 'demand': ('需求曲線', 'https://zh.wikipedia.org/wiki/%E9%9C%80%E6%B1%82%E6%9B%B2%E7%B7%9A'),
 'dividend': ('股息', 'https://zh.wikipedia.org/wiki/%E8%82%A1%E6%81%AF'),
 'effective-demand': ('有效需求', 'https://zh.wikipedia.org/wiki/%E6%9C%89%E6%95%88%E9%9C%80%E6%B1%82'),
 'modigliani-miller': ('莫迪利安尼-米勒定理', 'https://zh.wikipedia.org/wiki/%E8%8E%AB%E8%BF%AA%E5%88%A9%E5%AE%89%E5%B0%BC-%E7%B1%B3%E5%8B%92%E5%AE%9A%E7%90%86'),
 'property-rights': ('財產權', 'https://zh.wikipedia.org/wiki/%E8%B2%A1%E7%94%A2%E6%AC%8A'),
 'specialization': ('分工', 'https://zh.wikipedia.org/wiki/%E5%88%86%E5%B7%A5'),
 'toxic-assets': ('有毒资产', 'https://zh.wikipedia.org/wiki/%E6%9C%89%E6%AF%92%E8%B5%84%E4%BA%A7'),
}

sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
have = {s['id'] for s in sj['sources']}
n_src = 0
for eid, (zh, url) in ZH.items():
    sid = 'w-zh-' + eid
    if sid not in have:
        sj['sources'].append({
            'id': sid, 'title': zh, 'author': '维基百科编者', 'year': '2026',
            'type': '权威百科', 'url': url, 'url2': None, 'verified': True, 'link_ok': True,
            'note': '中文维基百科 API 核对（跨语言对照来源）',
        })
        n_src += 1
sj['count'] = len(sj['sources'])
json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

n_ent = 0
for eid in ZH:
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    sid = 'w-zh-' + eid
    if sid in d['sources']:
        continue
    d['sources'].append(sid)
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作HS】补中文维基作为跨语言第二来源（同属维基体系，非独立机构互证）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n_ent += 1

print('注册来源 %d | 补入条目 %d' % (n_src, n_ent))
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
single = [e['id'] for e in es if len(e.get('sources', [])) == 1]
print('剩余单来源条目:', len(single))
print('  ', ', '.join(single))
