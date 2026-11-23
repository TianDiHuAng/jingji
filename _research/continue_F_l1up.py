# -*- coding: utf-8 -*-
"""续作F：6条L1→L2（据REST摘要真实事实）。"""
import json
def svg(t,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x,lb in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)
D={
 'british-credit-1772':{'sid':'w-en-british-credit-1772','tl':[
   (1772,'1772年','伦敦起源的和平时期金融危机，随后蔓延至苏格兰与荷兰共和国（据 Wikipedia British credit crisis of 1772–1773）'),
   (1772,'1772—1773年','被称为英格兰银行所面对的首场现代银行危机（同上）')],
  'causal':['新殖民地资本需求旺盛 + 信贷与银行业快速扩张 → 投机与可疑金融创新(以保证金买股)','危机自伦敦爆发 → 蔓延至苏格兰与荷兰共和国','英格兰银行面临首场现代银行危机'],
  'schools':[('信贷扩张/投机视角','信贷快速扩张与投机(保证金交易)酿成危机'),('现代银行危机视角','被视为英格兰银行面对的首场现代银行危机')],
  'cmp':'与阿姆斯特丹1763危机同属18世纪欧洲信贷危机；被视为现代银行危机早期范例。具体异同待核实。'},
 'copper-panic-1789':{'sid':'w-en-copper-panic-of-1789','tl':[
   (1789,'1789年','美国早期货币危机：铜币贬值与信心丧失（据 Wikipedia Copper Panic of 1789）'),
   (1789,'独立战争后','各州自行铸币；伪造盛行迫使铸币者降低成色（同上）')],
  'causal':['独立战争后各州自行铸造铜币 → 铜币易伪造','伪造泛滥 → 铸币者降低成色以维持经营','铜币贬值、信心丧失 → 货币危机；财政部尚未建立加剧困境'],
  'schools':[('货币成色/信心视角','成色下降与伪造破坏货币信用'),('制度缺失视角','财政部尚未设立、旧币贬值加剧问题')],
  'cmp':'美国建国初期货币危机；与大陆币贬值同属早期货币问题。具体异同待核实。'},
 'danish-bankruptcy-1813':{'sid':'w-en-danish-bankruptcy-of-1813','tl':[
   (1813,'1813年1月','丹麦国家破产开始，影响延续至1818年（据 Wikipedia Danish state bankruptcy of 1813）'),
   (1813,'1813—1818年','拿破仑战争财政负担下货币贬值，冲击商人、市民与企业（同上）')],
  'causal':['拿破仑战争带来沉重财政负担 → 丹麦-挪威财政恶化','货币贬值 → 商人、市民与企业受损','国家破产，影响延续至1818年'],
  'schools':[('战争财政视角','战争开支与货币贬值导致破产'),('货币贬值视角','贬值损害各阶层实际财富')],
  'cmp':'拿破仑战争时期的欧洲国家破产案例；具体异同待核实。'},
 'german-crisis-2022':{'sid':'w-en-german-economic-crisis-2022-present','tl':[
   (2022,'2022年起','德国经济下行，逆转了2005-2019"劳动力市场奇迹"期（据 Wikipedia German economic crisis）'),
   (2023,'2023年','德国成为全球表现最差的主要经济体，萎缩0.9%（同上）'),
   (2024,'2024年','再萎缩0.5%，陷入衰退；2025年小幅回升（同上）')],
  'causal':['能源等结构性冲击 + 出口与工业承压 → 经济下行','2023年萎缩0.9%、2024年再萎缩0.5% → 衰退','专家担忧德国重获"欧洲病夫"之称；2025年小幅回升'],
  'schools':[('结构性/能源视角','能源成本与产业结构转型拖累德国模式'),('周期/外部需求视角','全球需求与出口下滑影响制造业')],
  'kd':[('2023年GDP增速','-0.9','%(德国,2023,萎缩)',2023,'原文：worst-performing major economy globally in 2023 with a 0.9% contraction；单一来源待核实。'),
        ('2024年GDP增速','-0.5','%(德国,2024,萎缩)',2024,'原文：further 0.5% contraction in 2024 leading to recession；单一来源待核实。')],
  'cmp':'与欧债危机(2010-12)不同，本轮为结构性/能源冲击下的德国经济困境。具体异同待核实。'},
 'greek-hyper-1941':{'sid':'w-en-greek-hyper-1941','tl':[
   (1941,'1941—1946年','希腊在二战及轴心国占领期间发生恶性通胀（据 Wikipedia Greek hyperinflation）')],
  'causal':['占领与战争 → 政府无税收能力、只能印钞融资','货币超发 → 物价飞涨、货币职能受损','恶性通胀（时长认定存在分歧）'],
  'schools':[('Palairet视角','长达50个月的"超长"恶性通胀，因政府不征税而任意印钞'),('其他学者视角','认为恶性通胀主要限于1943-44年，时长较短')],
  'cmp':'与魏玛、匈牙利恶性通胀同属20世纪恶性通胀案例；时长认定有分歧。具体异同待核实。'},
 'israel-bank-1983':{'sid':'w-en-israel-bank-1983','tl':[
   (1983,'1983年','以色列四大银行股票暴跌（据 Wikipedia 1983 Israel bank stock crisis）'),
   (1983,'1983年10月6日起','特拉维夫证交所关闭18天；实施复苏计划并将银行国有化（同上）')],
  'causal':['银行为支撑自家股价持续回购 → 制造虚假需求、人为托价','1983年10月银行资本耗尽、无法继续回购 → 股价暴跌','证交所关闭18天、银行国有化'],
  'schools':[('市场操纵/托价视角','银行回购自家股票人为支撑股价'),('监管/治理视角','暴露市场监管与公司治理缺陷')],
  'cmp':'与日本泡沫期银行持股等案例相关；具体异同待核实。'},
}
for eid,sp in D.items():
    f='data/entries/'+eid+'.json'; d=json.load(open(f,encoding='utf-8'))
    d['level']='L2'; sid=sp['sid']
    have={t.get('display') for t in d.get('timeline',[])}
    for y,disp,ev in sp['tl']:
        if disp not in have: d.setdefault('timeline',[]).append({'year':y,'display':disp,'event':ev,'sources':[sid]})
    d['timeline'].sort(key=lambda t:t.get('year',0))
    d['causal_chain']=[{'step':st,'sources':[sid]} for st in sp['causal']]
    d['schools']=[{'holder':h,'view':v,'basis':'据维基摘要归纳；具体表述待核实','sources':[sid]} for h,v in sp['schools']]
    hk={k.get('label') for k in d.get('key_data',[])}
    for kd in sp.get('kd',[]):
        if kd[0] not in hk: d.setdefault('key_data',[]).append({'label':kd[0],'value':kd[1],'unit':kd[2],'year':kd[3],'comparable_price':False,'note':kd[4],'sources':[sid]})
    d['policy_response']=[{'holder':'政策当局','view':'应对措施及效果待核实','basis':'需多来源印证','sources':[d['sources'][0]]}]
    d['comparison']=sp['cmp']
    if not d.get('svg'): d['svg']=svg(d['title'],[sp['tl'][0][2][:12],'传导','后果'])
    d['needs_verification']=True
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【续作F】升L2(据REST摘要)。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'->L2')
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in D: e['level']='L2'; e['last_updated']='2026-11-23'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('done')
