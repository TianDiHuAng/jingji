# -*- coding: utf-8 -*-
"""轮次16 协议F体检修复：为11条无related条目补有意义的同主题互链。"""
import json, glob, os
REL={
 'asian-financial-crisis-1997':['mexican-peso-1994','russian-1998','mini-crash-1997'],
 'bank-run':['deposit-insurance','lender-of-last-resort','contagion'],
 'black-monday-1987':['wall-street-1929','dotcom-bubble-2000','mini-crash-1997'],
 'central-bank':['lender-of-last-resort','gold-standard','bretton-woods'],
 'dawes-plan-1924':['weimar-hyper-1921','great-depression','latin-american-debt-1975'],
 'hainan-property-bubble-1992':['japan-asset-bubble-1990','taiwan-bubble','china-realestate-2020'],
 'kipper-wipper-1618':['tulip-mania-1637','crisis-third-century'],
 'recession-1937-1938':['great-depression','panic-1837'],
 'rodrigazo-1975':['brazil-hyper-1980','latin-american-debt-1975','argentina-crisis-2001'],
 'taiwan-bubble':['japan-asset-bubble-1990','hainan-property-bubble-1992','chinese-stock-bubble-2007'],
 'us-video-game-crash-1983':['dotcom-bubble-2000','black-monday-1987'],
}
ids={os.path.splitext(os.path.basename(f))[0] for f in glob.glob('data/entries/*.json')}
for eid,rels in REL.items():
    rels=[r for r in rels if r in ids and r!=eid]
    f='data/entries/'+eid+'.json'
    d=json.load(open(f,encoding='utf-8'))
    d['related']=rels
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'->',rels)
