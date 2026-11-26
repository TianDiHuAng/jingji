# 合并 _research/ov_add 中经核对的概述句到条目 overview 末尾
import json,re
IDS='aiib afdb idb adb ebrd bank-of-england iais arthur-andersen riksbank freddie-mac gdp stagflation diamond-dybvig externality actuarial j-curve gold-standard neutral-rate bullion marshall-lerner central-bank common-pool pigouvian-tax capital-control deindustrialization business-cycle credit-crunch debt-crisis subprime-lending'.split()
tot=0;rej=[]
for i in IDS:
    d=json.load(open(f'_research/ov_add/{i}.json',encoding='utf-8'))
    p=f'data/entries/{i}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw)
    t=open(f'_research/wiki_full/{i}.txt',encoding='utf-8').read();ov=e.get('overview','');add=[]
    for s in d.get('sentences',[]):
        x=s['text'].strip()
        ok=s['evidence'] in t and s['source'] in e['sources'] and all(y in s['evidence'] for y in re.findall(r'(?<!\d)(1[0-9]{3}|20[0-2]\d)(?!\d)',x) if not re.search(y+r'\s*(亿|万|项|个)',x))
        if not ok or x in ov: rej.append((i,x[:30]));continue
        add.append(x if x.endswith(('。','！','？')) else x+'。')
    if add:
        e['overview']=ov.rstrip()+''.join(add);tot+=len(add)
        s2=json.dumps(e,ensure_ascii=False,indent=2)+'\n';open(p,'w',encoding='utf-8',newline='').write(s2.replace('\n','\r\n') if crlf else s2)
print('added',tot);print('rejected',rej)
