# -*- coding: utf-8 -*-
"""续作DW：第八批人工核验补写policy_response。"""
import json

POL = {
 'puerto-rico-debt-2014': ('应对措施包括：将销售税提高至 **11%**；'
   '并依据《波多黎各监督、管理与经济稳定法》(PROMESA) 进入类似破产的重组程序'
   '（由财政监督与管理委员会主持）。',
   '据本条目正文（主体：波多黎各当局/美国国会授权的监督委员会；动作：增税、PROMESA重组）'),
 'rhode-island-banking-1990': ('1991年1月1日 RISDIC 被宣告无力偿付后，州政府随即**关闭了数十家**'
   '依赖该保险的机构，储户一度无法取款；州政府随后**为部分存款提供担保**并推动重组。',
   '据本条目正文（主体：罗得岛州政府；动作：关闭机构、为部分存款担保、推动重组）'),
 'rodrigazo-1975': ('一揽子紧缩措施（"罗德里加索"）：比索一次性大幅贬值（对美元官方汇率近乎翻倍）、'
   '大幅提高公用事业与燃料价格、并提高利率，意图纠正长期失衡与实际汇率高估。'
   '（正文同时记录其后果：物价与工资急剧上涨、实际工资暴跌、通胀加速失控。）',
   '据本条目正文（主体：阿根廷经济部；动作：贬值、提价、加息）'),
}

for eid, (view, basis) in POL.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if d.get('policy_response'):
        print('跳过（已有）', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
        'basis': basis + '；具体细节与效果评价待核实', 'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DW】policy_response 人工核验撰写。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补写', eid)
