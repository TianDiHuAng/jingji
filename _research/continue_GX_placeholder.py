# -*- coding: utf-8 -*-
"""续作GX：删除 2 条占位型 key_data（value=1 的"示意口径"，非史料原值）。

依据项目原则：宁可页面不显示某区块，也不显示对所有条目都成立、因而毫无信息量的话。
这类"归一化为1"的占位值既不是史料数据，又会让读者误以为该条目有量化数据。
"""
import json
import glob

DROP = {
 'south-sea-bubble-1720': '股价峰值相对面值（倍数口径）',
 'tulip-mania-1637': '常见品种价格峰值（简述）',
}

for eid, label in DROP.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    before = len(d.get('key_data', []))
    d['key_data'] = [k for k in d.get('key_data', []) if k.get('label') != label]
    after = len(d['key_data'])
    if not d['key_data']:
        d.pop('key_data', None)
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作GX】移除占位型数据项「%s」（原 value=1 为归一化示意口径，非史料原值）；'
                            '史料未载可核实的绝对数值，故本条目不设"关键数据"区块。' % label)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('%-24s key_data %d → %d%s' % (eid, before, after, '（已清空并移除字段）' if after == 0 else ''))

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
print('\n全站 key_data 条数:', sum(len(e.get('key_data', [])) for e in es))
