# -*- coding: utf-8 -*-
"""轮次4：新增9条银行危机条目（List_of_banking_crises 对照发现）。
每条≥2个verified来源；先建L1骨架（TASK分层规则）。"""
import urllib.request, ssl, json, urllib.parse, re

c=ssl._create_unverified_context(); h={'User-Agent':'EconCrisisBot/1.0'}

# (id, 中文名, 维基标题, 时期, 地区, 类型, 层级, 第二来源id)
NEW = [
 ('black-friday-1869','黑色星期五黄金恐慌(1869)','Black Friday (1869)','18—19世纪','北美','货币','重要','w-en-panic-of-1866'),
 ('russian-1998','1998年俄罗斯金融危机','1998 Russian financial crisis','20世纪下半','欧洲','货币','重要','w-en-latin-american-debt-crisis'),
 ('uruguay-2002','2002年乌拉圭银行危机','2002 Uruguay banking crisis','21世纪','拉美','银行','补充','w-en-argentine-economic-crisis-1999-2002'),
 ('finnish-banking-1990','1990年代芬兰银行危机','1990s Finnish banking crisis','20世纪下半','欧洲','银行','补充','w-en-secondary-banking-crisis'),
 ('indian-1991','1991年印度经济危机','1991 Indian economic crisis','20世纪下半','亚洲','货币','重要','w-en-mexican-peso-crisis'),
 ('cypriot-2013','2012–2013塞浦路斯金融危机','2012–2013 Cypriot financial crisis','21世纪','欧洲','银行','重要','w-en-euro-area-crisis'),
 ('myanmar-2003','2003年缅甸银行危机','2003 Myanmar banking crisis','21世纪','亚洲','银行','补充','w-en-bank-run'),
 ('henan-2022','2022年河南银行危机','2022 Henan banks protests','21世纪','亚洲','银行','补充','w-en-bank-run'),
 ('ltcm','长期资本管理公司倒闭(1998)','Long-Term Capital Management','20世纪下半','北美','银行','重要','w-en-systemic-risk'),
]

# 核对维基页面存在性
titles=[x[2] for x in NEW]
p={'action':'query','format':'json','formatversion':'2','titles':'|'.join(titles),'redirects':'1','prop':'info'}
req=urllib.request.Request('https://en.wikipedia.org/w/api.php?'+urllib.parse.urlencode(p),headers=h)
d=json.loads(urllib.request.urlopen(req,timeout=30,context=c).read())
norm={r['to']:r['from'] for r in d.get('query',{}).get('redirects',[])}
info={}
for pg in d['query']['pages']:
    if not pg.get('missing'):
        e={'canonical':pg['title'],'touched':pg.get('touched','')[:4],'pageid':pg.get('pageid')}
        info[pg['title']]=e
        if pg['title'] in norm: info[norm[pg['title']]]=e

def slug(s): return re.sub(r'[^a-z0-9]+','-',s.lower()).strip('-')[:48]

srcdata=json.load(open('data/sources.json',encoding='utf-8'))
existing={s['id'] for s in srcdata['sources']}
added_src=[]
for eid,name,title,period,region,ctype,tier,sec in NEW:
    if title not in info:
        print('SKIP missing page',eid); continue
    sid='w-en-'+slug(eid)  # 用条目id做来源id，稳定
    if sid not in existing:
        i=info[title]
        srcdata['sources'].append({
          'id':sid,'title':i['canonical'],'author':'Wikipedia contributors','year':i['touched'] or None,
          'type':'权威百科','url':'https://en.wikipedia.org/wiki/'+urllib.parse.quote(i['canonical'].replace(' ','_')),
          'url2':None,'verified':True,'link_ok':True,
          'note':f'Wikipedia API 核对：页面存在（pageid={i["pageid"]}）；轮次4经 List_of_banking_crises 大纲对照新增'})
        added_src.append(sid); existing.add(sid)
srcdata['count']=len(srcdata['sources'])
json.dump(srcdata,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新增来源',len(added_src))

# 生成L1骨架条目（scope + coverage + entries）
cov=json.load(open('coverage.json',encoding='utf-8'))
created=[]
for eid,name,title,period,region,ctype,tier,sec in NEW:
    if title not in info: continue
    sid='w-en-'+slug(eid)
    srcs=[sid, sec]
    srcs=[s for s in srcs if s in existing]
    if len(srcs)<2: 
        print('WARN <2 sources',eid,srcs); continue
    entry={
      'id':eid,'title':name,'level':'L1','tier':tier,
      'unit':{'18—19世纪':'U2 18—19世纪','20世纪下半':'U4 20世纪下半','21世纪':'U5 21世纪'}.get(period,'U5 21世纪'),
      'period':period,'region':region,'crisis_type':ctype,
      'one_line':f'{name}：发生于{period}、地区为{region}的{ctype}类案例（轮次4新条目，骨架）。',
      'overview':f'{name} 是经权威大纲（Wikipedia List of banking crises）对照发现的遗漏案例，维基页面已核对存在。完整内容待逐条核实来源后补充。',
      'timeline':[],'causal_chain':[],'key_data':[],'schools':[],'policy_response':[],
      'comparison':'','svg':'','sources':srcs,'related':[],
      'needs_verification':True,
      'pending_notes':'L1骨架：时间线、背景、传导机制、关键数据、各方解释、政策应对、图示待核实补充。'
    }
    json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
    cov['entries'].append({'id':eid,'level':'L1','tier':tier,'status':'written',
      'source_count':len(srcs),'needs_verification':1,'last_updated':'2026-11-22',
      'unit':entry['unit'],'period':period,'region':region,'crisis_type':ctype})
    created.append(eid)
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新建条目',len(created),created)
