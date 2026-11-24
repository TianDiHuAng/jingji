# -*- coding: utf-8 -*-
"""续作BS：修复L3骨架(第2批6条案例)。"""
import json

FIX = {
 'great-depression': {
   'one_line': '1929—1939年全球性经济大萧条：美国失业率峰值达25%，货币供给收缩近30%，全球GDP下降约15%。',
   'overview': ('大萧条是1929年开始、延续至1930年代末的全球性经济危机。以美国为中心，工业产出、物价与贸易大幅下滑，'
     '失业率飙升。据美联储历史记载，从1930年秋到1933年冬，美国货币供给下降了近30%——银行倒闭潮把金融危机转化为货币紧缩，'
     '是本轮萧条加深的关键传导环节。1933年美国失业率峰值达约25%；1929至1932年间全球GDP下降约15%。'
     '各国应对路径分化：英、美先后脱离金本位（英国1931年、美国1934年黄金国有化），以法国为首的"金集团"坚持金本位而承受更久的通缩。'
     '具体成因与责任（货币因素与结构因素之争）待核实。'),
   'timeline': [
     {'year':1929,'display':'1929年10月','event':'华尔街崩盘，危机起点','sources':['w-en-great-depression']},
     {'year':1931,'display':'1930年秋—1933年冬','event':'美国货币供给下降近30%','sources':['fed-great-depression']},
     {'year':1931,'display':'1931年','event':'英国脱离金本位','sources':['w-en-gold-standard']},
     {'year':1933,'display':'1933年','event':'美国失业率峰值约25%；全球GDP较1929年降约15%','sources':['w-en-great-depression']},
     {'year':1934,'display':'1934年1月30日','event':'美国《黄金储备法》，黄金与金券上缴财政部','sources':['w-en-gold-reserve-act-1934']},
   ],
 },
 'wall-street-1929': {
   'one_line': '1929年10月华尔街股市崩盘：黑色星期四成交1290万股，黑色星期一跌近13%、星期二跌近12%。',
   'overview': ('1929年华尔街崩盘是1929年10月纽约证券交易所的股价暴跌，通常被视为大萧条的起点。'
     '1929年10月24日（"黑色星期四"）纽约证交所成交量达1290万股。'
     '10月28日（"黑色星期一"）道琼斯工业平均指数下跌近13%；次日"黑色星期二"市场再跌近12%。'
     '跌势延续数年：到1932年，股指最低点较峰值低89%（美联储历史口径），另有以市值计下跌约90%的记载，两源基本一致。'
     '崩盘与随后的银行倒闭潮、货币收缩相互作用，使金融冲击演变为长期萧条。具体成因待核实。'),
   'timeline': [
     {'year':1929,'display':'1929年10月24日','event':'"黑色星期四"，成交1290万股','sources':['w-en-wall-street-crash-1929']},
     {'year':1929,'display':'1929年10月28日','event':'"黑色星期一"，道指跌近13%','sources':['fed-stock-crash-1929']},
     {'year':1929,'display':'1929年10月29日','event':'"黑色星期二"，市场跌近12%','sources':['fed-stock-crash-1929']},
     {'year':1932,'display':'1932年','event':'股指最低点较峰值低89%（市值口径约90%）','sources':['fed-stock-crash-1929']},
   ],
 },
 'weimar-hyper-1921': {
   'one_line': '魏玛德国1921—1923年恶性通胀：以印钞弥补赔款与财政缺口，马克购买力崩溃，终以地租马克改革收场。',
   'overview': ('魏玛共和国恶性通胀是1921至1923年间德国的货币崩溃。一战赔款负担、财政赤字与占领事件（1923年鲁尔）'
     '叠加，政府以中央银行融资弥补缺口，货币供给爆炸式扩张，物价失控上涨、马克购买力几近归零。'
     '恶性通胀的社会后果深刻：中产储蓄被 wiped out、工资需按日发放，并被认为削弱了对民主制度的支持。'
     '1923年末以地租马克(Rentenmark)改革稳定币值。'
     '理论上，本轮通胀被视为"财政赤字货币化导致恶性通胀"的经典案例（Cagan 的货币主义解释）。具体数据与年份待核实。'),
   'timeline': [
     {'year':1921,'display':'1921年起','event':'赔款与财政赤字推动印钞，通胀加速','sources':['w-en-hyperinflation']},
     {'year':1923,'display':'1923年','event':'鲁尔占领与恶性通胀高峰','sources':['w-en-hyperinflation']},
     {'year':1923,'display':'1923年末','event':'地租马克(Rentenmark)改革稳定币值（具体日期待核实）','sources':['w-en-hyperinflation']},
   ],
 },
 'hungarian-hyper-1945': {
   'one_line': '匈牙利1945—1946年 pengő 恶性通胀：史上最严重通胀，价格约15小时翻倍、约4天贬值90%。',
   'overview': ('匈牙利pengő恶性通胀发生于1945—1946年，被广泛认为是世界史上最严重的恶性通胀。'
     '战后赔偿负担、生产破坏与财政赤字货币化叠加。通胀之烈可从时间尺度看出：某一阶段价格约每15小时翻倍，'
     'pengő在约四天内失去此前价值的90%。1945年12月曾以75%的资本税等方式试图抑制。'
     '货币体系最终以1946年福林(forint)改革收场。'
     '该案例常与魏玛、津巴布韦并列，作为"财政赤字货币化→恶性通胀"的极端样本。具体数据待核实。'),
   'timeline': [
     {'year':1945,'display':'1945年12月','event':'实施75%资本税等措施试图抑制通胀','sources':['w-en-hungarian-pengo']},
     {'year':1946,'display':'1946年','event':'价格约15小时翻倍、pengő约4天贬值90%','sources':['w-en-hungarian-pengo']},
     {'year':1946,'display':'1946年','event':'以福林(forint)改革终结恶性通胀（具体日期待核实）','sources':['w-en-hyperinflation']},
   ],
 },
 'venezuela-hyper-2016': {
   'one_line': '委内瑞拉2016年后恶性通胀：2016年约800%、2018年约170万%，石油依赖与政策失当叠加。',
   'overview': ('委内瑞拉恶性通胀自2016年前后进入失控阶段。此前通胀已逐年攀升：2014年约69%、2015年约181%、2016年约800%、'
     '2017年超过4000%、2018年约170万%。油价依赖型经济、价格管制、外汇管制与财政赤字货币化共同作用，'
     '使本币玻利瓦尔迅速失去货币职能。**重要提示**：委内瑞拉自2015年后长期中断完整官方统计，'
     '各方估算分歧极大——世界银行/OWID 口径下2016年通胀为254.9%，与本条目所载800%差异显著（见 key_data 并列说明）。'
     '具体数值以何者为准待核实。'),
   'timeline': [
     {'year':2014,'display':'2014年','event':'年通胀约69%（维基口径）','sources':['w-en-hyperinflation-in-venezuela']},
     {'year':2016,'display':'2016年','event':'年通胀约800%（维基口径；世行口径254.9%）','sources':['w-en-hyperinflation-in-venezuela']},
     {'year':2018,'display':'2018年','event':'年通胀约170万%','sources':['w-en-hyperinflation-in-venezuela']},
   ],
 },
 'zimbabwe-hyper-2007': {
   'one_line': '津巴布韦2007—2009年恶性通胀：2008年11月峰值月率约7906亿%，终以美元化收场。',
   'overview': ('津巴布韦恶性通胀在2008年达到顶峰。据估算，峰值月份（2008年11月中）的通胀为月环比约790.6吉%（即7906亿%），'
     '年同比达8.97×10²²%。货币职能崩溃到极端程度——当时一张100万亿面额的钞票不足以支付一趟公交车费。'
     '土地改革后农业产出下滑、财政赤字货币化与外汇短缺被视为主要背景。'
     '2009年该国转向美元化以稳定物价；此后通胀一度回落，但2019年7月又升至175%（世界银行口径为255.3%，见并列说明）。'
     '具体时间线与政策细节待核实。'),
   'timeline': [
     {'year':2008,'display':'2008年11月','event':'峰值月通胀约7906亿%（月环比）','sources':['w-en-hyperinflation-in-zimbabwe']},
     {'year':2009,'display':'2009年','event':'转向美元化以稳定物价（具体日期待核实）','sources':['w-en-hyperinflation-in-zimbabwe']},
     {'year':2019,'display':'2019年7月','event':'通胀回升至175%（世行口径255.3%）','sources':['w-en-hyperinflation-in-zimbabwe']},
   ],
 },
}

for eid, fix in FIX.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    d['one_line'] = fix['one_line']
    d['overview'] = fix['overview']
    d['timeline'] = fix['timeline']
    d['pending_notes'] = (d.get('pending_notes','') + ' 【续作BS】已用抓取事实重写正文与时间线，替换骨架占位。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('重写', eid, '| timeline', len(fix['timeline']))
