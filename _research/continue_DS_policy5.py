# -*- coding: utf-8 -*-
"""续作DS：第四批人工核验补写policy_response。"""
import json

POL = {
 'edict-maximum-prices': ('戴克里先于301年颁布《价格敕令》：谴责贪婪，并为所有重要物品与服务'
   '设定最高价格与工资，试图以行政限价抑制通胀；但因普遍规避与供给萎缩而难以奏效。',
   '据本条目正文（主体：戴克里先；动作：颁布限价敕令，含价格与工资上限）'),
 'european-banking-1931': ('货币制度层面的应对是放弃金本位：德国于1931年7月15日退出金本位，'
   '英国随后于1931年9月19日退出——以此摆脱维持平价的通缩约束、恢复货币政策空间。',
   '据本条目正文（动作：退出金本位）'),
 'euro-area-crisis': ('危机应对以财政紧缩为核心，并伴随外部救助；'
   '希腊2009年预算赤字由最初预测的"6—8%"修正为12.7%（马斯特里赫特上限为3%），'
   '统计失真直到2009年9月才被纠正——这一暴露本身推动了财政统计监管的强化。',
   '据本条目正文（动作：财政紧缩、外部救助、赤字统计修正）'),
 'egypt-2023': ('埃及政府与埃及中央银行对埃及镑实施贬值，以应对持续的外汇短缺'
   '（正文同时指出外汇紧张使汇率与偿付承压）。',
   '据本条目正文（主体：政府与中央银行；动作：本币贬值）'),
 'exchange-equalisation': ('设立外汇平准账户(EEA) 作为英国财政部的一项基金，'
   '持有 SDR、外币与黄金储备，用于在外汇市场干预——'
   '使英国能在不直接改变货币政策的情况下影响汇率。',
   '据本条目正文（主体：英国财政部；动作：设立平准基金、干预外汇市场）'),
}

for eid, (view, basis) in POL.items():
    f = 'data/entries/' + eid + '.json'
    d = json.load(open(f, encoding='utf-8'))
    if d.get('policy_response'):
        print('跳过（已有）', eid); continue
    d['policy_response'] = [{'holder': '政策当局', 'view': view,
        'basis': basis + '；具体细节与效果评价待核实', 'sources': d['sources'][:2]}]
    d['pending_notes'] = (d.get('pending_notes', '') + ' 【续作DS】policy_response 人工核验撰写。')
    json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('补写', eid)
