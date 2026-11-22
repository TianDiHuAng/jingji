# -*- coding: utf-8 -*-
"""轮次6抽检修复：清理great-depression双源后残留的"单源待核实"矛盾表述；
subprime分歧来源补入key_data.sources。"""
import json

f='data/entries/great-depression.json'; d=json.load(open(f,encoding='utf-8'))
for kd in d['key_data']:
    n=kd['note']
    n=n.replace('；单一来源 w-en-great-depression，年份1933为通说峰值年（待核实精确年）。 【二源印证】',
                '；年份1933为通说峰值年（精确年待核实）。【双源印证：英文维基 w-en-great-depression + ')
    n=n.replace('；单源待核实。 【二源印证】中文维基《大萧条》原文"全球GDP下跌了约15%"，双源印证',
                '。【双源印证：英文维基 w-en-great-depression + 中文维基 w-zh-002，两来源均为"约15%"】')
    # 失业率的note收尾补引号
    if '【双源印证：英文维基 w-en-great-depression + ' in n and not n.rstrip().endswith('】'):
        n=n+'中文维基 w-zh-002，两来源均为25%】'
    kd['note']=n
# pending_notes
pn=d.get('pending_notes','')
pn=pn.replace(' 【轮次5数值复核】补入单源数值，需第二来源核实。',' 【轮次6二源复核】两条数值已双源印证；仍待核实：学者解释的具体适用与政策细节。')
d['pending_notes']=pn
# l3_detail
if 'l3_detail' in d:
    d['l3_detail']['data_caveat']=d['l3_detail']['data_caveat'].replace(
        '当前无经双源核实的具体数字，故不列数值。',
        '本条目失业率25%与全球GDP降幅约15%已经双源印证（见关键数据）；其余数值仍待核实。')
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('great-depression 矛盾表述已清理')

# subprime: 分歧来源补入
f='data/entries/subprime-crisis-2007.json'; d=json.load(open(f,encoding='utf-8'))
for kd in d['key_data']:
    if kd['label']=='家庭净资产缩水' and 'w-en-great-recession' not in kd['sources']:
        kd['sources'].append('w-en-great-recession')
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('subprime 分歧来源已补入')
