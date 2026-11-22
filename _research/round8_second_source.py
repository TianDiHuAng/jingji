# -*- coding: utf-8 -*-
"""轮次8：第3次单源核查发现法语维基第二来源，补入。"""
import json
sd=json.load(open('data/sources.json',encoding='utf-8'))
sid='w-fr-krach-1929'
note='法语维基API核对(pageid=81594)；轮次8第3次核查发现第二来源：原文 Les volumes échangés atteignent 12,9 millions d’actions 印证黑色星期四成交量'
if sid not in {x['id'] for x in sd['sources']}:
    sd['sources'].append({'id':sid,'title':'Krach de 1929','author':'Wikipédia contributors','year':'2026',
      'type':'权威百科','url':'https://fr.wikipedia.org/wiki/Krach_de_1929','url2':None,
      'verified':True,'link_ok':True,'note':note})
    sd['count']=len(sd['sources'])
    json.dump(sd,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('新增',sid,len(sd['sources']))
f='data/entries/wall-street-1929.json'; d=json.load(open(f,encoding='utf-8'))
for kd in d['key_data']:
    if kd['label']=='黑色星期四成交量':
        if sid not in kd['sources']: kd['sources'].append(sid)
        kd['note']=kd['note'].replace('单源待核实。','【双源印证】法语维基《Krach de 1929》原文「12,9 millions d’actions」，与英文来源一致。')
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('wall-street-1929 黑色星期四已双源')
