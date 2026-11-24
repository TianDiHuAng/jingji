# -*- coding: utf-8 -*-
"""续作CH：为剩余3个模板组(债务/货币/泡沫)定制因果链与观点。"""
import json

CAUSAL = {
 # ---- 债务组 ----
 'chilean-crisis-1982': [
   ('1970年代末金融自由化 + 钉住汇率 + 私人部门大量借入外币 → 外债至1982年逾170亿美元', 'w-en-chilean-crisis-1982'),
   ('美联储加息与贸易条件恶化 → 资本流入逆转、银行资产质量恶化', 'w-en-latin-american-debt-crisis'),
   ('银行救助与重组 → GDP下降14.3%、失业率升至23.7%，并转向结构性改革', 'w-en-chilean-crisis-1982'),
 ],
 'china-realestate-2020': [
   ('"三条红线"融资约束 + 预售制下的高杠杆扩张 → 开发商资金链断裂', 'w-en-china-realestate-2020'),
   ('恒大等违约（涉资约2万亿元人民币）→ 项目停工与供应商、购房者受损', 'w-en-china-realestate-2020'),
   ('政策以"保交楼"、项目纾困与需求端放松应对 → 地方土地财政承压（细节待核实）', 'w-en-china-realestate-2020'),
 ],
 'euro-area-crisis': [
   ('欧元区统一货币但财政各自为政 → 边缘国家以低利率累积债务与竞争力失衡', 'w-en-eurozone-crisis'),
   ('希腊赤字由"6—8%"修正为12.7% → 市场拒绝融资、主权利差飙升', 'w-en-eurozone-crisis'),
   ('救助+紧缩+银行-主权循环 → 希腊与西班牙失业率升至27%', 'w-en-eurozone-crisis'),
 ],
 'greek-debt-crisis': [
   ('入欧后长期赤字（1993—2007年债务/GDP均值102%）+ 竞争力流失 → 危机前脆弱性累积', 'w-en-greek-government-debt-crisis'),
   ('2009年赤字统计失真暴露 → 融资成本飙升，2010年起接受多轮外部救助', 'w-en-greek-government-debt-crisis'),
   ('紧缩致GDP大幅下滑 → 债务/GDP由127%升至179%（2017年，分母收缩）', 'w-en-greek-government-debt-crisis'),
 ],
 'latin-american-debt-1975': [
   ('石油美元回流 + 实际利率为负 → 拉美对商业银行债务年均增20.4%', 'w-en-latin-american-debt-crisis'),
   ('1979年起全球利率飙升 + 商品价格下跌 → 偿债额由120亿(1975)升至660亿(1982)', 'w-en-latin-american-debt-crisis'),
   ('1982年墨西哥宣布无力偿债 → "失去的十年"：1980—85年人均GDP近-9%', 'w-en-latin-american-debt-crisis'),
 ],
 'puerto-rico-debt-2014': [
   ('税收优惠取消与人口外流 → 税基萎缩而支出刚性（2007—2017年GNI降14%）', 'w-en-puerto-rican-debt-crisis'),
   ('以发债弥补赤字 → 债券债务达740亿美元，市场融资渠道关闭', 'w-en-puerto-rican-debt-crisis'),
   ('依PROMESA设立监督委员会并进入类似破产的重组（销售税提高至11%）', 'w-en-puerto-rican-debt-crisis'),
 ],
 'sri-lanka-crisis-2019': [
   ('大规模减税 + 旅游受创 + 长期经常账户赤字 → 外汇储备枯竭（2022年3月19亿美元）', 'w-en-sri-lankan-economic-crisis'),
   ('2022年到期偿还86亿美元（含7月主权债10亿）→ 无力偿付，宣布暂停外债', 'w-en-sri-lankan-economic-crisis'),
   ('IMF谈判与债务重组（印度提供40亿美元信贷额度曾使储备回升至27亿）', 'w-en-sri-lankan-economic-crisis'),
 ],
 # ---- 货币组 ----
 'bretton-woods': [
   ('双挂钩安排下美国须持续输出美元 → 特里芬难题：流动性供给与黄金兑换信心冲突', 'w-en-bretton-woods-system'),
   ('美国黄金储备相对对外负债下降 + 通胀上升 → 对美元平价的信心流失', 'w-en-nixon-shock'),
   ('1971年8月停止兑换黄金 → 1973年转向浮动，1976年牙买加协定确认', 'w-en-nixon-shock'),
 ],
 'crisis-third-century': [
   ('政治军事动荡与军费上升 → 铸币持续贬损（第纳尔含银量下降）', 'w-en-debasement'),
   ('货币贬值 + 瘟疫致人口锐减（亚历山大城-62%）→ 粮价半世纪涨20万%', 'w-en-crisis-of-the-third-century'),
   ('戴克里先改革与301年《价格敕令》限价 → 效果有限（见 edict-maximum-prices）', 'w-en-edict-maximum-prices'),
 ],
 'gold-standard': [
   ('金平价固定汇率 → 货币供给受黄金储备约束，国际收支靠内部调整', 'w-en-gold-standard'),
   ('大萧条中储备流失与失业上升 → 维持平价须承受通缩与产出损失', 'w-en-gold-standard'),
   ('英国1931年退出、美国1934年黄金国有化、金集团坚持更久 → 复苏速度分化', 'w-en-gold-reserve-act-1934'),
 ],
 'mexican-peso-1994': [
   ('经常账户赤字达GDP约7% + 大量发行短期比索债 → 对外部融资高度依赖', 'w-en-mexican-peso-crisis'),
   ('1994年12月20日宣布比索贬值13%—15% → 资本外逃、资金撤离新兴市场', 'w-en-mexican-peso-crisis'),
   ('通胀约52%；1995年1月美国组织500亿美元救助（IMF执行、G7与BIS支持）', 'w-en-mexican-peso-crisis'),
 ],
 'russian-crisis-2014': [
   ('油价自2014年6月高点至12月跌近50% + 西方制裁 → 出口收入与融资同时收缩', 'w-en-russian-financial-crisis-2014'),
   ('资本外流1540亿美元 → 卢布承压、通胀上升', 'w-en-russian-financial-crisis-2014'),
   ('央行加息至17%、动用1075亿美元储备、转向浮动 → 2015年GDP收缩3.7%', 'w-en-russian-financial-crisis-2014'),
 ],
 # ---- 泡沫组 ----
 'dotcom-bubble-2000': [
   ('互联网普及（1995年逾4000万人上网）+ 低利率与新经济叙事 → 科技股估值脱离盈利', 'w-en-dot-com-bubble'),
   ('1995—2000年3月纳斯达克上涨600%（1999年高通+2619%）→ 投机自我强化', 'w-en-dot-com-bubble'),
   ('2000年3月见顶后至2002年10月跌78%（思科-80%）→ 回吐全部涨幅', 'w-en-dot-com-bubble'),
 ],
 'japan-asset-bubble-1990': [
   ('广场协议后日元急升 → 日本转向激进宽松，官方贴现率1987年2月降至2.5%', 'w-en-japanese-asset-price-bubble'),
   ('信贷扩张推动地产与股市 → 东京商业地价较1985年+122%、住宅+45%', 'w-en-japanese-asset-price-bubble'),
   ('1992年初泡沫破裂 → 资产价格与信贷双收缩，经济陷入长期停滞', 'w-en-japanese-asset-price-bubble'),
 ],
 'mississippi-bubble-1720': [
   ('约翰·劳以纸币与殖民贸易叙事推动印度公司 → 1717—1718年面值1亿里弗公开发行', 'w-en-john-law-company'),
   ('股价飙升与货币扩张并行 → 1720年1月法国月通胀率达23%', 'w-en-john-law-company'),
   ('泡沫破裂 → 国家向公司支付5.14亿里弗赔偿并重组，公信受损', 'w-en-john-law-company'),
 ],
 'stock-crash-1973': [
   ('1972年道指上涨15%后市场预期更乐观 → 估值偏高、成长股受追捧', 'w-en-1973-1974-stock-crash'),
   ('1973年石油危机与滞胀 → 通胀上行、利率上升，盈利预期下修', 'w-en-1973-1974-stock-crash'),
   ('1973-01-11至1974-12-06（694天）→ 主要股指名义-34%、实际-43%；美国实际GDP 7.2%→-2.1%', 'w-en-1973-1974-stock-crash'),
 ],
 'wall-street-1929': [
   ('1920年代牛市 + 保证金交易与杠杆 → 股价脱离盈利，散户与投资信托广泛参与', 'w-en-wall-street-crash-1929'),
   ('1929年10月24日"黑色星期四"成交1290万股 → 10月28日跌近13%、29日跌近12%', 'fed-stock-crash-1929'),
   ('跌势延续至1932年（较峰值-89%）→ 与随后的银行倒闭潮共同构成大萧条起点', 'fed-stock-crash-1929'),
 ],
}

