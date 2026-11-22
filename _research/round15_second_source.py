# -*- coding: utf-8 -*-
"""轮次15 方法5：为2条核心数值补多语言维基第二来源（de/es，已实证上下文）。"""
import json
sd=json.load(open('data/sources.json',encoding='utf-8'))
existing={x['id'] for x in sd['sources']}
def add(sid,title,lang,slug,pid,note):
    if sid in existing: return
    sd['sources'].append({'id':sid,'title':title,'author':'Wikipedia contributors' if lang!='zh' else '维基百科贡献者',
      'year':'2026','type':'权威百科','url':f'https://{lang}.wikipedia.org/wiki/{slug}','url2':None,
      'verified':True,'link_ok':True,'note':note+'(pageid=%s)'%pid})
    existing.add(sid)
add('w-de-schwarzer-montag','Schwarzer Montag','de','Schwarzer_Montag',616732,
    '德语维基API核对；轮次15二源：原文"Der Dow Jones fiel innerhalb eines Tages um 22,6 % (508 Punkte)"')
add('w-es-rodrigazo','Rodrigazo','es','Rodrigazo',250391,
    '西语维基API核对；轮次15二源：原文"la tasa de inflación pasó del 24,4 % en 1974 al 182,4 % en 1975 y 444 % en 1976"')
sd['count']=len(sd['sources'])
json.dump(sd,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('来源库',len(sd['sources']))

# black-monday 22.6%
f='data/entries/black-monday-1987.json'; d=json.load(open(f,encoding='utf-8'))
for kd in d['key_data']:
    if kd['label']=='道指单日跌幅(1987-10-19)':
        if 'w-de-schwarzer-montag' not in kd['sources']: kd['sources'].append('w-de-schwarzer-montag')
        kd['note']=kd['note'].replace('单一来源待核实。','【双源印证】德语维基《Schwarzer Montag》原文"Dow Jones ... 22,6 % (508 Punkte)"，一致。')
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('black-monday 道指22.6% 双源')

# rodrigazo 444%
f='data/entries/rodrigazo-1975.json'; d=json.load(open(f,encoding='utf-8'))
for kd in d['key_data']:
    if kd['label']=='通胀率(1976年)':
        if 'w-es-rodrigazo' not in kd['sources']: kd['sources'].append('w-es-rodrigazo')
        kd['note']=kd['note'].replace('单一来源待核实。','【双源印证】西语维基《Rodrigazo》原文"24,4% en 1974 al 182,4% en 1975 y 444% en 1976"，一致（并验证444%属1976年）。')
json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('rodrigazo 444%(1976) 双源')
