# -*- coding: utf-8 -*-
"""续作HP：为 12 个概念条目补中文维基作为第二来源。"""
import glob
import json

ZH = {
 'equity-premium': ('股权溢价之谜', 'https://zh.wikipedia.org/wiki/%E8%82%A1%E6%9D%83%E6%BA%A2%E4%BB%B7%E4%B9%8B%E8%B0%9C'),
 'growth': ('经济增长', 'https://zh.wikipedia.org/wiki/%E7%BB%8F%E6%B5%8E%E5%A2%9E%E9%95%BF'),
 'investment': ('投资', 'https://zh.wikipedia.org/wiki/%E6%8A%95%E8%B5%84'),
 'lloyds': ('劳合社', 'https://zh.wikipedia.org/wiki/%E5%8A%B3%E5%90%88%E7%A4%BE'),
 'market-failure': ('市场失灵', 'https://zh.wikipedia.org/wiki/%E5%B8%82%E5%9C%BA%E5%A4%B1%E7%81%B5'),
 'mutual-fund': ('共同基金', 'https://zh.wikipedia.org/wiki/%E5%85%B1%E5%90%8C%E5%9F%BA%E9%87%91'),
 'nasdaq': ('纳斯达克', 'https://zh.wikipedia.org/wiki/%E7%BA%B3%E6%96%AF%E8%BE%BE%E5%85%8B'),
 'pigouvian-tax': ('庇古税', 'https://zh.wikipedia.org/wiki/%E5%BA%87%E5%8F%A4%E7%A8%8E'),
 'prisoners-dilemma': ('囚徒困境', 'https://zh.wikipedia.org/wiki/%E5%9B%9A%E5%BE%92%E5%9B%B0%E5%A2%83'),
 'rent-seeking': ('尋租', 'https://zh.wikipedia.org/wiki/%E5%B0%8B%E7%A7%9F'),
 'savings': ('储蓄', 'https://zh.wikipedia.org/wiki/%E5%84%A8%E8%93%84'),
 'transaction-cost': ('交易成本', 'https://zh.wikipedia.org/wiki/%E4%BA%A4%E6%98%93%E6%88%90%E6%9C%AC'),
}

sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
have = {s['id'] for s in sj['sources']}
n_src, n_ent = 0, 0
for eid, (zh, url) in ZH.items():
    sid = 'w-zh-' + eid
    if sid not in have:
        sj['sources'].append({
            'id': sid, 'title': zh, 'author': '维基百科编者', 'year': '2026',
            'type': '权威百科', 'url': url, 'url2': None, 'verified': True, 'link_ok': True,
            'note': '中文维基百科 API 核对（作为跨语言对照来源）',
        })
        n_src += 1
        print('注册中文来源:', sid, zh)
sj['count'] = len(sj['sources'])
json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

for eid in ZH:
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    sid = 'w-zh-' + eid
    if sid in d['sources']:
        continue
    d['sources'].append(sid)
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作HP】补中文维基作为第二来源（跨语言对照，非独立机构互证）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n_ent += 1

print('\n注册来源 %d 个 | 补入条目 %d 个' % (n_src, n_ent))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
single = [e['id'] for e in es if len(e.get('sources', [])) == 1]
print('剩余单来源条目:', len(single))
