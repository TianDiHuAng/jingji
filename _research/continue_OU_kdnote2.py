# -*- coding: utf-8 -*-
"""round 156b：改进判定——绝对值、更多换算因子、拼写数字，重筛 value vs note 原文。"""
import glob, json, re

es=[json.load(open(f,encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
NUM=re.compile(r'\d[\d,]*\.?\d*')
SPELL={'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,'nine':9,'ten':10,
       'eleven':11,'twelve':12,'thirteen':13,'fifteen':15,'twenty':20,'thirty':30,'fifty':50,'hundred':100}
def canon(x):
    try: return float(str(x).replace(',',''))
    except: return None
flags=[]
for e in es:
    for k in e.get('key_data') or []:
        v=canon(k.get('value'))
        if v is None: continue
        note=k.get('note') or ''
        m=re.search(r'原文[：:]\s*(.+)',note,re.S)
        if not m: continue
        quote=m.group(1)
        nums=[abs(canon(x)) for x in NUM.findall(quote)]
        nums=[n for n in nums if n is not None]
        for w,n in SPELL.items():
            if re.search(r'\b'+w+r'\b', quote, re.I): nums.append(n)
        av=abs(v)
        ok=False
        for n in nums:
            for f in (1,10,100,1000,1e4,1e6,1e9,0.1,0.01,0.001,1e-4,1e-6,1e-9):
                if n*f!=0 and abs(n*f-av)<=max(av*0.02,0.5): ok=True;break
            if ok:break
        if not ok:
            flags.append((e['id'],k.get('label','')[:26],k.get('value'),sorted(set(round(x,5) for x in nums))[:6],quote[:75]))
print('仍疑似不一致:',len(flags))
for f in flags:
    print('  %-24s %-26s v=%-11s noteNum=%s | %s'%f)
