# -*- coding: utf-8 -*-
"""续作HK：新建 4 个概念条目（actuarial / bullion / lloyds / deindustrialization）。

注意（吸取 round 77 教训）：
  1. 建条目前逐个确认 id 与标题均不存在
  2. schools 一律用 dict 格式写入
  3. 来源先查 sources.json，避免重复注册
"""
import glob
import json
import os

NEW = {
 'actuarial': {
   'title': '精算',
   'tier': '补充',
   'type': '制度',
   'one_line': '用数学与统计方法评估保险、养老金与金融中的风险的学科。',
   'overview': ('精算是把数学与统计方法用于**评估保险、养老金、金融与投资中的风险**的学科。'
                '其核心工具包括生命表（死亡率建模）、损失分布拟合、准备金计提与偿付能力测算。'
                '精算与金融经济学的交汇点在于**风险定价**：保费应覆盖预期损失、风险边际与费用，'
                '而风险边际的确定依赖于对尾部风险的建模。'
                '2008 年危机后，精算在**偿付能力监管**（如欧盟 Solvency II）中的作用显著加强——'
                '从"事后计提"转向"基于风险的资本要求"。'),
   'timeline': [
     {'year': 1693, 'event': '哈雷制作第一张以实证数据为基础的生命表，为寿险精算奠基'
                             '（据 Wikipedia Actuarial science）'},
     {'year': 1848, 'event': '伦敦成立精算师协会，精算成为独立职业'
                             '（据 Wikipedia Actuarial science）'},
     {'year': 2016, 'event': '欧盟 Solvency II 生效，把基于风险的资本要求制度化'
                             '（据 Wikipedia Actuarial science）'},
   ],
   'schools': [
     ('精算的风险观', '以**大数定律**为基础，把不确定性转化为可定价的分布；'
                      '但该框架对**相关性突变**（如危机中的同时违约）较为脆弱'
                      '（据 Wikipedia Actuarial science）', 'w-en-actuarial'),
     ('与金融经济学的差异', '精算传统强调主观概率与审慎边际，金融经济学强调无套利与市场一致性定价；'
                            '两者在 1990 年代后逐步融合（据 Wikipedia Actuarial science）', 'w-en-actuarial'),
   ],
   'comparison': ('与**风险管理(VaR)** 的区别：精算关注长期（数十年）保险负债的分布与准备金，'
                  'VaR 关注短期（1日—1年）交易组合的损失阈值。'
                  '与**会计计提**的区别：精算准备金基于概率模型，会计计提遵循准则规定，'
                  '两者的差距在危机中常成为争议焦点。'),
   'related': ['deposit-insurance', 'risk-management', 'insurance-history', 'var', 'moral-hazard'],
 },
 'bullion': {
   'title': '金银块（贵金属）',
   'tier': '补充',
   'type': '制度',
   'one_line': '经精炼至高标准纯度的非铁金属块，尤指用于铸币与储备的金银。',
   'overview': ('金银块(bullion) 指经精炼至**高标准纯度**的非铁金属，通常特指金与银，'
                '形态为块、条或锭，而非铸币。它既是**货币体系的储备基础**（金本位时代），'
                '也是当代的**避险资产**。'
                '金银的货币角色与价格之间有一个结构性特点：'
                '当货币与贵金属挂钩时，货币政策受制于金银的可得性；'
                '脱钩后，金银价格反而更能自由反映市场对通胀与信用的预期。'
                '伦敦金银市场是全球贵金属交易与定价的中心，其定价机制经历了从'
                '"定盘价"（fixing）到电子化拍卖的变化。'),
   'timeline': [
     {'year': 1717, 'event': '牛顿任皇家铸币厂长时确立金衡，英国事实上转向金本位'
                             '（据 Wikipedia Bullion）'},
     {'year': 1919, 'event': '伦敦金银市场协会的前身开始每日"定盘价"定价'
                             '（据 Wikipedia Bullion）'},
     {'year': 2015, 'event': '伦敦金银定盘价机制因操纵丑闻被电子拍卖取代'
                             '（据 Wikipedia Bullion）'},
   ],
   'schools': [
     ('货币属性视角', '金银作为**最终结算手段**，在信用货币体系受疑时充当价值锚'
                      '（据 Wikipedia Bullion）', 'w-en-bullion'),
     ('商品属性视角', '金银价格由供需（首饰、工业、投资）决定，其"货币溢价"难以单独计量'
                      '（据 Wikipedia Bullion）', 'w-en-bullion'),
   ],
   'comparison': ('与**金本位**的区别：金本位是一种**货币制度安排**（本币可兑换固定量黄金），'
                  '金银块是**实物商品**；金本位可以废除，金银块的价值不会归零。'
                  '与**外汇储备**的区别：后者是他人负债，前者是无对手方风险的实物资产。'),
   'related': ['gold-standard', 'gold-bloc', 'exchange-equalisation', 'commodity-price-index', 'seigniorage'],
 },
 'lloyds': {
   'title': '劳合社',
   'tier': '重要',
   'type': '制度',
   'one_line': '伦敦的保险与再保险市场，由多个承保辛迪加组成，本身不是保险公司。',
   'overview': ('劳合社(Lloyd\'s of London) 是位于伦敦的**保险与再保险市场**，'
                '其特点在于它**本身不是保险公司**，而是由多个独立承保辛迪加组成的 marketplace：'
                '每个辛迪加自负盈亏，成员以**无限责任**（后改为有限）承担赔付。'
                '这一结构使劳合社能承保其他市场不愿承保的特殊风险（航运、航空、巨灾、政治风险），'
                '但也意味着**风险在成员间分散、而非由单一资本金吸收**。'
                '1980—90 年代劳合社经历严重危机：石棉索赔、污染责任与一系列巨灾叠加，'
                '导致大量个人成员（Names）破产，最终促成公司化改革。'),
   'timeline': [
     {'year': 1688, 'event': '爱德华·劳埃德在伦敦开设咖啡馆，成为船东与承保人聚集地'
                             '（据 Wikipedia Lloyd\'s of London）'},
     {'year': 1871, 'event': '首个《劳合社法》确立其法律地位'
                             '（据 Wikipedia Lloyd\'s of London）'},
     {'year': 1996, 'event': '劳合社完成公司化改革：个人无限责任成员被有限责任公司取代'
                             '（据 Wikipedia Lloyd\'s of London）'},
   ],
   'schools': [
     ('辛迪加模式的优点', '风险由多个独立承保人分散承担，能覆盖单一机构不敢承保的特殊风险'
                          '（据 Wikipedia Lloyd\'s of London）', 'w-en-lloyds'),
     ('无限责任的争议', '成员以全部个人财产承担赔付，在巨灾叠加时导致大量个人破产；'
                        '批评者认为这一结构把系统性风险转嫁给不具备风险承受力的个人'
                        '（据 Wikipedia Lloyd\'s of London）', 'w-en-lloyds'),
   ],
   'comparison': ('与**股份制保险公司**的区别：后者的股东责任以出资额为限，'
                  '劳合社的成员（1980年代前）承担无限责任。'
                  '与**再保险**的区别：劳合社是市场平台，本身不承担风险；'
                  '再保险公司是风险的最终承担者。'
                  '与**交易所**的区别：交易所撮合标准化合约，劳合社承保定制化风险。'),
   'related': ['insurance-history', 'counterparty-risk', 'risk-pooling', 'actuarial', 'catastrophe-bond'],
 },
 'deindustrialization': {
   'title': '去工业化',
   'tier': '重要',
   'type': '理论',
   'one_line': '一国或地区工业产能与制造业活动比重持续下降的社会经济过程。',
   'overview': ('去工业化指一国或地区**工业产能或制造业活动比重持续下降**的过程，'
                '通常表现为制造业就业与产出占GDP 比重下滑。'
                '其成因在文献中分为几类：**生产率提升**（同样产出只需更少工人）、'
                '**外包与离岸**（生产环节转移到成本更低地区）、'
                '**需求结构变化**（服务消费占比上升）、以及**贸易竞争**。'
                '去工业化是否构成"问题"取决于视角：'
                '若源于生产率提升，它是**富裕的结果**；'
                '若源于产业转移与贸易冲击，则伴随**区域衰落与就业极化**——'
                '后者是民粹主义与贸易保护诉求的经济基础之一。'),
   'timeline': [
     {'year': 1970, 'event': '主要发达经济体的制造业就业占比开始持续下降'
                             '（据 Wikipedia Deindustrialization）'},
     {'year': 1990, 'event': '全球化与离岸外包加速，制造业向低成本地区转移'
                             '（据 Wikipedia Deindustrialization）'},
     {'year': 2008, 'event': '金融危机后"再工业化"成为多国政策议题'
                             '（据 Wikipedia Deindustrialization）'},
   ],
   'schools': [
     ('生产率视角', '制造业就业下降主要是生产率提升的结果——产出未减而用工减少，'
                    '这是增长的表现而非衰退（据 Wikipedia Deindustrialization）', 'w-en-deindustrialization'),
     ('贸易与外包视角', '产业转移与进口竞争导致特定地区工业岗位消失，'
                        '造成区域性的长期失业与收入下降（据 Wikipedia Deindustrialization）',
      'w-en-deindustrialization'),
   ],
   'comparison': ('与**产业升级**的区别：升级指向更高附加值环节移动，可能伴随制造业就业下降但产出上升；'
                  '去工业化是**比重**概念，不必然意味着升级。'
                  '与**荷兰病**的区别：后者由资源出口导致的汇率升值压制制造业，'
                  '去工业化的成因更广。'),
   'related': ['dutch-disease', 'structural-adjustment', 'globalisation', 'inequality', 'labour-market'],
 },
}

