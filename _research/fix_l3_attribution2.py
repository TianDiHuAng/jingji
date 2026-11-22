# -*- coding: utf-8 -*-
"""修复第二处学者归属错配：Reinhart&Rogoff→Nouriel Roubini（来源库真实作者）。"""
import json, glob
OLD='Carmen Reinhart & Kenneth Rogoff（This Time Is Different 主题，见危机经济学综述）'
NEW='Nouriel Roubini（Crisis Economics）'
OLDV='高债务与低增长之间存在关联，债务累积常 precede 危机'
NEWV='高债务与宏观失衡叠加时，危机风险上升；债务累积常先于危机（据 Crisis Economics 主题归纳）'
n=0
for f in glob.glob('data/entries/*.json'):
    d=json.load(open(f,encoding='utf-8')); ch=False
    for s in d.get('schools',[]):
        if s.get('holder')==OLD: s['holder']=NEW; ch=True
        if s.get('view')==OLDV: s['view']=NEWV; ch=True
    if ch:
        json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2); n+=1
print('修复',n,'条')
