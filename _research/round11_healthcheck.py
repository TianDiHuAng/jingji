# -*- coding: utf-8 -*-
"""协议F增强体检：现状类数据过期检查（>12个月未核对需刷新）。"""
import json, glob, re
from datetime import date

TODAY = date(2026,11,22)
CUTOFF_YEAR = 2025  # 2025-11之前的数据视为>12个月
report=['# 协议F增强体检：现状类数据过期检查（轮次11）','',
        f'检查日期：{TODAY}；现状类数据若截至年份 ≤ {CUTOFF_YEAR}，距核对已>12个月，需重新核对。','']
stale=[]
current_ok=[]
for f in sorted(glob.glob('data/entries/*.json')):
    d=json.load(open(f,encoding='utf-8'))
    # 检查 key_data 中标注"现状类"的
    for kd in d.get('key_data',[]):
        note=kd.get('note','')
        is_historical = ('历史快照' in note or '历史记录' in note
                         or ('协议F体检' in note and '最新' in note))  # 已标注为历史或已确认最新
        if '现状类' in note and not is_historical:
            y=kd.get('year')
            entry=(d['id'],kd.get('label'),y,note[:60])
            if isinstance(y,int) and y<=CUTOFF_YEAR:
                stale.append(entry)
            else:
                current_ok.append(entry)
    # 检查 timeline 中标注"现状类"的
    for t in d.get('timeline',[]):
        evt=t.get('event','')
        is_historical = '历史快照' in evt or '历史记录' in evt
        if '现状类' in evt and not is_historical:
            y=t.get('year')
            entry=(d['id'],t.get('display'),y,t.get('event','')[:50])
            if isinstance(y,int) and y<=CUTOFF_YEAR:
                stale.append(entry)
            else:
                current_ok.append(entry)

report.append(f'## 现状类数据总数：{len(stale)+len(current_ok)}')
report.append(f'## 过期（≤{CUTOFF_YEAR}，需刷新）：{len(stale)}')
for x in stale: report.append(f'  - {x[0]} | {x[1]} | {x[2]} | {x[3]}')
report.append(f'## 近期（无需刷新）：{len(current_ok)}')
for x in current_ok: report.append(f'  - {x[0]} | {x[1]} | {x[2]}')
open('HEALTH_CHECK_F.md','w',encoding='utf-8').write('\n'.join(report)+'\n')
print('\n'.join(report[:25]))
