# 合并 _research/tl_add 中经核对的时间线事件到条目（不写入 evidence，仅保留于 _research）
import json,glob,os,re
IDS=set('edict-maximum-prices london-econ-1933 first-republic flash-crash-2010 rodrigazo-1975 sterling-crisis-1976 panic-1884 souk-al-manakh-1982 great-recession-russia spain-2008 irish-banking-2008 haitian-independence-debt northern-rock british-credit-1772 federal-reserve-act second-bank panic-1825 zambian-kwacha-reform panic-1893 panic-1837 crypto-bubble defi recession-1920-1921 bond-crisis-1994 egypt-2023 nyc-fiscal-1975 oil-price-war-2020 national-banking-act uk-ldi-crisis-2022 nixon-shock henan-2022 terra-luna-2022 worldcom ems indian-1991 shanghai-rubber-1910 stocks-fall-2011 ukrainian-crisis-2008 ghana-banking-2017 free-banking railway-mania dubai-debt-2009 argentina-2018 australian-banking-1893 kennedy-slide-1962 overend-gurney franklin-national-1974 finnish-banking-1990 uruguay-2002 bardi-family panic-1866 kipper-wipper-1618 emergency-banking-act-1933 turkey-2001 mini-crash-1997 chilean-crisis-1982 banking-act-1935 angolan-kwanza-devaluation'.split())
DUP=('破产','倒闭','崩盘')
tot=0;rej=[];skipped=[]
for f in sorted(glob.glob('_research/tl_add/*.json')):
    d=json.load(open(f,encoding='utf-8'));i=d.get('id')
    if i not in IDS: continue
    if not d.get('add'): skipped.append((i,d.get('skip_reason','')[:60]));continue
    p=f'data/entries/{i}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw)
    t=open(f'_research/wiki_full/{i}.txt',encoding='utf-8').read()
    tl=e.setdefault('timeline',[]);n=0
    for a in d['add']:
        y=a['year']
        ok=a['evidence'] in t and all(s in e['sources'] for s in a['sources']) and isinstance(y,int) and len(a['event'])<=70
        if ok and y>0: ok=str(y) in a['evidence']
        same=[x for x in tl if x.get('year')==y and any(w in x.get('event','') and w in a['event'] for w in DUP)]
        if not ok or same: rej.append((i,y,a['event'][:30],'dup' if same else 'verify'));continue
        ev=re.sub(r'\$?(\d+(?:\.\d+)?) ?billion ?(美元)?',lambda m:f'{float(m.group(1))*10:g}亿'+('美元' if m.group(0).startswith('$') or m.group(2) else ''),a['event'])
        ev=re.sub(r'(\d+(?:\.\d+)?) ?million',lambda m:f'{float(m.group(1))*100:g}万',ev)
        tl.append({'year':y,'display':a['display'],'event':ev,'sources':a['sources']});n+=1
    tl.sort(key=lambda x:x['year'] if isinstance(x.get('year'),int) else 0)
    s=json.dumps(e,ensure_ascii=False,indent=2)+'\n'
    open(p,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s);tot+=n
print('added',tot);print('rejected',rej);print('skipped',skipped)
