# -*- coding: utf-8 -*-
"""续作FX：为 overview 中无法溯源的数字加"待核实"标记（诚实标注而非删除）。"""
import json

FIX = {
 'dotcom-bubble-2000': [
   ('1999年高通(Qualcomm)股价上涨2619%，另有12只大盘股涨幅超1000%、7只超900%。',
    '1999年高通(Qualcomm)等个股涨幅惊人（具体涨幅数值待核实：现行来源页面未载 2619%、'
    '超1000%、超900% 三项，需补充出处）。'),
 ],
 'panic-1901': [
   ('5月9日该股一日内从约170美元涨至1000美元附近，',
    '5月9日该股单日暴涨（具体价格数值待核实：现行来源页面未载 170 美元与 1000 美元两项，需补充出处），'),
 ],
}

for eid, pairs in FIX.items():
    p = 'data/entries/%s.json' % eid
    d = json.load(open(p, encoding='utf-8'))
    ov = d['overview']
    changed = 0
    for old, new in pairs:
        if old in ov:
            ov = ov.replace(old, new)
            changed += 1
    d['overview'] = ov
    d['pending_notes'] = (d.get('pending_notes', '')
                          + ' 【续作FX】overview 中 %d 处无来源支撑的具体数值已改为待核实表述。' % changed)
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('%s: 标注 %d 处' % (eid, changed))
