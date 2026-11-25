# 用 PyMuPDF 单词坐标解析 Laeven-Valencia(2018) Table 1（P31-P34）
# 列边界按实测横坐标：banking<262, currency<410, sovereign<482, 其后为 restructuring
# 多行单元格：每个年份词归到纵坐标最近的国家名行
import fitz, json, re
doc=fitz.open('_research/external/lv2018.pdf')
B=[(262,'banking'),(410,'currency'),(482,'sovereign'),(9999,'restructuring')]
rows={}
for pn in range(30,34):
    ws=doc[pn].get_text('words')
    hy=[w[1] for w in ws if w[4]=='Banking'][0]
    body=[w for w in ws if w[1]>hy+2 and w[1]<760]
    # 国家名：左列(x<185)的词，按行合并
    nl={}
    for w in body:
        if w[0]<185 and not re.fullmatch(r'[\d,]+',w[4]):
            nl.setdefault(round(w[1]),[]).append(w)
    names=[]
    for y in sorted(nl):
        txt=' '.join(w[4] for w in sorted(nl[y],key=lambda w:w[0]))
        if names and (txt[0].islower() or txt in('Kong','Rep.','Herzegovina','Republic','Rep','Nevis','Tobago','Principe','Grenadines','of') or names[-1][1].split()[-1] in ('Hong','and','Dem.','African','Dominican','Equatorial','Kong:')) and y-names[-1][2]<14:
            names[-1]=(names[-1][0],names[-1][1]+' '+txt,y)
        else:
            names.append((y,txt,y))
    for _,n,_ in names: rows.setdefault(n,{c:[] for _,c in B})
    for w in body:
        if w[0]<185: continue
        ys=re.findall(r'(19\d\d|20[01]\d)',w[4])
        if not ys: continue
        n=min(names,key=lambda t:min(abs(w[1]-t[0]),abs(w[1]-t[2])))[1]
        col=[c for x,c in B if w[0]<x][0]
        rows[n][col]+=[int(y) for y in ys]
for v in rows.values():
    for c in v: v[c]=sorted(set(v[c]))
json.dump(rows,open('_research/external/lv2018_table1.json','w',encoding='utf-8'),ensure_ascii=False,indent=0)
for c in ['Albania','Algeria','Angola','Argentina','Thailand','United Kingdom','United States','Turkey','Venezuela','Ghana','Zambia','Myanmar','Greece','Uruguay','Russia','Mexico','Chile']:
    print(c,rows.get(c))
print(len(rows))
