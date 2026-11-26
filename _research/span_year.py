# 统一规则：display 为“A—B年”跨度时，year 取起点年 A（同年内月份跨度除外）
import json,glob,re
ch=[]
for f in sorted(glob.glob('data/entries/*.json')):
    raw=open(f,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw);mod=False
    for x in e.get('timeline') or []:
        m=re.fullmatch(r'(\d{3,4})\s*[—–]\s*(\d{2,4})年(代)?',x.get('display','').strip())
        if not m or not isinstance(x.get('year'),int): continue
        a=int(m.group(1))
        if x['year']!=a: ch.append((e['id'],x['year'],a,x['display']));x['year']=a;mod=True
    if mod:
        e['timeline'].sort(key=lambda x:x['year'] if isinstance(x.get('year'),int) else 0)
        s=json.dumps(e,ensure_ascii=False,indent=2)+'\n';open(f,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s)
for c in ch: print(*c)
print(len(ch))
