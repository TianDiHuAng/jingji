# -*- coding: utf-8 -*-
"""续作GA：为 L3 条目中缺 policy_response 的核心案例补写。"""
import json
import os
import glob

POL = {
 'lehman': (
   '**未获救助，通过破产与业务出售处置**：**2008年9月13日**（周六），'
   '时任纽约联邦储备银行行长盖特纳召集会议讨论雷曼的前途，会议包含"紧急（救助）"的可能性；'
   '雷曼最终未获公共资金救助。'
   '**9月15日**雷曼依据**第11章**申请破产保护（此前客户大规模撤离、股价暴跌）。'
   '**次（16）日**英国巴克莱银行宣布达成协议，将收购雷曼的"重大且具控制性的权益"'
   '（须经监管批准）；**9月20日**修订版协议获美国破产法院法官 James M. Peck 批准。'
   '**随后一周**野村控股宣布收购雷曼亚太区（含日本）业务。'
   '其破产使全球市场随即暴跌。',
   '据 Wikipedia「Lehman Brothers」Bankruptcy／Liquidation 章节；'
   '政策主体：纽约联储（召集会议但不注资）／破产法院；处置方式：第11章破产＋业务分拆出售'),

 'subprime-crisis-2007': (
   '**大规模公共干预**：美国政府以一系列措施稳定金融体系，包括'
   '**问题资产救助计划(TARP)** 与 **2009 年美国复苏与再投资法(ARRA)**。'
   'TARP 的法律依据《紧急经济稳定法》于 **2008年10月3日**签署生效；'
   '据记载伯南克当时对议员表示："如果我们不做这件事，周一我们可能就没有经济了。"'
   '**监管改革**：**多德-弗兰克法**针对危机暴露的问题（资本与流动性要求、'
   '系统性风险监管权限等）作出回应，但**未拆分最大的银行**——后者因并购而变得更大。'
   '**财政结果的量级**：到 2018 年 1 月，计入贷款利息后美国的救助资金**已全部收回**'
   '（总额约 6,260 亿美元）；而 2008—2012 年间与危机相关的银行损失与失业估计达 9,400 亿欧元量级。',
   '据 Wikipedia「Subprime mortgage crisis」相关章节；'
   '政策主体：美国国会/财政部/美联储；动作：TARP、ARRA、多德-弗兰克法'),
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
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作GA】补写policy_response（L3条目结构完整化）。')
    json.dump(d, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('补写', eid)

# 复查 L3 结构完整性
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
l3 = [e for e in es if e.get('level') == 'L3']
miss = [(e['id'], [x for x in ('deep_svg','l3_detail','key_data','timeline','policy_response') if not e.get(x)])
        for e in l3]
miss = [m for m in miss if m[1]]
print('\nL3 共 %d 条 | 仍不完整 %d 条' % (len(l3), len(miss)))
for m in miss:
    print('  %-28s 缺: %s' % (m[0], ','.join(m[1])))
