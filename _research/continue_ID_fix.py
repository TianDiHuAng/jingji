# -*- coding: utf-8 -*-
"""续作ID：修正 original-sin——① timeline 中英混杂错字；② 移除"定义性"key_data。

判断依据（round 73 确立的标准）：key_data 用于**具体数值型事实**，
"OSIN 取值范围 0—1""3 个指标""6 个决定因素"属于概念定义而非数据，
放进 key_data 会让读者误以为该条目有量化证据。
"""
import json

p = 'data/entries/original-sin.json'
d = json.load(open(p, encoding='utf-8'))

# 1) 修错字
for t in d.get('timeline', []):
    t['event'] = t['event'].replace('衡measured指标', '衡量指标')

# 2) 移除定义性 key_data
before = len(d.get('key_data', []))
d['key_data'] = []
d['pending_notes'] = (d.get('pending_notes', '')
                      + ' 【续作ID】移除"定义性"key_data（OSIN 取值范围／指标个数／因素个数均为概念定义，'
                        '非具体数值数据）；原罪的具体国别指标值待补来源后再录。')

json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('timeline 已修正错字；key_data %d → 0 条（定义性内容不充作数据）' % before)
for t in d['timeline']:
    print('  %s: %s' % (t['year'], t['event'][:70]))
