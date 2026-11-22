# -*- coding: utf-8 -*-
"""轮次6体检修复：为无 related 入链的条目补互链（同危机类型+相邻时期）。"""
import json, glob
from collections import defaultdict

entries={}
for f in glob.glob('data/entries/*.json'):
    d=json.load(open(f,encoding='utf-8')); entries[d['id']]=d

# 按 (危机类型) 分组
by_type=defaultdict(list)
for eid,d in entries.items(): by_type[d['crisis_type']].append(eid)

# 同期优先
def pick_related(d, n=3):
    peers=[x for x in by_type[d['crisis_type']] if x!=d['id']]
    # 同期优先
    same_p=[x for x in peers if entries[x]['period']==d['period']]
    pool = same_p if len(same_p)>=n else peers
    # 避免已有 related 指向的
    have=set(d.get('related',[]))
    pool=[x for x in pool if x not in have]
    return pool[:n]

fixed=0
for eid,d in entries.items():
    if d.get('related'): continue  # 已有互链的不动
    rel=pick_related(d)
    if rel:
        d['related']=rel
        json.dump(d,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
        fixed+=1
print('补互链条目',fixed)
print('样例:',[(eid,entries[eid]['related']) for eid in list(entries)[:3]])
