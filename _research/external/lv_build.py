# 生成 data/chronology_lv.json：本库案例时间段 vs Laeven-Valencia(2018) 同类型危机起始年
# 只记录原表年份与本库时间线年份，判定规则机械化，不做解释
import json
cmp=json.load(open('_research/external/lv_compare.json',encoding='utf-8'))
COL={'银行':'banking','货币':'currency','债务':'sovereign','泡沫':'banking'}
ZH={'banking':'银行危机','currency':'货币危机','sovereign':'主权债务危机'}
out=[]
for o in cmp:
    col=COL.get(o['type'],'banking'); a,b=o['span']
    ys=o['lv'].get(col,[])
    inside=[y for y in ys if a-1<=y<=b+1]
    if inside: st='一致' if any(a<=y<=b for y in inside) else '相差1年'
    elif ys: st='该类型年份不同'
    else: st='LV未列该类型'
    other={ZH.get(k,k):v for k,v in o['lv'].items() if k!=col and k in ZH and v and any(a-1<=y<=b+1 for y in v)}
    out.append(dict(id=o['id'],country=o['country'],our_type=o['type'],lv_type=ZH[col],our_span=[a,b],lv_years=ys,status=st,lv_other_in_span=other))
json.dump({'source':'org-imf-lv2018','table':'Table 1. Crisis Dates','note':'起始年按原表；本库时间段取条目时间线最早与最晚年份','rows':out},open('data/chronology_lv.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
import collections;print(collections.Counter(r['status'] for r in out))
for r in out:
    if r['status']!='一致': print(r['id'],r['our_span'],r['lv_type'],r['lv_years'],r['status'],r['lv_other_in_span'])
s=json.load(open('data/sources.json',encoding='utf-8'))
s['org-imf-lv2018']={"id":"org-imf-lv2018","title":"Systemic Banking Crises Revisited (IMF Working Paper WP/18/206)","author":"Luc Laeven; Fabian Valencia","year":"2018","type":"官方机构","url":"https://www.imf.org/-/media/files/publications/wp/2018/wp18206.pdf","url2":"https://www.elibrary.imf.org/view/journals/001/2018/206/article-A001-en.xml","verified":True,"note":"2026-11-25 经代理下载 PDF（48页，2611489字节）核对；附录 Table 1 Crisis Dates 按单词坐标解析","link_ok":True}
json.dump(s,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('sources',len(s))
