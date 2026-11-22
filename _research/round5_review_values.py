# -*- coding: utf-8 -*-
"""轮次5：REVIEW-values — 补入经来源提取的具体数值。
纪律：数字直接来自 Wikipedia 正文（已抓取核对），每条注明来源、年份、口径；
单一来源的数值明确标注"单源待核实"，条目 needs_verification 保持 true。不编造。"""
import json

# 数值来自 _research/wiki_*.txt（Wikipedia API 正文，2026-11-22 抓取）
DATA = {
 'great-depression': [
   {'label':'美国失业率峰值','value':25,'unit':'%（美国，1930s，口径：失业人口/劳动力）',
    'year':1933,'comparable_price':False,
    'note':'原文：unemployment rate had risen to 25%；单一来源 w-en-great-depression，年份1933为通说峰值年（待核实精确年）。',
    'sources':['w-en-great-depression']},
   {'label':'全球GDP降幅(1929–1932)','value':15,'unit':'%（全球，1929–1932，口径：实际GDP累计变化）',
    'year':1932,'comparable_price':True,
    'note':'原文：Between 1929 and 1932, worldwide GDP fell by an estimated 15%；单源待核实。',
    'sources':['w-en-great-depression']},
 ],
 'weimar-hyper-1921': [
   {'label':'马克兑美元汇率(1922年中)','value':320,'unit':'马克/美元（1922年中，名义汇率）',
    'year':1922,'comparable_price':False,
    'note':'原文：320 marks per dollar in mid-1922；单源待核实。',
    'sources':['w-en-hyperinflation-in-the-weimar-republic']},
   {'label':'马克兑美元汇率(1923年11月)','value':4210500000000,'unit':'马克/美元（1923年11月，名义汇率）',
    'year':1923,'comparable_price':False,
    'note':'原文：one US dollar was worth 4,210,500,000,000 marks (Nov 1923)；单源待核实。',
    'sources':['w-en-hyperinflation-in-the-weimar-republic']},
 ],
 'wall-street-1929': [
   {'label':'股市市值跌幅(1929–1932)','value':90,'unit':'%（较崩盘前市值，至1932年7月）',
    'year':1932,'comparable_price':False,
    'note':'原文：stock market had lost some 90% of its pre-crash value by July 8 1932；单源待核实。',
    'sources':['w-en-wall-street-crash-of-1929']},
   {'label':'黑色星期四成交量','value':12.9,'unit':'百万股（1929-10-24，纽约证交所）',
    'year':1929,'comparable_price':False,
    'note':'原文：record 12.9 million shares traded on Black Thursday；单源待核实。',
    'sources':['w-en-wall-street-crash-of-1929']},
 ],
 'subprime-crisis-2007': [
   {'label':'房价平均跌幅','value':30,'unit':'%（美国，约2007–2009，口径：平均房价）',
    'year':2009,'comparable_price':False,
    'note':'原文：housing prices fell nearly 30% on average；单源待核实。',
    'sources':['w-en-subprime-mortgage-crisis']},
   {'label':'家庭净资产缩水','value':13,'unit':'万亿美元（美国，2007Q2峰值至2012Q4恢复前，约20%）',
    'year':2012,'comparable_price':False,
    'note':'原文：household net worth declined by nearly $13 trillion (20%) from Q2 2007 peak；单源待核实。',
    'sources':['w-en-subprime-mortgage-crisis']},
 ],
}

for eid, rows in DATA.items():
    f='data/entries/'+eid+'.json'
    d=json.load(open(f,encoding='utf-8'))
    # 只补入尚不存在的 label
    have={k.get('label') for k in d.get('key_data',[])}
    added=0
    for r in rows:
        if r['label'] in have: continue
        d.setdefault('key_data',[]).append(r); added+=1
    if added:
        d['needs_verification']=True
        d['pending_notes']=d.get('pending_notes','')+' 【轮次5数值复核】补入单源数值，需第二来源核实。'
        json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
        print(eid,'补入',added,'条数值')
