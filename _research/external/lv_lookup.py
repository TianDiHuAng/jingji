# 为每个1970-2017案例找到Laeven-Valencia(2018) Table 1 中对应国家的原始行，供人工核对
import re
t=open('_research/external/lv2018.txt',encoding='utf-8').read()
i=t.find('Table 1. Crisis Dates');j=t.find('Table 2. Banking Crises Resolution')
tab=t[i:j]
M={
'albania-pyramid-1997':'Albania','argentina-crisis-2001':'Argentina','asian-financial-crisis-1997':'Thailand',
'black-wednesday-1992':'United Kingdom','cameroon-crisis-1987':'Cameroon','chilean-crisis-1982':'Chile',
'cypriot-2013':'Cyprus','finnish-banking-1990':'Finland','ghana-banking-2017':'Ghana','greek-debt-crisis':'Greece',
'icelandic-crisis-2008':'Iceland','indian-1991':'India','irish-banking-2008':'Ireland','israel-bank-1983':'Israel',
'japan-asset-bubble-1990':'Japan','mexican-peso-1994':'Mexico','myanmar-2003':'Myanmar','nigeria-debt':'Nigeria',
'norwegian-banking-1988':'Norway','russian-1998':'Russia','russian-crisis-2014':'Russia','savings-loan-1986':'United States',
'subprime-crisis-2007':'United States','spain-2008':'Spain','swedish-crisis-1990s':'Sweden','turkey-2001':'Turkey',
'ukrainian-crisis-2008':'Ukraine','uruguay-2002':'Uruguay','venezuelan-banking-1994':'Venezuela','venezuelan-banking-2009':'Venezuela',
'sterling-crisis-1976':'United Kingdom','uk-secondary-banking-1973':'United Kingdom','great-recession-russia':'Russia',
'angolan-kwanza-devaluation':'Angola','zambian-kwacha-reform':'Zambia','yemen-currency-divergence':'Yemen',
'northern-rock':'United Kingdom','china-liquidity-2013':'China, P.R.','souk-al-manakh-1982':'Kuwait','taiwan-bubble':'Taiwan',
}
lines=tab.split('\n')
for k,c in M.items():
    hit=[n for n,l in enumerate(lines) if l.startswith(c)]
    out=' || '.join(' '.join(lines[n:n+3]).strip() for n in hit[:2]) or '(表中无此国)'
    print(f'{k} [{c}] => {out[:160]}')
