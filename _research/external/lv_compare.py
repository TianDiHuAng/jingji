# 对照：本库案例起始年 vs Laeven-Valencia(2018) Table 1 同国同类型危机年份
import json,glob
lv=json.load(open('_research/external/lv2018_table1.json',encoding='utf-8'))
M={'albania-pyramid-1997':'Albania','argentina-crisis-2001':'Argentina','asian-financial-crisis-1997':'Thailand',
'black-wednesday-1992':'United Kingdom','cameroon-crisis-1987':'Cameroon','chilean-crisis-1982':'Chile',
'cypriot-2013':'Cyprus','finnish-banking-1990':'Finland','ghana-banking-2017':'Ghana','greek-debt-crisis':'Greece',
'icelandic-crisis-2008':'Iceland','indian-1991':'India','irish-banking-2008':'Ireland','israel-bank-1983':'Israel',
'japan-asset-bubble-1990':'Japan','mexican-peso-1994':'Mexico','nigeria-debt':'Nigeria',
'norwegian-banking-1988':'Norway','russian-1998':'Russia','russian-crisis-2014':'Russia','savings-loan-1986':'United States',
'subprime-crisis-2007':'United States','spain-2008':'Spain','swedish-crisis-1990s':'Sweden','turkey-2001':'Turkey',
'ukrainian-crisis-2008':'Ukraine','uruguay-2002':'Uruguay','venezuelan-banking-1994':'Venezuela','venezuelan-banking-2009':'Venezuela',
'sterling-crisis-1976':'United Kingdom','uk-secondary-banking-1973':'United Kingdom','great-recession-russia':'Russia',
'angolan-kwanza-devaluation':'Angola','zambian-kwacha-reform':'Zambia','yemen-currency-divergence':'Yemen',
'northern-rock':'United Kingdom','souk-al-manakh-1982':'Kuwait','euro-area-crisis':None,'south-america-2002':'Argentina'}
T={'银行':'banking','货币':'currency','债务':'sovereign','泡沫':'banking'}
out=[]
for k,c in M.items():
    if not c or c not in lv: continue
    e=json.load(open(f'data/entries/{k}.json',encoding='utf-8'))
    ys=[t['year'] for t in e.get('timeline',[]) if isinstance(t.get('year'),int)]
    t=T.get(e.get('crisis_type'),'banking')
    near=[y for col in lv[c] for y in lv[c][col] if ys and min(ys)-3<=y<=max(ys)+1]
    out.append(dict(id=k,title=e['title'],country=c,type=e.get('crisis_type'),span=[min(ys),max(ys)] if ys else None,lv=lv[c],lv_in_span=sorted(set(near))))
json.dump(out,open('_research/external/lv_compare.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for o in out: print(o['id'],o['span'],o['country'],o['type'],'LV:',{a:b for a,b in o['lv'].items() if b},'近:',o['lv_in_span'])
