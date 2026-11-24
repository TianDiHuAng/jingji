# -*- coding: utf-8 -*-
"""续作DP：人工核验后补写policy_response（仅限overview中有明确政策依据者）。"""
import json

POL = {
 'bank-crisis-2023': ('监管应对包括：全额保护两家倒闭银行（SVB、Signature）的未保险存款；'
   '设立银行定期融资计划(BTFP)；动用美联储流动性工具。',
   '据本条目正文（政策主体：监管/美联储；动作：全额保护、设立BTFP、流动性工具）'),
 'argentina-crisis-2001': ('终结比索与美元的可兑换制度（"兑换计划"）并发生主权违约；'
   '约2003年上半年GDP恢复增长，其后五年平均增速约9%、超过危机前水平；2006年全额偿还IMF贷款。',
   '据本条目正文（动作：终结兑换制、违约、偿债；后果数据见正文）'),
 'assignat-1790s': ('1790年4月17日指券被宣布为法定清偿手段（利率降至3%）；'
   '1790年8月27日制宪议会决定再发行19亿指券；其后持续超发导致恶性通胀，最终于1796年被废止。',
   '据本条目正文（主体：制宪议会；动作：法定清偿、再发行、废止）'),
 'banking-act-1935': ('该法由国会于1935年8月19日通过、8月23日签署，'
   '改变美联储体系的结构与权力分配（变革始于1933年银行法）。',
   '据本条目正文（主体：国会/总统；动作：立法改组央行体系）'),
 'archegos-2021': ('2021年崩盘时监管未介入救助，损失由各银行自行承担；'
   '事后以刑事追责处理——2024年11月 Hwang 因联邦欺诈与敲诈勒索被判18年监禁。',
   '据本条目正文（事实：无救助；动作：刑事起诉与判决）'),
 'albania-pyramid-1997': ('骗局崩盘后秩序崩溃、武装抢劫军械库、大规模移民外流，'
   '最终由国际干预介入并推动重建。',
   '据本条目正文（主体：国际社会；动作：干预与重建）'),
}

for eid, (view, basis) in POL.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if d.get('policy_response'):
        print('跳过（已有）', eid); continue
    d['policy_response'] = [{
        'holder': '政策当局',
        'view': view,
        'basis': basis + '；具体措施细节与效果评价待核实',
        'sources': d['sources'][:2],
    }]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DP】policy_response 人工核验撰写。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补写', eid)
