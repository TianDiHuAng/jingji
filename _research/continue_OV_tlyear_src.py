# -*- coding: utf-8 -*-
"""round 157：timeline 事件年份是否出现在专属来源缓存中（防年份错）。"""
import glob, json, os, re
es=[json.load(open(f,encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
GEN=('a currency crisis','an economic bubble','a financial crisis is','a bank run','a speculative bubble','in economics, a recession','hyperinflation is')
flags=[]
for e in es:
    p='_research/wiki_full/%s.txt'%e['id']
    if not os.path.exists(p): continue
    t=open(p,encoding='utf-8').read()
    if t[:200].lower().strip().startswith(GEN): continue  # 通用页不作核对
    tl=e.get('timeline') or []
    miss=[]
    for ev in tl:
        y=ev.get('year')
        if not isinstance(y,int) or y==0: continue
        if str(y) not in t:
            miss.append((y,(ev.get('event') or '')[:40]))
    if miss:
        flags.append((e['id'], miss))
print('timeline 年份不在专属缓存中的条目:', len(flags))
for eid,miss in flags[:40]:
    print('  %-26s %s'%(eid, miss))
