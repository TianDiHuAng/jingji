# -*- coding: utf-8 -*-
"""续作ET：注册维基来源并创建 19 个概念条目（内容匹配的批次）。"""
import json
import glob
import os
import re

# 19 个内容匹配的抓取结果
GOOD = ['convergence', 'counterparty-risk', 'dividend', 'effective-demand', 'equity-premium',
        'eurodollar', 'expectations', 'externality', 'fractional-reserve', 'growth',
        'market-failure', 'modigliani-miller', 'mutual-fund', 'nasdaq', 'proprietary-trading',
        'recession', 'rent-seeking', 'subordination', 'utility']

# 中文标题与分类
META = {
 'growth': ('经济增长', '理论', '核心', '经济体所生产的商品与服务在数量与质量上的增加；通常以剔除通胀后的产出（实际GDP）增长率衡量。'),
 'recession': ('衰退', '理论', '核心', '经济活动普遍而持续的收缩；判定通常依据产出、就业、收入与销售的共同下降，而非单一指标。'),
 'utility': ('效用', '理论', '核心', '个人从某种状态中获得的满足程度的度量；经济学中用作偏好排序与福利分析的基础。'),
 'market-failure': ('市场失灵', '理论', '核心', '自由市场对商品与服务的配置未达到帕累托效率的情形，常导致经济价值的净损失。'),
 'rent-seeking': ('寻租', '理论', '重要', '通过操纵公共政策或经济条件来增加既有财富、而不创造新财富的行为。'),
 'externality': ('外部性', '理论', '重要', '某一方的活动给未参与的第三方带来的成本或收益，未被价格反映。'),
 'expectations': ('预期', '理论', '重要', '在不确定情形下，对最可能发生之结果的信念；它可能符合现实，也可能偏离现实。'),
 'effective-demand': ('有效需求', '理论', '重要', '在另一市场受到约束时实际出现的商品或服务需求；与不受约束的"名义需求"相对。'),
 'convergence': ('收敛', '理论', '重要', '较贫穷经济体的人均收入倾向于比较富裕经济体增长更快的假说。'),
 'modigliani-miller': ('莫迪利亚尼-米勒定理', '理论', '重要', '在无税收、无破产成本等假设下，企业价值与资本结构无关的定理；现代资本结构理论的基准。'),
 'equity-premium': ('股权溢价之谜', '理论', '重要', '一类重要经济模型无法解释股票组合相对于无风险资产的历史平均超额回报的现象。'),
 'counterparty-risk': ('对手方风险', '制度', '重要', '交易对手在己方已履约后未按约定交割证券或支付现金的风险，亦称结算风险。'),
 'fractional-reserve': ('部分准备金银行', '制度', '重要', '银行仅将存款负债的一部分保留为流动性资产作准备、其余用于放贷的银行体系。'),
 'subordination': ('次级化', '制度', '补充', '银行与金融中指对各类资产的求偿权或收益权的优先顺序。'),
 'proprietary-trading': ('自营交易', '制度', '重要', '交易员以公司自有资金买卖证券、债券、外汇、商品及其衍生品以获取利润的行为。'),
 'mutual-fund': ('共同基金', '制度', '重要', '汇集众多投资者资金购买证券的投资基金；该称谓主要用于美国、加拿大与印度。'),
 'nasdaq': ('纳斯达克', '制度', '补充', '美国的证券交易所；按上市公司总市值计为全球最大交易所，亦是首个完全电子化的股票市场。'),
 'eurodollar': ('欧洲美元', '制度', '重要', '存放于美国境外银行或其分支机构的美元计价存款负债。'),
 'dividend': ('股息', '制度', '补充', '公司向股东分配的利润；公司在取得利润或盈余后可将其一部分作为股息支付。'),
}

src = json.load(open('data/sources.json', encoding='utf-8'))
existing_src = {x['id'] for x in src['sources']}
new_src = 0
batch = {}
for eid in GOOD:
    f = '_research/wiki_batch/%s.json' % eid
    d = json.load(open(f, encoding='utf-8'))
    batch[eid] = d
    sid = 'w-en-' + eid
    if sid in existing_src:
        continue
    src['sources'].append({
        'id': sid,
        'title': d.get('title') or eid,
        'author': 'Wikipedia contributors',
        'year': '2026',
        'type': '权威百科',
        'url': d.get('url') or ('https://en.wikipedia.org/wiki/' + d['slug']),
        'url2': None,
        'verified': True,
        'note': 'REST summary API 核对：页面返回摘要（%d 字符）。' % len(d['extract']),
    })
    new_src += 1

src['count'] = len(src['sources'])
json.dump(src, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('新增来源:', new_src, '| 来源总数:', src['count'])

# 创建条目
created = 0
for eid in GOOD:
    path = 'data/entries/%s.json' % eid
    if os.path.exists(path):
        print('已存在，跳过:', eid)
        continue
    d = batch[eid]
    title, ctype, tier, one_line = META[eid]
    # overview：取摘要前 2-3 句，附来源标注
    sentences = re.split(r'(?<=[.!?])\s+', d['extract'].strip())
    body = ' '.join(sentences[:3]).strip()
    entry = {
        'id': eid,
        'title': title,
        'level': 'L2',
        'tier': tier,
        'unit': 'U6 理论与制度',
        'period': '理论制度',
        'region': '全球',
        'crisis_type': ctype,
        'one_line': one_line,
        'overview': '（据 Wikipedia「%s」摘要归纳）%s' % (d.get('title') or eid, body)
                    + ' 具体定义边界与学术争议待核实。',
        'timeline': [],
        'causal_chain': [],
        'schools': [],
        'key_data': [],
        'comparison': '',
        'related': [],
        'sources': ['w-en-' + eid],
        'needs_verification': True,
        'pending_notes': '【续作ET】维基恢复后新建；内容据摘要归纳，需补对照辨析与关联。',
    }
    json.dump(entry, open(path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    created += 1

print('新建条目:', created)
