# -*- coding: utf-8 -*-
"""续作DU：第六批人工核验补写policy_response。"""
import json

POL = {
 'kipper-wipper-1618': ('1623年前后各邦推行"置币改革"（Kipper- und Wipperzeit 的终结），'
   '恢复足色货币——代价是伴随债务减记与财富再分配。',
   '据本条目正文（主体：神圣罗马帝国各邦；动作：置币改革、恢复足色货币）'),
 'mississippi-bubble-1720': ('重组安排：法国国家向印度公司支付5.14亿里弗赔偿', 
   '据本条目正文（主体：法国国家/摄政王；动作：向公司支付赔偿以恢复偿付能力，并保留原股东特权）'),
 'lebanese-liquidity-2019': ('央行的应对包括：以黎镑公债置换外币（欧元债）债务，规模约20亿美元；'
   '银行体系对存款实施事实上的提取限制，储户资产被冻结。'
   '（正文指出"谁承担损失"的重组方案仍是核心争议。）',
   '据本条目正文（主体：央行/银行体系；动作：债务置换、存款提取限制）'),
 'london-econ-1933': ('国际协调尝试：66国于1933年6月12日—7月27日集会，'
   '拟就抗击大萧条、复兴贸易与稳定汇率达成协议；因美国不愿承诺汇率稳定、'
   '而金集团与英国希望恢复汇率秩序，会议最终失败。'
   '此后各国转向双边与帝国特惠安排（渥太华协定体系）。',
   '据本条目正文（主体：66国；动作：召开会议与协议失败）'),
 'mini-crash-1997': ('交易所层面的即时应对：因跌幅触发规则，纽约证券交易所**提前收市**'
   '（当时尚无现代全市场熔断，采用的是交易暂停规则）；'
   '该事件直接推动了此后美国对"熔断机制"的制度化讨论与1998年规则的引入。',
   '据本条目正文（主体：纽交所/监管；动作：提前收市、引入熔断规则）'),
}

for eid, (view, basis) in POL.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if d.get('policy_response'):
        print('跳过（已有）', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
        'basis': basis + '；具体细节与效果评价待核实', 'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DU】policy_response 人工核验撰写。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补写', eid)
