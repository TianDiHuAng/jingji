# -*- coding: utf-8 -*-
"""根据REST摘要升级6条L1补充条目到L2（真实事实,不编造）。"""
import json
def svg(title,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：机制示意</text>"]
    for x,t in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(t)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

# eid: (source_id, timeline[(year,display,event)], causal[(step,src)], schools[(holder,view,src)], comparison)
D={
 'panic-1847':('w-en-panic-of-1847',
   [(1847,'1847年3月','英国政府宣布举债以资助爱尔兰大饥荒救济，成为危机诱因（据 Wikipedia Panic of 1847）'),
    (1847,'1840年代末','与铁路热潮结束、商人破产相关联；酿成重大商业与银行危机（同上）')],
   [('政府为救济爱尔兰大饥荒举债 + 铁路热潮见顶 → 市场与信贷承压','w-en-panic-of-1847'),
    ('商人破产与银行收紧 → 重大商业与银行危机','w-en-panic-of-1847'),
    ('经济与金融受创','w-en-panic-of-1847')],
   [('政策/外部冲击视角','饥荒救济举债与铁路热潮退潮共同触发','w-en-panic-of-1847'),('信贷周期视角','信贷扩张后收缩放大危机','w-en-business-cycle')],
   '与1825、1866年英国危机同属19世纪商业/银行恐慌；诱因各有不同。具体异同待核实。'),
 'panic-1866':('w-en-panic-of-1866',
   [(1866,'1866年','伦敦主要批发贴现银行 Overend, Gurney and Company 倒闭，引发重大金融危机（据 Wikipedia Panic of 1866）')],
   [('Overend, Gurney 倒闭 → 批发贴现市场信心崩塌','w-en-panic-of-1866'),
    ('恐慌蔓延、信贷紧缩 → 银行业承压','w-en-panic-of-1866'),
    ('重大金融危机（英国）','w-en-panic-of-1866')],
   [('机构失败视角','大型贴现银行倒闭触发恐慌','w-en-panic-of-1866'),('最后贷款人视角','危机凸显央行流动性支持的必要(待核实)','w-en-lender-of-last-resort')],
   '与1847、1857等英国危机同属19世纪银行恐慌；具体异同待核实。'),
 'panic-1901':('w-en-panic-of-1901',
   [(1901,'1901年','纽约证券交易所首次股市崩盘（据 Wikipedia Panic of 1901）'),
    (1901,'1901年','源于争夺北太平洋铁路控制权的多方角力(Harriman/Schiff/Morgan/Hill)与逼空（同上）')],
   [('Harriman/Schiff/Morgan/Hill 争夺北太平洋铁路控制权 → 抢筹逼空','w-en-panic-of-1901'),
    ('股价剧烈波动 → 纽约证交所首次股市崩盘','w-en-panic-of-1901'),
    ('市场信心受创','w-en-panic-of-1901')],
   [('金融资本角力视角','铁路控制权之争引发逼空与崩盘','w-en-panic-of-1901'),('市场结构视角','凸显当时纽交所市场脆弱性','w-en-financial-crisis')],
   '与1907年恐慌同为美国早期股市/金融危机；具体异同待核实。'),
 'paris-bourse-1882':('w-en-paris-bourse-crash-of-1882',
   [(1882,'1882年1月','l\'Union Générale 银行倒闭，引发巴黎证交所崩盘（据 Wikipedia Paris Bourse crash of 1882）'),
    (1882,'1882年','约四分之一经纪商濒临破产；为19世纪法国最严重危机（同上）')],
   [('l\'Union Générale 倒闭 → 巴黎证交所恐慌','w-en-paris-bourse-crash-of-1882'),
    ('约1/4经纪商濒临破产 → 市场与融资受创','w-en-paris-bourse-crash-of-1882'),
    ('19世纪法国最严重经济危机','w-en-paris-bourse-crash-of-1882')],
   [('机构失败视角','一家大银行倒闭触发交易所崩盘','w-en-paris-bourse-crash-of-1882'),('投机/泡沫视角','前期投机积累脆弱性','w-en-speculative-bubble')],
   '与1882同期美国等市场波动相关；为法国19世纪最严重危机。具体异同待核实。'),
 'uk-secondary-banking-1973':('w-en-secondary-banking-crisis',
   [(1973,'1973—1975年','英国房价剧烈下跌，数十家小型"二级"放贷银行濒临破产（据 Wikipedia Secondary banking crisis of 1973–1975）')],
   [('英国房价剧烈下跌 → 抵押品贬值、二级银行承压','w-en-secondary-banking-crisis'),
    ('数十家小型二级银行濒临破产','w-en-secondary-banking-crisis'),
    ('触发对银行业的救助(待核实)','w-en-lender-of-last-resort')],
   [('房地产/抵押品视角','房价下跌冲击以地产为抵押的小银行','w-en-secondary-banking-crisis'),('监管/救助视角','需央行协调救助(待核实)','w-en-lender-of-last-resort')],
   '与同期英国房地产与银行业压力相关；具体异同待核实。'),
 'rhode-island-banking-1990':('w-en-rhode-island-banking-crisis',
   [(1990,'1990年代初','普罗维登斯 Heritage Loan & Investment 因长期挪用而倒闭，引发罗得岛银行危机（据 Wikipedia Rhode Island banking crisis）'),
    (1990,'1990年代初','约三分之一罗得岛居民一度无法动用其银行存款（同上）')],
   [('Heritage Loan & Investment 长期挪用 → 银行倒闭','w-en-rhode-island-banking-crisis'),
    ('存款人无法取款 → 挤兑与存款保险基金压力','w-en-rhode-island-banking-crisis'),
    ('约1/3州民一度失去存款使用权','w-en-rhode-island-banking-crisis')],
   [('欺诈/治理视角','长期挪用导致机构倒闭','w-en-rhode-island-banking-crisis'),('存款保险视角','凸显存款保险与监管的重要性','w-en-deposit-insurance')],
   '与储贷危机同期美国银行业问题相关；具体异同待核实。'),
}
for eid,(sid,tl,causal,schools,cmp) in D.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'
    have={t.get('display') for t in d.get('timeline',[])}
    for y,disp,ev in tl:
        if disp not in have: d.setdefault('timeline',[]).append({'year':y,'display':disp,'event':ev,'sources':[sid]})
    d['timeline'].sort(key=lambda t:t.get('year',0))
    d['causal_chain']=[{'step':s,'sources':[src]} for s,src in causal]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基摘要归纳；具体表述待核实','sources':[src]} for h,v,src in schools]
    d['policy_response']=[{'holder':'政策当局','view':'应对措施及效果待核实','basis':'需多来源印证','sources':[d['sources'][0]]}]
    d['comparison']=cmp
    if not d.get('svg'): d['svg']=svg(d['title'],[tl[0][2][:12],'传导','后果'])
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【续作】升L2(据REST摘要)。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'->L2')
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in D: e['level']='L2'; e['last_updated']='2026-11-23'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage synced')
