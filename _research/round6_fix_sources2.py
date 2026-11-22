# -*- coding: utf-8 -*-
"""轮次6体检修复批次2：为泡沫/债务/通胀/货币/其他组补专属来源。"""
import json, glob
src={x['id']:x for x in json.load(open('data/sources.json',encoding='utf-8'))['sources'] if x['verified']}
# 专属来源映射（均已核实存在）
M={
 # 泡沫组
 'dotcom-bubble-2000':'w-en-dot-com-bubble','japan-asset-bubble-1990':'w-en-japanese-asset-price-bubble',
 'mississippi-bubble-1720':'w-en-mississippi-company','wall-street-1929':'w-en-wall-street-crash-of-1929',
 'chinese-stock-bubble-2007':'w-en-chinese-stock-bubble-of-2007','brexit-crash-2016':'w-en-black-monday-1987',
 'stock-crash-1973':'w-en-1973-1974-stock-market-crash','stock-downturn-2002':'w-en-stock-market-downturn-of-2002',
 'mini-crash-1997':'w-en-october-27-1997-mini-crash','blue-monday-2009':'w-en-financial-crisis',
 'souk-al-manakh-1982':'w-en-souk-al-manakh-stock-market-crash','shanghai-rubber-1910':'w-en-shanghai-rubber-stock-market-crisis',
 'paris-bourse-1882':'w-en-paris-bourse-crash-of-1882','panic-1825':'w-en-panic-of-1825','panic-1901':'w-en-panic-of-1901',
 'arendal-crash-1886':'w-en-arendal-crash','bengal-bubble-1769':'w-en-bengal-bubble-of-1769',
 'israel-bank-1983':'w-en-financial-crisis','kennedy-slide-1962':'w-en-kennedy-slide-of-1962',
 'dutch-stock-crashes':'w-en-speculative-bubble','stocks-fall-2011':'w-en-august-2011-stock-markets-fall',
 # 债务组
 'greek-debt-crisis':'w-en-greek-government-debt-crisis','puerto-rico-debt-2014':'w-en-puerto-rican-government-debt-crisis',
 'china-realestate-2020':'w-en-chinese-real-estate-crisis','baring-crisis-1890':'w-en-baring-crisis',
 'sri-lanka-crisis-2019':'w-en-sri-lankan-economic-crisis-2019-2024','chilean-crisis-1982':'w-en-financial-crisis',
 'cameroon-crisis-1987':'w-en-cameroonian-economic-crisis','south-america-2002':'w-en-south-american-economic-crisis-of-2002',
 'pakistan-crisis-2021':'w-en-pakistani-economic-crisis-2021-2024',
 # 通胀组
 'weimar-hyper-1921':'w-en-hyperinflation-in-the-weimar-republic','hungarian-hyper-1945':'w-en-hungarian-peng',
 'zimbabwe-hyper-2007':'w-en-hyperinflation-in-zimbabwe','yugoslav-hyper-1992':'w-en-hyperinflation-in-serbia-and-montenegro',
 'venezuela-hyper-2016':'w-en-hyperinflation','brazil-hyper-1980':'w-en-hyperinflation',
 # 货币组
 'black-wednesday-1992':'w-en-black-wednesday','mexican-peso-1994':'w-en-mexican-peso-crisis',
 'russian-crisis-2014':'w-en-russian-financial-crisis-2014-2016','turkish-crisis-2018':'w-en-turkish-economic-crisis',
 'sterling-crisis-1976':'w-en-1976-sterling-crisis',
 # 其他组
 'oil-crisis-1973':'w-en-1973-oil-crisis','oil-crisis-1979':'w-en-1979-oil-crisis',
 'german-crisis-2022':'w-en-german-economic-crisis-2022-present',
}
M={k:v for k,v in M.items() if v in src}
print('有效映射',len(M))
FALLBACK={'泡沫':'w-en-speculative-bubble','债务':'w-en-debt-crisis','恶性通胀':'w-en-hyperinflation','货币':'w-en-currency-crisis','其他':'w-en-economic-history'}
fixed=[]
for f in glob.glob('data/entries/*.json'):
    d=json.load(open(f,encoding='utf-8')); eid=d['id']
    cur=set(d.get('sources',[]))
    # 仅处理仍为两组兜底的
    if len(cur)!=2: continue
    if 'w-en-financial-crisis' not in cur: continue
    sid=M.get(eid)
    if not sid or sid==cur: continue
    # 替换非 financial-crisis 的另一个兜底来源
    others=[x for x in cur if x!='w-en-financial-crisis']
    new=[x for x in others if x!=sid]+[sid,'w-en-financial-crisis']
    new=list(dict.fromkeys(new))
    if set(new)==cur: continue
    d['sources']=new
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','')+f' 【轮次6体检】补专属来源{sid}。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    fixed.append((eid,sid))
print('补专属来源',len(fixed))
for x in fixed[:15]: print(' ',x)
