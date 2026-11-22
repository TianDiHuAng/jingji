# -*- coding: utf-8 -*-
"""轮次6 REVIEW-second-source 结果落地：
- 4条找到二源的数值补入第二来源并更新note
- 4条仅单源的维持待核实
- 13万亿vs11万亿矛盾明确记录"""
import json, re, urllib.parse

srcdata=json.load(open('data/sources.json',encoding='utf-8'))
existing={s['id'] for s in srcdata['sources']}
# 新增2个核对过的来源
NEW=[
 ('w-en-great-depression-in-us','Great Depression in the United States','en','Great_Depression_in_the_United_States','2685269'),
 ('w-zh-weimar-hyper','威瑪共和國惡性通貨膨脹','zh','威瑪共和國惡性通貨膨脹','5950700'),
]
for sid,title,lang,slug,pid in NEW:
    if sid in existing: continue
    srcdata['sources'].append({'id':sid,'title':title,'author':'Wikipedia contributors' if lang=='en' else '维基百科贡献者',
      'year':'2026','type':'权威百科',
      'url':f'https://{lang}.wikipedia.org/wiki/{slug}',
      'url2':None,'verified':True,'link_ok':True,
      'note':f'Wikipedia API核对：页面存在(pageid={pid})；轮次6二源复核新增，用于印证数值'})
    existing.add(sid)
srcdata['count']=len(srcdata['sources'])
json.dump(srcdata,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新增来源',len(NEW))

# 为找到二源的数值补来源（按label定位）
FIX={
 'great-depression':{
   '美国失业率峰值':('w-zh-002','中文维基《大萧条》原文"美国失业率飙升到25%"，双源印证'),
   '全球GDP降幅(1929–1932)':('w-zh-002','中文维基《大萧条》原文"全球GDP下跌了约15%"，双源印证'),
 },
 'weimar-hyper-1921':{
   '马克兑美元汇率(1923年11月)':('w-zh-weimar-hyper','繁体维基《威瑪共和國惡性通貨膨脹》原文"1美元等於4,210,500,000,000德國馬克"，双源印证'),
 },
 'wall-street-1929':{
   '股市市值跌幅(1929–1932)':('w-en-great-depression-in-us','英文维基《Great Depression in the United States》原文"stock market lost almost 90% of its value"，双源印证'),
 },
}
for eid,fixes in FIX.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    for kd in d.get('key_data',[]):
        if kd['label'] in fixes:
            sid,notemsg=fixes[kd['label']]
            if sid not in kd['sources']: kd['sources'].append(sid)
            kd['note']=kd.get('note','')+' 【二源印证】'+notemsg
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('补二源',eid)

# 13万亿矛盾记录（subprime-crisis-2007）
f='data/entries/subprime-crisis-2007.json'; d=json.load(open(f,encoding='utf-8'))
for kd in d.get('key_data',[]):
    if kd['label']=='家庭净资产缩水':
        kd['note']=kd.get('note','')+' 【数据分歧待核实】另一来源（英文维基 Great Recession）记为约11万亿美元（非13万亿），数值存在分歧，维持待核实，不替读者定值。'
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('记录13万亿vs11万亿分歧')
