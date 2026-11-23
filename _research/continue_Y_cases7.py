# -*- coding: utf-8 -*-
"""续作Y：新增7条当代市场事件案例(L2,据REST摘要)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：机制示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；具体数值以正文为准。</text></svg>")
    return ''.join(s)

D = [
 ('terra-luna-2022', 'Terra/LUNA 崩盘(2022)', '泡沫', 'U5 21世纪', '21世纪', '全球', '重要',
  '2022年算法稳定币 TerraUSD 与其姊妹代币 LUNA 崩盘，成为加密资产领域标志性事件。',
  'Terra 是一个用于算法稳定币的区块链协议与支付平台，由 Terraform Labs（由 Do Kwon 与 Daniel Shin 共同创立的初创公司）于2018年创建。该项目以其 Terra 算法稳定币及关联的 LUNA 代币最为知名。2022年该体系崩盘，成为加密资产领域的标志性事件。具体规模与后续处置待核实。',
  [{'year': 2018, 'display': '2018年', 'event': 'Terraform Labs 创建 Terra 区块链协议与算法稳定币体系（据 Wikipedia Terra (blockchain)）', 'sources': ['w-en-terra-luna-2022']},
   {'year': 2022, 'display': '2022年', 'event': 'Terra 算法稳定币体系与 LUNA 崩盘（同上；具体日期与规模待核实）', 'sources': ['w-en-terra-luna-2022']}],
  [{'step': '算法稳定币依赖代币互换机制维持锚定 → 内在反身性', 'sources': ['w-en-terra-luna-2022']},
   {'step': '信心动摇致脱锚 → 套利机制反向放大抛压', 'sources': ['w-en-stablecoin']},
   {'step': '稳定币与 LUNA 螺旋崩盘 → 加密市场连锁损失', 'sources': ['w-en-crypto-bubble']}],
  [{'holder': '算法稳定币设计视角', 'view': '无足额储备的算法锚定在压力下易失败', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-stablecoin']},
   {'holder': '反身性/挤兑视角', 'view': '价格下跌自我强化，形成死亡螺旋', 'basis': '待核实', 'sources': ['w-en-bank-run']}],
  '与稳定币脱锚、银行挤兑共享"信心—赎回—抛售"螺旋机制，但缺乏存款保险与最后贷款人。具体异同待核实。'),
 ('gamestop-2021', 'GameStop 空头挤压(2021)', '泡沫', 'U5 21世纪', '21世纪', '美洲', '重要',
  '2021年1月美国游戏零售商 GameStop 等证券发生空头挤压，令部分对冲基金遭受重大损失。',
  '2021年1月，美国电子游戏零售商 GameStop 的股票及其他证券发生空头挤压，对某些对冲基金造成重大财务后果，并使卖空者蒙受重大损失。据维基条目，GameStop 约140%的（流通股）被做空。该事件凸显散户协同交易与卖空风险。具体规模待核实。',
  [{'year': 2021, 'display': '2021年1月', 'event': 'GameStop 等证券发生空头挤压，卖空者重大损失（据 Wikipedia GameStop short squeeze）', 'sources': ['w-en-gamestop-2021']},
   {'year': 2021, 'display': '2021年1月', 'event': '约140%的 GameStop 流通股被做空（同上）', 'sources': ['w-en-gamestop-2021']}],
  [{'step': '做空比例极高（约140%）→ 轧空条件具备', 'sources': ['w-en-gamestop-2021']},
   {'step': '散户协同买入推高股价 → 卖空者被迫回补', 'sources': ['w-en-gamestop-2021']},
   {'step': '回补进一步推高价格 → 对冲基金重大损失', 'sources': ['w-en-short-selling']}],
  [{'holder': '卖空风险视角', 'view': '空头过度拥挤时回补会引发自我强化上涨', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-short-selling']},
   {'holder': '市场结构视角', 'view': '散户协同与社交平台改变博弈结构', 'basis': '待核实', 'sources': ['w-en-gamestop-2021']}],
  '与1901年北太平洋铁路逼空（panic-1901）机制相似：空头拥挤+抢筹；但本轮由散户协同与社交平台驱动。具体异同待核实。'),
 ('china-2015-turbulence', '中国股市动荡(2015–2016)', '泡沫', 'U5 21世纪', '21世纪', '亚洲', '重要',
  '2015年6月12日股市泡沫破裂引发动荡，至2016年2月初结束；上交所A股一月内损失三分之一市值。',
  '2015—2016年中国股市动荡始于2015年6月12日股市泡沫的破裂，至2016年2月初结束。据维基条目，事件发生后的一个月内，上海证券交易所A股损失了三分之一的市值。此后出现重大后续影响。具体政策应对与影响待核实。',
  [{'year': 2015, 'display': '2015年6月12日', 'event': '股市泡沫破裂，动荡开始（据 Wikipedia 2015–2016 Chinese stock market turbulence）', 'sources': ['w-en-china-2015-turbulence']},
   {'year': 2015, 'display': '泡沫破裂后一个月内', 'event': '上交所A股市值损失三分之一（同上）', 'sources': ['w-en-china-2015-turbulence']},
   {'year': 2016, 'display': '2016年2月初', 'event': '动荡阶段结束（同上）', 'sources': ['w-en-china-2015-turbulence']}],
  [{'step': '杠杆资金推动股市泡沫 → 估值脱离基本面', 'sources': ['w-en-china-2015-turbulence']},
   {'step': '泡沫破裂 → 强制平仓与抛售螺旋', 'sources': ['w-en-margin-finance']},
   {'step': 'A股一月内损失三分之一市值 → 波及实体与全球市场', 'sources': ['w-en-china-2015-turbulence']}],
  [{'holder': '杠杆/强制平仓视角', 'view': '融资盘在下跌中触发平仓、放大跌幅', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-margin-finance']},
   {'holder': '泡沫破裂视角', 'view': '估值回归是主导机制', 'basis': '待核实', 'sources': ['w-en-speculative-bubble']}],
  '与1929、1987、2000年泡沫破裂共享"杠杆—抛售—平仓"螺旋，但中国市场以散户与融资盘为主。具体异同待核实。'),
 ('oil-price-war-2020', '2020年俄沙油价战', '其他', 'U5 21世纪', '21世纪', '全球', '重要',
  '2020年3月8日沙特对俄罗斯发起油价战，导致油价季度下跌65%。',
  '2020年3月8日，沙特阿拉伯对俄罗斯发起石油价格战，促成了油价在该季度的65%跌幅。价格战由石油输出国组织（OPEC）与俄罗斯之间的对话破裂所引发。该事件与新冠疫情需求冲击叠加，造成油价历史性暴跌。具体影响待核实。',
  [{'year': 2020, 'display': '2020年3月8日', 'event': '沙特对俄发起石油价格战（据 Wikipedia 2020 Russia–Saudi Arabia oil price war）', 'sources': ['w-en-oil-price-war-2020']},
   {'year': 2020, 'display': '2020年第一季度', 'event': '油价季度下跌65%（同上）', 'sources': ['w-en-oil-price-war-2020']}],
  [{'step': 'OPEC 与俄罗斯减产谈判破裂 → 沙特发动价格战', 'sources': ['w-en-oil-price-war-2020']},
   {'step': '供给激增叠加疫情需求骤降 → 油价暴跌65%（季度）', 'sources': ['w-en-oil-price-war-2020']},
   {'step': '产油国财政与能源企业承压，市场剧烈波动', 'sources': ['w-en-covid-crash-2020']}],
  [{'holder': '供给冲击视角', 'view': '价格战造成的供给激增是主因', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-oil-price-war-2020']},
   {'holder': '需求冲击视角', 'view': '疫情封锁致需求崩塌，与供给冲击叠加', 'basis': '待核实', 'sources': ['w-en-covid-crash-2020']}],
  '与1973、1979年石油危机方向相反（前者为供给减少推高油价），本轮为供给激增叠加需求崩塌压低油价。具体异同待核实。'),
 ('bond-crisis-1994', '1994年债券市场危机', '债务', 'U4 20世纪下半', '20世纪下半', '全球', '重要',
  '1994年发达国家债券价格突然下跌（“大债券屠杀”），始于日本与美国并蔓延全球。',
  '1994年债券市场危机（或称"大债券屠杀"）是发达世界债券市场价格的突然下跌。它始于日本与美国，随后蔓延至世界其他地区。在1990年代初衰退之后，利率处于历史低位，美联储转向加息引发债市剧烈调整。具体幅度待核实。',
  [{'year': 1994, 'display': '1994年', 'event': '发达国家债券价格突然下跌，始于日本与美国（据 Wikipedia 1994 bond market crisis）', 'sources': ['w-en-bond-crisis-1994']},
   {'year': 1994, 'display': '1994年', 'event': '下跌蔓延至全球债券市场（同上）', 'sources': ['w-en-bond-crisis-1994']}],
  [{'step': '1990年代初衰退后利率处历史低位 → 久期敞口集中', 'sources': ['w-en-bond-crisis-1994']},
   {'step': '美联储转向加息 → 债券价格急跌', 'sources': ['w-en-bond-crisis-1994']},
   {'step': '杠杆与久期风险暴露 → 全球债市连锁调整', 'sources': ['w-en-interest-rate']}],
  [{'holder': '利率风险视角', 'view': '低利率环境下的久期错配放大调整', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-interest-rate']},
   {'holder': '政策转向视角', 'view': '货币政策意外转向是直接触发', 'basis': '待核实', 'sources': ['w-en-monetary-policy']}],
  '与2022年全球债市调整机制相似（加息引发久期损失），但1994年以发达国家为主。具体异同待核实。'),
 ('credit-suisse-2023', '瑞信被瑞银收购(2023)', '银行', 'U5 21世纪', '21世纪', '欧洲', '重要',
  '2023年3月19日瑞银同意以30亿瑞郎全股票收购瑞信，由瑞士政府与FINMA促成、瑞士央行支持。',
  '2023年3月19日，瑞士银行瑞银集团（UBS）同意以30亿瑞郎（CHF 3 billion）的全股票交易收购瑞信（Credit Suisse），该交易由瑞士政府与瑞士金融市场监管局（FINMA）促成，瑞士国家银行通过提供支持协助完成。这是2008年以来最大的银行并购之一。具体条款与影响待核实。',
  [{'year': 2023, 'display': '2023年3月19日', 'event': '瑞银同意以30亿瑞郎全股票收购瑞信（据 Wikipedia Acquisition of Credit Suisse by UBS）', 'sources': ['w-en-credit-suisse-2023']},
   {'year': 2023, 'display': '2023年3月', 'event': '交易由瑞士政府与FINMA促成，瑞士央行提供支持（同上）', 'sources': ['w-en-credit-suisse-2023']}],
  [{'step': '瑞信信誉与资本受一系列丑闻与亏损侵蚀 → 存款与股价流失', 'sources': ['w-en-credit-suisse-2023']},
   {'step': '信心崩塌加速 → 监管促成紧急并购以避免无序倒闭', 'sources': ['w-en-bank-resolution']},
   {'step': '瑞银以30亿瑞郎收购 → 系统重要性银行整合', 'sources': ['w-en-sifi']}],
  [{'holder': '系统重要性视角', 'view': 'SIFI 无序倒闭风险迫使当局促成并购', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-sifi']},
   {'holder': '处置/信心视角', 'view': '信心流失速度超过资本缓冲消耗', 'basis': '待核实', 'sources': ['w-en-bank-run']}],
  '与2023年硅谷银行事件同期，同属"存款快速流失+监管紧急处置"模式；瑞士以跨境并购而非破产处置。具体异同待核实。'),
 ('crypto-bubble', '加密货币泡沫', '泡沫', 'U5 21世纪', '21世纪', '全球', '重要',
  '市场日益认为加密资产价格相对其假想价值被高估的现象；加密史上有多次投机泡沫。',
  '加密货币泡沫是一种现象：市场日益认为加密资产当前价格相对其假想价值而言被高估。加密货币的历史以多次从繁荣到崩溃的投机泡沫为特征。其价格波动剧烈、缺乏内在现金流锚定，估值争议很大。具体案例与规模待核实。',
  [{'year': 2017, 'display': '2010年代起', 'event': '加密资产多次出现从繁荣到崩溃的投机泡沫（据 Wikipedia Cryptocurrency bubble）', 'sources': ['w-en-crypto-bubble']},
   {'year': 2022, 'display': '2022年', 'event': 'Terra/LUNA 与多家加密机构崩盘，泡沫破裂的典型阶段（同上；细节待核实）', 'sources': ['w-en-terra-luna-2022']}],
  [{'step': '叙事与资金涌入推高价格 → 估值脱离任何现金流基准', 'sources': ['w-en-crypto-bubble']},
   {'step': '杠杆与散户参与放大涨幅 → 泡沫累积', 'sources': ['w-en-leverage']},
   {'step': '信心逆转 → 价格崩塌与机构连锁违约', 'sources': ['w-en-crypto-bubble']}],
  [{'holder': '投机泡沫视角', 'view': '缺乏基本面锚定使价格易暴涨暴跌', 'basis': '据维基摘要归纳；待核实', 'sources': ['w-en-crypto-bubble']},
   {'holder': '技术创新视角', 'view': '底层技术价值与代币价格未必一致', 'basis': '待核实', 'sources': ['w-en-cryptocurrency']}],
  '与郁金香狂热、南海泡沫共享"叙事驱动+杠杆+崩塌"结构；但加密资产全球化、24小时交易、监管分散。具体异同待核实。'),
]

for eid, title, cat, unit, period, region, tier, ol, ov, tl, causal, schools, comp in D:
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': tier,
        'unit': unit, 'period': period, 'region': region, 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': tl,
        'causal_chain': causal,
        'key_data': [],
        'schools': schools,
        'policy_response': [{'holder': '政策当局', 'view': '应对措施及效果待核实', 'basis': '需多来源印证', 'sources': [causal[0]['sources'][0]]}],
        'comparison': comp,
        'svg': svg(title, [tl[0]['event'][:12], '传导', '后果']),
        'sources': list(dict.fromkeys([s for c in causal for s in c['sources']])),
        'related': [], 'needs_verification': True,
        'pending_notes': 'L2：时间线与机制据维基摘要；具体数值、政策规模与影响程度待核实补充。【续作Y】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r43_cases.json', encoding='utf-8'))
for eid, v in meta.items():
    sid = 'w-en-' + eid
    if sid in ex:
        continue
    sd['sources'].append({
        'id': sid, 'title': v['title'], 'author': 'Wikipedia contributors', 'year': '2026',
        'type': '权威百科', 'url': 'https://en.wikipedia.org/wiki/' + v['slug'], 'url2': None,
        'verified': True, 'link_ok': True,
        'note': 'Wikipedia REST API核对(本会话抓取摘要)'
    })
    ex.add(sid)
sd['count'] = len(sd['sources'])
json.dump(sd, open('data/sources.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('来源总数', len(sd['sources']))

cov = json.load(open('coverage.json', encoding='utf-8'))
have = {e['id'] for e in cov['entries']}
for eid, title, cat, unit, period, region, tier, ol, ov, tl, causal, schools, comp in D:
    if eid in have:
        continue
    cov['entries'].append({
        'id': eid, 'level': 'L2', 'tier': tier, 'status': 'written',
        'source_count': 2, 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': unit, 'period': period, 'region': region, 'crisis_type': cat})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
