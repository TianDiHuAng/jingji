# -*- coding: utf-8 -*-
"""续作OS：修单元误分类（railway-mania U3→U2、cook-islands-currency U5→U4）+ creditanstalt 补 timeline。
并同步 coverage.json、COVERAGE_MATRIX、scope.md。"""
import json

def load(e): return json.load(open('data/entries/%s.json'%e, encoding='utf-8'))
def save(e,d): json.dump(d, open('data/entries/%s.json'%e,'w',encoding='utf-8'), ensure_ascii=False, indent=2)

# 1) railway-mania: U3 → U2
d=load('railway-mania'); d['unit']='U2 18—19世纪'; d['period']='18—19世纪'
d['pending_notes']=(d.get('pending_notes','')+' 【续作OS｜round155】单元误分类：铁路狂热(1845-47)原标 U3(20世纪上半)，改 U2(18—19世纪)。')
save('railway-mania',d); print('railway-mania → U2')

# 2) cook-islands-currency: U5 → U4
d=load('cook-islands-currency'); d['unit']='U4 20世纪下半'; d['period']='20世纪下半'
d['pending_notes']=(d.get('pending_notes','')+' 【续作OS｜round155】单元误分类：核心事件 1989-1995 原标 U5(21世纪)，改 U4(20世纪下半)。')
save('cook-islands-currency',d); print('cook-islands-currency → U4')

# 3) creditanstalt: 补 1931/1934 timeline
d=load('creditanstalt')
d['timeline']=[
 {'year':1855,'sources':['w-en-creditanstalt'],'event':'Creditanstalt 在维也纳成立'},
 {'year':1931,'sources':['w-en-creditanstalt'],'event':'该行 1931 年失败，引发中欧银行危机，被视为大萧条首批重大银行倒闭之一'},
 {'year':1934,'sources':['w-en-creditanstalt'],'event':'与维也纳银行协会(Wiener Bankverein)及下奥地利贴现公司的健全部分合并'},
]
d['pending_notes']=(d.get('pending_notes','')+' 【续作OS｜round155】timeline 原仅 1855 创立，补 1931 危机/1934 合并。')
save('creditanstalt',d); print('creditanstalt timeline 补 1931/1934')

# 4) 同步 coverage.json
cov=json.load(open('coverage.json',encoding='utf-8'))
newu={'railway-mania':'U2 18—19世纪','cook-islands-currency':'U4 20世纪下半'}
for c in cov['entries']:
    if c['id'] in newu:
        c['unit']=newu[c['id']]; c['period']='18—19世纪' if 'U2' in newu[c['id']] else '20世纪下半'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage.json 已同步')
