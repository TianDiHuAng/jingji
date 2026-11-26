# 合并 _research/tl_add 中经核对的时间线事件到条目（不写入 evidence，仅保留于 _research）
import json,glob,os,re
IDS=set('''brexit-crash-2016 turkish-crisis-2018 washington-mutual silicon-valley-bank merrill-lynch drexel signature-bank nz-1984-reform indymac myanmar-2003
bear-stearns danish-bankruptcy-1813 gold-reserve-act-1934 sterling-area enron nigeria-debt medici-bank gamestop-2021 bernie-madoff nira-1933 china-realestate-2020 lehman black-monday-1987
aig panic-1819 ltcm rhode-island-banking-1990 credit-suisse-2023 bcci dutch-collapse-1780 black-friday-1869 barings-1995 roman-currency panic-1873'''.split())
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
        tl.append({'year':y,'display':a['display'],'event':a['event'],'sources':a['sources']});n+=1
    tl.sort(key=lambda x:x['year'] if isinstance(x.get('year'),int) else 0)
    s=json.dumps(e,ensure_ascii=False,indent=2)+'\n'
    open(p,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s);tot+=n
print('added',tot);print('rejected',rej);print('skipped',skipped)
