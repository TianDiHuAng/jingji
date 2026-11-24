# -*- coding: utf-8 -*-
"""续作BC：引入美联储历史(federalreservehistory.org)作为第二独立来源，交叉验证并补充数据。"""
import json

# 新增官方来源
sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
NEW = {
 'fed-great-depression': ('The Great Depression', 'https://www.federalreservehistory.org/essays/great-depression'),
 'fed-stock-crash-1929': ('Stock Market Crash of 1929', 'https://www.federalreservehistory.org/essays/stock-market-crash-of-1929'),
}
for sid, (title, url) in NEW.items():
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': title, 'author': 'Federal Reserve History (美国联邦储备系统历史站)',
        'year': 'n.d.', 'type': '官方机构', 'url': url, 'url2': None,
        'verified': True, 'link_ok': True,
        'note': '官方机构页面(本会话抓取核对，非维基，作为第二独立来源)'
    })
    ex.add(sid)
    print('新增官方来源', sid, '|', title)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

# 1) wall-street-1929：补充美联储数据 + 交叉验证既有90%
f = 'data/entries/wall-street-1929.json'
d = json.load(open(f, encoding='utf-8'))
if 'fed-stock-crash-1929' not in d['sources']:
    d['sources'].append('fed-stock-crash-1929')
have = {k['label'] for k in d['key_data']}
add = [
 ('道指单日跌幅(1929-10-28黑色星期一)', -13, '%（近13%）', 1929,
  '原文：On Black Monday, October 28, 1929, the Dow Jones Industrial Average declined nearly 13 percent（美联储历史）。', ['fed-stock-crash-1929']),
 ('道指单日跌幅(1929-10-29黑色星期二)', -12, '%（近12%）', 1929,
  '原文：On the following day, Black Tuesday, the market dropped nearly 12 percent（美联储历史）。', ['fed-stock-crash-1929']),
 ('股指最低点较峰值跌幅(至1932)', -89, '%（美联储历史口径；本条目另有"市值跌幅90%"来自维基，两源基本一致）', 1932,
  '原文：its lowest value of the twentieth century, 89 percent below its peak（美联储历史）。与维基来源的90%相互印证。', ['fed-stock-crash-1929']),
]
for lab, val, unit, yr, note, srcs in add:
    if lab in have:
        continue
    d['key_data'].append({'label': lab, 'value': val, 'unit': unit, 'year': yr,
                          'comparable_price': False, 'note': note, 'sources': srcs})
# 交叉验证标注
for k in d['key_data']:
    if k['label'].startswith('股市市值跌幅'):
        k['note'] = k.get('note', '') + '｜**已交叉验证**：美联储历史站记载"较峰值低89%"，与本条90%基本一致（两个独立来源）。'
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BC】部分数据已引入美联储历史站作为第二独立来源交叉验证。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('wall-street-1929 补', len(add), '条 + 交叉验证标注')

# 2) great-depression：补充货币供给数据
f = 'data/entries/great-depression.json'
d = json.load(open(f, encoding='utf-8'))
if 'fed-great-depression' not in d['sources']:
    d['sources'].append('fed-great-depression')
have = {k['label'] for k in d['key_data']}
lab = '美国货币供给降幅(1930秋—1933冬)'
if lab not in have:
    d['key_data'].append({
        'label': lab, 'value': -30, 'unit': '%（近30%）', 'year': 1933,
        'comparable_price': False,
        'note': '原文：From the fall of 1930 through the winter of 1933, the money supply fell by nearly 30 percent（美联储历史）。',
        'sources': ['fed-great-depression']})
d['pending_notes'] = d.get('pending_notes', '') + ' 【续作BC】货币供给数据来自美联储历史站(第二独立来源)。'
json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('great-depression 补1条')
