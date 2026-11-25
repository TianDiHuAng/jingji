# 用 Reinhart-Rogoff 年通胀率（年均 CPI 变动）对照已有年度通胀 key_data：只在同国同年、同为年度通胀时并列
import json
R=json.load(open('_research/external/rr_infl.json'))
T=[('sterling-crisis-1976','英国通胀率(1975)','United Kingdom',1975,'ok'),
   ('stock-crash-1973','美国CPI通胀率(1974)','United States',1974,'diff'),
   ('rodrigazo-1975','通胀率(1976年)','Argentina',1976,'diff'),
   ('mexican-peso-1994','墨西哥通胀(危机期)','Mexico',1995,'diff'),
   ('venezuela-hyper-2016','委内瑞拉通胀率(2014)','Venezuela',2014,'ok'),
   ('venezuela-hyper-2016','委内瑞拉通胀率(2015)','Venezuela',2015,'diff'),
   ('venezuela-hyper-2016','委内瑞拉通胀率(2016)','Venezuela',2016,'diff')]
SID='org-hbs-rr-global';done=[]
for eid,lab,c,y,kind in T:
    p=f'data/entries/{eid}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw
    e=json.loads(raw);k=[x for x in e['key_data'] if x['label']==lab][0]
    if SID in k['sources']: continue
    v=round(R[f'{c}|{y}'],1)
    if kind=='ok':
        add=f' Reinhart–Rogoff 全球危机数据（年均CPI变动）{c} {y} 为 {v}%，与本行数值相近，构成统计口径对照印证（两者口径未必完全相同）。'
    else:
        add=f' Reinhart–Rogoff 全球危机数据（年均CPI变动）{c} {y} 为 {v}%，与本行 {k["value"]}% 口径不同（本行可能为年末同比或其他统计口径），两数并列，不作取舍。'
    k['note']=(k.get('note') or '')+add;k['sources'].append(SID)
    if SID not in e['sources']: e['sources'].append(SID)
    s=json.dumps(e,ensure_ascii=False,indent=2)+'\n'
    open(p,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s);done.append((eid,lab,k['value'],v,kind))
for d in done: print(*d)
