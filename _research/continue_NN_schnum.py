# -*- coding: utf-8 -*-
"""round 136：schools/comparison 中内嵌数字 vs 来源全文。"""
import glob, json, os, re

es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
FULL = '_research/wiki_full'
NUM = re.compile(r'(\d[\d,]*\.?\d*)\s*(%|％|亿|万|倍|个百分点|美元|英镑|日元|点)?')

def variants(num):
    out=set(); s=num.replace(',','')
    out.add(num); out.add(s)
    try:
        f=float(s)
        if f==int(f): out.add(str(int(f))); out.add('{:,}'.format(int(f)))
        else: out.add('%.1f'%f); out.add('%.2f'%f)
    except ValueError: pass
    return out

flags=[]
for e in es:
    p=os.path.join(FULL,e['id']+'.txt')
    if not os.path.exists(p): continue
    t=open(p,encoding='utf-8').read()
    # schools
    for s in e.get('schools') or []:
        v=s.get('view') or ''
        for m in NUM.finditer(v):
            num=m.group(1)
            # 只查 3 位以上数字或带单位的，减少噪声
            if len(num.replace(',','').split('.')[0])<2 and not m.group(2): continue
            if not any(x and x in t for x in variants(num)):
                flags.append((e['id'],'schools',num+(m.group(2) or ''), v[:50]))
    # comparison
    c=e.get('comparison') or ''
    for m in NUM.finditer(c):
        num=m.group(1)
        if len(num.replace(',','').split('.')[0])<2 and not m.group(2): continue
        if not any(x and x in t for x in variants(num)):
            flags.append((e['id'],'comparison',num+(m.group(2) or ''), c[:50]))
print('=== schools/comparison 数字未在来源全文 ===')
print('条数:', len(flags))
for f in flags[:40]:
    print('  %-26s %-11s %-8s | %s' % f)
