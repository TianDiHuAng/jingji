# -*- coding: utf-8 -*-
"""续作HH：新建 4 个概念条目（externalities / var / pigouvian-tax / common-pool）。"""
import json
import os
import glob

NEW = {
 'externalities': {
   'title': '外部性',
   'tier': '重要',
   'one_line': '某一方的活动给未参与交易的第三方带来成本或收益，而该成本/收益未反映在价格中。',
   'overview': ('外部性是经济活动的成本或收益落在**未参与交易的第三方**身上、而未被定价的情形。'
                '负外部性（污染、拥堵）使私人成本低于社会成本，产量超过社会最优；'
                '正外部性（教育、防疫、基础研究）使私人收益低于社会收益，供给不足。'
                '庇古的传统解法是征税/补贴以"内部化"外部性；科斯则指出，'
                '若产权清晰且交易成本低，当事人可自行议价解决，无需政府介入。'
                '金融领域的系统性风险常被视为一种负外部性——个体机构的风险承担成本由全体承担。'),
   'timeline': [
     {'year': 1920, 'event': '庇古在《福利经济学》中系统分析外部性，提出征税/补贴的矫正思路（据 Wikipedia Externality）'},
     {'year': 1960, 'event': '科斯《社会成本问题》提出：产权清晰且交易成本低时，当事人可自行议价解决外部性（据 Wikipedia Externality）'},
   ],
   'schools': [
     ('庇古传统', '外部性源于价格未反映社会成本，应由政府以税收/补贴矫正（据 Wikipedia Externality）', 'w-en-externalities'),
     ('科斯传统', '若产权清晰、交易成本足够低，当事人可通过议价自行解决，政府只需界定产权（据 Wikipedia Externality）', 'w-en-externalities'),
   ],
   'comparison': ('与**公共品**的区别：外部性是"影响他人但未定价"，公共品是"非竞争且非排他"；'
                  '两者常同时出现（如基础研究既产生正外部性又是公共品）。'
                  '与**市场失灵**的关系：外部性是市场失灵的一类原因，'
                  '但不是全部（信息不对称、市场势力同样导致失灵）。'),
   'related': ['market-failure', 'pigouvian-tax', 'common-pool', 'public-choice', 'coase-theorem'],
   'sources': ['w-en-externalities'],
 },
 'var': {
   'title': '风险价值(VaR)',
   'tier': '重要',
   'one_line': '在给定置信水平与持有期内，投资组合可能遭受的最大损失估计。',
   'overview': ('风险价值(Value at Risk, VaR) 估计在**给定概率与持有期**下，一组投资可能损失多少。'
                '例如"1 日 99% VaR 为 100 万元"意味着：正常市场条件下，有 99% 的把握单日损失不超过 100 万元，'
                '或者说约有 1% 的概率损失超过该数额。'
                '计算方法主要有三种：**历史模拟法**（用历史数据重放）、**方差-协方差法**（假设正态分布）、'
                '**蒙特卡洛模拟**（生成大量情景）。'
                'VaR 的关键局限是**不告诉你超过阈值后会有多严重**——即"尾部"信息缺失，'
                '这使它在极端事件中可能低估风险。'),
   'timeline': [
     {'year': 1994, 'event': '摩根大通公开发布 RiskMetrics 方法，使 VaR 成为行业标准（据 Wikipedia Value at risk）'},
     {'year': 1996, 'event': '巴塞尔委员会允许银行用内部模型（含 VaR）计量市场风险资本（据 Wikipedia Value at risk）'},
   ],
   'schools': [
     ('VaR 的实用价值', '用一个数字概括组合风险，便于限额管理与资本计量，成为行业与监管的共同语言（据 Wikipedia Value at risk）', 'w-en-var'),
     ('VaR 的批评', 'VaR 不满足次可加性（组合 VaR 可能大于各部分之和），且不描述尾部损失的规模——'
                    '危机中实际损失常远超 VaR 估计（据 Wikipedia Value at risk）', 'w-en-var'),
   ],
   'comparison': ('与**压力测试**的区别：VaR 描述"正常条件下的常规损失"，压力测试描述"极端情景下会怎样"；'
                  '两者互补而非替代。与**预期损失(Expected Shortfall)** 的区别：'
                  '后者对超过 VaR 的部分取平均，因此包含尾部信息，被巴塞尔III用于替代市场风险 VaR。'),
   'related': ['risk-management', 'basel-iii', 'procyclicality', 'leverage-ratio', 'stress-test'],
   'sources': ['w-en-var'],
 },
 'pigouvian-tax': {
   'title': '庇古税',
   'tier': '重要',
   'one_line': '对产生负外部性的市场活动征税，使私人成本等于社会成本。',
   'overview': ('庇古税是对**产生负外部性**的活动征收的税，税额应等于该活动造成的边际外部成本，'
                '从而把外部成本"内部化"到行为主体的决策中。'
                '其逻辑是：当价格反映真实社会成本时，产量会降到社会最优水平。'
                '**实践难题**是外部成本难以精确计量（如碳排放的社会成本估算区间很宽），'
                '因此现实中多用**代理税基**（如按燃料含碳量征税而非按实际排放）。'
                '庇古税还与"**双重红利假说**"相关：若税收用于降低其他扭曲性税种，'
                '可能同时获得环境改善与效率提升两重收益——但该假说的成立条件在文献中有争议。'),
   'timeline': [
     {'year': 1920, 'event': '庇古在《福利经济学》中提出以税收矫正负外部性的思路（据 Wikipedia Pigouvian tax）'},
     {'year': 1990, 'event': '芬兰、瑞典等国开征碳税，成为庇古税的最大规模实践（据 Wikipedia Pigouvian tax）'},
   ],
   'schools': [
     ('庇古式矫正', '按边际外部成本征税可使产量回到社会最优（据 Wikipedia Pigouvian tax）', 'w-en-pigouvian-tax'),
     ('双重红利假说的争议', '若税收收入用于削减其他扭曲性税种，可能同时改善环境与效率；'
                            '但该结论依赖于税制初始扭曲程度与收入使用方式，实证结果不一'
                            '（据 Wikipedia Pigouvian tax Double-dividend hypothesis）', 'w-en-pigouvian-tax'),
   ],
   'comparison': ('与**总量控制与交易（cap and trade）**的区别：庇古税固定**价格**、让数量随市场调整；'
                  '总量控制固定**数量**、让价格浮动。两者的不确定性来源不同——'
                  '若边际减排成本曲线陡峭，价格工具更优；若边际损害曲线陡峭，数量工具更优。'
                  '与**一般消费税**的区别：后者为筹资，前者为矫正行为。'),
   'related': ['externalities', 'market-failure', 'tax-incidence', 'carbon-pricing', 'coase-theorem'],
   'sources': ['w-en-pigouvian-tax'],
 },
 'common-pool': {
   'title': '公共池资源',
   'tier': '重要',
   'one_line': '规模大而难以排他、但一方的使用会减少他人可用量的资源。',
   'overview': ('公共池资源(CPR) 是一类**难以排他但具竞争性**的资源系统——'
                '如渔场、灌溉系统、地下水层、牧场。'
                '它与**公共品**的区别在于竞争性：一个人捕捞会减少他人可捕的量；'
                '与**私人品**的区别在于排他困难。'
                '传统分析（哈丁"公地悲剧"）认为此类资源必然被过度使用，'
                '但奥斯特罗姆的实证研究显示：**使用者社群可通过自定的规则实现可持续管理**，'
                '既不必然需要私有化，也不必然需要国家管制。'
                '金融稳定具有类似结构：金融机构对共同流动性与市场深度的依赖，'
                '使个体行为在压力下相互削弱。'),
   'timeline': [
     {'year': 1968, 'event': '哈丁发表"公地悲剧"，提出公共资源必然被过度使用的论断（据 Wikipedia Common-pool resource）'},
     {'year': 1990, 'event': '奥斯特罗姆《公共事物的治理之道》以大量案例证明社群自治理可行（据 Wikipedia Common-pool resource）'},
   ],
   'schools': [
     ('公地悲剧', '个体理性导致集体非理性：无人能排除他人使用，因此所有人竞相过度使用（据 Wikipedia Common-pool resource）', 'w-en-common-pool'),
     ('奥斯特罗姆的自主治理', '使用者社群可通过清晰边界、集体选择规则、分级制裁与冲突解决机制实现可持续管理；'
                              '既非必然私有化，也非必然国有化（据 Wikipedia Common-pool resource）', 'w-en-common-pool'),
   ],
   'comparison': ('与**公共品**的区别：公共品非竞争（一人消费不减他人），公共池资源具竞争性。'
                  '与**公地悲剧**的关系：后者是对前者的一种（悲观的）理论预测，而非同义词。'
                  '与金融的类比：市场流动性常被比作公共池资源——个体抛售会抽干共同的流动性池。'),
   'related': ['market-failure', 'externalities', 'prisoners-dilemma', 'coordination-games', 'lender-of-last-resort'],
   'sources': ['w-en-common-pool'],
 },
}