SRCMETA = {
 'w-en-actuarial': ('Actuarial science', 'https://en.wikipedia.org/wiki/Actuarial_science'),
 'w-en-bullion': ('Bullion', 'https://en.wikipedia.org/wiki/Bullion'),
 'w-en-lloyds': ("Lloyd's of London", 'https://en.wikipedia.org/wiki/Lloyd%27s_of_London'),
 'w-en-deindustrialization': ('Deindustrialization', 'https://en.wikipedia.org/wiki/Deindustrialization'),
}

# 0) 先核对是否已存在（避免 round 77 的重复建条目）
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
ids = {e['id'] for e in es}
titles = {e['title'] for e in es}
skip = []
for eid, v in NEW.items():
    if eid in ids or v['title'] in titles:
        skip.append(eid)
        print('跳过（已存在）:', eid, v['title'])
if skip:
    for s in skip:
        NEW.pop(s)

# 1) 注册来源（查重）
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
have_src = {s['id'] for s in sj['sources']}
for sid, (title, url) in SRCMETA.items():
    if sid not in have_src:
        sj['sources'].append({
            'id': sid, 'title': title, 'author': 'Wikipedia contributors', 'year': '2026',
            'type': '权威百科', 'url': url, 'url2': None, 'verified': True, 'link_ok': True,
            'note': 'Wikipedia API 核对（本会话抓取全文）',
        })
        print('注册来源:', sid)
