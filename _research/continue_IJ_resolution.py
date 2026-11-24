# -*- coding: utf-8 -*-
"""续作IJ：用 FSB 一手文献新建 bank-resolution（银行处置）。

这是"以国际机构一手文献为专属来源建条目"的首个完整案例——
此概念此前因维基只有通用页（Bank regulation and supervision）而被判定为缺口。
"""
import glob
import json

EID = 'bank-resolution'
es = [json.load(open(f, encoding='utf-8')) for f in glob.glob('data/entries/*.json')]
ids = {e['id'] for e in es}
titles = {e['title'] for e in es}
if EID in ids or '银行处置' in titles:
    print('已存在，跳过')
    raise SystemExit

SID = 'org-fsb-key-attributes'
sp = 'data/sources.json'
sj = json.load(open(sp, encoding='utf-8'))
if SID not in {s['id'] for s in sj['sources']}:
    sj['sources'].append({
        'id': SID,
        'title': 'Key Attributes of Effective Resolution Regimes for Financial Institutions',
        'author': 'Financial Stability Board (FSB)',
        'year': '2014',
        'type': '权威机构',
        'url': 'https://www.fsb.org/2014/10/r_141015/',
        'url2': None,
        'verified': True,
        'link_ok': True,
        'note': 'FSB 处置制度核心标准；2011年10月发布十二项关键属性，2014年版本增补附件（正文未改）',
    })
    sj['count'] = len(sj['sources'])
    json.dump(sj, open(sp, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
    print('注册来源:', SID)

D = {
 'id': EID, 'title': '银行处置', 'level': 'L2', 'tier': '重要',
 'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球', 'crisis_type': '制度',
 'one_line': '对有系统性风险的金融机构进行有序重组或清算的制度安排，使其退出而不引发系统性传染。',
 'overview': (
   '银行处置(resolution) 指监管当局对**陷入困境、且可能具有系统重要性**的金融机构'
   '进行有序重组或清算的制度安排。其目标是把机构"**平稳送走**"——'
   '让股东与债权人承担损失、维持关键业务不中断、并把系统性传染控制在可承受范围。'
   '这与"救助"截然不同：救助用公共资金维持机构存续，处置则让机构退出但**不制造混乱**。'
   '**国际标准**由金融稳定理事会(FSB)制定：'
   '**2011 年 10 月**发布《金融机构有效处置制度的关键属性》(Key Attributes)，'
   '含**十二项**关键属性，定位为覆盖"所有类型、可能在失败时具系统重要性"的金融机构的'
   '**总括标准(umbrella standard)**；**2014 年**版本增补附件，但十二项关键属性正文未改。'
   '**核心工具**（依通行理解，具体条文待核对原文）包括：'
   '**自救(bail-in)**——把债权转为股权以吸收损失；**过桥机构**——把好资产与关键业务'
   '临时转移出去；**资产分离**——把不良资产剥离到坏账银行；'
   '以及**临时接管**与**强制清算**。'
   '**难点**在于跨境协调：一家跨国银行在不同法域受不同处置制度约束，'
   '而处置决定几乎总是在极短时间内作出。'),
 'timeline': [
   {'year': 2011, 'event': 'FSB 发布《金融机构有效处置制度的关键属性》，确立十二项关键属性'
                           '（据 FSB Key Attributes）'},
   {'year': 2014, 'event': 'FSB 修订版本增补附件，十二项关键属性正文未改动'
                           '（据 FSB Key Attributes）'},
   {'year': 2023, 'event': '2023 年美国区域银行危机中，FDIC 以过桥银行方式处置'
                           '硅谷银行与 Signature 银行（本库见 bank-crisis-2023）'},
 ],
 'schools': [
   {'holder': '可信处置视角（FSB 标准）',
    'view': '关键前提是**可信性**：若市场相信大型机构终将获救，处置框架就无效；'
            '因此需要事先备好自救债券、处置资金与跨境协调安排'
            '（据 FSB Key Attributes）',
    'sources': [SID]},
   {'holder': '可行性质疑',
    'view': '批评者指出大型银行的组织复杂性与跨境业务使"有序处置"在实践中难以执行；'
            '一旦真的动手，当局往往因系统性风险而回归救助'
            '（本库据通行讨论归纳；具体批评出处待核实）',
    'sources': [SID]},
 ],
 'key_data': [
   {'label': 'FSB 关键属性的项数', 'value': 12, 'unit': '项', 'year': 2011,
    'comparable_price': False,
    'note': '原文：the twelve Key Attributes of October 2011；单一机构来源，待第二来源核实。',
    'sources': [SID]},
 ],
 'comparison': (
   '与**救助(bailout)** 的区别：救助用公共资金维持机构存续、保住股东与债权人；'
   '处置让机构退出、由股东与债权人承担损失（如通过 bail-in）。'
   '与**破产清算**的区别：普通破产程序以债权人受偿最大化为目标，'
   '处置还要兼顾**金融稳定**与**关键业务连续性**，因此可动用行政权力（临时接管、强制转移资产）。'
   '与**存款保险**的区别：后者保护小额存款人，前者处理机构本身的存续与退出。'),
 'related': [r for r in ('bail-in', 'bad-bank', 'too-big-to-fail', 'bank-failure',
                         'deposit-insurance', 'bank-crisis-2023', 'lender-of-last-resort')
             if r in ids],
 'sources': [SID],
 'needs_verification': True,
 'pending_notes': '【续作IJ】以 FSB 一手文献为专属来源新建（此前因维基仅通用页被判为缺口）；'
                  '十二项关键属性的具体条文、各国处置制度差异待核对原文。',
}

json.dump(D, open('data/entries/%s.json' % EID, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('新建:', EID)

cov = json.load(open('coverage.json', encoding='utf-8'))
if EID not in {e['id'] for e in cov['entries']}:
    cov['entries'].append({'id': EID, 'level': 'L2', 'tier': '重要', 'status': 'written',
                           'source_count': 1, 'needs_verification': 1, 'last_updated': '2026-11-24',
                           'unit': 'U6 理论与制度', 'period': '理论制度', 'region': '全球',
                           'crisis_type': '制度'})
    cov['total'] = len(cov['entries'])
    json.dump(cov, open('coverage.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
print('coverage total:', cov['total'])
