# -*- coding: utf-8 -*-
"""轮次5：L2-important-deepen — 为3条重要条目补入来源核实的timeline节点。
日期直接来自已抓取的 Wikipedia 正文，注明来源；保持L2层级（TASK: L3只给核心）。"""
import json

TL = {
 'panic-1907': [
   {'year':1906,'display':'1906年1月','event':'道琼斯工业平均指数见顶103点，随后开始调整（据 Wikipedia Panic of 1907）','sources':['w-en-panic-of-1907']},
   {'year':1906,'display':'1906年4月','event':'旧金山地震加剧市场不稳定（同上）','sources':['w-en-panic-of-1907']},
   {'year':1907,'display':'1907年10月','event':'联合铜业公司股票逼空失败触发危机，纽约证交所较前一年峰值跌近50%（同上）','sources':['w-en-panic-of-1907']},
   {'year':1907,'display':'1907年11月','event':'金融传染基本结束，但随后因紧急融资再度紧张（同上）','sources':['w-en-panic-of-1907']},
 ],
 'mexican-peso-1994': [
   {'year':1994,'display':'1994年1月1日','event':'北美自由贸易协定(NAFTA)生效，墨西哥政府与企业获得新的外资渠道（据 Wikipedia Mexican peso crisis）','sources':['w-en-mexican-peso-crisis']},
   {'year':1994,'display':'1994年3月','event':'总统候选人科洛西奥在蒂华纳遇刺，市场风险溢价上升（同上）','sources':['w-en-mexican-peso-crisis']},
   {'year':1994,'display':'1994年12月下旬','event':'墨西哥央行让比索贬值，外资恐慌导致风险溢价进一步上升（同上）','sources':['w-en-mexican-peso-crisis']},
   {'year':1995,'display':'1995年1月','event':'美国组织500亿美元救助，由IMF管理（同上）','sources':['w-en-mexican-peso-crisis']},
 ],
 'black-wednesday-1992': [
   {'year':1990,'display':'1990年10月8日','event':'英国以1英镑兑2.95德国马克的汇率加入ERM（据 Wikipedia Black Wednesday）','sources':['w-en-black-wednesday']},
   {'year':1992,'display':'1992年春','event':'丹麦公投否决马斯特里赫特条约，欧洲汇率机制承压（同上）','sources':['w-en-black-wednesday']},
   {'year':1992,'display':'1992年9月15日晚','event':'媒体已传出英镑将受攻击的消息（同上）','sources':['w-en-black-wednesday']},
   {'year':1992,'display':'1992年9月16日','event':'交易员大规模抛售英镑，英国政府退出ERM（即"黑色星期三"）（同上）','sources':['w-en-black-wednesday']},
 ],
}

for eid, rows in TL.items():
    f='data/entries/'+eid+'.json'
    d=json.load(open(f,encoding='utf-8'))
    have={(t.get('display'),t.get('year')) for t in d.get('timeline',[])}
    added=0
    for r in rows:
        if (r['display'],r['year']) in have: continue
        d.setdefault('timeline',[]).append(r); added+=1
    d['timeline'].sort(key=lambda t:t.get('year',0))
    if added:
        d['needs_verification']=True
        d['pending_notes']=d.get('pending_notes','')+' 【轮次5时间线深化】补入单源日期节点，待第二来源核实。'
        json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
        print(eid,'补入',added,'个时间节点')