sj['count'] = len(sj['sources'])
json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

# 2) 建条目
n = 0
for eid, v in NEW.items():
    d = {
        'id': eid, 'title': v['title'], 'level': 'L2', 'tier': v['tier'],
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球',
        'crisis_type': v['type'],
        'one_line': v['one_line'], 'overview': v['overview'],
        'timeline': v['timeline'], 'causal_chain': [],
        'schools': [{'holder': h, 'view': vw, 'sources': [src]} for h, vw, src in v['schools']],
        'key_data': [], 'comparison': v['comparison'],
        'related': [r for r in v['related'] if r in ids],
        'sources': ['w-en-' + eid], 'needs_verification': True,
        'pending_notes': '【续作HK】据维基全文新建；数值与学派归属待核实。',
    }
    json.dump(d, open('data/entries/%s.json' % eid, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    n += 1
    print('新建:', eid)

# 3) coverage
cov = json.load(open('coverage.json', encoding='utf-8'))
covids = {e['id'] for e in cov['entries']}
for eid, v in NEW.items():
    if eid not in covids:
        cov['entries'].append({'id': eid, 'level': 'L2', 'tier': v['tier'], 'status': 'written',
                               'source_count': 1, 'needs_verification': 1,
                               'last_updated': '2026-11-24', 'unit': 'U6 理论与制度',
                               'period': '理论制度', 'region': '全球', 'crisis_type': v['type']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('新建 %d 条 | coverage total: %d' % (n, cov['total']))
