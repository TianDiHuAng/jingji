# -*- coding: utf-8 -*-
"""修复L3学者归属错配：Kindleberger→来源库中不存在的著作。
改为来源库中真实存在的 Niall Ferguson《The Ascent of Money》的准确表述。"""
import json, glob
OLD_HOLDER = 'Charles Kindleberger（Manias, Panics, and Crashes）'
OLD_HOLDER2 = 'Charles Kindleberger'
NEW_HOLDER = 'Niall Ferguson（The Ascent of Money）'
OLD_VIEW = '投机泡沫经历「替代—繁荣—狂热—崩盘—恐慌」的阶段序列，信贷扩张是关键推手'
OLD_VIEW2 = '强调信贷创造与资产价格的正反馈以及最后贷款人缺位'
NEW_VIEW = '信贷扩张与维多利亚时代以来的金融创新使投机泡沫反复出现，泡沫是资本市场的内在特征之一（据 The Ascent of Money 主题归纳）'
NEW_VIEW2 = '信贷创造与金融创新放大资产价格波动，最后贷款人机制影响危机后果（据 The Ascent of Money 主题归纳）'

fixed=[]
for f in glob.glob('data/entries/*.json'):
    d=json.load(open(f,encoding='utf-8'))
    changed=False
    for s in d.get('schools',[]):
        if s.get('holder')==OLD_HOLDER or OLD_HOLDER2 in s.get('holder',''):
            s['holder']=NEW_HOLDER
            changed=True
        if s.get('view')==OLD_VIEW:
            s['view']=NEW_VIEW; changed=True
        if s.get('view')==OLD_VIEW2:
            s['view']=NEW_VIEW2; changed=True
    if changed:
        json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
        fixed.append(d['id'])
print('修复条目',len(fixed))
print(', '.join(sorted(fixed)))
