# Reinhart-Rogoff 全球危机数据（HBS, 2016-09-23 版）：按国家-年份取 银行危机/货币危机/外债违约 标记
# 对 chronology_lv.json 中的同一批案例，列出本库时间段(±1年)内被标记为危机的年份
import openpyxl, json
ws=openpyxl.load_workbook('_research/external/rr_global.xlsx',read_only=True)['Sheet1']
it=ws.iter_rows(values_only=True); next(it); next(it)
RR={}
def flag(v):
    try: return float(v)>=1
    except: return False
for r in it:
    c,y=r[2],r[3]
    if not c or not isinstance(y,(int,float)): continue
    d=RR.setdefault(c,{'银行危机':[],'货币危机':[],'外债违约':[]})
    if flag(r[4]): d['银行危机'].append(int(y))
    if flag(r[25]): d['货币危机'].append(int(y))
    if flag(r[18]): d['外债违约'].append(int(y))
ch=json.load(open('data/chronology_lv.json',encoding='utf-8'))
TYPE={'银行':'银行危机','货币':'货币危机','债务':'外债违约','泡沫':'银行危机'}
n=0
for row in ch['rows']:
    c=row['country']
    if c not in RR: row['rr']=None; continue
    a,b=row['our_span']
    row['rr']={k:[y for y in v if a-1<=y<=b+1] for k,v in RR[c].items()}
    t=TYPE[row['our_type']]
    row['rr_status']='一致' if any(a<=y<=b for y in row['rr'][t]) else ('相差1年' if row['rr'][t] else '未标记')
    n+=1
ch['source2']='org-hbs-rr-global'
ch['note2']='Reinhart–Rogoff 数据为国家-年份 0/1 标记；本页列出本库时间段前后各 1 年内被标记的年份'
json.dump(ch,open('data/chronology_lv.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
import collections
print(n,collections.Counter(r.get('rr_status') for r in ch['rows']))
for r in ch['rows']:
    if r.get('rr') is not None: print(r['id'],r['our_span'],r['our_type'],r['rr_status'],{k:v for k,v in r['rr'].items() if v})
p='data/sources.json';s=json.load(open(p,encoding='utf-8'))
if not any(x['id']=='org-hbs-rr-global' for x in s['sources']):
    s['sources'].append({'id':'org-hbs-rr-global','title':'Global Crises Data by Country (Reinhart–Rogoff, Behavioral Finance & Financial Stability, 2016-09-23 data file)','author':'Carmen M. Reinhart; Kenneth S. Rogoff; Harvard Business School BFFS','year':'2016','type':'官方机构','url':'https://www.hbs.edu/faculty/initiatives/behavioral-finance-and-financial-stability/Pages/global.aspx','url2':'https://www.hbs.edu/behavioral-finance-and-financial-stability/Documents/ChartData/MapCharts/20160923_global_crisis_data.xlsx','verified':True,'note':'2026-11-25 经代理下载 xlsx（1634548字节，70国，1800–2016）核对；取 Banking Crisis / Currency Crises / Sovereign External Debt 1 三列','link_ok':True})
    s['count']=len(s['sources'])
    open(p,'w',encoding='utf-8').write(json.dumps(s,ensure_ascii=False,indent=2)+'\n')
print('sources',s['count'])
