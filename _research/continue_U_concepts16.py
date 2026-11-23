# -*- coding: utf-8 -*-
"""续作U：新增16条金融工具/市场/核算概念(L2,据REST摘要)。"""
import json

def svg(t, labels):
    e = lambda s: str(s).replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')[:20]
    s = ["<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 760 200' role='img'>",
         f"<text x='20' y='28' class='ttl'>{e(t)}：概念示意</text>"]
    for x, lb in zip([20, 270, 520], labels):
        s.append(f"<g><rect x='{x}' y='55' width='210' height='52' rx='6' class='box'/>"
                 f"<text x='{x+9}' y='82' class='lbl'>{e(lb)}</text></g>")
    s.append("<line x1='230' y1='81' x2='265' y2='81' class='ar'/>"
             "<line x1='480' y1='81' x2='515' y2='81' class='ar'/>")
    s.append("<text x='20' y='150' class='note'>来源见本页；定义据标准口径。</text></svg>")
    return ''.join(s)

D = [
 ('bond', '债券', '制度',
  '发行者（债务人）对持有人（债权人）负有债务、须提供现金流的证券。',
  '在金融中，债券是一种证券：发行者（债务人）对持有人（债权人）负有债务，并有义务向债权人提供现金流。这通常包括在约定期限内支付利息，并在到期时偿还本金。债券价格与利率反向变动。具体品种待核实。',
  [('发行人借款 → 承诺按期付息、到期还本', 'w-en-bond'),
   ('投资者购买债券 → 获得固定或浮动现金流', 'w-en-bond'),
   ('利率上升 → 存量债券价格下跌', 'w-en-interest-rate')],
  [('固定收益视角', '债券提供可预期现金流与分散化', 'w-en-bond'),
   ('利率风险视角', '久期越长对利率变动越敏感', 'w-en-yield-curve')],
  ['w-en-bond', 'w-en-interest-rate'], []),
 ('stock', '股票', '制度',
  '公司所有权被划分成的全部股份，单股代表按比例的 fractional 所有权。',
  '股票由公司所有权被划分成的全部股份构成。单份股票意味着按总股数比例的 fractional 所有权，通常赋予股东相应权利（如分红与投票）。股票价格反映市场对公司未来现金流的预期，波动性高于债券。具体权利待核实。',
  [('公司发行股份 → 投资者获得所有权份额', 'w-en-stock'),
   ('股东按比例享有分红与剩余索取权', 'w-en-stock'),
   ('预期变化 → 股价波动，影响融资与财富', 'w-en-speculative-bubble')],
  [('股权视角', '股票提供增长收益与风险分担', 'w-en-stock'),
   ('泡沫视角', '股价可因投机显著偏离基本面', 'w-en-speculative-bubble')],
  ['w-en-stock', 'w-en-speculative-bubble'], []),
 ('option', '期权', '制度',
  '赋予持有人以约定执行价格在指定日期或之前买入或卖出标的资产权利的合约（非义务）。',
  '在金融中，期权是一种合约，赋予其所有者（持有人）按合约规定、在某一指定日期或之前以指定执行价格买入或卖出特定数量标的资产或工具的权利，而非义务。期权是衍生品的基本类型之一。具体定价待核实。',
  [('买方支付权利金 → 获得买入或卖出的权利', 'w-en-option'),
   ('可选择行权或放弃 → 风险收益不对称', 'w-en-option'),
   ('用于对冲或投机，定价依赖波动率等参数', 'w-en-black-scholes')],
  [('对冲视角', '期权可用于限定风险敞口', 'w-en-option'),
   ('投机视角', '杠杆与非线性收益吸引投机，也可能放大波动', 'w-en-derivative')],
  ['w-en-option', 'w-en-black-scholes'], []),
 ('futures', '期货合约', '制度',
  '在期货交易所、于未来指定时间以预定价格买卖某物的标准化法律合约。',
  '在金融中，期货合约是标准化法律合约：在彼此尚不知晓的双方之间，约定在未来指定时间以预定价格买卖某物。交易标的通常是商品或金融工具。期货用于对冲价格风险与投机，实行保证金与每日结算。具体机制待核实。',
  [('双方约定未来价格与交割时间 → 标准化合约', 'w-en-futures'),
   ('缴纳保证金、每日盯市结算', 'w-en-margin-finance'),
   ('用于对冲或投机，交割或平仓了结', 'w-en-futures')],
  [('套期保值视角', '期货转移价格风险', 'w-en-futures'),
   ('杠杆/投机视角', '保证金交易放大波动与外溢风险', 'w-en-margin-finance')],
  ['w-en-futures', 'w-en-margin-finance'], []),
 ('swap', '掉期（互换）', '制度',
  '双方按约定公式交换两笔现金流序列的合约，属衍生品。',
  '在金融中，掉期（互换）是双方约定按某一公式交换一笔现金流序列与另一笔现金流序列的合约，属于衍生品。最常见类型是利率互换：一方支付固定利率、另一方支付浮动利率。掉期用于管理利率、汇率与信用风险。具体品种待核实。',
  [('双方约定交换现金流公式 → 签订掉期合约', 'w-en-swap'),
   ('利率互换：固定与浮动利率现金流互换', 'w-en-swap'),
   ('用于对冲或调整资产负债的利率敏感度', 'w-en-derivative')],
  [('风险管理视角', '掉期可精细调整利率与汇率敞口', 'w-en-swap'),
   ('对手方风险视角', '场外掉期存在不透明与对手方风险', 'w-en-otc')],
  ['w-en-swap', 'w-en-derivative'], []),
 ('risk-premium', '风险溢价', '理论',
  '个人因承受更高风险而要求的超额回报。',
  '风险溢价是个人因承受更高风险水平而要求的超额回报的度量，广泛用于金融与经济学，一般定义为预期风险回报减去无风险回报。风险溢价的大小反映市场对风险的定价与厌恶程度。具体测算待核实。',
  [('投资者厌恶风险 → 要求高于无风险利率的补偿', 'w-en-risk-premium'),
   ('以预期风险回报减无风险回报衡量', 'w-en-risk-premium'),
   ('风险厌恶上升 → 溢价扩大、资产价格下跌', 'w-en-financial-accelerator')],
  [('资产定价视角', '风险溢价是风险定价的核心', 'w-en-risk-premium'),
   ('危机视角', '压力下溢价骤升、融资骤紧', 'w-en-sudden-stop')],
  ['w-en-risk-premium', 'w-en-financial-accelerator'], []),
 ('beta', '贝塔系数', '理论',
  '衡量单只股票价格相对整个股市变动的预期涨跌幅度的统计量。',
  '在金融中，贝塔是用来衡量单只股票价格相对整个股票市场变动的预期涨跌幅度的统计量。贝塔可用于表示单个资产对市场风险的贡献，是资本资产定价模型的核心参数。具体测算待核实。',
  [('以个股收益对市场收益回归 → 得到贝塔', 'w-en-beta'),
   ('贝塔大于1 → 波动放大；小于1 → 波动较小', 'w-en-beta'),
   ('用于估计要求回报率与系统性风险贡献', 'w-en-capm')],
  [('CAPM 视角', '贝塔衡量不可分散风险的暴露', 'w-en-beta'),
   ('行为/实证批判视角', '单一贝塔难以刻画全部风险', 'w-en-behavioral-finance')],
  ['w-en-beta', 'w-en-capm'], []),
 ('open-market-operation', '公开市场操作', '制度',
  '中央银行与银行或银行群体交换本币流动性的活动。',
  '在宏观经济学中，公开市场操作（OMO）是中央银行与某家银行或一组银行交换本币流动性的活动。央行可在公开市场买卖政府债券及其他金融资产，以调节银行体系流动性。它是货币政策最常用的日常工具。具体操作待核实。',
  [('央行在公开市场买入或卖出证券 → 投放或回笼流动性', 'w-en-open-market-operation'),
   ('银行体系准备金变化 → 短期利率受影响', 'w-en-open-market-operation'),
   ('传导至信贷与总需求', 'w-en-monetary-policy')],
  [('工具视角', 'OMO 灵活、可日常微调流动性', 'w-en-open-market-operation'),
   ('局限视角', '零利率下限时效果受限', 'w-en-quantitative-easing')],
  ['w-en-open-market-operation', 'w-en-monetary-policy'], []),
 ('discount-window', '贴现窗口', '制度',
  '允许符合条件的机构向中央银行短期借款、以应对临时流动性短缺的货币政策工具。',
  '贴现窗口是一种货币政策工具，允许符合条件的机构通常以短期方式向中央银行借款，以应对由内部或外部扰动造成的临时流动性短缺。贴现窗口是最后贷款人职能的具体操作渠道之一。具体条件待核实。',
  [('机构遭遇临时流动性短缺 → 向央行申请借款', 'w-en-discount-window'),
   ('以合格抵押品获得短期资金', 'w-en-discount-window'),
   ('发挥最后贷款人功能、遏制挤兑传染', 'w-en-lender-of-last-resort')],
  [('流动性支持视角', '贴现窗口可快速缓解临时短缺', 'w-en-discount-window'),
   ('污名效应视角', '使用贴现窗口可能被视为机构虚弱的信号', 'w-en-bank-run')],
  ['w-en-discount-window', 'w-en-lender-of-last-resort'], []),
 ('primary-market', '一级市场', '制度',
  '资本市场中由发行人直接向购买者发行并出售证券、发行人获得价款的部分。',
  '一级市场是资本市场的一部分，处理由发行人直接向购买者发行并出售证券的事务，发行人是价款收取方。一级市场即新发行证券的市场，区别于已发行证券在投资者之间转手的二级市场。具体机制待核实。',
  [('发行人直接向投资者发行新证券 → 募集资金', 'w-en-primary-market'),
   ('发行人获得发行价款', 'w-en-primary-market'),
   ('证券随后在二级市场流通交易', 'w-en-secondary-market')],
  [('融资视角', '一级市场为企业与政府提供融资渠道', 'w-en-primary-market'),
   ('定价视角', '发行定价影响抑价与投资者认购意愿', 'w-en-initial-public-offering')],
  ['w-en-primary-market', 'w-en-secondary-market'], []),
 ('secondary-market', '二级市场', '制度',
  '已发行金融工具（股票、债券、期权、期货等）在投资者之间买卖的市场，亦称流通市场。',
  '二级市场（亦称流通市场、售后市场）是此前已发行的金融工具（如股票、债券、期权与期货）被买卖的金融市场。与发行人向购买者首次出售证券的一级市场不同，二级市场交易在投资者之间进行，提供流动性与价格发现。具体机制待核实。',
  [('已发行证券在投资者之间转手 → 形成二级市场', 'w-en-secondary-market'),
   ('提供流动性与连续定价', 'w-en-secondary-market'),
   ('价格发现反馈影响一级市场发行', 'w-en-primary-market')],
  [('流动性视角', '二级市场为持有者提供退出渠道', 'w-en-secondary-market'),
   ('价格发现视角', '交易价格反映市场预期与信息', 'w-en-efficient-market')],
  ['w-en-secondary-market', 'w-en-primary-market'], []),
 ('gnp', '国民总收入(GNI)', '制度',
  '一国居民所获得的要素收入总额，前称国民生产总值(GNP)。',
  '国民总收入（GNI），前称国民生产总值（GNP），是一国居民所获得的要素收入总额。它等于国内生产总值（GDP）加上居民从非居民处获得的要素收入、减去付给非居民的要素收入。GNI 与 GDP 的区别在于是否考虑跨境要素收入。具体口径待核实。',
  [('居民提供要素获得收入 → 汇总为要素收入总额', 'w-en-gnp'),
   ('GDP 加跨境要素收入净额 → 得到 GNI', 'w-en-gnp'),
   ('用于比较国民收入水平与跨境收入流动', 'w-en-national-income')],
  [('国民视角', 'GNI 关注居民收入而非境内产出', 'w-en-gnp'),
   ('产出视角', 'GDP 关注境内生产活动', 'w-en-gdp')],
  ['w-en-gnp', 'w-en-gdp'], []),
 ('budget-balance', '政府预算平衡', '债务',
  '政府收入与支出之间的差额。',
  '政府预算平衡（亦称一般政府平衡、公共预算平衡或公共财政平衡）是政府收入与支出之间的差额。对采用权责发生制会计的政府，预算平衡按权责发生基础计量。赤字意味着支出超过收入、需通过借债融资。具体口径待核实。',
  [('政府收入与支出对比 → 形成盈余或赤字', 'w-en-budget-balance'),
   ('赤字需通过借债融资 → 政府债务累积', 'w-en-government-debt'),
   ('赤字规模受周期与自动稳定器影响', 'w-en-automatic-stabilizer')],
  [('财政纪律视角', '持续赤字削弱债务可持续性', 'w-en-budget-balance'),
   ('功能财政视角', '衰退期赤字具有稳定作用', 'w-en-fiscal-multiplier')],
  ['w-en-budget-balance', 'w-en-government-debt'], []),
 ('national-income', '国民收入与产出度量', '理论',
  '经济学中用于估计一国或地区总体经济活动的各类指标，包括GDP、GNI、NNI等。',
  '经济学中使用多种国民收入与产出度量来估计一国或地区的总体经济活动，包括国内生产总值（GDP）、国民总收入（GNI）、国民净收入（NNI）以及调整后国民收入等。不同指标侧重不同（境内生产、居民收入、扣除折旧等）。具体差异待核实。',
  [('界定统计范围（境内/国民、总额/净额）→ 选择指标', 'w-en-national-income'),
   ('按生产、收入或支出法核算 → 得到总量', 'w-en-national-income'),
   ('用于比较经济规模、增长与收入水平', 'w-en-gdp')],
  [('核算视角', '多指标体系适配不同分析目的', 'w-en-national-income'),
   ('批判视角', '总量指标无法反映分配与环境代价', 'w-en-gdp')],
  ['w-en-national-income', 'w-en-gdp'], []),
 ('etf', '交易所交易基金(ETF)', '制度',
  '在证券交易所买卖、持有股票债券等金融资产的投资基金。',
  '交易所交易基金（ETF）是一种既属投资基金、又属交易所交易产品的投资工具，即在证券交易所买卖。ETF 持有股票、债券、货币、加密货币、债务与期货合约等金融资产。其费用通常较低、可日内交易，但也可能带来流动性与跟踪误差问题。具体机制待核实。',
  [('基金持有一篮子资产 → 份额在交易所挂牌', 'w-en-etf'),
   ('投资者像股票一样买卖份额 → 获得分散化敞口', 'w-en-etf'),
   ('套利机制使价格贴近净值（偏离时出现折溢价）', 'w-en-secondary-market')],
  [('低成本分散视角', 'ETF 提供便捷、低成本的分散化投资', 'w-en-etf'),
   ('风险视角', '流动性错配与跟踪误差、杠杆型产品放大风险', 'w-en-liquidity')],
  ['w-en-etf', 'w-en-secondary-market'], []),
 ('convertible-bond', '可转换债券', '制度',
  '持有人可按约定转换为发行公司普通股或等值现金的债券，属混合证券。',
  '在金融中，可转换债券（可转换票据）是一种债券，持有人可将其转换为发行公司特定数量的普通股，或转换为等值现金。它是兼具债务与股权特征的混合证券。其定价同时受利率与股价波动影响。具体条款待核实。',
  [('发行人发行债券 → 约定转股条件', 'w-en-convertible-bond'),
   ('持有人可择机转为股票或等值现金', 'w-en-convertible-bond'),
   ('兼具债性与股性，降低发行成本但稀释股权', 'w-en-bond')],
  [('发行人视角', '可转债降低票息、延缓稀释', 'w-en-convertible-bond'),
   ('投资者视角', '兼具下行保护与上行参与', 'w-en-option')],
  ['w-en-convertible-bond', 'w-en-bond'], []),
]

for eid, title, cat, ol, ov, causal, schools, srcs, kds in D:
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': [],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in causal],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in schools],
        'policy_response': [],
        'comparison': '经济学/金融概念条目，与其他概念互补；具体适用与争论待核实。',
        'svg': svg(title, [causal[0][0][:12], causal[1][0][:12], causal[2][0][:12]]),
        'sources': srcs, 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作U】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r39_concepts.json', encoding='utf-8'))
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
for eid, title, cat, ol, ov, causal, schools, srcs, kds in D:
    if eid in have:
        continue
    cov['entries'].append({
        'id': eid, 'level': 'L2', 'tier': '重要', 'status': 'written',
        'source_count': len(srcs), 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