SCHOOLS = {
 'chilean-crisis-1982': [
   {'holder':'金融自由化视角','view':'过快放开资本账户与汇率钉住，使私人外债成为系统性风险','basis':'据危机前政策归纳','sources':['w-en-chilean-crisis-1982']},
   {'holder':'外部冲击视角','view':'美联储加息与贸易条件恶化是触发条件，脆弱性才是根因','basis':'据时序归纳；权重待核实','sources':['w-en-latin-american-debt-crisis']},
 ],
 'china-realestate-2020': [
   {'holder':'杠杆与预售视角','view':'预售制+高杠杆使开发商对销售回款极度敏感','basis':'据恒大案例归纳','sources':['w-en-china-realestate-2020']},
   {'holder':'土地财政视角','view':'地方财政对土地出让的依赖放大了调整的宏观影响','basis':'据政策应对归纳；量化待核实','sources':['w-en-china-realestate-2020']},
 ],
 'euro-area-crisis': [
   {'holder':'制度设计视角','view':'货币统一而财政分散，缺少调整与转移机制','basis':'据危机演进归纳','sources':['w-en-eurozone-crisis']},
   {'holder':'银行-主权循环视角','view':'银行持有本国国债使二者风险相互放大','basis':'据西班牙、爱尔兰案例归纳','sources':['w-en-eurozone-crisis']},
 ],
 'greek-debt-crisis': [
   {'holder':'财政纪律视角','view':'统计失真与长期赤字是危机的直接原因','basis':'据赤字修正与债务数据归纳','sources':['w-en-greek-government-debt-crisis']},
   {'holder':'调整代价视角','view':'以GDP收缩为代价的紧缩反而推高债务率','basis':'据债务/GDP由127%升至179%归纳','sources':['w-en-greek-government-debt-crisis']},
 ],
 'latin-american-debt-1975': [
   {'holder':'外部条件视角','view':'低利率与商品繁荣掩盖了债务不可持续性','basis':'据利率与偿债数据归纳','sources':['w-en-latin-american-debt-crisis']},
   {'holder':'结构调整视角','view':'紧缩与结构调整的代价主要由中下层承担','basis':'据工资下降20—40%归纳','sources':['w-en-latin-american-debt-crisis']},
 ],
 'puerto-rico-debt-2014': [
   {'holder':'财政结构视角','view':'税收优惠取消后税基萎缩而支出刚性未改','basis':'据GNI与债务数据归纳','sources':['w-en-puerto-rican-debt-crisis']},
   {'holder':'主权地位视角','view':'非州非国的地位限制其破产与调整工具','basis':'据PROMESA框架归纳；法律争议待核实','sources':['w-en-puerto-rican-debt-crisis']},
 ],
 'sri-lanka-crisis-2019': [
   {'holder':'政策失误视角','view':'大幅减税与汇率僵化加剧了外储枯竭','basis':'据政策时序归纳','sources':['w-en-sri-lankan-economic-crisis']},
   {'holder':'外债结构视角','view':'到期集中与外币债务占比高使再融资风险陡增','basis':'据2022年偿还数据归纳','sources':['w-en-sri-lankan-economic-crisis']},
 ],
 'bretton-woods': [
   {'holder':'特里芬视角','view':'储备货币国的流动性供给与兑换承诺存在内在冲突','basis':'据体系运行逻辑归纳','sources':['w-en-bretton-woods-system']},
   {'holder':'政策失误视角','view':'美国通胀与财政扩张加速了平价不可维持','basis':'据1971年前宏观背景归纳；权重待核实','sources':['w-en-nixon-shock']},
 ],
 'crisis-third-century': [
   {'holder':'货币贬损视角','view':'铸币成色下降是物价飞涨的主要机制','basis':'据罗马货币史归纳','sources':['w-en-debasement']},
   {'holder':'人口与供给视角','view':'瘟疫与劳动力减少造成供给冲击，与货币因素叠加','basis':'据瘟疫人口数据归纳','sources':['w-en-crisis-of-the-third-century']},
 ],
 'gold-standard': [
   {'holder':'纪律视角','view':'金本位提供可信的规则与汇率稳定','basis':'据一战前经验归纳','sources':['w-en-gold-standard']},
   {'holder':'束缚视角','view':'金本位限制了反危机政策，延长并加深了萧条','basis':'据各国退出时点与复苏对比归纳','sources':['w-en-gold-standard']},
 ],
 'mexican-peso-1994': [
   {'holder':'短期债视角','view':'以短期外币/指数化债务融资长期赤字是致命弱点','basis':'据tesobonos安排归纳；细节待核实','sources':['w-en-mexican-peso-crisis']},
   {'holder':'救助视角','view':'大规模外部救助迅速稳定了市场，但引发道德风险争议','basis':'据1995年救助结果归纳','sources':['w-en-mexican-peso-crisis']},
 ],
 'russian-crisis-2014': [
   {'holder':'外部冲击视角','view':'油价与制裁是直接触发因素','basis':'据油价与资本流动数据归纳','sources':['w-en-russian-financial-crisis-2014']},
   {'holder':'政策应对视角','view':'浮动汇率+高利率的组合较快恢复了稳定','basis':'据2015—16年稳定过程归纳；代价待核实','sources':['w-en-russian-financial-crisis-2014']},
 ],
 'dotcom-bubble-2000': [
   {'holder':'叙事视角','view':'"新经济"叙事使估值方法被抛弃','basis':'据泡沫期估值与媒体叙述归纳','sources':['w-en-dot-com-bubble']},
   {'holder':'基本面视角','view':'泡沫破裂后存活企业（如亚马逊）仍创造了巨大价值','basis':'据企业后续表现归纳；个案差异大','sources':['w-en-dot-com-bubble']},
 ],
 'japan-asset-bubble-1990': [
   {'holder':'货币政策视角','view':'长期超低利率与信贷扩张催生泡沫','basis':'据贴现率与信贷数据归纳','sources':['w-en-japanese-asset-price-bubble']},
   {'holder':'资产负债表视角','view':'泡沫破裂后的去杠杆导致长期停滞','basis':'据破裂后信贷与增长表现归纳','sources':['w-en-japanese-asset-price-bubble']},
 ],
 'mississippi-bubble-1720': [
   {'holder':'货币试验视角','view':'纸币与殖民贸易叙事的结合制造了早期现代泡沫','basis':'据劳的改革方案归纳','sources':['w-en-john-law-company']},
   {'holder':'国家信用视角','view':'国家为公司债务背书使私人投机转为主权损失','basis':'据5.14亿里弗赔偿归纳','sources':['w-en-john-law-company']},
 ],
 'stock-crash-1973': [
   {'holder':'滞胀视角','view':'通胀与增长的背离使股票失去估值锚','basis':'据GDP与CPI数据归纳','sources':['w-en-1973-1974-stock-crash']},
   {'holder':'石油冲击视角','view':'油价上涨改变了利润分配格局','basis':'据石油危机时序归纳','sources':['w-en-1973-oil-crisis']},
 ],
 'wall-street-1929': [
   {'holder':'杠杆与心理视角','view':'保证金交易与群体乐观放大了涨幅与跌幅','basis':'据崩盘过程归纳','sources':['w-en-wall-street-crash-1929']},
   {'holder':'货币与制度视角','view':'崩盘本身不足以致萧条，银行倒闭与货币收缩才是关键','basis':'据美联储历史与货币数据归纳','sources':['fed-great-depression']},
 ],
}

for eid, chain in CAUSAL.items():
    f='data/entries/'+eid+'.json'
    d=json.load(open(f,encoding='utf-8'))
    d['causal_chain']=[{'step':s,'sources':[src]} for s,src in chain]
    if eid in SCHOOLS:
        d['schools']=SCHOOLS[eid]
    d['pending_notes']=d.get('pending_notes','')+' 【续作CH】因果链与学派观点已按本条目史实定制。'
    json.dump(d,open(f,'w',encoding='utf-8'),ensure_ascii=False,indent=2)
    print('定制',eid)
