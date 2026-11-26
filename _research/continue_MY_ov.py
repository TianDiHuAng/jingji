import json
ADD={
'austrian-theory':'奥地利学派本身于1871年起源于维也纳，代表人物有门格尔（Carl Menger）、庞巴维克（Eugen von Böhm-Bawerk）与维塞尔（Friedrich von Wieser），方法论上主张从人的行动的基本公理推导理论，而非主要依赖统计分析；1974年哈耶克与缪尔达尔（Gunnar Myrdal）分享诺贝尔经济学奖后，该学派重新受到关注。',
'leading-indicator':'按与商业周期的时间关系，经济指标分为领先、同步与滞后三类；领先指标通常（但并非总是）先于整体经济变化，包括消费者预期指数、建筑许可与信贷条件等。美国经济咨商局（Conference Board）发布由十个指标构成的综合领先经济指数，用于预示美国经济未来六到九个月的活动。',
'bretton-woods':'1944年7月1日至22日，44个同盟国代表在布雷顿森林的华盛顿山酒店开会；当时掌握世界三分之二黄金的美国坚持体系须同时以黄金和美元为基础。苏联代表出席会议但后来拒绝批准协定。',
'minsky-theory':'“明斯基时刻”一词由太平洋投资管理公司（PIMCO）的保罗·麦卡利（Paul McCulley）于1998年提出，用以描述1998年俄罗斯金融危机；麦卡利将2008年金融危机的明斯基时刻定在2007年8月，也有人定在稍早或稍晚，例如2007年6月贝尔斯登两只基金的倒闭。',
'marxist-theory':'作为非主流学派，马克思主义经济学受到内部不一致、预测失败等批评，斯蒂格勒（George Stigler）与索洛（Robert Solow）等经济学家认为它与现代经济学关系不大；但其关于资本积累与商业周期的部分概念被主流吸收，熊彼特的“创造性破坏”即为一例。',
}
for eid,t in ADD.items():
    p=f'data/entries/{eid}.json';raw=open(p,encoding='utf-8',newline='').read();crlf='\r\n' in raw;e=json.loads(raw)
    e['overview']=e['overview'].rstrip('。')+'。'+t
    s=json.dumps(e,ensure_ascii=False,indent=2)+'\n';open(p,'w',encoding='utf-8',newline='').write(s.replace('\n','\r\n') if crlf else s)
    print(eid,len(e['overview']))
