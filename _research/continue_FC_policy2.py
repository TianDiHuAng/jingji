# -*- coding: utf-8 -*-
"""续作FC：补写 first-republic 与 franklin-national-1974 的 policy_response。"""
import json
import os

POL = {
 'first-republic': (
   '**私营部门联合存款**：2023年3月16日，包括摩根大通、美国银行、富国银行、花旗集团与 '
   'Truist Financial 在内的 **11 家美国银行**向 First Republic 存入 **300 亿美元**，'
   '以缓解挤兑担忧并支持存款提取；但该行股价仍继续下跌，3月19日标普再降三级至垃圾级。'
   '**监管处置**：2023年5月1日，加州金融保护与创新部关闭该行、联邦存款保险公司(FDIC)接管资产，'
   '摩根大通在竞拍中胜出并收购。'
   '该行在危机期间的季度财报显示客户提取存款达 **1045 亿美元**。',
   '据 Wikipedia「First Republic Bank」Collapse 章节及导言；'
   '政策主体：11家大型银行（私营）/加州监管机构/FDIC；动作：联合存款、关闭接管、竞拍出售'),

 'franklin-national-1974': (
   '**最后贷款人提供流动性但未能挽救**：1974年中该行披露巨额亏损后储户大量提款，'
   '该行不得不向**联邦储备银行借入超过 10 亿美元**；'
   '1974年10月8日，该行仍因管理不善与欺诈（外汇投机损失与不良贷款政策）被宣布**无偿付能力**。'
   '事后追究了刑事责任（1975年国际部前执行副主席对欺诈认罪）。'
   '该案常被作为"美联储提供流动性支持但机构仍因资不抵债而倒闭"的早期范例，'
   '与1984年大陆伊利诺伊的"全面保护存款人"形成对照。',
   '据 Wikipedia「Franklin National Bank」Collapse 章节；'
   '政策主体：联邦储备银行；动作：提供超10亿美元贷款（最终仍宣告无偿付能力）'),
}

n = 0
for eid, (view, basis) in POL.items():
    p = 'data/entries/%s.json' % eid
    if not os.path.exists(p):
        print('无条目', eid); continue
    d = json.load(open(p, encoding='utf-8'))
    if d.get('policy_response'):
        print('已有', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
                             'basis': basis + '；效果评价待核实',
                             'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作FC】基于维基全文补写policy_response。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1; print('补写', eid)

import glob
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
cases = [e for e in es if not e['unit'].startswith('U6')]
wp = sum(1 for e in cases if e.get('policy_response'))
print('本轮累计补写 %d | 案例政策覆盖 %d/%d = %d%%' % (n, wp, len(cases), wp * 100 // len(cases)))
