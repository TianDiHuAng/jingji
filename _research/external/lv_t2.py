# 解析 LV2018 Table 2（危机处置与结果），仅取单行完整的记录（10 个数值齐全）
import re,json
t=open('_research/external/lv2018.txt',encoding='utf-8').read()
i=t.find('Table 2. Banking Crises Resolution');j=t.find('Table 3. Banking Crisis Policy')
K=['output_loss','fiscal_gross','fiscal_net','fiscal_assets','liq_peak','liq_support','npl_peak','debt_increase']
rows=[];bad=0
for l in t[i:j].split('\n'):
    l=re.sub(r'\b\d\s*/\s*',' ',l.strip())   # 去脚注 "7 /" "8/"
    m=re.match(r'^([A-Z][^\d]*?)\s+((?:19|20)\d\d)\s+((?:19|20)\d\d)\s+(.*)$',l)
    if not m: continue
    v=re.findall(r'-?\d+(?:\.\d+)?|\.\.\.|…',m.group(4))
    if len(v)!=8: bad+=1;continue
    rows.append(dict(country=m.group(1).strip(),start=int(m.group(2)),end=int(m.group(3)),**{k:(None if x in('...','…') else float(x)) for k,x in zip(K,v)}))
json.dump(rows,open('_research/external/lv2018_table2.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
print(len(rows),'skipped',bad)
for r in rows:
    if r['country'] in('Argentina','Chile','Thailand','Korea','Indonesia','Iceland','Ireland','Sweden','Finland','Norway','Japan','United States','United Kingdom','Spain','Mexico','Turkey','Uruguay','Cyprus','Greece','Austria'): print(r)
