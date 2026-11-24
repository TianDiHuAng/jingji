# -*- coding: utf-8 -*-
"""续作EW：注册来源并创建第二批 15 个概念条目。"""
import json
import os
import re

GOOD = ['toxic-assets', 'junk-bond', 'payment-system', 'prisoners-dilemma', 'property-rights',
        'transaction-cost', 'savings', 'investment', 'demand', 'population', 'inequality',
        'labour-market', 'specialization', 'tax-incidence', 'buyback']

META = {
 'toxic-assets': ('有毒资产', '制度', '重要', '价值大幅下跌或已无法合理估值的金融资产；危机中常成为处置与救助的核心对象。'),
 'junk-bond': ('垃圾债', '制度', '重要', '信用评级低于投资级的债务工具（亦称高收益债）；其违约率与利差随周期显著波动。'),
 'payment-system': ('支付系统', '制度', '重要', '用于在参与者之间清算与结算资金债权的基础设施；其稳定性是金融体系运转的前提。'),
 'prisoners-dilemma': ('囚徒困境', '理论', '重要', '两个自利主体在缺乏信任与约束时选择"背叛"、结果双双更差的博弈结构。'),
 'property-rights': ('产权', '理论', '重要', '对资源使用、收益与转让的排他性权利；其界定与执行影响投资与交易的发生。'),
 'transaction-cost': ('交易成本', '理论', '重要', '达成与执行交易所需的成本（搜寻、议价、监督、履约）；是解释制度为何存在的核心概念。'),
 'savings': ('储蓄', '理论', '重要', '收入中未用于消费的部分；是投资的可贷资金来源，也是长期增长的条件之一。'),
 'investment': ('投资', '理论', '重要', '为未来收益而投入资源的行为；宏观上指资本形成（固定投资与存货变动）。'),
 'demand': ('需求', '理论', '重要', '在给定价格与条件下消费者愿意且有购买能力的数量；与供给共同决定价格与交易量。'),
 'population': ('人口', '理论', '补充', '一定区域内人的总体；其规模与结构通过劳动供给、储蓄与需求影响长期增长。'),
 'inequality': ('不平等', '理论', '重要', '收入或财富在社会成员之间分布的不均程度；常用基尼系数与份额指标度量。'),
 'labour-market': ('劳动市场', '理论', '重要', '劳动供给与需求相遇的场所与制度安排；工资、就业与失业在此决定。'),
 'specialization': ('专业化', '理论', '重要', '个体或地区专注于特定生产环节；通过分工提高效率，是增长与贸易的基础。'),
 'tax-incidence': ('税负归宿', '理论', '重要', '税收的最终经济负担归属于谁（生产者、消费者或要素所有者），与法定纳税人可能不同。'),
 'buyback': ('股票回购', '制度', '补充', '公司买回自家股份的行为；可减少股本、提升每股收益，亦常被用作向股东返还现金的手段。'),
}

src = json.load(open('data/sources.json', encoding='utf-8'))
have = {x['id'] for x in src['sources']}
new_src = 0
batch = {}
for eid in GOOD:
    d = json.load(open('_research/wiki_batch2/%s.json' % eid, encoding='utf-8'))
    batch[eid] = d
    sid = 'w-en-' + eid
    if sid in have:
        continue
    src['sources'].append({
        'id': sid, 'title': d.get('title') or eid,
        'author': 'Wikipedia contributors', 'year': '2026', 'type': '权威百科',
        'url': d.get('url') or ('https://en.wikipedia.org/wiki/' + d['slug']),
        'url2': None, 'verified': True,
        'note': 'REST summary API 核对：页面返回摘要（%d 字符）。' % len(d['extract']),
    })
    new_src += 1
src['count'] = len(src['sources'])
json.dump(src, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('新增来源:', new_src, '| 总数:', src['count'])

created = 0
for eid in GOOD:
    p = 'data/entries/%s.json' % eid
    if os.path.exists(p):
        print('已存在', eid); continue
    d = batch[eid]
    title, ctype, tier, one_line = META[eid]
    sents = re.split(r'(?<=[.!?])\s+', d['extract'].strip())
    body = ' '.join(sents[:3]).strip()
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': tier,
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球',
        'crisis_type': ctype, 'one_line': one_line,
        'overview': '（据 Wikipedia「%s」摘要归纳）%s 具体定义边界与争议待核实。' % (d.get('title') or eid, body),
        'timeline': [], 'causal_chain': [], 'schools': [], 'key_data': [],
        'comparison': '', 'related': [],
        'sources': ['w-en-' + eid], 'needs_verification': True,
        'pending_notes': '【续作EW】维基恢复后第二批新建；待补辨析与关联。',
    }
    json.dump(entry, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    created += 1
print('新建条目:', created)
