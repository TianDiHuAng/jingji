# -*- coding: utf-8 -*-
"""续作DQ：第二批人工核验补写policy_response。"""
import json

POL = {
 'black-friday-1869': ('格兰特总统识破逼空企图后，下令财政部抛售国库黄金——'
   '1869年9月政府释放了约400万美元黄金，金价随即崩跌。',
   '据本条目正文（主体：总统/财政部；动作：抛售国库黄金）'),
 'black-monday-1987': ('直接的政策/制度反应是引入"熔断机制"(circuit breaker)：'
   '此后美国建立了按跌幅暂停交易的规则，以打断程序化抛售的自我强化。'
   '（正文同时指出，本次崩盘未引发银行体系危机，与1929年形成对照。）',
   '据本条目正文（动作：建立熔断规则；属制度性应对）'),
 'brazil-hyper-1980': ('先后推出多次稳定计划——1986年克鲁扎多计划、1987年布雷塞尔计划、'
   '1989年夏季计划、1990年科洛尔计划（其中1990年计划一度冻结约80%的流动性），'
   '均未持久奏效；最终以1994年"雷亚尔计划"(Plano Real) 结合财政调整与事实上的汇率锚'
   '终结了恶性通胀。',
   '据本条目正文（主体：巴西政府；动作：多轮稳定计划、流动性冻结、汇率锚）'),
 'cameroon-crisis-1987': ('与IMF/世界银行展开结构调整(SAP)谈判并接受条件；'
   '1994年1月CFA法郎对法国法郎贬值50%，以提升出口竞争力——'
   '代价是外币债务负担与进口价格骤升、短期通胀与社会压力加剧。',
   '据本条目正文（主体：政府/IMF/世行；动作：结构调整、汇率贬值）'),
}

for eid, (view, basis) in POL.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if d.get('policy_response'):
        print('跳过（已有）', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
        'basis': basis + '；具体细节与效果评价待核实', 'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DQ】policy_response 人工核验撰写。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补写', eid)
