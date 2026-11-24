# -*- coding: utf-8 -*-
"""续作DX：第九批补写（本批仅2条有政策依据）。"""
import json

POL = {
 'bcci': ('多国监管机构的联合行动：1991年该行因大规模欺诈与洗钱被**多国监管机构关闭**'
   '（正文将其记为跨境银行监管失效的经典案例）。',
   '据本条目正文（主体：多国监管机构；动作：关闭该行）'),
 'bear-stearns': ('危机处置：2008年该公司因流动性枯竭而被**紧急收购**'
   '（正文未给出交易条款细节，具体安排待核实）。',
   '据本条目正文（动作：紧急收购；属危机中的应急处置）'),
}

for eid, (view, basis) in POL.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if d.get('policy_response'):
        print('跳过（已有）', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
        'basis': basis + '；具体细节与效果评价待核实', 'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DX】policy_response 人工核验撰写。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补写', eid)
print()
# 统计剩余条目的状况
import glob as g
cases = [json.load(open(x, encoding='utf-8')) for x in g.glob('data/entries/*.json')]
cases = [c for c in cases if not c['unit'].startswith('U6')]
nopol = [c['id'] for c in cases if not c.get('policy_response')]
print('仍无 policy_response 的案例:', len(nopol))
