# -*- coding: utf-8 -*-
"""续作KK：清理 overview 末尾的「具体XX待核实」套话。

问题（round 112）：564 个条目（88%）的 overview 以「具体XX待核实」结尾。
这不是纯套话，但它是**无信息量的模板化尾巴**，且让每条概述的结尾都一样。
「待核实」的信息本身有价值，应移入 pending_notes，而不是占据正文位置。

策略：移除该句，其内容并入 pending_notes；若移除后 overview 过短（<150 字）则**保留并标记**，
避免把内容不足的条目掩盖成"已清理"。
"""
import glob
import json
import re

PAT = re.compile(r'[；。]?\s*具体[^。]{0,24}待(核实|补充|查)[。]?\s*$')
LOW = 150

removed = kept = 0
short_list = []
for f in glob.glob('data/entries/*.json'):
    d = json.load(open(f, encoding='utf-8'))
    ov = d.get('overview') or ''
    m = PAT.search(ov)
    if not m:
        continue
    tail = m.group(0).strip('；。 ')
    new = PAT.sub('', ov).rstrip()
    if len(new) < LOW:
        kept += 1
        short_list.append((d['id'], len(new)))
        continue
    d['overview'] = new
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【清理】原概述结尾含「%s」，已移入此处。' % tail)
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    removed += 1

print('已移除套话: %d 条' % removed)
print('因移除后过短而保留: %d 条' % kept)
for s in short_list[:10]:
    print('   保留:', s)
