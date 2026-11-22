# -*- coding: utf-8 -*-
"""继续(目标完成后的人工续作)：2条L1→L2 + 2条案例化（据本地维基语料）。"""
import json
def svg(title,ct,a,b,cc):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:26]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(title)}：机制示意（{ct}）</text>"]
    for x,t,sub in [(20,a,'背景'),(270,b,'扩散'),(520,cc,'结果/政策')]:
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='78' class='lbl'>{t}</text><text x='{x+9}' y='96' class='sub'>{sub}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

def up_l2(eid,spec):
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'
    have={t.get('display') for t in d.get('timeline',[])}
    for t in spec.get('tl',[]):
        if t['display'] not in have: d.setdefault('timeline',[]).append(t)
    d['timeline'].sort(key=lambda t:t.get('year',0))
    hk={k.get('label') for k in d.get('key_data',[])}
    for k in spec.get('kd',[]):
        if k['label'] not in hk: d.setdefault('key_data',[]).append(k)
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基原文归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['policy_response']=[{'holder':'政策当局','view':spec.get('policy','应对措施及效果待核实'),'basis':'需多来源印证','sources':[d['sources'][0]]}]
    d['comparison']=spec.get('cmp',f'与同类案例共享机制，差异在时期地区；待核实。')
    if not d.get('svg'): d['svg']=svg(d['title'],d['crisis_type'],'触发','传导','后果')
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【续作】升L2/案例化（据本地维基语料）。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'->',d['level'])

SPECS={
 'amsterdam-crisis-1763':{
  'sid':'w-en-amsterdam-crisis-1763',
  'tl':[{'year':1763,'display':'1763年','event':'七年战争结束后，谷物等商品价格急跌、抵押品贬值致信贷枯竭（据 Wikipedia Amsterdam banking crisis of 1763）','sources':['w-en-amsterdam-crisis-1763']},
        {'year':1763,'display':'1763年7—9月','event':'De Neufville 等大银行倒闭，连锁引发阿姆斯特丹银行危机（同上）','sources':['w-en-amsterdam-crisis-1763']}],
  'causal':[('七年战争结束 → 商品价格急跌、抵押品贬值 → 信贷枯竭','w-en-amsterdam-crisis-1763'),
            ('阿姆斯特丹银行普遍过度杠杆且通过复杂金融工具相互关联 → 对信贷收紧高度脆弱','w-en-amsterdam-crisis-1763'),
            ('De Neufville 大银行倒闭 → 连锁反应','w-en-amsterdam-crisis-1763')],
  'schools':[('杠杆/关联性视角','银行过度杠杆与相互关联放大冲击','w-en-amsterdam-crisis-1763'),
             ('抵押品/信贷视角','商品价格下跌致抵押品贬值、信贷收缩','w-en-amsterdam-crisis-1763')],
 },
 'finnish-banking-1990':{
  'sid':'w-en-finnish-banking-1990',
  'tl':[{'year':1991,'display':'1991—1993年','event':'芬兰金融部门深度系统性危机（据 Wikipedia 1990s Finnish banking crisis）','sources':['w-en-finnish-banking-1990']}],
  'causal':[('1980年代债务驱动的经济繁荣 → 银行信贷与资产价格膨胀','w-en-finnish-banking-1990'),
            ('宏观经济动荡 + 监管薄弱 + 银行自身问题叠加 → 1991-93系统性银行危机','w-en-finnish-banking-1990'),
            ('政府接管与处置银行；纳税人成本约占芬兰GNP的8%','w-en-finnish-banking-1990')],
  'schools':[('信贷繁荣/监管视角','债务驱动繁荣与弱监管酿成系统性风险','w-en-finnish-banking-1990'),
             ('宏观冲击视角','外部宏观动荡触发危机','w-en-financial-crisis')],
  'kd':[{'label':'纳税人成本','value':8,'unit':'%GNP（芬兰，银行危机处置，约数）','year':1993,'comparable_price':False,
         'note':'原文：total taxpayer cost was roughly 8% of the Finnish GNP；单一来源待核实。','sources':['w-en-finnish-banking-1990']}],
 },
}
for eid,spec in SPECS.items():
    up_l2(eid,spec)

# 案例化2条已有L2
CASE={
 'recession-1937-1938':{'causal':[
   ('1937年春产出/利润/工资恢复至1929年水平，但失业仍高；政策与库存调整后经济于1937年中掉头向下','w-en-recession-1937-1938'),
   ('衰退持续13个月(至1938年大部分时间)，工业生产下降近30%、耐用品生产降幅更大、失业骤升','w-en-recession-1937-1938'),
   ('1938年中复苏，但就业直到1941年末参战才回到1937初水平','w-en-recession-1937-1938')],
  'schools':[('政策失误视角','过早收紧财政货币(增税、削减支出、准备金要求)抑制复苏','w-en-recession-1937-1938'),
             ('周期/需求视角','大萧条中的二次探底反映需求基础脆弱','w-en-business-cycle')]},
 'rodrigazo-1975':{'causal':[
   ('1975年6月4日阿根廷经济部长Rodrigo宣布一组经济政策(含大幅贬值约150%)，随后爆发骚乱','w-en-rodrigazo-1975'),
   ('通胀从1974年24.4%升至1975年182.4%、1976年444%；实际工资大跌、公共赤字达12.4%','w-en-rodrigazo-1975'),
   ('冲击削弱庇隆主义工会基础，与伊莎贝尔·庇隆一年内下台相关','w-en-rodrigazo-1975')],
  'schools':[('货币/财政视角','大幅贬值与赤字货币化引发恶性通胀','w-en-rodrigazo-1975'),
             ('政治经济视角','紧缩政策冲击工资与工会，引发社会动荡','w-en-rodrigazo-1975')]},
}
for eid,spec in CASE.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':t,'sources':[s]} for t,s in spec['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基原文归纳；具体表述待核实','sources':[s]} for h,v,s in spec['schools']]
    d['pending_notes']=d.get('pending_notes','')+' 【续作】案例化（据本地维基语料）。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'case-specialized')

# coverage 同步
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in SPECS: e['level']='L2'; e['last_updated']='2026-11-22'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('coverage synced')
