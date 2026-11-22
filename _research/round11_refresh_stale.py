# -*- coding: utf-8 -*-
"""轮次11协议F：刷新土耳其通胀现状类数据，补充2026-07最新值。"""
import json
f='data/entries/turkish-crisis-2018.json'; d=json.load(open(f,encoding='utf-8'))
# 新增2026-07最新值数据点
new_kd={'label':'通胀率(2026年7月,最新)','value':31.75,'unit':'%（土耳其CPI同比，2026-07；现状类数据）',
  'year':2026,'comparable_price':False,
  'note':'原文：As of July 2026 the YoY inflation stood on 31.75%；单一来源、现状类数据，核对日期2026-11-22（距数据4个月，未过期）。此前2024-11为47.09%，持续回落。','sources':['w-en-turkish-economic-crisis']}
have={k.get('label') for k in d.get('key_data',[])}
if new_kd['label'] not in have: d['key_data'].append(new_kd)
# timeline 补最新节点
new_tl={'year':2026,'display':'2026年7月','event':'土耳其CPI同比通胀降至31.75%（据 Wikipedia Turkish economic crisis；现状类数据，核对2026-11-22）','sources':['w-en-turkish-economic-crisis']}
have_t={t.get('display') for t in d.get('timeline',[])}
if new_tl['display'] not in have_t:
    d['timeline'].append(new_tl)
    d['timeline'].sort(key=lambda t:t.get('year',0))
# 旧数据点标注为历史快照
for kd in d['key_data']:
    if kd.get('label')=='通胀率(2024年11月)':
        kd['note']=kd.get('note','').replace('现状类数据待核实','历史快照（2024-11），已由2026-07数据点更新；仍为当时准确记录')
d['pending_notes']=d.get('pending_notes','')+' 【轮次11协议F体检】现状类数据刷新：补2026-07通胀31.75%，距核对4个月未过期；2024-11标注为历史快照。'
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('土耳其通胀数据已刷新，key_data',len(d['key_data']),'timeline',len(d['timeline']))

# 巴基斯坦：2024-25贫困率已是维基最新可查值，标注核对日期
f2='data/entries/pakistan-crisis-2021.json'; d2=json.load(open(f2,encoding='utf-8'))
for kd in d2.get('key_data',[]):
    if '贫困率' in kd.get('label',''):
        kd['note']=kd.get('note','')+' 【协议F体检2026-11-22】该值为维基可查最新（2024-25）；单一来源待核实。'
json.dump(d2,open(f2,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('巴基斯坦贫困率已标注核对日期')
