# -*- coding: utf-8 -*-
"""续作BR：修复L3核心骨架条目(第1批6条)——用已抓取缓存事实重写 one_line/overview/timeline。"""
import json

FIX = {
 'japan-asset-bubble-1990': {
   'one_line': '日本1986—1991年资产价格泡沫，房地产与股市价格大幅膨胀，1992年初破裂后经济陷入长期停滞。',
   'overview': ('日本资产价格泡沫（バブル景気）是1986至1991年间日本的经济泡沫，其间房地产与股票市场价格被大幅推高；'
     '1992年初泡沫破裂，日本经济随之停滞。泡沫的特征是资产价格快速上涨、经济活动过热，以及货币供给与信贷的不受控扩张。'
     '为阻止日元进一步升值，货币政策当局推行激进的货币宽松，将官方贴现率下调——1986年由5.0%降至3.0%，'
     '并于1987年2月进一步降至低至2.5%。地价方面，东京住宅区地价较1985年上涨45%，东京商业区平均地价较1985年上涨约122%，'
     '东京工业用地约上涨14%，大阪较上年上涨35%。具体成因与责任归属待核实。'),
   'timeline': [
     {'year':1985,'display':'1985年','event':'广场协议后日元大幅升值，日本转向宽松政策','sources':['w-en-japanese-asset-price-bubble']},
     {'year':1986,'display':'1986年','event':'日本央行将官方贴现率由5.0%下调至3.0%','sources':['w-en-japanese-asset-price-bubble']},
     {'year':1987,'display':'1987年2月','event':'官方贴现率进一步降至2.5%','sources':['w-en-japanese-asset-price-bubble']},
     {'year':1992,'display':'1992年初','event':'泡沫破裂，经济陷入停滞','sources':['w-en-japanese-asset-price-bubble']},
   ],
 },
 'greek-debt-crisis': {
   'one_line': '2009年后希腊主权债务危机：债务/GDP由127%升至179%，多轮外部救助伴随严重产出收缩。',
   'overview': ('希腊政府债务危机是欧元区主权债务危机的核心一环。2009至2017年间，希腊政府债务从3000亿欧元升至3180亿欧元；'
     '然而同期希腊债务/GDP比率却从127%升至179%，原因是危机处置期间GDP严重下降。'
     '历史对照：在1981年加入欧洲经济共同体之前的30年里，希腊政府债务/GDP平均仅19.8%；1993至2007年该比率大致不变，平均102%。'
     '危机暴露的起点之一是统计失真——2009年预算赤字最初预测为GDP的"6—8%"（马斯特里赫特条约要求不超过3%），后修正为12.7%。'
     '危机期间希腊与西班牙失业率一度升至27%。具体救助条款与债务重组细节待核实。'),
   'timeline': [
     {'year':1981,'display':'1981年','event':'希腊加入欧洲经济共同体；此前30年债务/GDP平均19.8%','sources':['w-en-greek-government-debt-crisis']},
     {'year':2009,'display':'2009年','event':'希腊预算赤字由"6—8%"预测修正为GDP的12.7%','sources':['w-en-greek-government-debt-crisis']},
     {'year':2009,'display':'2009年','event':'希腊政府债务约3000亿欧元，债务/GDP 127%','sources':['w-en-greek-government-debt-crisis']},
     {'year':2017,'display':'2017年','event':'债务升至3180亿欧元，债务/GDP升至179%','sources':['w-en-greek-government-debt-crisis']},
   ],
 },
 'panic-1907': {
   'one_line': '1907年美国银行家恐慌（Knickerbocker危机），持续约三周，成为美联储创立的直接契机。',
   'overview': ('1907年恐慌（亦称1907年银行家恐慌或Knickerbocker危机）是1907年10月中旬起在美国持续约三周的一场金融危机。'
     '危机之前市场已连续下挫：自1906年1月峰值至当年7月股价下跌18%；1906年9月至1907年3月市值缩水7.7%；'
     '3月9日至26日再跌9.8%；1907年前九个月股票累计下跌24.4%。'
     '一系列冲击袭击了体系：作为最常用抵押品之一的联合太平洋(Union Pacific)股价下跌50点；'
     '同年6月纽约市债券发行失败。10月14日，海因策(Heinze)兄弟开始大举买入联合铜业(United Copper)，该股一日内由39美元升至52美元，'
     '但逼空者从海因策以外渠道找到了大量股票，逼空失败成为导火索。具体事件序列待核实。'),
   'timeline': [
     {'year':1906,'display':'1906年1—7月','event':'股价自峰值下跌18%','sources':['w-en-panic-of-1907']},
     {'year':1907,'display':'1906-09—1907-03','event':'股市市值缩水7.7%；3月9—26日再跌9.8%','sources':['w-en-panic-of-1907']},
     {'year':1907,'display':'1907年10月14日','event':'联合铜业(United Copper)逼空，股价一日由$39升至$52','sources':['w-en-panic-of-1907']},
     {'year':1907,'display':'1907年10月中旬起','event':'恐慌持续约三周','sources':['w-en-panic-of-1907']},
   ],
 },
 'dotcom-bubble-2000': {
   'one_line': '1995—2000年互联网泡沫：纳斯达克上涨600%后自峰值跌78%，思科等公司市值损失达80%。',
   'overview': ('互联网泡沫是1990年代末以科技与互联网股票为核心的股市泡沫。1995年至2000年3月峰值期间，'
     '纳斯达克综合指数上涨600%；但到2002年10月，指数自峰值下跌78%，回吐了其间全部涨幅。'
     '大型公司同样损失惨重，思科系统(Cisco Systems)股价跌幅达80%。'
     '背景是互联网的快速普及：到1995年逾4000万人使用互联网；1990至1997年美国拥有电脑的家庭比例从15%升至35%，'
     '电脑从奢侈品变为日常品。1999年高通(Qualcomm)股价上涨2619%，另有12只大盘股涨幅超1000%、7只超900%。'
     '具体泡沫成因与估值争议待核实。'),
   'timeline': [
     {'year':1995,'display':'1995年','event':'逾4000万人使用互联网','sources':['w-en-dot-com-bubble']},
     {'year':1999,'display':'1999年','event':'高通股价上涨2619%，多只大盘股涨超1000%','sources':['w-en-dot-com-bubble']},
     {'year':2000,'display':'2000年3月','event':'纳斯达克见顶（自1995年累计上涨600%）','sources':['w-en-dot-com-bubble']},
     {'year':2002,'display':'2002年10月','event':'纳斯达克自峰值下跌78%','sources':['w-en-dot-com-bubble']},
   ],
 },
 'argentina-crisis-2001': {
   'one_line': '阿根廷1998—2002年经济危机（"阿根廷大萧条"），以主权违约与比索钉住制度终结为标志。',
   'overview': ('阿根廷经济危机（常称1998—2002年阿根廷大萧条）是新兴市场史上最严重的主权债务与货币危机之一。'
     '危机前的长期背景是高通胀：1975至1988年间阿根廷通胀平均每月10%（约合每年220%）。'
     '预算赤字升至GDP的15%，国家为接管私人债务与未完工项目等支出超过150亿美元。'
     '危机期间阿根廷发生主权违约，并终结了比索与美元的可兑换制度（"兑换计划"）。'
     '到2003年上半年GDP恢复增长，其后五年平均增速约9%，超过危机前水平；2006年阿根廷全额偿还了IMF贷款。'
     '具体时间节点与政策序列待核实。'),
   'timeline': [
     {'year':1980,'display':'1975—1988年','event':'通胀平均每月10%（约年220%）','sources':['w-en-argentine-economic-crisis']},
     {'year':1982,'display':'危机前','event':'预算赤字升至GDP 15%；国家接管逾150亿美元私人债务','sources':['w-en-argentine-economic-crisis']},
     {'year':2001,'display':'2001年','event':'主权违约，可兑换制度终结（具体日期待核实）','sources':['w-en-financial-crisis']},
     {'year':2003,'display':'2003年起','event':'GDP恢复，其后五年平均增速约9%；2006年还清IMF贷款','sources':['w-en-argentine-economic-crisis']},
   ],
 },
 'euro-area-crisis': {
   'one_line': '2010年前后欧元区主权债务危机：希腊、西班牙失业率一度达27%，多国需外部救助并推行紧缩。',
   'overview': ('欧元区主权债务危机（欧债危机）自2010年前后展开，是2008年全球金融危机在欧洲的延续与放大。'
     '危机应对伴随财政紧缩，希腊与西班牙失业率一度升至27%，受影响国家的贫困水平与收入不平等上升。'
     '危机的暴露与统计失真有关：希腊2009年预算赤字最初预测为GDP的"6—8%"，后修正为12.7%，'
     '而马斯特里赫特条约规定上限为3%；这一低估直到2009年很晚（9月）才被纠正。'
     '同期欧盟委员会预测2009年欧盟经济产出下降1.8%，令银行前景更趋恶化。'
     '具体救助规模与各国调整路径待核实。'),
   'timeline': [
     {'year':2009,'display':'2009年9月','event':'希腊赤字低估（"6—8%"）迟迟未纠正','sources':['w-en-eurozone-crisis']},
     {'year':2009,'display':'2009年','event':'希腊预算赤字修正为GDP的12.7%（上限3%）；欧盟预测产出下降1.8%','sources':['w-en-eurozone-crisis']},
     {'year':2013,'display':'危机期间','event':'希腊与西班牙失业率升至27%','sources':['w-en-eurozone-crisis']},
   ],
 },
}

for eid, fix in FIX.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    d['one_line'] = fix['one_line']
    d['overview'] = fix['overview']
    d['timeline'] = fix['timeline']
    d['pending_notes'] = (d.get('pending_notes', '').replace('【条目骨架', '【已补正文') +
                          ' 【续作BR】已用抓取事实重写正文与时间线，替换原骨架占位。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('重写', eid, '| timeline', len(fix['timeline']), '条')
