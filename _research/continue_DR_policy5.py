# -*- coding: utf-8 -*-
"""续作DR：第三批人工核验补写policy_response。"""
import json

POL = {
 'crisis-1914': ('英格兰银行急剧上调贴现率：7月30日由3%升至4%、7月31日升至8%、8月1日升至10%；'
   '美国国会于1914年8月4日通过法案，允许银行以不超过资本125%的规模发行货币以缓解现钞短缺；'
   '各国随后普遍采取交易所关闭与债务延期偿付等措施。',
   '据本条目正文（主体：英格兰银行/美国国会/各国当局；动作：加息、增发、关闭交易所、延期偿付）'),
 'crisis-third-century': ('戴克里先（284年即位）推行行政与货币改革，'
   '并于301年颁布《价格敕令》试图以限价抑制通胀（见 edict-maximum-prices）。',
   '据本条目正文（主体：戴克里先；动作：行政与货币改革、限价敕令）'),
 'cypriot-2013': ('2013年3月的救助协议规定：10万欧元以下的保险存款不受影响，'
   '超过10万欧元的存款被征收47.5%（即存款减记/bail-in），以此换取外部救助。',
   '据本条目正文（主体：救助方与塞浦路斯当局；动作：存款减记协议）'),
 'chinese-hyper-1937': ('货币改革尝试：1948年推行金圆券改革，但未能止住通胀而失败'
   '（正文将其记为危机的收场方式）。',
   '据本条目正文（动作：1948年金圆券改革及其失败）'),
 'continental-currency-1775': ('清算安排：1790年代美国宪法批准后，大陆币可按面值的1%兑换国债'
   '（即以极低比率折算为联邦债务）。',
   '据本条目正文（主体：美国联邦政府；动作：按1%面值兑换国债）'),
}

for eid, (view, basis) in POL.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if d.get('policy_response'):
        print('跳过（已有）', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
        'basis': basis + '；具体细节与效果评价待核实', 'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DR】policy_response 人工核验撰写。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补写', eid)
