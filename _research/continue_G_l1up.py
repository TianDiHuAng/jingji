# -*- coding: utf-8 -*-
"""续作G：5条L1→L2（据REST摘要真实事实,含数值）。"""
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
 'steel-crisis-1973':{'sid':'w-en-steel-crisis','tl':[
   (1973,'1973—1975年及1980年代初','全球钢铁市场长期低迷，发生在两次衰退期间，并由1973/1979石油危机加剧（据 Wikipedia Steel crisis）'),
   (1973,'延续至1980年代','冲击北美"锈带"、英格兰中部、西德鲁尔区、瑞典贝里斯拉根等工业区（同上）')],
  'causal':['二战后扩张期结束 + 1973与1979石油危机 → 全球钢铁需求与产能失衡','钢铁市场长期低迷 → 工业区衰退','持续至1980年代，冲击多个工业地区'],
  'schools':[('需求/能源冲击视角','石油危机与需求放缓致钢铁长期过剩'),('结构性/产业转移视角','传统钢铁工业区面临结构性衰退')],
  'cmp':'与1973石油危机同期，属产业结构性危机而非金融危机。具体异同待核实。'},
 'panic-1896':{'sid':'w-en-panic-of-1896','tl':[
   (1896,'1896年','美国急性经济萧条，由白银储备下降与市场对金本位的担忧引发（据 Wikipedia Panic of 1896）'),
   (1896,'1896年','恐慌期间拆借利率(call money)高达125%，为内战以来最高（同上）'),
   (1896,'1896年','股市创新低，直到克朗代克淘金热后才反转（同上）')],
  'causal':['白银储备下降 + 对金本位的担忧 → 市场恐慌','商品价格通缩 → 股市创新低','拆借利率飙至125%；克朗代克淘金热后反转'],
  'schools':[('货币/金本位视角','白银与金本位之争引发货币性恐慌'),('通缩视角','商品价格通缩拖累股市与债务')],
  'kd':[('拆借利率峰值(1896)','125','%(call money,美国,1896)',1896,'原文：call money would reach 125 percent, the highest level since the Civil War；单一来源待核实。')],
  'cmp':'与1893恐慌同属19世纪末美国货币/金融动荡；具体异同待核实。'},
 'panic-1796':{'sid':'w-en-panic-of-1796','tl':[
   (1796,'1796年','英美信贷市场一系列下挫，美国土地投机泡沫破裂（据 Wikipedia Panic of 1796–1797）'),
   (1797,'1797年2月25日','英格兰银行依《1797年银行限制法》暂停硬币支付，因担忧法国入侵引发挤兑（同上）')],
  'causal':['美国土地投机泡沫破裂 → 信贷市场下挫','英法战争恐惧致存款人挤兑 → 英格兰银行暂停硬币支付','通缩波及美国沿海与加勒比商业市场'],
  'schools':[('投机泡沫视角','土地投机破裂引发信贷收缩'),('战争/信心视角','战争恐惧引发挤兑与货币管制')],
  'cmp':'与1792恐慌同属美国早期金融危机；具体异同待核实。'},
 'panic-1910':{'sid':'w-en-panic-of-1910','tl':[
   (1910,'1910—1911年','谢尔曼反托拉斯法执行后的轻微萧条，持续约1年（据 Wikipedia Panic of 1910–11）'),
   (1910,'1910—1911年','美国主要股指下跌约26%，主要受标准石油与美国烟草公司分拆影响（同上）')],
  'causal':['反托拉斯执法(标准石油、美国烟草分拆) → 投资者信心受挫','股市下跌约26%','短暂萧条约1年'],
  'schools':[('政策/监管冲击视角','反托拉斯执法冲击相关企业与市场情绪'),('市场情绪视角','"trust buster"行动引发抛售')],
  'kd':[('美股主要指数跌幅(1910–11)','-26','%(美国主要股指,约)',1911,'原文：led to a drop of the major U.S. stock market index by ~26%；单一来源待核实。')],
  'cmp':'规模小于1907恐慌；属政策冲击型短暂萧条。具体异同待核实。'},
 'venezuela-energy-2010':{'sid':'w-en-energy-crisis-in-venezuela','tl':[
   (2009,'2009年12月21日','委内瑞拉政府宣布"电力紧急状态"（据 Wikipedia Energy crisis in Venezuela）'),
   (2010,'2010年','长期干旱致古里(Simón Bolívar)水电站水位极低，全国实施限电(首都加拉加斯除外)（同上）'),
   (2011,'2011年5月14日','经历两次全国性停电后，政府宣布临时限电计划并承认电力系统存在"发电弱点"（同上）')],
  'causal':['长期干旱 → 水电站水位极低、发电不足','政府实施全国限电(除首都)并宣布电力紧急状态','电力系统结构性弱点持续，2011年再现停电'],
  'schools':[('气候/供给视角','干旱致水电出力不足是直接原因'),('投资/治理视角','发电与电网投资不足导致结构性脆弱')],
  'cmp':'与委内瑞拉2013年经济危机同源（投资不足与治理问题），但属能源/基础设施危机。具体异同待核实。'},
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
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【续作G】升L2(据REST摘要)。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'->L2')
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in D: e['level']='L2'; e['last_updated']='2026-11-23'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('done')
