# -*- coding: utf-8 -*-
"""续作T：新增16条周期理论/市场机制/统计指标概念(L2,据REST摘要)。"""
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
 ('debt-deflation', '债务通缩', '理论',
  '认为衰退与萧条源于通缩使债务实际价值上升、引发违约的理论。',
  '债务通缩是一种理论：衰退与萧条源于债务总体水平因通缩而实际价值上升，导致人们对其消费贷款与抵押贷款违约。违约使银行资产下降，加上抵押品价值下跌，进一步收缩信贷、加深萧条。该理论以欧文·费雪为代表。具体机制待核实。',
  [('价格水平下降 → 债务的实际价值上升', 'w-en-debt-deflation'),
   ('借款人违约增加 → 银行资产与抵押品价值下跌', 'w-en-debt-deflation'),
   ('信贷收缩、需求进一步下滑 → 通缩与债务螺旋', 'w-en-great-depression')],
  [('债务通缩视角', '通缩加重实际债务负担，放大萧条', 'w-en-debt-deflation'),
   ('货币视角', '货币收缩是通缩与萧条的根源', 'w-en-money-supply')],
  ['w-en-debt-deflation', 'w-en-great-depression'], []),
 ('balance-sheet-recession', '资产负债表衰退', '理论',
  '私人部门高负债使其集体转向偿债储蓄、而非支出投资，从而导致增长放缓或下降的衰退类型。',
  '资产负债表衰退是一种经济衰退：当私人部门债务水平很高时，个人或企业会集体转向储蓄、优先偿还债务，而非支出或投资，从而导致经济增长放缓或下降。该术语归功于经济学家辜朝明（Richard Koo）。具体机制待核实。',
  [('资产价格下跌 → 私人部门资不抵债、债务高企', 'w-en-balance-sheet-recession'),
   ('企业与家庭集体转向偿债、减少支出与投资', 'w-en-balance-sheet-recession'),
   ('需求持续不足 → 即使利率很低也难以复苏', 'w-en-liquidity-trap')],
  [('资产负债表视角', '私人部门去杠杆使货币政策失效，需财政支持', 'w-en-balance-sheet-recession'),
   ('常规周期视角', '以利率与需求管理解释衰退', 'w-en-business-cycle')],
  ['w-en-balance-sheet-recession', 'w-en-liquidity-trap'], []),
 ('deleveraging', '去杠杆', '理论',
  '降低杠杆比率，即减少单个经济实体资产负债表中债务占比的过程。',
  '在微观经济层面，去杠杆指降低杠杆比率，即减少单个经济实体（如家庭或企业）资产负债表中债务所占的百分比。它是加杠杆的反向过程——加杠杆是借钱购买资产并放大头寸。去杠杆若集中发生，会收缩需求与资产价格。具体机制待核实。',
  [('债务过高或资产价格下跌 → 实体被迫削减债务', 'w-en-deleveraging'),
   ('偿债优先于支出 → 需求与资产价格承压', 'w-en-deleveraging'),
   ('集中去杠杆 → 通缩压力与增长下滑', 'w-en-debt-deflation')],
  [('微观视角', '单个主体的杠杆率调整是风险管理行为', 'w-en-deleveraging'),
   ('宏观视角', '集体去杠杆引发"节俭悖论"式收缩', 'w-en-balance-sheet-recession')],
  ['w-en-deleveraging', 'w-en-leverage'], []),
 ('short-selling', '卖空', '制度',
  '使投资者在资产市场价值下跌时获利的投资方式，与做多相反。',
  '在金融中，对某资产做空意味着以在市场价值下跌时获利的方式投资，与更常见的做多（资产市值上升时获利）相反。卖空者通常借入资产卖出、待价格下跌后买回归还。卖空提供流动性与价格发现，但在压力下可能加剧下跌。具体机制待核实。',
  [('借入资产并卖出 → 建立空头头寸', 'w-en-short-selling'),
   ('价格下跌后买回归还 → 获取价差收益', 'w-en-short-selling'),
   ('集中卖空或逼空 → 加剧价格波动与风险', 'w-en-market-manipulation')],
  [('价格发现视角', '卖空改善定价效率、提供流动性', 'w-en-short-selling'),
   ('稳定视角', '限制卖空以防恐慌性下跌（效果有争议）', 'w-en-market-manipulation')],
  ['w-en-short-selling', 'w-en-market-manipulation'], []),
 ('margin-finance', '保证金交易', '制度',
  '金融工具持有者向对手方缴存的抵押品，用以覆盖其带来的信用风险。',
  '在金融中，保证金是金融工具持有者必须向对手方缴存的抵押品，用于覆盖持有者对对手方构成的部分或全部信用风险。该风险可能源于持有者向对手方借入现金购买金融工具等行为。保证金要求影响杠杆水平与强制平仓风险。具体规则待核实。',
  [('借入资金购买证券 → 需缴存保证金作为抵押', 'w-en-margin-finance'),
   ('价格下跌致保证金不足 → 追加保证金或强制平仓', 'w-en-margin-finance'),
   ('集中平仓 → 放大价格下跌（保证金螺旋）', 'w-en-deleveraging')],
  [('风险控制视角', '保证金限制杠杆、保护对手方', 'w-en-margin-finance'),
   ('顺周期视角', '保证金要求在压力下上升、加剧抛售', 'w-en-deleveraging')],
  ['w-en-margin-finance', 'w-en-leverage'], []),
 ('otc', '场外交易(OTC)', '制度',
  '买卖双方直接在交易所监管之外进行的交易。',
  '场外交易（OTC，或称交易所外交易、粉单交易）由两方直接进行，不受交易所监督，与通过交易所进行的交易形成对照。交易所具有促进流动性、提供透明度等优势，而场外交易更灵活但透明度与对手方风险较高。具体市场待核实。',
  [('双方直接协商交易 → 绕过交易所', 'w-en-otc'),
   ('条款灵活但透明度低、对手方风险高', 'w-en-otc'),
   ('集中清算与信息不透明 → 压力下放大传染', 'w-en-systemic-risk')],
  [('灵活性视角', 'OTC 可定制合约、满足特定对冲需求', 'w-en-otc'),
   ('透明/稳定视角', '缺乏中央清算与披露放大系统性风险', 'w-en-systemic-risk')],
  ['w-en-otc', 'w-en-systemic-risk'], []),
 ('stress-test', '压力测试', '制度',
  '用于判定金融工具或机构应对经济危机能力的分析与模拟。',
  '在金融中，压力测试是一种分析或模拟，旨在判定特定金融工具或金融机构应对经济危机的能力。与基于"最佳估计"的财务预测不同，公司或其监管者会进行压力测试，考察在不利情景下的表现。压力测试已成为危机后监管的重要工具。具体方法待核实。',
  [('设定不利情景（衰退、失业上升、资产下跌等）→ 模拟冲击', 'w-en-stress-test'),
   ('评估资本与流动性是否充足', 'w-en-stress-test'),
   ('据结果要求补充资本或调整风险', 'w-en-capital-requirement')],
  [('审慎工具视角', '压力测试提前暴露脆弱性、增强韧性', 'w-en-stress-test'),
   ('局限视角', '情景假设与现实偏差可能低估风险', 'w-en-value-at-risk')],
  ['w-en-stress-test', 'w-en-capital-requirement'], []),
 ('sifi', '系统重要性金融机构', '制度',
  '其失败可能引发金融危机的银行、保险公司或其他金融机构，俗称"太大而不能倒"。',
  '系统重要性金融机构（SIFI）是指其失败可能触发金融危机的银行、保险公司或其他金融机构。这类机构俗称"太大而不能倒"。因其倒闭外溢巨大，监管对其施加更高资本与处置要求。具体认定标准待核实。',
  [('规模大、关联强、可替代性低 → 失败外溢巨大', 'w-en-sifi'),
   ('被视为"太大而不能倒" → 存在隐性担保预期', 'w-en-too-big-to-fail'),
   ('施加附加资本与处置规划以降低风险', 'w-en-capital-requirement')],
  [('系统性风险视角', 'SIFI 需更严格监管以限制外溢', 'w-en-sifi'),
   ('道德风险视角', '隐性担保诱发过度冒险', 'w-en-moral-hazard')],
  ['w-en-sifi', 'w-en-too-big-to-fail'], []),
 ('money-market', '货币市场', '制度',
  '经济中提供短期资金的组成部分，交易期限一般一年以内的短期贷款。',
  '货币市场是经济中提供短期资金的组成部分，交易短期贷款，期限一般为一年或更短。它是金融机构与央行进行流动性管理、短期融资与政策操作的重要场所。货币市场利率是政策传导的起点。具体工具待核实。',
  [('短期资金供求 → 形成货币市场利率', 'w-en-money-market'),
   ('央行通过货币市场操作调节流动性', 'w-en-monetary-policy'),
   ('市场冻结 → 短期融资中断、危机放大', 'w-en-credit-crunch')],
  [('流动性管理视角', '货币市场支持短期融资与流动性配置', 'w-en-money-market'),
   ('脆弱性视角', '货币市场冻结会迅速传导至整个金融体系', 'w-en-credit-crunch')],
  ['w-en-money-market', 'w-en-monetary-policy'], []),
 ('interbank-lending', '同业拆借市场', '制度',
  '银行之间按约定期限相互借贷资金的市场，多数为隔夜。',
  '同业拆借市场是银行之间按约定期限相互放贷资金的市场。多数同业贷款期限为一周或更短，其中大多数为隔夜；此类贷款按同业拆借利率成交。该市场交易量的急剧下降是（2008年）金融危机的一个主要因素。具体机制待核实。',
  [('银行为满足准备金与流动性需要 → 相互拆借', 'w-en-interbank-lending'),
   ('按同业利率成交，多为隔夜', 'w-en-interbank-lending'),
   ('信心崩塌致交易量骤降 → 系统性流动性危机', 'w-en-credit-crunch')],
  [('流动性配置视角', '同业市场高效分配短期流动性', 'w-en-interbank-lending'),
   ('对手方风险视角', '信心丧失时市场迅速冻结', 'w-en-credit-crunch')],
  ['w-en-interbank-lending', 'w-en-credit-crunch'], []),
 ('cpi', '消费者价格指数(CPI)', '制度',
  '对家庭消费所购商品与服务价格水平的统计估计，按消费篮子加权平均计算。',
  '消费者价格指数（CPI）是对家庭为消费目的所购买的商品与服务价格水平的统计估计，按一组消费商品与服务的市场篮子的加权平均价格计算。CPI 是最常用的通胀度量，也用于指数化调整。其编制方法与偏差（替代偏差等）存在讨论。具体口径待核实。',
  [('选定消费篮子并定期采集价格 → 计算加权平均', 'w-en-cpi'),
   ('与基期比较得出价格指数变动 → 通胀率', 'w-en-cpi'),
   ('用于衡量通胀、指数化与政策判断', 'w-en-inflation')],
  [('统计度量视角', 'CPI 提供标准化的消费通胀度量', 'w-en-cpi'),
   ('局限视角', '篮子固定与质量调整带来测量偏差', 'w-en-core-inflation')],
  ['w-en-cpi', 'w-en-inflation'], []),
 ('ppi', '生产者价格指数(PPI)', '制度',
  '衡量国内生产者就其产出所收到价格平均变化的指数。',
  '生产者价格指数（PPI）是衡量国内生产者就其产出所收到价格平均变化的指数。该指数在1902年至1978年间曾称为批发价格指数，由16000多家机构提供约64000个价格报价构成。PPI 常被视为消费通胀的先行指标。具体编制待核实。',
  [('采集生产者出厂价格 → 计算加权价格指数', 'w-en-ppi'),
   ('衡量生产环节价格变化', 'w-en-ppi'),
   ('成本变化向下游传导 → 影响消费通胀', 'w-en-cpi')],
  [('先行指标视角', 'PPI 变化常先于消费通胀', 'w-en-ppi'),
   ('传导视角', '传导程度取决于竞争与需求状况', 'w-en-cpi')],
  ['w-en-ppi', 'w-en-inflation'],
  [('调查机构数', 16000, '家（提供约64,000个价格报价）', 2025,
    '原文：made up of over 16,000 establishments providing approximately 64,000 price quotations；单一来源待核实。')]),
 ('pmi', '采购经理指数(PMI)', '制度',
  '由对私营部门公司的月度调查得出的经济指标。',
  '采购经理指数（PMI）是由对私营部门公司的月度调查得出的经济指标。因其发布及时、覆盖生产与新订单等环节，被视为经济活动的先行指标，常以50作为扩张与收缩的分界线（具体解读待核实）。具体编制待核实。',
  [('对采购经理开展月度调查 → 收集生产、订单、库存等信息', 'w-en-pmi'),
   ('汇总为扩散指数 → 反映扩张或收缩', 'w-en-pmi'),
   ('作为经济活动的先行指标用于判断周期', 'w-en-business-cycle')],
  [('先行指标视角', 'PMI 及时反映企业活动变化', 'w-en-pmi'),
   ('局限视角', '调查为主观判断，可能与实际产出偏离', 'w-en-cpi')],
  ['w-en-pmi', 'w-en-business-cycle'], []),
 ('kitchin-cycle', '基钦周期', '理论',
  '约40个月的短经济周期，1920年代由约瑟夫·基钦识别。',
  '基钦周期是一种约40个月的短经济周期，由约瑟夫·基钦（Joseph Kitchin）在1920年代识别。它通常与库存变动相联系（故也称库存周期），是经济周期中较短的一类。具体机制待核实。',
  [('库存调整 → 生产与订单短期波动', 'w-en-kitchin-cycle'),
   ('形成约40个月的短周期', 'w-en-kitchin-cycle'),
   ('与更长的投资周期（朱格拉）叠加', 'w-en-juglar-cycle')],
  [('库存周期视角', '短周期主要由库存调整驱动', 'w-en-kitchin-cycle'),
   ('投资周期视角', '更长周期由固定投资驱动', 'w-en-juglar-cycle')],
  ['w-en-kitchin-cycle', 'w-en-juglar-cycle'],
  [('周期长度', 40, '个月（约）', 1923,
    '原文：a short business cycle of about 40 months, identified in the 1920s by Joseph Kitchin；单一来源待核实。')]),
 ('juglar-cycle', '朱格拉周期', '理论',
  '7至11年的固定投资周期，1862年由克莱芒·朱格拉识别。',
  '朱格拉周期是1862年由克莱芒·朱格拉（Clément Juglar）识别的7至11年固定投资周期。在朱格拉周期中可以观察到固定资本投资的波动，而不只是固定资本使用水平的变化（后者是基钦周期的特征）。具体机制待核实。',
  [('企业固定资本投资波动 → 中期周期', 'w-en-juglar-cycle'),
   ('形成7—11年的周期长度', 'w-en-juglar-cycle'),
   ('与库存短周期（基钦）叠加形成复杂波动', 'w-en-kitchin-cycle')],
  [('投资周期视角', '固定投资波动驱动中期周期', 'w-en-juglar-cycle'),
   ('信用周期视角', '信贷扩张与收缩放大投资周期', 'w-en-financial-accelerator')],
  ['w-en-juglar-cycle', 'w-en-kitchin-cycle'], []),
 ('kondratiev', '康德拉季耶夫长波', '理论',
  '关于现代世界经济存在长周期现象的假说，与技术的生命周期密切相关。',
  '在经济学中，康德拉季耶夫长波是关于现代世界经济存在类周期现象的假说，该现象与技术的生命周期密切相关。长波理论认为经济存在数十年的长周期起伏，但其统计与理论依据存在争议。具体论述待核实。',
  [('重大技术集群出现 → 长期投资与增长浪潮', 'w-en-kondratiev'),
   ('技术成熟后增长放缓 → 长周期下行', 'w-en-kondratiev'),
   ('形成数十年的长波（假说，争议较大）', 'w-en-juglar-cycle')],
  [('长波视角', '技术革命驱动数十年长周期', 'w-en-kondratiev'),
   ('批判视角', '长波的统计证据与因果机制不足', 'w-en-business-cycle')],
  ['w-en-kondratiev', 'w-en-business-cycle'], []),
]

for eid, title, cat, ol, ov, causal, schools, srcs, kds in D:
    entry = {
        'id': eid, 'title': title, 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': cat,
        'one_line': ol, 'overview': ov, 'timeline': [],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in causal],
        'key_data': [{'label': k[0], 'value': k[1], 'unit': k[2], 'year': k[3],
                      'comparable_price': False, 'note': k[4], 'sources': [srcs[0]]} for k in kds],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in schools],
        'policy_response': [],
        'comparison': '经济学/金融概念条目，与其他概念互补；具体适用与争论待核实。',
        'svg': svg(title, [causal[0][0][:12], causal[1][0][:12], causal[2][0][:12]]),
        'sources': srcs, 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体数据与细节待核实。【续作T】'
    }
    json.dump(entry, open('data/entries/' + eid + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', eid)

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r38_concepts.json', encoding='utf-8'))
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
