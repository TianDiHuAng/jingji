# -*- coding: utf-8 -*-
"""轮次6：体检修复"来源雷同"——为共享兜底来源的条目补入专属维基来源。
匹配：panic-of-YYYY + 关键词映射；只补确实存在的专属来源，不硬凑。"""
import json, re, glob

src={x['id']:x for x in json.load(open('data/sources.json',encoding='utf-8'))['sources'] if x['verified']}

# 显式映射（条目id -> 专属来源id），来源均已核对存在
EXPLICIT={
 'savings-loan-1986':'w-en-savings-and-loan-crisis',
 'showa-crisis-1927':'w-en-sh-wa-financial-crisis',
 'irish-banking-2008':'w-en-post-2008-irish-banking-crisis',
 'china-liquidity-2013':'w-en-chinese-banking-liquidity-crisis-of-2013',
 'ghana-banking-2017':'w-en-ghana-banking-crisis',
 'venezuelan-banking-1994':'w-en-venezuelan-banking-crisis-of-1994',
 'venezuelan-banking-2009':'w-en-venezuelan-banking-crisis-of-2009-2010',
 'rhode-island-banking-1990':'w-en-rhode-island-banking-crisis',
 'uk-secondary-banking-1973':'w-en-secondary-banking-crisis',
 'lebanese-liquidity-2019':'w-en-lebanese-liquidity-crisis',
 'bank-crisis-2023':'w-en-2023-united-states-banking-crisis',
 'argentina-crisis-2001':'w-en-argentine-economic-crisis-1999-2002',
 'great-recession-russia':'w-en-great-recession-in-russia',
 'australian-banking-1893':'w-en-australian-banking-crisis-of-1893',
 'panic-1796':'w-en-panic-of-1796-1797',
}
# 验证显式映射都存在
EXPLICIT={k:v for k,v in EXPLICIT.items() if v in src}
print('显式映射有效',len(EXPLICIT))

fixed=[]
for f in glob.glob('data/entries/*.json'):
    d=json.load(open(f,encoding='utf-8')); eid=d['id']
    if set(d.get('sources',[]))!={'w-en-bank-run','w-en-financial-crisis'}: continue
    sid=None
    if eid in EXPLICIT: sid=EXPLICIT[eid]
    else:
        m=re.match(r'panic-(\d{4})',eid)
        if m:
            cand='w-en-panic-of-'+m.group(1)
            if cand in src: sid=cand
    if not sid: continue
    d['sources']=[x for x in d['sources'] if x!='w-en-bank-run']  # 替换兜底之一
    if sid not in d['sources']: d['sources'].append(sid)
    d['sources']=list(dict.fromkeys(d['sources']))
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','')+f' 【轮次6体检】补专属来源{sid}替换兜底，待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    fixed.append((eid,sid))
print('补专属来源',len(fixed),'条')
for x in fixed[:20]: print(' ',x)