# 需要注册的来源元数据
SRCMETA = {
 'w-en-externalities': ('Externality', 'https://en.wikipedia.org/wiki/Externality'),
 'w-en-var': ('Value at risk', 'https://en.wikipedia.org/wiki/Value_at_risk'),
 'w-en-pigouvian-tax': ('Pigouvian tax', 'https://en.wikipedia.org/wiki/Pigouvian_tax'),
 'w-en-common-pool': ('Common-pool resource', 'https://en.wikipedia.org/wiki/Common-pool_resource'),
}

sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
have = {s['id'] for s in sj['sources']}
for sid, (title, url) in SRCMETA.items():
    if sid not in have:
        sj['sources'].append({
            'id': sid, 'title': title, 'author': 'Wikipedia contributors', 'year': '2026',
            'type': '权威百科', 'url': url, 'url2': None, 'verified': True, 'link_ok': True,
            'note': 'Wikipedia API 核对（本会话抓取全文）',
        })
        print('注册来源:', sid)
sj['count'] = len(sj['sources'])
json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

ids = {json.load(open(f, encoding='utf-8'))['id'] for f in glob.glob('data/entries/*.json')}
n = 0
for eid, v in NEW.items():
    if eid in ids:
        print('已存在，跳过:', eid)
        continue
    d = {
        'id': eid, 'title': v['title'], 'level': 'L2', 'tier': v['tier'],
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球',
        'crisis_type': '理论' if eid != 'var' else '制度',
        'one_line': v['one_line'], 'overview': v['overview'],
        'timeline': v['timeline'], 'causal_chain': [], 'schools': v['schools'],
        'key_data': [], 'comparison': v['comparison'],
        'related': [r for r in v['related'] if r in ids or r in NEW],
        'sources': v['sources'], 'needs_verification': True,
        'pending_notes': '【续作HH】维基全文可用后新建；内容据全文归纳，数值与学派归属待核实。',
    }
    d['related'] = [r for r in d['related'] if r in ids or r in NEW]
    json.dump(d, open('data/entries/%s.json' % eid, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('新建:', eid)

# 更新 coverage.json 与 scope.md
cov = json.load(open('coverage.json', encoding='utf-8'))
covids = {e['id'] for e in cov['entries']}
for eid in NEW:
    if eid not in covids:
        cov['entries'].append({'id': eid, 'level': 'L2', 'tier': NEW[eid]['tier'],
                               'status': 'written', 'source_count': 1, 'needs_verification': 1,
                               'last_updated': '2026-11-24', 'unit': 'U6 理论与制度',
                               'period': '理论制度', 'region': '全球',
                               'crisis_type': '理论' if eid != 'var' else '制度'})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage.json 条目:', cov['total'])
