# -*- coding: utf-8 -*-
"""续作AK：新增11条经济学派/分支概念(L2)。"""
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
 dict(id='monetarism', title='货币主义', cat='理论',
  ol='货币经济学中强调决策者控制货币流通量作用的流派。',
  ov='货币主义是货币经济学中的一个思想流派，强调决策者在控制货币流通数量方面的作用。它在1970年代获得突出地位，但（此后）大体上（影响力下降）。货币主义主张通胀本质上是货币现象、反对相机抉择的积极干预。具体论述待核实。',
  causal=[('货币供给增速过快 → 通胀上升','w-en-monetarism'),
          ('政策应设定货币增长规则 → 稳定预期','w-en-monetarism'),
          ('（实践）货币流通速度不稳 → 货币目标制效果受限','w-en-velocity-of-money')],
  schools=[('货币主义视角','通胀是货币现象，政策应遵循规则','w-en-monetarism'),
           ('凯恩斯视角','货币需求不稳定，应关注总需求与财政','w-en-keynesian-economics')],
  srcs=['w-en-monetarism','w-en-quantity-theory-money']),
 dict(id='new-keynesian', title='新凯恩斯主义', cat='理论',
  ol='致力于为凯恩斯经济学提供微观基础的宏观经济学流派。',
  ov='新凯恩斯主义经济学是一个宏观经济学流派，致力于为凯恩斯经济学提供微观经济学基础。它部分地是对（对）凯恩斯宏观经济（理论）批评的回应而发展起来的。其核心包括名义刚性与不完全竞争等微观摩擦。具体论述待核实。',
  causal=[('引入名义刚性与不完全竞争 → 为凯恩斯结论提供微观基础','w-en-new-keynesian'),
          ('价格粘性使货币政策短期有效','w-en-sticky-prices'),
          ('支持逆周期政策（有微观依据）','w-en-monetary-policy')],
  schools=[('新凯恩斯视角','微观摩擦使短期政策有效','w-en-new-keynesian'),
           ('新古典视角','市场快速出清、政策无效','w-en-new-classical')],
  srcs=['w-en-new-keynesian','w-en-sticky-prices']),
 dict(id='post-keynesian', title='后凯恩斯主义', cat='理论',
  ol='源于凯恩斯《通论》、经 Kalecki、Joan Robinson 等发展的经济学流派。',
  ov='后凯恩斯主义经济学是一个经济学思想流派，其源头是约翰·梅纳德·凯恩斯的《通论》，后续发展在很大程度上受米哈乌·卡莱茨基（Michał Kalecki）、琼·罗宾逊（Joan Robinson）等影响。该流派强调不确定性、内生货币与金融脆弱性。具体论述待核实。',
  causal=[('强调根本不确定性 → 预期无法以概率完全刻画','w-en-post-keynesian'),
          ('货币内生、投资由预期驱动','w-en-endogenous-money'),
          ('金融脆弱性内生累积 → 危机不可避免','w-en-minsky-theory')],
  schools=[('后凯恩斯视角','不确定性与金融脆弱性是核心','w-en-post-keynesian'),
           ('主流视角','以代表性主体与均衡分析为主','w-en-new-classical')],
  srcs=['w-en-post-keynesian','w-en-endogenous-money']),
 dict(id='supply-side', title='供给学派', cat='理论',
  ol='主张通过降低税收、减少管制与自由贸易最能促进增长的宏观理论。',
  ov='供给学派经济学是一种宏观经济理论，主张经济增长可以通过降低税收、减少管制与允许自由贸易而最有效地得到促进。该理论在1980年代美国政策中影响显著，其减税自偿（增收）的主张存在争议（见拉弗曲线）。具体论述待核实。',
  causal=[('降低税率与减少管制 → 提升生产与工作激励','w-en-supply-side'),
          ('供给扩张 → 增长与税基变化','w-en-supply-side'),
          ('减税未必自偿 → 财政影响存争议','w-en-laffer-curve')],
  schools=[('供给视角','减税与放松管制刺激供给','w-en-supply-side'),
           ('需求视角','应通过总需求管理稳定经济','w-en-fiscal-multiplier')],
  srcs=['w-en-supply-side','w-en-laffer-curve']),
 dict(id='institutional-economics', title='制度经济学', cat='理论',
  ol='关注演化过程与制度如何塑造经济行为的 Economics 分支。',
  ov='制度经济学关注理解演化过程的作用以及制度在塑造经济行为中的作用。其最初焦点在于托尔斯坦·凡勃伦（Thorstein Veblen）的（本能-习惯）分析。制度经济学强调产权、组织与文化对经济绩效的影响。具体论述待核实。',
  causal=[('制度（产权、规则、组织）塑造激励 → 影响行为','w-en-institutional-economics'),
          ('制度演化路径依赖 → 绩效差异持久','w-en-institutional-economics'),
          ('解释长期增长与国家间分化','w-en-great-divergence')],
  schools=[('制度视角','制度是经济绩效的根本决定因素','w-en-institutional-economics'),
           ('新古典视角','以要素与技术解释增长','w-en-solow-model')],
  srcs=['w-en-institutional-economics','w-en-great-divergence']),
 dict(id='public-choice', title='公共选择理论', cat='理论',
  ol='把经济方法（理性选择、博弈论、决策论、社会选择）应用于政治与社会的形式化理论。',
  ov='公共选择（或公共选择理论）是一种政治科学与社会科学的形式化理论，它运用经济学方法——即理性选择理论、博弈论、决策论与社会选择（理论）——来（分析政治过程）。该理论把政治家与官僚视为追求自身利益的主体。具体论述待核实。',
  causal=[('政治主体追求自身利益 → 政策未必服务公共利益','w-en-public-choice'),
          ('寻租与选举周期 → 政策扭曲','w-en-public-choice'),
          ('需规则约束财政与监管行为','w-en-fiscal-policy')],
  schools=[('公共选择视角','以自利模型分析政治与官僚','w-en-public-choice'),
           ('公共利益视角','政策旨在纠正市场失灵','w-en-welfare-economics')],
  srcs=['w-en-public-choice','w-en-welfare-economics']),
 dict(id='game-theory', title='博弈论', cat='理论',
  ol='把理性主体之间的策略互动建模为"玩家"之间"博弈"的应用数学领域。',
  ov='博弈论是应用数学的一个领域，它把理性主体之间的策略互动建模为"玩家"之间的"博弈"。它是一种描述、预测与评价（策略情形）的科学方法。博弈论为协调博弈、银行挤兑与拍卖等分析提供了工具。具体论述待核实。',
  causal=[('主体行为相互依赖 → 收益取决于他人选择','w-en-game-theory'),
          ('以博弈模型刻画策略互动 → 识别均衡','w-en-game-theory'),
          ('多重均衡解释挤兑与协调失败','w-en-coordination-games')],
  schools=[('非合作视角','以纳什均衡刻画策略稳定','w-en-game-theory'),
           ('合作/机制设计视角','设计规则以实现合意结果','w-en-public-choice')],
  srcs=['w-en-game-theory','w-en-coordination-games']),
 dict(id='new-classical', title='新古典宏观经济学', cat='理论',
  ol='基于新古典框架、强调微观基础（尤其理性预期）的宏观经济学流派。',
  ov='新古典宏观经济学是一个基于新古典框架的宏观经济学流派。它强调建立在微观经济学之上的基础，尤其是理性预期。该流派提出政策无效性命题，与凯恩斯主义形成鲜明对照。具体论述待核实。',
  causal=[('主体具有理性预期 → 系统性政策被预见','w-en-new-classical'),
          ('市场快速出清 → 政策难以影响实际变量','w-en-rational-expectations'),
          ('形成政策无效性命题','w-en-lucas-critique')],
  schools=[('新古典视角','理性预期与市场出清使政策无效','w-en-new-classical'),
           ('新凯恩斯视角','摩擦与粘性使政策短期有效','w-en-new-keynesian')],
  srcs=['w-en-new-classical','w-en-rational-expectations']),
 dict(id='development-economics', title='发展经济学', cat='理论',
  ol='研究低收入与中等收入国家发展过程经济方面的经济学分支。',
  ov='发展经济学是经济学的一个分支，处理低收入与中等收入国家发展过程中的经济方面。其关注点不仅是促进经济增长的方法，还包括（结构转型、贫困与制度）。该领域与中等收入陷阱、资源诅咒等议题密切相关。具体论述待核实。',
  causal=[('资本、技术与制度约束 → 发展受限','w-en-development-economics'),
          ('结构转型与政策选择 → 增长路径分化','w-en-middle-income-trap'),
          ('治理与外部环境 → 决定追赶成败','w-en-resource-curse')],
  schools=[('结构主义视角','强调产业政策与结构转型','w-en-development-economics'),
           ('新古典视角','强调市场、开放与制度质量','w-en-washington-consensus')],
  srcs=['w-en-development-economics','w-en-middle-income-trap']),
 dict(id='welfare-economics', title='福利经济学', cat='理论',
  ol='应用微观经济技术评估社会整体福祉的经济学领域。',
  ov='福利经济学是经济学的一个领域，它应用微观经济学技术来评估一个社会的整体福祉（福利）。该领域为成本效益分析、外部性矫正与再分配政策提供规范基础（如帕累托效率与社会福利函数）。具体论述待核实。',
  causal=[('资源配置影响个体与总体福利 → 需评估标准','w-en-welfare-economics'),
          ('市场失灵使配置偏离最优 → 政策干预有据','w-en-externality'),
          ('再分配与效率之间存在权衡','w-en-welfare-economics')],
  schools=[('帕累托视角','以无人在不损他人的情况下变得更好为标准','w-en-welfare-economics'),
           ('社会选择视角','以社会福利函数加总个体偏好','w-en-public-choice')],
  srcs=['w-en-welfare-economics','w-en-externality']),
 dict(id='political-economy', title='政治经济学', cat='理论',
  ol='政治学与经济学的交叉领域，研究政治制度与经济制度之间的关系。',
  ov='政治经济学——有时称为比较经济学——是政治科学与经济学中的一个交叉领域，研究政治制度与经济制度之间的关系。该视角强调政策选择受政治约束与利益集团影响，对理解改革与危机的政治条件至关重要。具体论述待核实。',
  causal=[('政治制度塑造政策选择 → 影响经济结果','w-en-political-economy'),
          ('利益集团与选举约束 → 改革时机与内容受限','w-en-public-choice'),
          ('政治不稳定 → 危机概率与应对能力下降','w-en-capital-flight')],
  schools=[('政治经济学视角','经济结果须置于政治制度中理解','w-en-political-economy'),
           ('纯经济视角','以市场与技术因素解释结果','w-en-development-economics')],
  srcs=['w-en-political-economy','w-en-public-choice']),
]

