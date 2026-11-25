# 用 LV2018 Table 2 为银行危机案例新增 key_data（产出损失、总财政成本、不良贷款峰值），来源 org-imf-lv2018
# 仅当案例时间段覆盖该危机起始年；不改动已有数据；与已有同类数字差异只在 note 中并列
import json,glob
lv=json.load(open('_research/external/lv2018_table2.json',encoding='utf-8'))
ch={r['id']:r for r in json.load(open('data/chronology_lv.json',encoding='utf-8'))['rows']}
F=[('output_loss','产出损失(LV2018)','%（占趋势GDP，累计）'),('fiscal_gross','银行危机总财政成本(LV2018)','%（占GDP）'),('npl_peak','不良贷款峰值(LV2018)','%（占贷款总额）')]
CMP={'swedish-crisis-1990s':'本条目另载救助初始成本约占GDP 4%、净成本0—2%（维基）；与LV总财政成本3.6%、净成本0.2%口径不同，并列不作取舍。',
     'finnish-banking-1990':'本条目另载纳税人成本约占GNP 8%（维基）；LV按GDP计总财政成本12.8%、净11.1%，口径不同，并列不作取舍。'}
n=0;touched=[]
for f in sorted(glob.glob('data/entries/*.json')):
    e=json.load(open(f,encoding='utf-8'));r=ch.get(e['id'])
    if not r or r['our_type'] not in('银行','泡沫','债务','货币'): continue
    a,b=r['our_span']
    rows=[x for x in lv if x['country']==r['country'] and a-1<=x['start']<=b]
    if len(rows)!=1: continue
    x=rows[0];kd=e.setdefault('key_data',[])
    if any('LV2018' in str(k.get('label')) for k in kd): continue
    add=0
    for key,lab,unit in F:
        if x[key] is None: continue
        note=f'Laeven–Valencia(2018) Table 2：{r["country"]} {x["start"]}–{x["end"]} 银行危机，{key}={x[key]}。'
        if key=='fiscal_gross' and e['id'] in CMP: note+=CMP[e['id']]
        note+='单一来源（IMF 数据库，独立于维基）。'
        kd.append({'label':f'{lab}·{r["country"]} {x["start"]}','value':x[key],'unit':unit,'year':x['start'],'comparable_price':False,'note':note,'sources':['org-imf-lv2018']})
        add+=1
    if add:
        if 'org-imf-lv2018' not in e['sources']: e['sources'].append('org-imf-lv2018')
        open(f,'w',encoding='utf-8').write(json.dumps(e,ensure_ascii=False,indent=2)+'\n');n+=add;touched.append(e['id'])
print(n,len(touched),touched)
