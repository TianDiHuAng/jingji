# -*- coding: utf-8 -*-
"""续作JM：修正 crisis-33ce 的区域标注（全球→欧洲），并加入一致性规则。

依据：U1（早期—17世纪）10 条中 9 条标"欧洲"，仅 crisis-33ce（公元33年罗马危机）标"全球"。
罗马危机的地理范围与 crisis-third-century／roman-currency 等完全一致，应同为欧洲。
新增 R20：U1 单元的案例不得标"全球"（该时期尚无全球性金融体系）。
"""
import glob
import json

p = 'data/entries/crisis-33ce.json'
d = json.load(open(p, encoding='utf-8'))
old = d['region']
d['region'] = '欧洲'
json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('crisis-33ce: region %s → 欧洲' % old)

cov = json.load(open('coverage.json', encoding='utf-8'))
for e in cov['entries']:
    if e['id'] == 'crisis-33ce':
        e['region'] = '欧洲'
        break
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage.json 已同步')

# 复核：U1 是否还有"全球"
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
left = [(e['id'], e['region']) for e in es if e['unit'].startswith('U1') and e['region'] == '全球']
print('U1 仍标全球的:', left if left else '无')