for sp in D:
    entry = {
        'id': sp['id'], 'title': sp['title'], 'level': 'L2', 'tier': '重要',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat'],
        'one_line': sp['ol'], 'overview': sp['ov'], 'timeline': [],
        'causal_chain': [{'step': st, 'sources': [s]} for st, s in sp['causal']],
        'key_data': [],
        'schools': [{'holder': h, 'view': v, 'basis': '据来源/标准口径归纳；具体表述待核实', 'sources': [s]}
                    for h, v, s in sp['schools']],
        'policy_response': [],
        'comparison': '经济学流派/分支概念，与其他理论与概念互补；具体争论待核实。',
        'svg': svg(sp['title'], [sp['causal'][0][0][:12], sp['causal'][1][0][:12], sp['causal'][2][0][:12]]),
        'sources': list(dict.fromkeys(sp['srcs'])), 'related': [], 'needs_verification': True,
        'pending_notes': '概念条目：定义/机理据维基摘要与标准口径；具体细节待核实。【续作AK】'
    }
    json.dump(entry, open('data/entries/' + sp['id'] + '.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('新增', sp['id'])

sd = json.load(open('data/sources.json', encoding='utf-8'))
ex = {x['id'] for x in sd['sources']}
meta = json.load(open('_research/r56_schools.json', encoding='utf-8'))
for eid, v in meta.items():
    if eid == 'behavioral-econ':
        continue
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
for sp in D:
    if sp['id'] in have:
        continue
    cov['entries'].append({
        'id': sp['id'], 'level': 'L2', 'tier': '重要', 'status': 'written',
        'source_count': len(sp['srcs']), 'needs_verification': 1, 'last_updated': '2026-11-23',
        'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': sp['cat']})
cov['total'] = len(cov['entries'])
json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total', cov['total'])
