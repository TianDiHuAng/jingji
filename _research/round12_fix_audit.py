# -*- coding: utf-8 -*-
"""轮次12抽检修复：black-monday补deep_svg+修正主语；rodrigazo修正444%年份。"""
import json

# 1) black-monday-1987
f='data/entries/black-monday-1987.json'; d=json.load(open(f,encoding='utf-8'))
# 修正主语：1989恢复高点是标普500(336.77)，非道指
for t in d['timeline']:
    if t.get('year')==1989:
        t['event']='标普500指数直到1989年7月26日才恢复至崩盘前高点336.77点（据 Wikipedia Black Monday 1987）'
# 补 deep_svg（L3必需）——反馈回路图
def deep_svg(title):
    e=title.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:26]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 780 280' role='img'>",
       f"<text x='20' y='26' class='ttl'>{e}：机制与反馈回路</text>"]
    for x,t,sub in [(30,'触发条件','估值过高+杠杆'),(215,'放大机制','程序交易/恐慌'),(400,'临界转折','信心逆转'),(585,'后果与应对','崩盘/货币干预')]:
        s.append(f"<g><rect x='{x}' y='60' width='160' height='52' rx='6' class='box'/><text x='{x+9}' y='83' class='lbl'>{t}</text><text x='{x+9}' y='101' class='sub'>{sub}</text></g>")
    for a,b in [(190,215),(375,400),(560,585)]: s.append(f"<line x1='{a}' y1='86' x2='{b}' y2='86' class='ar'/>")
    s.append("<path d='M665 112 L665 170 L295 170 L295 112' fill='none' class='ar' style='stroke-dasharray:5,4'/>")
    s.append("<text x='400' y='163' class='sub'>反馈：后果强化放大机制</text>")
    s.append("<text x='20' y='230' class='note'>框架来源见本页来源列表；具体数值以正文为准。</text></svg>")
    return ''.join(s)
if not d.get('deep_svg'): d['deep_svg']=deep_svg(d['title'])
d['pending_notes']=d.get('pending_notes','')+' 【轮次12抽检修复】补deep_svg；修正1989恢复高点主语为标普500。'
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('black-monday 修复：deep_svg',bool(d.get('deep_svg')),'| timeline 1989:',[t['event'][:30] for t in d['timeline'] if t['year']==1989])

# 2) rodrigazo-1975：444%属1976
f='data/entries/rodrigazo-1975.json'; d=json.load(open(f,encoding='utf-8'))
# 修正 timeline
for t in d['timeline']:
    if '444%' in t.get('event',''):
        t['event']='通胀率从1974年24.4%升至1975年182.4%，1976年达444%（据 Wikipedia Rodrigazo）'
        t['year']=1976
        t['display']='1976年'
# 修正 key_data
for k in d.get('key_data',[]):
    if k.get('label')=='通胀率(1975年末)':
        k['label']='通胀率(1976年)'
        k['value']=444
        k['year']=1976
        k['unit']='%（阿根廷CPI，1976年）'
        k['note']='原文：inflation rate rose from 24.4% in 1974 to 182.4% in 1975 and 444% in 1976；444%属1976年；单一来源待核实。'
d['timeline'].sort(key=lambda t:t.get('year',0))
d['pending_notes']=d.get('pending_notes','')+' 【轮次12抽检修复】444%年份由1975末修正为1976（据维基原文）。'
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('rodrigazo 修复：key_data',[(k['label'],k['year'],k['value']) for k in d['key_data']])
