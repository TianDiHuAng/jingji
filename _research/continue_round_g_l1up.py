# -*- coding: utf-8 -*-
"""续作：13条L1补充条目→L2（据REST摘要真实事实,含明确数值）。"""
import json
def svg(t,labels):
    e=lambda s:str(s).replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')[:20]
    s=["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x,lb in zip([20,270,520],labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/><text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/><line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)
# eid: dict(sid, tl[(y,disp,ev)], causal[(step)], schools[(h,v)], kd=[(label,val,unit,year,note)], cmp)
D={
 'bengal-bubble-1769':{'sid':'w-en-bengal-bubble-of-1769','tl':[(1757,'1757年','东印度公司在克莱武率领下征服孟加拉（据 Wikipedia Bengal Bubble of 1769）'),(1769,'1757—1769年','东印度公司股票被持续高估形成泡沫，1769年崩盘("大东印度崩盘")（同上）')],
  'causal':['东印度公司征服孟加拉后权势与收益预期上升 → 股票估值持续走高','1757—1769年估值不断高估形成泡沫 → 1769年"大东印度崩盘"','重大金融危机并冲击市场'],
  'schools':[('基本面/殖民收益视角','征服孟加拉带来的收益预期推动股价'),('投机泡沫视角','估值脱离基本面最终崩盘')],
  'cmp':'18世纪早期殖民贸易泡沫案例，与南海/密西西比泡沫同期相继。具体异同待核实。'},
 'cameroon-crisis-1987':{'sid':'w-en-cameroonian-economic-crisis','tl':[(1987,'1980年代中期—2000年代初','喀麦隆经济下行，物价上涨、贸易逆差、政府收入流失；政府1987年承认危机（据 Wikipedia Cameroonian economic crisis）')],
  'causal':['经济治理不善(外部批评)与出口价格下跌(政府说法) → 经济下行','物价上涨、贸易逆差、政府收入流失','持续至2000年代初'],
  'schools':[('治理视角','外部观察者归咎政府经济管理不善'),('外部冲击视角','政府归因于出口商品价格下跌')],
  'cmp':'非洲撒哈拉以南债务/经济危机案例；具体异同待核实。'},
 'great-recession-russia':{'sid':'w-en-great-recession-in-russia','tl':[(2008,'2008—2009年','俄罗斯金融市场危机与经济衰退，叠加格鲁吉亚战争后的政治担忧（据 Wikipedia Great Recession in Russia）'),(2008,'2008年','乌拉尔重质原油自7月4日峰值147美元跌逾70%（同上）')],
  'causal':['油价自147美元峰值暴跌逾70% + 格鲁吉亚战争政治担忧 → 资本外流与市场动荡','金融市场危机 → 经济衰退','2009年温和反弹'],
  'schools':[('大宗商品/油价视角','油价暴跌是核心冲击'),('地缘政治视角','战争与政治担忧放大资本外流')],
  'kd':[('乌拉尔原油跌幅(2008)','>70','%（自147美元/桶峰值，2008年）',2008,'原文：lost more than 70% of its value since its record peak of US$147 on 4 July 2008；单一来源待核实。')],
  'cmp':'与2008全球金融危机同期；资源型经济体受油价冲击尤重。具体异同待核实。'},
 'henan-2022':{'sid':'w-en-henan-2022','tl':[(2022,'2022年','河南四家村镇银行储户因资金问题示威，涉及约400亿元存款（据 Wikipedia 2022 Henan banks protests）')],
  'causal':['涉事村镇银行资金/治理问题 → 储户取款困难','储户维权示威 → 引发关注','暴露出村镇银行风险与监管问题(待核实)'],
  'schools':[('治理/欺诈视角','涉金融腐败与资金问题'),('监管/存款保障视角','凸显中小银行监管与存款保障重要性')],
  'kd':[('涉事银行存款规模','400','亿元(约,河南四家村镇银行)',2022,'原文：Deposits totaling around 40 billion yuan；单一来源待核实。')],
  'cmp':'中国村镇银行风险事件；具体异同待核实。'},
 'myanmar-2003':{'sid':'w-en-myanmar-2003','tl':[(2003,'2003年2月','缅甸私营银行遭大规模挤兑，起于对私营金融机构信心下降与流动性谣言（据 Wikipedia 2003 Myanmar banking crisis）')],
  'causal':['小金融企业倒闭+关于大行流动性的谣言 → 信任下降','对Asia Wealth Bank挤兑 → 迅速蔓延至所有主要私营银行','银行业危机'],
  'schools':[('信心/挤兑视角','谣言与信心崩塌引发挤兑'),('金融脆弱视角','私营金融机构脆弱性放大传染')],
  'cmp':'新兴市场银行挤兑案例；具体异同待核实。'},
 'panic-1884':{'sid':'w-en-panic-of-1884','tl':[(1882,'1882—1885年','美国处于1882-85年萧条期（据 Wikipedia Panic of 1884）'),(1884,'1884年','恐慌在衰退末期而非初期爆发，造成信贷短缺、把衰退拖成萧条（同上）')],
  'causal':['在1882-85萧条末期爆发 → 信贷短缺','信贷紧缩 → 经济显著下滑','把衰退转为萧条'],
  'schools':[('信贷紧缩视角','恐慌造成信贷短缺、加深衰退'),('周期时点视角','在衰退末期爆发，冲击不同于常规')],
  'cmp':'美国19世纪末多起恐慌之一(1873/1884/1893)；具体异同待核实。'},
 'panic-1930':{'sid':'w-en-panic-of-1930','tl':[(1930,'1930年','美国金融危机：农业区银行接连倒闭引发储户恐慌与全国性挤兑（据 Wikipedia Panic of 1930）')],
  'causal':['农业区银行接连倒闭 → 储户恐慌','恐慌蔓延 → 全国性银行挤兑','货币供给急剧收缩、经济加速下滑'],
  'schools':[('货币收缩视角','银行倒闭致货币供给收缩，加深大萧条'),('银行恐慌视角','存款人恐慌性挤兑')],
  'cmp':'大萧条初期关键节点(1930年)，与1930-33银行危机相连。具体异同待核实。'},
 'stock-downturn-2002':{'sid':'w-en-stock-market-downturn-of-2002','tl':[(2002,'2001—2002年','美加亚欧股市自2001年急跌；2002年3月起持续下滑，7月与9月剧烈下跌至1997-98年低位（据 Wikipedia 2002 stock market downturn）')],
  'causal':['互联网泡沫破裂后估值回调 + 经济放缓 → 股价下滑','2002年3月起持续下跌、7/9月剧烈下挫','跌至1997-98低位；美元相对欧元走强'],
  'schools':[('泡沫破裂视角','互联网泡沫后估值回归'),('宏观/盈利视角','经济与盈利前景拖累')],
  'cmp':'互联网泡沫(2000-2004)的延续下跌阶段；具体异同待核实。'},
 'stocks-fall-2011':{'sid':'w-en-august-2011-stock-markets-fall','tl':[(2011,'2011年8月','美中东欧亚股市急跌，因担忧欧债危机蔓延至西班牙、意大利及美国增长与评级下调（据 Wikipedia August 2011 stock markets fall）')],
  'causal':['欧债危机蔓延(西/意)担忧 + 法国AAA评级担忧 + 美国增长放缓与评级下调 → 恐慌','全球股市急跌、剧烈波动','避险情绪上升'],
  'schools':[('主权债务传染视角','欧债危机传染担忧主导'),('增长/评级视角','美国增长与评级下调担忧叠加')],
  'cmp':'与欧债危机(2010-2012)同期；具体异同待核实。'},
 'venezuelan-banking-1994':{'sid':'w-en-venezuelan-banking-crisis-of-1994','tl':[(1994,'1994年1月','委内瑞拉第二大银行Banco Latino倒闭，随后占比18%存款的两家银行亦倒闭，政府接管多家银行（据 Wikipedia Venezuelan banking crisis of 1994）')],
  'causal':['多家银行经营恶化 → Banco Latino(第二大)率先倒闭','更多银行倒闭(占18%存款) → 政府接管','总统暂停宪法权利以实施价格管制；暴露深层腐败'],
  'schools':[('银行脆弱/治理视角','银行经营与治理问题致倒闭'),('政策应对视角','政府接管与管制应对')],
  'kd':[('后续倒闭银行存款占比','18','%(两家银行合计/总存款,委内瑞拉1994)',1994,'原文：two banks accounting for 18% of total deposits also failed；单一来源待核实。')],
  'cmp':'拉美1990s银行危机案例；具体异同待核实。'},
 'venezuelan-banking-2009':{'sid':'w-en-venezuelan-banking-crisis-of-2009-2010','tl':[(2009,'2009—2010年','委内瑞拉政府接管多家银行，因与查韦斯支持者相关的机构经营困难暴露（据 Wikipedia Venezuelan banking crisis of 2009–2010）')],
  'causal':['关联政治支持者的银行从事可疑业务 → 资本不足/挪用','问题暴露 → 政府接管多家银行','银行业危机'],
  'schools':[('治理/关联交易视角','银行向高管放贷、资本不足等治理问题'),('政治经济视角','与政治关联的机构风险积累')],
  'cmp':'委内瑞拉2009-10银行危机；具体异同待核实。'},
 'ukrainian-crisis-2008':{'sid':'w-en-ukrainian-crisis-2008','tl':[(2008,'2008—2009年','乌克兰受全球衰退重创；世界银行预计2009年经济萎缩15%、通胀16.4%（据 Wikipedia 2008-09 Ukrainian financial crisis）')],
  'causal':['全球金融危机 → 外部融资与出口受冲击','经济急剧萎缩、货币与银行承压','世行预计2009年萎缩约15%'],
  'schools':[('外部冲击视角','高度依赖外部融资与出口，受全球危机重创'),('宏观失衡视角','通胀与外部失衡放大脆弱性')],
  'kd':[('2009经济萎缩(世行预计)','-15','%(乌克兰,2009,世行预计)',2009,'原文：World Bank expected Ukraine\'s economy to shrink 15% in 2009；单一来源待核实。'),('通胀率(2009)','16.4','%(乌克兰,2009)',2009,'原文：inflation having been 16.4%；单一来源待核实。')],
  'cmp':'东欧转型经济体在2008危机中的案例；具体异同待核实。'},
 'arendal-crash-1886':{'sid':'w-en-arendal-crash','tl':[(1886,'1886年','挪威阿伦达尔银行Arendals Privatbank破产，共同所有者Herlofson被揭系统性欺诈客户（据 Wikipedia Arendal crash）'),(1886,'1886年后','连锁引发南挪威多起破产与失业，终结阿伦达尔作为重要航运城市的地位（同上）')],
  'causal':['Arendals Privatbank 破产 + 共同所有者系统性欺诈 → 信任崩塌','连锁破产与失业(南挪威)','阿伦达尔航运地位终结'],
  'schools':[('欺诈/治理视角','银行内部系统性欺诈致破产'),('区域经济视角','单一银行倒闭重创区域经济')],
  'cmp':'北欧19世纪银行危机案例；具体异同待核实。'},
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
    d['pending_notes']=d.get('pending_notes','').replace('L1骨架：内容待核实补充。','')+' 【续作】升L2(据REST摘要)。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print(eid,'->L2')
cov=json.load(open('coverage.json',encoding='utf-8'))
for e in cov['entries']:
    if e['id'] in D: e['level']='L2'; e['last_updated']='2026-11-23'
json.dump(cov,open('coverage.json','w',encoding='utf-8'),ensure_ascii=False,indent=2)
print('done')
