# -*- coding: utf-8 -*-
"""轮次14：2条核心遗漏升L3（1997亚洲金融危机/银行挤兑），维基原文实证。"""
import json
def deep_svg(title,ct):
    e=lambda s:s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:26]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 780 280' role='img'>",
       f"<text x='20' y='26' class='ttl'>{e(title)}：机制与反馈回路（{ct}）</text>"]
    for x,t,sub in [(30,'触发条件','冲击/失衡'),(215,'放大机制','预期/杠杆'),(400,'临界转折','信心逆转'),(585,'后果与应对','危机/政策')]:
        s.append(f"<g><rect x='{x}' y='60' width='160' height='52' rx='6' class='box'/><text x='{x+9}' y='83' class='lbl'>{t}</text><text x='{x+9}' y='101' class='sub'>{sub}</text></g>")
    for a,b in [(190,215),(375,400),(560,585)]: s.append(f"<line x1='{a}' y1='86' x2='{b}' y2='86' class='ar'/>")
    s.append("<path d='M665 112 L665 170 L295 170 L295 112' fill='none' class='ar' style='stroke-dasharray:5,4'/>")
    s.append("<text x='400' y='163' class='sub'>反馈：后果强化放大机制</text>")
    s.append("<text x='20' y='230' class='note'>框架来源见本页来源列表；具体数值以正文为准。</text></svg>")
    return ''.join(s)
def chain_schools(ct):
    if ct=='货币':
        return ([('固定汇率+资本流入 → 本币高估与外债累积','w-en-currency-crisis'),
                 ('外汇抛售/热钱逆转 → 贬值预期','w-en-currency-devaluation'),
                 ('放弃钉住/IMF救助 → 货币贬值与经济收缩','w-en-monetary-policy')],
                [('货币主义视角','危机源于汇率制度与货币政策失当','w-en-monetary-policy'),
                 ('传染视角','强调资本流动与市场预期的区域传导','w-en-financial-contagion')])
    return ([('负面信息/信心动摇 → 存款人集中提款','w-en-bank-run'),
             ('挤兑自我实现 → 健康银行亦受牵连','w-en-systemic-risk'),
             ('信贷收缩 → 实体经济融资中断','w-en-credit-crunch')],
            [('挤兑均衡视角','挤兑可视为协调博弈的坏均衡','w-en-bank-run'),
             ('系统性风险视角','强调机构关联与传染','w-en-systemic-risk')])
DATA={
 'asian-financial-crisis-1997':{
  'tl':[
   {'year':1993,'display':'1993–1996年','event':'东盟四国外债/GDP比从100%升至167%，危机时超180%（据 Wikipedia 1997 Asian financial crisis）','sources':['w-en-asian-financial-crisis']},
   {'year':1997,'display':'1997年7月','event':'危机始于泰国，随后波及多国，引发对全球金融传染的担忧（同上）','sources':['w-en-asian-financial-crisis']},
   {'year':1998,'display':'1998年','event':'菲律宾经济增长降至近零；韩国、印尼、泰国受创最重（同上）','sources':['w-en-asian-financial-crisis']},
   {'year':1999,'display':'1998–1999年','event':'经济快速复苏，全球崩溃担忧消退（同上）','sources':['w-en-asian-financial-crisis']},
  ],
  'kd':[
   {'label':'东盟四国外债/GDP(1993→1996)','value':167,'unit':'%（东盟四大经济体，外债/GDP，1996年；起点1993年100%）','year':1996,'comparable_price':False,
    'note':'原文：foreign debt-to-GDP ratios rose from 100% to 167% ... in 1993–1996；单一来源待核实。','sources':['w-en-asian-financial-crisis']},
  ],
 },
 'bank-run':{
  'tl':[
   {'year':1931,'display':'1931年6—12月','event':'大萧条期间波士顿、芝加哥、托莱多等城市爆发全城性挤兑（据 Wikipedia Bank run）','sources':['w-en-bank-run']},
   {'year':2008,'display':'2008年','event':'金融危机以类似银行挤兑的市场流动性失效为中心（同上）','sources':['w-en-bank-run']},
   {'year':2023,'display':'2023年3月','event':'硅谷银行客户一天内提取420亿美元（近总存款1/4），为网络时代挤兑实例（同上）','sources':['w-en-bank-run']},
  ],
  'kd':[
   {'label':'系统性银行危机清理财政成本','value':13,'unit':'%GDP（1970年后重要危机的财政成本均值）','year':2020,'comparable_price':False,
    'note':'原文：fiscal costs averaging 13% of GDP ... for important crises from 1970（统计区间均值，year列为整理年）；单一来源待核实。','sources':['w-en-bank-run']},
   {'label':'硅谷银行单日提款(2023-03)','value':42,'unit':'十亿美元（美元，SVB单日提款）','year':2023,'comparable_price':False,
    'note':'原文：customers withdrew $42 billion ... within a day；单一来源待核实。','sources':['w-en-bank-run']},
  ],
 },
}
for eid,add in DATA.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L3'; ct=d['crisis_type']; ch,sc=chain_schools(ct)
    have={t.get('display') for t in d.get('timeline',[])}
    for t in add['tl']:
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in add.get('kd',[]):
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    if not d.get('causal_chain'): d['causal_chain']=[{'step':t,'sources':[s]} for t,s in ch]
    if not d.get('schools'): d['schools']=[{'holder':h,'view':v,'basis':'类型学框架；待核实','sources':[s]} for h,v,s in sc]
    if not d.get('policy_response'): d['policy_response']=[{'holder':'政策当局','view':'应对措施及效果待核实','basis':'需多来源印证','sources':[d['sources'][0]]}]
    if not d.get('comparison'): d['comparison']=f'与同为「{ct}」类案例共享机制，差异在时期、地区与制度环境；具体待核实。'
    if not d.get('deep_svg'): d['deep_svg']=deep_svg(d['title'],ct)
    if not d.get('l3_detail'): d['l3_detail']={'data_caveat':'数值须注明来源/年份/口径；单一来源均待核实。','controversy_summary':'各方解释并列，不替读者下结论。','framework_type':ct}
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【轮次14】升L3，补维基原文实证timeline与数值，单源待核实。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'→L3 tl',len(d['timeline']),'kd',len(d['key_data']),'deep_svg',bool(d.get('deep_svg')))
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in DATA: e['level']='L3'; e['last_updated']='2026-11-22'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage同步')
