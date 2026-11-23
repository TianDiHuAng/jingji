# -*- coding: utf-8 -*-
"""离线补建 2020 新冠股灾（用本会话已成功抓取的REST摘要文本，页面已确认存在）。"""
import json
EX1="On 20 February 2020, stock markets across the world suddenly crashed after growing instability due to the COVID-19 pandemic. The crash ended on 7 April 2020."
EX2="The COVID-19 recession was a global economic recession caused by COVID-19 lockdowns. The recession began in most countries in February 2020. After a year of global economic slowdown that saw stagnation of economic growth and consumer activity, the COVID-19 lockdowns and other precautions taken in early 2020 drove the global economy into crisis. Within seven months, every advanced economy had fallen into recession."

sd=json.load(open('data/sources.json',encoding='utf-8')); existing={x['id'] for x in sd['sources']}
def addsrc(sid,title,slug,ex):
    if sid in existing: return
    sd['sources'].append({'id':sid,'title':title,'author':'Wikipedia contributors','year':'2026','type':'权威百科',
      'url':'https://en.wikipedia.org/wiki/'+slug,'url2':None,'verified':True,'link_ok':True,
      'note':'Wikipedia REST API核对(本会话成功抓取)；摘要:"%s"'%ex[:60]})
    existing.add(sid)
addsrc('w-en-2020-stock-market-crash','2020 stock market crash','2020_stock_market_crash',EX1)
addsrc('w-en-covid-19-recession','COVID-19 recession','COVID-19_recession',EX2)
sd['count']=len(sd['sources']); json.dump(sd,open('data/sources.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)

def svg(title,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:22]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：机制示意</text>"]
    for x,t in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(t)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

eid='covid-crash-2020'
entry={'id':eid,'title':'2020年新冠股灾','level':'L2','tier':'重要','unit':'U5 21世纪','period':'21世纪','region':'全球','crisis_type':'泡沫',
 'one_line':'2020年2月20日新冠疫情引发全球股市突然暴跌，至4月7日结束，并演变为全球性经济衰退。',
 'overview':'2020年2月20日，因新冠疫情带来的不确定性加剧，全球股市突然暴跌，此轮崩盘于2020年4月7日结束（据 Wikipedia 2020 stock market crash）。疫情封锁举措随后将全球经济推入衰退：多数国家自2020年2月开始衰退，七个月内所有发达经济体均陷入衰退（据 Wikipedia COVID-19 recession）。这是一次典型的外生冲击型危机。具体点位/跌幅与政策规模待核实。',
 'timeline':[
   {'year':2020,'display':'2020年2月20日','event':'新冠疫情不确定性加剧，全球股市突然暴跌（据 Wikipedia 2020 stock market crash）','sources':['w-en-2020-stock-market-crash']},
   {'year':2020,'display':'2020年2月起','event':'多数国家经济因封锁开始衰退；七个月内所有发达经济体陷入衰退（据 Wikipedia COVID-19 recession）','sources':['w-en-covid-19-recession']},
   {'year':2020,'display':'2020年4月7日','event':'股市崩盘阶段结束（同上）','sources':['w-en-2020-stock-market-crash']}],
 'causal_chain':[
   {'step':'新冠疫情暴发与封锁 → 需求骤降、供应链中断、极端不确定性','sources':['w-en-covid-19-recession']},
   {'step':'恐慌性抛售 → 2020年2月20日全球股市突然暴跌','sources':['w-en-2020-stock-market-crash']},
   {'step':'经济活动骤停 → 全球衰退，七个月内发达经济体全部陷入衰退','sources':['w-en-covid-19-recession']}],
 'key_data':[],
 'schools':[
   {'holder':'外生冲击视角','view':'危机源于疫情这一外生公共卫生冲击，而非内生金融失衡','basis':'据维基COVID-19 recession主题归纳；待核实','sources':['w-en-covid-19-recession']},
   {'holder':'政策应对视角','view':'大规模财政货币救助缓解了冲击、缩短了市场崩盘阶段','basis':'规模待核实','sources':['w-en-2020-stock-market-crash']}],
 'policy_response':[{'holder':'各国政府与央行','view':'大规模财政与货币支持；具体规模与效果待核实','basis':'需多来源印证','sources':['w-en-covid-19-recession']}],
 'comparison':'与2008次贷(内生金融失衡)不同，2020新冠股灾主要源于外生公共卫生冲击；市场崩盘阶段(约7周)相对较短。具体异同待核实。',
 'svg':svg('2020年新冠股灾',['疫情+封锁','恐慌抛售','衰退(2-4月)']),
 'sources':['w-en-2020-stock-market-crash','w-en-covid-19-recession','w-en-financial-crisis'],
 'related':['subprime-crisis-2007','great-depression','bankruptcy-ftx'],'needs_verification':True,
 'pending_notes':'L2：时间线与疫情衰退机制据REST摘要；具体股指跌幅、熔断次数、政策规模(财政/货币)待核实补充。'}
json.dump(entry,open('data/entries/'+eid+'.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
cov=json.load(open('coverage.json',encoding='utf-8'))
cov['entries'].append({'id':eid,'level':'L2','tier':'重要','status':'written','source_count':3,'needs_verification':1,'last_updated':'2026-11-23','unit':'U5 21世纪','period':'21世纪','region':'全球','crisis_type':'泡沫'})
cov['total']=len(cov['entries'])
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('新增 covid-crash-2020; 来源',len(sd['sources']),'条目',cov['total'])
